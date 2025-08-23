"""
Fault Detection and Isolation System for DAL-A Software Subsystem
=================================================================

Implements comprehensive fault detection, isolation, and recovery mechanisms
for safety-critical systems with Built-In Test (BIT) capabilities.

DO-178C Objectives:
- A-10: Software integration test procedures are correct and complete
- A-11: Software integration test results are correct and complete

Safety Requirements:
- SRS-FD-001: Continuous health monitoring of all critical components
- SRS-FD-002: Fault detection within 100ms of occurrence
- SRS-FD-003: Automatic fault isolation and containment
- SRS-FD-004: Fault recovery and graceful degradation
"""

import time
import threading
import logging
from typing import Dict, List, Optional, Callable, Any, Set
from dataclasses import dataclass, field
from enum import Enum
import statistics
import queue


class FaultSeverity(Enum):
    """Fault severity levels aligned with DAL classifications"""
    CATASTROPHIC = 1    # DAL-A: System failure could cause catastrophic event
    HAZARDOUS = 2      # DAL-B: System failure could cause hazardous event
    MAJOR = 3          # DAL-C: System failure could cause major event
    MINOR = 4          # DAL-D: System failure could cause minor event
    NO_EFFECT = 5      # DAL-E: System failure has no effect on safety


class FaultType(Enum):
    """Types of faults that can be detected"""
    HARDWARE_FAULT = "HARDWARE_FAULT"
    SOFTWARE_FAULT = "SOFTWARE_FAULT"
    TIMING_FAULT = "TIMING_FAULT"
    COMMUNICATION_FAULT = "COMMUNICATION_FAULT"
    PERFORMANCE_FAULT = "PERFORMANCE_FAULT"
    SECURITY_FAULT = "SECURITY_FAULT"
    DATA_CORRUPTION = "DATA_CORRUPTION"
    RESOURCE_EXHAUSTION = "RESOURCE_EXHAUSTION"


class ComponentState(Enum):
    """Component operational states"""
    OPERATIONAL = "OPERATIONAL"
    DEGRADED = "DEGRADED"
    FAILED = "FAILED"
    ISOLATED = "ISOLATED"
    RECOVERY = "RECOVERY"
    OFFLINE = "OFFLINE"


@dataclass
class FaultEvent:
    """Represents a detected fault event"""
    timestamp: float
    component_id: str
    fault_type: FaultType
    severity: FaultSeverity
    description: str
    fault_data: Dict = field(default_factory=dict)
    resolved: bool = False
    resolution_time: Optional[float] = None
    
    def __post_init__(self):
        if self.timestamp <= 0:
            self.timestamp = time.time()


@dataclass
class ComponentMonitor:
    """Monitoring configuration for a system component"""
    component_id: str
    health_check_function: Callable[[], Dict]
    check_interval_ms: float
    fault_threshold: Dict[str, float]
    recovery_function: Optional[Callable[[], bool]] = None
    isolation_function: Optional[Callable[[], bool]] = None
    
    # Runtime state
    state: ComponentState = ComponentState.OPERATIONAL
    last_check_time: float = 0.0
    fault_count: int = 0
    last_health_data: Dict = field(default_factory=dict)
    consecutive_failures: int = 0


class FaultDetector:
    """
    Comprehensive Fault Detection and Isolation System
    
    Provides continuous monitoring, fault detection, isolation, and recovery
    for safety-critical system components.
    """
    
    def __init__(self, detection_rate_hz: float = 10.0):
        """
        Initialize fault detection system
        
        Args:
            detection_rate_hz: Fault detection update rate in Hz
        """
        self.detection_rate_hz = detection_rate_hz
        self.detection_period_ms = 1000.0 / detection_rate_hz
        
        self.monitors: Dict[str, ComponentMonitor] = {}
        self.fault_history: List[FaultEvent] = []
        self.active_faults: Dict[str, FaultEvent] = {}
        
        # System state
        self.detector_active = False
        self.system_health_score = 100.0
        self.total_components = 0
        self.operational_components = 0
        
        # Performance metrics
        self.detection_cycles = 0
        self.total_faults_detected = 0
        self.faults_resolved = 0
        self.avg_detection_time_ms = 0.0
        
        # Fault event queue for processing
        self.fault_queue = queue.Queue()
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
    def register_component(self, monitor_config: ComponentMonitor) -> bool:
        """
        Register a component for fault monitoring
        
        Args:
            monitor_config: Component monitoring configuration
            
        Returns:
            bool: True if component registered successfully
            
        Implements: SRS-FD-001 (Continuous health monitoring)
        """
        try:
            if monitor_config.component_id in self.monitors:
                self.logger.warning(f"Component {monitor_config.component_id} already registered")
                return False
            
            # Validate configuration
            if monitor_config.check_interval_ms <= 0:
                raise ValueError("Check interval must be positive")
            
            self.monitors[monitor_config.component_id] = monitor_config
            self.total_components += 1
            self.operational_components += 1
            
            self.logger.info(f"Registered component for monitoring: {monitor_config.component_id}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to register component {monitor_config.component_id}: {e}")
            return False
    
    def start_detection(self) -> None:
        """
        Start the fault detection system
        
        Implements: SRS-FD-002 (Fault detection within 100ms)
        """
        if self.detector_active:
            self.logger.warning("Fault detector already active")
            return
        
        self.detector_active = True
        self.logger.info("Starting fault detection system")
        
        def detection_loop():
            last_cycle = time.time()
            
            while self.detector_active:
                cycle_start = time.time()
                
                # Check all registered components
                for component_id, monitor in self.monitors.items():
                    if not self.detector_active:
                        break
                    
                    # Check if it's time for this component's health check
                    if (cycle_start - monitor.last_check_time) * 1000 >= monitor.check_interval_ms:
                        self._check_component_health(monitor, cycle_start)
                
                # Process fault events
                self._process_fault_events()
                
                # Update system health
                self._update_system_health()
                
                # Enforce detection rate
                cycle_time = time.time() - cycle_start
                sleep_time = max(0, (self.detection_period_ms / 1000.0) - cycle_time)
                if sleep_time > 0:
                    time.sleep(sleep_time)
                
                self.detection_cycles += 1
        
        # Start detection thread
        self.detection_thread = threading.Thread(target=detection_loop, daemon=True)
        self.detection_thread.start()
        
        # Start fault processing thread
        self.processing_thread = threading.Thread(target=self._fault_processing_loop, daemon=True)
        self.processing_thread.start()
    
    def stop_detection(self) -> None:
        """Stop the fault detection system"""
        self.detector_active = False
        self.logger.info("Stopping fault detection system")
        
        if hasattr(self, 'detection_thread'):
            self.detection_thread.join(timeout=1.0)
        if hasattr(self, 'processing_thread'):
            self.processing_thread.join(timeout=1.0)
    
    def _check_component_health(self, monitor: ComponentMonitor, check_time: float) -> None:
        """
        Perform health check on a component
        
        Implements: SRS-FD-002 (Fault detection timing)
        """
        try:
            monitor.last_check_time = check_time
            
            # Execute health check function
            health_data = monitor.health_check_function()
            monitor.last_health_data = health_data
            
            # Analyze health data for faults
            fault_detected = self._analyze_health_data(monitor, health_data)
            
            if fault_detected:
                monitor.consecutive_failures += 1
                monitor.fault_count += 1
            else:
                monitor.consecutive_failures = 0
                
                # Recovery check for previously failed components
                if monitor.state in [ComponentState.FAILED, ComponentState.DEGRADED]:
                    self._attempt_component_recovery(monitor)
            
        except Exception as e:
            self.logger.error(f"Health check failed for {monitor.component_id}: {e}")
            self._create_fault_event(
                monitor.component_id,
                FaultType.SOFTWARE_FAULT,
                FaultSeverity.MAJOR,
                f"Health check exception: {e}",
                {"exception": str(e)}
            )
    
    def _analyze_health_data(self, monitor: ComponentMonitor, health_data: Dict) -> bool:
        """
        Analyze component health data for fault conditions
        
        Returns:
            bool: True if fault detected
        """
        fault_detected = False
        
        for metric, threshold in monitor.fault_threshold.items():
            if metric in health_data:
                value = health_data[metric]
                
                # Check threshold violations
                if isinstance(value, (int, float)):
                    if value > threshold:
                        fault_detected = True
                        self._create_fault_event(
                            monitor.component_id,
                            FaultType.PERFORMANCE_FAULT,
                            self._determine_fault_severity(monitor.component_id, metric, value),
                            f"Metric {metric} exceeded threshold: {value} > {threshold}",
                            {"metric": metric, "value": value, "threshold": threshold}
                        )
                elif isinstance(value, bool) and not value:
                    # Boolean health indicators
                    fault_detected = True
                    self._create_fault_event(
                        monitor.component_id,
                        FaultType.HARDWARE_FAULT,
                        FaultSeverity.MAJOR,
                        f"Health indicator {metric} failed",
                        {"metric": metric, "value": value}
                    )
        
        return fault_detected
    
    def _create_fault_event(self, component_id: str, fault_type: FaultType, 
                          severity: FaultSeverity, description: str, fault_data: Dict) -> None:
        """
        Create and queue a fault event for processing
        
        Implements: SRS-FD-002 (Fault detection timing)
        """
        fault_event = FaultEvent(
            timestamp=time.time(),
            component_id=component_id,
            fault_type=fault_type,
            severity=severity,
            description=description,
            fault_data=fault_data
        )
        
        self.fault_queue.put(fault_event)
        self.total_faults_detected += 1
        
        # Log based on severity
        if severity in [FaultSeverity.CATASTROPHIC, FaultSeverity.HAZARDOUS]:
            self.logger.critical(f"Critical fault detected: {component_id} - {description}")
        elif severity == FaultSeverity.MAJOR:
            self.logger.error(f"Major fault detected: {component_id} - {description}")
        else:
            self.logger.warning(f"Minor fault detected: {component_id} - {description}")
    
    def _fault_processing_loop(self) -> None:
        """Process fault events from the queue"""
        while self.detector_active:
            try:
                # Wait for fault events with timeout
                fault_event = self.fault_queue.get(timeout=1.0)
                
                # Add to history
                self.fault_history.append(fault_event)
                self.active_faults[fault_event.component_id] = fault_event
                
                # Process the fault
                self._process_fault(fault_event)
                
            except queue.Empty:
                continue
            except Exception as e:
                self.logger.error(f"Error processing fault event: {e}")
    
    def _process_fault(self, fault_event: FaultEvent) -> None:
        """
        Process a detected fault event
        
        Implements: SRS-FD-003 (Fault isolation) and SRS-FD-004 (Recovery)
        """
        component_id = fault_event.component_id
        monitor = self.monitors.get(component_id)
        
        if not monitor:
            self.logger.error(f"No monitor found for component {component_id}")
            return
        
        # Update component state based on fault severity
        if fault_event.severity == FaultSeverity.CATASTROPHIC:
            monitor.state = ComponentState.FAILED
            self._isolate_component(monitor)
        elif fault_event.severity == FaultSeverity.HAZARDOUS:
            monitor.state = ComponentState.FAILED
            self._isolate_component(monitor)
        elif fault_event.severity == FaultSeverity.MAJOR:
            monitor.state = ComponentState.DEGRADED
        else:
            # Minor faults don't change operational state immediately
            pass
        
        # Update operational count
        self._update_operational_count()
        
        # Log fault processing
        self.logger.info(f"Processed fault for {component_id}: "
                        f"State={monitor.state.value}, Severity={fault_event.severity.name}")
    
    def _isolate_component(self, monitor: ComponentMonitor) -> None:
        """
        Isolate a failed component
        
        Implements: SRS-FD-003 (Fault isolation)
        """
        try:
            if monitor.isolation_function:
                success = monitor.isolation_function()
                if success:
                    monitor.state = ComponentState.ISOLATED
                    self.logger.info(f"Successfully isolated component {monitor.component_id}")
                else:
                    self.logger.error(f"Failed to isolate component {monitor.component_id}")
            else:
                self.logger.warning(f"No isolation function for component {monitor.component_id}")
                
        except Exception as e:
            self.logger.error(f"Exception during isolation of {monitor.component_id}: {e}")
    
    def _attempt_component_recovery(self, monitor: ComponentMonitor) -> None:
        """
        Attempt to recover a failed component
        
        Implements: SRS-FD-004 (Fault recovery)
        """
        try:
            if monitor.recovery_function:
                monitor.state = ComponentState.RECOVERY
                success = monitor.recovery_function()
                
                if success:
                    monitor.state = ComponentState.OPERATIONAL
                    monitor.fault_count = 0
                    monitor.consecutive_failures = 0
                    
                    # Mark active fault as resolved
                    if monitor.component_id in self.active_faults:
                        fault = self.active_faults[monitor.component_id]
                        fault.resolved = True
                        fault.resolution_time = time.time()
                        del self.active_faults[monitor.component_id]
                        self.faults_resolved += 1
                    
                    self.logger.info(f"Successfully recovered component {monitor.component_id}")
                else:
                    monitor.state = ComponentState.FAILED
                    self.logger.error(f"Failed to recover component {monitor.component_id}")
            
        except Exception as e:
            monitor.state = ComponentState.FAILED
            self.logger.error(f"Exception during recovery of {monitor.component_id}: {e}")
    
    def _determine_fault_severity(self, component_id: str, metric: str, value: float) -> FaultSeverity:
        """Determine fault severity based on component and metric"""
        # This would be configured based on system safety analysis
        # For now, using simple heuristics
        
        if "critical" in component_id.lower() or "safety" in component_id.lower():
            return FaultSeverity.CATASTROPHIC
        elif "power" in metric.lower() or "temperature" in metric.lower():
            return FaultSeverity.HAZARDOUS
        elif "performance" in metric.lower() or "latency" in metric.lower():
            return FaultSeverity.MAJOR
        else:
            return FaultSeverity.MINOR
    
    def _update_operational_count(self) -> None:
        """Update count of operational components"""
        self.operational_components = sum(
            1 for monitor in self.monitors.values()
            if monitor.state == ComponentState.OPERATIONAL
        )
    
    def _update_system_health(self) -> None:
        """Update overall system health score"""
        if self.total_components == 0:
            self.system_health_score = 100.0
            return
        
        operational_score = (self.operational_components / self.total_components) * 100
        degraded_components = sum(
            1 for monitor in self.monitors.values()
            if monitor.state == ComponentState.DEGRADED
        )
        degraded_score = (degraded_components / self.total_components) * 50
        
        self.system_health_score = operational_score + degraded_score
    
    def get_system_status(self) -> Dict:
        """
        Get comprehensive system fault detection status
        
        Returns:
            Dict containing fault detection metrics and component status
        """
        return {
            "timestamp": time.time(),
            "detector_active": self.detector_active,
            "system_health_score": self.system_health_score,
            "total_components": self.total_components,
            "operational_components": self.operational_components,
            "degraded_components": sum(1 for m in self.monitors.values() if m.state == ComponentState.DEGRADED),
            "failed_components": sum(1 for m in self.monitors.values() if m.state == ComponentState.FAILED),
            "isolated_components": sum(1 for m in self.monitors.values() if m.state == ComponentState.ISOLATED),
            "active_faults": len(self.active_faults),
            "total_faults_detected": self.total_faults_detected,
            "faults_resolved": self.faults_resolved,
            "detection_cycles": self.detection_cycles,
            "components": {
                comp_id: {
                    "state": monitor.state.value,
                    "fault_count": monitor.fault_count,
                    "consecutive_failures": monitor.consecutive_failures,
                    "last_check_time": monitor.last_check_time,
                    "health_data": monitor.last_health_data
                } for comp_id, monitor in self.monitors.items()
            },
            "recent_faults": [
                {
                    "timestamp": fault.timestamp,
                    "component_id": fault.component_id,
                    "fault_type": fault.fault_type.value,
                    "severity": fault.severity.name,
                    "description": fault.description,
                    "resolved": fault.resolved
                } for fault in self.fault_history[-10:]  # Last 10 faults
            ]
        }
    
    def get_component_status(self, component_id: str) -> Optional[Dict]:
        """Get detailed status for a specific component"""
        if component_id not in self.monitors:
            return None
        
        monitor = self.monitors[component_id]
        component_faults = [f for f in self.fault_history if f.component_id == component_id]
        
        return {
            "component_id": component_id,
            "state": monitor.state.value,
            "fault_count": monitor.fault_count,
            "consecutive_failures": monitor.consecutive_failures,
            "last_check_time": monitor.last_check_time,
            "check_interval_ms": monitor.check_interval_ms,
            "health_data": monitor.last_health_data,
            "fault_thresholds": monitor.fault_threshold,
            "has_recovery_function": monitor.recovery_function is not None,
            "has_isolation_function": monitor.isolation_function is not None,
            "fault_history": [
                {
                    "timestamp": fault.timestamp,
                    "fault_type": fault.fault_type.value,
                    "severity": fault.severity.name,
                    "description": fault.description,
                    "resolved": fault.resolved
                } for fault in component_faults[-5:]  # Last 5 faults for this component
            ]
        }
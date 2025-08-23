"""
Cyber Threat Monitor for DAL-A Software Subsystem
=================================================

Implements comprehensive cyber threat detection and mitigation for safety-critical
aerospace systems. Provides real-time monitoring and automated response to cyber attacks.

DO-178C Objectives:
- A-13: Software integration tests are complete and correct

Security Requirements:
- SRS-TM-001: Real-time detection of cyber threats and anomalies
- SRS-TM-002: Automated threat response and mitigation
- SRS-TM-003: Threat intelligence integration and analysis
- SRS-TM-004: Incident response and forensic logging
"""

import time
import threading
import logging
import hashlib
import statistics
from typing import Dict, List, Optional, Set, Callable, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum
import queue
import json
import re
from collections import defaultdict, deque


class ThreatLevel(Enum):
    """Threat severity levels"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4
    CATASTROPHIC = 5


class ThreatType(Enum):
    """Types of cyber threats"""
    INTRUSION_ATTEMPT = "INTRUSION_ATTEMPT"
    MALWARE_DETECTED = "MALWARE_DETECTED"
    DATA_EXFILTRATION = "DATA_EXFILTRATION"
    DENIAL_OF_SERVICE = "DENIAL_OF_SERVICE"
    PRIVILEGE_ESCALATION = "PRIVILEGE_ESCALATION"
    UNAUTHORIZED_ACCESS = "UNAUTHORIZED_ACCESS"
    ANOMALOUS_BEHAVIOR = "ANOMALOUS_BEHAVIOR"
    COMMUNICATION_HIJACK = "COMMUNICATION_HIJACK"
    TIMING_ATTACK = "TIMING_ATTACK"
    SIDE_CHANNEL_ATTACK = "SIDE_CHANNEL_ATTACK"


class ResponseAction(Enum):
    """Automated response actions"""
    MONITOR = "MONITOR"
    ALERT = "ALERT"
    BLOCK = "BLOCK"
    ISOLATE = "ISOLATE"
    TERMINATE = "TERMINATE"
    FAILSAFE = "FAILSAFE"


@dataclass
class ThreatEvent:
    """Represents a detected threat event"""
    event_id: str
    timestamp: float
    threat_type: ThreatType
    threat_level: ThreatLevel
    source_component: str
    description: str
    indicators: Dict[str, Any] = field(default_factory=dict)
    mitigated: bool = False
    mitigation_actions: List[ResponseAction] = field(default_factory=list)
    
    def __post_init__(self):
        if self.timestamp <= 0:
            self.timestamp = time.time()
        if not self.event_id:
            self.event_id = hashlib.sha256(
                f"{self.source_component}:{self.threat_type.value}:{self.timestamp}".encode()
            ).hexdigest()[:16]


@dataclass
class ThreatPattern:
    """Pattern definition for threat detection"""
    pattern_id: str
    pattern_name: str
    threat_type: ThreatType
    detection_rules: List[Dict[str, Any]]
    threshold_values: Dict[str, float]
    response_actions: List[ResponseAction]
    enabled: bool = True


@dataclass
class SystemMetrics:
    """System metrics for anomaly detection"""
    timestamp: float
    cpu_usage: float
    memory_usage: float
    network_in_bps: float
    network_out_bps: float
    disk_io_rate: float
    active_connections: int
    failed_authentications: int
    
    def to_dict(self) -> Dict[str, float]:
        """Convert to dictionary for analysis"""
        return {
            "cpu_usage": self.cpu_usage,
            "memory_usage": self.memory_usage,
            "network_in_bps": self.network_in_bps,
            "network_out_bps": self.network_out_bps,
            "disk_io_rate": self.disk_io_rate,
            "active_connections": float(self.active_connections),
            "failed_authentications": float(self.failed_authentications)
        }


class ThreatMonitor:
    """
    Comprehensive Cyber Threat Monitoring System
    
    Provides real-time threat detection, analysis, and automated response
    for safety-critical aerospace systems.
    """
    
    def __init__(self, detection_interval_ms: float = 100.0):
        """
        Initialize threat monitor
        
        Args:
            detection_interval_ms: Threat detection update interval in milliseconds
        """
        self.detection_interval_ms = detection_interval_ms
        
        # Threat detection components
        self.threat_patterns: Dict[str, ThreatPattern] = {}
        self.active_threats: Dict[str, ThreatEvent] = {}
        self.threat_history: List[ThreatEvent] = []
        
        # Monitoring state
        self.monitor_active = False
        self.metrics_queue = queue.Queue()
        self.alert_queue = queue.Queue()
        
        # Anomaly detection
        self.baseline_metrics: Dict[str, deque] = defaultdict(lambda: deque(maxlen=1000))
        self.anomaly_thresholds: Dict[str, float] = {}
        self.learning_mode = True
        self.learning_samples = 0
        self.min_learning_samples = 100
        
        # Performance metrics
        self.total_events_processed = 0
        self.threats_detected = 0
        self.threats_mitigated = 0
        self.false_positives = 0
        
        # Response mechanisms
        self.response_handlers: Dict[ResponseAction, Callable] = {}
        self.automatic_response_enabled = True
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Initialize default threat patterns
        self._initialize_default_patterns()
    
    def add_threat_pattern(self, pattern: ThreatPattern) -> bool:
        """
        Add a threat detection pattern
        
        Args:
            pattern: Threat pattern configuration
            
        Returns:
            bool: True if pattern added successfully
            
        Implements: SRS-TM-001 (Threat detection)
        """
        try:
            if pattern.pattern_id in self.threat_patterns:
                self.logger.warning(f"Threat pattern {pattern.pattern_id} already exists")
                return False
            
            self.threat_patterns[pattern.pattern_id] = pattern
            
            self.logger.info(f"Added threat pattern: {pattern.pattern_name} "
                           f"({pattern.threat_type.value})")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to add threat pattern {pattern.pattern_id}: {e}")
            return False
    
    def register_response_handler(self, action: ResponseAction, handler: Callable) -> None:
        """
        Register a response handler for automated threat mitigation
        
        Implements: SRS-TM-002 (Automated response)
        """
        self.response_handlers[action] = handler
        self.logger.info(f"Registered response handler for {action.value}")
    
    def process_metrics(self, metrics: SystemMetrics) -> List[ThreatEvent]:
        """
        Process system metrics and detect threats
        
        Args:
            metrics: Current system metrics
            
        Returns:
            List[ThreatEvent]: Detected threats
            
        Implements: SRS-TM-001 (Real-time detection)
        """
        detected_threats = []
        
        try:
            self.total_events_processed += 1
            
            # Update baseline for anomaly detection
            self._update_baseline(metrics)
            
            # Check each threat pattern
            for pattern_id, pattern in self.threat_patterns.items():
                if not pattern.enabled:
                    continue
                
                # Apply detection rules
                if self._evaluate_threat_pattern(pattern, metrics):
                    threat_event = ThreatEvent(
                        event_id="",  # Will be generated
                        timestamp=metrics.timestamp,
                        threat_type=pattern.threat_type,
                        threat_level=self._calculate_threat_level(pattern, metrics),
                        source_component="system_monitor",
                        description=f"Threat pattern '{pattern.pattern_name}' triggered",
                        indicators=self._extract_threat_indicators(pattern, metrics)
                    )
                    
                    detected_threats.append(threat_event)
                    self._process_threat_event(threat_event)
            
            # Anomaly detection
            if not self.learning_mode:
                anomaly_threats = self._detect_anomalies(metrics)
                detected_threats.extend(anomaly_threats)
                for threat in anomaly_threats:
                    self._process_threat_event(threat)
            
            return detected_threats
            
        except Exception as e:
            self.logger.error(f"Error processing metrics: {e}")
            return []
    
    def start_monitoring(self, metrics_provider: Callable[[], SystemMetrics]) -> None:
        """
        Start the threat monitoring system
        
        Args:
            metrics_provider: Function that provides current system metrics
            
        Implements: SRS-TM-001 (Real-time monitoring)
        """
        if self.monitor_active:
            self.logger.warning("Threat monitor already active")
            return
        
        self.monitor_active = True
        self.logger.info("Starting cyber threat monitor")
        
        def monitoring_loop():
            last_detection = time.time()
            
            while self.monitor_active:
                try:
                    current_time = time.time()
                    
                    # Get current metrics
                    metrics = metrics_provider()
                    
                    # Process metrics for threats
                    threats = self.process_metrics(metrics)
                    
                    # Queue any detected threats
                    for threat in threats:
                        self.alert_queue.put(threat)
                    
                    # Enforce detection interval
                    elapsed_ms = (time.time() - current_time) * 1000
                    sleep_time = max(0, (self.detection_interval_ms - elapsed_ms) / 1000)
                    if sleep_time > 0:
                        time.sleep(sleep_time)
                    
                except Exception as e:
                    self.logger.error(f"Error in monitoring loop: {e}")
                    time.sleep(0.1)  # Prevent tight error loop
        
        def alert_processing_loop():
            while self.monitor_active:
                try:
                    # Wait for threat alerts
                    threat = self.alert_queue.get(timeout=1.0)
                    
                    # Process the threat alert
                    self._handle_threat_alert(threat)
                    
                except queue.Empty:
                    continue
                except Exception as e:
                    self.logger.error(f"Error processing threat alert: {e}")
        
        # Start monitoring threads
        self.monitoring_thread = threading.Thread(target=monitoring_loop, daemon=True)
        self.alert_thread = threading.Thread(target=alert_processing_loop, daemon=True)
        
        self.monitoring_thread.start()
        self.alert_thread.start()
    
    def stop_monitoring(self) -> None:
        """Stop the threat monitoring system"""
        self.monitor_active = False
        self.logger.info("Stopping cyber threat monitor")
        
        if hasattr(self, 'monitoring_thread'):
            self.monitoring_thread.join(timeout=1.0)
        if hasattr(self, 'alert_thread'):
            self.alert_thread.join(timeout=1.0)
    
    def _initialize_default_patterns(self) -> None:
        """Initialize default threat detection patterns"""
        
        # DOS attack pattern
        dos_pattern = ThreatPattern(
            pattern_id="dos_attack",
            pattern_name="Denial of Service Attack",
            threat_type=ThreatType.DENIAL_OF_SERVICE,
            detection_rules=[
                {"metric": "network_in_bps", "operator": ">", "threshold": 100_000_000},  # 100 Mbps
                {"metric": "active_connections", "operator": ">", "threshold": 1000}
            ],
            threshold_values={"sustained_duration": 5.0},  # 5 seconds
            response_actions=[ResponseAction.BLOCK, ResponseAction.ALERT]
        )
        
        # Intrusion attempt pattern
        intrusion_pattern = ThreatPattern(
            pattern_id="intrusion_attempt",
            pattern_name="Intrusion Attempt",
            threat_type=ThreatType.INTRUSION_ATTEMPT,
            detection_rules=[
                {"metric": "failed_authentications", "operator": ">", "threshold": 10}
            ],
            threshold_values={"time_window": 60.0},  # 1 minute
            response_actions=[ResponseAction.BLOCK, ResponseAction.ALERT]
        )
        
        # Resource exhaustion pattern
        resource_exhaustion_pattern = ThreatPattern(
            pattern_id="resource_exhaustion",
            pattern_name="Resource Exhaustion Attack",
            threat_type=ThreatType.DENIAL_OF_SERVICE,
            detection_rules=[
                {"metric": "cpu_usage", "operator": ">", "threshold": 95.0},
                {"metric": "memory_usage", "operator": ">", "threshold": 90.0}
            ],
            threshold_values={"sustained_duration": 10.0},  # 10 seconds
            response_actions=[ResponseAction.ALERT, ResponseAction.ISOLATE]
        )
        
        # Add patterns
        self.add_threat_pattern(dos_pattern)
        self.add_threat_pattern(intrusion_pattern)
        self.add_threat_pattern(resource_exhaustion_pattern)
    
    def _evaluate_threat_pattern(self, pattern: ThreatPattern, metrics: SystemMetrics) -> bool:
        """Evaluate if a threat pattern matches current metrics"""
        metrics_dict = metrics.to_dict()
        
        # Check all detection rules
        for rule in pattern.detection_rules:
            metric_name = rule["metric"]
            operator = rule["operator"]
            threshold = rule["threshold"]
            
            if metric_name not in metrics_dict:
                continue
            
            value = metrics_dict[metric_name]
            
            # Apply operator
            if operator == ">" and value <= threshold:
                return False
            elif operator == "<" and value >= threshold:
                return False
            elif operator == "==" and value != threshold:
                return False
            elif operator == "!=" and value == threshold:
                return False
        
        return True
    
    def _calculate_threat_level(self, pattern: ThreatPattern, metrics: SystemMetrics) -> ThreatLevel:
        """Calculate threat level based on pattern and metrics"""
        
        # Base threat level based on type
        base_levels = {
            ThreatType.DENIAL_OF_SERVICE: ThreatLevel.HIGH,
            ThreatType.INTRUSION_ATTEMPT: ThreatLevel.MEDIUM,
            ThreatType.MALWARE_DETECTED: ThreatLevel.CRITICAL,
            ThreatType.DATA_EXFILTRATION: ThreatLevel.CATASTROPHIC,
            ThreatType.UNAUTHORIZED_ACCESS: ThreatLevel.HIGH,
            ThreatType.ANOMALOUS_BEHAVIOR: ThreatLevel.LOW
        }
        
        base_level = base_levels.get(pattern.threat_type, ThreatLevel.MEDIUM)
        
        # Adjust based on system criticality
        # In aerospace systems, any threat to flight-critical systems is escalated
        if "flight" in pattern.pattern_name.lower() or "critical" in pattern.pattern_name.lower():
            if base_level.value < ThreatLevel.CRITICAL.value:
                return ThreatLevel.CRITICAL
        
        return base_level
    
    def _extract_threat_indicators(self, pattern: ThreatPattern, metrics: SystemMetrics) -> Dict[str, Any]:
        """Extract threat indicators from metrics"""
        indicators = {
            "pattern_id": pattern.pattern_id,
            "detection_time": metrics.timestamp,
            "triggered_rules": []
        }
        
        metrics_dict = metrics.to_dict()
        
        for rule in pattern.detection_rules:
            metric_name = rule["metric"]
            if metric_name in metrics_dict:
                indicators["triggered_rules"].append({
                    "metric": metric_name,
                    "value": metrics_dict[metric_name],
                    "threshold": rule["threshold"],
                    "operator": rule["operator"]
                })
        
        return indicators
    
    def _process_threat_event(self, threat_event: ThreatEvent) -> None:
        """Process a detected threat event"""
        
        # Add to history and active threats
        self.threat_history.append(threat_event)
        self.active_threats[threat_event.event_id] = threat_event
        self.threats_detected += 1
        
        # Log the threat
        if threat_event.threat_level.value >= ThreatLevel.HIGH.value:
            self.logger.critical(f"Critical threat detected: {threat_event.description}")
        elif threat_event.threat_level.value >= ThreatLevel.MEDIUM.value:
            self.logger.error(f"High-priority threat detected: {threat_event.description}")
        else:
            self.logger.warning(f"Threat detected: {threat_event.description}")
        
        # Trigger automated response if enabled
        if self.automatic_response_enabled:
            self._trigger_automated_response(threat_event)
    
    def _trigger_automated_response(self, threat_event: ThreatEvent) -> None:
        """
        Trigger automated threat response
        
        Implements: SRS-TM-002 (Automated response)
        """
        pattern = None
        for p in self.threat_patterns.values():
            if p.threat_type == threat_event.threat_type:
                pattern = p
                break
        
        if not pattern:
            return
        
        for action in pattern.response_actions:
            if action in self.response_handlers:
                try:
                    success = self.response_handlers[action](threat_event)
                    if success:
                        threat_event.mitigation_actions.append(action)
                        self.logger.info(f"Executed response action {action.value} for threat {threat_event.event_id}")
                    else:
                        self.logger.error(f"Failed to execute response action {action.value}")
                except Exception as e:
                    self.logger.error(f"Error executing response action {action.value}: {e}")
        
        # Mark as mitigated if any actions were successful
        if threat_event.mitigation_actions:
            threat_event.mitigated = True
            self.threats_mitigated += 1
    
    def _handle_threat_alert(self, threat_event: ThreatEvent) -> None:
        """
        Handle threat alert processing
        
        Implements: SRS-TM-004 (Incident response)
        """
        
        # For catastrophic threats, trigger immediate failsafe
        if threat_event.threat_level == ThreatLevel.CATASTROPHIC:
            self.logger.critical("CATASTROPHIC THREAT DETECTED - INITIATING FAILSAFE PROCEDURES")
            
            if ResponseAction.FAILSAFE in self.response_handlers:
                try:
                    self.response_handlers[ResponseAction.FAILSAFE](threat_event)
                except Exception as e:
                    self.logger.error(f"Failsafe response failed: {e}")
        
        # Log forensic information
        self._log_forensic_data(threat_event)
    
    def _log_forensic_data(self, threat_event: ThreatEvent) -> None:
        """
        Log forensic data for threat analysis
        
        Implements: SRS-TM-004 (Forensic logging)
        """
        forensic_data = {
            "event_id": threat_event.event_id,
            "timestamp": threat_event.timestamp,
            "threat_type": threat_event.threat_type.value,
            "threat_level": threat_event.threat_level.name,
            "source_component": threat_event.source_component,
            "description": threat_event.description,
            "indicators": threat_event.indicators,
            "mitigation_actions": [action.value for action in threat_event.mitigation_actions],
            "mitigated": threat_event.mitigated
        }
        
        # In a real system, this would be logged to a secure forensic database
        self.logger.info(f"FORENSIC: {json.dumps(forensic_data)}")
    
    def _update_baseline(self, metrics: SystemMetrics) -> None:
        """Update baseline metrics for anomaly detection"""
        if not self.learning_mode and self.learning_samples < self.min_learning_samples:
            return
        
        metrics_dict = metrics.to_dict()
        
        for metric_name, value in metrics_dict.items():
            self.baseline_metrics[metric_name].append(value)
        
        self.learning_samples += 1
        
        # Switch to detection mode after learning
        if self.learning_mode and self.learning_samples >= self.min_learning_samples:
            self._calculate_anomaly_thresholds()
            self.learning_mode = False
            self.logger.info("Anomaly detection learning complete, switching to detection mode")
    
    def _calculate_anomaly_thresholds(self) -> None:
        """Calculate anomaly detection thresholds from baseline data"""
        for metric_name, values in self.baseline_metrics.items():
            if len(values) < 10:  # Need minimum samples
                continue
            
            mean_val = statistics.mean(values)
            std_val = statistics.stdev(values) if len(values) > 1 else 0
            
            # Set threshold at 3 standard deviations (99.7% of normal data)
            self.anomaly_thresholds[metric_name] = mean_val + (3 * std_val)
    
    def _detect_anomalies(self, metrics: SystemMetrics) -> List[ThreatEvent]:
        """Detect anomalous system behavior"""
        anomalies = []
        metrics_dict = metrics.to_dict()
        
        for metric_name, value in metrics_dict.items():
            if metric_name in self.anomaly_thresholds:
                threshold = self.anomaly_thresholds[metric_name]
                
                if value > threshold:
                    threat_event = ThreatEvent(
                        event_id="",
                        timestamp=metrics.timestamp,
                        threat_type=ThreatType.ANOMALOUS_BEHAVIOR,
                        threat_level=ThreatLevel.MEDIUM,
                        source_component="anomaly_detector",
                        description=f"Anomalous {metric_name}: {value:.2f} > {threshold:.2f}",
                        indicators={
                            "metric": metric_name,
                            "value": value,
                            "threshold": threshold,
                            "deviation": value - threshold
                        }
                    )
                    anomalies.append(threat_event)
        
        return anomalies
    
    def get_monitor_status(self) -> Dict:
        """
        Get comprehensive threat monitor status
        
        Returns:
            Dict containing monitor metrics and threat information
        """
        return {
            "timestamp": time.time(),
            "monitor_active": self.monitor_active,
            "learning_mode": self.learning_mode,
            "learning_samples": self.learning_samples,
            "automatic_response_enabled": self.automatic_response_enabled,
            "total_patterns": len(self.threat_patterns),
            "enabled_patterns": sum(1 for p in self.threat_patterns.values() if p.enabled),
            "active_threats": len(self.active_threats),
            "total_events_processed": self.total_events_processed,
            "threats_detected": self.threats_detected,
            "threats_mitigated": self.threats_mitigated,
            "mitigation_rate": (self.threats_mitigated / max(1, self.threats_detected)) * 100,
            "threat_patterns": {
                pattern_id: {
                    "name": pattern.pattern_name,
                    "type": pattern.threat_type.value,
                    "enabled": pattern.enabled,
                    "response_actions": [action.value for action in pattern.response_actions]
                } for pattern_id, pattern in self.threat_patterns.items()
            },
            "recent_threats": [
                {
                    "event_id": threat.event_id,
                    "timestamp": threat.timestamp,
                    "type": threat.threat_type.value,
                    "level": threat.threat_level.name,
                    "source": threat.source_component,
                    "description": threat.description,
                    "mitigated": threat.mitigated
                } for threat in self.threat_history[-10:]  # Last 10 threats
            ]
        }
    
    def get_threat_intelligence(self) -> Dict:
        """
        Get threat intelligence summary
        
        Implements: SRS-TM-003 (Threat intelligence)
        """
        # Analyze threat patterns and frequencies
        threat_type_counts = defaultdict(int)
        severity_counts = defaultdict(int)
        hourly_counts = defaultdict(int)
        
        current_time = time.time()
        recent_threats = [
            t for t in self.threat_history
            if current_time - t.timestamp <= 86400  # Last 24 hours
        ]
        
        for threat in recent_threats:
            threat_type_counts[threat.threat_type.value] += 1
            severity_counts[threat.threat_level.name] += 1
            hour = int((current_time - threat.timestamp) / 3600)
            hourly_counts[hour] += 1
        
        return {
            "analysis_period": "24_hours",
            "total_threats": len(recent_threats),
            "threat_types": dict(threat_type_counts),
            "severity_distribution": dict(severity_counts),
            "hourly_distribution": dict(hourly_counts),
            "top_threat_sources": self._get_top_threat_sources(recent_threats),
            "mitigation_effectiveness": (
                sum(1 for t in recent_threats if t.mitigated) / max(1, len(recent_threats))
            ) * 100,
            "recommendations": self._generate_threat_recommendations(recent_threats)
        }
    
    def _get_top_threat_sources(self, threats: List[ThreatEvent]) -> Dict[str, int]:
        """Get top threat sources from recent threats"""
        source_counts = defaultdict(int)
        for threat in threats:
            source_counts[threat.source_component] += 1
        
        # Return top 5 sources
        sorted_sources = sorted(source_counts.items(), key=lambda x: x[1], reverse=True)
        return dict(sorted_sources[:5])
    
    def _generate_threat_recommendations(self, threats: List[ThreatEvent]) -> List[str]:
        """Generate threat mitigation recommendations"""
        recommendations = []
        
        # Analyze unmitigated threats
        unmitigated = [t for t in threats if not t.mitigated]
        if len(unmitigated) > len(threats) * 0.2:  # >20% unmitigated
            recommendations.append("Consider strengthening automated response mechanisms")
        
        # Check for repeated threat types
        type_counts = defaultdict(int)
        for threat in threats:
            type_counts[threat.threat_type] += 1
        
        for threat_type, count in type_counts.items():
            if count > 10:  # Frequent occurrence
                recommendations.append(f"High frequency of {threat_type.value} - review prevention measures")
        
        # Check for critical threats
        critical_threats = [t for t in threats if t.threat_level.value >= ThreatLevel.CRITICAL.value]
        if critical_threats:
            recommendations.append("Critical threats detected - review security posture immediately")
        
        return recommendations
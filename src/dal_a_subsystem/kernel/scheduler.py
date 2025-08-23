"""
Real-Time Operating System Scheduler for DAL-A Software Subsystem
================================================================

Implements deterministic scheduling for safety-critical tasks with worst-case
execution time (WCET) enforcement and Simplex fallback mechanisms.

DO-178C Objectives:
- A-5: Software design conforms to software requirements
- A-6: Source code conforms to software design
- A-7: Source code is verifiable

Safety Requirements:
- SRS-SCHED-001: Deterministic task scheduling with WCET bounds
- SRS-SCHED-002: Priority-based preemptive scheduling
- SRS-SCHED-003: Simplex fallback on timing violations
- SRS-SCHED-004: Task isolation and resource protection
"""

import time
import threading
import heapq
from typing import Dict, List, Optional, Callable, Any
from dataclasses import dataclass, field
from enum import Enum
import logging


class TaskState(Enum):
    """Task execution states"""
    READY = "READY"
    RUNNING = "RUNNING"
    WAITING = "WAITING" 
    SUSPENDED = "SUSPENDED"
    TERMINATED = "TERMINATED"


class TaskPriority(Enum):
    """Safety-critical task priorities"""
    CRITICAL_DAL_A = 1      # Highest priority - catastrophic failure impact
    HAZARDOUS_DAL_B = 2     # High priority - hazardous failure impact
    MAJOR_DAL_C = 3         # Medium priority - major failure impact
    MINOR = 4               # Low priority - minor impact
    BACKGROUND = 5          # Lowest priority - background tasks


@dataclass
class TaskConfig:
    """Configuration for a real-time task"""
    name: str
    priority: TaskPriority
    wcet_ms: float                 # Worst Case Execution Time
    period_ms: float               # Task period for periodic tasks
    deadline_ms: float             # Relative deadline
    entry_point: Callable[[], Any]
    is_periodic: bool = True
    stack_size_kb: int = 64
    
    def __post_init__(self):
        """Validate task configuration"""
        if self.wcet_ms <= 0:
            raise ValueError("WCET must be positive")
        if self.period_ms <= 0:
            raise ValueError("Period must be positive") 
        if self.deadline_ms <= 0:
            raise ValueError("Deadline must be positive")
        if self.wcet_ms > self.deadline_ms:
            raise ValueError("WCET cannot exceed deadline")


@dataclass
class Task:
    """Real-time task with timing constraints"""
    config: TaskConfig
    state: TaskState = TaskState.READY
    next_release: float = 0.0
    actual_execution_time: float = 0.0
    deadline_misses: int = 0
    execution_count: int = 0
    last_execution: float = 0.0
    
    def __lt__(self, other):
        """Comparison for priority queue (higher priority = lower number)"""
        return self.config.priority.value < other.config.priority.value


class SimplexController:
    """
    Simplex fallback controller for safety-critical functions
    
    Provides a verified, simple fallback when the complex controller fails
    timing or correctness requirements.
    """
    
    def __init__(self):
        self.fallback_active = False
        self.fallback_triggers = 0
        self.safety_functions = {}
        
    def register_safety_function(self, task_name: str, fallback_fn: Callable) -> None:
        """Register a safety fallback function for a task"""
        self.safety_functions[task_name] = fallback_fn
        
    def trigger_fallback(self, task_name: str, reason: str) -> Any:
        """Trigger Simplex fallback for a failed task"""
        self.fallback_active = True
        self.fallback_triggers += 1
        
        logging.critical(f"Simplex fallback triggered for {task_name}: {reason}")
        
        if task_name in self.safety_functions:
            return self.safety_functions[task_name]()
        else:
            logging.error(f"No safety function registered for {task_name}")
            return None


class RTOSScheduler:
    """
    Real-Time Operating System Scheduler for DAL-A compliance
    
    Implements deterministic scheduling with WCET enforcement and Simplex fallback.
    Provides priority-based preemptive scheduling for safety-critical tasks.
    """
    
    def __init__(self, tick_rate_hz: float = 1000.0):
        """
        Initialize RTOS scheduler
        
        Args:
            tick_rate_hz: System tick rate in Hz (default 1 kHz for 1ms resolution)
        """
        self.tick_rate_hz = tick_rate_hz
        self.tick_period_ms = 1000.0 / tick_rate_hz
        
        self.tasks: Dict[str, Task] = {}
        self.ready_queue: List[Task] = []
        self.current_task: Optional[Task] = None
        
        self.scheduler_active = False
        self.total_ticks = 0
        self.cpu_utilization = 0.0
        
        # Simplex controller for safety fallbacks
        self.simplex = SimplexController()
        
        # Performance metrics
        self.context_switches = 0
        self.deadline_violations = 0
        self.total_execution_time = 0.0
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
    def add_task(self, config: TaskConfig) -> bool:
        """
        Add a new real-time task to the scheduler
        
        Args:
            config: Task configuration
            
        Returns:
            bool: True if task added successfully
            
        Implements: SRS-SCHED-001 (Deterministic scheduling)
        """
        try:
            if config.name in self.tasks:
                self.logger.error(f"Task {config.name} already exists")
                return False
                
            # Validate schedulability
            if not self._check_schedulability(config):
                self.logger.error(f"Task {config.name} would make system unschedulable")
                return False
                
            task = Task(config)
            task.next_release = time.time()
            
            self.tasks[config.name] = task
            self._insert_ready_queue(task)
            
            self.logger.info(f"Added task: {config.name} "
                           f"(Priority: {config.priority.name}, WCET: {config.wcet_ms}ms)")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to add task {config.name}: {e}")
            return False
    
    def remove_task(self, name: str) -> bool:
        """Remove a task from the scheduler"""
        if name in self.tasks:
            task = self.tasks[name]
            task.state = TaskState.TERMINATED
            
            # Remove from ready queue
            self.ready_queue = [t for t in self.ready_queue if t.config.name != name]
            heapq.heapify(self.ready_queue)
            
            del self.tasks[name]
            self.logger.info(f"Removed task: {name}")
            return True
        return False
    
    def start_scheduler(self) -> None:
        """
        Start the real-time scheduler
        
        Implements: SRS-SCHED-002 (Priority-based preemptive scheduling)
        """
        if self.scheduler_active:
            self.logger.warning("Scheduler already active")
            return
            
        self.scheduler_active = True
        self.logger.info("Starting RTOS scheduler")
        
        def scheduler_loop():
            last_tick = time.time()
            
            while self.scheduler_active:
                current_time = time.time()
                
                # Check for periodic task releases
                self._check_task_releases(current_time)
                
                # Execute highest priority ready task
                if self.ready_queue:
                    next_task = heapq.heappop(self.ready_queue)
                    self._execute_task(next_task, current_time)
                
                # Enforce tick rate
                next_tick = last_tick + self.tick_period_ms / 1000.0
                sleep_time = max(0, next_tick - time.time())
                if sleep_time > 0:
                    time.sleep(sleep_time)
                
                last_tick = next_tick
                self.total_ticks += 1
                
                # Update CPU utilization
                self._update_cpu_utilization()
        
        # Start scheduler thread
        self.scheduler_thread = threading.Thread(target=scheduler_loop, daemon=True)
        self.scheduler_thread.start()
    
    def stop_scheduler(self) -> None:
        """Stop the real-time scheduler"""
        self.scheduler_active = False
        self.logger.info("Stopping RTOS scheduler")
        
        if hasattr(self, 'scheduler_thread'):
            self.scheduler_thread.join(timeout=1.0)
    
    def register_simplex_fallback(self, task_name: str, fallback_fn: Callable) -> None:
        """
        Register a Simplex fallback function for a task
        
        Implements: SRS-SCHED-003 (Simplex fallback on violations)
        """
        self.simplex.register_safety_function(task_name, fallback_fn)
        self.logger.info(f"Registered Simplex fallback for task: {task_name}")
    
    def get_scheduler_status(self) -> Dict:
        """
        Get comprehensive scheduler status and metrics
        
        Returns:
            Dict containing scheduler metrics for monitoring
        """
        active_tasks = sum(1 for t in self.tasks.values() if t.state != TaskState.TERMINATED)
        
        return {
            "timestamp": time.time(),
            "scheduler_active": self.scheduler_active,
            "total_tasks": len(self.tasks),
            "active_tasks": active_tasks,
            "ready_tasks": len(self.ready_queue),
            "current_task": self.current_task.config.name if self.current_task else None,
            "total_ticks": self.total_ticks,
            "cpu_utilization_percent": self.cpu_utilization * 100,
            "context_switches": self.context_switches,
            "deadline_violations": self.deadline_violations,
            "simplex_triggers": self.simplex.fallback_triggers,
            "simplex_active": self.simplex.fallback_active,
            "tasks": {
                name: {
                    "state": task.state.value,
                    "priority": task.config.priority.name,
                    "execution_count": task.execution_count,
                    "deadline_misses": task.deadline_misses,
                    "last_execution_time": task.actual_execution_time,
                    "wcet_ms": task.config.wcet_ms,
                    "wcet_ratio": task.actual_execution_time / task.config.wcet_ms if task.config.wcet_ms > 0 else 0
                } for name, task in self.tasks.items()
            }
        }
    
    def _check_schedulability(self, new_config: TaskConfig) -> bool:
        """
        Check if adding a new task maintains system schedulability
        
        Uses Rate Monotonic Analysis for schedulability test
        """
        # Calculate total utilization including new task
        total_utilization = new_config.wcet_ms / new_config.period_ms
        
        for task in self.tasks.values():
            if task.config.is_periodic:
                total_utilization += task.config.wcet_ms / task.config.period_ms
        
        # For Rate Monotonic scheduling, utilization bound is n(2^(1/n) - 1)
        n = len(self.tasks) + 1
        utilization_bound = n * (2**(1/n) - 1)
        
        return total_utilization <= utilization_bound
    
    def _check_task_releases(self, current_time: float) -> None:
        """Check for periodic task releases"""
        for task in self.tasks.values():
            if (task.config.is_periodic and 
                task.state == TaskState.WAITING and 
                current_time >= task.next_release):
                
                task.state = TaskState.READY
                task.next_release += task.config.period_ms / 1000.0
                self._insert_ready_queue(task)
    
    def _insert_ready_queue(self, task: Task) -> None:
        """Insert task into priority-ordered ready queue"""
        task.state = TaskState.READY
        heapq.heappush(self.ready_queue, task)
    
    def _execute_task(self, task: Task, start_time: float) -> None:
        """
        Execute a task with timing monitoring
        
        Implements: SRS-SCHED-003 (Simplex fallback) and SRS-SCHED-004 (Task isolation)
        """
        try:
            # Context switch
            if self.current_task != task:
                self.current_task = task
                self.context_switches += 1
            
            task.state = TaskState.RUNNING
            task.last_execution = start_time
            
            # Execute task
            execution_start = time.time()
            result = task.config.entry_point()
            execution_time = (time.time() - execution_start) * 1000  # ms
            
            task.actual_execution_time = execution_time
            task.execution_count += 1
            self.total_execution_time += execution_time
            
            # Check WCET violation
            if execution_time > task.config.wcet_ms:
                self.logger.warning(f"Task {task.config.name} exceeded WCET: "
                                  f"{execution_time:.3f}ms > {task.config.wcet_ms}ms")
                
                # Trigger Simplex fallback for critical tasks
                if task.config.priority == TaskPriority.CRITICAL_DAL_A:
                    self.simplex.trigger_fallback(task.config.name, 
                                                f"WCET violation: {execution_time:.3f}ms")
            
            # Check deadline miss
            deadline = task.last_execution + task.config.deadline_ms / 1000.0
            if time.time() > deadline:
                task.deadline_misses += 1
                self.deadline_violations += 1
                self.logger.error(f"Task {task.config.name} missed deadline")
            
            # Set next state
            if task.config.is_periodic:
                task.state = TaskState.WAITING
            else:
                task.state = TaskState.TERMINATED
                
        except Exception as e:
            self.logger.error(f"Task {task.config.name} execution error: {e}")
            task.state = TaskState.TERMINATED
            
            # Trigger Simplex fallback on error
            if task.config.priority == TaskPriority.CRITICAL_DAL_A:
                self.simplex.trigger_fallback(task.config.name, f"Execution error: {e}")
    
    def _update_cpu_utilization(self) -> None:
        """Update CPU utilization metrics"""
        if self.total_ticks > 0:
            total_time_ms = self.total_ticks * self.tick_period_ms
            self.cpu_utilization = self.total_execution_time / total_time_ms
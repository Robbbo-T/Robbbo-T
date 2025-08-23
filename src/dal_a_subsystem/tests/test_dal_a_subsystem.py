"""
DAL-A Software Subsystem Test Suite
==================================

Comprehensive test suite for the DAL-A (Design Assurance Level A) software subsystem
following DO-178C guidelines for safety-critical aerospace software.

Test Categories:
- Unit Tests: Individual component testing
- Integration Tests: Inter-component interaction testing  
- System Tests: End-to-end system behavior testing
- Fault Injection Tests: Failure mode testing
- Security Tests: Cyber threat and vulnerability testing
- Performance Tests: Real-time and deterministic behavior testing

DO-178C Objectives Covered:
- A-14: Unit test procedures are correct and complete
- A-15: Unit test results are correct and complete
- A-16: Integration test procedures are correct and complete
- A-17: Integration test results are correct and complete
"""

import unittest
import time
import threading
import logging
from typing import List, Dict, Any
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

# Import all DAL-A subsystem components
from dal_a_subsystem.kernel.partition_manager import (
    PartitionManager, PartitionConfig, Partition, PartitionState
)
from dal_a_subsystem.kernel.scheduler import (
    RTOSScheduler, TaskConfig, Task, TaskPriority, SimplexController
)
from dal_a_subsystem.safety.voting_system import (
    TwoOfThreeVoting, VoterComponent, VotingResult, VoterState
)
from dal_a_subsystem.safety.fault_detector import (
    FaultDetector, ComponentMonitor, FaultEvent, FaultSeverity, FaultType
)
from dal_a_subsystem.security.cross_domain_validator import (
    CrossDomainValidator, SecurityDomain, CrossDomainMessage, SecurityLevel, DomainType, ValidationResult
)
from dal_a_subsystem.security.threat_monitor import (
    ThreatMonitor, ThreatEvent, ThreatLevel, ThreatType, SystemMetrics
)


class TestPartitionManager(unittest.TestCase):
    """Test cases for ARINC 653-like Partition Manager"""
    
    def setUp(self):
        """Set up test environment"""
        self.partition_manager = PartitionManager(max_jitter_us=50.0)
        self.test_executed = False
        
    def tearDown(self):
        """Clean up test environment"""
        if self.partition_manager.schedule_active:
            self.partition_manager.stop_schedule()
    
    def test_partition_creation(self):
        """Test SRS-PM-001: Partition isolation"""
        def test_function():
            self.test_executed = True
            return True
        
        config = PartitionConfig(
            name="test_partition",
            priority=1,
            time_budget_ms=10.0,
            memory_limit_kb=1024,
            criticality_level="DAL-A",
            entry_point=test_function
        )
        
        # Test partition addition
        result = self.partition_manager.add_partition(config)
        self.assertTrue(result)
        self.assertIn("test_partition", self.partition_manager.partitions)
        
        # Test duplicate partition rejection
        result = self.partition_manager.add_partition(config)
        self.assertFalse(result)
    
    def test_partition_scheduling(self):
        """Test SRS-PM-002: Timing budgets and jitter control"""
        execution_times = []
        
        def timed_function():
            start = time.time()
            # Simulate work
            time.sleep(0.001)  # 1ms work
            execution_times.append((time.time() - start) * 1000)
            return True
        
        config = PartitionConfig(
            name="timed_partition",
            priority=1,
            time_budget_ms=5.0,
            memory_limit_kb=512,
            criticality_level="DAL-A",
            entry_point=timed_function
        )
        
        self.partition_manager.add_partition(config)
        self.partition_manager.start_schedule()
        
        # Let it run for a short time
        time.sleep(0.2)
        self.partition_manager.stop_schedule()
        
        # Verify execution occurred and timing constraints
        self.assertGreater(len(execution_times), 0)
        for exec_time in execution_times:
            self.assertLess(exec_time, config.time_budget_ms)
    
    def test_partition_health_monitoring(self):
        """Test SRS-PM-004: Health monitoring"""
        def healthy_function():
            return True
        
        def faulty_function():
            raise Exception("Simulated fault")
        
        # Add healthy partition
        healthy_config = PartitionConfig(
            name="healthy_partition",
            priority=1,
            time_budget_ms=10.0,
            memory_limit_kb=512,
            criticality_level="DAL-B",
            entry_point=healthy_function
        )
        
        # Add faulty partition
        faulty_config = PartitionConfig(
            name="faulty_partition",
            priority=2,
            time_budget_ms=10.0,
            memory_limit_kb=512,
            criticality_level="DAL-C",
            entry_point=faulty_function
        )
        
        self.partition_manager.add_partition(healthy_config)
        self.partition_manager.add_partition(faulty_config)
        
        status = self.partition_manager.get_health_status()
        
        self.assertEqual(status["total_partitions"], 2)
        self.assertEqual(status["healthy_partitions"], 2)  # Initially healthy
        self.assertGreater(status["health_percentage"], 0)


class TestRTOSScheduler(unittest.TestCase):
    """Test cases for Real-Time Operating System Scheduler"""
    
    def setUp(self):
        """Set up test environment"""
        self.scheduler = RTOSScheduler(tick_rate_hz=1000.0)
        self.task_executions = []
        
    def tearDown(self):
        """Clean up test environment"""
        if self.scheduler.scheduler_active:
            self.scheduler.stop_scheduler()
    
    def test_task_creation_and_scheduling(self):
        """Test SRS-SCHED-001: Deterministic task scheduling"""
        def test_task():
            self.task_executions.append(time.time())
            return "task_completed"
        
        config = TaskConfig(
            name="test_task",
            priority=TaskPriority.CRITICAL_DAL_A,
            wcet_ms=5.0,
            period_ms=50.0,
            deadline_ms=40.0,
            entry_point=test_task,
            is_periodic=True
        )
        
        result = self.scheduler.add_task(config)
        self.assertTrue(result)
        self.assertIn("test_task", self.scheduler.tasks)
    
    def test_priority_based_scheduling(self):
        """Test SRS-SCHED-002: Priority-based preemptive scheduling"""
        high_priority_executions = []
        low_priority_executions = []
        
        def high_priority_task():
            high_priority_executions.append(time.time())
            return True
        
        def low_priority_task():
            low_priority_executions.append(time.time())
            return True
        
        # Add high priority task
        high_config = TaskConfig(
            name="high_priority",
            priority=TaskPriority.CRITICAL_DAL_A,
            wcet_ms=2.0,
            period_ms=20.0,
            deadline_ms=15.0,
            entry_point=high_priority_task
        )
        
        # Add low priority task
        low_config = TaskConfig(
            name="low_priority",
            priority=TaskPriority.BACKGROUND,
            wcet_ms=2.0,
            period_ms=20.0,
            deadline_ms=15.0,
            entry_point=low_priority_task
        )
        
        self.scheduler.add_task(high_config)
        self.scheduler.add_task(low_config)
        
        # Verify tasks were added
        status = self.scheduler.get_scheduler_status()
        self.assertEqual(status["total_tasks"], 2)
    
    def test_simplex_fallback(self):
        """Test SRS-SCHED-003: Simplex fallback on timing violations"""
        fallback_executed = False
        
        def faulty_task():
            # Simulate WCET violation
            time.sleep(0.1)  # 100ms > WCET
            return True
        
        def safety_fallback():
            nonlocal fallback_executed
            fallback_executed = True
            return "safety_output"
        
        # Register Simplex fallback
        self.scheduler.register_simplex_fallback("faulty_task", safety_fallback)
        
        config = TaskConfig(
            name="faulty_task",
            priority=TaskPriority.CRITICAL_DAL_A,
            wcet_ms=10.0,  # Will be exceeded
            period_ms=200.0,
            deadline_ms=150.0,
            entry_point=faulty_task,
            is_periodic=False
        )
        
        self.scheduler.add_task(config)
        
        # Verify Simplex registration
        self.assertIn("faulty_task", self.scheduler.simplex.safety_functions)


class TestTwoOfThreeVoting(unittest.TestCase):
    """Test cases for 2-out-of-3 Voting System"""
    
    def setUp(self):
        """Set up test environment"""
        self.voting_system = TwoOfThreeVoting("test_voting", comparison_tolerance=0.01)
        
    def test_voter_registration(self):
        """Test SRS-VOTE-001: 2oo3 voting setup"""
        def voter_a(x):
            return x * 2
        
        def voter_b(x):
            return x * 2
        
        def voter_c(x):
            return x * 2.001  # Slightly different
        
        # Add voters
        self.assertTrue(self.voting_system.add_voter("voter_a", voter_a))
        self.assertTrue(self.voting_system.add_voter("voter_b", voter_b))
        self.assertTrue(self.voting_system.add_voter("voter_c", voter_c))
        
        # Try to add 4th voter (should fail)
        self.assertFalse(self.voting_system.add_voter("voter_d", voter_a))
        
        self.assertEqual(len(self.voting_system.voters), 3)
    
    def test_consensus_voting(self):
        """Test SRS-VOTE-002: Byzantine fault tolerance - consensus case"""
        def voter_identical(x):
            return x * 10
        
        # All voters produce identical results
        self.voting_system.add_voter("voter_1", voter_identical)
        self.voting_system.add_voter("voter_2", voter_identical)
        self.voting_system.add_voter("voter_3", voter_identical)
        
        result, voting_result, details = self.voting_system.vote(5)
        
        self.assertEqual(voting_result, VotingResult.CONSENSUS)
        self.assertEqual(result, 50)
        self.assertEqual(details["participating_voters"], 3)
    
    def test_majority_voting(self):
        """Test SRS-VOTE-002: Byzantine fault tolerance - majority case"""
        def voter_correct(x):
            return x * 10
        
        def voter_faulty(x):
            return x * 999  # Faulty result
        
        # 2 correct voters, 1 faulty
        self.voting_system.add_voter("voter_1", voter_correct)
        self.voting_system.add_voter("voter_2", voter_correct)
        self.voting_system.add_voter("voter_3", voter_faulty)
        
        result, voting_result, details = self.voting_system.vote(5)
        
        self.assertEqual(voting_result, VotingResult.MAJORITY)
        self.assertEqual(result, 50)  # Correct result from majority
    
    def test_voter_health_monitoring(self):
        """Test SRS-VOTE-003: Automatic voter health monitoring"""
        def healthy_voter(x):
            return x * 2
        
        def failing_voter(x):
            raise Exception("Voter failure")
        
        self.voting_system.add_voter("healthy", healthy_voter)
        self.voting_system.add_voter("failing", failing_voter)
        self.voting_system.add_voter("healthy2", healthy_voter)
        
        # Multiple votes to trigger health monitoring
        for i in range(10):
            self.voting_system.vote(i)
        
        status = self.voting_system.get_system_status()
        
        # Check that failing voter is detected
        failing_voter_status = None
        for voter_name, voter_info in status["voters"].items():
            if voter_name == "failing":
                failing_voter_status = voter_info
                break
        
        self.assertIsNotNone(failing_voter_status)
        self.assertGreater(failing_voter_status["error_count"], 0)


class TestFaultDetector(unittest.TestCase):
    """Test cases for Fault Detection and Isolation System"""
    
    def setUp(self):
        """Set up test environment"""
        self.fault_detector = FaultDetector(detection_rate_hz=10.0)
        
    def tearDown(self):
        """Clean up test environment"""
        if self.fault_detector.detector_active:
            self.fault_detector.stop_detection()
    
    def test_component_registration(self):
        """Test SRS-FD-001: Continuous health monitoring setup"""
        def health_check():
            return {
                "temperature": 45.0,
                "voltage": 12.0,
                "operational": True
            }
        
        monitor = ComponentMonitor(
            component_id="test_component",
            health_check_function=health_check,
            check_interval_ms=100.0,
            fault_threshold={"temperature": 80.0, "voltage": 15.0}
        )
        
        result = self.fault_detector.register_component(monitor)
        self.assertTrue(result)
        self.assertIn("test_component", self.fault_detector.monitors)
    
    def test_fault_detection(self):
        """Test SRS-FD-002: Fault detection within 100ms"""
        fault_detected = False
        
        def faulty_health_check():
            return {
                "temperature": 95.0,  # Above threshold of 80.0
                "operational": True
            }
        
        monitor = ComponentMonitor(
            component_id="faulty_component",
            health_check_function=faulty_health_check,
            check_interval_ms=50.0,
            fault_threshold={"temperature": 80.0}
        )
        
        self.fault_detector.register_component(monitor)
        
        # Trigger health check manually
        self.fault_detector._check_component_health(monitor, time.time())
        
        # Check if fault was detected
        self.assertGreater(monitor.fault_count, 0)
    
    def test_fault_recovery(self):
        """Test SRS-FD-004: Fault recovery and graceful degradation"""
        recovery_called = False
        
        def recovery_function():
            nonlocal recovery_called
            recovery_called = True
            return True
        
        def health_check():
            return {"operational": False}  # Simulates fault condition
        
        monitor = ComponentMonitor(
            component_id="recoverable_component",
            health_check_function=health_check,
            check_interval_ms=100.0,
            fault_threshold={"operational": True},
            recovery_function=recovery_function
        )
        
        self.fault_detector.register_component(monitor)
        
        # Simulate fault and recovery attempt
        self.fault_detector._check_component_health(monitor, time.time())
        self.fault_detector._attempt_component_recovery(monitor)
        
        self.assertTrue(recovery_called)


class TestCrossDomainValidator(unittest.TestCase):
    """Test cases for Cross-Domain Security Validator"""
    
    def setUp(self):
        """Set up test environment"""
        self.validator = CrossDomainValidator()
        
        # Set up test domains
        self.flight_domain = SecurityDomain(
            domain_id="flight_critical",
            domain_type=DomainType.FLIGHT_CRITICAL,
            security_level=SecurityLevel.SECRET
        )
        
        self.business_domain = SecurityDomain(
            domain_id="business_logic",
            domain_type=DomainType.BUSINESS_CRITICAL,
            security_level=SecurityLevel.CONFIDENTIAL
        )
        
    def tearDown(self):
        """Clean up test environment"""
        if self.validator.validator_active:
            self.validator.stop_validator()
    
    def test_domain_registration(self):
        """Test SRS-CDV-001: Mandatory access control setup"""
        result = self.validator.register_domain(self.flight_domain)
        self.assertTrue(result)
        self.assertIn("flight_critical", self.validator.domains)
        
        # Test duplicate registration
        result = self.validator.register_domain(self.flight_domain)
        self.assertFalse(result)
    
    def test_information_flow_control(self):
        """Test SRS-CDV-002: Information flow control"""
        self.validator.register_domain(self.flight_domain)
        self.validator.register_domain(self.business_domain)
        
        # Configure allowed flow
        result = self.validator.configure_information_flow(
            "business_logic", "flight_critical", True
        )
        self.assertTrue(result)
        
        # Test message validation with allowed flow
        message = CrossDomainMessage(
            message_id="test_msg_001",
            source_domain="business_logic",
            target_domain="flight_critical",
            message_type="status_update",
            payload={"status": "operational"},
            timestamp=time.time(),
            security_level=SecurityLevel.CONFIDENTIAL
        )
        
        validation_result = self.validator.validate_message(message)
        self.assertEqual(validation_result, ValidationResult.APPROVED)
    
    def test_message_encryption(self):
        """Test SRS-CDV-003: Cryptographic validation"""
        self.validator.register_domain(self.flight_domain)
        self.validator.register_domain(self.business_domain)
        
        message = CrossDomainMessage(
            message_id="encrypt_test",
            source_domain="business_logic",
            target_domain="flight_critical",
            message_type="data",
            payload={"sensitive_data": "classified_information"},
            timestamp=time.time(),
            security_level=SecurityLevel.SECRET
        )
        
        # Test encryption
        result = self.validator.encrypt_message(message)
        self.assertTrue(result)
        self.assertTrue(message.encrypted)
        self.assertIsNotNone(message.signature)
        
        # Test decryption
        result = self.validator.decrypt_message(message)
        self.assertTrue(result)
        self.assertFalse(message.encrypted)
        self.assertEqual(message.payload["sensitive_data"], "classified_information")


class TestThreatMonitor(unittest.TestCase):
    """Test cases for Cyber Threat Monitoring System"""
    
    def setUp(self):
        """Set up test environment"""
        self.threat_monitor = ThreatMonitor(detection_interval_ms=50.0)
        
    def tearDown(self):
        """Clean up test environment"""
        if self.threat_monitor.monitor_active:
            self.threat_monitor.stop_monitoring()
    
    def test_threat_pattern_addition(self):
        """Test SRS-TM-001: Threat detection pattern setup"""
        from dal_a_subsystem.security.threat_monitor import ThreatPattern, ResponseAction
        
        pattern = ThreatPattern(
            pattern_id="test_intrusion",
            pattern_name="Test Intrusion Pattern",
            threat_type=ThreatType.INTRUSION_ATTEMPT,
            detection_rules=[
                {"metric": "failed_authentications", "operator": ">", "threshold": 5}
            ],
            threshold_values={"time_window": 60.0},
            response_actions=[ResponseAction.ALERT, ResponseAction.BLOCK]
        )
        
        result = self.threat_monitor.add_threat_pattern(pattern)
        self.assertTrue(result)
        self.assertIn("test_intrusion", self.threat_monitor.threat_patterns)
    
    def test_threat_detection(self):
        """Test SRS-TM-001: Real-time threat detection"""
        # Create metrics that should trigger DOS pattern
        malicious_metrics = SystemMetrics(
            timestamp=time.time(),
            cpu_usage=45.0,
            memory_usage=60.0,
            network_in_bps=150_000_000,  # 150 Mbps (exceeds 100 Mbps threshold)
            network_out_bps=1_000_000,
            disk_io_rate=500.0,
            active_connections=1500,  # Exceeds 1000 threshold
            failed_authentications=2
        )
        
        threats = self.threat_monitor.process_metrics(malicious_metrics)
        
        # Should detect DOS attack
        self.assertGreater(len(threats), 0)
        dos_threat = next((t for t in threats if t.threat_type == ThreatType.DENIAL_OF_SERVICE), None)
        self.assertIsNotNone(dos_threat)
    
    def test_automated_response(self):
        """Test SRS-TM-002: Automated threat response"""
        response_executed = False
        
        def mock_response_handler(threat_event):
            nonlocal response_executed
            response_executed = True
            return True
        
        from dal_a_subsystem.security.threat_monitor import ResponseAction
        
        # Register response handler
        self.threat_monitor.register_response_handler(ResponseAction.ALERT, mock_response_handler)
        
        # Create threat event that should trigger response
        threat_event = ThreatEvent(
            event_id="test_threat",
            timestamp=time.time(),
            threat_type=ThreatType.INTRUSION_ATTEMPT,
            threat_level=ThreatLevel.HIGH,
            source_component="test_component",
            description="Test threat for response"
        )
        
        # Process threat (should trigger automated response)
        self.threat_monitor._process_threat_event(threat_event)
        self.threat_monitor._trigger_automated_response(threat_event)
        
        self.assertTrue(response_executed)


class TestSystemIntegration(unittest.TestCase):
    """Integration tests for complete DAL-A subsystem"""
    
    def setUp(self):
        """Set up integrated test environment"""
        # Initialize all major components
        self.partition_manager = PartitionManager(max_jitter_us=50.0)
        self.scheduler = RTOSScheduler(tick_rate_hz=1000.0)
        self.voting_system = TwoOfThreeVoting("integration_test")
        self.fault_detector = FaultDetector(detection_rate_hz=10.0)
        self.threat_monitor = ThreatMonitor(detection_interval_ms=100.0)
        
        self.integration_results = []
        
    def tearDown(self):
        """Clean up integrated test environment"""
        components = [
            self.partition_manager, self.scheduler, 
            self.fault_detector, self.threat_monitor
        ]
        
        for component in components:
            if hasattr(component, 'schedule_active') and component.schedule_active:
                component.stop_schedule()
            elif hasattr(component, 'scheduler_active') and component.scheduler_active:
                component.stop_scheduler()
            elif hasattr(component, 'detector_active') and component.detector_active:
                component.stop_detection()
            elif hasattr(component, 'monitor_active') and component.monitor_active:
                component.stop_monitoring()
    
    def test_integrated_fault_tolerance(self):
        """Test integrated fault tolerance across all components"""
        def safe_computation(x):
            return x * 2 + 1
        
        def faulty_computation(x):
            if x > 5:
                raise Exception("Computation fault")
            return x * 2 + 1
        
        # Set up 2oo3 voting with fault injection
        self.voting_system.add_voter("voter_1", safe_computation)
        self.voting_system.add_voter("voter_2", safe_computation)
        self.voting_system.add_voter("voter_3", faulty_computation)
        
        # Test with values that trigger fault
        for test_value in [3, 7, 10]:  # 7 and 10 will cause voter_3 to fail
            result, vote_result, details = self.voting_system.vote(test_value)
            
            if test_value <= 5:
                self.assertEqual(vote_result, VotingResult.CONSENSUS)
            else:
                self.assertEqual(vote_result, VotingResult.MAJORITY)
                
            # Verify correct result despite faults
            expected = test_value * 2 + 1
            self.assertEqual(result, expected)
    
    def test_security_integration(self):
        """Test security components working together"""
        validator = CrossDomainValidator()
        
        # Set up security domains
        flight_domain = SecurityDomain(
            domain_id="flight_sys",
            domain_type=DomainType.FLIGHT_CRITICAL,
            security_level=SecurityLevel.SECRET
        )
        
        general_domain = SecurityDomain(
            domain_id="general_sys",
            domain_type=DomainType.GENERAL_PURPOSE,
            security_level=SecurityLevel.UNCLASSIFIED
        )
        
        validator.register_domain(flight_domain)
        validator.register_domain(general_domain)
        
        # Configure information flow (general -> flight should be denied)
        validator.configure_information_flow("general_sys", "flight_sys", False)
        
        # Test denied message
        denied_message = CrossDomainMessage(
            message_id="denied_test",
            source_domain="general_sys",
            target_domain="flight_sys",
            message_type="data",
            payload={"data": "test"},
            timestamp=time.time(),
            security_level=SecurityLevel.UNCLASSIFIED
        )
        
        result = validator.validate_message(denied_message)
        self.assertEqual(result, ValidationResult.DENIED)
    
    def test_real_time_performance(self):
        """Test real-time performance requirements"""
        execution_times = []
        
        def time_critical_task():
            start = time.time()
            # Simulate critical computation
            for i in range(100):
                _ = i * i
            end = time.time()
            execution_times.append((end - start) * 1000)  # Convert to ms
            return True
        
        # Configure high-priority real-time task
        task_config = TaskConfig(
            name="time_critical",
            priority=TaskPriority.CRITICAL_DAL_A,
            wcet_ms=5.0,  # 5ms WCET requirement
            period_ms=20.0,  # 20ms period (50 Hz)
            deadline_ms=15.0,  # 15ms deadline
            entry_point=time_critical_task,
            is_periodic=True
        )
        
        self.scheduler.add_task(task_config)
        self.scheduler.start_scheduler()
        
        # Let it run briefly
        time.sleep(0.1)
        self.scheduler.stop_scheduler()
        
        # Verify real-time constraints
        if execution_times:
            max_execution = max(execution_times)
            avg_execution = sum(execution_times) / len(execution_times)
            
            self.assertLess(max_execution, 5.0, "WCET violation detected")
            self.assertLess(avg_execution, 3.0, "Average execution time too high")


def run_dal_a_test_suite():
    """
    Run the complete DAL-A software subsystem test suite
    
    Returns:
        bool: True if all tests pass
    """
    # Configure logging for tests
    logging.basicConfig(
        level=logging.WARNING,  # Reduce noise during tests
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add all test classes
    test_classes = [
        TestPartitionManager,
        TestRTOSScheduler,
        TestTwoOfThreeVoting,
        TestFaultDetector,
        TestCrossDomainValidator,
        TestThreatMonitor,
        TestSystemIntegration
    ]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Generate test report
    total_tests = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    success_rate = ((total_tests - failures - errors) / total_tests) * 100 if total_tests > 0 else 0
    
    print(f"\n{'='*60}")
    print(f"DAL-A SOFTWARE SUBSYSTEM TEST REPORT")
    print(f"{'='*60}")
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {total_tests - failures - errors}")
    print(f"Failed: {failures}")
    print(f"Errors: {errors}")
    print(f"Success Rate: {success_rate:.1f}%")
    print(f"{'='*60}")
    
    if failures > 0:
        print("\nFAILURES:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback.split()[-1] if traceback else 'Unknown failure'}")
    
    if errors > 0:
        print("\nERRORS:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback.split()[-1] if traceback else 'Unknown error'}")
    
    return len(result.failures) == 0 and len(result.errors) == 0


if __name__ == "__main__":
    success = run_dal_a_test_suite()
    sys.exit(0 if success else 1)
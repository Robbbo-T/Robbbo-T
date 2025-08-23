"""
AMEDEO DAL-A Software Subsystem
===============================

This module implements the safety-critical software subsystem following DO-178C DAL-A guidelines.
It provides the core functionality for the AQUA-OS/ADT (Aerospace Digital Transponder) system
with aerospace-grade integrity and fault tolerance.

Key Components:
- Kernel: Time/space partitioning with ARINC 653-like scheduling
- Safety: 2oo3 voting system and fault tolerance mechanisms  
- Security: Cyber threat detection and cross-domain validation
- Monitoring: System health and performance monitoring

Compliance: DO-178C DAL-A, ARINC 653, ARP4754A, ARP4761
Version: 1.0.0
Classification: Safety-Critical
"""

__version__ = "1.0.0"
__compliance__ = "DO-178C DAL-A"
__safety_level__ = "CATASTROPHIC"

# Export main subsystem components
from .kernel.partition_manager import PartitionManager
from .kernel.scheduler import RTOSScheduler
from .safety.voting_system import TwoOfThreeVoting
from .safety.fault_detector import FaultDetector
from .security.cross_domain_validator import CrossDomainValidator
from .security.threat_monitor import ThreatMonitor

__all__ = [
    'PartitionManager',
    'RTOSScheduler', 
    'TwoOfThreeVoting',
    'FaultDetector',
    'CrossDomainValidator',
    'ThreatMonitor'
]
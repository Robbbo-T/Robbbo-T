"""
Cross-Domain Validator for DAL-A Software Subsystem
===================================================

Implements secure communication and validation between different security domains
in aerospace systems. Provides multi-level security (MLS) and prevents information leakage.

DO-178C Objectives:
- A-12: Software verification results are correct and complete

Security Requirements:
- SRS-CDV-001: Mandatory access control between security domains
- SRS-CDV-002: Information flow control and leak prevention
- SRS-CDV-003: Cryptographic validation of inter-domain messages
- SRS-CDV-004: Audit trail for all cross-domain operations
"""

import time
import hashlib
import hmac
import logging
from typing import Dict, List, Optional, Any, Tuple, Set
from dataclasses import dataclass, field
from enum import Enum
import threading
import json
import queue
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os


class SecurityLevel(Enum):
    """Security classification levels"""
    UNCLASSIFIED = 1
    RESTRICTED = 2
    CONFIDENTIAL = 3
    SECRET = 4
    TOP_SECRET = 5


class DomainType(Enum):
    """Types of security domains"""
    FLIGHT_CRITICAL = "FLIGHT_CRITICAL"     # Flight control systems
    MISSION_CRITICAL = "MISSION_CRITICAL"   # Navigation, communication
    SAFETY_CRITICAL = "SAFETY_CRITICAL"     # Emergency systems
    BUSINESS_CRITICAL = "BUSINESS_CRITICAL" # Business logic
    GENERAL_PURPOSE = "GENERAL_PURPOSE"     # Non-critical functions


class ValidationResult(Enum):
    """Cross-domain validation results"""
    APPROVED = "APPROVED"
    DENIED = "DENIED"
    PENDING = "PENDING"
    ERROR = "ERROR"


@dataclass
class SecurityDomain:
    """Represents a security domain with access controls"""
    domain_id: str
    domain_type: DomainType
    security_level: SecurityLevel
    allowed_communications: Set[str] = field(default_factory=set)
    encryption_key: Optional[bytes] = None
    
    def __post_init__(self):
        if not self.encryption_key:
            # Generate domain-specific encryption key
            self.encryption_key = Fernet.generate_key()


@dataclass
class CrossDomainMessage:
    """Message for cross-domain communication"""
    message_id: str
    source_domain: str
    target_domain: str
    message_type: str
    payload: Dict[str, Any]
    timestamp: float
    security_level: SecurityLevel
    signature: Optional[str] = None
    encrypted: bool = False
    
    def __post_init__(self):
        if self.timestamp <= 0:
            self.timestamp = time.time()
        if not self.message_id:
            self.message_id = hashlib.sha256(
                f"{self.source_domain}:{self.target_domain}:{self.timestamp}".encode()
            ).hexdigest()[:16]


@dataclass
class AuditEvent:
    """Audit event for cross-domain operations"""
    timestamp: float
    event_type: str
    source_domain: str
    target_domain: str
    message_id: str
    validation_result: ValidationResult
    details: Dict = field(default_factory=dict)


class CrossDomainValidator:
    """
    Cross-Domain Security Validator for Safety-Critical Systems
    
    Implements mandatory access control and information flow validation
    between different security domains in aerospace systems.
    """
    
    def __init__(self, master_key: Optional[bytes] = None):
        """
        Initialize cross-domain validator
        
        Args:
            master_key: Master encryption key for the system
        """
        self.domains: Dict[str, SecurityDomain] = {}
        self.pending_messages: Dict[str, CrossDomainMessage] = {}
        self.message_queue = queue.Queue()
        
        # Security policy
        self.security_policy: Dict[str, Any] = {}
        self.information_flow_rules: Dict[Tuple[str, str], bool] = {}
        
        # Audit and monitoring
        self.audit_log: List[AuditEvent] = []
        self.validator_active = False
        self.processed_messages = 0
        self.denied_messages = 0
        
        # Cryptographic setup
        if master_key:
            self.master_key = master_key
        else:
            # Generate master key from system entropy
            salt = os.urandom(16)
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
            )
            self.master_key = kdf.derive(b"AMEDEO_DAL_A_MASTER_KEY")
        
        self.cipher_suite = Fernet(base64.urlsafe_b64encode(self.master_key))
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
    def register_domain(self, domain: SecurityDomain) -> bool:
        """
        Register a new security domain
        
        Args:
            domain: Security domain configuration
            
        Returns:
            bool: True if domain registered successfully
            
        Implements: SRS-CDV-001 (Mandatory access control)
        """
        try:
            if domain.domain_id in self.domains:
                self.logger.warning(f"Domain {domain.domain_id} already registered")
                return False
            
            self.domains[domain.domain_id] = domain
            
            # Initialize default security policy for this domain
            self._initialize_domain_policy(domain)
            
            self.logger.info(f"Registered security domain: {domain.domain_id} "
                           f"(Type: {domain.domain_type.value}, Level: {domain.security_level.name})")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to register domain {domain.domain_id}: {e}")
            return False
    
    def configure_information_flow(self, source_domain: str, target_domain: str, allowed: bool) -> bool:
        """
        Configure information flow policy between domains
        
        Implements: SRS-CDV-002 (Information flow control)
        """
        try:
            if source_domain not in self.domains or target_domain not in self.domains:
                self.logger.error("Both domains must be registered before configuring flow")
                return False
            
            self.information_flow_rules[(source_domain, target_domain)] = allowed
            
            # Also update the domain's allowed communications
            if allowed:
                self.domains[source_domain].allowed_communications.add(target_domain)
            else:
                self.domains[source_domain].allowed_communications.discard(target_domain)
            
            self.logger.info(f"Information flow {source_domain} -> {target_domain}: "
                           f"{'ALLOWED' if allowed else 'DENIED'}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to configure information flow: {e}")
            return False
    
    def validate_message(self, message: CrossDomainMessage) -> ValidationResult:
        """
        Validate a cross-domain message
        
        Args:
            message: Message to validate
            
        Returns:
            ValidationResult: Validation decision
            
        Implements: SRS-CDV-001, SRS-CDV-002, SRS-CDV-003
        """
        try:
            # Check if domains exist
            if (message.source_domain not in self.domains or 
                message.target_domain not in self.domains):
                self._log_audit_event(message, ValidationResult.DENIED, 
                                    {"reason": "Unknown domain"})
                return ValidationResult.DENIED
            
            source_domain = self.domains[message.source_domain]
            target_domain = self.domains[message.target_domain]
            
            # Check information flow policy
            flow_key = (message.source_domain, message.target_domain)
            if not self.information_flow_rules.get(flow_key, False):
                self._log_audit_event(message, ValidationResult.DENIED,
                                    {"reason": "Information flow not permitted"})
                return ValidationResult.DENIED
            
            # Check security level (Bell-LaPadula model: no read up, no write down)
            if not self._check_security_level_policy(source_domain, target_domain, message):
                self._log_audit_event(message, ValidationResult.DENIED,
                                    {"reason": "Security level violation"})
                return ValidationResult.DENIED
            
            # Verify message integrity
            if not self._verify_message_integrity(message):
                self._log_audit_event(message, ValidationResult.DENIED,
                                    {"reason": "Message integrity check failed"})
                return ValidationResult.DENIED
            
            # Check message format and content
            if not self._validate_message_content(message):
                self._log_audit_event(message, ValidationResult.DENIED,
                                    {"reason": "Invalid message content"})
                return ValidationResult.DENIED
            
            # All checks passed
            self._log_audit_event(message, ValidationResult.APPROVED,
                                {"validation_time": time.time()})
            return ValidationResult.APPROVED
            
        except Exception as e:
            self.logger.error(f"Error validating message {message.message_id}: {e}")
            self._log_audit_event(message, ValidationResult.ERROR,
                                {"error": str(e)})
            return ValidationResult.ERROR
    
    def encrypt_message(self, message: CrossDomainMessage) -> bool:
        """
        Encrypt message payload for secure transmission
        
        Implements: SRS-CDV-003 (Cryptographic validation)
        """
        try:
            if message.encrypted:
                return True
            
            # Get target domain encryption key
            target_domain = self.domains.get(message.target_domain)
            if not target_domain or not target_domain.encryption_key:
                self.logger.error(f"No encryption key for domain {message.target_domain}")
                return False
            
            # Encrypt payload
            payload_json = json.dumps(message.payload)
            domain_cipher = Fernet(target_domain.encryption_key)
            encrypted_payload = domain_cipher.encrypt(payload_json.encode())
            
            # Update message
            message.payload = {"encrypted_data": base64.b64encode(encrypted_payload).decode()}
            message.encrypted = True
            
            # Generate message signature
            message.signature = self._generate_message_signature(message)
            
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to encrypt message {message.message_id}: {e}")
            return False
    
    def decrypt_message(self, message: CrossDomainMessage) -> bool:
        """
        Decrypt message payload for processing
        
        Implements: SRS-CDV-003 (Cryptographic validation)
        """
        try:
            if not message.encrypted:
                return True
            
            # Get source domain encryption key
            source_domain = self.domains.get(message.source_domain)
            if not source_domain or not source_domain.encryption_key:
                self.logger.error(f"No encryption key for domain {message.source_domain}")
                return False
            
            # Verify signature first
            if not self._verify_message_signature(message):
                self.logger.error(f"Message signature verification failed: {message.message_id}")
                return False
            
            # Decrypt payload
            encrypted_data = base64.b64decode(message.payload["encrypted_data"])
            domain_cipher = Fernet(source_domain.encryption_key)
            decrypted_payload = domain_cipher.decrypt(encrypted_data)
            
            # Update message
            message.payload = json.loads(decrypted_payload.decode())
            message.encrypted = False
            
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to decrypt message {message.message_id}: {e}")
            return False
    
    def process_message(self, message: CrossDomainMessage) -> bool:
        """
        Process a cross-domain message through validation pipeline
        
        Returns:
            bool: True if message was successfully processed
        """
        try:
            # Validate the message
            validation_result = self.validate_message(message)
            
            if validation_result != ValidationResult.APPROVED:
                self.denied_messages += 1
                return False
            
            # Encrypt if not already encrypted
            if not message.encrypted:
                if not self.encrypt_message(message):
                    return False
            
            # Queue for delivery
            self.message_queue.put(message)
            self.processed_messages += 1
            
            self.logger.info(f"Successfully processed message {message.message_id} "
                           f"from {message.source_domain} to {message.target_domain}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error processing message {message.message_id}: {e}")
            return False
    
    def start_validator(self) -> None:
        """Start the cross-domain validator"""
        if self.validator_active:
            self.logger.warning("Validator already active")
            return
        
        self.validator_active = True
        self.logger.info("Starting cross-domain validator")
        
        def validation_loop():
            while self.validator_active:
                try:
                    # Process queued messages
                    message = self.message_queue.get(timeout=1.0)
                    # In a real system, this would deliver the message to the target domain
                    self.logger.debug(f"Delivered message {message.message_id}")
                    
                except queue.Empty:
                    continue
                except Exception as e:
                    self.logger.error(f"Error in validation loop: {e}")
        
        # Start validation thread
        self.validation_thread = threading.Thread(target=validation_loop, daemon=True)
        self.validation_thread.start()
    
    def stop_validator(self) -> None:
        """Stop the cross-domain validator"""
        self.validator_active = False
        self.logger.info("Stopping cross-domain validator")
        
        if hasattr(self, 'validation_thread'):
            self.validation_thread.join(timeout=1.0)
    
    def _initialize_domain_policy(self, domain: SecurityDomain) -> None:
        """Initialize default security policy for a domain"""
        domain_policy = {
            "max_message_size": 1024 * 1024,  # 1MB
            "allowed_message_types": ["data", "control", "status"],
            "encryption_required": domain.security_level.value >= SecurityLevel.CONFIDENTIAL.value,
            "audit_required": True
        }
        
        self.security_policy[domain.domain_id] = domain_policy
    
    def _check_security_level_policy(self, source: SecurityDomain, target: SecurityDomain, 
                                   message: CrossDomainMessage) -> bool:
        """
        Check security level policy (Bell-LaPadula model)
        
        Implements: SRS-CDV-002 (Information flow control)
        """
        # Simple *-property: no write down (higher classification cannot write to lower)
        if source.security_level.value > target.security_level.value:
            return False
        
        # Message security level must not exceed target domain capability
        if message.security_level.value > target.security_level.value:
            return False
        
        return True
    
    def _verify_message_integrity(self, message: CrossDomainMessage) -> bool:
        """Verify message integrity"""
        # Check message completeness
        required_fields = ['message_id', 'source_domain', 'target_domain', 
                          'message_type', 'payload', 'timestamp']
        
        for field in required_fields:
            if not hasattr(message, field) or getattr(message, field) is None:
                return False
        
        # Check timestamp validity (not too old, not in future)
        current_time = time.time()
        if (current_time - message.timestamp) > 300:  # 5 minutes max age
            return False
        if message.timestamp > current_time + 60:  # 1 minute max future
            return False
        
        return True
    
    def _validate_message_content(self, message: CrossDomainMessage) -> bool:
        """Validate message content against domain policy"""
        source_policy = self.security_policy.get(message.source_domain, {})
        
        # Check message type
        allowed_types = source_policy.get("allowed_message_types", [])
        if allowed_types and message.message_type not in allowed_types:
            return False
        
        # Check message size
        max_size = source_policy.get("max_message_size", 1024 * 1024)
        payload_size = len(json.dumps(message.payload).encode())
        if payload_size > max_size:
            return False
        
        return True
    
    def _generate_message_signature(self, message: CrossDomainMessage) -> str:
        """Generate HMAC signature for message"""
        message_data = f"{message.message_id}:{message.source_domain}:" \
                      f"{message.target_domain}:{message.timestamp}:" \
                      f"{json.dumps(message.payload, sort_keys=True)}"
        
        signature = hmac.new(
            self.master_key,
            message_data.encode(),
            hashlib.sha256
        ).hexdigest()
        
        return signature
    
    def _verify_message_signature(self, message: CrossDomainMessage) -> bool:
        """Verify message HMAC signature"""
        if not message.signature:
            return False
        
        expected_signature = self._generate_message_signature(message)
        return hmac.compare_digest(message.signature, expected_signature)
    
    def _log_audit_event(self, message: CrossDomainMessage, result: ValidationResult, 
                        details: Dict) -> None:
        """
        Log audit event for cross-domain operation
        
        Implements: SRS-CDV-004 (Audit trail)
        """
        audit_event = AuditEvent(
            timestamp=time.time(),
            event_type="cross_domain_validation",
            source_domain=message.source_domain,
            target_domain=message.target_domain,
            message_id=message.message_id,
            validation_result=result,
            details=details
        )
        
        self.audit_log.append(audit_event)
        
        # Keep audit log size manageable
        if len(self.audit_log) > 10000:
            self.audit_log = self.audit_log[-5000:]  # Keep last 5000 events
    
    def get_validator_status(self) -> Dict:
        """
        Get comprehensive validator status and metrics
        
        Returns:
            Dict containing validator metrics and domain information
        """
        return {
            "timestamp": time.time(),
            "validator_active": self.validator_active,
            "total_domains": len(self.domains),
            "processed_messages": self.processed_messages,
            "denied_messages": self.denied_messages,
            "pending_messages": len(self.pending_messages),
            "approval_rate": (self.processed_messages / max(1, self.processed_messages + self.denied_messages)) * 100,
            "domains": {
                domain_id: {
                    "domain_type": domain.domain_type.value,
                    "security_level": domain.security_level.name,
                    "allowed_communications": list(domain.allowed_communications),
                    "has_encryption_key": domain.encryption_key is not None
                } for domain_id, domain in self.domains.items()
            },
            "information_flows": {
                f"{source}->{target}": allowed 
                for (source, target), allowed in self.information_flow_rules.items()
            },
            "recent_audit_events": [
                {
                    "timestamp": event.timestamp,
                    "event_type": event.event_type,
                    "source_domain": event.source_domain,
                    "target_domain": event.target_domain,
                    "message_id": event.message_id,
                    "validation_result": event.validation_result.value,
                    "details": event.details
                } for event in self.audit_log[-10:]  # Last 10 events
            ]
        }
    
    def get_audit_report(self, start_time: Optional[float] = None, 
                        end_time: Optional[float] = None) -> Dict:
        """
        Generate audit report for specified time period
        
        Implements: SRS-CDV-004 (Audit trail)
        """
        if start_time is None:
            start_time = time.time() - 3600  # Last hour
        if end_time is None:
            end_time = time.time()
        
        # Filter events by time range
        filtered_events = [
            event for event in self.audit_log
            if start_time <= event.timestamp <= end_time
        ]
        
        # Calculate statistics
        total_events = len(filtered_events)
        approved_events = sum(1 for e in filtered_events if e.validation_result == ValidationResult.APPROVED)
        denied_events = sum(1 for e in filtered_events if e.validation_result == ValidationResult.DENIED)
        error_events = sum(1 for e in filtered_events if e.validation_result == ValidationResult.ERROR)
        
        return {
            "report_period": {
                "start_time": start_time,
                "end_time": end_time,
                "duration_hours": (end_time - start_time) / 3600
            },
            "summary": {
                "total_events": total_events,
                "approved_events": approved_events,
                "denied_events": denied_events,
                "error_events": error_events,
                "approval_rate": (approved_events / max(1, total_events)) * 100
            },
            "events": [
                {
                    "timestamp": event.timestamp,
                    "source_domain": event.source_domain,
                    "target_domain": event.target_domain,
                    "message_id": event.message_id,
                    "validation_result": event.validation_result.value,
                    "details": event.details
                } for event in filtered_events
            ]
        }
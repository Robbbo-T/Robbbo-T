from dataclasses import dataclass, field
from typing import Any, Dict, Optional, List
from enum import Enum

class VerificationMethod(Enum):
    ANALYSIS = 'A'
    DEMONSTRATION = 'D'
    INSPECTION = 'I'
    TEST = 'T'

@dataclass
class ValidationResult:
    passed: bool
    plugin: str
    details: Dict[str, Any] = field(default_factory=dict)
    error: Optional[str] = None

@dataclass
class Requirement:
    id: str
    shall_statement: str
    verification_method: VerificationMethod
    acceptance_criteria: Dict[str, Any]
    tolerance: Dict[str, float]
    environmental_conditions: Dict[str, Any]
    category: str
    criticality: str
    standards: List[str] = field(default_factory=list)
    derives_from: List[str] = field(default_factory=list)
    verified_by: List[str] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'shall_statement': self.shall_statement,
            'verification_method': self.verification_method.value,
            'acceptance_criteria': self.acceptance_criteria,
            'tolerance': self.tolerance,
            'environmental_conditions': self.environmental_conditions,
            'category': self.category,
            'criticality': self.criticality,
            'standards': self.standards,
            'derives_from': self.derives_from,
            'verified_by': self.verified_by
        }

class SolverError(Exception):
    def __init__(self, solver: str, case: str, stderr: str = "", return_code: int = -1):
        super().__init__(f"{solver} failed for case '{case}' (rc={return_code})")
        self.solver = solver
        self.case = case
        self.stderr = stderr
        self.return_code = return_code

class SolverTimeoutError(Exception):
    def __init__(self, solver: str, timeout: float, case: str):
        super().__init__(f"{solver} timed out after {timeout}s for case '{case}'")
        self.solver = solver
        self.timeout = timeout
        self.case = case
import traceback
import uuid
import json
import os
from datetime import datetime
from typing import Optional, Dict, Any, List

class TraceableError(Exception):
    def __init__(self, message: str, **context):
        super().__init__(message)
        self.error_id = uuid.uuid4().hex[:8]
        self.timestamp = datetime.utcnow().isoformat()
        self.context = context
        self.stack_trace = traceback.format_stack()

    def to_dict(self) -> Dict[str, Any]:
        return {
            'error_id': self.error_id,
            'timestamp': self.timestamp,
            'message': str(self),
            'type': self.__class__.__name__,
            'context': self.context,
            'stack_trace': self.stack_trace
        }

class RequirementValidationError(TraceableError):
    def __init__(self, requirement_id: str, validation_type: str, 
                 details: Dict[str, Any], suggestion: Optional[str] = None):
        super().__init__(
            f"Validation failed for {requirement_id}",
            requirement_id=requirement_id,
            validation_type=validation_type,
            details=details,
            suggestion=suggestion
        )

class PhysicsConstraintViolation(TraceableError):
    def __init__(self, constraint: str, computed_value: float, 
                 limit: float, units: str, correction_hint: str, **extra):
        ctx = dict(
            constraint=constraint,
            computed_value=computed_value,
            limit=limit,
            units=units,
            correction_hint=correction_hint
        )
        ctx.update(extra or {})
        super().__init__(
            f"Physics constraint '{constraint}' violated: "
            f"{computed_value} {units} exceeds {limit} {units}",
            **ctx
        )

class ErrorReporter:
    def __init__(self, out_dir: str = "errors"):
        self.errors: List[Dict[str, Any]] = []
        self.warnings: List[Dict[str, Any]] = []
        self.out_dir = out_dir
        os.makedirs(self.out_dir, exist_ok=True)

    def log_error(self, error: TraceableError) -> Dict[str, Any]:
        error_dict = error.to_dict()
        error_dict['debugging_hints'] = self.generate_debugging_hints(error)
        self.errors.append(error_dict)
        
        error_file = os.path.join(self.out_dir, f"{error.error_id}.json")
        with open(error_file, 'w') as f:
            json.dump(error_dict, f, indent=2)
        
        return error_dict

    def generate_debugging_hints(self, error: TraceableError) -> List[str]:
        hints: List[str] = []
        
        if isinstance(error, PhysicsConstraintViolation):
            mat = error.context.get('material', '<unknown>')
            hints.extend([
                f"Verify material properties for: {mat}",
                "Check boundary conditions and load cases in the physics model",
                f"Consider: {error.context.get('correction_hint', 'N/A')}"
            ])
        elif isinstance(error, RequirementValidationError):
            derives = error.context.get('derives_from')
            stds = error.context.get('standards')
            if derives:
                hints.append(f"Review parent requirements: {derives}")
            if stds:
                hints.append(f"Check standards compliance: {stds}")
        
        return hints

    def generate_report(self) -> str:
        lines = [
            "# Requirements Generation Error Report",
            f"Generated: {datetime.utcnow().isoformat()}",
            f"Total Errors: {len(self.errors)}",
            f"Total Warnings: {len(self.warnings)}"
        ]
        
        by_type: Dict[str, List[Dict[str, Any]]] = {}
        for e in self.errors:
            by_type.setdefault(e['type'], []).append(e)
        
        for error_type, errors in by_type.items():
            lines.append(f"\n## {error_type} ({len(errors)} occurrences)")
            for e in errors[:5]:
                lines.append(f"- [{e['error_id']}] {e['message']}")
                for hint in e.get('debugging_hints', []):
                    lines.append(f"  → {hint}")
        
        return '\n'.join(lines)
from typing import Dict, Any, List
from core.types import Requirement, VerificationMethod
from utcs_mi.compliant_generator import UTCSMICompliantGenerator

class RequirementGenerator:
    """Basic requirements generator without UTCS MI compliance."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
    
    def generate_basic_requirements(self, inputs: Dict[str, Any]) -> List[Requirement]:
        """Generate basic requirements from design inputs."""
        requirements = []
        
        # Example structural requirement
        req = Requirement(
            id="REQ-STR-001",
            shall_statement="The wing structure shall withstand design ultimate loads",
            verification_method=VerificationMethod.ANALYSIS,
            acceptance_criteria={"load_factor": 1.5, "safety_margin": 0.15},
            tolerance={"stress": 0.05},
            environmental_conditions={"temperature": [-55, 85]},
            category="Structural",
            criticality="Critical",
            standards=["CS-25.301"]
        )
        requirements.append(req)
        
        return requirements

class EnhancedRequirementGenerator(RequirementGenerator):
    """Enhanced generator with physics validation and plugin support."""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.utcs_generator = UTCSMICompliantGenerator(config)
    
    def generate_validated_requirements(self, 
                                      design_inputs: Dict[str, Any],
                                      validation_enabled: bool = True) -> Dict[str, Any]:
        """Generate requirements with optional physics validation."""
        
        if validation_enabled:
            return self.utcs_generator.generate_requirements(
                design_inputs=design_inputs,
                regulatory_standards=self.config.get('regulatory_standards', []),
                physics_domains=self.config.get('physics_domains', [])
            )
        else:
            basic_reqs = self.generate_basic_requirements(design_inputs)
            return {
                'requirements': [req.to_dict() for req in basic_reqs],
                'validation_enabled': False
            }
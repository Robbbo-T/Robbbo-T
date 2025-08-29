# core/generator.py
from typing import Dict, List, Any, Optional
import json
import yaml
import os
try:
    from .types import Requirement, ValidationResult, VerificationMethod
    from ..physics_solvers.multiphysics import MultiphysicsOrchestrator
    from ..error_handling.traceable_errors import ErrorReporter, RequirementValidationError
except ImportError:
    # Fallback for direct execution
    import sys
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    sys.path.insert(0, parent_dir)
    
    from core.types import Requirement, ValidationResult, VerificationMethod
    from physics_solvers.multiphysics import MultiphysicsOrchestrator
    from error_handling.traceable_errors import ErrorReporter, RequirementValidationError

class RequirementsGenerator:
    """Main requirements generator orchestrating physics validation"""
    
    def __init__(self, config_path: Optional[str] = None):
        self.config = self._load_config(config_path)
        self.multiphysics = MultiphysicsOrchestrator()
        self.error_reporter = ErrorReporter()
        self.generated_requirements: List[Requirement] = []
        
    def _load_config(self, config_path: Optional[str]) -> Dict[str, Any]:
        """Load configuration from YAML file"""
        if config_path and os.path.exists(config_path):
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        
        # Default configuration
        return {
            'project': {
                'name': 'H2-BWB-Q',
                'version': '1.0.0',
                'standards': ['CS-25', 'FAR-25', 'RTCA-DO-178C']
            },
            'validation': {
                'physics_domains': ['aerodynamic', 'structural', 'thermal', 'hydrogen'],
                'safety_factors': {
                    'structural': 1.5,
                    'pressure': 2.0,
                    'temperature': 1.2
                }
            },
            'solvers': {
                'cfd_timeout': 600,
                'fea_timeout': 900,
                'thermal_timeout': 300
            }
        }
    
    def generate_requirement(self, template: Dict[str, Any]) -> Requirement:
        """Generate a single requirement from template"""
        req_id = template.get('id', f"REQ-{len(self.generated_requirements):03d}")
        
        requirement = Requirement(
            id=req_id,
            shall_statement=template['shall_statement'],
            verification_method=VerificationMethod(template.get('verification_method', 'A')),
            acceptance_criteria=template.get('acceptance_criteria', {}),
            tolerance=template.get('tolerance', {}),
            environmental_conditions=template.get('environmental_conditions', {}),
            category=template.get('category', 'General'),
            criticality=template.get('criticality', 'Medium'),
            standards=template.get('standards', []),
            derives_from=template.get('derives_from', []),
            verified_by=template.get('verified_by', [])
        )
        
        self.generated_requirements.append(requirement)
        return requirement
    
    def validate_requirement(self, requirement: Requirement) -> ValidationResult:
        """Validate a requirement using physics solvers"""
        try:
            # Convert requirement to dict for solver input
            req_dict = requirement.to_dict()
            
            # Determine which physics domains apply
            domains = self._extract_physics_domains(requirement)
            if domains:
                req_dict['physics_domains'] = domains
                results = self.multiphysics.validate_coupled(req_dict)
                
                if not results.get('overall_passed', True):
                    failed_domains = [
                        domain for domain, result in results.items()
                        if isinstance(result, dict) and not result.get('passed', True)
                    ]
                    return ValidationResult(
                        passed=False,
                        plugin='multiphysics',
                        details=results,
                        error=f"Physics validation failed in domains: {failed_domains}"
                    )
            
            return ValidationResult(
                passed=True,
                plugin='multiphysics',
                details=results if domains else {'status': 'no_physics_validation_required'}
            )
            
        except Exception as e:
            error = RequirementValidationError(
                requirement.id,
                'physics_validation',
                {'exception': str(e)},
                'Check solver configuration and input parameters'
            )
            self.error_reporter.log_error(error)
            
            return ValidationResult(
                passed=False,
                plugin='multiphysics',
                error=str(e)
            )
    
    def _extract_physics_domains(self, requirement: Requirement) -> List[str]:
        """Extract physics domains from requirement text and criteria"""
        domains = []
        text = requirement.shall_statement.lower()
        criteria = requirement.acceptance_criteria
        
        # Check for aerodynamic keywords
        if any(keyword in text for keyword in ['pressure', 'aerodynamic', 'flow', 'lift', 'drag']):
            domains.append('aerodynamic')
        
        # Check for structural keywords
        if any(keyword in text for keyword in ['stress', 'strain', 'structural', 'load', 'strength']):
            domains.append('structural')
        
        # Check for thermal keywords
        if any(keyword in text for keyword in ['temperature', 'thermal', 'heat', 'cooling']):
            domains.append('thermal')
        
        # Check for hydrogen keywords
        if any(keyword in text for keyword in ['hydrogen', 'h2', 'embrittlement', 'permeation']):
            domains.append('hydrogen')
        
        # Check acceptance criteria for domain-specific parameters
        if 'pressure_distribution' in criteria or 'cp_limit' in criteria:
            domains.append('aerodynamic')
        
        if 'stress_limit' in criteria or 'material' in criteria:
            domains.append('structural')
        
        if 'temperature_range' in criteria:
            domains.append('thermal')
        
        if 'h2_permeation_rate' in criteria:
            domains.append('hydrogen')
        
        return list(set(domains))  # Remove duplicates
    
    def batch_generate(self, templates: List[Dict[str, Any]]) -> List[Requirement]:
        """Generate multiple requirements from templates"""
        requirements = []
        for template in templates:
            try:
                req = self.generate_requirement(template)
                requirements.append(req)
            except Exception as e:
                self.error_reporter.log_error(RequirementValidationError(
                    template.get('id', 'unknown'),
                    'generation',
                    {'template': template, 'exception': str(e)}
                ))
        
        return requirements
    
    def export_requirements(self, output_path: str, format: str = 'json') -> None:
        """Export generated requirements to file"""
        requirements_data = {
            'project': self.config['project'],
            'generated_at': __import__('datetime').datetime.utcnow().isoformat(),
            'requirements': [req.to_dict() for req in self.generated_requirements],
            'count': len(self.generated_requirements)
        }
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        if format.lower() == 'json':
            with open(output_path, 'w') as f:
                json.dump(requirements_data, f, indent=2)
        elif format.lower() == 'yaml':
            with open(output_path, 'w') as f:
                yaml.dump(requirements_data, f, default_flow_style=False)
        else:
            raise ValueError(f"Unsupported format: {format}")
    
    def generate_validation_report(self) -> str:
        """Generate comprehensive validation report"""
        total = len(self.generated_requirements)
        if total == 0:
            return "No requirements generated yet."
        
        validated = sum(1 for req in self.generated_requirements 
                       if self.validate_requirement(req).passed)
        
        lines = [
            f"# Requirements Validation Report",
            f"Project: {self.config['project']['name']}",
            f"Generated: {__import__('datetime').datetime.utcnow().isoformat()}",
            f"",
            f"## Summary",
            f"- Total Requirements: {total}",
            f"- Validated: {validated}",
            f"- Failed: {total - validated}",
            f"- Success Rate: {validated/total*100:.1f}%",
            f"",
            f"## Error Summary",
            self.error_reporter.generate_report()
        ]
        
        return '\n'.join(lines)
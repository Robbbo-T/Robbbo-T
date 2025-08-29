# physics_solvers/multiphysics.py
from typing import Dict, Any
try:
    from .cfd_solver import CFDSolver
    from .fea_solver import FEASolver
    from .thermal_solver import ThermalSolver
    from .hydrogen_solver import HydrogenCompatibilitySolver
except ImportError:
    from cfd_solver import CFDSolver
    from fea_solver import FEASolver
    from thermal_solver import ThermalSolver
    from hydrogen_solver import HydrogenCompatibilitySolver

class MultiphysicsOrchestrator:
    """Orchestrate multiple physics solvers"""
    
    def __init__(self):
        self.solvers = {
            'cfd': CFDSolver(),
            'fea': FEASolver(),
            'thermal': ThermalSolver(),
            'hydrogen': HydrogenCompatibilitySolver()
        }

    def validate_coupled(self, requirement: Dict[str, Any]) -> Dict[str, Any]:
        """Run coupled multiphysics validation"""
        results: Dict[str, Any] = {}
        domains = set(requirement.get('physics_domains', []))

        # Thermal first for temperature distribution
        if 'thermal' in domains:
            thermal_result = self.solvers['thermal'].compute(requirement)
            results['thermal'] = thermal_result
            
            # Update structural model with thermal loads
            if 'structural' in domains:
                requirement['thermal_loads'] = thermal_result.get('temperature_field')

        # CFD for pressure loads
        if 'aerodynamic' in domains:
            cfd_pass, cfd_payload = self.solvers['cfd'].validate(requirement)
            results['aerodynamic'] = {'passed': cfd_pass, **cfd_payload}
            
            if 'structural' in domains and cfd_pass:
                # Transfer pressure loads to structural
                requirement['pressure_loads'] = cfd_payload.get('metrics', {})

        # Structural with all loads
        if 'structural' in domains:
            fea_pass, fea_payload = self.solvers['fea'].validate(requirement)
            results['structural'] = {'passed': fea_pass, **fea_payload}

        # Hydrogen compatibility check
        if 'hydrogen' in domains:
            h2_pass, h2_payload = self.solvers['hydrogen'].validate(requirement)
            results['hydrogen'] = {'passed': h2_pass, **h2_payload}

        # Overall pass/fail
        all_passed = all(
            v.get('passed', True) for v in results.values() 
            if isinstance(v, dict)
        )
        results['overall_passed'] = all_passed
        
        return results
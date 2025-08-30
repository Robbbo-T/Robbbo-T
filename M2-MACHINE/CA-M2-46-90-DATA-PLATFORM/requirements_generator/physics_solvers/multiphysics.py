from typing import Dict, Any
from .cfd_solver import CFDSolver
from .fea_solver import FEASolver
from .thermal_solver import ThermalSolver
from .hydrogen_solver import HydrogenCompatibilitySolver

class MultiphysicsOrchestrator:
    def __init__(self):
        self.solvers = {
            'cfd': CFDSolver(),
            'fea': FEASolver(),
            'thermal': ThermalSolver(),
            'hydrogen': HydrogenCompatibilitySolver()
        }

    def validate_coupled(self, requirement: Dict[str, Any]) -> Dict[str, Any]:
        results: Dict[str, Any] = {}
        domains = set(requirement.get('physics_domains', []))

        if 'thermal' in domains:
            thermal_result = self.solvers['thermal'].compute(requirement)
            results['thermal'] = thermal_result
            
            if 'structural' in domains:
                requirement['thermal_loads'] = thermal_result.get('temperature_field')

        if 'aerodynamic' in domains:
            cfd_pass, cfd_payload = self.solvers['cfd'].validate(requirement)
            results['aerodynamic'] = {'passed': cfd_pass, **cfd_payload}
            
            if 'structural' in domains and cfd_pass:
                requirement['pressure_loads'] = cfd_payload.get('metrics', {})

        if 'structural' in domains:
            fea_pass, fea_payload = self.solvers['fea'].validate(requirement)
            results['structural'] = {'passed': fea_pass, **fea_payload}

        if 'hydrogen' in domains:
            h2_pass, h2_payload = self.solvers['hydrogen'].validate(requirement)
            results['hydrogen'] = {'passed': h2_pass, **h2_payload}

        all_passed = all(
            v.get('passed', True) for v in results.values() 
            if isinstance(v, dict)
        )
        results['overall_passed'] = all_passed
        
        return results
from typing import Dict, Any, Tuple
import os
from .base import PhysicsSolverInterface, ExternalSolverAdapter
from .solver_configs import SolverConfigurations

class FEASolver(PhysicsSolverInterface):
    def __init__(self):
        self.adapter = ExternalSolverAdapter(
            {
                'type': 'CalculiX',
                'executable': 'ccx',
                'templates': 'templates/calculix/',
                'timeout': 900
            },
            command_builder=SolverConfigurations.calculix_command,
            result_parser=SolverConfigurations.parse_calculix_stress,
            workdir="work/calculix"
        )
        self.model_counter = 0

    def prepare_fea_model(self, requirement: Dict[str, Any]) -> str:
        self.model_counter += 1
        model_path = os.path.abspath(f"work/calculix/model_{self.model_counter:04d}.inp")
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        
        with open(model_path, "w") as f:
            f.write("*HEADING\n")
            f.write("Automated FEA Model\n")
            f.write("*NODE\n")
            f.write("1, 0.0, 0.0, 0.0\n")
            f.write("2, 1.0, 0.0, 0.0\n")
            f.write("*ELEMENT, TYPE=C3D8\n")
            f.write("1, 1, 2, 3, 4, 5, 6, 7, 8\n")
            f.write("*MATERIAL, NAME=MAT1\n")
            f.write("*ELASTIC\n")
            f.write("210000.0, 0.3\n")
            f.write("*STEP\n")
            f.write("*STATIC\n")
            f.write("*END STEP\n")
        
        return model_path

    def validate(self, requirement: Dict[str, Any]) -> Tuple[bool, Dict[str, Any]]:
        if 'stress_limit' in requirement or 'material' in requirement:
            model = self.prepare_fea_model(requirement)
            
            try:
                results = self.adapter.run_solver(model, case_name="structural")
            except Exception as e:
                return False, {'error': 'solver_failed', 'details': str(e)}
            
            von_mises = results.get('max_von_mises', 100e6)
            material = requirement.get('material', {})
            yield_strength = material.get('yield', 250e6)
            
            safety_factor = yield_strength / max(von_mises, 1e-9)
            min_sf = requirement.get('min_safety_factor', 1.5)

            if safety_factor < min_sf:
                return False, {
                    'error': 'insufficient_safety_factor',
                    'computed_sf': safety_factor,
                    'required_sf': min_sf,
                    'max_stress': von_mises,
                    'critical_element': results.get('critical_element')
                }
            
            return True, {
                'status': 'validated',
                'metrics': {
                    'safety_factor': safety_factor,
                    'max_stress': von_mises,
                    'yield_strength': yield_strength
                }
            }

        return True, {'status': 'not_applicable'}
    
    def compute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'max_stress': inputs.get('load', 1000) * 0.1,
            'max_displacement': inputs.get('load', 1000) * 0.001,
            'natural_frequency': 100.0
        }
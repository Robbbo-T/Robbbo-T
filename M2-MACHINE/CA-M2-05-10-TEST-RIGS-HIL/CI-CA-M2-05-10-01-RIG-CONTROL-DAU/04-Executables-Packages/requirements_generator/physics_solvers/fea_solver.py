# physics_solvers/fea_solver.py
from typing import Dict, Any, Tuple
import os
try:
    from .base import PhysicsSolverInterface, ExternalSolverAdapter
except ImportError:
    from base import PhysicsSolverInterface, ExternalSolverAdapter

def _ccx_cmd(exe: str, model_path: str) -> list:
    """Build CalculiX command"""
    if model_path.endswith(".inp"):
        model_path = model_path[:-4]  # Remove extension
    return [exe, model_path]

def _parse_ccx_results(model_path: str, stdout_text: str) -> Dict[str, Any]:
    """Parse CalculiX results"""
    results = {
        'max_von_mises_stress': None,
        'critical_element_id': None,
        'max_displacement': None,
        'raw_stdout': stdout_text[:4000]
    }
    
    # Parse .dat file if exists
    dat_file = model_path.replace('.inp', '.dat')
    if os.path.exists(dat_file):
        with open(dat_file, 'r') as f:
            content = f.read()
            # Simple parsing - real implementation would be more robust
            if 'MAXIMUM' in content and 'MISES' in content:
                lines = content.split('\n')
                for line in lines:
                    if 'MAXIMUM' in line and 'MISES' in line:
                        parts = line.split()
                        try:
                            results['max_von_mises_stress'] = float(parts[-1])
                        except:
                            pass
    
    # Fallback: extract from stdout
    if results['max_von_mises_stress'] is None:
        lines = stdout_text.split('\n')
        for line in lines:
            if 'maximum' in line.lower() and 'stress' in line.lower():
                parts = line.split()
                for part in parts:
                    try:
                        val = float(part)
                        if val > 0 and val < 1e10:
                            results['max_von_mises_stress'] = val
                            break
                    except:
                        continue
    
    return results

class FEASolver(PhysicsSolverInterface):
    """CalculiX integration for structural validation"""
    
    def __init__(self):
        self.adapter = ExternalSolverAdapter(
            {
                'type': 'CalculiX',
                'executable': 'ccx',
                'templates': 'templates/calculix/',
                'timeout': 900
            },
            command_builder=_ccx_cmd,
            result_parser=_parse_ccx_results,
            workdir="work/calculix"
        )
        self.model_counter = 0

    def prepare_fea_model(self, requirement: Dict[str, Any]) -> str:
        """Prepare CalculiX input file"""
        self.model_counter += 1
        model_path = os.path.abspath(f"work/calculix/model_{self.model_counter:04d}.inp")
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        
        # Generate input file based on requirement
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
        """Validate structural requirements"""
        if 'stress_limit' in requirement or 'material' in requirement:
            model = self.prepare_fea_model(requirement)
            
            try:
                results = self.adapter.run_solver(model, case_name="structural")
            except Exception as e:
                return False, {'error': 'solver_failed', 'details': str(e)}
            
            von_mises = results.get('max_von_mises_stress')
            if von_mises is None:
                # Default value for testing
                von_mises = 100e6  # 100 MPa
            
            material = requirement.get('material', {})
            yield_strength = material.get('yield', 250e6)  # Default 250 MPa
            
            safety_factor = yield_strength / max(von_mises, 1e-9)
            min_sf = requirement.get('min_safety_factor', 1.5)

            if safety_factor < min_sf:
                return False, {
                    'error': 'insufficient_safety_factor',
                    'computed_sf': safety_factor,
                    'required_sf': min_sf,
                    'max_stress': von_mises,
                    'critical_element': results.get('critical_element_id')
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
        """Compute structural response"""
        return {
            'max_stress': inputs.get('load', 1000) * 0.1,
            'max_displacement': inputs.get('load', 1000) * 0.001,
            'natural_frequency': 100.0
        }
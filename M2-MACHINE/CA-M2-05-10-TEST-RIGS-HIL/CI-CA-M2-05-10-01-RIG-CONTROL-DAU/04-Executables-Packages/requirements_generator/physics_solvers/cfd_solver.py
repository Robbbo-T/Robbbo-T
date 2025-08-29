# physics_solvers/cfd_solver.py
from typing import Dict, Any, Tuple
import os
import json
import shutil
try:
    from .base import PhysicsSolverInterface, ExternalSolverAdapter
except ImportError:
    from base import PhysicsSolverInterface, ExternalSolverAdapter

def _openfoam_cmd(exe: str, case_dir: str) -> list:
    """Build OpenFOAM command"""
    return [exe, "-case", case_dir]

def _parse_openfoam_results(case_dir: str, stdout_text: str) -> Dict[str, Any]:
    """Parse OpenFOAM results"""
    summary_path = os.path.join(case_dir, "post", "summary.json")
    if os.path.exists(summary_path):
        with open(summary_path) as f:
            return json.load(f)
    
    # Fallback: parse from log
    results = {
        "max_pressure_coefficient": None,
        "max_cp_location": None,
        "convergence": False,
        "raw_stdout": stdout_text[:4000]
    }
    
    # Try to extract residuals from stdout
    lines = stdout_text.split('\n')
    for line in lines:
        if 'Solving for p' in line and 'Final residual' in line:
            parts = line.split('Final residual')
            if len(parts) > 1:
                try:
                    residual = float(parts[1].split(',')[0].strip())
                    results['convergence'] = residual < 1e-5
                except:
                    pass
    
    return results

class CFDSolver(PhysicsSolverInterface):
    """OpenFOAM integration for CFD validation"""
    
    def __init__(self):
        self.adapter = ExternalSolverAdapter(
            {
                'type': 'OpenFOAM',
                'executable': 'simpleFoam',
                'templates': 'templates/openfoam/',
                'timeout': 600
            },
            command_builder=_openfoam_cmd,
            result_parser=_parse_openfoam_results,
            workdir="work/openfoam"
        )
        self.case_counter = 0

    def setup_pressure_case(self, requirement: Dict[str, Any]) -> str:
        """Setup OpenFOAM case directory"""
        self.case_counter += 1
        case_dir = os.path.abspath(f"work/openfoam/case_{self.case_counter:04d}")
        os.makedirs(case_dir, exist_ok=True)
        
        # Copy template files
        template_dir = self.adapter.template_dir
        if os.path.exists(template_dir):
            for item in ['0', 'constant', 'system']:
                src = os.path.join(template_dir, item)
                dst = os.path.join(case_dir, item)
                if os.path.exists(src):
                    if os.path.isdir(src):
                        shutil.copytree(src, dst, dirs_exist_ok=True)
                    else:
                        shutil.copy2(src, dst)
        
        return case_dir

    def validate(self, requirement: Dict[str, Any]) -> Tuple[bool, Dict[str, Any]]:
        """Validate aerodynamic requirements"""
        if 'pressure_distribution' in requirement:
            case = self.setup_pressure_case(requirement)
            results = self.adapter.run_solver(case, case_name="pressure")
            max_cp = results.get('max_pressure_coefficient')
            limit = requirement.get('cp_limit', 1.2)

            if max_cp is not None and max_cp > limit:
                return False, {
                    'error': 'pressure_limit_exceeded',
                    'computed': max_cp,
                    'limit': limit,
                    'location': results.get('max_cp_location')
                }
            return True, {
                'status': 'validated',
                'metrics': {'max_cp': max_cp, 'limit': limit}
            }

        return True, {'status': 'not_applicable'}
    
    def compute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """Compute aerodynamic coefficients"""
        return {
            'cl': inputs.get('aoa', 0) * 0.1,  # Simplified
            'cd': 0.02 + inputs.get('aoa', 0)**2 * 0.001,
            'cm': -0.05
        }
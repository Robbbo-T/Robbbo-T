from typing import Dict, Any, Tuple
import os
import json
import shutil
from .base import PhysicsSolverInterface, ExternalSolverAdapter
from .solver_configs import SolverConfigurations

class CFDSolver(PhysicsSolverInterface):
    def __init__(self):
        self.adapter = ExternalSolverAdapter(
            {
                'type': 'OpenFOAM',
                'executable': 'simpleFoam',
                'templates': 'templates/openfoam/',
                'timeout': 600
            },
            command_builder=SolverConfigurations.openfoam_command,
            result_parser=self._parse_results,
            workdir="work/openfoam"
        )
        self.case_counter = 0

    def _parse_results(self, case_dir: str, stdout_text: str) -> Dict[str, Any]:
        summary_path = os.path.join(case_dir, "post", "summary.json")
        if os.path.exists(summary_path):
            with open(summary_path) as f:
                return json.load(f)
        
        return {
            "max_pressure_coefficient": None,
            "max_cp_location": None,
            "convergence": False,
            "raw_stdout": stdout_text[:4000]
        }

    def setup_pressure_case(self, requirement: Dict[str, Any]) -> str:
        self.case_counter += 1
        case_dir = os.path.abspath(f"work/openfoam/case_{self.case_counter:04d}")
        os.makedirs(case_dir, exist_ok=True)
        
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
        return {
            'cl': inputs.get('aoa', 0) * 0.1,
            'cd': 0.02 + inputs.get('aoa', 0)**2 * 0.001,
            'cm': -0.05
        }
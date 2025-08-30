from typing import List, Dict, Any
import os
import re

class SolverConfigurations:
    @staticmethod
    def openfoam_command(executable: str, case_dir: str) -> List[str]:
        return [executable, "-case", case_dir]
    
    @staticmethod
    def calculix_command(executable: str, model_path: str) -> List[str]:
        if model_path.endswith('.inp'):
            model_path = model_path[:-4]
        return [executable, model_path]
    
    @staticmethod
    def parse_openfoam_convergence(log_path: str) -> Dict[str, Any]:
        results = {
            'converged': False,
            'final_residuals': {},
            'iterations': 0
        }
        
        if not os.path.exists(log_path):
            return results
            
        with open(log_path, 'r') as f:
            content = f.read()
            
        residual_pattern = r'Final residual = ([\d.e-]+)'
        matches = re.findall(residual_pattern, content)
        if matches:
            results['final_residuals'] = {
                f'residual_{i}': float(r) 
                for i, r in enumerate(matches[-10:])
            }
            
        if results['final_residuals']:
            max_residual = max(results['final_residuals'].values())
            results['converged'] = max_residual < 1e-5
            
        return results
    
    @staticmethod
    def parse_calculix_stress(dat_path: str) -> Dict[str, Any]:
        results = {
            'max_von_mises': None,
            'max_principal': None,
            'critical_element': None
        }
        
        if not os.path.exists(dat_path):
            return results
            
        with open(dat_path, 'r') as f:
            lines = f.readlines()
            
        in_stress_section = False
        for line in lines:
            if 'STRESS' in line and 'ELEMENT' in line:
                in_stress_section = True
                continue
                
            if in_stress_section and line.strip():
                parts = line.split()
                if len(parts) >= 3:
                    try:
                        elem_id = int(parts[0])
                        von_mises = float(parts[-1])
                        
                        if results['max_von_mises'] is None or von_mises > results['max_von_mises']:
                            results['max_von_mises'] = von_mises
                            results['critical_element'] = elem_id
                    except (ValueError, IndexError):
                        continue
                        
        return results
# physics_solvers/hydrogen_solver.py
from typing import Dict, Any, Tuple
try:
    from .base import PhysicsSolverInterface
except ImportError:
    from base import PhysicsSolverInterface

class HydrogenCompatibilitySolver(PhysicsSolverInterface):
    """Hydrogen compatibility validation"""
    
    def __init__(self):
        self.incompatible_materials = {
            '300M': 'High strength steel susceptible to H2 embrittlement',
            '4340': 'Steel alloy with poor H2 compatibility',
            'Maraging_250': 'Susceptible to hydrogen-induced cracking'
        }
        
        self.compatible_materials = {
            'Al-5083': 'Excellent H2 compatibility',
            'Ti-6Al-4V-ELI': 'Good with controlled H2 content',
            '316L': 'Acceptable for H2 service',
            'Inconel_718': 'Good H2 resistance'
        }
    
    def validate(self, requirement: Dict[str, Any]) -> Tuple[bool, Dict[str, Any]]:
        """Validate hydrogen compatibility"""
        material = requirement.get('material', {}).get('name', '')
        
        if material in self.incompatible_materials:
            return False, {
                'error': 'h2_incompatible_material',
                'material': material,
                'reason': self.incompatible_materials[material]
            }
        
        # Check permeation rate
        permeation_rate = requirement.get('h2_permeation_rate')
        if permeation_rate and permeation_rate > 1e-17:
            return False, {
                'error': 'excessive_permeation',
                'rate': permeation_rate,
                'limit': 1e-17
            }
        
        return True, {
            'status': 'validated',
            'compatibility': self.compatible_materials.get(material, 'Unknown')
        }
    
    def compute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """Compute H2 related parameters"""
        return {
            'permeation_rate': 5e-18,
            'embrittlement_factor': 0.95,
            'diffusion_coefficient': 1e-10
        }
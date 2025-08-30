from typing import Dict, Any, Tuple
from .base import PhysicsSolverInterface

class ThermalSolver(PhysicsSolverInterface):
    def validate(self, requirement: Dict[str, Any]) -> Tuple[bool, Dict[str, Any]]:
        if 'temperature_range' in requirement:
            t_min, t_max = requirement['temperature_range']
            if t_min < -273.15:
                return False, {'error': 'below_absolute_zero'}
            if t_max - t_min > 400:
                return False, {'error': 'excessive_temperature_range'}
        
        return True, {'status': 'validated'}
    
    def compute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'temperature_field': [[20.0 + i*j*0.1 for j in range(10)] for i in range(10)],
            'max_temperature': 85.0,
            'min_temperature': -253.0,
            'thermal_gradient': 20.0
        }
# plugins/validators/h2_compatibility.py
from typing import Dict, Any, List
try:
    from ..plugin_interface import ValidationPlugin
    from ...core.types import ValidationResult
except ImportError:
    import sys
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    grandparent_dir = os.path.dirname(parent_dir)
    sys.path.insert(0, grandparent_dir)
    from plugins.plugin_interface import ValidationPlugin
    from core.types import ValidationResult

class H2CompatibilityValidator(ValidationPlugin):
    """Hydrogen compatibility validation plugin"""
    
    def __init__(self):
        self.compatible_materials = {
            'Al-5083': {'rating': 'excellent', 'max_pressure': 700},
            'Ti-6Al-4V-ELI': {'rating': 'good', 'max_pressure': 350},
            '316L': {'rating': 'acceptable', 'max_pressure': 200},
            'Inconel_718': {'rating': 'good', 'max_pressure': 500}
        }
        
        self.incompatible_materials = {
            '300M': 'High strength steel susceptible to H2 embrittlement',
            '4340': 'Steel alloy with poor H2 compatibility',
            'Maraging_250': 'Susceptible to hydrogen-induced cracking'
        }
    
    def get_name(self) -> str:
        return "h2_compatibility"
    
    def get_version(self) -> str:
        return "1.0.0"
    
    def get_supported_categories(self) -> List[str]:
        return ["Hydrogen", "Materials", "Structures"]
    
    def validate(self, requirement: Dict[str, Any]) -> ValidationResult:
        """Validate hydrogen compatibility requirements"""
        
        # Check material compatibility
        material_name = requirement.get('material', {}).get('name', '')
        if material_name:
            if material_name in self.incompatible_materials:
                return ValidationResult(
                    passed=False,
                    plugin=self.get_name(),
                    details={
                        'material': material_name,
                        'reason': self.incompatible_materials[material_name],
                        'recommendation': 'Consider alternative H2-compatible materials'
                    },
                    error='Incompatible material for hydrogen service'
                )
            
            if material_name in self.compatible_materials:
                material_data = self.compatible_materials[material_name]
                operating_pressure = requirement.get('operating_pressure', 0)
                
                if operating_pressure > material_data['max_pressure']:
                    return ValidationResult(
                        passed=False,
                        plugin=self.get_name(),
                        details={
                            'material': material_name,
                            'operating_pressure': operating_pressure,
                            'max_pressure': material_data['max_pressure'],
                            'rating': material_data['rating']
                        },
                        error='Operating pressure exceeds material H2 compatibility limit'
                    )
        
        # Check permeation rate
        permeation_rate = requirement.get('h2_permeation_rate')
        if permeation_rate and permeation_rate > 1e-17:
            return ValidationResult(
                passed=False,
                plugin=self.get_name(),
                details={
                    'permeation_rate': permeation_rate,
                    'limit': 1e-17,
                    'units': 'mol/m²/s/Pa'
                },
                error='Hydrogen permeation rate exceeds acceptable limit'
            )
        
        # Check temperature effects on H2 compatibility
        temp_range = requirement.get('temperature_range', [])
        if temp_range:
            min_temp, max_temp = temp_range
            if max_temp > 150:  # Celsius
                return ValidationResult(
                    passed=False,
                    plugin=self.get_name(),
                    details={
                        'max_temperature': max_temp,
                        'limit': 150,
                        'concern': 'High temperature increases H2 embrittlement risk'
                    },
                    error='Temperature exceeds safe limit for H2 service'
                )
        
        return ValidationResult(
            passed=True,
            plugin=self.get_name(),
            details={
                'material_rating': self.compatible_materials.get(material_name, {}).get('rating', 'unknown'),
                'status': 'hydrogen_compatible'
            }
        )
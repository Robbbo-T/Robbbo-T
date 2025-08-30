from typing import Dict, Any, List
from plugins.plugin_interface import RequirementValidatorPlugin
from core.types import ValidationResult

class HydrogenCompatibilityValidator(RequirementValidatorPlugin):
    """Validates hydrogen compatibility requirements."""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        
        # Define materials known to be incompatible with hydrogen
        self.incompatible_materials = {
            '300M', '4340', 'Maraging_250', '15-5PH', '17-4PH',
            'AM355', 'Custom_450', 'PH13-8Mo'
        }
        
        # Define compatible materials
        self.compatible_materials = {
            'Al-5083', 'Al-6061', 'Ti-6Al-4V-ELI', '316L', '321', 
            'Inconel_718', 'Hastelloy_C276', 'Monel_400'
        }
        
        # Pressure limits for different materials (in MPa)
        self.pressure_limits = {
            'Al-5083': 70.0,
            'Ti-6Al-4V-ELI': 35.0,
            '316L': 100.0,
            'Inconel_718': 200.0
        }
    
    def validate(self, requirement: Dict[str, Any]) -> ValidationResult:
        """Validate hydrogen compatibility of materials and conditions."""
        
        material = requirement.get('material', {})
        material_name = material.get('name', '')
        
        # Check for incompatible materials
        if material_name in self.incompatible_materials:
            return ValidationResult(
                passed=False,
                plugin=self.name,
                details={
                    'material': material_name,
                    'issue': 'hydrogen_embrittlement_risk',
                    'severity': 'critical'
                },
                error=f"Material {material_name} is not compatible with hydrogen service"
            )
        
        # Check hydrogen pressure requirements
        h2_pressure = requirement.get('hydrogen_pressure', 0)
        if material_name in self.pressure_limits:
            limit = self.pressure_limits[material_name]
            if h2_pressure > limit:
                return ValidationResult(
                    passed=False,
                    plugin=self.name,
                    details={
                        'material': material_name,
                        'pressure': h2_pressure,
                        'limit': limit,
                        'units': 'MPa'
                    },
                    error=f"Hydrogen pressure {h2_pressure} MPa exceeds limit {limit} MPa for {material_name}"
                )
        
        # Check permeation rate requirements
        permeation_rate = requirement.get('h2_permeation_rate')
        if permeation_rate and permeation_rate > 1e-17:
            return ValidationResult(
                passed=False,
                plugin=self.name,
                details={
                    'permeation_rate': permeation_rate,
                    'limit': 1e-17,
                    'units': 'mol/m²·s·Pa'
                },
                error=f"Hydrogen permeation rate {permeation_rate} exceeds limit 1e-17"
            )
        
        # Check temperature range for hydrogen service
        temp_range = requirement.get('temperature_range')
        if temp_range:
            t_min, t_max = temp_range
            if t_min < -253 or t_max > 200:  # Typical hydrogen service limits
                return ValidationResult(
                    passed=False,
                    plugin=self.name,
                    details={
                        'temperature_range': temp_range,
                        'valid_range': [-253, 200],
                        'units': 'Celsius'
                    },
                    error=f"Temperature range {temp_range} outside hydrogen service limits [-253, 200] °C"
                )
        
        # If all checks pass
        compatibility_rating = 'excellent' if material_name in self.compatible_materials else 'unknown'
        
        return ValidationResult(
            passed=True,
            plugin=self.name,
            details={
                'material': material_name,
                'compatibility_rating': compatibility_rating,
                'checked_parameters': ['material_compatibility', 'pressure_limits', 'permeation_rate', 'temperature_range']
            }
        )
    
    def get_requirements(self) -> List[str]:
        """Return list of requirement fields this plugin needs."""
        return [
            'material',
            'hydrogen_pressure',
            'h2_permeation_rate',
            'temperature_range'
        ]
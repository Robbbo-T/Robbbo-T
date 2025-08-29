# AMPEL360 H₂-BWB-Q Requirements Generator

## Overview

The Requirements Generator is an engineering automation tool (M2 classification) that automates requirements generation with integrated physics solver validation for the H₂-BWB-Q (Hydrogen-powered Blended Wing Body) aircraft project.

## Key Features

### 🏗️ **Requirements Generation**
- Template-based requirement generation
- Full traceability with unique IDs
- Standards compliance mapping (CS-25, FAR-25, RTCA-DO-178C)
- Verification method assignment (Analysis, Demonstration, Inspection, Test)

### 🔬 **Physics Solver Integration**
- **CFD Validation**: OpenFOAM integration for aerodynamic requirements
- **FEA Validation**: CalculiX integration for structural requirements  
- **Thermal Analysis**: Temperature distribution and thermal gradient validation
- **Hydrogen Compatibility**: Material compatibility and permeation analysis
- **Multiphysics Orchestration**: Coupled validation across multiple domains

### 🔌 **Plugin System**
- Extensible validation framework
- H2 compatibility validator included
- Easy plugin development interface

### 📊 **Error Handling & Reporting**
- Traceable errors with unique IDs
- Context-aware debugging hints
- Comprehensive validation reports
- Export in JSON/YAML formats

## Quick Start

### Installation

1. **Clone the repository** (if not already done)
2. **Navigate to the requirements generator directory**:
   ```bash
   cd M2-MACHINE/CA-M2-05-10-TEST-RIGS-HIL/CI-CA-M2-05-10-01-RIG-CONTROL-DAU/04-Executables-Packages/requirements_generator
   ```

3. **Install dependencies** (optional - the core system works without external dependencies):
   ```bash
   pip install -r requirements.txt
   ```

### Basic Usage

#### List Available Plugins
```bash
python main.py --list-plugins
```

#### Generate and Validate Example Requirements
```bash
python main.py --validate-examples --output results/validation.json --verbose
```

#### Generate Requirements Only
```bash
python main.py --generate --output results/requirements.json
```

#### Use Custom Configuration
```bash
python main.py --config custom_config.yaml --validate-examples
```

## Configuration

The system uses YAML configuration files. See `config/h2_bwb_config.yaml` for the default configuration:

```yaml
project:
  name: "H2-BWB-Q"
  version: "1.0.0"
  standards: ["CS-25", "FAR-25", "RTCA-DO-178C"]

validation:
  physics_domains: ["aerodynamic", "structural", "thermal", "hydrogen"]
  safety_factors:
    structural: 1.5
    pressure: 2.0
    temperature: 1.2

solvers:
  cfd:
    executable: "simpleFoam"
    timeout: 600
  fea:
    executable: "ccx"
    timeout: 900
```

## Architecture

### Core Components

```
requirements_generator/
├── core/                   # Core types and generator logic
│   ├── types.py           # Data models and enums
│   └── generator.py       # Main requirements generator
├── physics_solvers/       # Physics validation
│   ├── base.py           # Solver interface and adapter
│   ├── cfd_solver.py     # OpenFOAM CFD integration
│   ├── fea_solver.py     # CalculiX FEA integration
│   ├── thermal_solver.py # Thermal analysis
│   ├── hydrogen_solver.py # H2 compatibility
│   └── multiphysics.py   # Coupled validation
├── plugins/               # Plugin system
│   ├── plugin_interface.py
│   └── validators/        # Validation plugins
├── error_handling/        # Error management
├── regulatory/           # Standards compliance
├── config/               # Configuration files
├── templates/            # Solver templates
└── tests/                # Test suite
```

### Example Requirements

The system includes example requirements demonstrating:

1. **Aerodynamic Requirements**: Wing pressure coefficient limits
2. **Structural Requirements**: Safety factor validation under loads
3. **Hydrogen Requirements**: Material compatibility and permeation

## Physics Validation Details

### CFD Validation (OpenFOAM)
- Pressure distribution analysis
- Pressure coefficient limits
- Convergence validation
- Automatic case setup from templates

### FEA Validation (CalculiX)
- Von Mises stress analysis
- Safety factor calculations
- Material property integration
- Load case generation

### Hydrogen Compatibility
- Material embrittlement assessment
- Permeation rate validation
- Temperature-pressure interaction effects
- Standards compliance (ASTM F3022)

## Extending the System

### Adding New Validators

1. **Create a new plugin class**:
```python
from plugins.plugin_interface import ValidationPlugin
from core.types import ValidationResult

class MyValidator(ValidationPlugin):
    def get_name(self) -> str:
        return "my_validator"
    
    def validate(self, requirement: Dict[str, Any]) -> ValidationResult:
        # Your validation logic here
        return ValidationResult(passed=True, plugin=self.get_name())
```

2. **Register the plugin**:
```python
plugin_manager.register_plugin(MyValidator())
```

### Adding New Solvers

1. **Implement the PhysicsSolverInterface**:
```python
from physics_solvers.base import PhysicsSolverInterface

class MyCustomSolver(PhysicsSolverInterface):
    def validate(self, requirement: Dict[str, Any]) -> Tuple[bool, Dict[str, Any]]:
        # Your solver logic here
        pass
```

2. **Add to MultiphysicsOrchestrator**:
```python
self.solvers['my_solver'] = MyCustomSolver()
```

## Testing

Run the test suite to validate installation:

```bash
python tests/test_basic.py
```

Expected output:
```
Requirements Generator Test Suite
==================================================
=== Testing Basic Functionality ===
✓ Successfully imported all modules
✓ Successfully initialized RequirementsGenerator
✓ Plugin system works

=== Physics Validation ===
✓ H2 validation completed - Passed: True
✓ Structural validation completed - Passed: True

=== Export Functionality ===
✓ JSON export works correctly

=== Test Results ===
Passed: 3/3
Success Rate: 100.0%
✓ All tests passed!
```

## Integration with M2-MACHINE

This requirements generator is implemented as part of the M2-MACHINE pillar:

- **Location**: `CA-M2-05-10-TEST-RIGS-HIL` (Test rigs/HIL integration)
- **Classification**: M2 (Engineering automation system)
- **Integration**: Physics solver integration for validation
- **Lifecycle Phase**: 04-Executables-Packages (Deployment-ready software)

### Relationship to OPTIME Framework

```
M2-05-10: Test rigs/HIL (integración con solvers)
M2-46-90: Data platform (procesamiento actual) 
M2-46-100: Training pipelines (si agregara ML)
```

This tool bridges engineering requirements with physics-based validation, supporting the transition from M2 (automation) toward potential I3 (intelligent) capabilities through data-driven validation and adaptive requirement generation.

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure you're running from the correct directory
2. **Solver Not Found**: CFD/FEA solvers are optional - validation will use fallback methods
3. **Configuration Issues**: Check YAML syntax in configuration files

### Debug Mode

Enable verbose logging:
```bash
python main.py --validate-examples --verbose
```

### Support

For issues related to:
- **Requirements generation**: Check `error_handling/` logs
- **Physics validation**: Review solver configurations
- **Plugin development**: Refer to `plugins/plugin_interface.py`

## License

Part of the AMPEL360 OPTIME framework. See project license for details.
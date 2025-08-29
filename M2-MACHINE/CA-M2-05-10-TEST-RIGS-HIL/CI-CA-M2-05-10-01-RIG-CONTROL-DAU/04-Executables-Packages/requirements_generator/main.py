#!/usr/bin/env python3
"""
AMPEL360 H₂-BWB-Q Requirements Generator

Main entry point for the requirements generation system.
Integrates physics solvers for automated validation.
"""

import argparse
import sys
import os
import json
import yaml
from pathlib import Path

# Add the requirements_generator to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.generator import RequirementsGenerator
from core.types import VerificationMethod
from plugins.plugin_interface import PluginManager
from plugins.validators.h2_compatibility import H2CompatibilityValidator
from regulatory.loaders import CS25Loader, FAR25Loader

def load_example_templates():
    """Load example requirement templates for demonstration"""
    return [
        {
            'id': 'REQ-AERO-001',
            'shall_statement': 'The wing shall maintain pressure coefficient below 1.2 at critical sections',
            'verification_method': 'A',
            'acceptance_criteria': {
                'pressure_distribution': True,
                'cp_limit': 1.2
            },
            'tolerance': {'cp': 0.05},
            'environmental_conditions': {
                'altitude': 35000,
                'mach': 0.85,
                'temperature': -54
            },
            'category': 'Aerodynamic',
            'criticality': 'High',
            'standards': ['CS-25.341', 'CS-25.345']
        },
        {
            'id': 'REQ-STRUCT-001',
            'shall_statement': 'Wing structure shall maintain safety factor >= 1.5 under limit loads',
            'verification_method': 'A',
            'acceptance_criteria': {
                'stress_limit': True,
                'min_safety_factor': 1.5
            },
            'tolerance': {'stress': 0.1},
            'environmental_conditions': {
                'load_factor': 2.5,
                'temperature': 85
            },
            'material': {
                'name': 'Al-5083',
                'yield': 250e6
            },
            'category': 'Structures',
            'criticality': 'Critical',
            'standards': ['CS-25.303', 'CS-25.307']
        },
        {
            'id': 'REQ-H2-001',
            'shall_statement': 'Hydrogen tank materials shall resist embrittlement at operating conditions',
            'verification_method': 'T',
            'acceptance_criteria': {
                'h2_permeation_rate': 5e-18,
                'operating_pressure': 350
            },
            'tolerance': {'permeation': 1e-18},
            'environmental_conditions': {
                'temperature_range': [-40, 85],
                'pressure': 350,
                'humidity': 'N/A'
            },
            'material': {
                'name': 'Al-5083'
            },
            'category': 'Hydrogen',
            'criticality': 'Critical',
            'standards': ['ASTM F3022', 'CS-25.963']
        }
    ]

def main():
    parser = argparse.ArgumentParser(
        description='AMPEL360 H₂-BWB-Q Requirements Generator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --generate --config config/h2_bwb_config.yaml
  python main.py --validate-examples --output results/validation_report.json
  python main.py --list-plugins
        """
    )
    
    parser.add_argument('--config', '-c', 
                       help='Path to configuration YAML file',
                       default='config/h2_bwb_config.yaml')
    
    parser.add_argument('--generate', '-g', action='store_true',
                       help='Generate requirements from examples')
    
    parser.add_argument('--validate-examples', action='store_true',
                       help='Validate example requirements with physics solvers')
    
    parser.add_argument('--output', '-o',
                       help='Output file path',
                       default='output/requirements.json')
    
    parser.add_argument('--format', '-f',
                       choices=['json', 'yaml'],
                       default='json',
                       help='Output format')
    
    parser.add_argument('--list-plugins', action='store_true',
                       help='List available validation plugins')
    
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose output')
    
    args = parser.parse_args()
    
    # Initialize the requirements generator
    try:
        generator = RequirementsGenerator(args.config)
        if args.verbose:
            print(f"✓ Initialized requirements generator with config: {args.config}")
    except Exception as e:
        print(f"✗ Failed to initialize generator: {e}")
        return 1
    
    # Initialize plugin manager
    plugin_manager = PluginManager()
    plugin_manager.register_plugin(H2CompatibilityValidator())
    
    if args.list_plugins:
        print("\n=== Available Validation Plugins ===")
        plugins = plugin_manager.list_plugins()
        for name, info in plugins.items():
            print(f"  {name} v{info['version']}")
            print(f"    Categories: {', '.join(info['categories'])}")
        return 0
    
    if args.generate or args.validate_examples:
        # Load example templates
        templates = load_example_templates()
        if args.verbose:
            print(f"✓ Loaded {len(templates)} example templates")
        
        # Generate requirements
        requirements = generator.batch_generate(templates)
        if args.verbose:
            print(f"✓ Generated {len(requirements)} requirements")
        
        # Validate with physics solvers if requested
        validation_results = {}
        if args.validate_examples:
            print("\n=== Physics Validation Results ===")
            for req in requirements:
                if args.verbose:
                    print(f"\nValidating {req.id}: {req.shall_statement[:60]}...")
                
                result = generator.validate_requirement(req)
                validation_results[req.id] = {
                    'passed': result.passed,
                    'plugin': result.plugin,
                    'details': result.details,
                    'error': result.error
                }
                
                status = "✓ PASS" if result.passed else "✗ FAIL"
                print(f"  {req.id}: {status}")
                if not result.passed and result.error:
                    print(f"    Error: {result.error}")
                
                # Run plugin validations
                plugin_results = plugin_manager.validate_with_plugins(req.to_dict())
                for plugin_result in plugin_results:
                    status = "✓ PASS" if plugin_result.passed else "✗ FAIL"
                    print(f"    Plugin {plugin_result.plugin}: {status}")
                    if not plugin_result.passed and plugin_result.error:
                        print(f"      Error: {plugin_result.error}")
        
        # Export results
        os.makedirs(os.path.dirname(args.output), exist_ok=True)
        
        output_data = {
            'requirements': [req.to_dict() for req in requirements],
            'validation_results': validation_results,
            'summary': {
                'total_requirements': len(requirements),
                'validation_enabled': args.validate_examples,
                'passed_validations': sum(1 for r in validation_results.values() if r['passed']) if validation_results else 0
            }
        }
        
        if args.format == 'json':
            with open(args.output, 'w') as f:
                json.dump(output_data, f, indent=2)
        else:
            with open(args.output, 'w') as f:
                yaml.dump(output_data, f, default_flow_style=False)
        
        print(f"\n✓ Results exported to: {args.output}")
        
        # Generate validation report
        if args.validate_examples:
            report = generator.generate_validation_report()
            report_path = args.output.replace('.json', '_report.md').replace('.yaml', '_report.md')
            with open(report_path, 'w') as f:
                f.write(report)
            print(f"✓ Validation report: {report_path}")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
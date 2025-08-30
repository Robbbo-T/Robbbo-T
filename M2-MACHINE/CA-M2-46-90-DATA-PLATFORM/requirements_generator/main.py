#!/usr/bin/env python3
"""
Requirements Generator for H2-BWB Aircraft
UTCS MI Compliant Engineering Automation Infrastructure

This system maps to M2-MACHINE framework:
- M2-46-90: Data platform (requirement processing pipeline) 
- M2-05-10: Test rigs/HIL (solver integration)
- M2-45-110: Orchestration (workflow management)
"""

import sys
import os
import json
import yaml
import argparse
from pathlib import Path
from typing import Dict, Any

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.enhanced_generator import EnhancedRequirementGenerator
from utcs_mi.compliant_generator import UTCSMICompliantGenerator

def load_config(config_path: str) -> Dict[str, Any]:
    """Load configuration from YAML file."""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def save_results(results: Dict[str, Any], output_path: str, format_type: str = 'json'):
    """Save results to file in specified format."""
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    if format_type.lower() == 'json':
        with open(output_file.with_suffix('.json'), 'w') as f:
            json.dump(results, f, indent=2)
    elif format_type.lower() == 'yaml':
        with open(output_file.with_suffix('.yaml'), 'w') as f:
            yaml.dump(results, f, default_flow_style=False)
    else:
        raise ValueError(f"Unsupported format: {format_type}")

def print_summary(results: Dict[str, Any]):
    """Print a summary of the generation results."""
    print("\n" + "="*60)
    print("REQUIREMENTS GENERATION SUMMARY")
    print("="*60)
    
    # Basic statistics
    req_count = len(results.get('requirements', []))
    print(f"Total Requirements Generated: {req_count}")
    
    # Domain breakdown
    domains = results.get('requirements_by_domain', {})
    if domains:
        print("\nRequirements by Domain:")
        for domain, reqs in domains.items():
            print(f"  {domain.capitalize()}: {len(reqs)} requirements")
    
    # Validation summary
    validation_summary = results.get('validation_summary', {})
    if validation_summary:
        print(f"\nValidation Results:")
        print(f"  Physics Validation: {'PASSED' if validation_summary.get('physics_validation_passed') else 'FAILED'}")
        print(f"  Plugin Validation: {'PASSED' if validation_summary.get('plugin_validation_passed') else 'FAILED'}")
        print(f"  Overall Status: {'PASSED' if validation_summary.get('overall_validation_passed') else 'FAILED'}")
    
    # Error summary
    error_analysis = results.get('error_analysis', {})
    if error_analysis:
        print(f"\nError Analysis:")
        print(f"  Total Errors: {error_analysis.get('total_errors', 0)}")
        print(f"  Total Warnings: {error_analysis.get('total_warnings', 0)}")
    
    # Compliance metadata
    compliance = results.get('compliance_metadata', {})
    if compliance:
        print(f"\nUTCS MI Compliance:")
        print(f"  Framework: {compliance.get('mi_framework', 'Unknown')}")
        print(f"  Version: {compliance.get('utcs_version', 'Unknown')}")
        print(f"  Traceability: {'Enabled' if compliance.get('traceability_enabled') else 'Disabled'}")
    
    print("="*60)

def main():
    """Main entry point for the requirements generator."""
    parser = argparse.ArgumentParser(
        description="H2-BWB Requirements Generator - UTCS MI Compliant",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --config config/h2_bwb_config.yaml --output results/h2_bwb_requirements
  python main.py --config config/h2_bwb_config.yaml --mode utcs --format yaml
  python main.py --config config/h2_bwb_config.yaml --no-physics --no-plugins
        """
    )
    
    parser.add_argument(
        '--config', '-c',
        default='config/h2_bwb_config.yaml',
        help='Configuration file path (default: config/h2_bwb_config.yaml)'
    )
    
    parser.add_argument(
        '--output', '-o', 
        default='output/requirements',
        help='Output file path (default: output/requirements)'
    )
    
    parser.add_argument(
        '--format', '-f',
        choices=['json', 'yaml'],
        default='json',
        help='Output format (default: json)'
    )
    
    parser.add_argument(
        '--mode', '-m',
        choices=['basic', 'enhanced', 'utcs'],
        default='enhanced',
        help='Generation mode (default: enhanced)'
    )
    
    parser.add_argument(
        '--no-physics',
        action='store_true',
        help='Disable physics validation'
    )
    
    parser.add_argument(
        '--no-plugins', 
        action='store_true',
        help='Disable plugin validation'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )
    
    args = parser.parse_args()
    
    try:
        # Load configuration
        if args.verbose:
            print(f"Loading configuration from: {args.config}")
        config = load_config(args.config)
        
        # Extract design inputs from config
        design_inputs = {
            **config.get('aircraft_config', {}),
            **config.get('design_loads', {}),
            **config.get('hydrogen_system', {}),
            **config.get('environmental_conditions', {}),
            'materials': config.get('materials', {}),
            'regulatory_standards': config.get('regulatory_standards', {})
        }
        
        # Initialize generator based on mode
        if args.mode == 'utcs':
            if args.verbose:
                print("Initializing UTCS MI Compliant Generator...")
            generator = UTCSMICompliantGenerator(config)
            results = generator.generate_requirements(
                design_inputs=design_inputs,
                regulatory_standards=config.get('regulatory_standards', {}).get('airworthiness', []),
                physics_domains=['structural', 'thermal', 'hydrogen', 'aerodynamic']
            )
        elif args.mode == 'enhanced':
            if args.verbose:
                print("Initializing Enhanced Requirements Generator...")
            generator = EnhancedRequirementGenerator(config)
            results = generator.generate_with_full_validation(
                design_inputs=design_inputs,
                enable_physics=not args.no_physics,
                enable_plugins=not args.no_plugins
            )
        else:  # basic mode
            if args.verbose:
                print("Initializing Basic Requirements Generator...")
            from core.generator import RequirementGenerator
            generator = RequirementGenerator(config)
            basic_reqs = generator.generate_basic_requirements(design_inputs)
            results = {
                'requirements': [req.to_dict() for req in basic_reqs],
                'mode': 'basic'
            }
        
        # Save results
        if args.verbose:
            print(f"Saving results to: {args.output}")
        save_results(results, args.output, args.format)
        
        # Print summary
        print_summary(results)
        
        print(f"\nResults saved to: {args.output}.{args.format}")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
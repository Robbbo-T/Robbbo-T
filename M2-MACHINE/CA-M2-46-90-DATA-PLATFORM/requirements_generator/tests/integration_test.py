#!/usr/bin/env python3
"""
Integration Test for Requirements Generator
Tests the complete end-to-end functionality of the H2-BWB requirements generator.
"""

import sys
import os
import tempfile
import json
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.enhanced_generator import EnhancedRequirementGenerator
from utcs_mi.compliant_generator import UTCSMICompliantGenerator
from physics_solvers.multiphysics import MultiphysicsOrchestrator
from plugins.plugin_interface import PluginManager

def test_basic_functionality():
    """Test basic requirements generation functionality."""
    print("Testing basic functionality...")
    
    # Sample configuration
    config = {
        'system': {'name': 'H2-BWB-Q', 'version': '1.0.0'},
        'physics_domains': ['structural', 'thermal', 'hydrogen'],
        'regulatory_standards': ['CS-25', 'FAR-25']
    }
    
    # Sample design inputs
    design_inputs = {
        'aircraft_type': 'blended_wing_body',
        'propulsion': 'hydrogen_fuel_cell',
        'design_ultimate_load': 150000,
        'max_operating_temperature': 85,
        'hydrogen_pressure': 70,
        'target_lift_coefficient': 1.8,
        'material': {'name': 'Al-5083', 'yield': 250e6}
    }
    
    try:
        # Test UTCS MI compliant generator
        utcs_generator = UTCSMICompliantGenerator(config)
        utcs_results = utcs_generator.generate_requirements(
            design_inputs=design_inputs,
            regulatory_standards=['CS-25', 'FAR-25'],
            physics_domains=['structural', 'thermal', 'hydrogen', 'aerodynamic']
        )
        
        assert len(utcs_results['requirements']) > 0, "No requirements generated"
        assert 'compliance_metadata' in utcs_results, "Missing compliance metadata"
        assert utcs_results['compliance_metadata']['mi_framework'] == 'M2-MACHINE'
        
        print("✓ UTCS MI generator working correctly")
        
        # Test enhanced generator
        enhanced_generator = EnhancedRequirementGenerator(config)
        enhanced_results = enhanced_generator.generate_with_full_validation(
            design_inputs=design_inputs,
            enable_physics=False,  # Disable physics solvers for basic test
            enable_plugins=True
        )
        
        assert len(enhanced_results['requirements']) > 0, "No enhanced requirements generated"
        assert 'validation_summary' in enhanced_results, "Missing validation summary"
        
        print("✓ Enhanced generator working correctly")
        
        return True
        
    except Exception as e:
        print(f"✗ Basic functionality test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_physics_solvers():
    """Test physics solver components."""
    print("Testing physics solvers...")
    
    try:
        orchestrator = MultiphysicsOrchestrator()
        
        # Test requirement with multiple physics domains
        test_requirement = {
            'physics_domains': ['structural', 'thermal', 'hydrogen'],
            'material': {'name': 'Al-5083', 'yield': 250e6},
            'stress_limit': 200e6,
            'min_safety_factor': 1.5,
            'temperature_range': [-55, 85],
            'hydrogen_pressure': 70,
            'h2_permeation_rate': 5e-18
        }
        
        results = orchestrator.validate_coupled(test_requirement)
        
        assert 'overall_passed' in results, "Missing overall validation result"
        assert isinstance(results['overall_passed'], bool), "Invalid validation result type"
        
        print("✓ Physics solvers working correctly")
        return True
        
    except Exception as e:
        print(f"✗ Physics solvers test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_plugin_system():
    """Test plugin validation system."""
    print("Testing plugin system...")
    
    try:
        plugin_manager = PluginManager([])  # Empty plugin dirs for basic test
        
        # Test requirement
        test_requirement = {
            'id': 'TEST-001',
            'material': {'name': 'Al-5083'},
            'hydrogen_pressure': 70,
            'h2_permeation_rate': 5e-18,
            'temperature_range': [-55, 85]
        }
        
        # Should work even with no plugins loaded
        results = plugin_manager.validate_requirement(test_requirement)
        assert isinstance(results, list), "Plugin results should be a list"
        
        summary = plugin_manager.get_plugin_summary()
        assert 'loaded_plugins' in summary, "Missing plugin summary"
        
        print("✓ Plugin system working correctly")
        return True
        
    except Exception as e:
        print(f"✗ Plugin system test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_error_handling():
    """Test error handling and traceability."""
    print("Testing error handling...")
    
    try:
        from error_handling.traceable_errors import ErrorReporter, TraceableError
        
        with tempfile.TemporaryDirectory() as temp_dir:
            reporter = ErrorReporter(temp_dir)
            
            # Create and log a test error
            test_error = TraceableError("Test error message", test_param="test_value")
            error_dict = reporter.log_error(test_error)
            
            assert 'error_id' in error_dict, "Missing error ID"
            assert 'timestamp' in error_dict, "Missing timestamp"
            assert len(reporter.errors) == 1, "Error not recorded"
            
            # Check error file was created
            error_file = Path(temp_dir) / f"{test_error.error_id}.json"
            assert error_file.exists(), "Error file not created"
            
            # Generate report
            report = reporter.generate_report()
            assert "Test error message" in report, "Error message missing from report"
        
        print("✓ Error handling working correctly")
        return True
        
    except Exception as e:
        print(f"✗ Error handling test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_end_to_end():
    """Test complete end-to-end workflow."""
    print("Testing end-to-end workflow...")
    
    try:
        # Complete configuration
        config = {
            'system': {
                'name': 'H2-BWB-Q',
                'version': '1.0.0',
                'description': 'Hydrogen Blended Wing Body aircraft'
            },
            'aircraft_config': {
                'type': 'blended_wing_body',
                'propulsion': 'hydrogen_fuel_cell',
                'design_range': 3000,
                'passenger_capacity': 180,
                'cruise_mach': 0.78
            },
            'design_loads': {
                'design_ultimate_load': 150000,
                'design_limit_load': 100000,
                'gust_load_factor': 2.5
            },
            'hydrogen_system': {
                'storage_pressure': 70,
                'storage_temperature': -253,
                'fuel_cell_power': 2000,
                'tank_material': 'Al-5083'
            },
            'environmental_conditions': {
                'operating_temperature': [-55, 85],
                'humidity': [0, 95],
                'altitude': [0, 45000]
            },
            'regulatory_standards': {
                'airworthiness': ['CS-25', 'FAR-25'],
                'hydrogen_safety': ['ISO-11114-4']
            },
            'physics_domains': ['structural', 'thermal', 'hydrogen', 'aerodynamic']
        }
        
        # Design inputs from configuration
        design_inputs = {
            **config['aircraft_config'],
            **config['design_loads'],
            **config['hydrogen_system'],
            **config['environmental_conditions'],
            'regulatory_standards': config['regulatory_standards']
        }
        
        # Run complete generation
        generator = UTCSMICompliantGenerator(config)
        results = generator.generate_requirements(
            design_inputs=design_inputs,
            regulatory_standards=config['regulatory_standards']['airworthiness'],
            physics_domains=config['physics_domains']
        )
        
        # Validate complete results structure
        required_keys = [
            'requirements',
            'requirements_by_domain', 
            'validation_results',
            'compliance_metadata',
            'generation_context',
            'traceability_matrix'
        ]
        
        for key in required_keys:
            assert key in results, f"Missing key in results: {key}"
        
        # Validate requirements structure
        assert len(results['requirements']) > 0, "No requirements generated"
        
        first_req = results['requirements'][0]
        required_req_fields = [
            'id', 'shall_statement', 'verification_method',
            'acceptance_criteria', 'category', 'criticality'
        ]
        
        for field in required_req_fields:
            assert field in first_req, f"Missing field in requirement: {field}"
        
        # Validate compliance metadata
        compliance = results['compliance_metadata']
        assert compliance['mi_framework'] == 'M2-MACHINE', "Wrong framework"
        assert compliance['traceability_enabled'] == True, "Traceability not enabled"
        
        # Validate traceability matrix
        matrix = results['traceability_matrix']
        assert 'requirements_count' in matrix, "Missing requirements count"
        assert matrix['requirements_count'] == len(results['requirements']), "Count mismatch"
        
        print("✓ End-to-end workflow working correctly")
        return True
        
    except Exception as e:
        print(f"✗ End-to-end test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all integration tests."""
    print("="*60)
    print("REQUIREMENTS GENERATOR INTEGRATION TESTS")
    print("="*60)
    
    tests = [
        test_basic_functionality,
        test_physics_solvers,
        test_plugin_system,
        test_error_handling,
        test_end_to_end
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        print(f"\n{test.__name__.replace('_', ' ').title()}:")
        if test():
            passed += 1
        else:
            failed += 1
    
    print("\n" + "="*60)
    print(f"TEST RESULTS: {passed} passed, {failed} failed")
    print("="*60)
    
    if failed == 0:
        print("✓ All tests passed! Requirements generator is working correctly.")
        return 0
    else:
        print("✗ Some tests failed. Please check the error messages above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
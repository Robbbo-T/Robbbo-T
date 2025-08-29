#!/usr/bin/env python3
"""
Simple test script to validate the requirements generator implementation
"""

import sys
import os
import tempfile
import json

# Add the requirements_generator to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

def test_basic_functionality():
    """Test basic requirements generator functionality"""
    print("=== Testing Basic Functionality ===")
    
    try:
        # Import modules
        from core.generator import RequirementsGenerator
        from core.types import Requirement, VerificationMethod
        from plugins.plugin_interface import PluginManager
        from plugins.validators.h2_compatibility import H2CompatibilityValidator
        print("✓ Successfully imported all modules")
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False
    
    try:
        # Initialize generator without config file
        generator = RequirementsGenerator()
        print("✓ Successfully initialized RequirementsGenerator")
    except Exception as e:
        print(f"✗ Generator initialization failed: {e}")
        return False
    
    try:
        # Test requirement generation
        template = {
            'id': 'TEST-REQ-001',
            'shall_statement': 'Test component shall meet basic requirements',
            'verification_method': 'A',
            'acceptance_criteria': {'test_param': 42},
            'tolerance': {'test_tolerance': 0.1},
            'environmental_conditions': {'temperature': 20},
            'category': 'Test',
            'criticality': 'Low'
        }
        
        req = generator.generate_requirement(template)
        print(f"✓ Successfully generated requirement: {req.id}")
        
        # Test requirement to dict conversion
        req_dict = req.to_dict()
        assert req_dict['id'] == 'TEST-REQ-001'
        print("✓ Requirement dictionary conversion works")
        
    except Exception as e:
        print(f"✗ Requirement generation failed: {e}")
        return False
    
    try:
        # Test plugin system
        plugin_manager = PluginManager()
        h2_plugin = H2CompatibilityValidator()
        plugin_manager.register_plugin(h2_plugin)
        
        plugins = plugin_manager.list_plugins()
        assert 'h2_compatibility' in plugins
        print("✓ Plugin system works")
        
    except Exception as e:
        print(f"✗ Plugin system failed: {e}")
        return False
    
    return True

def test_physics_validation():
    """Test physics validation functionality"""
    print("\n=== Testing Physics Validation ===")
    
    try:
        from core.generator import RequirementsGenerator
        from physics_solvers.multiphysics import MultiphysicsOrchestrator
        
        generator = RequirementsGenerator()
        
        # Test with hydrogen requirement
        h2_template = {
            'id': 'TEST-H2-001',
            'shall_statement': 'Hydrogen tank material shall be compatible',
            'verification_method': 'T',
            'acceptance_criteria': {
                'h2_permeation_rate': 5e-18,
                'operating_pressure': 350
            },
            'material': {'name': 'Al-5083'},
            'category': 'Hydrogen',
            'criticality': 'Critical'
        }
        
        req = generator.generate_requirement(h2_template)
        result = generator.validate_requirement(req)
        
        print(f"✓ H2 validation completed - Passed: {result.passed}")
        
        # Test with structural requirement
        struct_template = {
            'id': 'TEST-STRUCT-001',
            'shall_statement': 'Structure shall meet safety factor requirements',
            'verification_method': 'A',
            'acceptance_criteria': {
                'stress_limit': True,
                'min_safety_factor': 1.5
            },
            'material': {'name': 'Al-5083', 'yield': 250e6},
            'category': 'Structures',
            'criticality': 'High'
        }
        
        req2 = generator.generate_requirement(struct_template)
        result2 = generator.validate_requirement(req2)
        
        print(f"✓ Structural validation completed - Passed: {result2.passed}")
        
    except Exception as e:
        print(f"✗ Physics validation failed: {e}")
        return False
    
    return True

def test_export_functionality():
    """Test export functionality"""
    print("\n=== Testing Export Functionality ===")
    
    try:
        from core.generator import RequirementsGenerator
        
        generator = RequirementsGenerator()
        
        # Generate a few requirements
        templates = [
            {
                'id': 'EXPORT-TEST-001',
                'shall_statement': 'First test requirement',
                'verification_method': 'A',
                'acceptance_criteria': {},
                'tolerance': {},
                'environmental_conditions': {},
                'category': 'Test',
                'criticality': 'Low'
            },
            {
                'id': 'EXPORT-TEST-002',
                'shall_statement': 'Second test requirement',
                'verification_method': 'D',
                'acceptance_criteria': {},
                'tolerance': {},
                'environmental_conditions': {},
                'category': 'Test',
                'criticality': 'Medium'
            }
        ]
        
        requirements = generator.batch_generate(templates)
        print(f"✓ Generated {len(requirements)} requirements for export test")
        
        # Test JSON export
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json_path = f.name
        
        generator.export_requirements(json_path, 'json')
        
        # Verify the export
        with open(json_path, 'r') as f:
            exported_data = json.load(f)
        
        assert len(exported_data['requirements']) == 2
        assert exported_data['count'] == 2
        print("✓ JSON export works correctly")
        
        # Cleanup
        os.unlink(json_path)
        
    except Exception as e:
        print(f"✗ Export functionality failed: {e}")
        return False
    
    return True

def main():
    """Run all tests"""
    print("Requirements Generator Test Suite")
    print("=" * 50)
    
    tests = [
        test_basic_functionality,
        test_physics_validation,
        test_export_functionality
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        else:
            print("Test failed!")
    
    print(f"\n=== Test Results ===")
    print(f"Passed: {passed}/{total}")
    print(f"Success Rate: {passed/total*100:.1f}%")
    
    if passed == total:
        print("✓ All tests passed!")
        return 0
    else:
        print("✗ Some tests failed!")
        return 1

if __name__ == '__main__':
    sys.exit(main())
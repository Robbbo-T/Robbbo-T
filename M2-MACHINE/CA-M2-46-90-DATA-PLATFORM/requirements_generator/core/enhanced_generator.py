from typing import Dict, Any, List
from core.generator import EnhancedRequirementGenerator
from physics_solvers.multiphysics import MultiphysicsOrchestrator
from error_handling.traceable_errors import ErrorReporter
from plugins.plugin_interface import PluginManager

class EnhancedRequirementGenerator(EnhancedRequirementGenerator):
    """
    Enhanced requirements generator with full physics simulation,
    error tracking, and plugin validation capabilities.
    """
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.multiphysics = MultiphysicsOrchestrator()
        self.error_reporter = ErrorReporter(config.get('error_output_dir', 'errors'))
        self.plugin_manager = PluginManager(config.get('plugin_dirs', ['plugins/validators']))
    
    def generate_with_full_validation(self, 
                                    design_inputs: Dict[str, Any],
                                    enable_physics: bool = True,
                                    enable_plugins: bool = True) -> Dict[str, Any]:
        """
        Generate requirements with comprehensive validation including:
        - Physics-based validation using multiphysics solvers
        - Plugin-based validation for specialized checks
        - Comprehensive error tracking and reporting
        """
        
        # Generate base requirements using UTCS MI generator
        result = self.utcs_generator.generate_requirements(
            design_inputs=design_inputs,
            regulatory_standards=self.config.get('regulatory_standards', []),
            physics_domains=self.config.get('physics_domains', [])
        )
        
        # Enhanced physics validation if enabled
        if enable_physics:
            enhanced_physics_results = {}
            for req_dict in result['requirements']:
                try:
                    # Run detailed multiphysics validation
                    physics_result = self.multiphysics.validate_coupled({
                        **req_dict,
                        **design_inputs,
                        'physics_domains': self.config.get('physics_domains', [])
                    })
                    enhanced_physics_results[req_dict['id']] = physics_result
                except Exception as e:
                    error = self.error_reporter.log_error(e)
                    enhanced_physics_results[req_dict['id']] = {
                        'error': str(e),
                        'error_id': error.get('error_id'),
                        'overall_passed': False
                    }
            
            result['enhanced_physics_validation'] = enhanced_physics_results
        
        # Enhanced plugin validation if enabled
        if enable_plugins:
            enhanced_plugin_results = {}
            for req_dict in result['requirements']:
                try:
                    plugin_results = self.plugin_manager.validate_requirement(req_dict)
                    enhanced_plugin_results[req_dict['id']] = {
                        'results': [r.__dict__ for r in plugin_results],
                        'passed': all(r.passed for r in plugin_results),
                        'plugin_count': len(plugin_results)
                    }
                except Exception as e:
                    error = self.error_reporter.log_error(e)
                    enhanced_plugin_results[req_dict['id']] = {
                        'error': str(e),
                        'error_id': error.get('error_id'),
                        'passed': False
                    }
            
            result['enhanced_plugin_validation'] = enhanced_plugin_results
        
        # Add comprehensive error reporting
        result['error_analysis'] = {
            'total_errors': len(self.error_reporter.errors),
            'total_warnings': len(self.error_reporter.warnings),
            'error_report': self.error_reporter.generate_report(),
            'plugin_summary': self.plugin_manager.get_plugin_summary()
        }
        
        # Add validation summary
        physics_passed = all(
            v.get('overall_passed', True) 
            for v in result.get('enhanced_physics_validation', {}).values()
        )
        plugins_passed = all(
            v.get('passed', True) 
            for v in result.get('enhanced_plugin_validation', {}).values()
        )
        
        result['validation_summary'] = {
            'physics_validation_passed': physics_passed,
            'plugin_validation_passed': plugins_passed,
            'overall_validation_passed': physics_passed and plugins_passed,
            'requirements_generated': len(result['requirements']),
            'physics_domains_validated': len(set(self.config.get('physics_domains', []))),
            'plugins_executed': len(self.plugin_manager.plugins)
        }
        
        return result
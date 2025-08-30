from typing import Dict, Any, List, Type
from importlib import import_module
from pathlib import Path
import inspect
import sys
from core.types import ValidationResult

class RequirementValidatorPlugin:
    """Base class for requirement validation plugins."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.name = self.__class__.__name__
    
    def validate(self, requirement: Dict[str, Any]) -> ValidationResult:
        """Validate a requirement. Must be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement validate method")
    
    def get_requirements(self) -> List[str]:
        """Return list of requirement fields this plugin needs."""
        return []

class PluginManager:
    """Manages loading and execution of validation plugins."""
    
    def __init__(self, plugin_dirs: List[str] = None):
        self.plugin_dirs = plugin_dirs or ["plugins/validators"]
        self.plugins: Dict[str, RequirementValidatorPlugin] = {}
        self._load_plugins()
    
    def _load_plugins(self):
        """Discover and load all validation plugins."""
        for plugin_dir in self.plugin_dirs:
            plugin_path = Path(plugin_dir)
            if not plugin_path.exists():
                continue
                
            # Add plugin directory to Python path
            if str(plugin_path.parent) not in sys.path:
                sys.path.insert(0, str(plugin_path.parent))
            
            # Load all Python files in plugin directory
            for py_file in plugin_path.glob("*.py"):
                if py_file.name.startswith("__"):
                    continue
                    
                module_name = f"{plugin_path.name}.{py_file.stem}"
                try:
                    module = import_module(module_name)
                    self._register_plugin_classes(module)
                except ImportError as e:
                    print(f"Failed to load plugin {module_name}: {e}")
    
    def _register_plugin_classes(self, module):
        """Register plugin classes from a module."""
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if (issubclass(obj, RequirementValidatorPlugin) and 
                obj != RequirementValidatorPlugin):
                # Create instance with empty config for now
                plugin_instance = obj({})
                self.plugins[plugin_instance.name] = plugin_instance
    
    def register_plugin(self, plugin: RequirementValidatorPlugin):
        """Manually register a plugin instance."""
        self.plugins[plugin.name] = plugin
    
    def validate_requirement(self, requirement: Dict[str, Any]) -> List[ValidationResult]:
        """Run all applicable plugins on a requirement."""
        results = []
        
        for plugin_name, plugin in self.plugins.items():
            try:
                result = plugin.validate(requirement)
                results.append(result)
            except Exception as e:
                error_result = ValidationResult(
                    passed=False,
                    plugin=plugin_name,
                    error=f"Plugin error: {str(e)}"
                )
                results.append(error_result)
        
        return results
    
    def get_plugin_summary(self) -> Dict[str, Any]:
        """Get summary of loaded plugins."""
        return {
            'loaded_plugins': list(self.plugins.keys()),
            'plugin_count': len(self.plugins),
            'plugin_details': {
                name: {
                    'class': plugin.__class__.__name__,
                    'requirements': plugin.get_requirements()
                }
                for name, plugin in self.plugins.items()
            }
        }
# plugins/plugin_interface.py
from abc import ABC, abstractmethod
from typing import Dict, Any, List
try:
    from ..core.types import ValidationResult
except ImportError:
    import sys
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    sys.path.insert(0, parent_dir)
    from core.types import ValidationResult

class ValidationPlugin(ABC):
    """Base interface for validation plugins"""
    
    @abstractmethod
    def get_name(self) -> str:
        """Return plugin name"""
        pass
    
    @abstractmethod
    def get_version(self) -> str:
        """Return plugin version"""
        pass
    
    @abstractmethod
    def validate(self, requirement: Dict[str, Any]) -> ValidationResult:
        """Validate requirement and return result"""
        pass
    
    @abstractmethod
    def get_supported_categories(self) -> List[str]:
        """Return list of requirement categories this plugin supports"""
        pass

class PluginManager:
    """Manage and orchestrate validation plugins"""
    
    def __init__(self):
        self.plugins: Dict[str, ValidationPlugin] = {}
        self.category_map: Dict[str, List[str]] = {}
    
    def register_plugin(self, plugin: ValidationPlugin) -> None:
        """Register a validation plugin"""
        name = plugin.get_name()
        self.plugins[name] = plugin
        
        # Update category mapping
        for category in plugin.get_supported_categories():
            if category not in self.category_map:
                self.category_map[category] = []
            self.category_map[category].append(name)
    
    def get_plugins_for_category(self, category: str) -> List[ValidationPlugin]:
        """Get all plugins that support a given category"""
        plugin_names = self.category_map.get(category, [])
        return [self.plugins[name] for name in plugin_names]
    
    def validate_with_plugins(self, requirement: Dict[str, Any]) -> List[ValidationResult]:
        """Run all applicable plugins on a requirement"""
        category = requirement.get('category', 'General')
        applicable_plugins = self.get_plugins_for_category(category)
        
        results = []
        for plugin in applicable_plugins:
            try:
                result = plugin.validate(requirement)
                results.append(result)
            except Exception as e:
                results.append(ValidationResult(
                    passed=False,
                    plugin=plugin.get_name(),
                    error=f"Plugin execution failed: {str(e)}"
                ))
        
        return results
    
    def list_plugins(self) -> Dict[str, Dict[str, Any]]:
        """List all registered plugins with their info"""
        return {
            name: {
                'version': plugin.get_version(),
                'categories': plugin.get_supported_categories()
            }
            for name, plugin in self.plugins.items()
        }
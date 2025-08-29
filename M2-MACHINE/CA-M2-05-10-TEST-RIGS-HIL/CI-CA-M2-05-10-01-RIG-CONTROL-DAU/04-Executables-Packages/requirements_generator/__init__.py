"""
AMPEL360 H₂-BWB-Q Requirements Generator

Engineering automation tool for requirements generation with integrated physics solver validation.
Classified as M2 (automation system) with capability for physics-based constraint validation.
"""

__version__ = "1.0.0"
__author__ = "AMPEL360 Engineering Team"
__description__ = "Requirements generator with physics solver integration for H2-BWB-Q aircraft"

from .core.generator import RequirementsGenerator
from .core.types import Requirement, ValidationResult, VerificationMethod
from .physics_solvers.multiphysics import MultiphysicsOrchestrator
from .plugins.plugin_interface import PluginManager
from .error_handling.traceable_errors import ErrorReporter

__all__ = [
    'RequirementsGenerator',
    'Requirement', 
    'ValidationResult',
    'VerificationMethod',
    'MultiphysicsOrchestrator',
    'PluginManager',
    'ErrorReporter'
]
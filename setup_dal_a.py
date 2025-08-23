#!/usr/bin/env python3
"""
DAL-A Software Subsystem Installation and Setup
===============================================

Installation script for the AMEDEO DAL-A software subsystem.
Ensures proper Python environment and dependency installation.
"""

import subprocess
import sys
import os
from pathlib import Path


def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("ERROR: Python 3.7 or higher is required")
        return False
    print(f"✓ Python version: {sys.version}")
    return True


def install_dependencies():
    """Install required dependencies"""
    requirements_file = Path(__file__).parent / "requirements-dal-a.txt"
    
    if not requirements_file.exists():
        print("ERROR: requirements-dal-a.txt not found")
        return False
    
    try:
        print("Installing DAL-A subsystem dependencies...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", str(requirements_file)
        ])
        print("✓ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Failed to install dependencies: {e}")
        return False


def setup_pythonpath():
    """Set up Python path for the DAL-A subsystem"""
    src_path = Path(__file__).parent / "src"
    if src_path.exists():
        # Add to PYTHONPATH
        current_path = os.environ.get("PYTHONPATH", "")
        if str(src_path) not in current_path:
            new_path = f"{src_path}:{current_path}" if current_path else str(src_path)
            os.environ["PYTHONPATH"] = new_path
            print(f"✓ Added {src_path} to PYTHONPATH")
        return True
    else:
        print("ERROR: src directory not found")
        return False


def run_basic_validation():
    """Run basic validation of the subsystem"""
    try:
        # Try to import main modules
        sys.path.insert(0, str(Path(__file__).parent / "src"))
        
        from dal_a_subsystem.kernel.partition_manager import PartitionManager
        from dal_a_subsystem.safety.voting_system import TwoOfThreeVoting
        from dal_a_subsystem.security.cross_domain_validator import CrossDomainValidator
        
        print("✓ Core modules imported successfully")
        
        # Basic instantiation test
        pm = PartitionManager()
        voting = TwoOfThreeVoting("test")
        validator = CrossDomainValidator()
        
        print("✓ Core components instantiated successfully")
        return True
        
    except ImportError as e:
        print(f"ERROR: Failed to import modules: {e}")
        return False
    except Exception as e:
        print(f"ERROR: Validation failed: {e}")
        return False


def main():
    """Main setup function"""
    print("=" * 60)
    print("AMEDEO DAL-A Software Subsystem Setup")
    print("=" * 60)
    
    success = True
    
    # Check Python version
    if not check_python_version():
        success = False
    
    # Install dependencies
    if success and not install_dependencies():
        success = False
    
    # Setup Python path
    if success and not setup_pythonpath():
        success = False
    
    # Run validation
    if success and not run_basic_validation():
        success = False
    
    print("=" * 60)
    if success:
        print("✓ DAL-A Software Subsystem setup completed successfully!")
        print("\nTo run tests:")
        print("  cd src/dal-a-subsystem/tests")
        print("  python test_dal_a_subsystem.py")
    else:
        print("✗ Setup failed. Please check the errors above.")
    print("=" * 60)
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
#!/usr/bin/env python3
"""
Link and Path Validator - FCR-1 Gate

Validates that all file paths and links in the repository are correct and accessible.
Part of the CI gate system for ROBBBO-T project.

Usage:
    python link_path_validator.py --check-all
    python link_path_validator.py --files file1.md file2.py
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import List, Tuple, Set


class PathValidator:
    """Validates paths and links in repository files"""
    
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.errors: List[str] = []
        self.warnings: List[str] = []
        
    def validate_file_exists(self, file_path: Path) -> bool:
        """Check if a file exists"""
        if not file_path.exists():
            self.errors.append(f"File does not exist: {file_path}")
            return False
        return True
    
    def validate_markdown_links(self, md_file: Path) -> None:
        """Validate all links in a markdown file"""
        if not md_file.exists():
            return
            
        content = md_file.read_text(encoding='utf-8')
        
        # Find markdown links [text](path)
        link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
        links = re.findall(link_pattern, content)
        
        for text, link in links:
            # Skip external URLs
            if link.startswith(('http://', 'https://', 'mailto:', 'ftp://')):
                continue
            
            # Skip anchors only
            if link.startswith('#'):
                continue
            
            # Handle links with anchors
            if '#' in link:
                link_path, anchor = link.split('#', 1)
                if not link_path:  # Just an anchor
                    continue
                link = link_path
            
            # Resolve relative path
            if link.startswith('/'):
                target = self.repo_root / link.lstrip('/')
            else:
                target = (md_file.parent / link).resolve()
            
            # Check if target exists
            if not target.exists():
                self.errors.append(
                    f"Broken link in {md_file.relative_to(self.repo_root)}: "
                    f"'{link}' -> {target} not found"
                )
    
    def validate_directory_structure(self, file_path: Path) -> None:
        """Validate directory structure follows canon"""
        rel_path = file_path.relative_to(self.repo_root)
        path_parts = rel_path.parts
        
        # Check for invalid characters
        for part in path_parts:
            if ' ' in part:
                self.errors.append(f"Path contains spaces: {rel_path}")
            if part != part.lower() and not part.startswith('.'):
                self.warnings.append(f"Path contains uppercase: {rel_path}")
        
        # Check TFA order in products
        if len(path_parts) >= 3 and path_parts[0] == 'products':
            tfa_layers = ['QS', 'FWD', 'UE', 'FE', 'CB', 'QB']
            if any(layer in path_parts for layer in tfa_layers):
                # Verify it's in a product directory
                if path_parts[1] not in ['ampel360-t-air', 'ampel360-t-space']:
                    self.warnings.append(
                        f"TFA layer found outside standard products: {rel_path}"
                    )
    
    def validate_python_imports(self, py_file: Path) -> None:
        """Validate Python imports reference existing modules"""
        if not py_file.exists():
            return
            
        content = py_file.read_text(encoding='utf-8')
        
        # Find relative imports
        import_pattern = r'from \.([\w.]+) import'
        relative_imports = re.findall(import_pattern, content)
        
        for imp in relative_imports:
            # Convert import path to file path
            parts = imp.split('.')
            module_path = py_file.parent
            for part in parts:
                module_path = module_path / part
            
            # Check if module exists (as .py file or directory with __init__.py)
            if not (module_path.with_suffix('.py').exists() or 
                    (module_path / '__init__.py').exists()):
                self.errors.append(
                    f"Import not found in {py_file.relative_to(self.repo_root)}: "
                    f"from .{imp}"
                )
    
    def validate_files(self, files: List[Path]) -> bool:
        """Validate a list of files"""
        for file_path in files:
            if not file_path.exists():
                self.errors.append(f"File not found: {file_path}")
                continue
            
            # Validate based on file type
            if file_path.suffix == '.md':
                self.validate_markdown_links(file_path)
            elif file_path.suffix == '.py':
                self.validate_python_imports(file_path)
            
            # Always validate directory structure
            self.validate_directory_structure(file_path)
        
        return len(self.errors) == 0
    
    def validate_all(self) -> bool:
        """Validate all files in repository"""
        all_files = []
        
        # Find all markdown and python files
        for pattern in ['**/*.md', '**/*.py']:
            all_files.extend(self.repo_root.glob(pattern))
        
        # Filter out .git directory
        all_files = [f for f in all_files if '.git' not in f.parts]
        
        return self.validate_files(all_files)
    
    def print_results(self) -> None:
        """Print validation results"""
        if self.errors:
            print("\n❌ ERRORS:")
            for error in self.errors:
                print(f"  - {error}")
        
        if self.warnings:
            print("\n⚠️  WARNINGS:")
            for warning in self.warnings:
                print(f"  - {warning}")
        
        if not self.errors and not self.warnings:
            print("\n✅ All validations passed!")
        
        print(f"\nSummary: {len(self.errors)} errors, {len(self.warnings)} warnings")


def main():
    parser = argparse.ArgumentParser(
        description='Validate file paths and links in repository'
    )
    parser.add_argument(
        '--check-all',
        action='store_true',
        help='Check all files in repository'
    )
    parser.add_argument(
        '--files',
        nargs='+',
        help='Specific files to check'
    )
    
    args = parser.parse_args()
    
    # Determine repository root
    repo_root = Path(__file__).parent.parent.parent
    
    validator = PathValidator(repo_root)
    
    if args.check_all:
        print("🔍 Validating all files in repository...")
        success = validator.validate_all()
    elif args.files:
        print(f"🔍 Validating {len(args.files)} files...")
        files = [Path(f) for f in args.files]
        success = validator.validate_files(files)
    else:
        parser.print_help()
        return 1
    
    validator.print_results()
    
    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())

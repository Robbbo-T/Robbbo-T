#!/usr/bin/env python3
"""
FCR Enforcer - FCR-2 Gate

Enforces Follow-up Chain Rules for TFA order and UTCS traceability.
Part of the CI gate system for ROBBBO-T project.

Usage:
    python fcr_enforcer.py --pr-title "FWD/update-geometry" --files-changed "products/ampel360-t-air/FWD/**"
"""

import argparse
import os
import re
import sys
import yaml
from pathlib import Path
from typing import List, Dict, Optional, Set


class FCREnforcer:
    """Enforces Follow-up Chain Rules for TFA and UTCS"""
    
    TFA_LAYERS = ['QS', 'FWD', 'UE', 'FE', 'CB', 'QB']
    TFA_ORDER = {layer: i for i, layer in enumerate(TFA_LAYERS)}
    
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.errors: List[str] = []
        self.warnings: List[str] = []
    
    def extract_tfa_layer_from_title(self, pr_title: str) -> Optional[str]:
        """Extract TFA layer from PR title prefix"""
        pattern = r'^(QS|FWD|UE|FE|CB|QB|GOV|CI)/'
        match = re.match(pattern, pr_title)
        if match:
            layer = match.group(1)
            if layer in self.TFA_LAYERS:
                return layer
        return None
    
    def extract_tfa_layers_from_files(self, files: List[Path]) -> Set[str]:
        """Extract TFA layers from file paths"""
        layers = set()
        for file_path in files:
            for layer in self.TFA_LAYERS:
                if f'/{layer}/' in str(file_path) or str(file_path).endswith(f'/{layer}'):
                    layers.add(layer)
        return layers
    
    def validate_tfa_prefix(self, pr_title: str, files: List[Path]) -> bool:
        """Validate PR title prefix matches changed files"""
        declared_layer = self.extract_tfa_layer_from_title(pr_title)
        file_layers = self.extract_tfa_layers_from_files(files)
        
        if not declared_layer:
            # Check if files contain TFA layers
            if file_layers:
                self.errors.append(
                    f"PR title missing TFA prefix but files modified in layers: {file_layers}"
                )
                return False
            else:
                # Non-TFA change (GOV, CI, docs, etc.)
                return True
        
        # Validate declared layer matches file layers
        if file_layers and declared_layer not in file_layers:
            self.errors.append(
                f"PR title declares '{declared_layer}/' but files modified in: {file_layers}"
            )
            return False
        
        return True
    
    def extract_utcs_metadata(self, file_path: Path) -> Optional[Dict]:
        """Extract UTCS metadata from file"""
        if not file_path.exists():
            return None
        
        content = file_path.read_text(encoding='utf-8')
        
        # Try to extract YAML frontmatter for markdown
        if file_path.suffix == '.md':
            frontmatter_pattern = r'^---\s*\n(.*?)\n---'
            match = re.match(frontmatter_pattern, content, re.DOTALL)
            if match:
                try:
                    metadata = yaml.safe_load(match.group(1))
                    return metadata.get('utcs')
                except yaml.YAMLError:
                    pass
        
        # Try to extract from Python docstring
        elif file_path.suffix == '.py':
            docstring_pattern = r'"""\s*\nUTCS:\s*\n(.*?)\n"""'
            match = re.search(docstring_pattern, content, re.DOTALL)
            if match:
                try:
                    # Parse YAML-like structure in docstring
                    utcs_text = match.group(1)
                    # Simple key-value extraction
                    utcs_data = {}
                    for line in utcs_text.split('\n'):
                        if ':' in line:
                            key, value = line.split(':', 1)
                            utcs_data[key.strip()] = value.strip()
                    if utcs_data:
                        return utcs_data
                except Exception:
                    pass
        
        return None
    
    def validate_utcs_metadata(self, file_path: Path) -> bool:
        """Validate UTCS metadata is complete"""
        required_fields = ['context', 'content', 'cache', 'structure', 'style', 'sheet']
        
        metadata = self.extract_utcs_metadata(file_path)
        
        if metadata is None:
            # Only warn for new/modified files in products/
            if 'products/' in str(file_path):
                self.warnings.append(
                    f"Missing UTCS metadata in {file_path.relative_to(self.repo_root)}"
                )
            return True  # Don't fail, just warn
        
        # Check required fields
        missing_fields = [f for f in required_fields if f not in metadata]
        if missing_fields:
            self.warnings.append(
                f"Incomplete UTCS metadata in {file_path.relative_to(self.repo_root)}: "
                f"missing {missing_fields}"
            )
        
        return True
    
    def validate_tfa_order(self, product_path: Path, target_layer: str) -> bool:
        """Validate that previous TFA layers exist"""
        target_index = self.TFA_ORDER.get(target_layer)
        if target_index is None:
            return True
        
        # Check that all previous layers have at least a README
        for i in range(target_index):
            prev_layer = self.TFA_LAYERS[i]
            prev_layer_path = product_path / prev_layer
            
            # Check if directory exists and has content
            if not prev_layer_path.exists():
                self.errors.append(
                    f"Cannot work on {target_layer} before {prev_layer} exists in "
                    f"{product_path.relative_to(self.repo_root)}"
                )
                return False
        
        return True
    
    def validate_files(self, pr_title: str, files: List[Path]) -> bool:
        """Validate all FCR rules for given files"""
        # 1. Validate TFA prefix
        if not self.validate_tfa_prefix(pr_title, files):
            return False
        
        # 2. Extract declared layer
        declared_layer = self.extract_tfa_layer_from_title(pr_title)
        
        # 3. Validate each file
        for file_path in files:
            # Validate UTCS metadata
            self.validate_utcs_metadata(file_path)
            
            # Validate TFA order for product files
            if 'products/' in str(file_path) and declared_layer:
                # Find product root
                parts = file_path.relative_to(self.repo_root).parts
                if len(parts) >= 2 and parts[0] == 'products':
                    product_path = self.repo_root / 'products' / parts[1]
                    self.validate_tfa_order(product_path, declared_layer)
        
        return len(self.errors) == 0
    
    def print_results(self) -> None:
        """Print validation results"""
        if self.errors:
            print("\n❌ FCR-2 ERRORS:")
            for error in self.errors:
                print(f"  - {error}")
        
        if self.warnings:
            print("\n⚠️  FCR-2 WARNINGS:")
            for warning in self.warnings:
                print(f"  - {warning}")
        
        if not self.errors and not self.warnings:
            print("\n✅ All FCR-2 validations passed!")
        
        print(f"\nSummary: {len(self.errors)} errors, {len(self.warnings)} warnings")


def main():
    parser = argparse.ArgumentParser(
        description='Enforce Follow-up Chain Rules for TFA and UTCS'
    )
    parser.add_argument(
        '--pr-title',
        required=True,
        help='PR title with TFA prefix (e.g., "FWD/update-geometry")'
    )
    parser.add_argument(
        '--files-changed',
        nargs='+',
        required=True,
        help='List of changed files'
    )
    
    args = parser.parse_args()
    
    # Determine repository root
    repo_root = Path(__file__).parent.parent.parent
    
    enforcer = FCREnforcer(repo_root)
    
    # Convert file patterns to paths
    files = []
    for pattern in args.files_changed:
        if '*' in pattern:
            # Handle glob patterns
            files.extend(repo_root.glob(pattern))
        else:
            # Convert to absolute path if relative
            file_path = Path(pattern)
            if not file_path.is_absolute():
                file_path = repo_root / file_path
            files.append(file_path)
    
    print(f"🔍 Validating FCR-2 for PR: {args.pr_title}")
    print(f"📁 Checking {len(files)} files...")
    
    success = enforcer.validate_files(args.pr_title, files)
    
    enforcer.print_results()
    
    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""
RTX CLI - ROBBBO-T eXtended CLI Tool

CLI para crear estructuras TFA (QS→FWD→UE→FE→CB→QB) y gestionar el repositorio.

Usage:
    rtx.py init-product <product-name>
    rtx.py add-tfa-layer <product-name> <layer>
    rtx.py validate
    rtx.py status
"""

import argparse
import os
import sys
from pathlib import Path
from datetime import datetime


class RTX:
    """ROBBBO-T eXtended CLI"""
    
    TFA_LAYERS = ['QS', 'FWD', 'UE', 'FE', 'CB', 'QB']
    
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.products_dir = repo_root / 'products'
    
    def init_product(self, product_name: str) -> bool:
        """Initialize a new product with TFA structure"""
        print(f"🚀 Initializing product: {product_name}")
        
        product_path = self.products_dir / product_name
        
        if product_path.exists():
            print(f"❌ Product '{product_name}' already exists!")
            return False
        
        # Create product directory
        product_path.mkdir(parents=True, exist_ok=True)
        print(f"✅ Created: {product_path.relative_to(self.repo_root)}")
        
        # Create TFA layer directories
        for layer in self.TFA_LAYERS:
            layer_path = product_path / layer
            layer_path.mkdir(exist_ok=True)
            
            # Create README in each layer
            readme_path = layer_path / 'README.md'
            self._create_layer_readme(readme_path, product_name, layer)
            print(f"✅ Created: {layer_path.relative_to(self.repo_root)}")
        
        # Create product README
        product_readme = product_path / 'README.md'
        self._create_product_readme(product_readme, product_name)
        print(f"✅ Created: {product_readme.relative_to(self.repo_root)}")
        
        print(f"\n🎉 Product '{product_name}' initialized successfully!")
        print(f"📁 Location: {product_path.relative_to(self.repo_root)}")
        print(f"📂 TFA layers: {', '.join(self.TFA_LAYERS)}")
        
        return True
    
    def add_tfa_layer(self, product_name: str, layer: str) -> bool:
        """Add or reinitialize a TFA layer for a product"""
        if layer not in self.TFA_LAYERS:
            print(f"❌ Invalid layer '{layer}'. Must be one of: {', '.join(self.TFA_LAYERS)}")
            return False
        
        product_path = self.products_dir / product_name
        if not product_path.exists():
            print(f"❌ Product '{product_name}' does not exist!")
            print(f"💡 Use: rtx.py init-product {product_name}")
            return False
        
        layer_path = product_path / layer
        layer_path.mkdir(exist_ok=True)
        
        readme_path = layer_path / 'README.md'
        if readme_path.exists():
            print(f"⚠️  {layer} already exists. Updating README...")
        
        self._create_layer_readme(readme_path, product_name, layer)
        print(f"✅ Layer '{layer}' ready: {layer_path.relative_to(self.repo_root)}")
        
        return True
    
    def validate(self) -> bool:
        """Validate repository structure and UTCS"""
        print("🔍 Validating repository structure...")
        
        errors = []
        warnings = []
        
        # Check canon directory
        canon_dir = self.repo_root / 'canon'
        if not canon_dir.exists():
            errors.append("Missing: canon/ directory")
        else:
            required_files = ['GENESIS_ASI-T2.md', 'CANON_FACTS.md', 'INJECTION_PROMPT_v1.md']
            for file in required_files:
                if not (canon_dir / file).exists():
                    errors.append(f"Missing: canon/{file}")
        
        # Check products
        if not self.products_dir.exists():
            errors.append("Missing: products/ directory")
        else:
            for product in self.products_dir.iterdir():
                if product.is_dir() and product.name not in ['.git', '__pycache__']:
                    # Check TFA layers
                    for layer in self.TFA_LAYERS:
                        layer_path = product / layer
                        if not layer_path.exists():
                            warnings.append(f"Missing TFA layer: {product.name}/{layer}")
        
        # Print results
        if errors:
            print("\n❌ ERRORS:")
            for error in errors:
                print(f"  - {error}")
        
        if warnings:
            print("\n⚠️  WARNINGS:")
            for warning in warnings:
                print(f"  - {warning}")
        
        if not errors and not warnings:
            print("\n✅ Repository structure is valid!")
            return True
        
        return len(errors) == 0
    
    def status(self) -> None:
        """Show repository status"""
        print("📊 Repository Status\n")
        
        # Canon files
        print("📜 Canon:")
        canon_dir = self.repo_root / 'canon'
        if canon_dir.exists():
            for file in canon_dir.glob('*.md'):
                print(f"  ✅ {file.name}")
        else:
            print("  ❌ canon/ not found")
        
        # Products
        print("\n🏭 Products:")
        if self.products_dir.exists():
            for product in sorted(self.products_dir.iterdir()):
                if product.is_dir() and product.name not in ['.git', '__pycache__']:
                    layers_exist = [layer for layer in self.TFA_LAYERS if (product / layer).exists()]
                    completion = len(layers_exist) / len(self.TFA_LAYERS) * 100
                    print(f"  📦 {product.name}: {completion:.0f}% complete ({len(layers_exist)}/{len(self.TFA_LAYERS)} layers)")
        else:
            print("  ❌ products/ not found")
        
        # CI gates
        print("\n🚦 CI Gates:")
        ci_gates_dir = self.repo_root / 'ci' / 'gates'
        if ci_gates_dir.exists():
            for file in ['link_path_validator.py', 'fcr_enforcer.py']:
                if (ci_gates_dir / file).exists():
                    print(f"  ✅ {file}")
                else:
                    print(f"  ❌ {file}")
        else:
            print("  ❌ ci/gates/ not found")
    
    def _create_layer_readme(self, path: Path, product_name: str, layer: str) -> None:
        """Create README for a TFA layer"""
        layer_descriptions = {
            'QS': 'Quantum Seal - Requirements, sizing, KPIs, mission planning',
            'FWD': 'Forward Design - Aerodynamics, structures, integration',
            'UE': 'User Experience - Human factors, cabin, HMI',
            'FE': 'Final Engineering - Propulsion, systems, avionics',
            'CB': 'Certification Basis - Regulatory, compliance, safety cases',
            'QB': 'Quality Baseline - Testing, validation, flight test'
        }
        
        content = f"""# {layer} - {layer_descriptions.get(layer, 'TFA Layer')}

## Product: {product_name}

---

## Overview

This directory contains all deliverables for the **{layer}** phase of the TFA flow.

**TFA Flow Position**: `{'→'.join(self.TFA_LAYERS[:self.TFA_LAYERS.index(layer)])}` → **{layer}** → `{'→'.join(self.TFA_LAYERS[self.TFA_LAYERS.index(layer)+1:])}`

---

## Objectives

{self._get_layer_objectives(layer)}

---

## Deliverables

[List key deliverables for this layer]

- [ ] Deliverable 1
- [ ] Deliverable 2
- [ ] Deliverable 3

---

## Dependencies

### Upstream (Required)
{self._get_upstream_dependencies(layer)}

### Downstream (Feeds into)
{self._get_downstream_dependencies(layer)}

---

## UTCS Metadata

```yaml
utcs:
  context: "{product_name} / {layer}"
  content: "TFA layer {layer} for {product_name}"
  cache: "refs: {self._get_layer_refs(layer)}"
  structure: "TFA canonical structure"
  style: "Engineering documentation"
  sheet:
    id: "{layer}-{product_name.upper()}-000"
    version: "0.1"
    date: "{datetime.now().strftime('%Y-%m-%d')}"
```

---

## Status

- **TRL**: [X]
- **Completion**: [0%]
- **Next Milestone**: [Define first milestone]

---

**Created**: {datetime.now().strftime('%Y-%m-%d')}  
**Last Updated**: {datetime.now().strftime('%Y-%m-%d')}
"""
        path.write_text(content)
    
    def _create_product_readme(self, path: Path, product_name: str) -> None:
        """Create main README for product"""
        content = f"""# {product_name}

## Product Overview

[Add product description here]

---

## TFA Structure

This product follows the canonical TFA flow:

```
QS → FWD → UE → FE → CB → QB
```

### Layers

- **[QS](QS/)**: Quantum Seal - Requirements & sizing
- **[FWD](FWD/)**: Forward Design - Aerodynamics & structures
- **[UE](UE/)**: User Experience - Human factors
- **[FE](FE/)**: Final Engineering - Systems integration
- **[CB](CB/)**: Certification Basis - Regulatory compliance
- **[QB](QB/)**: Quality Baseline - Testing & validation

---

## Status

- **TRL**: [X]
- **Phase**: [Planning / Development / Testing]
- **Next Milestone**: [Define]

---

## UTCS Metadata

```yaml
utcs:
  context: "Product / {product_name}"
  content: "[Product description]"
  cache: "refs: /canon/, /governance/"
  structure: "TFA flow (QS→FWD→UE→FE→CB→QB)"
  style: "Product documentation"
  sheet:
    id: "PRODUCT-{product_name.upper()}-000"
    version: "0.1"
    date: "{datetime.now().strftime('%Y-%m-%d')}"
```

---

**Created**: {datetime.now().strftime('%Y-%m-%d')}
"""
        path.write_text(content)
    
    def _get_layer_objectives(self, layer: str) -> str:
        objectives = {
            'QS': '- Define system requirements and constraints\n- Size critical components\n- Establish KPIs and success metrics\n- Plan missions and scenarios',
            'FWD': '- Design aerodynamic configuration\n- Design structures and materials\n- Integrate critical systems (e.g., H₂ tanks)\n- Define mass and balance',
            'UE': '- Design crew and passenger experience\n- Define HMI and interfaces\n- Plan emergency procedures\n- Ensure ergonomics and accessibility',
            'FE': '- Integrate propulsion systems\n- Design avionics and control\n- Define thermal management\n- Establish power distribution',
            'CB': '- Identify applicable regulations\n- Define compliance approach\n- Develop safety cases\n- Coordinate with authorities',
            'QB': '- Plan testing campaign\n- Execute ground and flight tests\n- Validate requirements\n- Demonstrate compliance'
        }
        return objectives.get(layer, '- [Define objectives]')
    
    def _get_upstream_dependencies(self, layer: str) -> str:
        idx = self.TFA_LAYERS.index(layer)
        if idx == 0:
            return '- `/canon/`: Canon documents (GENESIS, CANON_FACTS)'
        prev_layers = self.TFA_LAYERS[:idx]
        return '\n'.join([f'- `../{l}/`: {l} layer must be complete' for l in prev_layers])
    
    def _get_downstream_dependencies(self, layer: str) -> str:
        idx = self.TFA_LAYERS.index(layer)
        if idx == len(self.TFA_LAYERS) - 1:
            return '- End of TFA flow'
        next_layers = self.TFA_LAYERS[idx+1:]
        return '\n'.join([f'- `../{l}/`: Feeds requirements and design to {l}' for l in next_layers[:2]])
    
    def _get_layer_refs(self, layer: str) -> str:
        refs = {
            'QS': '/canon/, /governance/UTCS/',
            'FWD': '../QS/, /cax/',
            'UE': '../QS/, ../FWD/',
            'FE': '../FWD/, ../UE/',
            'CB': '../FE/, /governance/COMPLIANCE/',
            'QB': '../CB/, /qox/'
        }
        return refs.get(layer, '../')


def main():
    parser = argparse.ArgumentParser(
        description='RTX - ROBBBO-T eXtended CLI Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  rtx.py init-product ampel360-t-cargo
  rtx.py add-tfa-layer ampel360-t-air QS
  rtx.py validate
  rtx.py status
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # init-product
    init_parser = subparsers.add_parser('init-product', help='Initialize new product')
    init_parser.add_argument('product_name', help='Product name (e.g., ampel360-t-cargo)')
    
    # add-tfa-layer
    add_parser = subparsers.add_parser('add-tfa-layer', help='Add TFA layer to product')
    add_parser.add_argument('product_name', help='Product name')
    add_parser.add_argument('layer', help='TFA layer (QS/FWD/UE/FE/CB/QB)')
    
    # validate
    subparsers.add_parser('validate', help='Validate repository structure')
    
    # status
    subparsers.add_parser('status', help='Show repository status')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    # Determine repository root
    repo_root = Path(__file__).parent.parent.parent
    rtx = RTX(repo_root)
    
    # Execute command
    if args.command == 'init-product':
        success = rtx.init_product(args.product_name)
        return 0 if success else 1
    
    elif args.command == 'add-tfa-layer':
        success = rtx.add_tfa_layer(args.product_name, args.layer)
        return 0 if success else 1
    
    elif args.command == 'validate':
        success = rtx.validate()
        return 0 if success else 1
    
    elif args.command == 'status':
        rtx.status()
        return 0
    
    return 0


if __name__ == '__main__':
    sys.exit(main())

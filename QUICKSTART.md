# Quick Start Guide - ROBBBO-T Repository

This guide helps you get started with the ROBBBO-T TFA V2 / ASI-T2 repository.

---

## Overview

This repository contains two main products:
- **AMPEL360-T-Air**: BWB H₂ hybrid-electric aircraft
- **AMPEL360-T-Space**: Crewed space transport (suborbital → orbital)

Both follow the canonical **TFA flow**: `QS → FWD → UE → FE → CB → QB`

---

## Repository Structure

```
robbbo-t/
├── canon/                  # ⭐ CANON & GENESIS (read first!)
├── governance/             # MAL-EEM, UTCS, COMPLIANCE
├── ci/                     # CI gates and workflows
├── docs/                   # ROADMAP, PARTNERS, FUNDING
├── domains/                # AAA…PPP (15 technical domains)
├── products/               # ⭐ Product developments
│   ├── ampel360-t-air/     # Air product (BWB H₂)
│   └── ampel360-t-space/   # Space product (crewed)
├── sim/                    # Simulation models
├── cax/                    # CAD/CAE/CFD/FEA
├── qox/                    # Test data and metrics
├── data/                   # Datasets
└── tools/                  # CLI tools and templates
```

---

## Getting Started

### 1. Read Canon Documents (Required!)

Start by reading these foundational documents:

```bash
# Core principles and domains
cat canon/GENESIS_ASI-T2.md

# TFA flow and rules
cat canon/CANON_FACTS.md

# Universal injection prompt (for agents/humans)
cat canon/INJECTION_PROMPT_v1.md
```

**Key concepts to understand**:
- **TFA Flow**: QS → FWD → UE → FE → CB → QB (must follow this order!)
- **UTCS**: Universal Threading for traceability
- **MAL-EEM**: Ethics/empathy checklist
- **15 Domains**: AAA (Architecture) to PPP (Propulsion/Production)

### 2. Understand a Product

Pick a product to explore:

```bash
# Air product (BWB H₂ hybrid-electric)
cat products/ampel360-t-air/README.md

# Space product (crewed transport)
cat products/ampel360-t-space/README.md
```

Each product has 6 TFA layers:
- **QS**: Requirements, sizing, KPIs
- **FWD**: Design (aero, structures, integration)
- **UE**: User experience (cabin, HMI, safety)
- **FE**: Final engineering (propulsion, systems)
- **CB**: Certification (regulatory, compliance)
- **QB**: Quality baseline (testing, validation)

### 3. Install CLI Tool

```bash
# Make sure Python 3.10+ is installed
python3 --version

# No installation needed - tool is already in repo
# Test it:
python tools/cli/rtx.py status
```

---

## Common Tasks

### Check Repository Status

```bash
python tools/cli/rtx.py status
```

Output shows:
- Canon documents (3 files)
- Products (completeness %)
- CI gates (validators)

### Validate Repository Structure

```bash
python tools/cli/rtx.py validate
```

This checks:
- Canon files exist
- Products have all TFA layers
- Directory structure is correct

### Create a New Product

```bash
python tools/cli/rtx.py init-product my-new-product
```

This creates:
- Product directory
- All 6 TFA layers (QS, FWD, UE, FE, CB, QB)
- README template for product and each layer

### Validate Paths and Links

```bash
python ci/gates/link_path_validator.py --check-all
```

This checks:
- All file paths are valid
- No broken links in markdown
- Directory structure follows canon

### Check UTCS Traceability

```bash
python ci/gates/fcr_enforcer.py \
  --pr-title "QS/update-sizing" \
  --files-changed "products/ampel360-t-air/QS/sizing.md"
```

This validates:
- PR title has correct TFA prefix
- UTCS metadata is present
- TFA order is respected

---

## Working on a Product

### Before You Start

1. ✅ Read canon documents
2. ✅ Understand the TFA flow
3. ✅ Identify which layer(s) you're working on
4. ✅ Check that previous layers are complete

### PR Conventions

Use TFA layer prefixes in PR titles:
- `QS/` - Quantum Seal (requirements, sizing)
- `FWD/` - Forward design (aero, structures)
- `UE/` - User Experience (cabin, HMI)
- `FE/` - Final Engineering (systems)
- `CB/` - Certification Basis (regulatory)
- `QB/` - Quality Baseline (testing)

Examples:
```
QS/update-h2-sizing-model
FWD/add-bwb-cfd-results
CB/draft-special-conditions-h2
```

### Include UTCS Metadata

All technical documents should include UTCS metadata:

```yaml
---
utcs:
  context: "ampel360-t-air / FWD / AAA"
  content: "BWB aerodynamic configuration baseline"
  cache: "refs: QS/sizing-001, cax/cfd-baseline"
  structure: "Analysis report"
  style: "Technical documentation"
  sheet:
    id: "FWD-AAA-001"
    version: "1.0"
    author: "Aero Team"
    date: "2024-11-15"
---
```

### Complete MAL-EEM Checklist

Before submitting:
- [ ] **Ethics**: Is this development ethical?
- [ ] **Empathy**: Have we considered human impact?
- [ ] **Meaning**: Does this add value to the project?

---

## Using Templates

### Means of Compliance (MoC)

For certification work:

```bash
cp tools/templates/MoC_template.md \
   products/ampel360-t-air/CB/MoC-H2-tank.md

# Then edit the file to fill in your compliance approach
```

### Hazard Log

For safety assessment:

```bash
cp tools/templates/hazard_log_template.md \
   products/ampel360-t-air/CB/HAZ-001-h2-leak.md

# Then complete the hazard analysis
```

---

## Key Documentation

### Roadmap
```bash
cat docs/ROADMAP.md
```
12-18 month plan with TRL milestones for both products.

### Partners
```bash
cat docs/PARTNERS.md
```
Strategic partners for technology, certification, and funding.

### EU Funding
```bash
cat docs/FUNDING_EU.md
```
Grant opportunities (Clean Aviation, ESA, EIC Accelerator).

---

## CI/CD Gates

Every PR is automatically validated:

1. **FCR-1 Gate**: Path and link validation
   - Checks all file paths exist
   - Validates markdown links
   - Ensures directory structure

2. **FCR-2 Gate**: UTCS and TFA order
   - Validates PR title prefix
   - Checks UTCS metadata
   - Ensures TFA order

**PR will be blocked if validation fails!**

---

## Getting Help

### Documentation
- Read `IMPLEMENTATION_SUMMARY.md` for full details
- Check individual README files in each directory
- Review templates in `tools/templates/`

### CLI Help
```bash
python tools/cli/rtx.py --help
python ci/gates/link_path_validator.py --help
python ci/gates/fcr_enforcer.py --help
```

### Key Contacts
- Governance questions: Open issue with `governance` label
- Technical questions: Reference canon documents
- Tool issues: Open issue with `tooling` label

---

## Best Practices

### Do's ✅
- Always read canon documents first
- Follow TFA order (QS → FWD → UE → FE → CB → QB)
- Include UTCS metadata in technical docs
- Use correct PR title prefixes
- Complete MAL-EEM checklist
- Validate locally before pushing
- Reference related documents

### Don'ts ❌
- Don't skip TFA layers
- Don't break links to canon documents
- Don't modify canon without governance approval
- Don't commit large binary files (use external storage)
- Don't bypass CI gates without justification

---

## Next Steps

1. **Explore**: Browse the product structures
2. **Learn**: Read technical documentation in each TFA layer
3. **Contribute**: Pick a layer and start adding content
4. **Validate**: Run validators frequently
5. **Collaborate**: Coordinate with domain experts

---

## Quick Reference

| Task | Command |
|------|---------|
| Check status | `python tools/cli/rtx.py status` |
| Validate structure | `python tools/cli/rtx.py validate` |
| Create product | `python tools/cli/rtx.py init-product <name>` |
| Check paths | `python ci/gates/link_path_validator.py --check-all` |
| Check UTCS | `python ci/gates/fcr_enforcer.py --pr-title "QS/..." --files-changed "..."` |

---

**Version**: 1.0  
**Last Updated**: 2024-Q4  
**Happy Building!** 🚀

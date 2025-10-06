# Tools

This directory contains development tools, templates, and utilities for the ROBBBO-T project.

---

## Structure

### templates/
**Document Templates**

Standardized templates for compliance, safety, and design documentation.

**Available templates**:
- `MoC_template.md`: Means of Compliance template (for certification)
- `hazard_log_template.md`: Hazard analysis and safety assessment
- PDR/CDR templates (TBD)
- Design review templates (TBD)

### cli/
**Command-Line Tools**

CLI utilities for repository management and automation.

**RTX CLI** (`rtx.py`):
```bash
# Initialize new product
python tools/cli/rtx.py init-product <product-name>

# Add TFA layer to product
python tools/cli/rtx.py add-tfa-layer <product-name> <layer>

# Validate repository structure
python tools/cli/rtx.py validate

# Show repository status
python tools/cli/rtx.py status
```

---

## Using Templates

### Creating a Means of Compliance document

1. Copy template:
   ```bash
   cp tools/templates/MoC_template.md products/ampel360-t-air/CB/MoC-H2-tank.md
   ```

2. Fill in all sections:
   - Document info
   - UTCS metadata
   - Requirement statement
   - Compliance approach
   - Evidence
   - Risk assessment

3. Link to supporting analyses and tests

### Creating a Hazard Log

1. Copy template:
   ```bash
   cp tools/templates/hazard_log_template.md products/ampel360-t-air/CB/HAZ-001-h2-leak.md
   ```

2. Complete hazard analysis:
   - Identification
   - Classification (severity, likelihood)
   - Causes and effects
   - Mitigations
   - Residual risk

---

## Adding New Templates

To add a new template:

1. Create in `tools/templates/`
2. Include UTCS metadata section
3. Document in this README
4. Reference from `/governance/UTCS/`

---

**Version**: 1.0  
**Last Updated**: 2024-Q4

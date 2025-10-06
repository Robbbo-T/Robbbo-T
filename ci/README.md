# CI - Continuous Integration

This directory contains all CI/CD infrastructure for automated validation and deployment.

---

## Structure

### gates/
**CI Gates - Automated Validation**

Validation scripts that run on every PR to ensure compliance with project standards.

**Gates**:
- **FCR-1**: Path and link validation (`link_path_validator.py`)
- **FCR-2**: UTCS traceability and TFA order (`fcr_enforcer.py`)

**Checklists**:
- `FCR-1_checklist.md`: Follow-up Chain Rule 1 requirements
- `FCR-2_checklist.md`: Follow-up Chain Rule 2 requirements

### workflows/
**CI/CD Workflows**

GitHub Actions workflows for automated testing, validation, and deployment.

**Workflows**:
- `fcr-gates.yml`: Runs FCR-1 and FCR-2 validation on all PRs

---

## Running Locally

### FCR-1 (Path Validation)
```bash
python ci/gates/link_path_validator.py --check-all
```

### FCR-2 (UTCS Validation)
```bash
python ci/gates/fcr_enforcer.py \
  --pr-title "FWD/update-geometry" \
  --files-changed "products/ampel360-t-air/FWD/**"
```

---

## PR Requirements

All PRs must:
1. ✅ Pass FCR-1 (no broken links, valid paths)
2. ✅ Pass FCR-2 (UTCS metadata, TFA order)
3. ✅ Include MAL-EEM checklist
4. ✅ Use correct PR title prefix (QS/, FWD/, UE/, FE/, CB/, QB/)

**Failure in any gate blocks merge automatically.**

---

**Version**: 1.0  
**Last Updated**: 2024-Q4

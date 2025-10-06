# QOx - Quality Ops eXchange

This directory indexes test data, metrics, and experimental results.

---

## Purpose

**QOx** is the quality operations exchange: a repository index for all physical test data, quality metrics, and validation results.

Large test data files are stored externally and referenced here with metadata.

---

## Categories

### Test Data
- Component tests (bench tests, subassembly)
- System tests (integrated systems)
- Ground tests (taxi, structural, thermal)
- Flight tests (if applicable)

### Metrics
- KPI tracking (energy consumption, turnaround time, MTBUR)
- Performance metrics (thrust, efficiency, range)
- Quality metrics (defect rates, inspection results)

### Validation
- Model validation data (sim vs. test)
- Compliance validation (regulatory tests)
- Acceptance test results

---

## File Naming Convention

```
<product>-<test-type>-<component>-<date>-<run>.<ext>

Examples:
  ampel360-t-air-bench-e-fan-2024-11-15-run01.csv
  ampel360-t-space-drop-test-cabin-2024-12-01-run03.h5
  ampel360-t-air-hil-powertrain-2024-10-20-sim-results.mat
```

---

## Test Entry Template

```markdown
### Test: E-fan Ground Test (Thrust & Efficiency)
- **Product**: AMPEL360-T-Air
- **Component**: E-fan (Model XYZ-500)
- **Test Type**: Bench test (ground)
- **Date**: 2024-11-15
- **Facility**: [Test lab name/location]
- **Objective**: Measure thrust, efficiency, noise at various RPM
- **Conditions**: 
  - Ambient: 15°C, 101.3 kPa, 60% RH
  - Power: 50-500 kW (variable)
  - RPM: 1000-5000 rpm
- **Results**: 
  - Max thrust: 3500 N @ 4500 rpm, 450 kW
  - Efficiency: 89% @ 4000 rpm, 400 kW
  - Noise: 72 dB @ 1m, 4000 rpm
- **Files**: 
  - Raw data: `s3://robbbo-t-qox/air/e-fan-test-2024-11-15.csv`
  - Processed: `s3://robbbo-t-qox/air/e-fan-test-2024-11-15-analysis.xlsx`
  - Plots: `s3://robbbo-t-qox/air/e-fan-test-2024-11-15-plots.pdf`
- **Report**: `/products/ampel360-t-air/QB/test-reports/e-fan-ground-test-v1.0.pdf`
- **Validation**: 
  - Compared to model: `sim/air/e-fan-model.py`
  - Agreement: Thrust within 5%, efficiency within 3%
```

---

## Integration

QOx data is used by:
- `/sim/`: Validate and calibrate models
- `/products/.../QB/`: Demonstrate test completion
- `/products/.../CB/`: Provide compliance evidence
- `/cax/`: Validate CFD/FEA predictions

---

## Data Management

### Version Control
- Metadata and indices: Committed to git
- Raw data: Stored externally (S3, institutional storage)
- Processed results: Summary committed, full files external

### Access Control
- Public: Non-sensitive performance data
- Internal: Detailed test setups, proprietary results
- Confidential: Safety-critical, pre-certification data

---

## Metrics Dashboard

Track key metrics over time:

| Metric | Target | Current | Trend | Last Updated |
|--------|--------|---------|-------|--------------|
| E-fan efficiency | >90% | 89% | ↗️ | 2024-11-15 |
| H₂ tank BOG rate | <1%/day | 0.8%/day | ✅ | 2024-11-10 |
| Turnaround time | <30 min | 35 min | ➡️ | 2024-10-20 |

---

**Version**: 1.0  
**Last Updated**: 2024-Q4

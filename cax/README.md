# CAx - Computer-Aided Engineering

This directory contains CAD, CAE, CFD, and FEA models and results.

---

## Structure

This directory serves as a **reference and index** for CAx outputs. Large files (STEP, IGES, result files) should be stored externally (Git LFS, cloud storage) and referenced here.

---

## Categories

### CAD (Computer-Aided Design)
- 3D models (STEP, IGES, Parasolid)
- Assembly models
- Drawings (2D, engineering drawings)

**Tools**: CATIA, NX, SolidWorks, Fusion 360

**External storage**: Link to PLM system or cloud storage

### CFD (Computational Fluid Dynamics)
- Aerodynamics (lift, drag, pressure distribution)
- H₂ leak dispersion analysis
- Thermal analysis (cooling flows, heat exchangers)
- Combustion (if applicable)

**Tools**: ANSYS Fluent, Star-CCM+, OpenFOAM, SU2

**Results**: Stored externally, indexed here with metadata

### FEA (Finite Element Analysis)
- Structural analysis (stress, deflection, buckling)
- Vibration and modal analysis
- Fatigue and fracture mechanics
- Thermal-structural coupling

**Tools**: ANSYS Mechanical, Abaqus, Nastran, LS-DYNA

**Results**: Stored externally, indexed here with metadata

### CAM (Computer-Aided Manufacturing)
- Toolpaths for machining
- Additive manufacturing (3D printing) files
- CNC programs

**Tools**: Mastercam, Fusion 360 CAM, Siemens NX CAM

---

## File Naming Convention

```
<product>-<component>-<discipline>-<version>.<ext>

Examples:
  ampel360-t-air-wing-cad-v1.2.step
  ampel360-t-space-cabin-fea-v2.0-results.rst
  ampel360-t-air-bwb-cfd-baseline-v1.0.cas
```

---

## Index File Structure

Each CAx analysis should have an index entry:

```markdown
### Analysis: BWB Aerodynamics CFD Baseline
- **Product**: AMPEL360-T-Air
- **Component**: BWB outer mold line
- **Discipline**: CFD (aerodynamics)
- **Version**: 1.0
- **Date**: 2024-11-15
- **Tool**: ANSYS Fluent 2023 R2
- **Mesh**: 15M cells, polyhedral
- **Results**: 
  - Lift coefficient: CL = 0.52 @ α=3°
  - Drag coefficient: CD = 0.0195 @ α=3°
  - L/D = 26.7
- **Files**: 
  - Mesh: `s3://robbbo-t-cax/air/bwb-cfd-baseline-v1.0.msh`
  - Results: `s3://robbbo-t-cax/air/bwb-cfd-baseline-v1.0.cas/.dat`
- **Report**: `/products/ampel360-t-air/FWD/reports/cfd-baseline-v1.0.pdf`
```

---

## Storage Recommendations

### For Git LFS (< 100 MB)
```bash
git lfs track "*.step"
git lfs track "*.iges"
```

### For Cloud Storage (> 100 MB)
- AWS S3, Google Cloud Storage, Azure Blob
- Document access credentials in `/governance/COMPLIANCE/`
- Never commit large binaries directly to git

---

## Integration

CAx outputs feed into:
- `/sim/`: Provide geometry, mass properties, performance data
- `/products/.../FWD/`: Design validation
- `/products/.../CB/`: Compliance evidence (stress analysis, safety factors)

---

**Version**: 1.0  
**Last Updated**: 2024-Q4

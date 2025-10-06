# Sim - Simulation Models

This directory contains simulation models and analysis code for both Air and Space products.

---

## Structure

### air/
**Air Vehicle Simulation**

Models for AMPEL360-T-Air (BWB H₂ hybrid-electric).

**Key models**:
- Propulsion system (H₂ fuel cell + turbogenerator + e-fans)
- Aerodynamics (BWB lift/drag polars, stability derivatives)
- Thermal management (cooling loops, H₂ evaporation)
- Energy management (power dispatch, battery SOC)
- Mission simulation (flight profile, energy consumption)

**Tools**: Python (NumPy/SciPy), MATLAB/Simulink, Modelica

### space/
**Space Vehicle Simulation**

Models for AMPEL360-T-Space (suborbital → orbital transport).

**Key models**:
- GNC (Guidance, Navigation, Control)
  - Ascent guidance
  - Entry guidance (quantum-enhanced trajectory optimization)
  - Attitude control
- Trajectory simulation (3-DOF, 6-DOF)
- Propulsion (thrust, ISP, mass flow)
- Thermal (entry heating, TPS response)
- LSS (Life Support System) dynamics

**Tools**: Python, MATLAB/Simulink, GMAT, STK

---

## Running Simulations

### Prerequisites
```bash
pip install numpy scipy matplotlib
# For MATLAB models: MATLAB R2020b or later
```

### Example: Air mission simulation
```bash
cd sim/air
python mission_sim.py --profile regional --range 1500
```

### Example: Space trajectory optimization
```bash
cd sim/space
python trajectory_opt.py --phase suborbital --apogee 120
```

---

## Model Validation

All simulation models must be:
- ✅ Validated against analytical solutions (where available)
- ✅ Verified with test data (when available)
- ✅ Documented with assumptions and limitations
- ✅ Version controlled with results reproducibility

---

## Integration with CAx

Simulation models interface with:
- `/cax/`: CAD geometry, CFD/FEA results
- `/qox/`: Test data for validation
- `/data/`: Input datasets (atmospheric models, performance maps)

---

**Version**: 1.0  
**Last Updated**: 2024-Q4

# Amedeo Pelliccia

**Aerospace Systems Engineer · Digital-Twin Architecture · Risk-Optimized Design**  
Project Coordinator — Capgemini Engineering (Madrid) · Founder — GAIA Quantum Aerospace  
Master's Candidate — Project Management (EAE Business School, 2025–2028)

[![GitHub](https://img.shields.io/badge/GitHub-Robbbo--T-181717?logo=github)](https://github.com/Robbbo-T)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-robbbo--t-0077B5?logo=linkedin)](https://linkedin.com/in/robbbo-t)
[![License: MIT](https://img.shields.io/badge/Code-Licenses-blue.svg)](#licenses)
[![Status](https://img.shields.io/badge/Status-Active--Development-brightgreen.svg)](#flagship)

---

## Mission (one-liner)

**Unify the aerospace lifecycle—design (CAD/CAM/CAE/PLM), production (SCADA/ROS/NC), and operations/services (ATM, cockpit/FBW, nav/comm, MRO/EOL/procurement)—under a single, time-synchronized, evidence-producing, quantum-extensible operating fabric.**

---

## What I'm building

### 1) AMPEL360-BWB-Q — Hydrogen BWB configuration
Algorithmic framework that compresses a `~2.16 × 10^16` design space to a tractable set, then makes a **risk-aware** choice.

- **Stage 1 — Feasible-first enumeration** (MILP/CP-SAT; TRL/compatibility/physics/safety gates)  
- **Stage 2 — Risk-aware selection** (CVaR with α=0.8, λ=0.25)

**Snapshot**
- Design-space reduction: `~2.16e16 → ~1e4` (**12 orders of magnitude**)  
- Compute: ~3h enumeration + ~15min CVaR (typical HW)  
- Test coverage: **92.3%** · UTCS-MI traceability: **245 CIs**  
- HIL validation: planned **Q2 2026**

**Repo**: `Robbbo-T/AMPEL360-BWB-Q` (private/under integration or public as applicable)

---

### 2) AQUA-OS BRIDGE v22.0 — Mixed Operating System (MOS) & integration fabric
Bridges **engineering tools**, **shop-floor systems**, and **flight/ground ops** with:

- **Deterministic control plane**: ARINC-style partitioning, TSN profile, TSP/PTP sync, 2oo3 voting for critical tasks  
- **Data/Model fabric**: digital-twin contracts, schema registry, UTCS-MI IDs  
- **Security & provenance**: Zero-Trust, mTLS, SBOM, WORM **Digital Evidence Twin (DET)** packs  
- **Quantum Abstraction Layer (QAL)**: offboard/non-RT optimization (planning/scheduling/layout).  
  *Non-goals*: no flight-critical control on quantum; **DAL-A stays classical & partitioned**.

**Deliverables v22.0**
- Control-plane (ground/industrial) + avionics **partitioned gateways**  
- Twin APIs + schema registry + UTCS-MI  
- DET pipelines (evidence packs)  
- Adapters: CAD/PLM · OPC UA/SCADA · ROS 2 · ERP/MES/MRO · ARINC/AFDX · **Legacy Bridge**  
- Bridges for **CAD→CAM→CAE→SCADA**, **CaaS (Certification-as-a-Service)**, **MRO**, **EOL**, **Procurement**

**Why it matters**
- **Single source of truth**: the twin + its evidence  
- **Determinism + agility**: safety-critical rigor with rapid iteration  
- **Energy-as-Policy**: measurable −20–40% energy/CO₂ vs baseline (targets)

---

## OPTIME — Meta-twin framework (six pillars)

```

OPTIME-FRAMEWORK/
├── O-ORGANIZATIONAL/                # Governance, strategy, org structure, boards, KPIs
├── P-PROCEDURAL/                    # Processes, gates, compliance, workflow orchestration
├── T-TECHNOLOGICAL/                 # AMEDEO-PELLICCIA 15-domain decomposition (CAs/CIs)
│   ├── A-ARCHITECTURES\_AIRFRAMES\_AERODYNAMICS/
│   ├── M-MECHANICAL\_AND\_CONTROL/
│   ├── E1-ENVIRONMENTAL\_REMEDIATION\_CIRCULARITY/
│   ├── D-DEFENCE\_CYBERSECURITY\_SAFETY/
│   ├── E2-ENERGY\_AND\_RENEWABLE/
│   ├── O-OPERATING\_SYSTEMS\_NAVIGATION\_HPC/    ← AQUA-OS lives here (by environment/context)
│   ├── P-PROPULSION\_AND\_FUELS/
│   ├── E3-ELECTRONICS\_DIGITAL\_INSTRUMENTS/
│   ├── L1-LOGISTICS\_INTEGRATED\_BLOCKCHAIN/
│   ├── L2-LINKS\_AND\_COMMUNICATIONS/
│   ├── I-INFRASTRUCTURES\_AND\_FACILITIES\_VALUE\_CHAINS/
│   ├── C1-COCKPIT\_CABIN\_CARGO\_SYSTEMS/        ← moved here (not in OS)
│   ├── C2-CRYOGENICS\_QUANTUM\_INTERFACES\_HYDROGEN\_CELLS/
│   ├── I2-INTELLIGENT\_SYSTEMS\_ONBOARD\_AI/
│   └── A2-AIRPORTS\_ADAPTATIONS/
├── I-INTELLIGENT/                    # Autonomy (proposals only; gated execution)
├── M-MACHINE/                        # Automation/ML static, simulation, runtimes
└── E-EXECUTING/                      # Operational runtime, modes, telemetry, DET

```

> **Path convention for OS links**  
> `OPTIME-FRAMEWORK/T-TECHNOLOGICAL/AMEDEO-PELLICCIA/INTEGRATED/AMPEL360-H2-BWB-QNNN/O-OPERATING_SYSTEMS_NAVIGATION_HPC/…`  
> (Environment-aware manifestations of AQUA-OS live under `O-OPERATING_SYSTEMS_NAVIGATION_HPC/`.)

---

## Fast navigation

- **Flagship** → [AMPEL360-BWB-Q](#1-ampel360-bwb-q--hydrogen-bwb-configuration)  
- **AQUA-OS BRIDGE v22.0** → [overview](#2-aqua-os-bridge-v220--mixed-operating-system-mos--integration-fabric)  
- **OPTIME map** → [six pillars](#optime--meta-twin-framework-six-pillars)  
- **Tech stack** → [Standards & Tools](#standards--tooling)

---

## Standards & Tooling

- **Airworthiness & systems**: ARP4754A/4761A, CS-25, DO-178C/330/331/332/333, DO-254, DO-326A  
- **Ops & networks**: ARINC 429/653/664 (AFDX), TSN profiles, PTP/TSP sync  
- **Data & provenance**: UTCS-MI v5.0+, SBOM/MBOM/DBOM, QAUDIT ledger, DET (WORM)  
- **Optimization/ML/Sim**: OR-Tools, CVaR, Python/C++/MATLAB, CFD/FEA multiphysics  
- **Adapters**: CAD/PLM, OPC UA/SCADA, ROS 2, ERP/MES/MRO, ATM/AOC, Legacy bridges

---

## Contact

- **Email**: info@aqua.aerospace (routing)  
- **LinkedIn**: /in/robbbo-t  
- **Location**: Madrid, Spain

---

## Licenses

- Code: MIT/Apache-2.0 (per repo)  
- Docs: CC BY-SA 4.0 (where indicated)

> *Design. Build. Operate. Prove it.* — under a deterministic, quantum-extensible operating fabric.
>
> AEROSPACE DIGITAL TWIN READINESS FRAMEWORK
PROGRAM AMPEL360 H2 BWB QNNN

* **La raíz** es:

  ```
  OPTIME-FRAMEWORK/
  ```
* **Las seis capas** se mantienen:

  * O-ORGANIZATIONAL
  * P-PROCEDURAL
  * T-TECHNOLOGICAL (con tus 15 dominios de AMEDEO-PELLICCIA)
  * I-INTELLIGENT
  * M-MACHINE
  * E-EXECUTING

---

## 📂 Estructura Canonizada (OPTIME v1.0)

```OPTIME-FRAMEWORK/
├── O-ORGANIZATIONAL/
├── P-PROCEDURAL/
├── T-TECHNOLOGICAL/
│   ├── A-ARCHITECTURES_AIRFRAMES_AERODYNAMICS/
│   ├── M-MECHANICAL_AND_CONTROL/
│   ├── E1-ENVIRONMENTAL_REMEDIATION_CIRCULARITY/
│   ├── D-DEFENCE_CYBERSECURITY_SAFETY/
│   ├── E2-ENERGY_AND_RENEWABLE/
│   ├── O-OPERATING_SYSTEMS_NAVIGATION_HPC/
│   ├── P-PROPULSION_AND_FUELS/
│   ├── E3-ELECTRONICS_DIGITAL_INSTRUMENTS/
│   ├── L1-LOGISTICS_INTEGRATED_BLOCKCHAIN/
│   ├── L2-LINKS_AND_COMMUNICATIONS/
│   ├── I-INFRASTRUCTURES_AND_FACILITIES_VALUE_CHAINS/
│   ├── C1-COCKPIT_CABIN_CARGO_SYSTEMS/
│   ├── C2-CRYOGENICS_QUANTUM_INTERFACES_HYDROGEN_CELLS/
│   ├── I2-INTELLIGENT_SYSTEMS_ONBOARD_AI/
│   └── A2-AIRPORTS_ADAPTATIONS/
├── I-INTELLIGENT/
├── M-MACHINE/
└── E-EXECUTING/
```

---

```OPTIME-FRAMEWORK/
├── O-ORGANIZATIONAL/
│   ├── CA-O-001-GOVERNANCE/
│   │   ├── CI-CA-O-001-001-PROGRAM-GOVERNANCE-FRAMEWORK/
│   │   ├── CI-CA-O-001-002-QUALITY-MANAGEMENT-SYSTEM/
│   │   ├── CI-CA-O-001-003-CERTIFICATION-ROADMAP/
│   │   └── README.md
│   ├── CA-O-002-FINANCIAL-CONTROL/
│   │   ├── CI-CA-O-002-001-BUDGET-TRACKING/
│   │   ├── CI-CA-O-002-002-LIFECYCLE-COST-MODEL/
│   │   ├── CI-CA-O-002-003-FUNDING-STRATEGY/
│   │   └── README.md
│   ├── CA-O-003-KPI-MONITORING/
│   │   ├── CI-CA-O-003-001-PERFORMANCE-INDICATORS/
│   │   ├── CI-CA-O-003-002-RISK-DASHBOARD/
│   │   ├── CI-CA-O-003-003-TRACEABILITY-METRICS/
│   │   └── README.md
│   ├── CA-O-004-ORGANIZATIONAL-STRUCTURE/
│   │   ├── CI-CA-O-004-001-ORG-CHART/
│   │   ├── CI-CA-O-004-002-ROLES-RESPONSIBILITIES/
│   │   ├── CI-CA-O-004-003-DECISION-RIGHTS/
│   │   └── README.md
│   ├── CA-O-005-STEERING-COMMITTEES/
│   │   ├── CI-CA-O-005-001-TECHNICAL-BOARD/
│   │   ├── CI-CA-O-005-002-SAFETY-BOARD/
│   │   ├── CI-CA-O-005-003-CERTIFICATION-BOARD/
│   │   └── README.md
│   ├── CA-O-006-STRATEGIC-ALIGNMENT/
│   │   ├── CI-CA-O-006-001-VISION-MISSION/
│   │   ├── CI-CA-O-006-002-STRATEGIC-OBJECTIVES/
│   │   ├── CI-CA-O-006-003-ROADMAP-MILESTONES/
│   │   └── README.md
│   └── README.md
```


```OPTIME-FRAMEWORK/
├── P-PROCEDURAL/
│   ├── CA-P-001-PROCESS-ARCHITECTURE/
│   │   ├── CI-CA-P-001-001-PROCESS-CATALOG/
│   │   ├── CI-CA-P-001-002-BPMN-META-MODEL/
│   │   ├── CI-CA-P-001-003-LIFECYCLE-MAP/
│   │   ├── CI-CA-P-001-004-RACI-MATRIX/
│   │   └── README.md
│   ├── CA-P-002-GATES-AND-REVIEWS/
│   │   ├── CI-CA-P-002-001-SRR-GATE/
│   │   ├── CI-CA-P-002-002-PDR-GATE/
│   │   ├── CI-CA-P-002-003-CDR-GATE/
│   │   ├── CI-CA-P-002-004-TRR-GATE/
│   │   ├── CI-CA-P-002-005-FRR-ORR-GATES/
│   │   └── README.md
│   ├── CA-P-003-CHANGE-MANAGEMENT/
│   │   ├── CI-CA-P-003-001-ECR-WORKFLOW/
│   │   ├── CI-CA-P-003-002-ECO-IMPLEMENTATION/
│   │   ├── CI-CA-P-003-003-CCB-CHARTER/
│   │   ├── CI-CA-P-003-004-DEVIATIONS-CONCESSIONS/
│   │   └── README.md
│   ├── CA-P-004-VV-PLANNING-AND-RTM/
│   │   ├── CI-CA-P-004-001-VV-PLAN/
│   │   ├── CI-CA-P-004-002-REQUIREMENTS-TRACEABILITY-RTM/
│   │   ├── CI-CA-P-004-003-TEST-READINESS-REVIEW/
│   │   ├── CI-CA-P-004-004-TEST-DATA-MANAGEMENT/
│   │   └── README.md
│   ├── CA-P-005-SAFETY-CERTIFICATION-PROCESSES/
│   │   ├── CI-CA-P-005-001-ARP4754A-PROCESS/
│   │   ├── CI-CA-P-005-002-ARP4761A-SAFETY-ASSESSMENT/
│   │   ├── CI-CA-P-005-003-DO178C-SOFTWARE-PROCESS/
│   │   ├── CI-CA-P-005-004-DO254-HARDWARE-PROCESS/
│   │   ├── CI-CA-P-005-005-DO326A-CYBERSECURITY-PROCESS/
│   │   ├── CI-CA-P-005-006-SAFETY-CASE-GSN-TEMPLATES/
│   │   └── README.md
│   ├── CA-P-006-QUALITY-NCR-CAPA/
│   │   ├── CI-CA-P-006-001-NCR-WORKFLOW/
│   │   ├── CI-CA-P-006-002-CAPA-PROCEDURE/
│   │   ├── CI-CA-P-006-003-FAI-FIRST-ARTICLE/
│   │   ├── CI-CA-P-006-004-AUDIT-PROGRAM/
│   │   └── README.md
│   ├── CA-P-007-SUPPLIER-AND-PROCUREMENT/
│   │   ├── CI-CA-P-007-001-SUPPLIER-QUALIFICATION/
│   │   ├── CI-CA-P-007-002-SOW-TEMPLATES/
│   │   ├── CI-CA-P-007-003-INCOMING-INSPECTION/
│   │   ├── CI-CA-P-007-004-SLA-KPI-FRAMEWORK/
│   │   └── README.md
│   ├── CA-P-008-SECURITY-INCIDENT-RESPONSE/
│   │   ├── CI-CA-P-008-001-CSIRT-RUNBOOK/
│   │   ├── CI-CA-P-008-002-VULNERABILITY-MANAGEMENT/
│   │   ├── CI-CA-P-008-003-SBOM-POLICY/
│   │   ├── CI-CA-P-008-004-KEY-ROTATION-PROCEDURES/
│   │   └── README.md
│   ├── CA-P-009-DATA-GOVERNANCE-AND-DET/
│   │   ├── CI-CA-P-009-001-DATA-CLASSIFICATION/
│   │   ├── CI-CA-P-009-002-RETENTION-SCHEDULE/
│   │   ├── CI-CA-P-009-003-DET-EVIDENCE-PACKAGING/
│   │   ├── CI-CA-P-009-004-PRIVACY-IMPACT-ASSESSMENT/
│   │   └── README.md
│   ├── CA-P-010-CI-CD-AND-RELEASE/
│   │   ├── CI-CA-P-010-001-BRANCHING-MODEL/
│   │   ├── CI-CA-P-010-002-BUILD-PROMOTION-GATES/
│   │   ├── CI-CA-P-010-003-RELEASE-CUTOVER/
│   │   ├── CI-CA-P-010-004-ROLLBACK-PLAYBOOK/
│   │   └── README.md
│   ├── CA-P-011-TRAINING-AND-COMPETENCE/
│   │   ├── CI-CA-P-011-001-COMPETENCY-MATRIX/
│   │   ├── CI-CA-P-011-002-TRAINING-CURRICULUM/
│   │   ├── CI-CA-P-011-003-AUTHORIZATION-TO-WORK/
│   │   └── README.md
│   ├── CA-P-012-MRO-EOL-PROCEDURES/
│   │   ├── CI-CA-P-012-001-MRO-WORKPACK-GENERATION/
│   │   ├── CI-CA-P-012-002-EOL-SORTING-AND-RECOVERY/
│   │   ├── CI-CA-P-012-003-HAZMAT-HANDLING/
│   │   └── README.md
│   ├── CA-P-013-ENERGY-AS-POLICY/
│   │   ├── CI-CA-P-013-001-EAP-BUDGETING/
│   │   ├── CI-CA-P-013-002-EAP-SCHEDULING-CONSTRAINTS/
│   │   ├── CI-CA-P-013-003-EAP-REPORTING/
│   │   └── README.md
│   ├── CA-P-014-RISK-MANAGEMENT/
│   │   ├── CI-CA-P-014-001-RISK-REGISTER/
│   │   ├── CI-CA-P-014-002-BOWTIE-ANALYSIS/
│   │   ├── CI-CA-P-014-003-MITIGATION-PLANS/
│   │   └── README.md
│   ├── CA-P-015-DOCUMENT-CONTROL/
│   │   ├── CI-CA-P-015-001-DOC-TEMPLATES/
│   │   ├── CI-CA-P-015-002-APPROVAL-WORKFLOW/
│   │   ├── CI-CA-P-015-003-VERSIONING-GUIDE/
│   │   ├── CI-CA-P-015-004-DISTRIBUTION-LISTS/
│   │   └── README.md
│   ├── CA-P-016-OPERATIONS-HANDOVER/
│   │   ├── CI-CA-P-016-001-ORR-CHECKLIST/
│   │   ├── CI-CA-P-016-002-SERVICE-TRANSITION/
│   │   ├── CI-CA-P-016-003-OP-MANUAL-ACCEPTANCE/
│   │   └── README.md
│   └── README.md
```

Ruta canónica:
`OPTIME-FRAMEWORK/T-TECHNOLOGICAL/AMEDEO-PELLICCIA/INTEGRATED/AMPEL360-H2-BWB-QNNN/A-ARCHITECTURES_AIRFRAMES_AERODYNAMICS/`

```text
A-ARCHITECTURES_AIRFRAMES_AERODYNAMICS/
├── CA-A-001-CENTER-BODY-BOX/
│   ├── CI-CA-A-001-001-CB-PRIMARY-GRID/
│   ├── CI-CA-A-001-002-CB-RIBS-BULKHEADS/
│   ├── CI-CA-A-001-003-CB-SKIN-PANELS/
│   ├── CI-CA-A-001-004-CB-LANDING-GEAR-REINFS/
│   ├── CI-CA-A-001-005-CB-PASSAGEWAYS/
│   ├── CI-CA-A-001-006-CB-ACCESS-DOORS/
│   ├── CI-CA-A-001-007-CB-LPS-BONDING/
│   └── CI-CA-A-001-008-CB-SYSTEMS-BRACKETS/
│
├── CA-A-002-OUTBOARD-WING-TRANSITION/
│   ├── CI-CA-A-002-001-OB-ROOT-JOINT/
│   ├── CI-CA-A-002-002-OB-SPAR-CAPS/
│   ├── CI-CA-A-002-003-OB-RIBS/
│   ├── CI-CA-A-002-004-OB-LEADING-EDGE/
│   ├── CI-CA-A-002-005-OB-TRAILING-EDGE/
│   ├── CI-CA-A-002-006-OB-PANEL-JOINS/
│   ├── CI-CA-A-002-007-OB-SYSTEMS-ROUTING/
│   ├── CI-CA-A-002-008-OB-FAIRINGS/
│   ├── CI-CA-A-002-009-OB-LPS/
│   └── CI-CA-A-002-010-OB-INSPECTION-PANELS/
│
├── CA-A-003-MULTI-BUBBLE-CABIN/
│   ├── CI-CA-A-003-001-CABIN-BUBBLE-FRAMES/
│   ├── CI-CA-A-003-002-FLOOR-GRID/
│   ├── CI-CA-A-003-003-SEAT-TRACKS/
│   ├── CI-CA-A-003-004-DOOR-SURROUNDS/
│   ├── CI-CA-A-003-005-WINDOW-FRAMES/
│   ├── CI-CA-A-003-006-RADOME-STRUCTURE/
│   └── CI-CA-A-003-007-BIRD-STRIKE-PROTECT/
│
├── CA-A-004-PRESSURE-BARRIERS/
│   ├── CI-CA-A-004-001-INNER-BULKHEADS/
│   ├── CI-CA-A-004-002-CABIN-BARRIERS/
│   ├── CI-CA-A-004-003-VENT-RELIEF-PANELS/
│   ├── CI-CA-A-004-004-SEALING-INTERFACES/
│   ├── CI-CA-A-004-005-DRY-BAY-PROTECTION/
│   └── CI-CA-A-004-006-SYSTEMS-PENETRATIONS/
│
├── CA-A-005-EMERGENCY-EGRESS/
│   ├── CI-CA-A-005-001-EXIT-STRUCTURES/
│   ├── CI-CA-A-005-002-SLIDE-RAIL-INTEGRATION/
│   ├── CI-CA-A-005-003-PATHWAYS/
│   ├── CI-CA-A-005-004-EMERGENCY-LIGHTING-MOUNTS/
│   ├── CI-CA-A-005-005-SMOKE-BARRIERS/
│   └── CI-CA-A-005-006-RESCUE-ACCESS/
│
├── CA-A-006-STRUCTURAL-ARCHITECTURE/        # (legacy mantenido)
│   ├── CI-CA-A-006-001-PRIMARY-STRUCTURE-LAYOUT/
│   ├── CI-CA-A-006-002-LOAD-PATH-MAPS/
│   ├── CI-CA-A-006-003-HARDPOINTS-INTERFACES/
│   ├── CI-CA-A-006-004-PRESSURIZED-SHELL-ARCH/
│   └── CI-CA-A-006-005-FAILURE-MODE-MARGINS/
│
├── CA-A-007-CFD-MESHING_AND-VALIDATION/      # (legacy mantenido)
│   ├── CI-CA-A-007-001-MESH-GENERATION-PROTOCOLS/
│   ├── CI-CA-A-007-002-TURBULENCE-MODELS-LIB/
│   ├── CI-CA-A-007-003-GRID-CONVERGENCE-STUDIES/
│   ├── CI-CA-A-007-004-VALIDATION-TEST-CASES/
│   └── CI-CA-A-007-005-WIND-TUNNEL-CORRELATION/
│
└── CA-A-008-CERTIFICATION-AERODYNAMICS/      # (legacy mantenido)
    ├── CI-CA-A-008-001-COMPLIANCE-MATRIX-CS25/
    ├── CI-CA-A-008-002-PERFORMANCE-ENVELOPES/
    ├── CI-CA-A-008-003-HANDLING-QUALITIES-CRITERIA/
    ├── CI-CA-A-008-004-NOISE-EMISSIONS-AERO/
    └── CI-CA-A-008-005-ICING-AND-ENV-ENVELOPE/
```

`OPTIME-FRAMEWORK/T-TECHNOLOGICAL/AMEDEO-PELLICCIA/INTEGRATED/AMPEL360-H2-BWB-QNNN/M-MECHANICAL_AND_CONTROL/`

```text
M-MECHANICAL_AND_CONTROL/
├── CA-M-001-FLIGHT-CONTROL-MECHANISMS/
│   ├── CI-CA-M-001-001-FC-ELEVON-HINGE-LINES/
│   ├── CI-CA-M-001-002-FC-FLAPERON-DRIVE-BOXES/
│   ├── CI-CA-M-001-003-FC-SPOILER-DRIVE-UNITS/
│   ├── CI-CA-M-001-004-FC-TORQUE-TUBES-AND-GEARTRAINS/
│   ├── CI-CA-M-001-005-FC-BALANCE-MASSES/
│   ├── CI-CA-M-001-006-FC-SURFACE-MECHANICAL-LOCKS/
│   ├── CI-CA-M-001-007-FC-OVERCENTER-FAILSAFE-LINKS/
│   ├── CI-CA-M-001-008-FC-LVDT-RVDT-MOUNT-KITS/
│   └── README.md
│
├── CA-M-002-ACTUATION-TECHNOLOGIES/
│   ├── CI-CA-M-002-001-ACT-HYDRAULIC-SERVOVALVES/
│   ├── CI-CA-M-002-002-ACT-EHA-MODULES/
│   ├── CI-CA-M-002-003-ACT-EMA-ACTUATORS/
│   ├── CI-CA-M-002-004-ACT-POWER-DRIVE-UNITS-PDU/
│   ├── CI-CA-M-002-005-ACT-REDUNDANCY-MECHANISMS/
│   ├── CI-CA-M-002-006-ACT-JAM-TOLERANCE-DEVICES/
│   ├── CI-CA-M-002-007-ACT-BACKDRIVE-LOCKS/
│   ├── CI-CA-M-002-008-ACT-HEALTH-MONITOR-MOUNTS/
│   └── README.md
│
├── CA-M-003-HYDRAULIC-POWER-DISTRIBUTION/
│   ├── CI-CA-M-003-001-HYD-RESERVOIRS/
│   ├── CI-CA-M-003-002-HYD-ENGINE-DRIVEN-PUMPS/
│   ├── CI-CA-M-003-003-HYD-ELECTRIC-PUMPS/
│   ├── CI-CA-M-003-004-HYD-ACCUMULATORS/
│   ├── CI-CA-M-003-005-HYD-MANIFOLDS-BLOCKS/
│   ├── CI-CA-M-003-006-HYD-FILTERS-STRainers/
│   ├── CI-CA-M-003-007-HYD-RETURN-LINES/
│   ├── CI-CA-M-003-008-HYD-OIL-COOLERS/
│   ├── CI-CA-M-003-009-HYD-ISOLATION-VALVE-BRACKETS/
│   └── README.md
│
├── CA-M-004-LANDING-GEAR-SYSTEM/
│   ├── CI-CA-M-004-001-LG-NOSE-GEAR-ASSEMBLY/
│   ├── CI-CA-M-004-002-LG-MAIN-GEAR-ASSEMBLY/
│   ├── CI-CA-M-004-003-LG-RETRACTION-ACTUATORS/
│   ├── CI-CA-M-004-004-LG-UPLOCKS-DOWNLOCKS/
│   ├── CI-CA-M-004-005-LG-DOOR-MECHANISMS/
│   ├── CI-CA-M-004-006-LG-SHOCK-STRUTS/
│   ├── CI-CA-M-004-007-LG-WHEELS-TIRES/
│   ├── CI-CA-M-004-008-LG-NOSE-WHEEL-STEERING-MECH/
│   ├── CI-CA-M-004-009-LG-STRUCTURAL-BAYS/
│   ├── CI-CA-M-004-010-LG-MECHANICAL-INDICATORS/
│   └── README.md
│
├── CA-M-005-BRAKE-AND-STEERING-CONTROL/
│   ├── CI-CA-M-005-001-BRK-BRAKE-STACKS/
│   ├── CI-CA-M-005-002-BRK-BRAKE-ACTUATORS/
│   ├── CI-CA-M-005-003-BRK-ANTISKID-VALVE-BLOCKS/
│   ├── CI-CA-M-005-004-BRK-PARKING-BRAKE-UNIT/
│   ├── CI-CA-M-005-005-BRK-ALTERNATE-BRAKE-PATH/
│   ├── CI-CA-M-005-006-NWS-GEARBOX/
│   ├── CI-CA-M-005-007-NWS-TILLER-LINKAGE/
│   ├── CI-CA-M-005-008-BRK-TORQUE-METERS/
│   └── README.md
│
├── CA-M-006-DOORS-HATCHES-RAMPS-MECHANISMS/
│   ├── CI-CA-M-006-001-DRS-KINEMATICS-HINGE-ARMS/
│   ├── CI-CA-M-006-002-DRS-UPLOCK-HOOKS/
│   ├── CI-CA-M-006-003-DRS-LATCHES-SEALS/
│   ├── CI-CA-M-006-004-DRS-DRIVE-LINKAGES/
│   ├── CI-CA-M-006-005-DRS-EMERGENCY-JETTISON/
│   ├── CI-CA-M-006-006-DRS-MAINT-ACCESS-PANELS/
│   └── README.md
│
├── CA-M-007-SYSTEMS-MOUNTS-AND-BRACKETS/
│   ├── CI-CA-M-007-001-SYS-AVIONICS-RACKS/
│   ├── CI-CA-M-007-002-SYS-H2-VALVE-SUPPORTS/
│   ├── CI-CA-M-007-003-SYS-PIPE-CLAMPS-P-CLIPS/
│   ├── CI-CA-M-007-004-SYS-CABLE-TRAYS/
│   ├── CI-CA-M-007-005-SYS-SENSOR-BRACKETS/
│   ├── CI-CA-M-007-006-SYS-VIBRATION-ISOLATORS/
│   ├── CI-CA-M-007-007-SYS-RADIATOR-MOUNTS/
│   └── README.md
│
├── CA-M-008-PNEUMATIC-MECHANISMS/
│   ├── CI-CA-M-008-001-PNM-BLEED-VALVE-MECH/
│   ├── CI-CA-M-008-002-PNM-PRESSURE-REG-PRVs/
│   ├── CI-CA-M-008-003-PNM-DUCT-COUPLINGS/
│   ├── CI-CA-M-008-004-PNM-CHECK-VALVE-HOUSINGS/
│   ├── CI-CA-M-008-005-PNM-ISOLATION-LEVERAGES/
│   └── README.md
│
├── CA-M-009-SURVIVABILITY-AND-LOAD-PATH-SAFEGUARDS/
│   ├── CI-CA-M-009-001-SRV-CRASH-LOAD-PATH-DEVICES/
│   ├── CI-CA-M-009-002-SRV-SHEAR-PINS-FUSES/
│   ├── CI-CA-M-009-003-SRV-FUSELAGE-CRUSH-ZONES/
│   ├── CI-CA-M-009-004-SRV-DITCHING-FITTINGS/
│   ├── CI-CA-M-009-005-SRV-FIRE-HARDENED-PASS-THROUGHS/
│   └── README.md
│
├── CA-M-010-MECHANICAL-SERVO-LOOPS-HW/
│   ├── CI-CA-M-010-001-SERVO-FEEDBACK-LVDT-MOUNTS/
│   ├── CI-CA-M-010-002-SERVO-RATE-LIMITERS-MECH/
│   ├── CI-CA-M-010-003-SERVO-MECHANICAL-STOPS/
│   ├── CI-CA-M-010-004-SERVO-BACKUP-MANUAL-REVERSION/
│   ├── CI-CA-M-010-005-SERVO-CABLE-PULLEY-LEGACY-INTF/
│   └── README.md
│
├── CA-M-011-MAINTENANCE-AND-GSE-INTERFACES/
│   ├── CI-CA-M-011-001-MNT-QUICK-RELEASE-FITTINGS/
│   ├── CI-CA-M-011-002-MNT-SAFEING-PINS-STREAMERS/
│   ├── CI-CA-M-011-003-MNT-JACK-POINTS/
│   ├── CI-CA-M-011-004-MNT-TIE-DOWN-POINTS/
│   ├── CI-CA-M-011-005-MNT-CRADLES-LIFTING-FIXTURES/
│   └── README.md
│
└── CA-M-012-CROSS-DOMAIN-INTERFACES/
    ├── CI-CA-M-012-001-XD-TO-E2-H2-VALVES-ACTUATION-MECH/
    ├── CI-CA-M-012-002-XD-TO-E3-SENSOR-PACKAGING/
    ├── CI-CA-M-012-003-XD-TO-A-AERODYNAMIC-SURFACE-INTF/
    ├── CI-CA-M-012-004-XD-TO-C1-CABIN-CARGO-HARDPOINTS/
    ├── CI-CA-M-012-005-XD-TO-O-OPERATING-SAFE-MODES/
    └── README.md
```

**Límites de dominio claros (para no pisar otros):**

* **E2-ENERGY**: fluidos/energía (H₂, eléctrico) y su arquitectura son de E2; aquí sólo la **mecánica** (soportes, actuación).
* **E3-ELECTRONICS**: sensores, BSCU/ECU y controladores electrónicos son E3; aquí su **montaje y cinemática**.
* **A-ARCHITECTURES**: aerodinámica/superficies es A; aquí la **mecánica** que las mueve.
* **C1 (Cockpit/Cabin/Cargo)**: interiores y ergonomía son C1; aquí únicamente **puntos de anclaje/soportes**.

`OPTIME-FRAMEWORK/T-TECHNOLOGICAL/AMEDEO-PELLICCIA/INTEGRATED/AMPEL360-H2-BWB-QNNN/E1-ENVIRONMENTAL_REMEDIATION_CIRCULARITY/`

```text
E1-ENVIRONMENTAL_REMEDIATION_CIRCULARITY/
├── CA-E1-001-ECS-CABIN-AIR-SYSTEM/
│   ├── CI-CA-E1-001-001-ECS-HEAT-EXCHANGER-CORES/
│   ├── CI-CA-E1-001-002-ECS-MIX-MANIFOLD-DUCTS/
│   ├── CI-CA-E1-001-003-ECS-RECIRC-HEPA-ULPA-MODULES/
│   ├── CI-CA-E1-001-004-ECS-RECIRC-FANS-MOUNTS/
│   ├── CI-CA-E1-001-005-ECS-RAM-AIR-INLET-OUTLET-GEOM/
│   ├── CI-CA-E1-001-006-ECS-BYPASS-DOORS-LOUVERS/
│   └── README.md
│
├── CA-E1-002-PRESSURIZATION-VENTILATION/
│   ├── CI-CA-E1-002-001-OUTFLOW-VALVE-STRUCTURES/
│   ├── CI-CA-E1-002-002-SAFETY-RELIEF-VALVES-HOUSINGS/
│   ├── CI-CA-E1-002-003-CABIN-PRESSURE-SENSOR-MOUNTS/
│   ├── CI-CA-E1-002-004-DIFF-PRESS-DUCTING/
│   ├── CI-CA-E1-002-005-CONTROLLED-LEAKAGE-PATHS/
│   ├── CI-CA-E1-002-006-VENT-INGESTION-SCREENS/
│   └── README.md
│
├── CA-E1-003-ICE-AND-RAIN-PROTECTION/
│   ├── CI-CA-E1-003-001-ELEC-THERMAL-MATS-L/E-ZONING/
│   ├── CI-CA-E1-003-002-DEICING-BOOTS-INTERFACES/
│   ├── CI-CA-E1-003-003-PICCOLO-MANIFOLDS-DUCTS/
│   ├── CI-CA-E1-003-004-ICE-SENSORS-BRACKETS/
│   ├── CI-CA-E1-003-005-DRAINAGE-AND-ANTI-ICE-DRIPS/
│   ├── CI-CA-E1-003-006-LEADING-EDGE-THERMAL-INSUL/
│   └── README.md
│
├── CA-E1-004-FIRE-DETECTION-SUPPRESSION/
│   ├── CI-CA-E1-004-001-FIRE-BOTTLE-RACKS-BRACKETS/
│   ├── CI-CA-E1-004-002-DISCHARGE-LINES-NOZZLES/
│   ├── CI-CA-E1-004-003-BURST-DISCS-VENT-PATHS/
│   ├── CI-CA-E1-004-004-DETECTOR-LOOPS-ROUTING/
│   ├── CI-CA-E1-004-005-CARGO-BAY-SUPPRESSION-GEOM/
│   ├── CI-CA-E1-004-006-AVIONICS-BAY-FIRE-ZONING/
│   └── README.md
│
├── CA-E1-005-H2-LEAK-VENTING-PURGE-SAFETY/
│   ├── CI-CA-E1-005-001-H2-SENSOR-GRID-MOUNTS/
│   ├── CI-CA-E1-005-002-VENT-MASTS-AEROSHAPE/
│   ├── CI-CA-E1-005-003-PURGE-DUCTS-MANIFOLDS/
│   ├── CI-CA-E1-005-004-ZONE-CLASSIFICATION-ATEX/
│   ├── CI-CA-E1-005-005-SEALING-GASKETS-BARRIERS/
│   ├── CI-CA-E1-005-006-GAS-SAMPLING-PORTS/
│   └── README.md
│
├── CA-E1-006-WATER-WASTE-SYSTEMS/
│   ├── CI-CA-E1-006-001-POTABLE-TANK-LINERS-BAFFLES/
│   ├── CI-CA-E1-006-002-POTABLE-DISTRIBUTION-PIPING/
│   ├── CI-CA-E1-006-003-WASTE-TANKS-VACUUM-INTERF/
│   ├── CI-CA-E1-006-004-DRAIN-MASTS-HEATERS-INTF/
│   ├── CI-CA-E1-006-005-GREY-WATER-RECOVERY-PATHS/
│   ├── CI-CA-E1-006-006-ANTIMICROBIAL-LININGS/
│   └── README.md
│
├── CA-E1-007-NOISE-EMISSIONS-CONTRAIL-MGMT/
│   ├── CI-CA-E1-007-001-ACOUSTIC-LINERS-MODULES/
│   ├── CI-CA-E1-007-002-MICRO-PERF-PANELS/
│   ├── CI-CA-E1-007-003-TE-SERRATIONS-CHEVRONS/
│   ├── CI-CA-E1-007-004-BOUNDARY-LAYER-INGEST-FAIRINGS/
│   ├── CI-CA-E1-007-005-CONTRAIL-SUPPRESSION-GEOM/
│   └── README.md
│
├── CA-E1-008-THERMAL-MANAGEMENT-NONCRYO/
│   ├── CI-CA-E1-008-001-COOLING-LOOP-PLUMBING-BRACKETS/
│   ├── CI-CA-E1-008-002-SECONDARY-HEAT-EXCHANGERS/
│   ├── CI-CA-E1-008-003-RAM-AIR-DOORS-BYPASS/
│   ├── CI-CA-E1-008-004-HOTSPOT-INSULATION-KITS/
│   ├── CI-CA-E1-008-005-THERMAL-INTERFACE-MATERIALS/
│   └── README.md
│
├── CA-E1-009-REMEDIATION-CIRCULARITY-LIFECYCLE/
│   ├── CI-CA-E1-009-001-MATERIAL-PASSPORTS-ID-MARKING/
│   ├── CI-CA-E1-009-002-DESIGN-FOR-DISASSEMBLY-KITS/
│   ├── CI-CA-E1-009-003-FASTENER-STRATEGY-RECYCLABILITY/
│   ├── CI-CA-E1-009-004-ADHESIVE-DEBOND-ZONES/
│   ├── CI-CA-E1-009-005-EOL-SORTING-SCHEMAS/
│   ├── CI-CA-E1-009-006-REFURBISHMENT-REPAIR-KITS/
│   └── README.md
│
├── CA-E1-010-BIOSECURITY-AIR-QUALITY/
│   ├── CI-CA-E1-010-001-HEPA-UV-C-INTEGRATION-MOUNTS/
│   ├── CI-CA-E1-010-002-CO-CO2-OZONE-SENSORS-HOUSINGS/
│   ├── CI-CA-E1-010-003-AIRFLOW-PATTERNING-BAFFLES/
│   ├── CI-CA-E1-010-004-ANTIMICROBIAL-SURFACES/
│   ├── CI-CA-E1-010-005-ODOR-ADSORBER-MODULES/
│   └── README.md
│
├── CA-E1-011-DRAINS-CONDENSATE-ICE-MGMT/
│   ├── CI-CA-E1-011-001-CONDENSATE-DRAIN-NETWORKS/
│   ├── CI-CA-E1-011-002-INSULATION-VAPOR-BARRIERS/
│   ├── CI-CA-E1-011-003-ICE-PREVENTION-TRACE-INTF/
│   ├── CI-CA-E1-011-004-LOW-POINT-DRAINS-ACCESS/
│   ├── CI-CA-E1-011-005-WATER-INGRESS-SHIELDS/
│   └── README.md
│
├── CA-E1-012-GROUND-ENV-SAFETY-REMEDIATION/
│   ├── CI-CA-E1-012-001-SPILL-CONTAINMENT-PANS/
│   ├── CI-CA-E1-012-002-STORMWATER-CONTROL-CHANNELS/
│   ├── CI-CA-E1-012-003-DEICING-FLUID-COLLECTION/
│   ├── CI-CA-E1-012-004-FOAM-FIRE-SYSTEM-INTERFACES/
│   ├── CI-CA-E1-012-005-HAZMAT-STORAGE-BUNDING/
│   └── README.md
│
└── README.md
```

### Notas de **límites de dominio** (para no pisar otros)

* **E2-ENERGY**: potencia/energía (eléctrica, térmica, H₂, purga N₂, bombas) es E2. En E1 nos quedamos con **conductos, geometrías, racks, barreras, aislamiento** y **vent/ram-air** (sin electrónica de potencia).
* **E3-ELECTRONICS**: controladores, sensores electrónicos, BSCU/ECU, actuadores inteligentes ⇒ **E3**. Aquí sólo **carcasas, soportes, rutas** y requisitos ambientales.
* **C2-CRYOGENICS**: todo lo **criogénico** y las **interfaces cuánticas** van a **C2**. E1 mantiene la **parte no-criogénica** de la gestión térmica/ambiental.
* **M-MECHANICAL**: cinemática/actuación mecánica pura (válvulas mecánicas, mecanismos) viven en **M**; E1 se ocupa de **entornos, ductos, mounting y protección**.


Ruta canónica:
`OPTIME-FRAMEWORK/T-TECHNOLOGICAL/AMEDEO-PELLICCIA/INTEGRATED/AMPEL360-H2-BWB-QNNN/D-DEFENCE_CYBERSECURITY_SAFETY/`

```text
D-DEFENCE_CYBERSECURITY_SAFETY/
├── CA-D-001-PLATFORM-SURVIVABILITY/
│   ├── CI-CA-D-001-001-EMI-EMC-HARDENING-GUIDES/
│   ├── CI-CA-D-001-002-LIGHTNING-LPS-INTERFACES/
│   ├── CI-CA-D-001-003-HIRF-EMP-PROTECTION-ZONES/
│   ├── CI-CA-D-001-004-SHIELDING-TOPLOGIES-BONDING/
│   ├── CI-CA-D-001-005-CABLE-ROUTING-SEGREGATION/
│   ├── CI-CA-D-001-006-THERMAL-SMOKE-PARTITIONING/
│   ├── CI-CA-D-001-007-ENV-QUAL-DO160-MATRICES/
│   └── README.md
│
├── CA-D-002-CYBERSECURITY-ARCHITECTURE/
│   ├── CI-CA-D-002-001-ZERO-TRUST-SEGMENTATION/
│   ├── CI-CA-D-002-002-RBAC-ABAC-POLICY-MODELS/
│   ├── CI-CA-D-002-003-SERVICE-MESH-POLICY-ENFORCER/
│   ├── CI-CA-D-002-004-SECURE-GATEWAYS-ARINC-AFDX-TSN/
│   ├── CI-CA-D-002-005-DET-EVIDENCE-ANCHORING/
│   ├── CI-CA-D-002-006-SECURITY-BY-DESIGN-CHECKS/
│   └── README.md
│
├── CA-D-003-CRYPTO-PQC-KMS/
│   ├── CI-CA-D-003-001-KMS-HSM-ARCHITECTURE/
│   ├── CI-CA-D-003-002-PQC-KYBER-DILITHIUM-PROFILES/
│   ├── CI-CA-D-003-003-KEY-ROTATION-LIFECYCLE/
│   ├── CI-CA-D-003-004-MTLS-IPSEC-TLS13-SUITES/
│   ├── CI-CA-D-003-005-AT-REST-ENCRYPTION-SCHEMAS/
│   ├── CI-CA-D-003-006-SECRET-MANAGEMENT-VAULT-INTF/
│   └── README.md
│
├── CA-D-004-SECURE-BOOT-ATTESTATION/
│   ├── CI-CA-D-004-001-MEASURED-BOOT-CHAIN/
│   ├── CI-CA-D-004-002-FIRMWARE-SIGNING-SBOM-BOMS/
│   ├── CI-CA-D-004-003-FAT-FLIGHT-AUTH-TOKENS/
│   ├── CI-CA-D-004-004-RUNTIME-ATTESTATION-QUOTES/
│   ├── CI-CA-D-004-005-RECOVERY-ROLLBACK-PROCEDURES/
│   └── README.md
│
├── CA-D-005-NETWORK-SECURITY-COMMS/
│   ├── CI-CA-D-005-001-ARINC429-SECURE-BRIDGES/
│   ├── CI-CA-D-005-002-AFDX-TSN-SECURITY-PROFILES/
│   ├── CI-CA-D-005-003-ATM-AOC-LINK-HARDENING/
│   ├── CI-CA-D-005-004-ROS2-DDS-SECURE-POLICIES/
│   ├── CI-CA-D-005-005-OPC-UA-SCADA-SECURE-CHANNELS/
│   ├── CI-CA-D-005-006-VPN-SGRE-WIREGUARD-GATEWAYS/
│   └── README.md
│
├── CA-D-006-THREAT-MODELING-RISK/
│   ├── CI-CA-D-006-001-TARA-ISO21434-TEMPLATES/
│   ├── CI-CA-D-006-002-STRIDE-ATTACK-TREES/
│   ├── CI-CA-D-006-003-MISSION-HAZARD-MAPPING/
│   ├── CI-CA-D-006-004-RISK-METRICS-HEATMAPS/
│   ├── CI-CA-D-006-005-CONTROL-SET-TRACEABILITY/
│   └── README.md
│
├── CA-D-007-IDS-MONITORING-DETECTION/
│   ├── CI-CA-D-007-001-NIDS-ARINC-AFDX-TSN-SENSORS/
│   ├── CI-CA-D-007-002-HIDS-RTOS-LINUX-AGENTS/
│   ├── CI-CA-D-007-003-ANOMALY-ML-PROFILES/
│   ├── CI-CA-D-007-004-LOG-NORMALIZATION-SCHEMAS/
│   ├── CI-CA-D-007-005-DET-PUBLISHERS-WORM/
│   └── README.md
│
├── CA-D-008-SAFETY-ENGINEERING/
│   ├── CI-CA-D-008-001-FHA-FUNCTIONAL-HAZARD-ANALYSIS/
│   ├── CI-CA-D-008-002-PSSA-PRELIM-SAFETY-ASSESSMENT/
│   ├── CI-CA-D-008-003-SSA-SYSTEM-SAFETY-ASSESSMENT/
│   ├── CI-CA-D-008-004-FTA-FAULT-TREE-ANALYSIS/
│   ├── CI-CA-D-008-005-FMEA-FMECA-LIBRARY/
│   ├── CI-CA-D-008-006-SAFETY-REQUIREMENTS-RTM/
│   └── README.md
│
├── CA-D-009-FAULT-MANAGEMENT-FDI-SRM/
│   ├── CI-CA-D-009-001-FAULT-DETECTION-MONITORS/
│   ├── CI-CA-D-009-002-ISOLATION-DIAGNOSTIC-TREES/
│   ├── CI-CA-D-009-003-RECOVERY-SAFE-STATES/
│   ├── CI-CA-D-009-004-SIMPLEX-FALLBACK-MODES/
│   ├── CI-CA-D-009-005-ALERTING-POLICIES-DO178C/
│   └── README.md
│
├── CA-D-010-SECURE-SUPPLY-CHAIN/
│   ├── CI-CA-D-010-001-SBOM-SLSA-PROVENANCE/
│   ├── CI-CA-D-010-002-3RD-PARTY-COMPONENT-REVIEWS/
│   ├── CI-CA-D-010-003-CVE-VULN-MANAGEMENT/
│   ├── CI-CA-D-010-004-BUILD-HERMETICITY-CI-CD/
│   ├── CI-CA-D-010-005-HW-SERIALIZATION-TRACE/
│   └── README.md
│
├── CA-D-011-INCIDENT-RESPONSE-DRILLS/
│   ├── CI-CA-D-011-001-PLAYBOOKS-IR-ATM-AOC/
│   ├── CI-CA-D-011-002-TABLETOP-EXERCISES/
│   ├── CI-CA-D-011-003-RED-TEAM-EMULATION/
│   ├── CI-CA-D-011-004-POST-INCIDENT-DET-REPORTS/
│   ├── CI-CA-D-011-005-SERVICE-RESTORE-RUNBOOKS/
│   └── README.md
│
├── CA-D-012-GNSS-INTEGRITY-ANTI-JAM/
│   ├── CI-CA-D-012-001-RAIM-SBAS-CHECKS/
│   ├── CI-CA-D-012-002-ANTI-SPOOF-DETECTION/
│   ├── CI-CA-D-012-003-ANTENNA-PLACEMENT-AJ-STRATEGY/
│   ├── CI-CA-D-012-004-TIME-SYNC-HOLDOVER-PROFILES/
│   ├── CI-CA-D-012-005-INTEGRITY-ALERTING-THRESHOLDS/
│   └── README.md
│
├── CA-D-013-QUANTUM-SECURITY-INTERFACES/
│   ├── CI-CA-D-013-001-QKD-GW-ABSTRACTIONS/
│   ├── CI-CA-D-013-002-QSAFE-POLICY-COMPAT-MATRIX/
│   ├── CI-CA-D-013-003-QPU-CONTAINMENT-BOUNDARIES/
│   ├── CI-CA-D-013-004-QAL-RESULT-VALIDATION-RULES/
│   ├── CI-CA-D-013-005-DET-FORENSICS-QUANTUM/
│   └── README.md
│
├── CA-D-014-PHYSICAL-SECURITY-ANTI-TAMPER/
│   ├── CI-CA-D-014-001-TAMPER-EVIDENT-SEALS/
│   ├── CI-CA-D-014-002-MESH-TAMPER-SWITCHES/
│   ├── CI-CA-D-014-003-LOCKOUT-TAGOUT-INTERLOCKS/
│   ├── CI-CA-D-014-004-ACCESS-CONTROL-HARDWARE/
│   ├── CI-CA-D-014-005-STORAGE-TRANSPORT-SECURITY/
│   └── README.md
│
├── CA-D-015-REGULATORY-COMPLIANCE/
│   ├── CI-CA-D-015-001-DO326A-ED202A-CHECKLISTS/
│   ├── CI-CA-D-015-002-DO356A-AIRWORTHY-SEC-GUIDE/
│   ├── CI-CA-D-015-003-ARP4754A-4761A-MAPPING/
│   ├── CI-CA-D-015-004-ISO21434-IEC62443-CROSSREF/
│   ├── CI-CA-D-015-005-AUDIT-PACKS-DET-INDEX/
│   └── README.md
│
└── README.md
```

### Límites y cruces de dominio (para no pisar otras áreas)

* **E3-ELECTRONICS**: controladores/ECUs, sensores electrónicos y diseño de PCBs → E3.
  *Aquí nos quedamos con políticas, criptografía, gateways, detección y hardening a nivel de sistema.*
* **O-OPERATING\_SYSTEMS**: particionado ARINC, RTOS, QAL runtime, UIs → O.
  *Desde D definimos requisitos de seguridad/ciber y evidencias a cumplir por O.*
* **L2-LINKS & COMMS**: performance/protoco los RF/GNSS → L2.
  *En D fijamos integridad y medidas anti-spoof/anti-jam (política y verificación).*
* **I-INTELLIGENT / M-MACHINE**: detección con ML y agentes autónomos se alojan allí;
  *en D definimos los invariantes de seguridad, límites y explicabilidad que deben respetar.*



Ruta canónica:
`OPTIME-FRAMEWORK/T-TECHNOLOGICAL/AMEDEO-PELLICCIA/INTEGRATED/AMPEL360-H2-BWB-QNNN/E2-ENERGY_AND_RENEWABLE/`

```text
E2-ENERGY_AND_RENEWABLE/
├── CA-E2-001-POWER-ARCHITECTURE/
│   ├── CI-CA-E2-001-001-BUS-TOPOLOGIES-HVDC-MVDC-LVDC/
│   ├── CI-CA-E2-001-002-GALLEY-AND-SERVICE-BRANCHES/
│   ├── CI-CA-E2-001-003-SEGREGATION-ZONES-ISOLATION/
│   ├── CI-CA-E2-001-004-FAULT-LEVELS-PROTECTION-COORD/
│   ├── CI-CA-E2-001-005-ENERGY-NOMENCLATURE-SCHEMAS/
│   └── README.md
│
├── CA-E2-002-FUEL-CELL-POWERPLANT/
│   ├── CI-CA-E2-002-001-FC-STACK-MODULE-ENVELOPES/
│   ├── CI-CA-E2-002-002-ANODE-CATHODE-MANIFOLDS/
│   ├── CI-CA-E2-002-003-HUMIDIFIERS-WATER-MGMT/
│   ├── CI-CA-E2-002-004-VENTS-PURGE-LINES-ROUTING/
│   ├── CI-CA-E2-002-005-STARTUP-SHUTDOWN-LOGIC-IFC/
│   ├── CI-CA-E2-002-006-FC-STACK-ISOLATION-INTERLOCKS/
│   └── README.md
│
├── CA-E2-003-H2-DISTRIBUTION-NONCRYO/
│   ├── CI-CA-E2-003-001-REGULATORS-VALVES-ARRAYS/
│   ├── CI-CA-E2-003-002-MANIFOLDS-PIPING-SUPPORTS/
│   ├── CI-CA-E2-003-003-VENT-AND-RELIEF-PATHS/
│   ├── CI-CA-E2-003-004-LEAK-SEGMENTATION-TOPOLOGY/
│   ├── CI-CA-E2-003-005-DRIP-PANS-DRAINAGE-INTERFACES/
│   └── README.md
│
├── CA-E2-004-POWER-CONVERSION-DISTRIBUTION/
│   ├── CI-CA-E2-004-001-DC-DC-ISOLATED-MODULES/
│   ├── CI-CA-E2-004-002-DC-AC-INVERTERS-400HZ/
│   ├── CI-CA-E2-004-003-PDU-PRIMARY-SECONDARY/
│   ├── CI-CA-E2-004-004-FUSE-BREAKER-SELECTIVITY/
│   ├── CI-CA-E2-004-005-HVIL-HIGH-VOLT-INTERLOCK-LOOPS/
│   ├── CI-CA-E2-004-006-HARNESS-POWER-ROUTING/
│   └── README.md
│
├── CA-E2-005-BATTERY-SYSTEMS/
│   ├── CI-CA-E2-005-001-CELL-CHEMISTRY-SELECTION/
│   ├── CI-CA-E2-005-002-PACK-ARCH-VENTING-PATHS/
│   ├── CI-CA-E2-005-003-THERMAL-RUNAWAY-CONTAINMENT/
│   ├── CI-CA-E2-005-004-MECHANICAL-ISOLATION-MOUNTS/
│   ├── CI-CA-E2-005-005-BMS-INTERFACE-REQUIREMENTS/
│   └── README.md
│
├── CA-E2-006-ENERGY-MANAGEMENT-EMS/
│   ├── CI-CA-E2-006-001-POWER-BUDGETS-NOMINAL-EMER/
│   ├── CI-CA-E2-006-002-LOAD-SHEDDING-POLICIES/
│   ├── CI-CA-E2-006-003-STATE-OF-ENERGY-SOE-MODEL/
│   ├── CI-CA-E2-006-004-EMS-API-TO-FC-BMS-PDU/
│   ├── CI-CA-E2-006-005-ENERGY-AS-POLICY-RULES/
│   └── README.md
│
├── CA-E2-007-THERMAL-ENERGY-RECOVERY/
│   ├── CI-CA-E2-007-001-TEG-THERMOELECTRIC-MODULES/
│   ├── CI-CA-E2-007-002-HEAT-EXCHANGERS-WASTE-HEAT/
│   ├── CI-CA-E2-007-003-LOOPS-COOLANT-INTERFACES/
│   ├── CI-CA-E2-007-004-VALVING-BYPASS-STRATEGIES/
│   ├── CI-CA-E2-007-005-COUPLING-TO-ECS-RAM-AIR/
│   └── README.md
│
├── CA-E2-008-RENEWABLE-SOURCES-ONBOARD/
│   ├── CI-CA-E2-008-001-PV-AEROSKIN-TILES/
│   ├── CI-CA-E2-008-002-MPPT-INTERFACE-REQS/
│   ├── CI-CA-E2-008-003-PV-ROUTING-PROTECTION/
│   ├── CI-CA-E2-008-004-STRUCTURAL-INTEGRATION-GUIDES/
│   ├── CI-CA-E2-008-005-ENERGY-HARVESTING-VIBRATION/
│   └── README.md
│
├── CA-E2-009-ELECTRIC-PROPULSION-INTERFACES/
│   ├── CI-CA-E2-009-001-MOTOR-INVERTER-POWER-IFC/
│   ├── CI-CA-E2-009-002-FEEDERS-AND-RETURN-PATHS/
│   ├── CI-CA-E2-009-003-EMI-FILTERING-POWER-SIDE/
│   ├── CI-CA-E2-009-004-COOLING-IFC-NONCRYO/
│   ├── CI-CA-E2-009-005-FAULT-CONTAINMENT-ZONES/
│   └── README.md
│
├── CA-E2-010-GROUND-POWER-CHARGING-REFUEL/
│   ├── CI-CA-E2-010-001-GPU-400HZ-28V-INTERFACES/
│   ├── CI-CA-E2-010-002-DC-FAST-CHARGE-COUPLERS/
│   ├── CI-CA-E2-010-003-H2-REFUEL-COUPLING-NONCRYO/
│   ├── CI-CA-E2-010-004-INTERLOCKS-EARTH-BONDING/
│   ├── CI-CA-E2-010-005-GROUND-SAFETY-RUNUP-PADS/
│   └── README.md
│
├── CA-E2-011-POWER-QUALITY-AND-HARMONICS/
│   ├── CI-CA-E2-011-001-THD-LIMITS-SPECTRA/
│   ├── CI-CA-E2-011-002-FILTERS-LCL-LC-SELECTION/
│   ├── CI-CA-E2-011-003-TRANSIENTS-RIDE-THROUGH/
│   ├── CI-CA-E2-011-004-INRUSH-CONTROL-PROFILES/
│   ├── CI-CA-E2-011-005-EMISSIONS-IMMUNITY-DO160/
│   └── README.md
│
├── CA-E2-012-MEASUREMENT-METERING/
│   ├── CI-CA-E2-012-001-METERING-POINTS-PLACEMENT/
│   ├── CI-CA-E2-012-002-CURRENT-SHUNTS-CT-HV/
│   ├── CI-CA-E2-012-003-VOLTAGE-TAPS-PROTECTION/
│   ├── CI-CA-E2-012-004-ENERGY-ACCOUNTING-LEDGER/
│   ├── CI-CA-E2-012-005-DATA-QUALITY-VALIDATION/
│   └── README.md
│
├── CA-E2-013-SAFETY-ISOLATION-PROTECTION/
│   ├── CI-CA-E2-013-001-INSULATION-RESIST-MONITORING/
│   ├── CI-CA-E2-013-002-ARC-FAULT-DETECTION-ZONING/
│   ├── CI-CA-E2-013-003-GALVANIC-ISOLATION-PATHS/
│   ├── CI-CA-E2-013-004-EARTHING-BONDING-REQUIREMENTS/
│   ├── CI-CA-E2-013-005-HAZARD-LABELS-PLACARDS/
│   └── README.md
│
├── CA-E2-014-ENERGY-SCHEDULING-OPTIMIZATION/
│   ├── CI-CA-E2-014-001-MISSION-PROFILES-ENERGY-GLIDES/
│   ├── CI-CA-E2-014-002-COST-RISK-MODELS-CVAR/
│   ├── CI-CA-E2-014-003-FLEET-LEVEL-OPT-QAL-IFC/
│   ├── CI-CA-E2-014-004-MRO-ENERGY-IMPACT-METRICS/
│   ├── CI-CA-E2-014-005-CO2-POLICIES-EAP-ENFORCERS/
│   └── README.md
│
└── README.md
```

### Límites y cruces de dominio (para que no haya solapes)

* **C2-CRYOGENICS**: tanques LH₂, intercambiadores criogénicos, líneas subenfriadas y criostatía → **C2**.
  *En E2 gestionamos distribución **no criogénica**, conversión de potencia y política energética.*
* **E3-ELECTRONICS**: BMS, controladores de convertidores, sensórica electrónica → **E3**.
  *E2 define interfaces, topologías, rutas y requisitos de potencia; la electrónica vive en E3.*
* **E1-ENVIRONMENTAL**: ECS/ram-air y térmica de cabina → **E1**.
  *E2 sólo trata recuperación térmica y acoplos energéticos (no el acondicionamiento ambiental).*
* **O-OPERATING\_SYSTEMS**: EMS runtime, orquestación, QAL, DET → **O**.
  *E2 define contratos energéticos y puntos de medida; la ejecución vive en O.*
* **D-DEFENCE/CYBER**: HVIL políticas, FAT/attestation, cifrado de telemetría energética → **D**.


**Ruta canónica:**
`OPTIME-FRAMEWORK/T-TECHNOLOGICAL/AMEDEO-PELLICCIA/INTEGRATED/AMPEL360-H2-BWB-QNNN/O-OPERATING_SYSTEMS_NAVIGATION_HPC/`

```text
O-OPERATING_SYSTEMS_NAVIGATION_HPC/
├── CA-O-001-AQUA-OS-BRIDGE-CORE/
│   ├── CI-CA-O-001-001-CONTROL-PLANE-ARCH/
│   ├── CI-CA-O-001-002-PARTITION-MANAGER/
│   ├── CI-CA-O-001-003-SERVICE-REGISTRY/
│   ├── CI-CA-O-001-004-CONFIG-POLICY-ENGINE/
│   ├── CI-CA-O-001-005-RUNTIME-CONTRACTS-DIGITAL-TWIN/
│   └── README.md
│
├── CA-O-002-GAIA-AIR-RTOS/
│   ├── CI-CA-O-002-001-SCHEDULER-HTS/
│   ├── CI-CA-O-002-002-TIME-SLOTS-ARINC653/
│   ├── CI-CA-O-002-003-INTERRUPT-CONTROLLER/
│   ├── CI-CA-O-002-004-DRIVERS-HAL-CRITICAL/
│   ├── CI-CA-O-002-005-WCET-PROFILES/
│   └── README.md
│
├── CA-O-003-IMA-PARTITIONING-ARINC/
│   ├── CI-CA-O-003-001-PARTITION-LAYOUTS/
│   ├── CI-CA-O-003-002-HEALTH-MONITOR/
│   ├── CI-CA-O-003-003-INTERPARTITION-COMMS/
│   ├── CI-CA-O-003-004-STARTUP-RESET-SEQUENCES/
│   ├── CI-CA-O-003-005-CERT-ARTIFACTS-DO178C/
│   └── README.md
│
├── CA-O-004-TSN-TSP-TIME-SYNC/
│   ├── CI-CA-O-004-001-PTP-TSP-PROFILES/
│   ├── CI-CA-O-004-002-TSN-QBV-SCHEDULES/
│   ├── CI-CA-O-004-003-CLOCK-HOLDOVER-OCXO/
│   ├── CI-CA-O-004-004-TIMESTAMPING-APIs/
│   ├── CI-CA-O-004-005-SYNC-QUALITY-MONITOR/
│   └── README.md
│
├── CA-O-005-QAL-QUANTUM-ABSTRACTION-LAYER/
│   ├── CI-CA-O-005-001-QOPT-API-JOBS/
│   ├── CI-CA-O-005-002-QPU-BACKENDS-ADAPTERS/
│   ├── CI-CA-O-005-003-RESULT-VALIDATION-RULES/
│   ├── CI-CA-O-005-004-NON-RT-ISOLATION-BOUNDARY/
│   ├── CI-CA-O-005-005-QSIM-DRIVERS/
│   └── README.md
│
├── CA-O-006-DET-DIGITAL-EVIDENCE-TWIN/
│   ├── CI-CA-O-006-001-WORM-LOGGERS/
│   ├── CI-CA-O-006-002-EVIDENCE-PACK-FORMATS/
│   ├── CI-CA-O-006-003-HASH-ANCHORING-LEDGER/
│   ├── CI-CA-O-006-004-TRACEPOINTS-RUNTIME/
│   ├── CI-CA-O-006-005-DET-VIEWER-TOOLS/
│   └── README.md
│
├── CA-O-007-SERVICE-MESH-ORCHESTRATION/
│   ├── CI-CA-O-007-001-SIDECARS-PROXIES/
│   ├── CI-CA-O-007-002-CANARY-ROLLS-RBAC/
│   ├── CI-CA-O-007-003-RESILIENCE-CIRCUIT-BREAKERS/
│   ├── CI-CA-O-007-004-OBSERVABILITY-METRICS/
│   ├── CI-CA-O-007-005-POLICY-ENFORCERS/
│   └── README.md
│
├── CA-O-008-CAD-CAM-CAE-SCADA-BRIDGE/
│   ├── CI-CA-O-008-001-CAD-ADAPTERS-AP242-JT/
│   ├── CI-CA-O-008-002-CAM-TOOLPATH-CONTRACTS/
│   ├── CI-CA-O-008-003-CAE-CASE-EXCHANGE/
│   ├── CI-CA-O-008-004-SCADA-OPC-UA-ADAPTERS/
│   ├── CI-CA-O-008-005-ROS2-CELL-GATEWAY/
│   ├── CI-CA-O-008-006-TWIN-DIFF-PIPELINES/
│   └── README.md
│
├── CA-O-009-CaaS-CERTIFICATION-AS-A-SERVICE/
│   ├── CI-CA-O-009-001-REQUIREMENTS-RTM-API/
│   ├── CI-CA-O-009-002-TEST-EVIDENCE-INGEST/
│   ├── CI-CA-O-009-003-SAFETY-CASE-GSN-COMPILER/
│   ├── CI-CA-O-009-004-TOOL-QUAL-DO330/
│   ├── CI-CA-O-009-005-AUDIT-EXPORTS/
│   └── README.md
│
├── CA-O-010-MRO-EOL-PROCUREMENT-BRIDGE/
│   ├── CI-CA-O-010-001-MRO-WORKPACK-GENERATOR/
│   ├── CI-CA-O-010-002-SPARES-ERP-MES-ADAPTER/
│   ├── CI-CA-O-010-003-EOL-MATERIAL-RECOVERY/
│   ├── CI-CA-O-010-004-LIFE-LIMIT-LEDGER/
│   ├── CI-CA-O-010-005-COST-CO2-ACCOUNTING/
│   └── README.md
│
├── CA-O-011-LEGACY-BRIDGE-ARINC-AFDX/
│   ├── CI-CA-O-011-001-ARINC429-GATEWAYS/
│   ├── CI-CA-O-011-002-AFDX-VL-MAPPING/
│   ├── CI-CA-O-011-003-ARINC653-PARTITION-PROXIES/
│   ├── CI-CA-O-011-004-ICD-TRANSLATION-LAYER/
│   ├── CI-CA-O-011-005-BIT-BITE-INTF/
│   └── README.md
│
├── CA-O-012-NAVIGATION-RUNTIMES/
│   ├── CI-CA-O-012-001-NAV-STACK-API/
│   ├── CI-CA-O-012-002-SENSOR-FUSION-IFC/
│   ├── CI-CA-O-012-003-RAIM-INTEGRITY-HOOKS/
│   ├── CI-CA-O-012-004-MAP-DATABASE-ADAPTERS/
│   ├── CI-CA-O-012-005-TRAJECTORY-SERVICES/
│   └── README.md
│
├── CA-O-013-FBW-IO-GATEWAY-(PARTITIONED)/
│   ├── CI-CA-O-013-001-FBW-COMMAND-GUARDS/
│   ├── CI-CA-O-013-002-SENSOR-BUS-BRIDGE/
│   ├── CI-CA-O-013-003-HEALTH-HEARTBEAT-GATE/
│   ├── CI-CA-O-013-004-MODE-MANAGEMENT/
│   ├── CI-CA-O-013-005-ALERTING-CHANNELS/
│   └── README.md
│
├── CA-O-014-EFB-COCKPIT-APPS/
│   ├── CI-CA-O-014-001-EFB-FRAMEWORK/
│   ├── CI-CA-O-014-002-CHARTS-PIXMAP-ADAPTERS/
│   ├── CI-CA-O-014-003-PERF-CALCS-APP/
│   ├── CI-CA-O-014-004-CHECKLISTS-DET-LINK/
│   ├── CI-CA-O-014-005-MAINT-MSGING-APP/
│   └── README.md
│
├── CA-O-015-HPC-CLUSTER-ORCH/
│   ├── CI-CA-O-015-001-EDGE-NODES-RUNTIME/
│   ├── CI-CA-O-015-002-GROUND-CLUSTER-OPS/
│   ├── CI-CA-O-015-003-WORKLOAD-SCHEDULER/
│   ├── CI-CA-O-015-004-ACCEL-DRIVERS-GPU-FPGA/
│   ├── CI-CA-O-015-005-DATA-PIPELINES/
│   └── README.md
│
├── CA-O-016-ROS2-OPC-UA-BRIDGE/
│   ├── CI-CA-O-016-001-DDS-QOS-PROFILES/
│   ├── CI-CA-O-016-002-OPC-UA-NAMESPACE-MAPS/
│   ├── CI-CA-O-016-003-ROBOT-CELL-ADAPTERS/
│   ├── CI-CA-O-016-004-TEST-RIG-DRIVERS/
│   ├── CI-CA-O-016-005-SAFETY-INTERLOCK-API/
│   └── README.md
│
├── CA-O-017-ERP-MES-INTEGRATION/
│   ├── CI-CA-O-017-001-ORDER-API/
│   ├── CI-CA-O-017-002-MES-JOB-TICKETS/
│   ├── CI-CA-O-017-003-SPARES-LOGISTICS-HOOKS/
│   ├── CI-CA-O-017-004-QUALITY-COC-COA-INGEST/
│   ├── CI-CA-O-017-005-COMPLIANCE-REPORTERS/
│   └── README.md
│
├── CA-O-018-OBSERVABILITY/
│   ├── CI-CA-O-018-001-METRICS-REGISTRY/
│   ├── CI-CA-O-018-002-LOG-STRUCTURE-JSON-PB/
│   ├── CI-CA-O-018-003-TRACING-SPANS/
│   ├── CI-CA-O-018-004-ALERT-RULESETS/
│   ├── CI-CA-O-018-005-DASHBOARDS/
│   └── README.md
│
├── CA-O-019-PACKAGING-DISTRIBUTION/
│   ├── CI-CA-O-019-001-BUILD-SYSTEMS/
│   ├── CI-CA-O-019-002-SBOM-SUPPLY-CHAIN/
│   ├── CI-CA-O-019-003-OTA-UPDATE-CHANNELS/
│   ├── CI-CA-O-019-004-ARTIFACT-SIGNING/
│   ├── CI-CA-O-019-005-RELEASE-PROCEDURES/
│   └── README.md
│
├── CA-O-020-OS-UI-KITS/
│   ├── CI-CA-O-020-001-HMI-COMPONENTS/
│   ├── CI-CA-O-020-002-THEME-ACCESSIBILITY/
│   ├── CI-CA-O-020-003-INPUT-DEVICE-ABSTRACTIONS/
│   ├── CI-CA-O-020-004-DISPLAY-PIPELINE/
│   ├── CI-CA-O-020-005-LOCALIZATION/
│   └── README.md
│
└── README.md
```

### Límites y cruces (para no pisar otros dominios)

* **D-DEFENCE\_CYBERSECURITY\_SAFETY** → políticas de seguridad, PQC/KMS, attestation, IDS, cumplimiento.
  *Aquí (O) vive la **ejecución** del mesh, particionado, runtime, DET y bridges.*
* **L2-LINKS\_AND\_COMMUNICATIONS** → protocolos RF/sat, radios, GNSS, enlace físico.
  *En O están los **gateways** y APIs de integración con L2.*
* **E3-ELECTRONICS\_DIGITAL\_INSTRUMENTS** → ECUs, BMS, controladores, PCB.
  *O consume sus drivers/abstracciones y define contratos de servicio.*
* **E2-ENERGY\_AND\_RENEWABLE** → contratos energéticos y EMS;
  *O implementa el **runtime EMS** y orquestación de políticas (Energy-as-Policy).*


**Ruta canónica:**
`OPTIME-FRAMEWORK/T-TECHNOLOGICAL/AMEDEO-PELLICCIA/INTEGRATED/AMPEL360-H2-BWB-QNNN/P-PROPULSION_AND_FUELS/`

```text
P-PROPULSION_AND_FUELS/
├── CA-P-001-PROPULSOR-MODULE-EDF/
│   ├── CI-CA-P-001-001-ROTOR-STATOR-STAGES/
│   ├── CI-CA-P-001-002-BLADES-HUB-CONTAINMENT/
│   ├── CI-CA-P-001-003-DUCT-ACOUSTIC-LINERS/
│   ├── CI-CA-P-001-004-TIP-CLEARANCE-SEALS/
│   ├── CI-CA-P-001-005-SENSORS-VIB-ENCODER-IFC-(E3)/
│   └── README.md
│
├── CA-P-002-DISTRIBUTED-PROPULSION-PODS/
│   ├── CI-CA-P-002-001-POD-STRUCTURE-MOUNTS/
│   ├── CI-CA-P-002-002-POWER-AND-RETURN-FEEDERS-(E2)/
│   ├── CI-CA-P-002-003-COOLING-JACKETS-NONCRYO/
│   ├── CI-CA-P-002-004-EMI-SHIELDING-ROUTING-(E3)/
│   ├── CI-CA-P-002-005-QUICK-ACCESS-DOORS/
│   └── README.md
│
├── CA-P-003-BLI-INLETS-DIFFUSERS/
│   ├── CI-CA-P-003-001-LIP-GEOMETRY-ANTI-ICE-IFC-(E1)/
│   ├── CI-CA-P-003-002-BOUNDARY-LAYER-MANAGEMENT/
│   ├── CI-CA-P-003-003-DIFFUSER-DISTORTION-GRIDS/
│   ├── CI-CA-P-003-004-S-DUCT-INSTRUMENTATION-(E3)/
│   ├── CI-CA-P-003-005-INSPECTION-PANELS/
│   └── README.md
│
├── CA-P-004-NACELLES-PYLONS-GONDOLAS/
│   ├── CI-CA-P-004-001-PRIMARY-STRUCTURE-ATTACH/
│   ├── CI-CA-P-004-002-FIRE-ZONES-INSULATION-(D)/
│   ├── CI-CA-P-004-003-ANTI-ICE-DRAINS-(E1)/
│   ├── CI-CA-P-004-004-ACCESS-AND-MAINT-DOORS/
│   ├── CI-CA-P-004-005-ACOUSTIC-TREATMENTS/
│   └── README.md
│
├── CA-P-005-THRUST-MANAGEMENT/
│   ├── CI-CA-P-005-001-VARIABLE-PITCH-MECHANISMS/
│   ├── CI-CA-P-005-002-REVERSING-MODES-EDF/
│   ├── CI-CA-P-005-003-THRUST-VECTORING-NOZZLES/
│   ├── CI-CA-P-005-004-LIMITS-PROTECTIONS-(D)/
│   ├── CI-CA-P-005-005-FADEC-INTERFACE-(E3,O)/
│   └── README.md
│
├── CA-P-006-H2-TURBINE-CORE-(OPTIONAL)/
│   ├── CI-CA-P-006-001-COMPRESSOR-SYSTEMS/
│   ├── CI-CA-P-006-002-PREMIX-INJECTORS-H2-FLASHBACK/
│   ├── CI-CA-P-006-003-COMBUSTOR-LINERS-COOLING/
│   ├── CI-CA-P-006-004-TURBINE-STAGES-COOLING/
│   ├── CI-CA-P-006-005-IGNITION-FUEL-CONTROL-(E3,E2)/
│   └── README.md
│
├── CA-P-007-FINAL-FUEL-CONDITIONING-METERING/
│   ├── CI-CA-P-007-001-WARM-UP-HX-VAPORIZERS-(C2->P)/
│   ├── CI-CA-P-007-002-PRESSURE-REG-TRIM-VALVES/
│   ├── CI-CA-P-007-003-METERING-RAILS-INJECTORS/
│   ├── CI-CA-P-007-004-PURGE-VENT-NEAR-ENGINE/
│   ├── CI-CA-P-007-005-FLAME-ARRESTERS-RETURN/
│   └── README.md
│
├── CA-P-008-MOTOR-INTEGRATION-(ELECTRIC)/
│   ├── CI-CA-P-008-001-MOUNTS-ISOLATORS/
│   ├── CI-CA-P-008-002-GEARBOX-OPTIONAL-DRIVES/
│   ├── CI-CA-P-008-003-THERMAL-PATHS-COOLING/
│   ├── CI-CA-P-008-004-ENCODER-RESOLVER-IFC-(E3)/
│   ├── CI-CA-P-008-005-EMI-BONDING-HVIL-(E2,D)/
│   └── README.md
│
├── CA-P-009-TRANSMISSION-GEARBOX-DRIVES/
│   ├── CI-CA-P-009-001-GEARS-BEARINGS-LUBE/
│   ├── CI-CA-P-009-002-TORQUE-SENSORS-CHIP-DETECT-(E3)/
│   ├── CI-CA-P-009-003-CONTAINMENT-CASING/
│   ├── CI-CA-P-009-004-COOLING-LUBE-INTERFACES-(E1)/
│   ├── CI-CA-P-009-005-MAINT-ACCESS-PORTS/
│   └── README.md
│
├── CA-P-010-STARTING-APU-ALTERNATIVES/
│   ├── CI-CA-P-010-001-E-START-CONVERTERS-(E2,E3)/
│   ├── CI-CA-P-010-002-FUEL-CELL-ASSIST-START/
│   ├── CI-CA-P-010-003-H2-APU-ENCLOSURE-(D)/
│   ├── CI-CA-P-010-004-START-SEQUENCES-LOGIC-(O)/
│   ├── CI-CA-P-010-005-INTERLOCKS-GROUND-SAFETY/
│   └── README.md
│
├── CA-P-011-EXHAUST-PLUMES-ACOUSTICS/
│   ├── CI-CA-P-011-001-MIXERS-DEFLECTORS/
│   ├── CI-CA-P-011-002-ACOUSTIC-LINERS-DUCT-END/
│   ├── CI-CA-P-011-003-IR-SIGNATURE-MANAGEMENT-(D)/
│   ├── CI-CA-P-011-004-CONDENSATE-MGMT-ICING-(E1)/
│   ├── CI-CA-P-011-005-PLUME-SENSORS-(E3)/
│   └── README.md
│
├── CA-P-012-ICE-PROTECTION-PROPULSOR/
│   ├── CI-CA-P-012-001-ELECTRO-THERMAL-ANTI-ICE/
│   ├── CI-CA-P-012-002-BLEED-HOT-AIR-IFC-(TURBINE)/
│   ├── CI-CA-P-012-003-DE-ICE-BOOTS-EDF/
│   ├── CI-CA-P-012-004-ICE-DETECT-SENSORS-(E3)/
│   ├── CI-CA-P-012-005-CONTROL-LOGIC-BOUNDARIES-(O)/
│   └── README.md
│
├── CA-P-013-FIRE-DETECTION-SUPPRESSION/
│   ├── CI-CA-P-013-001-FIRE-ZONES-CLASSIFICATION/
│   ├── CI-CA-P-013-002-DETECT-LOOPS-TEST-PORTS-(E3)/
│   ├── CI-CA-P-013-003-BOTTLES-DISCHARGE-LINES/
│   ├── CI-CA-P-013-004-VENT-ROUTING-SAFETY-(D)/
│   ├── CI-CA-P-013-005-MAINT-INSPECTION-PROVISIONS/
│   └── README.md
│
├── CA-P-014-PROP-HEALTH-MONITORING-(PHM)/
│   ├── CI-CA-P-014-001-VIBRATION-SPECTRA/
│   ├── CI-CA-P-014-002-BEARING-TEMP-TRENDS/
│   ├── CI-CA-P-014-003-BLADE-DAMAGE-INDICATORS/
│   ├── CI-CA-P-014-004-RUL-MODELS-INTERFACES-(O)/
│   ├── CI-CA-P-014-005-DATA-QUALITY-(D,E3)/
│   └── README.md
│
├── CA-P-015-CONTROL-INTERFACES-(FADEC)/
│   ├── CI-CA-P-015-001-FADEC-HW-SW-BOUNDARY-(E3,O)/
│   ├── CI-CA-P-015-002-THRUST-COMMAND-APIs-(O)/
│   ├── CI-CA-P-015-003-LIMIT-PROTECTION-TABLES-(D)/
│   ├── CI-CA-P-015-004-DATA-BUS-ARINC-AFDX-MAPPING-(L2)/
│   ├── CI-CA-P-015-005-LOGGING-DET-HOOKS-(O)/
│   └── README.md
│
├── CA-P-016-GROUND-TEST-INSTALLATION/
│   ├── CI-CA-P-016-001-THRUST-STAND-IFC/
│   ├── CI-CA-P-016-002-ALIGNMENT-JIGS/
│   ├── CI-CA-P-016-003-RUNUP-PROCEDURES-(PPE-D)/
│   ├── CI-CA-P-016-004-DAQ-HIGH-RATE-(E3)/
│   ├── CI-CA-P-016-005-DET-EVIDENCE-PACKS-(O)/
│   └── README.md
│
├── CA-P-017-HYBRID-ARCHITECTURE-(SERIES-PARALLEL)/
│   ├── CI-CA-P-017-001-POWER-SPLIT-DEVICE/
│   ├── CI-CA-P-017-002-CLUTCHING-MODES/
│   ├── CI-CA-P-017-003-MODE-MANAGER-API-(O,E2)/
│   ├── CI-CA-P-017-004-FAILSAFE-PATHS-(D)/
│   ├── CI-CA-P-017-005-INTEGRATION-WITH-EMS-(E2)/
│   └── README.md
│
├── CA-P-018-FUEL-QUALITY-SPECS-(H2)/
│   ├── CI-CA-P-018-001-ISO-14687-LIMITS/
│   ├── CI-CA-P-018-002-DEWPOINT-AND-MOISTURE/
│   ├── CI-CA-P-018-003-PARTICULATE-LIMITS/
│   ├── CI-CA-P-018-004-SAMPLING-PORTS-PROTOCOLS/
│   ├── CI-CA-P-018-005-QUALITY-EVIDENCE-LEDGER-(O)/
│   └── README.md
│
├── CA-P-019-VENTING-PURGING-STRATEGIES/
│   ├── CI-CA-P-019-001-PURGE-CYCLES-NEAR-ENGINE/
│   ├── CI-CA-P-019-002-VENT-STACKS-FLAME-ARRESTERS/
│   ├── CI-CA-P-019-003-ESD-BONDING-POINTS-(D)/
│   ├── CI-CA-P-019-004-HAZARD-ZONE-CLASSIFICATION-(D)/
│   ├── CI-CA-P-019-005-DET-ALARM-ROUTES-(O)/
│   └── README.md
│
├── CA-P-020-CERTIFICATION-MAPPING/
│   ├── CI-CA-P-020-001-CS25-PART33-ENGINE-RULES/
│   ├── CI-CA-P-020-002-DO160-ENVIRON-QUAL/
│   ├── CI-CA-P-020-003-FIRE-PROTECTION-SUBPARTS/
│   ├── CI-CA-P-020-004-EMI-HIRF-LIGHTNING-(D)/
│   ├── CI-CA-P-020-005-CONTINUED-AIRWORTHINESS/
│   └── README.md
│
└── README.md
```

### Límites (para no solapar dominios)

* **C2-CRYOGENICS:** tanques LH₂, líneas criogénicas y vaporización primaria → C2.
  *P gestiona el **acondicionamiento final** y la **dosificación** hacia motor/inyectores.*
* **E2-ENERGY:** distribución no criogénica, conversión de potencia, EMS → E2.
  *P consume potencia/contratos de energía y define interfaces de propulsor.*
* **E3-ELECTRONICS:** FADEC/ECU, sensórica, drivers → E3.
  *P define **interfaces** y requisitos de instalación/EMI; la electrónica vive en E3.*
* **D-DEFENCE/SAFETY:** zonas de fuego, ESD/HAZLOC, límites y protecciones.
* **O-OPERATING\_SYSTEMS:** control lógico, modos, DET y orquestación runtime.

**Ruta canónica**
`OPTIME-FRAMEWORK/T-TECHNOLOGICAL/AMEDEO-PELLICCIA/INTEGRATED/AMPEL360-H2-BWB-QNNN/E3-ELECTRONICS_DIGITAL_INSTRUMENTS/`

```text
E3-ELECTRONICS_DIGITAL_INSTRUMENTS/
├── CA-E3-001-AVIONICS-LRU-CCAs/
│   ├── CI-CA-E3-001-001-COMPUTE-CCA-CPU-GPU-FPGA
│   ├── CI-CA-E3-001-002-MEM-NVM-SUPERVISORS
│   ├── CI-CA-E3-001-003-POWER-ENTRY-PROTECTION-(E2)
│   ├── CI-CA-E3-001-004-BACKPLANE-INTERFACE
│   ├── CI-CA-E3-001-005-CONFIG-JUMPERS-SECURE-BOOT-(D)
│   └── README.md
│
├── CA-E3-002-POWER-ELECTRONICS-DRIVES/
│   ├── CI-CA-E3-002-001-INVERTERS-EDF-MOTOR
│   ├── CI-CA-E3-002-002-IGBT-MOSFET-MODULES
│   ├── CI-CA-E3-002-003-GATE-DRIVERS-ISOLATION
│   ├── CI-CA-E3-002-004-DESAT-OVERCURRENT-PROTECTION-(D)
│   ├── CI-CA-E3-002-005-DC-LINK-CAP-BUSBAR-(E2)
│   └── README.md
│
├── CA-E3-003-SENSOR-SUITES-AIR-DATA-IMU/
│   ├── CI-CA-E3-003-001-PITOT-STATIC-ADC-CHAIN
│   ├── CI-CA-E3-003-002-AOA-VANE-ENCODER
│   ├── CI-CA-E3-003-003-IMU-IMU-FILTERING
│   ├── CI-CA-E3-003-004-BARO-TEMP-HUMIDITY
│   ├── CI-CA-E3-003-005-CAL-BENCH-PORTS
│   └── README.md
│
├── CA-E3-004-ENGINE-CONTROL-FADEC-HW/
│   ├── CI-CA-E3-004-001-FADEC-MAIN-BOARD
│   ├── CI-CA-E3-004-002-ANALOG-INJECTOR-IO
│   ├── CI-CA-E3-004-003-SPEED-TEMP-PRESS-SENSORS
│   ├── CI-CA-E3-004-004-REDUNDANCY-VOTING-(D)
│   ├── CI-CA-E3-004-005-DATA-BUS-IFC-(L2,O)
│   └── README.md
│
├── CA-E3-005-IO-MODULES-ACTUATOR-DRIVERS/
│   ├── CI-CA-E3-005-001-LVDT-RVDT-EXCITATION
│   ├── CI-CA-E3-005-002-SERVO-VALVE-DRIVERS
│   ├── CI-CA-E3-005-003-HBRIDGE-LINEAR-STAGE
│   ├── CI-CA-E3-005-004-FAILSAFE-RELAY-LATCH-(D)
│   ├── CI-CA-E3-005-005-STATUS-LED-TESTPOINTS
│   └── README.md
│
├── CA-E3-006-DATA-ACQUISITION-HI-RATE/
│   ├── CI-CA-E3-006-001-DAQ-ADC-CARDS
│   ├── CI-CA-E3-006-002-SYNC-TRIGGER-LINES
│   ├── CI-CA-E3-006-003-HIGH-SPEED-LOGGERS
│   ├── CI-CA-E3-006-004-BUFFERING-LOSSLESS
│   ├── CI-CA-E3-006-005-DET-WRITERS-(O)
│   └── README.md
│
├── CA-E3-007-TIMING-CLOCKING-PLL/
│   ├── CI-CA-E3-007-001-10MHZ-REF-DISTRIBUTION
│   ├── CI-CA-E3-007-002-PPS-FANOUT
│   ├── CI-CA-E3-007-003-PTP-HW-NICs-(O)
│   ├── CI-CA-E3-007-004-OCXO-HOLDOVER
│   ├── CI-CA-E3-007-005-JITTER-MONITOR
│   └── README.md
│
├── CA-E3-008-EMC-ESD-LIGHTNING/
│   ├── CI-CA-E3-008-001-FILTER-PI-INPUT
│   ├── CI-CA-E3-008-002-COMMON-MODE-CHOKES
│   ├── CI-CA-E3-008-003-SURGE-TVS-LIGHTNING-(D)
│   ├── CI-CA-E3-008-004-CABLE-SHIELD-TERMINATION
│   ├── CI-CA-E3-008-005-GROUNDING-BONDING
│   └── README.md
│
├── CA-E3-009-LV-POWER-REGULATION/
│   ├── CI-CA-E3-009-001-ISOLATED-DC-DC-(E2)
│   ├── CI-CA-E3-009-002-LDO-POINT-OF-LOAD
│   ├── CI-CA-E3-009-003-ORING-FET-REDUNDANCY
│   ├── CI-CA-E3-009-004-POWER-GOOD-SEQUENCERS
│   ├── CI-CA-E3-009-005-THERMAL-SENSING
│   └── README.md
│
├── CA-E3-010-PCB-DESIGN-STACKUPS/
│   ├── CI-CA-E3-010-001-STACKUP-RF-ANALOG-MIXED
│   ├── CI-CA-E3-010-002-IMPEDANCE-CONTROL
│   ├── CI-CA-E3-010-003-COUPLING-AND-ISOLATION
│   ├── CI-CA-E3-010-004-DDR-PCIe-ROUTING
│   ├── CI-CA-E3-010-005-DFM-DFT-GUIDES
│   └── README.md
│
├── CA-E3-011-CONNECTORS-HARNESS/
│   ├── CI-CA-E3-011-001-CIRCULAR-ARINC-MIL
│   ├── CI-CA-E3-011-002-EDGE-MEZZANINE
│   ├── CI-CA-E3-011-003-HARNESS-SPEC-BUNDLES
│   ├── CI-CA-E3-011-004-STRAIN-RELIEF
│   ├── CI-CA-E3-011-005-TEST-HARNESS-KITS
│   └── README.md
│
├── CA-E3-012-RACKS-CHASSIS-THERMAL/
│   ├── CI-CA-E3-012-001-ATR-ARINC-ENCLOSURES
│   ├── CI-CA-E3-012-002-VIBRATION-MOUNTS
│   ├── CI-CA-E3-012-003-LIQUID-AIR-COOL-PLATES
│   ├── CI-CA-E3-012-004-HOT-SWAP-CADDIES
│   ├── CI-CA-E3-012-005-EMI-GASKETS
│   └── README.md
│
├── CA-E3-013-DISPLAYS-INSTRUMENT-DRIVERS/
│   ├── CI-CA-E3-013-001-LCD-OLED-TCON-BOARDS
│   ├── CI-CA-E3-013-002-BACKLIGHT-PSU-(E2)
│   ├── CI-CA-E3-013-003-SENSOR-INPUT-BOARDS
│   ├── CI-CA-E3-013-004-REDUNDANT-VIDEO-PATHS-(L2)
│   ├── CI-CA-E3-013-005-BIT-TEST-PATTERNS
│   └── README.md
│
├── CA-E3-014-BIT-BITE-MONITORING/
│   ├── CI-CA-E3-014-001-POWER-ON-SELF-TEST
│   ├── CI-CA-E3-014-002-LINE-REPLACEABLE-DIAGS
│   ├── CI-CA-E3-014-003-SENSOR-LOOPBACKS
│   ├── CI-CA-E3-014-004-FAULT-LOG-MIRROR-(O)
│   ├── CI-CA-E3-014-005-MAINT-PORTS
│   └── README.md
│
├── CA-E3-015-SAFETY-INTERLOCK-HW/
│   ├── CI-CA-E3-015-001-HARDWIRED-INTERLOCKS
│   ├── CI-CA-E3-015-002-EMERGENCY-STOP-CHAINS
│   ├── CI-CA-E3-015-003-OVERSPEED-TRIPS
│   ├── CI-CA-E3-015-004-ESD-HVIL-LATCHING
│   ├── CI-CA-E3-015-005-FAILSAFE-POWER-CUT
│   └── README.md
│
├── CA-E3-016-PRODUCTION-TEST-INTERFACES/
│   ├── CI-CA-E3-016-001-JTAG-SWD-BOUNDARY
│   ├── CI-CA-E3-016-002-FUNCTIONAL-TEST-FIXTURES
│   ├── CI-CA-E3-016-003-ICT-FLYING-PROBE
│   ├── CI-CA-E3-016-004-EEPROM-CAL-SLOTS
│   ├── CI-CA-E3-016-005-PROG-CONNECTOR-KEYING
│   └── README.md
│
├── CA-E3-017-NETWORK-INTERFACES-ARINC-AFDX-TSN/
│   ├── CI-CA-E3-017-001-ARINC429-TRANSCEIVERS-(L2)
│   ├── CI-CA-E3-017-002-AFDX-ENET-MAC-PHY-(L2)
│   ├── CI-CA-E3-017-003-TSN-NIC-QBV-QCI-(O)
│   ├── CI-CA-E3-017-004-BUS-ISOLATION-REDUNDANCY
│   ├── CI-CA-E3-017-005-CABLE-PLANT-QUAL
│   └── README.md
│
├── CA-E3-018-MOTOR-SENSING-ENCODER-ASIC/
│   ├── CI-CA-E3-018-001-RESOLVER-EXCITATION-DEMOD
│   ├── CI-CA-E3-018-002-HALL-EFFECT-ARRAYS
│   ├── CI-CA-E3-018-003-OPTICAL-ENCODER-IFC
│   ├── CI-CA-E3-018-004-CAL-AND-LINEARIZATION
│   ├── CI-CA-E3-018-005-EMC-IMMUNITY
│   └── README.md
│
├── CA-E3-019-FUEL-MEASUREMENT-TRANSDUCERS/
│   ├── CI-CA-E3-019-001-MASS-FLOW-H2-(C2->E3)
│   ├── CI-CA-E3-019-002-PRESSURE-TX-CRYO-SAFE-(C2)
│   ├── CI-CA-E3-019-003-TEMP-SENSING-CRYO-(C2)
│   ├── CI-CA-E3-019-004-LEAK-DETECT-ECHELON-(D)
│   ├── CI-CA-E3-019-005-CAL-AND-TRACEABILITY-(O)
│   └── README.md
│
├── CA-E3-020-HARDWARE-SECURITY-HSM/
│   ├── CI-CA-E3-020-001-ROOT-OF-TRUST-TPM
│   ├── CI-CA-E3-020-002-SECURE-BOOT-CRYPTO-(D)
│   ├── CI-CA-E3-020-003-KEYSTORES-PQC-READY-(D)
│   ├── CI-CA-E3-020-004-ANTI-TAMPER-MESH
│   ├── CI-CA-E3-020-005-ATTESTATION-PERIPHERALS-(O)
│   └── README.md
│
└── README.md
```

### Límites entre dominios (para no pisarnos)

* **L2-LINKS\_AND\_COMMUNICATIONS:** radios/RF/GNSS/transceptores → L2; aquí (E3) solo el **hardware de interfaz** de bus y PHYs genéricos.
* **O-OPERATING\_SYSTEMS\_NAVIGATION\_HPC:** runtime/OS, malla de servicios, DET, QAL → O; E3 provee **el hardware** que O gobierna.
* **D-DEFENCE\_CYBERSECURITY\_SAFETY:** políticas, IDS, certificación de seguridad → D; E3 aloja el **HSM/secure boot** como hardware.
* **E2-ENERGY\_AND\_RENEWABLE:** conversión de potencia a nivel de sistema, EMS → E2; en E3 quedan **regulaciones locales/PoL** y drives.
* **C2-CRYOGENICS:** sensores/líneas criogénicas primarias → C2; en E3 integramos las **tarjetas electrónicas** y acondicionamiento.


**Ruta canónica**
`OPTIME-FRAMEWORK/T-TECHNOLOGICAL/AMEDEO-PELLICCIA/INTEGRATED/AMPEL360-H2-BWB-QNNN/L1-LOGISTICS_INTEGRATED_BLOCKCHAIN/`

```text
L1-LOGISTICS_INTEGRATED_BLOCKCHAIN/
├── CA-L1-001-ENGINEERING-BOMS/
│   ├── CI-CA-L1-001-001-EBOM-INGEST
│   ├── CI-CA-L1-001-002-MBOM-DERIVATION
│   ├── CI-CA-L1-001-003-DBOM-PROCESS-ROUTINGS
│   ├── CI-CA-L1-001-004-EFFECTIVITY-VARIANTS
│   ├── CI-CA-L1-001-005-CHANGE-NOTICES-SYNC
│   └── README.md
│
├── CA-L1-002-CONFIGURATION-BASELINES/
│   ├── CI-CA-L1-002-001-BASELINE-MANAGEMENT
│   ├── CI-CA-L1-002-002-SERIAL-BATCH-CODING
│   ├── CI-CA-L1-002-003-VERSION-LOCKS
│   ├── CI-CA-L1-002-004-CO-BO-ECN-WORKFLOW
│   ├── CI-CA-L1-002-005-LINK-TO-DET-(O)
│   └── README.md
│
├── CA-L1-003-PROCUREMENT-SOURCING/
│   ├── CI-CA-L1-003-001-SUPPLIER-MASTER
│   ├── CI-CA-L1-003-002-RFQ-RFP-TENDERS
│   ├── CI-CA-L1-003-003-FRAME-CONTRACTS
│   ├── CI-CA-L1-003-004-INCOTERMS-TRADE-COMPLIANCE
│   ├── CI-CA-L1-003-005-ERP-API-EDI-(L2,O)
│   └── README.md
│
├── CA-L1-004-SUPPLIER-ONBOARDING-QUALITY/
│   ├── CI-CA-L1-004-001-QUAL-AUDITS-AS9100D
│   ├── CI-CA-L1-004-002-PPAP-FAI-PROOF
│   ├── CI-CA-L1-004-003-NCR-CAPA-8D
│   ├── CI-CA-L1-004-004-APPROVED-VENDOR-LIST
│   ├── CI-CA-L1-004-005-LEDGER-ATTESTATION-(D,O)
│   └── README.md
│
├── CA-L1-005-MANUFACTURING-EXECUTION-IFC/
│   ├── CI-CA-L1-005-001-WO-RTE-MES-BRIDGE
│   ├── CI-CA-L1-005-002-OPC-UA-SCADA-(L2)
│   ├── CI-CA-L1-005-003-WIP-TRACK-ANDON
│   ├── CI-CA-L1-005-004-KANBAN-KITTING
│   ├── CI-CA-L1-005-005-MES-DET-STAMPS-(O)
│   └── README.md
│
├── CA-L1-006-WAREHOUSE-INVENTORY/
│   ├── CI-CA-L1-006-001-LOCATION-SCHEMAS
│   ├── CI-CA-L1-006-002-LOT-SERIAL-TRACK
│   ├── CI-CA-L1-006-003-QUARANTINE-QA
│   ├── CI-CA-L1-006-004-CYCLE-COUNT
│   ├── CI-CA-L1-006-005-KIT-BUILD-BOM
│   └── README.md
│
├── CA-L1-007-TRACEABILITY-SERIALIZATION/
│   ├── CI-CA-L1-007-001-GS1-DATAMATRIX-ISO15459
│   ├── CI-CA-L1-007-002-RFID-EPC-UID
│   ├── CI-CA-L1-007-003-GENEALOGY-BIRTH-TRAVEL
│   ├── CI-CA-L1-007-004-LLP-ROTABLE-PARTS
│   ├── CI-CA-L1-007-005-LEDGER-EVIDENCE-LINK
│   └── README.md
│
├── CA-L1-008-TRANSPORT-LOGISTICS/
│   ├── CI-CA-L1-008-001-SHIPMENT-PLAN-AWB
│   ├── CI-CA-L1-008-002-HAZMAT-ADR-IATA
│   ├── CI-CA-L1-008-003-COLD-CHAIN-SENSORS-(E3)
│   ├── CI-CA-L1-008-004-CARRIER-PORTAL-EDI-(L2)
│   ├── CI-CA-L1-008-005-POD-DET-ANCHORS-(O)
│   └── README.md
│
├── CA-L1-009-BLOCKCHAIN-LEDGER-QAUDIT/
│   ├── CI-CA-L1-009-001-LEDGER-CHANNELS
│   ├── CI-CA-L1-009-002-EVIDENCE-SCHEMAS
│   ├── CI-CA-L1-009-003-WORM-ANCHORING
│   ├── CI-CA-L1-009-004-NODE-ROLES-KEYS-(D)
│   ├── CI-CA-L1-009-005-RETENTION-POLICY-(O)
│   └── README.md
│
├── CA-L1-010-SMART-CONTRACTS-PAYMENTS/
│   ├── CI-CA-L1-010-001-MILESTONE-PAYMENTS
│   ├── CI-CA-L1-010-002-WARRANTY-ESCROW
│   ├── CI-CA-L1-010-003-PENALTY-LIQUIDATION
│   ├── CI-CA-L1-010-004-SERVICE-LEVELS
│   ├── CI-CA-L1-010-005-AUDIT-TRAIL-DET-(O)
│   └── README.md
│
├── CA-L1-011-SBOM-MBOM-DBOM-LEDGER/
│   ├── CI-CA-L1-011-001-SBOM-INGEST-CYBER-(D)
│   ├── CI-CA-L1-011-002-MBOM-NC-TOOLING
│   ├── CI-CA-L1-011-003-DBOM-PROCESS-REV
│   ├── CI-CA-L1-011-004-VULN-NOTICES-LINK-(D)
│   ├── CI-CA-L1-011-005-PROVENANCE-ROLLUP
│   └── README.md
│
├── CA-L1-012-COMPLIANCE-STANDARDS/
│   ├── CI-CA-L1-012-001-AS9100D-MAPPING
│   ├── CI-CA-L1-012-002-ATA-SPEC2000-CH9-ID
│   ├── CI-CA-L1-012-003-iSPEC-2200-S1000D
│   ├── CI-CA-L1-012-004-ISO8000-22745-DATA-QUAL
│   ├── CI-CA-L1-012-005-ISO28000-SC-SECURITY-(D)
│   └── README.md
│
├── CA-L1-013-MRO-SPARES-SERVICE/
│   ├── CI-CA-L1-013-001-SPARES-CATALOG
│   ├── CI-CA-L1-013-002-ROTABLE-EXCHANGE
│   ├── CI-CA-L1-013-003-LLP-LIFE-CONSUMPTION
│   ├── CI-CA-L1-013-004-MAINT-WORKPACK-LINK-(O)
│   ├── CI-CA-L1-013-005-CORE-RETURN-LEDGER
│   └── README.md
│
├── CA-L1-014-EOL-REVERSE-LOGISTICS/
│   ├── CI-CA-L1-014-001-TEARDOWN-KIT
│   ├── CI-CA-L1-014-002-MATERIAL-RECOVERY
│   ├── CI-CA-L1-014-003-HAZARDOUS-HANDLING-(E1)
│   ├── CI-CA-L1-014-004-REFURBISH-PATHS
│   ├── CI-CA-L1-014-005-LEDGER-CHAIN-OF-CUSTODY
│   └── README.md
│
├── CA-L1-015-DATA-EXCHANGE-EDI-API/
│   ├── CI-CA-L1-015-001-EDIFACT-X12-MAPS-(L2)
│   ├── CI-CA-L1-015-002-AS2-SFTP-TLS-PROFILES-(D)
│   ├── CI-CA-L1-015-003-REST-GraphQL-GATEWAY-(O)
│   ├── CI-CA-L1-015-004-SCHEMA-REGISTRY
│   ├── CI-CA-L1-015-005-RATE-LIMITING-QOS-(O)
│   └── README.md
│
├── CA-L1-016-RISK-RESILIENCE/
│   ├── CI-CA-L1-016-001-SUPPLIER-RISK-SCORES
│   ├── CI-CA-L1-016-002-DUAL-SOURCE-POLICY
│   ├── CI-CA-L1-016-003-BUFFER-STRATEGY
│   ├── CI-CA-L1-016-004-GEO-INCIDENT-TRACK
│   ├── CI-CA-L1-016-005-BCP-RUNBOOKS
│   └── README.md
│
├── CA-L1-017-PLANNING-SOP-MRP/
│   ├── CI-CA-L1-017-001-DEMAND-FORECAST
│   ├── CI-CA-L1-017-002-MRP-NET-REQUIREMENTS
│   ├── CI-CA-L1-017-003-CAPACITY-PLAN
│   ├── CI-CA-L1-017-004-ATP-CTP-RULES
│   ├── CI-CA-L1-017-005-S&OP-CYCLE-DET-(O)
│   └── README.md
│
├── CA-L1-018-COSTING-CARBON-LEDGER/
│   ├── CI-CA-L1-018-001-COST-ROLLUP
│   ├── CI-CA-L1-018-002-CARBON-FOOTPRINT-LCA-(E2)
│   ├── CI-CA-L1-018-003-ENERGY-AS-POLICY-LINK-(O,E2)
│   ├── CI-CA-L1-018-004-SUPPLIER-DECLARATIONS
│   ├── CI-CA-L1-018-005-REPORTING-DASHBOARDS-(O)
│   └── README.md
│
├── CA-L1-019-IDENTITY-ACCESS-ROLES/
│   ├── CI-CA-L1-019-001-RBAC-SoD-(D,O)
│   ├── CI-CA-L1-019-002-SUPPLIER-PORTAL-IAM-(D)
│   ├── CI-CA-L1-019-003-KEY-ROTATION-LEDGER-(D)
│   ├── CI-CA-L1-019-004-AUDIT-TRAILS
│   ├── CI-CA-L1-019-005-ACCESS-REVIEW
│   └── README.md
│
├── CA-L1-020-MASTER-DATA-GOVERNANCE/
│   ├── CI-CA-L1-020-001-PART-MASTER
│   ├── CI-CA-L1-020-002-ATTRIBUTE-TEMPLATES
│   ├── CI-CA-L1-020-003-GOLDEN-RECORD-MATCH
│   ├── CI-CA-L1-020-004-DQ-RULES
│   ├── CI-CA-L1-020-005-CHANGE-APPROVALS
│   └── README.md
│
└── README.md
```

### Límites de dominio (para no solapar)

* **O-OPERATING\_SYSTEMS\_NAVIGATION\_HPC:** orquestación runtime, **DET**, QAL, RBAC operativo → O. L1 consume/expone APIs/evidencias.
* **D-DEFENCE\_CYBERSECURITY\_SAFETY:** cripto, IAM, hardening, IDS → D. L1 referencia (contraseñas/llaves/seguridad).
* **L2-LINKS\_AND\_COMMUNICATIONS:** EDI, AS2, redes físicas y RF → L2. L1 define los **mensajes**, L2 los **transportes**.
* **E2-ENERGY\_AND\_RENEWABLE:** huella/energía y políticas → E2. L1 integra **declaraciones** y KPIs de CO₂.
* **E-EXECUTING:** explotación operacional (as-flown) y cierres de ciclo; L1 enlaza **as-built/as-maintained** con MRO/EOL.

**Ruta canónica**
`OPTIME-FRAMEWORK/T-TECHNOLOGICAL/AMEDEO-PELLICCIA/INTEGRATED/AMPEL360-H2-BWB-QNNN/L2-LINKS_AND_COMMUNICATIONS/`

```text
L2-LINKS_AND_COMMUNICATIONS/
├── CA-L2-001-RF-ANTENNA-SUBSYSTEMS/            # Diseño funcional RF; instalación mecánica → A
│   ├── CI-CA-L2-001-001-ANTENNA-ARRAYS
│   ├── CI-CA-L2-001-002-DUPLEXERS-DIPLEXERS
│   ├── CI-CA-L2-001-003-RF-FEEDS-COUPLERS
│   ├── CI-CA-L2-001-004-CABLE-LOSS-BUDGETS
│   ├── CI-CA-L2-001-005-STATIC-LIGHTNING-PROTECT-(D,E3)
│   └── README.md
│
├── CA-L2-002-VHF-UHF-HF-COMMS/                 # Voz/datos AM/SSB; 8.33 kHz, SELCAL
│   ├── CI-CA-L2-002-001-VHF-AM-VOICE
│   ├── CI-CA-L2-002-002-UHF-AM-OPS
│   ├── CI-CA-L2-002-003-HF-SSB-DATALINK
│   ├── CI-CA-L2-002-004-SELCAL-CODING
│   ├── CI-CA-L2-002-005-EMERG-CHAN-PROFILES
│   └── README.md
│
├── CA-L2-003-SATCOM-INMARSAT-IRIDIUM/
│   ├── CI-CA-L2-003-001-LBAND-TERMINALS
│   ├── CI-CA-L2-003-002-SATCOM-ROUTER-(O)
│   ├── CI-CA-L2-003-003-AIRTIME-QOS-PROFILES
│   ├── CI-CA-L2-003-004-ANTENNA-BEAM-SWITCH
│   ├── CI-CA-L2-003-005-CERT-FRU-INTEROP
│   └── README.md
│
├── CA-L2-004-ATN-ACARS-CPDLC/
│   ├── CI-CA-L2-004-001-ACARS-STACK
│   ├── CI-CA-L2-004-002-ATN-B1-B2-PROFILES
│   ├── CI-CA-L2-004-003-CPDLC-SESSION-MGMT
│   ├── CI-CA-L2-004-004-MESSAGE-MAPPING-(L1,O)
│   ├── CI-CA-L2-004-005-AOC-ROUTING-POLICY-(O)
│   └── README.md
│
├── CA-L2-005-ADS-B-SSR-MODE-S/
│   ├── CI-CA-L2-005-001-TRANSPONDER-MODE-S
│   ├── CI-CA-L2-005-002-ADS-B-1090ES-OUT
│   ├── CI-CA-L2-005-003-ADS-B-IN-FUSION-(O)
│   ├── CI-CA-L2-005-004-SQUITTER-RATES
│   ├── CI-CA-L2-005-005-GROUND-INTEROP
│   └── README.md
│
├── CA-L2-006-ACASX-TCAS-SURVEILLANCE/
│   ├── CI-CA-L2-006-001-ACASX-LOGIC-IFC-(O,D)
│   ├── CI-CA-L2-006-002-TCAS-RX-TX-PROFILES
│   ├── CI-CA-L2-006-003-RA-ADVISORY-ROUTES-(O)
│   ├── CI-CA-L2-006-004-SIL-SDA-MONITORING
│   ├── CI-CA-L2-006-005-FLT-TEST-PATTERNS
│   └── README.md
│
├── CA-L2-007-GNSS-GPS-GALILEO-GLONASS-BDS/
│   ├── CI-CA-L2-007-001-RCVR-L1-L5-E1-E5
│   ├── CI-CA-L2-007-002-SBAS-GBAS-PROFILES
│   ├── CI-CA-L2-007-003-RAIM-AIM-FDE-(O)
│   ├── CI-CA-L2-007-004-TIME-TRANSFER-(O,E3)
│   ├── CI-CA-L2-007-005-NAV-DB-LINK-(O)
│   └── README.md
│
├── CA-L2-008-VOR-ILS-LOC-GS-DME-ADF/
│   ├── CI-CA-L2-008-001-VOR-ILS-RX-STACK
│   ├── CI-CA-L2-008-002-LOC-GS-DEMOD
│   ├── CI-CA-L2-008-003-DME-INTERROGATION
│   ├── CI-CA-L2-008-004-ADF-NDB-PROCESSING
│   ├── CI-CA-L2-008-005-NAV-MODE-SELECT-(O)
│   └── README.md
│
├── CA-L2-009-RADIO-ALTIMETER-PROC/
│   ├── CI-CA-L2-009-001-RA-SIGNAL-CHAIN-(E3)
│   ├── CI-CA-L2-009-002-AGL-COMPUTE-(O)
│   ├── CI-CA-L2-009-003-RFI-MITIGATION
│   ├── CI-CA-L2-009-004-SELF-TEST-BITE
│   ├── CI-CA-L2-009-005-APPROACH-MODES-(O)
│   └── README.md
│
├── CA-L2-010-AFDX-ARINC429-717-BUS/
│   ├── CI-CA-L2-010-001-ARINC429-SCHEDULING
│   ├── CI-CA-L2-010-002-ARINC717-DFDAU-LINK
│   ├── CI-CA-L2-010-003-AFDX-VL-QOS
│   ├── CI-CA-L2-010-004-BRIDGE-GATEWAYS-(O,E3)
│   ├── CI-CA-L2-010-005-BUS-HEALTH
│   └── README.md
│
├── CA-L2-011-TSN-ETHERNET-BACKBONE/
│   ├── CI-CA-L2-011-001-QBV-SCHEDULES
│   ├── CI-CA-L2-011-002-QCI-POLICING
│   ├── CI-CA-L2-011-003-REDUNDANT-PATHS
│   ├── CI-CA-L2-011-004-FRER-RECOVERY
│   ├── CI-CA-L2-011-005-LATENCY-BUDGETS-(O)
│   └── README.md
│
├── CA-L2-012-PTP-TSP-SYNC-DISTRIBUTION/
│   ├── CI-CA-L2-012-001-PTP-PROFILES-AVIATION
│   ├── CI-CA-L2-012-002-GM-BC-OC-ROLES
│   ├── CI-CA-L2-012-003-HOLDOVER-POLICY-(E3)
│   ├── CI-CA-L2-012-004-DRIFT-MONITOR-(O)
│   ├── CI-CA-L2-012-005-TEST-HARNESS
│   └── README.md
│
├── CA-L2-013-5G-NTN-GATE-LINKS/
│   ├── CI-CA-L2-013-001-eSIM-PROFILES
│   ├── CI-CA-L2-013-002-APN-QOS-MAPS
│   ├── CI-CA-L2-013-003-NTN-SAT-CELL-HO
│   ├── CI-CA-L2-013-004-GATE-WIFI-ETH-(O)
│   ├── CI-CA-L2-013-005-OPS-POLICY-(D,O)
│   └── README.md
│
├── CA-L2-014-FSO-LASER-A2A-A2G/
│   ├── CI-CA-L2-014-001-OPTICAL-MODEMS
│   ├── CI-CA-L2-014-002-POINTING-ACQ-TRACK
│   ├── CI-CA-L2-014-003-ATMOSPHERIC-COMP
│   ├── CI-CA-L2-014-004-FALLBACK-SWITCH-(O)
│   ├── CI-CA-L2-014-005-SAFETY-INTERLOCKS-(D)
│   └── README.md
│
├── CA-L2-015-MESH-FORMATION-LINKS/
│   ├── CI-CA-L2-015-001-MESH-ROUTING
│   ├── CI-CA-L2-015-002-RELAYS-REPEATERS
│   ├── CI-CA-L2-015-003-TOPOLOGY-HEALTH
│   ├── CI-CA-L2-015-004-SYNC-DISCI-(O,012)
│   ├── CI-CA-L2-015-005-PRIORIZATION-RULES
│   └── README.md
│
├── CA-L2-016-GSE-GATE-MAINT-PORTS/
│   ├── CI-CA-L2-016-001-ETH-USB-SERIAL-PORTS-(E3)
│   ├── CI-CA-L2-016-002-ACCESS-CONTROL-(D)
│   ├── CI-CA-L2-016-003-DATA-DIODE-OPTIONS
│   ├── CI-CA-L2-016-004-TEST-BRIDGES-(O)
│   ├── CI-CA-L2-016-005-AIRPORT-NET-INTEROP
│   └── README.md
│
├── CA-L2-017-DATA-ROUTER-GATEWAY/
│   ├── CI-CA-L2-017-001-PATH-SELECTION-(O)
│   ├── CI-CA-L2-017-002-NAT-FW-FILTERS-(D)
│   ├── CI-CA-L2-017-003-DPI-PROFILES-(D)
│   ├── CI-CA-L2-017-004-LOG-TELEMETRY-(O)
│   ├── CI-CA-L2-017-005-REDUNDANCY-TAKEOVER
│   └── README.md
│
├── CA-L2-018-EDI-TRANSPORT-BRIDGES/
│   ├── CI-CA-L2-018-001-AS2-SMIME-TLS-(D)
│   ├── CI-CA-L2-018-002-SFTP-OFTP2
│   ├── CI-CA-L2-018-003-QUEUE-GATEWAY-(O)
│   ├── CI-CA-L2-018-004-THROTTLE-RETRY
│   ├── CI-CA-L2-018-005-MONITOR-ALERTS
│   └── README.md
│
├── CA-L2-019-QOS-MONITORING-METRICS/
│   ├── CI-CA-L2-019-001-LATENCY-JITTER-LOSS
│   ├── CI-CA-L2-019-002-SLA-ALERT-RULES
│   ├── CI-CA-L2-019-003-PASSIVE-ACTIVE-PROBES
│   ├── CI-CA-L2-019-004-FLOW-RECORDS
│   ├── CI-CA-L2-019-005-DET-EXPORT-(O)
│   └── README.md
│
├── CA-L2-020-INTEROP-CERT-PROFILES/
│   ├── CI-CA-L2-020-001-RTCA-EUROCAE-MOPS
│   ├── CI-CA-L2-020-002-ARINC-ITP-DO-160-LINKS
│   ├── CI-CA-L2-020-003-SPECTRUM-LICENSING
│   ├── CI-CA-L2-020-004-GROUND-ANSP-INTEROP
│   ├── CI-CA-L2-020-005-FLT-TEST-CARDS
│   └── README.md
│
└── README.md
```

### Límites entre dominios (para no solapar)

* **E3-ELECTRONICS\_DIGITAL\_INSTRUMENTS**: PHY/placas/IO/clock HW; L2 define **stacks, perfiles y redes**.
* **O-OPERATING\_SYSTEMS\_NAVIGATION\_HPC**: scheduling QoS, DET, seguridad de ejecución, PTP runtime; L2 expone **perfiles y políticas**.
* **D-DEFENCE\_CYBERSECURITY\_SAFETY**: cripto, firewalling, IDS, certificación seguridad; L2 referencia y enruta.
* **L1-LOGISTICS\_INTEGRATED\_BLOCKCHAIN**: EDI semántico, SBOM/MBOM; L2 transporta (AS2/SFTP).
* **A-ARCHITECTURES**: instalación/ubicación de antenas, rutas de cableado; L2 aporta **requisitos RF**.



**Ruta canónica**
`OPTIME-FRAMEWORK/T-TECHNOLOGICAL/AMEDEO-PELLICCIA/INTEGRATED/AMPEL360-H2-BWB-QNNN/I-INFRASTRUCTURES_AND_FACILITIES_VALUE_CHAINS/`

```text
I-INFRASTRUCTURES_AND_FACILITIES_VALUE_CHAINS/
├── CA-I-001-SITE-MASTER-PLANNING-ZONING/
│   ├── CI-CA-I-001-001-SITE-BOUNDARIES-TOPO
│   ├── CI-CA-I-001-002-EXCLUSION-ZONES-LH2
│   ├── CI-CA-I-001-003-BLAST-NOISE-FLIGHT-PATH
│   ├── CI-CA-I-001-004-ACCESS-ROADS-APRON-INTERFACE
│   ├── CI-CA-I-001-005-DRAINAGE-SPILL-CONTAINMENT
│   └── README.md
│
├── CA-I-002-UTILITIES-MICROGRID/
│   ├── CI-CA-I-002-001-SUBSTATION-TIE-IN
│   ├── CI-CA-I-002-002-BESS-GENSET-UPS
│   ├── CI-CA-I-002-003-PCC-LOAD-SHED-PROFILES
│   ├── CI-CA-I-002-004-PTP-TSP-TIME-DIST-(L2,O)
│   ├── CI-CA-I-002-005-EMC-GROUNDING-BONDING
│   └── README.md
│
├── CA-I-003-HYDROGEN-PRODUCTION/
│   ├── CI-CA-I-003-001-ELECTROLYZER-STACKS
│   ├── CI-CA-I-003-002-WATER-TREATMENT
│   ├── CI-CA-I-003-003-DRYING-PURIFICATION
│   ├── CI-CA-I-003-004-COMPRESSION-GH2
│   ├── CI-CA-I-003-005-QA-SAMPLING-ISO14687
│   └── README.md
│
├── CA-I-004-HYDROGEN-STORAGE-DISTRIBUTION/
│   ├── CI-CA-I-004-001-LH2-TANK-FARM-API620
│   ├── CI-CA-I-004-002-BOILOFF-RECONDENSATION
│   ├── CI-CA-I-004-003-GH2-RINGS-MANIFOLDS
│   ├── CI-CA-I-004-004-VALVE-PITS-REMOTE-SHUT
│   ├── CI-CA-I-004-005-HAZOP-LOPA-(E1,D)
│   └── README.md
│
├── CA-I-005-CRYOGENIC-TRANSFER-SYSTEMS/
│   ├── CI-CA-I-005-001-VACUUM-JACKETED-LINES
│   ├── CI-CA-I-005-002-CRYO-PUMPS-HEAT-EXCH
│   ├── CI-CA-I-005-003-EXPANSION-JOINTS-SUPPORTS
│   ├── CI-CA-I-005-004-INSULATION-ALBEDO-LOSSES
│   ├── CI-CA-I-005-005-LEAK-TEST-HELIUM-MASSSPEC
│   └── README.md
│
├── CA-I-006-REFUELING-HYDRANT-TRUCKS/
│   ├── CI-CA-I-006-001-HYDRANT-ISLANDS
│   ├── CI-CA-I-006-002-COUPLERS-QD-SAE-J2601
│   ├── CI-CA-I-006-003-FLOW-CONTROL-METERING
│   ├── CI-CA-I-006-004-EMERGENCY-DUMP-VENT
│   ├── CI-CA-I-006-005-INTERLOCKS-FOD-SENSORS-(E3,D)
│   └── README.md
│
├── CA-I-007-SAFETY-FIRE-ATEX/
│   ├── CI-CA-I-007-001-GAS-DETECTION-NDIR-TCD
│   ├── CI-CA-I-007-002-VENTILATION-RATES
│   ├── CI-CA-I-007-003-ATEX-ZONING-IEC60079
│   ├── CI-CA-I-007-004-FIRE-SUPPRESSION-NFPA
│   ├── CI-CA-I-007-005-ERT-MUSTER-PLANS
│   └── README.md
│
├── CA-I-008-ENVIRONMENTAL-REMEDIATION/
│   ├── CI-CA-I-008-001-VOC-LH2-MONITORING
│   ├── CI-CA-I-008-002-WASTEWATER-NEUTRAL
│   ├── CI-CA-I-008-003-SPILL-KITS-LINERS
│   ├── CI-CA-I-008-004-LCA-REPORTS-(E2)
│   ├── CI-CA-I-008-005-BIODIVERSITY-OFFSETS
│   └── README.md
│
├── CA-I-009-MRO-HANGARS-DOCKS/
│   ├── CI-CA-I-009-001-HANGAR-BAY-LAYOUTS
│   ├── CI-CA-I-009-002-CRANES-JACKING-POINTS
│   ├── CI-CA-I-009-003-TAIL-DOORS-SAFETY-LOCKS
│   ├── CI-CA-I-009-004-LOCAL-EXHAUST-FANS
│   ├── CI-CA-I-009-005-TOOL-CRIBS-ESD
│   └── README.md
│
├── CA-I-010-ENGINE-RUNUP-TEST-FACILITIES/
│   ├── CI-CA-I-010-001-RUNUP-PADS-BLASTFENCES
│   ├── CI-CA-I-010-002-NOISE-CONTOURS-MAPS
│   ├── CI-CA-I-010-003-FUEL-INERTING-PROVS
│   ├── CI-CA-I-010-004-INSTRUMENTATION-DAQ-(E3)
│   ├── CI-CA-I-010-005-DET-PACKS-(O)
│   └── README.md
│
├── CA-I-011-GSE-FLEET-CHARGING/
│   ├── CI-CA-I-011-001-GPU-ASU-STARTER-PADS
│   ├── CI-CA-I-011-002-EV-CHARGERS-DC-FAST
│   ├── CI-CA-I-011-003-H2-GSE-DEPOT
│   ├── CI-CA-I-011-004-FLEET-MGMT-TELEMATICS-(L2)
│   ├── CI-CA-I-011-005-MAINT-BAYS-GSE
│   └── README.md
│
├── CA-I-012-APRON-TAXI-MARKINGS/
│   ├── CI-CA-I-012-001-APRON-LIGHTING
│   ├── CI-CA-I-012-002-FOD-MONITORING
│   ├── CI-CA-I-012-003-MARSHALLING-LINES
│   ├── CI-CA-I-012-004-NAVAID-CLEARANCES
│   ├── CI-CA-I-012-005-DEICING-ZONES
│   └── README.md
│
├── CA-I-013-AIRPORT-IT-INTERFACES/
│   ├── CI-CA-I-013-001-AODB-MESSAGES-(L2)
│   ├── CI-CA-I-013-002-CUPPS-CUTE-INTEGRATIONS
│   ├── CI-CA-I-013-003-RFID-BAGGAGE-TIE
│   ├── CI-CA-I-013-004-GATE-RESOURCE-MGMT
│   ├── CI-CA-I-013-005-SECURITY-API-(D)
│   └── README.md
│
├── CA-I-014-WAREHOUSE-KITTING-HUBS/
│   ├── CI-CA-I-014-001-DOCKS-STAGING
│   ├── CI-CA-I-014-002-AUTOSTORE-ROBOTICS
│   ├── CI-CA-I-014-003-ULD-RACKS-TUG-ROUTES
│   ├── CI-CA-I-014-004-HAZMAT-ROOMS
│   ├── CI-CA-I-014-005-WMS-EDI-(L1,L2)
│   └── README.md
│
├── CA-I-015-MANUFACTURING-LINES-TOOLS/
│   ├── CI-CA-I-015-001-FINAL-ASSY-LINES
│   ├── CI-CA-I-015-002-COMPOSITE-AUTOCLAVES
│   ├── CI-CA-I-015-003-NC-CELLS-ROBOT-ROS-(O)
│   ├── CI-CA-I-015-004-NDT-ROOMS
│   ├── CI-CA-I-015-005-EHS-INTERLOCKS
│   └── README.md
│
├── CA-I-016-QUALITY-LABS-METROLOGY/
│   ├── CI-CA-I-016-001-CMM-BAYS
│   ├── CI-CA-I-016-002-CLIMATE-CHAMBERS
│   ├── CI-CA-I-016-003-MATERIALS-LAB
│   ├── CI-CA-I-016-004-CALIBRATION-SCHEDULES
│   ├── CI-CA-I-016-005-DATA-LINK-DET-(O)
│   └── README.md
│
├── CA-I-017-DATACENTER-EDGE-HPC/
│   ├── CI-CA-I-017-001-EDGE-RACKS-COOLING
│   ├── CI-CA-I-017-002-FIBER-PLANT-(L2)
│   ├── CI-CA-I-017-003-PTP-GM-REDUNDANCY-(L2,O)
│   ├── CI-CA-I-017-004-ZTA-SEGMENTATION-(D)
│   ├── CI-CA-I-017-005-QAL-OFFBOARD-NODES-(O)
│   └── README.md
│
├── CA-I-018-5G-WIFI-CAMPUS/
│   ├── CI-CA-I-018-001-SMALLCELLS-AP-PLANS
│   ├── CI-CA-I-018-002-SPECTRUM-COORD
│   ├── CI-CA-I-018-003-ROAMING-POLICIES-(D)
│   ├── CI-CA-I-018-004-QOS-SSIDs-(O)
│   ├── CI-CA-I-018-005-SITE-SURVEYS
│   └── README.md
│
├── CA-I-019-SECURITY-PERIMETER-ACCESS/
│   ├── CI-CA-I-019-001-CCTV-VMS
│   ├── CI-CA-I-019-002-LPR-GATES
│   ├── CI-CA-I-019-003-TURNSTILES-BADGING
│   ├── CI-CA-I-019-004-PANIC-LOCKS
│   ├── CI-CA-I-019-005-ALARM-PSIM
│   └── README.md
│
├── CA-I-020-EMERGENCY-RESPONSE/
│   ├── CI-CA-I-020-001-FIRE-DEPOT-LAYOUT
│   ├── CI-CA-I-020-002-HAZMAT-TRAILERS
│   ├── CI-CA-I-020-003-DRILLS-TABLETOP
│   ├── CI-CA-I-020-004-AIRPORT-COORD-PROTS
│   ├── CI-CA-I-020-005-POST-INCIDENT-DET-(O)
│   └── README.md
│
├── CA-I-021-SUSTAINABILITY-WATER/
│   ├── CI-CA-I-021-001-RAINWATER-HARVEST
│   ├── CI-CA-I-021-002-GREYWATER-REUSE
│   ├── CI-CA-I-021-003-HVAC-RECOVERY
│   ├── CI-CA-I-021-004-PV-CANOPIES-(E2)
│   ├── CI-CA-I-021-005-LCA-KPIS-(E2,O)
│   └── README.md
│
├── CA-I-022-VALUE-CHAIN-MODEL/
│   ├── CI-CA-I-022-001-NODE-REGISTRY
│   ├── CI-CA-I-022-002-PROCESS-FLOWS
│   ├── CI-CA-I-022-003-KPI-THROUGHPUT
│   ├── CI-CA-I-022-004-BOTTLENECK-ANALYSIS
│   ├── CI-CA-I-022-005-DET-CHAIN-OF-CUSTODY-(O,L1)
│   └── README.md
│
├── CA-I-023-REGULATORY-PERMITS/
│   ├── CI-CA-I-023-001-BUILDING-PERMITS
│   ├── CI-CA-I-023-002-HAZARDOUS-SUBSTANCES
│   ├── CI-CA-I-023-003-EMISSIONS-NOISE
│   ├── CI-CA-I-023-004-AVIATION-AUTH-INTEROP
│   ├── CI-CA-I-023-005-RECORDS-RETENTION-(O)
│   └── README.md
│
├── CA-I-024-COMMISSIONING-O&M/
│   ├── CI-CA-I-024-001-COMMISSION-PLANS
│   ├── CI-CA-I-024-002-STARTUP-PROCS
│   ├── CI-CA-I-024-003-PM-SCHEDULES
│   ├── CI-CA-I-024-004-SPARES-ROTATION-(L1)
│   ├── CI-CA-I-024-005-OEE-DASHBOARDS-(O)
│   └── README.md
│
└── README.md
```

### Límites y enlaces cruzados (para no pisarnos)

* **E2-ENERGY\_AND\_RENEWABLE:** microgrid, PV/BESS, políticas de energía/CO₂.
* **O-OPERATING\_SYSTEMS\_NAVIGATION\_HPC:** runtime, DET, QAL, orquestación; I expone **gemelos de instalaciones** y consume **políticas**.
* **L2-LINKS\_AND\_COMMUNICATIONS:** planta de fibra/5G/PTP, AODB/ACARS pasarelas.
* **E1-ENVIRONMENTAL\_REMEDIATION\_CIRCULARITY:** gestión ambiental y EHS.
* **D-DEFENCE\_CYBERSECURITY\_SAFETY:** ZTA, IAM, hardening, PSIM/alarma.
* **L1-LOGISTICS\_INTEGRATED\_BLOCKCHAIN:** WMS/EDI, cadena de custodia y SBOM/MBOM.
* **A2-AIRPORTS\_ADAPTATIONS:** compatibilidad aeropuertos y procedimientos.


**Ruta canónica**
`OPTIME-FRAMEWORK/T-TECHNOLOGICAL/AMEDEO-PELLICCIA/INTEGRATED/AMPEL360-H2-BWB-QNNN/C1-COCKPIT_CABIN_CARGO_SYSTEMS/`

```text
C1-COCKPIT_CABIN_CARGO_SYSTEMS/
├── CA-C1-001-COCKPIT-HMI-ERGONOMICS/
│   ├── CI-CA-C1-001-001-SEATS-PILOT-COPILOT
│   ├── CI-CA-C1-001-002-CONTROLS-THROTTLE-SIDESTICK/YOKE
│   ├── CI-CA-C1-001-003-PEDALS-RUDDER-BRAKE
│   ├── CI-CA-C1-001-004-PANELS-MAIN-OVERHEAD-PEDESTAL
│   ├── CI-CA-C1-001-005-STORAGE-COCKPIT
│   ├── CI-CA-C1-001-006-EMERGENCY-EQUIPMENT-COCKPIT
│   ├── CI-CA-C1-001-007-HARNESS-OXYGEN-QUICK-DON
│   └── README.md
│
├── CA-C1-002-COCKPIT-INTEGRATION-RACKS-COOLING/
│   ├── CI-CA-C1-002-001-AVIONICS-RACKS-MOUNTS  (↔ E3,O)
│   ├── CI-CA-C1-002-002-COOLING-DUCTS-FANS     (↔ E1)
│   ├── CI-CA-C1-002-003-WIRING-HARNESS-PANELS  (↔ E3)
│   ├── CI-CA-C1-002-004-EFB-MOUNTS-POWER-DATA  (↔ O,L2)
│   ├── CI-CA-C1-002-005-LIGHTING-COCKPIT       (↔ E3)
│   └── README.md
│
├── CA-C1-003-CABIN-INTERIORS/
│   ├── CI-CA-C1-003-001-PASSENGER-SEATS
│   ├── CI-CA-C1-003-002-GALLEYS
│   ├── CI-CA-C1-003-003-LAVATORIES
│   ├── CI-CA-C1-003-004-STORAGE-BINS-OHSC
│   ├── CI-CA-C1-003-005-CREW-REST
│   ├── CI-CA-C1-003-006-MONUMENTS-PARTITIONS
│   ├── CI-CA-C1-003-007-CABIN-LIGHTING         (↔ E3)
│   ├── CI-CA-C1-003-008-IFE/IFC-SEAT-NETWORK   (↔ E3,L2)
│   └── README.md
│
├── CA-C1-004-CABIN-SAFETY-EMERGENCY/
│   ├── CI-CA-C1-004-001-PSU-PANELS-O2-MASKS
│   ├── CI-CA-C1-004-002-EMERGENCY-LIGHTING     (↔ E3, A-EMERGENCY-EGRESS)
│   ├── CI-CA-C1-004-003-LIFE-VESTS-RAFTS-STOWAGE (↔ A-EMERGENCY-EGRESS)
│   ├── CI-CA-C1-004-004-FIRST-AID-MEDICAL-KITS
│   ├── CI-CA-C1-004-005-SAFETY-CARDS-SIGNAGE
│   └── README.md
│
├── CA-C1-005-CABIN-ENVIRONMENT-TRIM/
│   ├── CI-CA-C1-005-001-AIR-OUTLETS-DIFFUSERS  (↔ E1)
│   ├── CI-CA-C1-005-002-THERMAL-BLANKETS-NOISE (↔ E1)
│   ├── CI-CA-C1-005-003-FLOORING-CARPETS
│   ├── CI-CA-C1-005-004-WINDOW-SHADES-INNERS
│   ├── CI-CA-C1-005-005-AROMAS-SPEAKERS-ZONES  (↔ E3)
│   └── README.md
│
├── CA-C1-006-CARGO-BAYS-COMPARTMENTS/
│   ├── CI-CA-C1-006-001-CARGO-COMPARTMENTS-LINERS
│   ├── CI-CA-C1-006-002-FLOOR-GRID-ROLLER-TRAYS
│   ├── CI-CA-C1-006-003-INSULATION-FIRE-ZONES  (↔ E1,D)
│   ├── CI-CA-C1-006-004-TEMP-CONTROL-VENTING   (↔ E1)
│   ├── CI-CA-C1-006-005-INSPECTION-ACCESS
│   └── README.md
│
├── CA-C1-007-CARGO-LOADING-RESTRAINT/
│   ├── CI-CA-C1-007-001-LOADING-SYSTEMS-CLS
│   ├── CI-CA-C1-007-002-ULD-INTERFACES-LOCKS
│   ├── CI-CA-C1-007-003-RESTRAINT-SYSTEMS
│   ├── CI-CA-C1-007-004-FIRE-SUPPRESSION-CARGO (↔ E1,D)
│   ├── CI-CA-C1-007-005-HMI-SENSORS-CARGO      (↔ E3,O)
│   └── README.md
│
├── CA-C1-008-POWER-DATA-DISTRIBUTION-CABIN/
│   ├── CI-CA-C1-008-001-SEAT-POWER-USB-110VAC  (↔ E3)
│   ├── CI-CA-C1-008-002-SEAT-BOXES-SWITCHES    (↔ E3)
│   ├── CI-CA-C1-008-003-ETHERNET/TSN-SEGMENTS  (↔ L2)
│   ├── CI-CA-C1-008-004-ROUTERS-GW-SECURITY    (↔ D)
│   ├── CI-CA-C1-008-005-DET-EVIDENCE-LINKS     (↔ O)
│   └── README.md
│
├── CA-C1-009-ACCESSIBILITY-PRM/
│   ├── CI-CA-C1-009-001-PRM-LAVATORY-KITS
│   ├── CI-CA-C1-009-002-AISLE-CHAIR-STOWAGE
│   ├── CI-CA-C1-009-003-ASSIST-HANDRAILS
│   ├── CI-CA-C1-009-004-BRAILLE-SIGNAGE
│   ├── CI-CA-C1-009-005-TCS-TEMP-COMFORT-ZONES (↔ E1)
│   └── README.md
│
├── CA-C1-010-CABIN-HMI-OPS/
│   ├── CI-CA-C1-010-001-CCS-CABIN-CONTROL-PANELS (↔ O,E3)
│   ├── CI-CA-C1-010-002-PA-INTERPHONE-SYSTEMS    (↔ L2,E3)
│   ├── CI-CA-C1-010-003-ANNUNCIATORS-STATUS      (↔ E3)
│   ├── CI-CA-C1-010-004-CREW-TABLETS-EFB-CABIN   (↔ O,L2)
│   ├── CI-CA-C1-010-005-DET-OPS-LOGS             (↔ O)
│   └── README.md
│
├── CA-C1-011-DOORS-HATCHES-INTERIOR-TRIM/
│   ├── CI-CA-C1-011-001-INTERIOR-TRIM-DOORS      (↔ A for structure)
│   ├── CI-CA-C1-011-002-SEALS-TRIMS-FINISHES     (↔ A)
│   ├── CI-CA-C1-011-003-ASSIST-HANDLES
│   ├── CI-CA-C1-011-004-SAFETY-COVERS
│   ├── CI-CA-C1-011-005-INSPECTION-VIEWS
│   └── README.md
│
├── CA-C1-012-CABIN-CLEANLINESS-WASTE/
│   ├── CI-CA-C1-012-001-WASTE-BINS-LINERS
│   ├── CI-CA-C1-012-002-CLEANING-PANELS
│   ├── CI-CA-C1-012-003-UVC/SANIT-FEATURES      (↔ E1)
│   ├── CI-CA-C1-012-004-ODOUR-CONTROL
│   ├── CI-CA-C1-012-005-DET-WASTE-TRACKING      (↔ O,L1)
│   └── README.md
│
└── README.md
```

### Notas de límite y trazas (para no pisar otros dominios)

* **E3-ELECTRONICS\_DIGITAL\_INSTRUMENTS:** todo lo que sea electrónica/ILs/buses/sensórica física.
* **O-OPERATING\_SYSTEMS\_NAVIGATION\_HPC:** runtime, CCS/EFB apps, DET, orquestación; C1 consume servicios.
* **E1-ENVIRONMENTAL…:** HVAC, presurización, agua/residuos; C1 integra salidas (difusores/aislamientos).
* **D-DEFENCE\_CYBERSECURITY\_SAFETY:** ZTA, PA/annunciators seguros, segmentación.
* **A-ARCHITECTURES…:** puertas/estructura, egress estructural; C1 cubre el “interior trim & equipment”.
* **L1/L2:** logística (stowage/chain-of-custody) y redes (PA, IFE/IFC, Ethernet/TSN, PTP/TSP).


**Ruta canónica**
`OPTIME-FRAMEWORK/T-TECHNOLOGICAL/AMEDEO-PELLICCIA/INTEGRATED/AMPEL360-H2-BWB-QNNN/C2-CRYOGENICS_QUANTUM_INTERFACES_HYDROGEN_CELLS/`

```text
C2-CRYOGENICS_QUANTUM_INTERFACES_HYDROGEN_CELLS/
├── CA-C2-001-CRYO-INTERFACE-MANIFOLDS/
│   ├── CI-CA-C2-001-001-VACUUM-JACKETED-MANIFOLDS   (↔ E2)
│   ├── CI-CA-C2-001-002-ISOLATION-VALVES-COLD-SEATS (↔ D)
│   ├── CI-CA-C2-001-003-COOL-DOWN-PURGE-CIRCUITS    (↔ O)
│   ├── CI-CA-C2-001-004-RELIEF-BURST-DISKS          (↔ D,E1)
│   ├── CI-CA-C2-001-005-CRYO-QUICK-DISCONNECTS      (↔ E2)
│   └── README.md
│
├── CA-C2-002-CRYO-DISTRIBUTION-LINES/
│   ├── CI-CA-C2-002-001-VJ-LINES-SPEC-SUPPORTS      (↔ A)
│   ├── CI-CA-C2-002-002-FLEX-HOSES-ROTARY-JOINTS
│   ├── CI-CA-C2-002-003-HEAT-LEAK-BUDGET-MLI        (↔ E1)
│   ├── CI-CA-C2-002-004-PIPE-STRESS-ANALYSIS
│   ├── CI-CA-C2-002-005-INSPECTION-PORTS-NDT
│   └── README.md
│
├── CA-C2-003-LH2-THERMAL-MANAGEMENT-ONBOARD/
│   ├── CI-CA-C2-003-001-BOILOFF-HANDLING-EJECTORS   (↔ E2)
│   ├── CI-CA-C2-003-002-VAPORIZERS-HEATERS          (↔ P,O)
│   ├── CI-CA-C2-003-003-RECONDENSER-INTERFACES      (↔ I,E2)
│   ├── CI-CA-C2-003-004-COLD-SOAK-STRATEGIES        (↔ A)
│   ├── CI-CA-C2-003-005-DET-THERMAL-LOGGING         (↔ O)
│   └── README.md
│
├── CA-C2-004-CRYO-SENSORS-INSTRUMENTATION/
│   ├── CI-CA-C2-004-001-TC-PT100-LOX-T-SENSORS      (↔ E3)
│   ├── CI-CA-C2-004-002-LEVEL-GAUGES-CAP-ULTRASONIC (↔ E3)
│   ├── CI-CA-C2-004-003-LEAK-DETECT-MASS-SPEC       (↔ D)
│   ├── CI-CA-C2-004-004-PRESSURE-TRANSDUCERS-CRYO   (↔ E3)
│   ├── CI-CA-C2-004-005-CALIBRATION-PORTS-PROCS     (↔ O)
│   └── README.md
│
├── CA-C2-005-QUANTUM-MICROCRYOSTATS-(R&D)/
│   ├── CI-CA-C2-005-001-1-4K-MICROCRYO-MODULES      (↔ O,E3)
│   ├── CI-CA-C2-005-002-VIBRATION-ISOLATION-MOUNTS  (↔ A)
│   ├── CI-CA-C2-005-003-THERMAL-ANCHORS-STAGES
│   ├── CI-CA-C2-005-004-COOLDOWN-SEQUENCER-APPS     (↔ O)
│   ├── CI-CA-C2-005-005-FLIGHT-BOUNDARY-NOTES       (DAL-N/A)
│   └── README.md
│
├── CA-C2-006-QUANTUM-RF-CHAIN-CRYO/
│   ├── CI-CA-C2-006-001-HEMT-LNAs-CRYO              (↔ E3)
│   ├── CI-CA-C2-006-002-ATTENUATORS-FILTERS-ISOLATORS
│   ├── CI-CA-C2-006-003-CRYO-COAX-FEEDTHROUGHS      (↔ A,E3)
│   ├── CI-CA-C2-006-004-RF-EMC-SHIELDING-LOW-TEMP   (↔ D)
│   ├── CI-CA-C2-006-005-DET-RF-CHARACTERIZATION     (↔ O)
│   └── README.md
│
├── CA-C2-007-QUANTUM-TIMING-CLOCK-DISTRIBUTION/
│   ├── CI-CA-C2-007-001-TSP/PTP-GRANDMASTER-LOCK    (↔ L2,O)
│   ├── CI-CA-C2-007-002-DISTRIBUTION-TREES-FANOUT   (↔ E3)
│   ├── CI-CA-C2-007-003-PHASE-NOISE-BUDGET          (↔ E3)
│   ├── CI-CA-C2-007-004-HOLDOVER-OCXO-PROFILE       (↔ O)
│   ├── CI-CA-C2-007-005-REDUNDANCY-2oo3-MONITOR     (↔ O,D)
│   └── README.md
│
├── CA-C2-008-FUEL-CELL-STACKS/
│   ├── CI-CA-C2-008-001-PEM-STACK-MODULES
│   ├── CI-CA-C2-008-002-STACK-MONITORING-BMS        (↔ E3)
│   ├── CI-CA-C2-008-003-ISOLATION-CONTACTORS        (↔ D)
│   ├── CI-CA-C2-008-004-STACK-ENCLOSURE-COOLING     (↔ E1)
│   ├── CI-CA-C2-008-005-DET-STACK-PERF              (↔ O)
│   └── README.md
│
├── CA-C2-009-FUEL-CELL-BALANCE-OF-PLANT/
│   ├── CI-CA-C2-009-001-AIR-COMPRESSOR-HUMIDIFIER   (↔ P,E1)
│   ├── CI-CA-C2-009-002-H2-REGULATOR-PURGE-MANIFOLD (↔ E2)
│   ├── CI-CA-C2-009-003-WATER-MGMT-SEPARATOR        (↔ E1)
│   ├── CI-CA-C2-009-004-COOLING-LOOP-PLATE-HX       (↔ E1)
│   ├── CI-CA-C2-009-005-STARTUP-SHUTDOWN-LOGIC      (↔ O)
│   └── README.md
│
├── CA-C2-010-H2-CONDITIONING-AND-VAPORIZERS/
│   ├── CI-CA-C2-010-001-LH2-TO-GH2-VAPORIZERS       (↔ E2,P)
│   ├── CI-CA-C2-010-002-HEATED-LINES-ANTIFREEZE     (↔ E1)
│   ├── CI-CA-C2-010-003-PRESSURE-TRACKING-CONTROL   (↔ O)
│   ├── CI-CA-C2-010-004-MIXERS-ORIFICES             (↔ P)
│   ├── CI-CA-C2-010-005-DET-TRACEABILITY            (↔ O)
│   └── README.md
│
├── CA-C2-011-CRYO-SAFETY-INTERLOCKS/
│   ├── CI-CA-C2-011-001-ATEX-ZONING-IEC60079        (↔ D,E1)
│   ├── CI-CA-C2-011-002-O2-DEFICIENCY-MONITORING    (↔ E1)
│   ├── CI-CA-C2-011-003-ESD-BONDING-LPS             (↔ A,D)
│   ├── CI-CA-C2-011-004-EMERGENCY-VENT-STACKS       (↔ A)
│   ├── CI-CA-C2-011-005-SAFE-STOP-PERMS-(FUEL/CRYO) (↔ O,D)
│   └── README.md
│
├── CA-C2-012-CRYO-INSULATION-COMPOSITES/
│   ├── CI-CA-C2-012-001-MLI-BLANKETS-AEROGELS
│   ├── CI-CA-C2-012-002-COLD-SUPPORT-STRUTS         (↔ A)
│   ├── CI-CA-C2-012-003-THERMAL-INTERCEPTS
│   ├── CI-CA-C2-012-004-ALBEDO-COATINGS
│   ├── CI-CA-C2-012-005-AGING-AND-REPAIR-KITS
│   └── README.md
│
├── CA-C2-013-CRYO-FEEDTHROUGHS-HERMETICS/
│   ├── CI-CA-C2-013-001-ELECTRICAL-PASSTHROUGHS     (↔ E3)
│   ├── CI-CA-C2-013-002-RF-COAX-BULKHEADS           (↔ E3)
│   ├── CI-CA-C2-013-003-FIBER-OPTIC-FEEDTHROUGH     (↔ L2)
│   ├── CI-CA-C2-013-004-SEALING-GLASS-METAL
│   ├── CI-CA-C2-013-005-HELIUM-LEAK-SPECS
│   └── README.md
│
├── CA-C2-014-PRECOOL-COOLDOWN-VENT-PROCS/
│   ├── CI-CA-C2-014-001-PRECOOL-SEQUENCES           (↔ O)
│   ├── CI-CA-C2-014-002-COOLDOWN-RAMPS              (↔ O)
│   ├── CI-CA-C2-014-003-VENT-PROFILES
│   ├── CI-CA-C2-014-004-ENERGY-BUDGETS-(EaP)        (↔ O,E2)
│   ├── CI-CA-C2-014-005-DET-PROCEDURE-EVIDENCE      (↔ O)
│   └── README.md
│
├── CA-C2-015-EMI-EMC-LOW-TEMP/
│   ├── CI-CA-C2-015-001-SHIELDING-ENCLOSURES        (↔ D,E3)
│   ├── CI-CA-C2-015-002-FILTERED-FEEDTHROUGHS       (↔ E3)
│   ├── CI-CA-C2-015-003-GROUNDING-STAR-TOPOLOGY     (↔ E3)
│   ├── CI-CA-C2-015-004-NOISE-MAPS-CRYO             (↔ O)
│   ├── CI-CA-C2-015-005-VERIFICATION-PLANS
│   └── README.md
│
├── CA-C2-016-CRYO-DIAGNOSTICS-MAINT/
│   ├── CI-CA-C2-016-001-LEAK-LOCATE-PROTOCOLS
│   ├── CI-CA-C2-016-002-VALVE-STROKE-TESTS
│   ├── CI-CA-C2-016-003-SENSOR-CAL-INTERVALS        (↔ O)
│   ├── CI-CA-C2-016-004-BORESCOPE-PORTS
│   ├── CI-CA-C2-016-005-MRO-KITS-SPARES-(L1)
│   └── README.md
│
├── CA-C2-017-VENTING-STACKS-ROUTES/
│   ├── CI-CA-C2-017-001-VENT-STACK-PLACEMENT        (↔ A)
│   ├── CI-CA-C2-017-002-DISPERSION-ANALYSIS         (↔ E1)
│   ├── CI-CA-C2-017-003-NO-INGEST-NO-IGNITION       (↔ D)
│   ├── CI-CA-C2-017-004-ICE-ACCUMULATION-CONTROL
│   ├── CI-CA-C2-017-005-INSPECTION-ACCESS
│   └── README.md
│
├── CA-C2-018-INTERFACES-PROPULSION-FUELS/
│   ├── CI-CA-C2-018-001-ENGINE-FEED-LINES           (↔ P)
│   ├── CI-CA-C2-018-002-RECIRC-RETURN-LOOPS         (↔ P,E2)
│   ├── CI-CA-C2-018-003-STARTUP-PURGE-ENGINE        (↔ P,O)
│   ├── CI-CA-C2-018-004-ISOLATION-LOCKOUTS          (↔ D)
│   ├── CI-CA-C2-018-005-DET-FEED-TRACE              (↔ O)
│   └── README.md
│
└── README.md
```

### Límites funcionales (para no duplicar con otros dominios)

* **E2-ENERGY\_AND\_RENEWABLE**: tanqueado principal LH₂/GH₂ y microred—C2 gestiona **interfaces criogénicas y celdas/fuel cells a bordo**.
* **O-OPERATING\_SYSTEMS\_NAVIGATION\_HPC**: secuenciadores, DET, QAL; C2 **expone** sensores/actuadores y **consume** políticas (Energy-as-Policy).
* **E3-ELECTRONICS\_DIGITAL\_INSTRUMENTS**: hardware electrónico, buses, DAQ; C2 define condiciones criogénicas y feedthroughs.
* **D-DEFENCE\_CYBERSECURITY\_SAFETY**: ATEX, ZTA, interlocks; C2 enlaza requisitos y dispositivos.
* **L2-LINKS\_AND\_COMMUNICATIONS**: TSP/PTP/GNSS y fibra para **timing** cuántico (C2-007).
* **E1-ENVIRONMENTAL\_REMEDIATION\_CIRCULARITY**: ventilación, O₂, vertidos y LCA.


**Ruta canónica**
`OPTIME-FRAMEWORK/T-TECHNOLOGICAL/AMEDEO-PELLICCIA/INTEGRATED/AMPEL360-H2-BWB-QNNN/I2-INTELLIGENT_SYSTEMS_ONBOARD_AI/`

```text
I2-INTELLIGENT_SYSTEMS_ONBOARD_AI/
├── CA-I2-001-AUTONOMY-LAYERING-ARCH/
│   ├── CI-CA-I2-001-001-AUTONOMY-LEVELS-STATE-MACHINE
│   ├── CI-CA-I2-001-002-ROLE-ARBITRATION-(CREW/AUTOMATION)
│   ├── CI-CA-I2-001-003-HAZARD-MODEL-MAPPING-(ARP4761)
│   ├── CI-CA-I2-001-004-POLICY-HIERARCHY-(AMORES/SEAL)     (↔ O,D)
│   ├── CI-CA-I2-001-005-FAIL-OP/FAIL-SAFE-DEGRADATION      (↔ E)
│   └── README.md
│
├── CA-I2-002-PERCEPTION-FUSION-(NON-DAL)/
│   ├── CI-CA-I2-002-001-SENSOR-INGEST-(E3/L2)
│   ├── CI-CA-I2-002-002-MULTI-SENSOR-FUSION-(EKF/UKF/Graph)
│   ├── CI-CA-I2-002-003-OBJECT-TRACKS-SEMANTICS
│   ├── CI-CA-I2-002-004-ENV-MAPS-(WEATHER/TERRAIN/NOTAM)   (↔ L2)
│   ├── CI-CA-I2-002-005-QUALITY-MONITORS-DRIFT
│   └── README.md
│
├── CA-I2-003-PREDICTIVE-MAINTENANCE-(MRO)/
│   ├── CI-CA-I2-003-001-RUL-ESTIMATION-(ENG/STRUCT/AVN)    (↔ L1,P,E3)
│   ├── CI-CA-I2-003-002-ANOMALY-SCORES-(VIB/TEMP/POWER)
│   ├── CI-CA-I2-003-003-WORKPACK-AUTOGEN-(DET-EVIDENCE)    (↔ O,L1)
│   ├── CI-CA-I2-003-004-SPARES-OPTIMIZER                    (↔ L1)
│   ├── CI-CA-I2-003-005-COST/RISK-CVAR-SELECTOR             (↔ O)
│   └── README.md
│
├── CA-I2-004-COCKPIT-ADVISORY-(HMI)/
│   ├── CI-CA-I2-004-001-CHECKLIST-ASSIST
│   ├── CI-CA-I2-004-002-ABNORMAL-PROCEDURE-REASONER
│   ├── CI-CA-I2-004-003-EXP-RECAP-(WHY/WHAT-IF/CONFIDENCE) (↔ O,DET)
│   ├── CI-CA-I2-004-004-VOICE-CO-PILOT-(OFFLINE)           (↔ C1,L2)
│   ├── CI-CA-I2-004-005-CREW-WORKLOAD-METER
│   └── README.md
│
├── CA-I2-005-TRAJECTORY-ENERGY-OPTIMIZATION/
│   ├── CI-CA-I2-005-001-COST-INDEX/CO₂-POLICY-(EaP)        (↔ O,E2)
│   ├── CI-CA-I2-005-002-4D-TRAJ-SUGGESTER-(NON-RT)         (↔ L2,ATM)
│   ├── CI-CA-I2-005-003-ALTN/ETOPS-ADVISOR                 (↔ A2)
│   ├── CI-CA-I2-005-004-EXPLAINABILITY-CONSTRAINTS
│   ├── CI-CA-I2-005-005-DET-PLAN-VS-FLEW
│   └── README.md
│
├── CA-I2-006-FLEET/AOC-OPTIMIZATION-(ONBOARD-EDGE)/
│   ├── CI-CA-I2-006-001-TURNAROUND-FORECAST
│   ├── CI-CA-I2-006-002-CREW/TAIL-PAIRING-ASSISTS          (↔ L1)
│   ├── CI-CA-I2-006-003-IRREGULAR-OPS-DECIDER              (↔ L2)
│   ├── CI-CA-I2-006-004-SLOT/CTOT-SENSITIVITY
│   ├── CI-CA-I2-006-005-SYNC-TO-AOC-(DELAY-TOLERANT)       (↔ L2)
│   └── README.md
│
├── CA-I2-007-ANOMALY-DETECTION-SAFETY/
│   ├── CI-CA-I2-007-001-STREAMING-ANOMS-(VOTE/THRESHOLD)   (↔ D,O)
│   ├── CI-CA-I2-007-002-OUTLIER-EXPLAINER
│   ├── CI-CA-I2-007-003-ALERT-ROUTING-(CCS/EICAS/EFB)      (↔ C1,O)
│   ├── CI-CA-I2-007-004-POST-FLIGHT-ROOT-CAUSE             (↔ DET)
│   ├── CI-CA-I2-007-005-BENCHMARK-SCENARIOS
│   └── README.md
│
├── CA-I2-008-EXPLAINABILITY-AND-DET/
│   ├── CI-CA-I2-008-001-RATIONALE-TEMPLATES-(GSn-Claims)   (↔ O)
│   ├── CI-CA-I2-008-002-INPUT-REFERENCES-LOG
│   ├── CI-CA-I2-008-003-MODEL-CARD/HAZARD-CARD
│   ├── CI-CA-I2-008-004-AUDIT-PACK-WORM-(DET)
│   ├── CI-CA-I2-008-005-HUMAN-READABLE-SUMMARY
│   └── README.md
│
├── CA-I2-009-MLOPS/CERT-PACKAGING/
│   ├── CI-CA-I2-009-001-MODEL-SBOM-SIGNING                (↔ O,D)
│   ├── CI-CA-I2-009-002-VERSIONING/IMMUTABILITY
│   ├── CI-CA-I2-009-003-DRIFT-MONITOR-NO-ONLINE-LEARNING
│   ├── CI-CA-I2-009-004-DATA-LINEAGE-UTCS-MI
│   ├── CI-CA-I2-009-005-TQL/TOOL-QUAL-GATES               (↔ DO-330)
│   └── README.md
│
├── CA-I2-010-EDGE-ACCELERATION-(DSP/NPU/GPU)/
│   ├── CI-CA-I2-010-001-STATIC-INFERENCE-BUDGETS          (↔ O,E3)
│   ├── CI-CA-I2-010-002-QUANT/PRUNING-POLICY
│   ├── CI-CA-I2-010-003-WCET/THERMAL-LIMITS               (↔ E1)
│   ├── CI-CA-I2-010-004-MEMORY-SAFETY/ISOLATION           (↔ D)
│   ├── CI-CA-I2-010-005-BENCH-SUITE-(COCKPIT/CABIN/CARGO) (↔ C1)
│   └── README.md
│
├── CA-I2-011-CABIN-AI-(PERSONALIZATION/IFE)/
│   ├── CI-CA-I2-011-001-RECSYS-ONBOARD-(PRIVACY)          (↔ D)
│   ├── CI-CA-I2-011-002-ZONE-COMFORT-OPT                   (↔ E1)
│   ├── CI-CA-I2-011-003-DYNAMIC-LIGHTING-SCENES            (↔ E3)
│   ├── CI-CA-I2-011-004-PA-MULTILINGUAL-TTS                (↔ L2)
│   ├── CI-CA-I2-011-005-A11Y-ASSISTS-(PRM)                 (↔ C1)
│   └── README.md
│
├── CA-I2-012-CARGO-AI-(CLS/HAZARD)/
│   ├── CI-CA-I2-012-001-COG/LOADING-SIM-ASSIST             (↔ A,C1)
│   ├── CI-CA-I2-012-002-ULD-ANOMALY-DETECT
│   ├── CI-CA-I2-012-003-FIRE-RISK-ESTIMATOR                (↔ D,E1)
│   ├── CI-CA-I2-012-004-CLS-SEQUENCE-SUGGESTER             (↔ L1)
│   ├── CI-CA-I2-012-005-DET-CARGO-TRACE
│   └── README.md
│
├── CA-I2-013-ENERGY/CO₂-ADVISORS-(EaP)/
│   ├── CI-CA-I2-013-001-EAP-POLICY-BINDINGS                (↔ O,E2)
│   ├── CI-CA-I2-013-002-REALTIME-FOQA/CO₂-EST
│   ├── CI-CA-I2-013-003-PROFILE-SHAPE-SUGGESTIONS
│   ├── CI-CA-I2-013-004-COST/RISK-TRADE-CVAR
│   ├── CI-CA-I2-013-005-DET-ENERGY-EVIDENCE
│   └── README.md
│
├── CA-I2-014-SECURITY-AI-(ZTA)/
│   ├── CI-CA-I2-014-001-NIDS/NIPS-ML                       (↔ D,L2)
│   ├── CI-CA-I2-014-002-ANOMALOUS-IDENTITY/BEHAVIOR
│   ├── CI-CA-I2-014-003-CONTENT-SAFETY-(EFB/IFE)
│   ├── CI-CA-I2-014-004-THREAT-INTEL-ONBOARD-COMPAT
│   ├── CI-CA-I2-014-005-DET-SECURITY-LOGS                  (↔ O)
│   └── README.md
│
├── CA-I2-015-SIM/DATASETS-SCENARIOS/
│   ├── CI-CA-I2-015-001-SCENARIO-GEN-(WEATHER/ATM/FAIL)
│   ├── CI-CA-I2-015-002-DATASET-STANDARDS-(UTCS/Protobuf)  (↔ O)
│   ├── CI-CA-I2-015-003-BIAS/A11Y-CHECKS
│   ├── CI-CA-I2-015-004-SIM2REAL-GUARDRAILS
│   ├── CI-CA-I2-015-005-REPLAY/DEBRIEF-TOOLS               (↔ DET)
│   └── README.md
│
├── CA-I2-016-AGENT-MESH-(ExMCP)/
│   ├── CI-CA-I2-016-001-SKILLS/TOOLS-REGISTRY              (↔ O)
│   ├── CI-CA-I2-016-002-MEMORY-RAG-LIMITS-(PRIVACY)        (↔ D)
│   ├── CI-CA-I2-016-003-COORDINATION/NEGOTIATION
│   ├── CI-CA-I2-016-004-HRI-PROMPTS-(COCKPIT/CABIN)        (↔ C1)
│   ├── CI-CA-I2-016-005-DET-RATIONALES                     (↔ O)
│   └── README.md
│
├── CA-I2-017-SPEECH/INTENT-COCKPIT/
│   ├── CI-CA-I2-017-001-ASR-OFFLINE-NO-CLOUD               (↔ D)
│   ├── CI-CA-I2-017-002-INTENT-GRAMMARS-(ABN/EMER)
│   ├── CI-CA-I2-017-003-BARGE-IN/LATENCY-BUDGET            (↔ O)
│   ├── CI-CA-I2-017-004-ROBUST-NOISE/ACCENTS
│   ├── CI-CA-I2-017-005-CREW-OVERRIDE-ALWAYS
│   └── README.md
│
├── CA-I2-018-VISION-INSPECTION-(MRO/RAMP)/
│   ├── CI-CA-I2-018-001-FOD/LEAK-DETECT
│   ├── CI-CA-I2-018-002-BORESCOPE-AI-ASSIST
│   ├── CI-CA-I2-018-003-DAMAGE-CLASSIFY-(BIRD/ICE/IMPACT)
│   ├── CI-CA-I2-018-004-REPORTING-TO-CERT/DET              (↔ O)
│   ├── CI-CA-I2-018-005-BOUNDARY-CONDITIONS-(LIGHT/WX)
│   └── README.md
│
├── CA-I2-019-RECOVERY-ADVISOR-(ABNORMAL)/
│   ├── CI-CA-I2-019-001-ECAM/EICAS-MERGE-ASSIST            (↔ C1)
│   ├── CI-CA-I2-019-002-NEXT-BEST-ACTION-(NBA)
│   ├── CI-CA-I2-019-003-CHECKLIST-ADAPTATION
│   ├── CI-CA-I2-019-004-TERRAIN/WEATHER-THREATS            (↔ L2)
│   ├── CI-CA-I2-019-005-EXP-LIMITS-ALWAYS-VISIBLE
│   └── README.md
│
├── CA-I2-020-ETHICS-&-GOVERNANCE-(AMORES)/
│   ├── CI-CA-I2-020-001-POLICY-COMPILER→RUNTIME            (↔ O)
│   ├── CI-CA-I2-020-002-RISK-GATES-(DAL-C/≤)
│   ├── CI-CA-I2-020-003-HUMAN-IN-THE-LOOP-MANDATES
│   ├── CI-CA-I2-020-004-BLACKLIST-OF-DIRECT-ACTUATIONS
│   ├── CI-CA-I2-020-005-PERIODIC-REVIEW/ATTESTATION        (↔ D,DET)
│   └── README.md
│
└── README.md
```

### Límites y reglas (críticas)

* **Nada de control directo.** I2 **nunca actúa** sobre actuadores; sólo emite **propuestas/avisos**. Toda acción pasa por **P-PROCEDURAL** (gates) y **E-EXECUTING** (runtime modes) con **aprobación humana** donde aplique.
* **DAL-A clásico**: flight-laws/FBW y funciones críticas siguen en **M-MACHINE/E3/O** particionadas (ARINC-653). I2 es **advisory** o **DAL-C o menor**.
* **Sin aprendizaje online**: entrenamiento **offboard**; a bordo sólo inferencia **inmutable** (versionada/sellada). **Drift ⇒ flag**, no re-entrena.
* **Proveniencia**: toda recomendación lleva **rationale + inputs** firmados (**DET/WORM**).

**Ruta canónica**
`OPTIME-FRAMEWORK/T-TECHNOLOGICAL/AMEDEO-PELLICCIA/INTEGRATED/AMPEL360-H2-BWB-QNNN/A2-AIRPORTS_ADAPTATIONS/`

```text
A2-AIRPORTS_ADAPTATIONS/
├── CA-A2-001-AIRFIELD-GEOMETRY-COMPAT/
│   ├── CI-CA-A2-001-001-RWY/TWY-WIDTH-FILLET-CHECKS
│   ├── CI-CA-A2-001-002-ACN/PCN-CAPACITY-MATCH
│   ├── CI-CA-A2-001-003-SWEPT-PATH/WINGTIP-CLEARANCE
│   ├── CI-CA-A2-001-004-BWB-CONTOUR-MARKINGS
│   ├── CI-CA-A2-001-005-PAVEMENT-EDGE/SHOULDER-RISKS
│   └── README.md
│
├── CA-A2-002-STAND-&-GATE-INTERFACE/
│   ├── CI-CA-A2-002-001-STAND-GEOMETRY/LEAD-IN-LINES
│   ├── CI-CA-A2-002-002-SERVICE-POINTS-(GPU/PCA/WATER)
│   ├── CI-CA-A2-002-003-STOP-MARK/VDGS-PROFILES
│   ├── CI-CA-A2-002-004-H2-SAFETY-OFFSETS/VENT-CLEAR
│   ├── CI-CA-A2-002-005-JET/PLUME-PROTECTION-ZONES
│   └── README.md
│
├── CA-A2-003-BOARDING-BRIDGES-&-ACCESS/
│   ├── CI-CA-A2-003-001-MULTI-DOOR-BWB-BRIDGES           (↔ C1)
│   ├── CI-CA-A2-003-002-HEIGHT/RANGE/ROLL-ANGLES
│   ├── CI-CA-A2-003-003-PRM/A11Y-ROUTES
│   ├── CI-CA-A2-003-004-EGRESS/CUT-OUT-INTERFACES        (↔ A, C1)
│   ├── CI-CA-A2-003-005-OPERABILITY-IN-WIND/ICE
│   └── README.md
│
├── CA-A2-004-GSE-INTERFACES-(GROUND-SUPPORT)/
│   ├── CI-CA-A2-004-001-LOADER/HI-LOADER-ENVELOPES       (↔ C1)
│   ├── CI-CA-A2-004-002-BELT-LOADER/STAIRS-CLEARANCES
│   ├── CI-CA-A2-004-003-DE-ICER-BOOM-REACH/SAFETY        (↔ E1)
│   ├── CI-CA-A2-004-004-TOWBAR/LLTV/NOSE-GEAR-ADAPT      (↔ M)
│   ├── CI-CA-A2-004-005-GSE-ROUTES/NO-BLAST-CORRIDORS
│   └── README.md
│
├── CA-A2-005-H2-INFRASTRUCTURE-&-FUELING/
│   ├── CI-CA-A2-005-001-LH2-STORAGE/FARM-OPTIONS         (↔ E2)
│   ├── CI-CA-A2-005-002-HYDRANT-VS-BOWSER-TOPOLOGIES     (↔ L1)
│   ├── CI-CA-A2-005-003-COUPLERS/HOSES/FILTERS-STD       (↔ P)
│   ├── CI-CA-A2-005-004-VENT-STACKS/DISPER-ANALYSIS      (↔ E1)
│   ├── CI-CA-A2-005-005-LEAK-DET/E-STOP/GAS-ALARM        (↔ D)
│   ├── CI-CA-A2-005-006-EXCLUSION-ZONES/SETBACKS
│   └── README.md
│
├── CA-A2-006-ELECTRICAL-&-THERMAL-SHORE/
│   ├── CI-CA-A2-006-001-400HZ/270VDC-CAPACITY            (↔ E3,O)
│   ├── CI-CA-A2-006-002-PCAIR-FLOW/TEMP-SPECS            (↔ E1)
│   ├── CI-CA-A2-006-003-HVDC/SMART-CHARGING-ROADMAP      (↔ O,E2)
│   ├── CI-CA-A2-006-004-CONNECTOR-STANDARDS/MATING       (↔ E3)
│   ├── CI-CA-A2-006-005-POWER-QUALITY/HARMONICS
│   └── README.md
│
├── CA-A2-007-RESCUE/FIREFIGHTING-&-SAFETY-ZONES/
│   ├── CI-CA-A2-007-001-RFFS-AGENT/RESPONSE-PROFILES
│   ├── CI-CA-A2-007-002-H2/CRYO-SCENARIO-SETS            (↔ E2,D)
│   ├── CI-CA-A2-007-003-SPILL/CONTAINMENT-PLANS          (↔ E1)
│   ├── CI-CA-A2-007-004-MUSTER-POINTS/EVAC-ROUTES
│   ├── CI-CA-A2-007-005-SAFETY-SIGNAGE/MARKINGS
│   └── README.md
│
├── CA-A2-008-MAINTENANCE-BAYS-&-HANGARS/
│   ├── CI-CA-A2-008-001-HANGAR-DOOR/CLEAR-ENVELOPE
│   ├── CI-CA-A2-008-002-DOCKING/PLATFORMS-SET            (↔ I,L1)
│   ├── CI-CA-A2-008-003-CRANE/LIFT-POINTS                (↔ M)
│   ├── CI-CA-A2-008-004-VENT/DETECT/LH2-HANGAR           (↔ E2)
│   ├── CI-CA-A2-008-005-GLYCOL/WASTE-MANAGEMENT          (↔ E1)
│   └── README.md
│
├── CA-A2-009-NAVAIDS-&-SURFACE-SURVEILLANCE/
│   ├── CI-CA-A2-009-001-ILS/GBAS-COMPAT/EMI              (↔ L2,E3)
│   ├── CI-CA-A2-009-002-A-SMGCS/STOP-BAR-LAYOUT
│   ├── CI-CA-A2-009-003-TAXI-GUIDANCE/MARKINGS
│   ├── CI-CA-A2-009-004-SAFETY-NETS-(RWSL/ASDE-X)
│   ├── CI-CA-A2-009-005-DRONE-UTM-INTERACTIONS           (↔ CA-O-005)
│   └── README.md
│
├── CA-A2-010-NOISE/EMISSIONS-FOOTPRINTS/
│   ├── CI-CA-A2-010-001-NOISE-CONTOURS-(SID/STAR)
│   ├── CI-CA-A2-010-002-HOTSPOTS/BLAST-MAPS
│   ├── CI-CA-A2-010-003-CO₂/NOx-PROFILES                  (↔ E2,P)
│   ├── CI-CA-A2-010-004-CURFEW/OPS-RESTRICTIONS
│   ├── CI-CA-A2-010-005-MITIGATION-WORKS/BERMS
│   └── README.md
│
├── CA-A2-011-WINTER-OPS-&-DE-ICING/
│   ├── CI-CA-A2-011-001-DE-ICING-BAYS/LANES               (↔ E1)
│   ├── CI-CA-A2-011-002-GLYCOL-RECOVERY/SUMP
│   ├── CI-CA-A2-011-003-HEATED-STANDS/UTILITIES           (↔ O,E2)
│   ├── CI-CA-A2-011-004-ANTI-ICING-PROFILES
│   ├── CI-CA-A2-011-005-CHEMICAL-COMPAT/H2-RISKS          (↔ E2)
│   └── README.md
│
├── CA-A2-012-SECURITY-&-ACCESS-CONTROL/
│   ├── CI-CA-A2-012-001-STERILE-ZONES/H2-AREAS            (↔ D)
│   ├── CI-CA-A2-012-002-BADGING/ACCESS-MATRIX
│   ├── CI-CA-A2-012-003-CCTV/ANALYTICS-BLIND-SPOTS
│   ├── CI-CA-A2-012-004-CYBER/GATEWAY-HARDENING           (↔ D,L2)
│   ├── CI-CA-A2-012-005-AUTHORIZED-GSE/ROBOTICS-PATHS     (↔ C1)
│   └── README.md
│
├── CA-A2-013-CARGO-FLOW-&-ULD-BAYS/
│   ├── CI-CA-A2-013-001-ULD-ROUTES/BWB-DOORS              (↔ C1)
│   ├── CI-CA-A2-013-002-HIGH-DECK-LOADER-INTERFACE
│   ├── CI-CA-A2-013-003-LEVELING/PITCH-LIMITS
│   ├── CI-CA-A2-013-004-ULD-ID/TRACE-(DET)                (↔ O,L1)
│   ├── CI-CA-A2-013-005-HAZMAT-ZONE/SEPARATION            (↔ D,E1)
│   └── README.md
│
├── CA-A2-014-A-CDM/ATM-COORDINATION/
│   ├── CI-CA-A2-014-001-A-CDM-MILESTONES/MAPS             (↔ L2,O)
│   ├── CI-CA-A2-014-002-TURNAROUND-TARGETS/TTOT/CTOT
│   ├── CI-CA-A2-014-003-DATA-EXCHANGE-(AIDX/ OLD/NEW)     (↔ L2)
│   ├── CI-CA-A2-014-004-DET-LIVE-FEEDS-TO-AOC             (↔ O)
│   ├── CI-CA-A2-014-005-IRREGULAR-OPS-PLAYBOOKS
│   └── README.md
│
├── CA-A2-015-RESILIENCE/CONTINGENCY/
│   ├── CI-CA-A2-015-001-BLACK-START/POWER-FALLBACK        (↔ O,E2)
│   ├── CI-CA-A2-015-002-WATER/VENT/INERTING-FALLBACK      (↔ E2)
│   ├── CI-CA-A2-015-003-ALTERNATE-FUELING/ROUTES
│   ├── CI-CA-A2-015-004-DATA/LINK-DEGRADATION-MODES       (↔ L2,O)
│   ├── CI-CA-A2-015-005-EMERGENCY-SHARED-OPS/JOINT-USE
│   └── README.md
│
└── README.md
```

### Scope & notas (rápido)

* **Airfield & Stand**: compatibilidad geométrica, ACN/PCN, señalización específica BWB y zonas de blast/plume.
* **Acceso & GSE**: fingers multipuerta para BWB, rutas GSE seguras, reach de de-icers y loaders.
* **H₂ & Shore**: granja LH₂, hidrantes/bowsers, offsets de seguridad, shore power/PCA dimensionados.
* **Safety & Winter**: RFFS para escenarios criogénicos, contención de derrames, bahías de de-icing con recuperación.
* **NAVAIDs & A-CDM**: compatibilidad ILS/GBAS, A-SMGCS y milestones A-CDM integrados a **DET/AOC**.
* **MRO & Cargo**: hangares adaptados a BWB y flujos ULD con trazabilidad **DET**.


---

## Rutas canónicas

* `OPTIME-FRAMEWORK/I-INTELLIGENT/`
* `OPTIME-FRAMEWORK/M-MACHINE/`
* `OPTIME-FRAMEWORK/E-EXECUTING/`

---

### I-INTELLIGENT (Autonomía, asesoramiento, decisiones)

> **Límites:** sin actuadores directos; sólo **propuestas**. Aprobación y ejecución siempre pasan por **P-PROCEDURAL** (gates) y **E-EXECUTING** (modos). Sin aprendizaje online; inferencia inmutable y versionada; todo con evidencia **DET**.

```text
I-INTELLIGENT/
├── CA-I-001-AUTONOMY-LAYERING-ARCH/
│   ├── CI-CA-I-001-001-AUTONOMY-LEVELS-STATE-MACHINE
│   ├── CI-CA-I-001-002-CREW/AUTOMATION-ARBITRATION
│   ├── CI-CA-I-001-003-HAZARD-MAP-(ARP4761)               (↔ D)
│   ├── CI-CA-I-001-004-POLICY-HIERARCHY-(AMORES/SEAL)      (↔ O,E)
│   └── CI-CA-I-001-005-DEGRADATION-MODES-(FAIL-OP/SAFE)    (↔ E)
│
├── CA-I-002-AGENT-MESH-(ExMCP)/
│   ├── CI-CA-I-002-001-SKILLS/TOOLS-REGISTRY               (↔ O)
│   ├── CI-CA-I-002-002-MEMORY-RAG-LIMITS-(PRIVACY)         (↔ D)
│   ├── CI-CA-I-002-003-NEGOTIATION/COORDINATION
│   ├── CI-CA-I-002-004-HRI-PROMPTS-(COCKPIT/CABIN/CARGO)   (↔ C1)
│   └── CI-CA-I-002-005-DET-RATIONALES/WORM                 (↔ E)
│
├── CA-I-003-PERCEPTION-FUSION-(NON-DAL)/
│   ├── CI-CA-I-003-001-INGEST-(RADAR/LIDAR/EO/WEATHER)     (↔ E3,L2)
│   ├── CI-CA-I-003-002-FUSION-(EKF/FACTOR-GRAPH)
│   ├── CI-CA-I-003-003-SEMANTIC-TRACKS
│   ├── CI-CA-I-003-004-ENV-MAPS-(NOTAM/TERRAIN)            (↔ L2)
│   └── CI-CA-I-003-005-QUALITY/DRIFT-MONITORS
│
├── CA-I-004-REASONING/PLANNING/
│   ├── CI-CA-I-004-001-GOAL-STACK/CONSTRAINTS
│   ├── CI-CA-I-004-002-SEARCH-(A*/MCTS)-WITH-COST/PENALTIES
│   ├── CI-CA-I-004-003-ROBUST-NBA-(NEXT-BEST-ACTION)
│   ├── CI-CA-I-004-004-SAFETY-ASSUMPTIONS-CHECKER          (↔ D,O)
│   └── CI-CA-I-004-005-ANYTIME-PLANNING
│
├── CA-I-005-COCKPIT-ADVISORY-(HMI)/
│   ├── CI-CA-I-005-001-CHECKLIST-ASSIST
│   ├── CI-CA-I-005-002-ABNORMAL-REASONER
│   ├── CI-CA-I-005-003-VOICE-CO-PILOT-(OFFLINE)            (↔ C1,L2)
│   ├── CI-CA-I-005-004-EXPLAINER-(WHY/WHAT-IF/CONF)
│   └── CI-CA-I-005-005-WORKLOAD-METER
│
├── CA-I-006-PREDICTIVE-MAINTENANCE-(MRO)/
│   ├── CI-CA-I-006-001-RUL-ESTIMATION-(ENG/AVN/STRUCT)     (↔ L1,E3)
│   ├── CI-CA-I-006-002-ANOMALY-SCORES
│   ├── CI-CA-I-006-003-WORKPACK-AUTO-(DET-EVIDENCE)        (↔ O,E)
│   ├── CI-CA-I-006-004-SPARES/INVENTORY-OPT                 (↔ L1)
│   └── CI-CA-I-006-005-CVAR-RISK-SELECTOR                   (↔ O)
│
├── CA-I-007-TRAJECTORY/ENERGY-ADVISORS/
│   ├── CI-CA-I-007-001-EaP-POLICY-BINDINGS                  (↔ O,E2)
│   ├── CI-CA-I-007-002-4D-TRAJ-SUGGESTER-(NON-RT)           (↔ L2)
│   ├── CI-CA-I-007-003-ALTERNATES/ETOPS                     (↔ A2)
│   ├── CI-CA-I-007-004-EXPLAINABILITY-CONSTRAINTS
│   └── CI-CA-I-007-005-DET-PLAN-VS-FLEW
│
├── CA-I-008-FLEET/AOC-OPTIMIZATION/
│   ├── CI-CA-I-008-001-TURNAROUND-FORECAST
│   ├── CI-CA-I-008-002-PAIRING/SCHEDULING-ASSISTS           (↔ L1)
│   ├── CI-CA-I-008-003-IRROPS-DECIDER                       (↔ L2)
│   ├── CI-CA-I-008-004-SLOT/CTOT-SENSITIVITY
│   └── CI-CA-I-008-005-AOC-SYNC-(DTN)                       (↔ L2)
│
├── CA-I-009-ANOMALY-DETECTION-SAFETY/
│   ├── CI-CA-I-009-001-STREAMING-ANOMS-(VOTE/THR)           (↔ D,O)
│   ├── CI-CA-I-009-002-OUTLIER-EXPLAINER
│   ├── CI-CA-I-009-003-ALERT-ROUTING-(ECAM/EICAS/EFB)       (↔ C1,O)
│   ├── CI-CA-I-009-004-POST-FLIGHT-RCA-(DET)
│   └── CI-CA-I-009-005-BENCHMARK-SCENARIOS
│
├── CA-I-010-EXPLAINABILITY-&-DET/
│   ├── CI-CA-I-010-001-GSn-RATIONALE-TEMPLATES              (↔ O)
│   ├── CI-CA-I-010-002-INPUT-REFERENCES-LOG
│   ├── CI-CA-I-010-003-MODEL/MISSION-CARDS
│   ├── CI-CA-I-010-004-WORM-AUDIT-PACKS                     (↔ E)
│   └── CI-CA-I-010-005-HUMAN-READABLE-SUMMARY
│
├── CA-I-011-MLOPS/CERT-PACKAGING/
│   ├── CI-CA-I-011-001-MODEL-SBOM-SIGNING                   (↔ O,D)
│   ├── CI-CA-I-011-002-VERSIONING/IMMUTABILITY
│   ├── CI-CA-I-011-003-DRIFT-MONITOR-(NO-ONLINE-LEARN)
│   ├── CI-CA-I-011-004-DATA-LINEAGE-(UTCS-MI)
│   └── CI-CA-I-011-005-TOOL-QUAL-(DO-330)
│
├── CA-I-012-EDGE-ACCEL-(DSP/NPU/GPU)/
│   ├── CI-CA-I-012-001-INFERENCE-BUDGETS                    (↔ O,E3)
│   ├── CI-CA-I-012-002-QUANT/PRUNING-POLICY
│   ├── CI-CA-I-012-003-WCET/THERMAL-LIMITS                  (↔ E1)
│   ├── CI-CA-I-012-004-MEMORY-SAFETY/ISOLATION              (↔ D)
│   └── CI-CA-I-012-005-BENCHMARK-(COCKPIT/CABIN/CARGO)      (↔ C1)
│
└── README.md
```

---

### M-MACHINE (Automatización clásica, ML estático, simulación)

> **Límites:** sin aprendizaje online; modelos **estáticos** y “hash-lock”. Enlaces deterministas; trazabilidad completa; respeta particiones/RTOS. Es la **fábrica** que ejecuta.

```text
M-MACHINE/
├── CA-M-001-AUTOMATION-JOBS/ETL/
│   ├── CI-CA-M-001-001-BATCH/STREAM-ENGINES
│   ├── CI-CA-M-001-002-CANONICAL-SCHEMAS-(Protobuf)
│   ├── CI-CA-M-001-003-QUALITY-GATES/RETRY
│   ├── CI-CA-M-001-004-LEDGER-WRITE-(QAUDIT/DET)
│   └── CI-CA-M-001-005-ERROR-BUDGETS/SLO
│
├── CA-M-002-ORCHESTRATION-(HTS/NON-SAFETY)/
│   ├── CI-CA-M-002-001-JOB-SCHEDULER-(HPC/K8s)
│   ├── CI-CA-M-002-002-RESOURCES/QoS
│   ├── CI-CA-M-002-003-CHECKPOINT/RESUME
│   ├── CI-CA-M-002-004-REPRODUCIBILITY-(SEED/HASH)
│   └── CI-CA-M-002-005-OBSERVABILITY-(METRICS/TRACES)
│
├── CA-M-003-STATIC-INFERENCE-AT-SCALE/
│   ├── CI-CA-M-003-001-MODEL-ARTIFACTS-STORE
│   ├── CI-CA-M-003-002-RUNTIME-IMMUTABLE
│   ├── CI-CA-M-003-003-AB-TESTING-OFFLINE
│   ├── CI-CA-M-003-004-DRIFT-ALERTS
│   └── CI-CA-M-003-005-GPU/DSP-DISPATCH
│
├── CA-M-004-PHYSICS-SIM-(CFD/FEA/MULTIPHYSICS)/
│   ├── CI-CA-M-004-001-MESH/BC-MANAGER
│   ├── CI-CA-M-004-002-COUPLED-SOLVERS
│   ├── CI-CA-M-004-003-JOB-PACKAGING-(HPC)
│   ├── CI-CA-M-004-004-RESULTS-LINEAGE
│   └── CI-CA-M-004-005-EXP-EVIDENCE-(DET)
│
├── CA-M-005-DIGITAL-TWIN-RUNTIMES/
│   ├── CI-CA-M-005-001-CONTRACTS-(APIs/STATES)
│   ├── CI-CA-M-005-002-SYNCHRONIZATION
│   ├── CI-CA-M-005-003-STATE-RECONCILERS
│   ├── CI-CA-M-005-004-SAFETY-BOUNDARIES
│   └── CI-CA-M-005-005-REPLAY/WHAT-IF
│
├── CA-M-006-ROS2/SCADA-ADAPTERS/
│   ├── CI-CA-M-006-001-OPC-UA-GATEWAYS                      (↔ L2,O)
│   ├── CI-CA-M-006-002-ROS2-BRIDGES
│   ├── CI-CA-M-006-003-SCHEMA-MAPPING
│   ├── CI-CA-M-006-004-RATE-LIMIT/ISOLATION
│   └── CI-CA-M-006-005-DET-ADAPTER-LOGS
│
├── CA-M-007-NC/CNC-TOOLCHAIN/
│   ├── CI-CA-M-007-001-GCODE/STEP-NC
│   ├── CI-CA-M-007-002-POSTS/PP
│   ├── CI-CA-M-007-003-VERIFICATION/PROBES
│   ├── CI-CA-M-007-004-TOOL-OFFSETS/LIFE
│   └── CI-CA-M-007-005-TRACE-TO-PLM                         (↔ T/D)
│
├── CA-M-008-TEST-RIGS/HIL/
│   ├── CI-CA-M-008-001-RIG-CONTROL/DAU
│   ├── CI-CA-M-008-002-SCENARIO-RUNNER
│   ├── CI-CA-M-008-003-SIGNAL-INJECTION/FAULTS
│   ├── CI-CA-M-008-004-LATENCY/THROUGHPUT-PROFILES
│   └── CI-CA-M-008-005-DET-RUN-PACKS                        (↔ E)
│
├── CA-M-009-QUALITY/METROLOGY/
│   ├── CI-CA-M-009-001-CMM/SCAN-PROCESS
│   ├── CI-CA-M-009-002-TOL-STACKUP
│   ├── CI-CA-M-009-003-CAPABILITY-INDEX-(Cp/Cpk)
│   ├── CI-CA-M-009-004-NCR/CONCESSIONS                      (↔ O)
│   └── CI-CA-M-009-005-FEEDBACK-TO-PLM
│
├── CA-M-010-TRACEABILITY/QAUDIT/
│   ├── CI-CA-M-010-001-UTCS-MI-IDS
│   ├── CI-CA-M-010-002-SBOM/MBOM/DBOM
│   ├── CI-CA-M-010-003-SIGNATURES/ATTEST
│   ├── CI-CA-M-010-004-LEDGER-ANCHOR
│   └── CI-CA-M-010-005-COMPLIANCE-QUERIES
│
└── README.md
```

---

### E-EXECUTING (Runtime operativo, telemetría, cierre de bucle)

> **Límites:** guarda y ejecuta **modos**; aplica **gates**; genera **evidencia**. Es el cierre operacional (linea/vuelo/MRO), no decide objetivos: asegura que lo aprobado se hace **de forma segura y trazable**.

```text
E-EXECUTING/
├── CA-E-001-RUNTIME-MODES/
│   ├── CI-CA-E-001-001-MODE-MANAGER-(NORM/INHIBIT/EMERG)
│   ├── CI-CA-E-001-002-AUTHZ/RBAC-BINDINGS                 (↔ O)
│   ├── CI-CA-E-001-003-SAFE-STATE-TRANSITIONS
│   ├── CI-CA-E-001-004-FLEET-POLICY-SYNC
│   └── CI-CA-E-001-005-READINESS-HEALTH-GATES              (↔ D)
│
├── CA-E-002-COMMAND-GATES/
│   ├── CI-CA-E-002-001-PROCEDURE-GATEWAY-(P)               (↔ P)
│   ├── CI-CA-E-002-002-CONTEXT-CHECKS/INHIBITS
│   ├── CI-CA-E-002-003-HUMAN-APPROVAL-FLOWS
│   ├── CI-CA-E-002-004-ROLLBACK/QUARANTINE
│   └── CI-CA-E-002-005-DET-DECISION-TRAIL
│
├── CA-E-003-TELEMETRY-BUS/
│   ├── CI-CA-E-003-001-TOPICS/SCHEMAS
│   ├── CI-CA-E-003-002-RATES/QOS
│   ├── CI-CA-E-003-003-EDGE-BUFFERING
│   ├── CI-CA-E-003-004-REPLAY/RECONSTRUCT
│   └── CI-CA-E-003-005-EXPORT-AOC/ATM                      (↔ L2)
│
├── CA-E-004-DET-EVIDENCE-WORM/
│   ├── CI-CA-E-004-001-SIGN/ANCHOR
│   ├── CI-CA-E-004-002-TRACEPOINTS/KPI
│   ├── CI-CA-E-004-003-WORM/RETENTION
│   ├── CI-CA-E-004-004-EVIDENCE-PACKS-(POST-FLIGHT)
│   └── CI-CA-E-004-005-AUDIT-PORTAL                         (↔ O)
│
├── CA-E-005-EFB/MAINT-APPS/
│   ├── CI-CA-E-005-001-OFFLINE-MODELS-(IMMUTABLE)          (↔ M)
│   ├── CI-CA-E-005-002-WORKPACK-VIEW/EDIT
│   ├── CI-CA-E-005-003-DET-ATTACHMENTS
│   ├── CI-CA-E-005-004-ROLE-BASED-VIEWS
│   └── CI-CA-E-005-005-DELTA-UPDATES
│
├── CA-E-006-MRO-LINE-OPS/
│   ├── CI-CA-E-006-001-JOB-CARDS/AIRWORTHINESS
│   ├── CI-CA-E-006-002-TOOL/LOT-TRACE                      (↔ L1)
│   ├── CI-CA-E-006-003-FINDINGS/NCR→PLM                    (↔ M)
│   ├── CI-CA-E-006-004-CERT-SIGNOFF
│   └── CI-CA-E-006-005-RECYCLE/EoL-ROUTES                  (↔ E1)
│
├── CA-E-007-A-CDM/ATM-EXCHANGE/
│   ├── CI-CA-E-007-001-DATA-LINKS-(AIDX,OLD,NEW)           (↔ L2)
│   ├── CI-CA-E-007-002-TURNAROUND-MILESTONES
│   ├── CI-CA-E-007-003-CTOT/SLOT-COORD
│   ├── CI-CA-E-007-004-IRROPS-PLAYBOOKS
│   └── CI-CA-E-007-005-LIVE-FEEDS-TO-AOC                   (↔ O)
│
├── CA-E-008-EAP-ENFORCER-(ENERGY-as-POLICY)/
│   ├── CI-CA-E-008-001-POLICY-INGEST
│   ├── CI-CA-E-008-002-RUNTIME-BUDGETS
│   ├── CI-CA-E-008-003-THROTTLING/SHAPING
│   ├── CI-CA-E-008-004-DET-ENERGY-PACKS
│   └── CI-CA-E-008-005-CO₂-REPORTS                         (↔ O,E2)
│
├── CA-E-009-INCIDENT/ALERT-HANDLING/
│   ├── CI-CA-E-009-001-SEVERITY/MITIGATION
│   ├── CI-CA-E-009-002-CORRELATION-ENGINE
│   ├── CI-CA-E-009-003-PAGING/ESCALATION
│   ├── CI-CA-E-009-004-POSTMORTEMS-(DET)
│   └── CI-CA-E-009-005-LESSONS-LEARNED→POLICY              (↔ O)
│
├── CA-E-010-TIME-SYNC-(TSP/PTP)/
│   ├── CI-CA-E-010-001-GRANDMASTER/OCXO
│   ├── CI-CA-E-010-002-HOLDOVER/ALARMS
│   ├── CI-CA-E-010-003-DRIFT-STATS
│   ├── CI-CA-E-010-004-NTP/BRIDGING-(NON-CRIT)
│   └── CI-CA-E-010-005-VERIFICATION-PACKS
│
└── README.md
```
Each CI of TECHNOLOGICAL stack has 11 subfolders, representing main lifecycle phases 
```
01-Requirements
02-Design
03-Building-Prototyping
04-Executables-Packages
05-Verification-Validation
06-Integration-Qualification
07-Certification-Security
08-Production-Scale
09-Ops-Services
10-MRO
11-Sustainment-Recycle


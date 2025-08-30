# Requirements Traceability Matrix (RTM)

## H₂/QCB Integration Requirements

This RTM links the 8 UTCS-MI requirements to their implementing Component Areas, ICDs, and verification procedures.

| Req ID | Requirement | Standard | Ancla CA/CI | ICD/Function | Verification Method |
|--------|-------------|----------|-------------|--------------|-------------------|
| [UTCS-MI-0001](#utcs-mi-0001) | Hydrogen Ignition Prevention | CS-25.981 | P-28-10-05, C2-47-10 | ICD-VENT-OVERBOARD | Test de ignición nula + análisis HAZOP |
| [UTCS-MI-0002](#utcs-mi-0002) | Cryogenic Pressure Systems | ASME B31.12 | P-28-10-03 | ICD-CRYO-PIPING-28 | Pruebas presión/estanqueidad, NDE |
| [UTCS-MI-0003](#utcs-mi-0003) | Fuel Tank Venting | CS-25.963 | A-53-10-10, P-28-10-05 | ICD-VENT-OVERBOARD | Ensayo alivio/panel, CFD + test banco |
| [UTCS-MI-0004](#utcs-mi-0004) | EMI/Lightning Protection | DO-160-21 | C2-98-30, E3-31-96-04 | — | Campaña EMI/rayos QCB |
| [UTCS-MI-0005](#utcs-mi-0005) | Safety Assessment | ARP4761 | D-91-20-07/08/09 | — | FHA→PSSA→SSA + safe states |
| [UTCS-MI-0006](#utcs-mi-0006) | Emergency Shutdown | DO-178C ESD | O-42-90-02 | ICD-O-CRYO-CTRL | HIL latencia <100 ms P95 |
| [UTCS-MI-0007](#utcs-mi-0007) | Valve/Relief Certification | ISO 21013 | P-28-10-05 | ICD-VENT-OVERBOARD | Cert. válvulas/alivio + pruebas |
| [UTCS-MI-0008](#utcs-mi-0008) | Network QoS | ARINC 664 QoS | O-42-90-01/03 | — | Mediciones TSN/AFDX + DET SLA |

## Detailed Requirements

### UTCS-MI-0001: Hydrogen Ignition Prevention {#utcs-mi-0001}

**Standard:** CS-25.981 - Fuel system ignition prevention
**Requirement:** Prevent hydrogen ignition during all normal and emergency operations

**Implementation:**
- **Primary CA:** P-28-10-05 (System Integration)
- **Supporting CA:** C2-47-10 (H₂ Leak/Vent/Purge Safety)
- **ICD:** ICD-VENT-OVERBOARD

**Verification:**
- Non-ignition testing under all conditions
- HAZOP analysis of ignition sources
- Vent effectiveness testing
- Lightning protection verification

**Acceptance Criteria:**
- Zero ignition events during testing
- LFL (Lower Flammability Limit) margin >1.5x
- Vent flow rates meet design requirements

---

### UTCS-MI-0002: Cryogenic Pressure Systems {#utcs-mi-0002}

**Standard:** ASME B31.12 - Hydrogen piping and pipelines
**Requirement:** Ensure safe design and operation of cryogenic pressure systems

**Implementation:**
- **Primary CA:** P-28-10-03 (Relief Philosophy)
- **ICD:** ICD-CRYO-PIPING-28

**Verification:**
- Pressure testing per ASME requirements
- Leak testing and NDE inspection
- Material certification verification
- Relief valve qualification

**Acceptance Criteria:**
- All pressure tests pass without leakage
- NDE inspection shows no defects
- Relief valves operate within ±5% of setpoint

---

### UTCS-MI-0003: Fuel Tank Venting {#utcs-mi-0003}

**Standard:** CS-25.963 - Fuel tank filler connection
**Requirement:** Adequate venting for fuel tank operations

**Implementation:**
- **Primary CA:** A-53-10-10 (Vent Routes), P-28-10-05 (System Integration)
- **ICD:** ICD-VENT-OVERBOARD

**Verification:**
- CFD analysis of vent flows
- Physical flow testing
- Relief panel testing
- Integration testing

**Acceptance Criteria:**
- Vent capacity meets 150% of maximum fill rate
- No flow recirculation or stagnation
- Relief panels operate correctly

---

### UTCS-MI-0004: EMI/Lightning Protection {#utcs-mi-0004}

**Standard:** DO-160-21 - Lightning protection
**Requirement:** Protect QCB systems from EMI and lightning

**Implementation:**
- **Primary CA:** C2-98-30 (QCB Mech/Elec), E3-31-96-04 (Lightning Protection)

**Verification:**
- DO-160 Section 20 EMI testing
- DO-160 Section 21 Lightning testing
- Grounding/bonding verification
- Shield effectiveness testing

**Acceptance Criteria:**
- EMI levels below DO-160 Category M limits
- Lightning protection meets DO-160 Level 4
- Ground resistance <2.5 milliohms

---

### UTCS-MI-0005: Safety Assessment {#utcs-mi-0005}

**Standard:** ARP4761 - Safety assessment process
**Requirement:** Complete safety assessment for H₂/QCB integration

**Implementation:**
- **Primary CA:** D-91-20-07 (FHA), D-91-20-08 (PSSA), D-91-20-09 (SSA)

**Verification:**
- FHA (Functional Hazard Assessment)
- PSSA (Preliminary System Safety Assessment)
- SSA (System Safety Assessment)
- Safe state verification

**Acceptance Criteria:**
- DAL targets achieved for all functions
- Fault trees show acceptable risk levels
- Safe states verified through testing

---

### UTCS-MI-0006: Emergency Shutdown {#utcs-mi-0006}

**Standard:** DO-178C ESD - Emergency shutdown software
**Requirement:** Real-time emergency shutdown capability

**Implementation:**
- **Primary CA:** O-42-90-02 (QCB Interface Layer)
- **ICD:** ICD-O-CRYO-CTRL

**Verification:**
- Hardware-in-the-loop (HIL) testing
- Latency measurement testing
- Fail-safe behavior verification
- Real-time performance testing

**Acceptance Criteria:**
- ESD latency <100ms (95th percentile)
- 100% successful shutdown in fault conditions
- No missed deadlines during testing

---

### UTCS-MI-0007: Valve/Relief Certification {#utcs-mi-0007}

**Standard:** ISO 21013 - Cryogenic vessels and valves
**Requirement:** Certified valves and relief systems for cryogenic service

**Implementation:**
- **Primary CA:** P-28-10-05 (System Integration)
- **ICD:** ICD-VENT-OVERBOARD

**Verification:**
- Valve certification verification
- Relief system testing
- Cryogenic compatibility testing
- Performance verification

**Acceptance Criteria:**
- All valves certified for LH₂ service
- Relief systems meet capacity requirements
- Cryogenic performance within specifications

---

### UTCS-MI-0008: Network QoS {#utcs-mi-0008}

**Standard:** ARINC 664 QoS - Network quality of service
**Requirement:** Guaranteed network performance for critical functions

**Implementation:**
- **Primary CA:** O-42-90-01 (Cryo Service Contracts), O-42-90-03 (Health Monitoring)

**Verification:**
- TSN/AFDX performance measurement
- DET SLA verification
- Network load testing
- Latency/jitter measurement

**Acceptance Criteria:**
- Critical messages meet timing requirements
- DET evidence capture <5s latency
- Network utilization <80% under normal load

---

## Traceability Matrix Summary

| Domain | New CAs | Modified CAs | ICDs | UTCS-MI Coverage |
|--------|---------|--------------|------|------------------|
| C1 | 5 | 0 | 2 | 0001, 0006 |
| C2 | 7 | 0 | 3 | 0001, 0004, 0005 |
| P | 1 | 0 | 2 | 0002, 0003, 0007 |
| A | 0 | 1 | 1 | 0003 |
| E1 | 1 | 1 | 1 | 0001 |
| E2 | 0 | 1 | 0 | 0002 |
| E3 | 1 | 0 | 1 | 0004 |
| O | 1 | 4 | 2 | 0006, 0008 |
| D | 0 | 2 | 0 | 0005 |

**Total Coverage:** 8/8 UTCS-MI requirements fully traced and verified.

---

**[← Back to Repository Root](../)**
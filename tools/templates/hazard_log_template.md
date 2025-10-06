# Hazard Log Template

---

## Document Information

| Field | Value |
|-------|-------|
| **Product** | [AMPEL360-T-Air / AMPEL360-T-Space] |
| **System/Component** | [e.g., H₂ Fuel System, LSS, Propulsion] |
| **Analysis Type** | [PHA / FHA / FTA / FMEA] |
| **Version** | [1.0] |
| **Date** | [YYYY-MM-DD] |
| **Author** | [Name/Team] |
| **Status** | [Draft / Review / Approved] |

---

## UTCS Metadata

```yaml
utcs:
  context: "[Product] / CB / Safety"
  content: "Hazard log for [System]"
  cache: "refs: [Safety standards, related analyses]"
  structure: "Hazard log template v1.0"
  style: "Safety documentation"
  sheet:
    id: "[HAZ-XXX]"
    version: "1.0"
    author: "[Name]"
    date: "YYYY-MM-DD"
```

---

## 1. Hazard Identification

### Hazard ID: [HAZ-XXX]

**Hazard Title**: [Brief descriptive title]

**Description**:
[Detailed description of the hazard]

**System/Component Affected**:
[Which system(s) or component(s) are involved]

**Phase of Flight / Mission**:
- [ ] Ground / Pre-launch
- [ ] Taxi / Takeoff
- [ ] Climb
- [ ] Cruise
- [ ] Descent
- [ ] Approach / Landing
- [ ] Post-landing
- [ ] Ascent (Space)
- [ ] Orbit (Space)
- [ ] Entry (Space)

---

## 2. Hazard Classification

### 2.1 Severity

Select one (per CS-25 or equivalent):

- [ ] **Catastrophic** (Cat I): Prevents continued safe flight and landing; multiple fatalities
- [ ] **Hazardous** (Cat II): Large reduction in safety margins; serious injuries; significant property damage
- [ ] **Major** (Cat III): Significant reduction in safety margins; some injuries; major system damage
- [ ] **Minor** (Cat IV): Slight reduction in safety margins; minor injuries; minor system damage
- [ ] **No Safety Effect** (Cat V): No effect on safety

**Justification**:
[Explain why this severity was assigned]

### 2.2 Likelihood

Select one (per CS-25 AMC 25.1309):

- [ ] **Frequent**: Probability > 10⁻³ per flight hour (> 1 in 1,000)
- [ ] **Reasonably Probable**: 10⁻³ to 10⁻⁵ per flight hour
- [ ] **Remote**: 10⁻⁵ to 10⁻⁷ per flight hour
- [ ] **Extremely Remote**: 10⁻⁷ to 10⁻⁹ per flight hour
- [ ] **Extremely Improbable**: < 10⁻⁹ per flight hour

**Estimated Probability**: [X.X × 10⁻ʸ per flight hour]

**Justification**:
[Explain how probability was estimated: analysis, similarity, test data, etc.]

### 2.3 Risk Matrix

| Severity → | No Effect | Minor | Major | Hazardous | Catastrophic |
|------------|-----------|-------|-------|-----------|--------------|
| **Frequent** | | | | | |
| **Reasonably Probable** | | | | | |
| **Remote** | | | **[X]** | | |
| **Extremely Remote** | | | | | |
| **Extremely Improbable** | | | | | |

**Risk Level**: [Acceptable / Unacceptable / Conditional]

---

## 3. Hazard Causes

### 3.1 Failure Modes

[List all failure modes that could cause this hazard]

1. **FM-1**: [e.g., H₂ tank leak due to fatigue crack]
   - **Mechanism**: [Fatigue from pressure cycles]
   - **Indicators**: [Pressure drop, leak detection alarm]

2. **FM-2**: [e.g., Leak detection system failure]
   - **Mechanism**: [Sensor contamination, electrical fault]
   - **Indicators**: [Self-test failure, no response to test gas]

### 3.2 Human Factors

[Identify any human error contributions]

**Example**:
- Maintenance error: Incorrect torque on fitting
- Operational error: Crew fails to monitor H₂ status

### 3.3 Environmental Factors

[Identify environmental contributions]

**Example**:
- Lightning strike
- Extreme cold affecting seals
- Bird strike damaging external components

---

## 4. Effects and Consequences

### 4.1 Immediate Effects

[What happens immediately when hazard occurs]

**Example**:
- H₂ leak into fuselage
- Concentration builds up in confined space

### 4.2 Cascading Effects

[What secondary effects may occur]

**Example**:
- If H₂ reaches 4% concentration → flammability risk
- If ignition source present → fire/explosion
- Loss of propulsion power

### 4.3 End State

[Ultimate consequence if not mitigated]

**Example**:
- Fire in fuselage → catastrophic structural failure
- Loss of aircraft

---

## 5. Mitigations

### 5.1 Design Mitigations

[Design features that reduce likelihood or severity]

| Mitigation | Type | Effectiveness | Status |
|------------|------|---------------|--------|
| [Redundant leak detection] | [Detection] | [Reduces likelihood by 10x] | [Implemented] |
| [Ventilation system] | [Containment] | [Prevents buildup] | [Implemented] |
| [Inertization N₂] | [Prevention] | [Eliminates flammability] | [Planned] |

### 5.2 Operational Mitigations

[Procedures, checklists, training]

| Mitigation | Type | Effectiveness | Status |
|------------|------|---------------|--------|
| [Pre-flight leak check] | [Procedure] | [Detects leaks before flight] | [Implemented] |
| [Crew H₂ awareness training] | [Training] | [Improves response] | [Planned] |
| [Emergency H₂ venting procedure] | [Procedure] | [Limits exposure] | [Implemented] |

### 5.3 Warning/Protection Systems

[Systems that alert crew or auto-protect]

| System | Function | Status |
|--------|----------|--------|
| [H₂ leak detection alarm] | [Alert crew] | [Implemented] |
| [Auto fuel cutoff] | [Isolate leak] | [Planned] |
| [Ventilation auto-activation] | [Dilute H₂] | [Implemented] |

---

## 6. Residual Risk

### 6.1 After Mitigation

**Revised Likelihood**: [X.X × 10⁻ʸ per flight hour]  
**Revised Severity**: [Cat I-V]  
**Residual Risk**: [Acceptable / Conditional]

**Justification**:
[Explain how mitigations reduce risk to acceptable level]

### 6.2 Acceptance Criteria

[Define what makes residual risk acceptable]

**Example**:
- Catastrophic hazards: Extremely Improbable (< 10⁻⁹/FH)
- Hazardous: Extremely Remote (< 10⁻⁷/FH)
- Major: Remote (< 10⁻⁵/FH)

**Status**: [✅ Meets criteria / ❌ Does not meet / ⏳ Under review]

---

## 7. Verification

### 7.1 Analysis

| Analysis | Purpose | Status | Location |
|----------|---------|--------|----------|
| [FTA-001] | [Quantify likelihood] | [Done/Pending] | [/products/.../CB/fta-001.md] |
| [CFD-001] | [H₂ dispersion sim] | [Done/Pending] | [/cax/cfd/h2-dispersion/] |

### 7.2 Testing

| Test | Purpose | Status | Results |
|------|---------|--------|---------|
| [TST-001] | [Leak detection validation] | [Done/Pending] | [Link] |
| [TST-002] | [Ventilation effectiveness] | [Done/Pending] | [Link] |

### 7.3 Inspections

| Inspection | Purpose | Frequency | Status |
|------------|---------|-----------|--------|
| [INS-001] | [Tank integrity] | [Pre-flight] | [Procedure defined] |
| [INS-002] | [Sensor calibration] | [Monthly] | [Procedure defined] |

---

## 8. Open Items

[Track any open actions related to this hazard]

| Item | Owner | Due Date | Status |
|------|-------|----------|--------|
| [Complete FTA analysis] | [Name] | [YYYY-MM-DD] | [⏳] |
| [Validate ventilation test] | [Name] | [YYYY-MM-DD] | [⏳] |
| [Finalize inertization design] | [Name] | [YYYY-MM-DD] | [⏳] |

---

## 9. Authority Review

### 9.1 Coordination

[Document interactions with certification authority]

| Date | Authority | Discussion | Outcome |
|------|-----------|------------|---------|
| [YYYY-MM-DD] | [EASA] | [Mitigation approach] | [Feedback received] |

### 9.2 Authority Acceptance

- [ ] Hazard classification accepted
- [ ] Mitigations accepted
- [ ] Residual risk acceptable
- [ ] Verification approach agreed

**Comments**:
[Any authority feedback or conditions]

---

## 10. Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Safety Engineer** | [Name] | | [YYYY-MM-DD] |
| **Chief Engineer** | [Name] | | [YYYY-MM-DD] |
| **Compliance Manager** | [Name] | | [YYYY-MM-DD] |
| **Authority (if required)** | [Name] | | [YYYY-MM-DD] |

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [YYYY-MM-DD] | [Name] | Initial hazard identification |
| 1.0 | [YYYY-MM-DD] | [Name] | Mitigations implemented, approved |

---

**Template Version**: 1.0  
**Last Updated**: 2024-Q4

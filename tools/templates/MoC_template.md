# Means of Compliance (MoC) Template

---

## Document Information

| Field | Value |
|-------|-------|
| **Product** | [AMPEL360-T-Air / AMPEL360-T-Space] |
| **System/Component** | [e.g., H₂ Tank System, LSS, E-fan Array] |
| **Regulation** | [e.g., EASA CS-25, ESA ECSS-E-ST-10C] |
| **Requirement ID** | [e.g., CS-25.1309, ECSS-E-ST-10C-5.2] |
| **Version** | [1.0] |
| **Date** | [YYYY-MM-DD] |
| **Author** | [Name/Team] |
| **Status** | [Draft / Review / Approved] |

---

## UTCS Metadata

```yaml
utcs:
  context: "[Product] / CB / [Domain]"
  content: "Means of Compliance for [Requirement ID]"
  cache: "refs: [Related docs, standards, analyses]"
  structure: "MoC template v1.0"
  style: "Compliance documentation"
  sheet:
    id: "[MoC-XXX-YYY]"
    version: "1.0"
    author: "[Name]"
    date: "YYYY-MM-DD"
```

---

## 1. Requirement Statement

**Regulation**: [e.g., CS-25.1309]

**Full Text**:
> [Copy verbatim text of the requirement from the regulation]

**Interpretation**:
[Brief explanation of what the requirement means in plain language]

**Applicability**:
[Explain why/how this requirement applies to your system]

---

## 2. Proposed Means of Compliance

### 2.1 Compliance Method

Select one or more:
- [ ] **Analysis**: Theoretical demonstration via calculations, models
- [ ] **Test**: Physical testing, bench tests, flight tests
- [ ] **Inspection**: Visual, NDT, functional inspection
- [ ] **Similarity**: Reference to previously certified similar design
- [ ] **AMC/GM**: Use of Acceptable Means of Compliance or Guidance Material

### 2.2 Detailed Approach

[Describe in detail how you will demonstrate compliance]

**Example**:
- **Analysis**: CFD simulation of H₂ leak dispersion + FEA of tank structure
- **Test**: Pressure cycle testing of tank (10,000 cycles), leak detection system validation
- **Inspection**: Post-manufacture inspection protocol (X-ray, ultrasonic)

### 2.3 Acceptance Criteria

[Define clear, measurable criteria that will demonstrate compliance]

**Example**:
- Tank withstands 1.5x max operating pressure without failure
- Leak detection system detects 0.1% H₂ concentration within 2 seconds
- No structural defects >1mm detected in inspection

---

## 3. Supporting Evidence

### 3.1 Analyses

| Analysis ID | Description | Status | Location |
|-------------|-------------|--------|----------|
| [ANA-001] | [e.g., FEA tank structure] | [Done/Pending] | [/cax/fea/tank-001/] |
| [ANA-002] | [e.g., Leak dispersion CFD] | [Done/Pending] | [/cax/cfd/leak-sim/] |

### 3.2 Tests

| Test ID | Description | Status | Location |
|---------|-------------|--------|----------|
| [TST-001] | [e.g., Pressure cycle test] | [Done/Pending] | [/qox/test-001/] |
| [TST-002] | [e.g., Leak detection validation] | [Done/Pending] | [/qox/test-002/] |

### 3.3 Documentation

| Document ID | Description | Status | Location |
|-------------|-------------|--------|----------|
| [DOC-001] | [e.g., Safety assessment] | [Done/Pending] | [/products/.../CB/safety-001.md] |
| [DOC-002] | [e.g., Design justification] | [Done/Pending] | [/products/.../FWD/design-just.md] |

---

## 4. Deviations & Special Conditions

### 4.1 Deviations from AMC

[If you are not using standard Acceptable Means of Compliance, explain why]

**Justification**:
[Explain why alternative approach is equivalent or better]

### 4.2 Special Conditions Needed

[If novel technology requires new Special Conditions]

**Description**:
[Describe the SC needed and its status]

**Example**:
- **SC-H2-001**: Hydrogen fuel system safety (in discussion with EASA)
- **Status**: Draft submitted Q4 2024, feedback expected Q1 2025

---

## 5. Risk Assessment

### 5.1 Residual Risks

[Identify any residual risks after implementing this MoC]

| Risk | Likelihood | Severity | Mitigation |
|------|------------|----------|------------|
| [e.g., Undetected micro-leak] | [Low/Med/High] | [Cat I-V] | [Redundant sensors, periodic inspection] |

### 5.2 Dependencies

[List dependencies on other systems/MoCs]

**Example**:
- Depends on MoC-002 (ventilation system) to ensure safe H₂ dispersion

---

## 6. Verification Status

| Activity | Planned Date | Actual Date | Status | Evidence |
|----------|--------------|-------------|--------|----------|
| Analysis complete | [YYYY-MM] | [YYYY-MM] | [✅/⏳/❌] | [Link] |
| Test complete | [YYYY-MM] | [YYYY-MM] | [✅/⏳/❌] | [Link] |
| Inspection complete | [YYYY-MM] | [YYYY-MM] | [✅/⏳/❌] | [Link] |
| Authority review | [YYYY-MM] | [YYYY-MM] | [✅/⏳/❌] | [Link] |
| **Final approval** | [YYYY-MM] | [YYYY-MM] | [✅/⏳/❌] | [Link] |

---

## 7. Authority Coordination

### 7.1 Discussions with Authority

[Document any discussions with EASA, ESA, NASA, etc.]

| Date | Authority | Topic | Outcome |
|------|-----------|-------|---------|
| [YYYY-MM-DD] | [EASA/ESA] | [MoC approach] | [Feedback, agreement, pending] |

### 7.2 Open Issues

[List any open questions or issues to resolve with authority]

1. [Issue 1: ...]
2. [Issue 2: ...]

---

## 8. Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Author** | [Name] | | [YYYY-MM-DD] |
| **Reviewer** | [Name] | | [YYYY-MM-DD] |
| **Compliance Manager** | [Name] | | [YYYY-MM-DD] |
| **Authority Representative** | [Name] | | [YYYY-MM-DD] |

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [YYYY-MM-DD] | [Name] | Initial draft |
| 1.0 | [YYYY-MM-DD] | [Name] | Approved version |

---

**Template Version**: 1.0  
**Last Updated**: 2024-Q4

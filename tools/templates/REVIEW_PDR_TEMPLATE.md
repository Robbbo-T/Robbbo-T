# Preliminary Design Review (PDR) — Review Package Template

> **NAME‑LOCK:** Use only the canonical names **AMPEL360-AIR-T** / **AMPEL360-SPACE-T**.  
> **Canon:** Adhere to TFA layers in the order `QS → FWD → UE → FE → CB → QB`.  
> **UTCS:** Each PDR package must reference at least one UTCS record ID and link MoC/Hazard artifacts.

---

## Document control

| Field | Value |
|---|---|
| Product | AMPEL360-AIR-T ☐ / AMPEL360-SPACE-T ☐ |
| Review ID | PDR-YYYY-XXX |
| Date | YYYY‑MM‑DD |
| Version | v0.1 (Draft) |
| Commit/Tag | <git SHA / tag> |
| UTCS Record ID(s) | utcs-XXXX, … |
| Review Board | Chair: … · Reviewers: … |
| Location | <onsite / virtual> |
| Distribution | Internal / Partners |
| Confidentiality | <level> |

---

## 1) Scope & Objectives

**Scope**  
- In-scope: …  
- Out-of-scope: …

**Objectives (success criteria)**  
- [ ] Objective #1 …  
- [ ] Objective #2 …  
- [ ] Objective #3 …

**Background / Prior reviews**  
- SRR outcome & deltas since SRR: …

---

## 2) Configuration & Baseline

- **Baseline under review:**  
  - Airframe/stack version: …  
  - Data package: … (link)  
  - Simulation configs: … (link)  

- **References**  
  - Drawings/models (CAE/CAD/CFD/FEA): …  
  - Analysis reports: …  
  - Test reports (bench/HIL/SIL): …  
  - External standards: EASA CS‑25 (+ SC H₂/electric), ESA/NASA HRP, …  
  - **CB matrix path(s):** see `qox/metrics.yaml → compliance.cb_matrix_paths`

- **Means of Compliance (MoC) landscape**  
  - List MoCs by requirement (Analysis / Inspection / Test / Similarity).  
  - Link specific MoC sheets (use `tools/templates/MoC_TEMPLATE.md`).

---

## 3) Requirements status

**Summary**  
- Total reqs: … · Closed: … · Open: … · At risk: …  
- Coverage by layer: QS ☐ / FWD ☐ / UE ☐ / FE ☐ / CB ☐ / QB ☐

**Requirements table**

| ID | Title | Source | MoC | Status | Owner | Notes |
|---|---|---|---|---|---|---|
| REQ‑… | … | Spec/Std | A/I/T/S | Open / Closed / Risk | … | … |

> **UTCS:** Update or attach UTCS record(s) summarizing requirement changes and artifact paths (`structure`, `sheet`).

---

## 4) Design overview (by TFA layer)

**QS** — Mission modeling, energy sizing, climate scenarios, optimization:  
- Key updates: …  
- Evidence (models/reports): …

**FWD** — Airframe/structure/TPS (SPACE) · BWB + tanks (AIR):  
- Key updates: …  
- Loads/margins: …

**UE** — HMI, cabin, evacuation, accessibility; aborts (SPACE):  
- Key updates: …  
- Human-factors findings: …

**FE** — Propulsion integration, thermal, BMS/avionics; LSS/docking (SPACE):  
- Key updates: …  
- Thermal & power budgets: …

**CB** — Certification basis & MoCs; standards mapping:  
- Key updates: …  
- Gaps & assumptions: …

**QB** — HIL/SIL, benches, test planning & results:  
- Key updates: …  
- Test readiness level (TRL) evidence: …

---

## 5) Risks (top‑5) & mitigations

| Risk ID | Description | Sev | Lklhd | Risk | Mitigation / Contingency | Owner | Due | Status |
|---|---|---|---|---|---|---|---|---|
| R‑1 | … | H/M/L | H/M/L | … | … | … | … | Open/Closed |

- **Notes:** Include risk scoring method, triggers, and exit criteria for “Closed”.  
- Link to hazard log entries in `tools/templates/HAZARD_LOG_TEMPLATE.csv` (or system).

---

## 6) Open items & actions

| Action ID | Description | Owner | Layer | Artifact (path) | Due | Status |
|---|---|---|---|---|---|---|
| A‑1 | … | … | QS/FWD/UE/FE/CB/QB | … | YYYY‑MM‑DD | Open |

> **Traceability:** Each action should reference UTCS record ID(s) and affected paths (`structure`).

---

## 7) Compliance & Safety (MAL‑EEM / CB)

- **MAL‑EEM checklist:** ☐ Attached (`governance/MAL-EEM/CHECKLIST.md`)  
- **Ethics & safety risk level:** Low ☐ · Medium ☐ · High ☐  
- **Compliance deltas:** New/changed SC/AMC, HRP items, national authority notes.  
- **Hazard log:** Entries added/updated → IDs: … (link)  
- **IV&V / Independent review hooks:** …

---

## 8) Demos / Analysis artifacts

- Simulation runs (IDs, configs, seeds): …  
- Test artifacts (data, plots, photos): …  
- Presentations / briefings: …

> Ensure all artifacts are UTCS-indexed. Large data should be linked, not embedded.

---

## 9) Decision & conditions

**Board decision**  
- [ ] **APPROVED** (proceed to CDR)  
- [ ] **CONDITIONALLY APPROVED** (conditions below)  
- [ ] **NOT APPROVED** (rework and re-review)

**Conditions / Exit criteria before CDR**  
1. …  
2. …  
3. …

**Sign-offs**  
- Chair: ___ · Date: ___  
- Product Lead: ___ · Date: ___  
- Safety Officer: ___ · Date: ___  
- Compliance: ___ · Date: ___

---

## Appendices

A) **Attendance & minutes** — Names, roles, timestamps, key comments.  
B) **Acronyms & glossary** — BWB, TPS, HIL, SIL, HRP, AMC, SC, …  
C) **Change log** — v0.1: draft; v0.2: added risks; v1.0: approved.

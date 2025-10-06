# MAL‑EEM Checklist (attach in PR)

> **Purpose:** Ethics & safety guardrail for all changes. Complete and attach this file to your PR.  
> **UTCS:** Reference at least one UTCS record and ensure hazard log entries are updated.  
> **Canon:** TFA layers `QS → FWD → UE → FE → CB → QB`; NAME‑LOCK enforced elsewhere in CI.

---

## 0) PR Metadata

- **PR title/ID:** …  
- **Author(s):** … · **Date:** YYYY‑MM‑DD  
- **UTCS record ID(s):** …  
- **Product(s) touched:** ☐ AMPEL360‑AIR‑T ☐ AMPEL360‑SPACE‑T  
- **TFA layers touched:** `QS` `FWD` `UE` `FE` `CB` `QB` (highlight those touched)

---

## 1) Core Checklist

- [ ] **Safety impact assessed** (crew / pax / ground / environment)  
  - Summary: …  
  - Impacted phases: ☐ storage ☐ handling ☐ fueling/defueling ☐ taxi/ops ☐ test/bench ☐ flight (sim/demo)

- [ ] **Data provenance recorded (UTCS record)**  
  - UTCS `structure` paths updated (logs, photos, data): …  
  - Primary `sheet` artifact: …

- [ ] **Hazard log entry added/updated** (`tools/templates/HAZARD_LOG_TEMPLATE.csv`)  
  - Hazard ID(s): …  
  - Link(s) to evidence: …

- [ ] **Dual‑use risk considered; mitigations documented**  
  - Scenario(s): …  
  - Mitigations / controls: …

- [ ] **If high‑risk: safety officer sign‑off attached**  
  - Safety risk level (select): ☐ low ☐ medium ☐ **high**  
  - Safety Officer: … · Date: … · Attachments: …

---

## 2) Risk Rating (required)

| Dimension | Value | Notes |
|---|---|---|
| **Severity** (S) | 1–5 | … |
| **Likelihood** (L) | 1–5 | … |
| **Risk = S × L** | … | Thresholds: Low ≤ 4 · Med 5–12 · High ≥ 15 |

**Acceptance gates**  
- **Quality score ≥ 0.95** (if applicable) → evidence: …  
- **Risk score ≤ 0.08** (if applicable) → method/calculation: …

---

## 3) Compliance & References

- **Regulatory basis** (as applicable):  
  ☐ CS‑25 SC H₂/electric ☐ ESA/NASA HRP ☐ ISO 21384‑3 (UAS) ☐ EASA Part 21 Subpart G ☐ other: …  
- **MoC sheets touched/created:** …  
- **References:**  
  - DMC‑ATA57‑STRUCT‑INSPECT‑EN (if applicable)  
  - SBOM: `sbom/AMPEL360‑AIR‑T.spdx.json` (or product‑specific)  
  - Policy: `policies/AMPEL360‑MoC‑v1.2.md` (or latest)

---

## 4) Hazard Log Snapshot (paste rows or summarize)

| id | date | product | layer | hazard | severity | likelihood | risk | mitigations | owner | utcs_id | status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| … | … | … | QS/FWD/… | … | … | … | … | … | … | … | Open/Closed |

---

## 5) Attachments & Evidence

- Test logs / data: …  
- Photos / diagrams: …  
- Procedures / permits: …  
- Calibration records: …  
- Others: …

> Store evidence under `.evidence/…` and list all relevant paths in your **UTCS** record’s `structure` array.

---

## 6) Approvals

- Product Lead: ___ · Date: ___  
- Safety Officer: ___ · Date: ___ (required for **high** risk)  
- Compliance (CB): ___ · Date: ___

---

## 7) Maintainer Notes (optional)

- CI results summary (UTCS schema, NAME‑LOCK, gates): …  
- Follow‑ups / actions opened: … (issue links)

---

### How to use
1. Copy this checklist into your PR description **or** attach it as `governance/MAL‑EEM/CHECKLIST_PR.md` in the diff.  
2. Ensure UTCS record(s) and hazard log are updated *in the same PR*.  
3. For **high‑risk** items, obtain Safety Officer signature before merge.

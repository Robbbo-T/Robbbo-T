# AMPEL360 — Project Overview

> **NAME‑LOCK:** Use canonical product names **AMPEL360‑AIR‑T** and **AMPEL360‑SPACE‑T**.  
> **Canon:** Follow TFA flow `QS → FWD → UE → FE → CB → QB`.  
> **Traceability:** All artifacts must have a **UTCS record** and, where applicable, **MAL‑EEM** checklist + hazard‑log entries.

**Mission:** Crewed aerospace (certified passenger transport) — advanced passenger and cargo transport systems with **quantum‑enhanced** capabilities.

---

## Product Lines (canonical)

### [products/ampel360-air-t/](../products/ampel360-air-t/)
Air transport product line for commercial aviation (BWB H₂ hybrid‑electric, quantum‑enhanced).

- **Variant concept:** `bwb-q100` — Blended Wing Body ~100‑passenger aircraft  
  _Proposed path:_ `products/ampel360-air-t/variants/bwb-q100/`

### [products/ampel360-space-t/](../products/ampel360-space-t/)
Crewed space transport (suborbital → orbital), with human‑rating path (ESA/NASA alignment).

- **Variant concept:** `plus` — tourism‑oriented suborbital system (AMPEL360 PLUS)  
  _Proposed path:_ `products/ampel360-space-t/variants/plus/`

> **Note:** Previous labels like `AMPEL360_AIR_TRANSPORT` / `AMPEL360_SPACE_TOURISM` are normalized to the canonical names above to satisfy CI **NAME‑LOCK** gates.

---

## Architecture & Framework

AMPEL360 products are built on a unified **Domain → Process → ATA** framework with full integration of:

- **QAFbW** — Quantum‑Augmented Flight for BWB and related configurations (optimization, guidance, scheduling, maintenance).  
- **AAA domain** — Advanced Aerodynamics (airframe aero, BWB integration, aero‑propulsive coupling).  
- **PPP domain** — Sustainable Propulsion (H₂ integration: fuel‑cell stacks + H₂ turbogenerator, thermal/icing control, e‑fans).  
- **IIS domain** — Integrated Intelligence Systems (avionics, onboard AI, health monitoring, digital twins).

**TFA flow** (repo‑wide): `QS (system/mission) → FWD (airframe/structure/TPS) → UE (crew/pax) → FE (propulsion/thermal/avionics) → CB (compliance) → QB (test/IV&V)`

**Traceability:** The **UTCS** system (governance/UTCS) indexes every artifact; CI blocks PRs without UTCS coverage.

---

## Certification Posture (targets)

- **AMPEL360‑AIR‑T:** EASA **CS‑25** baseline with **Special Conditions (H₂/electric)**; MoCs authored per requirement (Analysis/Inspection/Test/Similarity).  
- **AMPEL360‑SPACE‑T:** Human‑rating path aligned to **ESA/NASA HRP**; national authority engagement per test campaign phase.

> This program targets certification; until formally approved, documents must avoid asserting “is certified.” Use “**targeting certification**” or “**pre‑application engagement**”.

**References & templates**
- MoC template: `tools/templates/MoC_TEMPLATE.md` (and `tools/templates/MoC_RECORD_TEMPLATE.yaml`)  
- Hazard log: `tools/templates/HAZARD_LOG_TEMPLATE.csv`  
- MAL‑EEM policy & checklist: `governance/MAL‑EEM/`

---

## KPIs (program‑level)

- **AIR‑T efficiency:** ≥ **40%** reduction in E_pax‑km vs cylindrical baseline by PDR window.  
- **SPACE‑T cadence (Phase A):** readiness to demonstrate **≥ X/month**; **turnaround < 2 weeks**.  
- **Noise (AIR‑T):** **10–15 dB SEL** reduction in taxi/take‑off phases (electric modes).  
- **UTCS coverage:** 100% of significant artifacts indexed by Q3.

---

## Roadmap (12–18 months) — snapshot

### AMPEL360‑AIR‑T
- **Q1–Q2:** BWB subscale aero + cryo loop bench  
- **Q2–Q3:** HIL/SIL powertrain; e‑fan demo  
- **Q3–Q4:** Electric taxi trials; SC engagement; **PDR**

### AMPEL360‑SPACE‑T
- **Q1–Q2:** Phase A requirements; escape/abort study  
- **Q2–Q3:** TPS trade; captive‑carry plan; recovery ops concept  
- **Q3–Q4:** Drop tests; IV&V kickoff; **PDR**

**Cross‑cutting**
- UTCS indexing in `data/` and `qox/`  
- MAL‑EEM audits; hazard log stands up

> See `docs/ROADMAP.md` for the detailed, milestone‑level plan with exit criteria and risks.

---

## Repository Pointers

- **UTCS**: `governance/UTCS/` (SCHEMA, README, records/)  
- **Compliance**: `governance/COMPLIANCE/` (MoCs, CB matrices)  
- **Safety**: `docs/PLAYBOOKS/H2_SAFETY.md` (Hydrogen Ops)  
- **CI Gates**: `ci/gates/` (link/path validator, FCR/UTCS/NAME‑LOCK enforcer)  
- **Product pages**:  
  - AIR‑T → `products/ampel360-air-t/README.md`  
  - SPACE‑T → `products/ampel360-space-t/README.md`

---

## Directory Layout (suggested additions)

```
products/
  ampel360-air-t/
    variants/
      bwb-q100/
        README.md
  ampel360-space-t/
    variants/
      plus/
        README.md
```

Each variant keeps the canonical **TFA layer** folders beneath it as needed (`QS/ FWD/ UE/ FE/ CB/ QB`) and references UTCS records for traceability.

---

## Change Log

- **2025‑10‑06:** Initial normalization to NAME‑LOCK; mapped legacy labels and links to canonical repo structure; added certification posture caveat and pointers.

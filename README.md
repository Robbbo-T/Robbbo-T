# ROBBBO‑T · BOOTSTRAP REPO (TFA V2 / ASI‑T2)

> **SSoT & Guardrails:** This repository applies **ASI‑T · Universal Injection Prompt (v1)** as the **single source of truth** for all agent and human actions. **MAL‑EEM** (ethics & empathy) and **UTCS** (UiX Threading Context/Content/Cache and Structure/Style/Sheet) enforce full provenance and safety.

**TFA FLOW (Canon):** `QS → FWD → UE → FE → CB → QB`  
**PAx Orientation Markers:** `ONB` (Onboard), `OUT` (Outboard)

---

## NAME‑LOCK (SSoT)

Canonical product names are locked and must be used verbatim across code, docs, and CI:

- **AMPEL360‑AIR‑T** (Air: BWB H₂ hybrid‑electric, quantum‑enhanced)
- **AMPEL360‑SPACE‑T** (Space: crewed transport, suborbital → orbital)

> Any PR using alternative spellings (e.g., AMPEL360‑T‑Air / AMPEL360‑T‑Space) will be rejected by CI gates.

---

## 0) PORTFOLIO MANIFESTO

**Thesis:** Air & Space transport using **hybrid‑electric hydrogen** and **quantum‑enhanced systems**, with physics‑based verification, climate governance, and UTCS traceability.

**Product lines (T = transport, crewed):**
- **AMPEL360‑AIR‑T**: BWB H₂ hybrid‑electric (quantum‑enhanced)
- **AMPEL360‑SPACE‑T**: Crewed space transport (suborbital → orbital)

---

## 1) REPOSITORY STRUCTURE (MOD‑STACK / MOD‑PACK)

```text
robbbo-t/
├── canon/                         # CANON & GENESIS (SSoT)
│   ├── GENESIS_ASI-T2.md
│   ├── CANON_FACTS.md
│   └── INJECTION_PROMPT_v1.md
├── governance/
│   ├── MAL-EEM/                   # Ethics/Safety (policies, checklists)
│   ├── UTCS/                      # Traceability structures, SSoT templates
│   │   ├── SCHEMA.json
│   │   ├── README.md
│   │   └── records/
│   │       └── 2025-10-06_init.json
│   └── COMPLIANCE/                # Certification routes (EASA/ESA/NASA), Means of Compliance
├── ci/
│   ├── gates/
│   │   ├── FCR-1_checklist.md
│   │   ├── FCR-2_checklist.md
│   │   ├── link_path_validator.py
│   │   ├── fcr_enforcer.py
│   │   └── NAME_LOCK_ALLOWLIST.txt
│   ├── requirements.txt
│   └── workflows/
│       └── ci.yml
├── docs/
│   ├── ROADMAP.md
│   ├── PARTNERS.md
│   ├── FUNDING_EU.md
│   └── PLAYBOOKS/
│       └── H2_SAFETY.md
├── domains/                       # AAA…PPP (15 TFA domains)
│   ├── AAA/ …                     # (placeholders for all canonical domains)
│   └── PPP/
├── products/
│   ├── ampel360-air-t/
│   │   ├── README.md              # One‑pager + KPIs + TRLs
│   │   ├── QS/  FWD/  UE/  FE/  CB/  QB/
│   └── ampel360-space-t/
│       ├── README.md
│       ├── QS/  FWD/  UE/  FE/  CB/  QB/
├── sim/
│   ├── air/
│   └── space/
├── cax/
├── qox/
│   └── metrics.yaml
├── data/
└── tools/
    ├── templates/
    │   ├── MoC_TEMPLATE.md
    │   ├── HAZARD_LOG_TEMPLATE.csv
    │   └── REVIEW_PDR_TEMPLATE.md
    └── cli/
        └── rtx.py                 # CLI to create QS→FWD→UE→FE→CB→QB scaffolds
```

> **Rule:** Every product module must respect the **canonical order** `QS→FWD→UE→FE→CB→QB`. PRs that break the order or fail to update UTCS will be blocked by **CI gates**.

---

## 2) CHECKLISTS (by TFA layer)

**QS**

* [ ] Demand/energy models; H₂ sizing; routes; climate sensitivity.
* [ ] Noise, NOx, CO₂ targets (well‑to‑wake); H₂ grid scenarios.

**FWD**

* [ ] BWB integration (AIR) / structure & TPS (SPACE).
* [ ] Cryogenic management (insulation, ventilation, inerting).

**UE**

* [ ] Crew/pax HMI, evacuation, ergonomics, accessibility; aborts (SPACE).

**FE**

* [ ] H₂‑electric propulsion, BMS, thermal, distributed e‑fans; LSS/docking (SPACE).

**CB**

* [ ] Compliance matrix (EASA electric/H₂ SC; ESA/NASA HRP).

**QB**

* [ ] HIL/SIL, benches, taxi tests, drop/hover tests.

---

## 3) ONE‑PAGER · AMPEL360‑AIR‑T (BWB H₂ Hybrid‑Electric, Quantum‑Enhanced)

**Value proposition**

* 30–60% lower energy per pax‑km vs. cylindrical fuselage baseline (BWB advantages).
* Zero CO₂ in use (H₂) and strongly reduced NOx; very low noise in taxi/take‑off with electric modes.
* **Quantum‑enhanced**: hybrid quantum‑classical optimization for energy, routing, maintenance, certification cases.

**Architecture (QS→FWD→UE→FE→CB→QB)**

* **QS:** Hybrid/quantum digital twin; H₂L tank sizing; mission & climate scenarios; KPI dashboards.
* **FWD:** BWB airframe with conformal ONB cryogenic tanks; mass distribution; H₂ safety (inerting, ventilation, detection).
* **UE:** Cabin layout, evacuation, ergonomics; flight/energy HMI and procedures.
* **FE:** Fuel cell stack(s) + H₂ turbogenerator (peak/reserve) → distributed e‑fans; thermal management & icing control.
* **CB:** EASA CS‑25 baseline + special conditions for H₂/electric; emerging AMC; safety cases & compliance matrices.
* **QB:** Electric iron‑bird; cryogenic loop testbed; e‑fan demo; full‑electric taxi trials.

**Initial KPIs**

* ≥ 40% reduction in E_pax‑km; ≤ 30 min turnaround; ↑ MTBUR; 10–15 dB SEL noise reduction in critical ops phases.

**TRLs & milestones (12–18 months)**

* TRL 3–4: BWB subscale + cryogenic loop bench.
* TRL 5–6: HIL/SIL powertrain; electric taxi demonstration.
* TRL 6–7: Flight‑test prototype + special conditions for H₂/electric.

**Key risks**

* Effective energy density incl. insulation mass; thermal management; maturity of special conditions & MoC.

---

## 4) ONE‑PAGER · AMPEL360‑SPACE‑T (Crewed Transport)

**Evolutive strategy**

* **Phase A (Suborbital):** 6–10 pax; rapid turnaround; spaceport‑style ops; high‑reliability abort and recovery.
* **Phase B (LEO):** Light crew logistics; docking & on‑orbit ops; life support integration.
* **Phase C (LEO→GTO/Gateway):** H₂/O₂ refueled stages; **federated** architecture (FE) with partners & depots.

**Architecture (QS→FWD→UE→FE→CB→QB)**

* **QS:** Mission planning, abort envelopes, thermal margins; assisted entry‑guidance; reliability modeling.
* **FWD:** Pressurized structure; reusable TPS; high‑performance GNC and aero‑propulsive integration.
* **UE:** Human factors; escape/abort systems; fast recovery and line maintenance.
* **FE:** Stage integration; ground segment; life support; docking & interfaces.
* **CB:** ESA/NASA human‑rating path; flight safety; independent verification.
* **QB:** Drop/hover tests; captive carry; free flights; post‑flight inspection workflows.

**Initial KPIs**

* Cadence ≥ X/month; turnaround < 2 weeks (Phase A); abort‑safe reliability targets.

**Milestones**

* Progressive flight envelope expansion: uncrewed → crewed.
* Validated abort/escape; established recovery ops (sea/land).

**Key risks**

* Reusable TPS at sustainable cost; robust aborts; multi‑agency regulatory coordination.

---

## 5) REGULATORY PATH & PARTNERS

* **AIR:** Early EASA pre‑applications; special conditions for H₂/electric; safety cases & MoC.
* **SPACE:** ESA/NASA human‑rating, space standards; national authorities.
* **Key partners:** cryogenics, fuel cells, e‑fans, TPS, and spaceport operators.

---

## 6) CI GATES (PR/Commit Conventions)

* **PR conventions:** layer prefixes (`QS/`, `FWD/` …), UTCS links; MAL‑EEM checklist.
* **Validators:** `link_path_validator.py` and `fcr_enforcer.py` are mandatory; failures block merges.
* **Artifacts:** every PR must update UTCS (structure/style/sheet) and CB matrices.

---

## 7) NEXT STEPS

1. Generate product‑level *README.md* files using templates inside `products/…`.
2. Seed **GENESIS** and **CANON_FACTS** in `canon/` (as marked by the user).
3. Initialize **CI workflows** (lint + UTCS check + FCR gates).
4. Add initial MoC and hazard‑log templates under `tools/templates/`.
5. Open **issues** per TFA layer for each product (initial backlog).

---

## Quickstart (developer)

```bash
# 1) Install pre-commit for local guardrails
pipx install pre-commit || pip install pre-commit
pre-commit install

# 2) Run CI gates locally (same as Action)
make gate

# 3) Scaffold a product or a new TFA layer module
python tools/cli/rtx.py scaffold product ampel360-air-t
python tools/cli/rtx.py scaffold layer products/ampel360-air-t FE
```

**Contribution & Security**

* See `CONTRIBUTING.md`, `SECURITY.md`, and `governance/MAL-EEM/` for ethics & safety.




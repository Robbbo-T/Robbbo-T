# Roadmap (12–18 months) · **AMPEL360-AIR-T** & **AMPEL360-SPACE-T**

> **NAME-LOCK:** Use canonical strings **AMPEL360-AIR-T** / **AMPEL360-SPACE-T** everywhere.
> **Canon:** Follow TFA flow `QS → FWD → UE → FE → CB → QB`.
> **Traceability:** Every milestone must have at least one **UTCS record** (governance/UTCS/records) with `layers_touched`, `structure`, `sheet`, and MAL-EEM fields completed.

**Program start (assumed):** 2025-10-06 (Europe/Madrid)
**Quarter mapping (relative to start):**

* **Q1:** 2025-10-06 → 2025-12-31
* **Q2:** 2026-01-01 → 2026-03-31
* **Q3:** 2026-04-01 → 2026-06-30
* **Q4:** 2026-07-01 → 2026-09-30
  *(Optionally extend to Q5/Q6 for the 18-month horizon; see “Extension” at the end.)*

---

## Global goals & KPIs

* **Energy efficiency (AIR-T):** ≥ 40% ↓ E_pax-km vs cylindrical baseline by end of Q4.
* **Ops cadence (SPACE-T, Phase A):** readiness to demonstrate **cadence target ≥ X/month** with **turnaround < 2 weeks** by end of Q4.
* **Safety/Compliance:** MAL-EEM audits at each gate; live hazard log; CB matrices evolving monthly; special conditions (SC) engagement logged.
* **Readiness reviews:** SRR (if pending) → **PDR** (Q4) for both products with conditions to enter CDR.
* **UTCS coverage:** 100% of design/test artifacts indexed (UTCS) by Q3.

---

# AMPEL360-AIR-T

## Q1–Q2 · BWB subscale aero + cryo loop bench

**Objectives**

* Validate **BWB subscale aerodynamics** (low-Re wind-tunnel or CFD-validated) and **cryogenic loop bench** fundamentals for H₂L handling.

**Work packages (by TFA layer)**

* **QS:** Mission set & energy sizing; sensitivity to climate/route; define KPIs & acceptance thresholds.
* **FWD:** Subscale BWB geometry; tank placement & mass properties; aero/struct coupling plan.
* **UE:** Early cabin & evacuation layouts; HMI concepts for energy awareness.
* **FE:** Cryogenic loop architecture (insulation, venting, detection); heat-rejection concept; e-fan power budget.
* **CB:** Map CS-25 + SC (H₂/electric) landscape; initial MoC list; compliance matrix skeleton.
* **QB:** Build **cryo loop bench** (instrumented); bench-level procedures & safety.

**Deliverables**

* Subscale BWB CAD/CFD pack; force/moment & stability report.
* Cryo loop P&ID, **bench test plan**, commissioning logs, and **test report v1**.
* UTCS records for each artifact; MAL-EEM checklist; updated hazard log entries (ODH, cryo burn, ignition).

**Exit criteria**

* Aero subscale **corr. coefficient ≥ 0.9** vs target curves in validation regime.
* Cryo loop stable operation for **≥ 3 continuous hours**, controlled boil-off, sensors calibrated.
* Compliance matrix v0.1 published; ≥ 1 MoC draft per critical requirement.

**Primary risks & mitigations**

* **Low-Re fidelity gap →** matched-Re fixtures / CFD-WT correlation plan; scale correction.
* **Cryo icing / sensor drift →** heated taps, redundant sensors, calibration before/after runs.

---

## Q2–Q3 · HIL/SIL powertrain; **e-fan demo**

**Objectives**

* Validate electric powertrain control in **SIL/HIL** and demonstrate **e-fan** at representative load points.

**Work packages**

* **QS:** Optimization loop for mission power profiles; battery/fuel-cell hybridization strategy.
* **FWD:** Mounting & ducts integration envelopes for distributed e-fans (BWB).
* **UE:** Procedures for taxi & ramp ops; noise and ground-crew UX.
* **FE:** Integrate **fuel cell stack(s) + H₂ turbogenerator (peak/reserve)**; thermal/icing control logic.
* **CB:** Draft MoCs for power quality, EMC/EMI, and thermal safety; engage DER/experts as needed.
* **QB:** Build **SIL/HIL rig**; run functional & fault-injection tests; **e-fan demo** on test stand.

**Deliverables**

* HIL/SIL results report (latency, stability margins, FDIR cases).
* E-fan performance curves (η vs RPM, thrust vs power).
* Updated UTCS + hazard log (electric arc, hydrogen leak, rotating mass failures).

**Exit criteria**

* HIL closed-loop **phase margin ≥ 45°**, adequate gain margin; pass key FDIR scripts.
* E-fan demo reaches **≥ 95%** of predicted thrust at target power; vibration within limits.
* MoC drafts accepted internally; compliance gaps list with owners/dates.

**Risks & mitigations**

* **Thermal bottlenecks →** add heat-exchanger capacity, staged testing at rising loads.
* **Control oscillations →** tune with hardware-in-loop delay modeling; rate limiters, anti-windup.

---

## Q3–Q4 · Electric taxi trials; **SC engagement; PDR**

**Objectives**

* Conduct **electric taxi trials** (ground); formalize **special conditions (SC)** engagement; hold **PDR**.

**Work packages**

* **QS:** Mission-level energy accounting with measured taxi data; update KPIs.
* **FWD:** Gear loads & ground handling constraints; structural margin update.
* **UE:** Cockpit HMI for taxi/dispatch; ramp safety; crew training outline.
* **FE:** Integrated drivetrain-thermal-braking interactions during taxi; regenerative strategies.
* **CB:** Authority touchpoints (issue papers/questions); MoC updates; CB matrix v0.3.
* **QB:** Taxi test plan & safety case; run trials; post-trial inspection and teardown.

**Deliverables**

* Taxi trials **test report** (power draw, noise SEL, thermal margins).
* Authority engagement notes (Q&A, data requests).
* **PDR package** (use the PDR template): scope, requirements status, top-5 risks & mitigations, open actions, **Decision & conditions**.

**Exit criteria**

* Taxi power & thermal **within ±10%** of QS predictions for ≥ 30-min operation.
* Noise SEL reduction **10–15 dB** demonstrated vs baseline procedure.
* **PDR decision** recorded with conditions to proceed to CDR track.

**Risks & mitigations**

* **Unexpected power spikes →** refine ramp-rate limits / soft-start profiles.
* **Regulatory uncertainty →** early SC drafts + expert reviews; maintain MoC alternatives.

---

# AMPEL360-SPACE-T

## Q1–Q2 · Phase A requirements; **escape/abort study**

**Objectives**

* Freeze **Phase A (Suborbital) requirements** and complete **escape/abort study** with recovery concepts.

**Work packages**

* **QS:** Mission profiles, entry corridor, abort envelopes; reliability targets.
* **FWD:** Pressurized structure prelim sizing; mass & CG; interfaces for abort system.
* **UE:** Human-factors baselining; seats/restraints; egress; recovery ops UX.
* **FE:** **Life support** minima; GNC concept; ground segment outline.
* **CB:** Human-rating path mapping (ESA/NASA); safety/IV&V hooks.
* **QB:** Drop/hover **test planning**; instrumentation & site readiness.

**Deliverables**

* Requirements spec v0.9 (with MoC mapping).
* Abort modes analysis (credible failure trees; timelines; loads).
* Recovery concept of ops (sea/land), kitting & comms trees.

**Exit criteria**

* Closed requirements set with **≤ 10%** changes expected to PDR.
* Abort modes quantified with **decision logic** and survivability criteria.
* UTCS records for specs, models, and safety analyses.

---

## Q2–Q3 · **TPS trade; captive-carry plan;** recovery ops concept

**Objectives**

* Down-select **TPS** concept; design **captive-carry** demo plan; mature **recovery ops**.

**Work packages**

* **QS:** Thermal budgets; entry heating profiles; sensitivity to angle-of-attack and dispersion.
* **FWD:** TPS candidate trades (mass, maintainability, cost); structure-TPS integration.
* **UE:** Ground crew procedures; passenger pre-briefing materials; emergency roles.
* **FE:** GNC-TPS interaction; aero-propulsive integration impacts; docking (future phases) kept as interface.
* **CB:** IV&V plan; standards mapping updates; safety case outline for demo flights.
* **QB:** Captive-carry **test card set**; envelope build-up; range & safety coordination.

**Deliverables**

* TPS trade study with **weighted scoring**; down-select decision log.
* Captive-carry demo plan (aircraft, pylons/fixtures, telemetry, chase).
* Recovery ops **playbook v1** and drills plan.

**Exit criteria**

* TPS down-select justified (mass/thermals/ops) and approved.
* Captive-carry plan approved by safety & range; IV&V hooks integrated.

---

## Q3–Q4 · **Drop tests; IV&V kickoff; PDR**

**Objectives**

* Execute initial **drop tests** (or hover/captive-release as applicable); start **IV&V**; hold **PDR**.

**Work packages**

* **QS:** Update flight dynamics models with test data; refine reliability allocations.
* **FWD:** Structural responses and TPS local heating checks from test data.
* **UE:** Egress/recovery rehearsals; timelines & comms; human-factors notes.
* **FE:** GNC performance; sensor latency & noise characterization; ground segment drill.
* **CB:** IV&V kickoff (independent reviewers engaged); MoC updates; HRP alignment.
* **QB:** Execute drop/hover tests; inspections & non-conformance reports; data curation.

**Deliverables**

* Drop test report(s) with **high-speed video + telemetry**; model correlation.
* IV&V plan & minutes; issues list with owners.
* **PDR package** and decision log with conditions to advance.

**Exit criteria**

* Measured dynamic response **within ±15%** of model; identified deltas closed or planned.
* PDR approved (or conditionally approved) with a clear path to CDR.

---

# Cross-cutting (AIR-T & SPACE-T)

## UTCS indexing in `data/` and `qox/`

* **Goal:** 100% artifacts UTCS-indexed by end of Q3.
* **Actions:**

  * Enforce UTCS schema in CI; require `structure` paths for every major change.
  * Populate `qox/metrics.yaml` with KPI targets (energy, noise, turnaround, reliability).
  * Create UTCS “passports” for critical tests (sheet + attachments).

## MAL-EEM audits; hazard log stands up

* **Goal:** Routine MAL-EEM audits at the close of each quarter; live hazard log from Q1.
* **Actions:**

  * Run MAL-EEM checklist on all test plans and PDR pack.
  * Maintain `tools/templates/HAZARD_LOG_TEMPLATE.csv`; link IDs into UTCS records.
  * Classify safety risk level (low/medium/high) per change; require sign-off on high.

---

## Reviews & gates

| Gate                | When          | Inputs                                          | Exit criteria                                      |
| ------------------- | ------------- | ----------------------------------------------- | -------------------------------------------------- |
| **Quarterly Audit** | End of each Q | UTCS coverage, MAL-EEM, KPI deltas              | All red items have owners & dates; hazards triaged |
| **PDR (AIR-T)**     | Q4            | Taxi trials report, MoCs, CB matrix v0.3        | PDR decision + conditions to CDR                   |
| **PDR (SPACE-T)**   | Q4            | Drop test report(s), IV&V plan, TPS down-select | PDR decision + conditions to CDR                   |

---

## Staffing & roles (suggested)

* **Product Leads (AIR/SPACE)** — scope, priorities, external engagement.
* **Systems (QS/FE)** — mission modeling, integration, thermal & power budgets.
* **Structures/Propulsion (FWD/FE)** — BWB/TPS, cryo/drive systems.
* **Avionics & Controls (FE/QB)** — HIL/SIL, GNC, FDIR.
* **Safety & Compliance (CB/MAL-EEM)** — MoC authoring, audits, IV&V coordination.
* **Test & Ops (QB/UE)** — benches, taxi/drop ops, recovery drills.

---

## Risks register (top-level)

| ID | Risk                         | Impact        | Mitigation                                          | Owner        |
| -- | ---------------------------- | ------------- | --------------------------------------------------- | ------------ |
| R1 | Cryo bench instability       | Slips Q1–Q2   | Gradual cooldown protocol; redundant sensing        | Test lead    |
| R2 | Thermal limits in e-fan demo | Slips Q2–Q3   | Extra HX capacity; staged loads; real-time derating | FE lead      |
| R3 | SC/HRP ambiguity             | PDR delay     | Parallel MoCs; early authority Q&A; expert reviews  | CB lead      |
| R4 | TPS down-select deadlock     | SPACE-T slip  | Clear scoring rubric; schedule hold for re-trade    | FWD lead     |
| R5 | UTCS under-coverage          | Audit failure | CI enforcement; weekly UTCS review                  | Systems lead |

---

## Extension (Q5–Q6 · optional, to 18 months)

* **AIR-T:** Captive-carry propulsor nacelle aero; first towed-taxi + emergency stop; CDR prep.
* **SPACE-T:** Captive-carry execution; additional hover/dynamic tests; early environmental tests; CDR prep.
* **Both:** Supplier down-selects; SBOM baselining; cyber-safety review; pre-CDR audits.

---

### Required artifacts per milestone (summary)

* **UTCS record(s)** with `layers_touched`, `sheet`, `structure`, `mal_eem`.
* **MoC sheets** for new/changed requirements.
* **Hazard log updates** with mitigations.
* **Test plans & reports** (SIL/HIL, benches, taxi, drop).
* **PDR pack** using the standard template (Scope & Objectives, Requirements status, Risks (top-5) & mitigations, Open items & actions, Decision & conditions).

> If you want this rendered into a repo-ready `docs/ROADMAP.md` with checklists and pre-filled UTCS IDs, I can generate the file directly.

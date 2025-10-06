# H₂ Safety Playbook (Operations)

> **NAME‑LOCK:** Use canonical names **AMPEL360‑AIR‑T** / **AMPEL360‑SPACE‑T** only.
> **Canon:** Follow TFA layers `QS → FWD → UE → FE → CB → QB`.
> **UTCS:** Every procedure must reference a **UTCS record ID** and add/update entries in the **hazard log** (`tools/templates/HAZARD_LOG_TEMPLATE.csv`).
> **Scope:** This playbook governs storage, handling, operations (fueling/defueling), and emergency response for gaseous/liquid hydrogen (H₂) systems used by AIR‑T/SPACE‑T benches, ground equipment, and test articles.

---

## 0) Principles & Responsibilities

**Safety principles**
1. **Eliminate > Substitute > Engineer > Admin > PPE** (hierarchy of controls).
2. **Prove it with traceability** — if it isn’t UTCS‑indexed, it didn’t happen.
3. **No single point** of catastrophic failure: design for safe vent/isolation/relief.
4. **Static control** and **ignition source control** in all hazardous zones.

**Roles**
- **Safety Officer (SO):** authority to stop work; approves hot work/line breaks.
- **Test Conductor (TC):** controls the run; owns comms; executes E‑stop calls.
- **Hydrogen Custodian (HC):** custody of cylinders/cryogenic tanks; inventory & permits.
- **Instrumentation Lead (IL):** gas detection, ODH, data logging & calibration.
- **All Personnel:** badge in/out; follow muster & comms tree.

For *each* task or test, record **SO/TC/HC/IL** names and UTCS record in the procedure header.

---

## 1) Site Zoning & Equipment Ratings

- **Hazardous areas** must be classified and marked (e.g., Zone 1/2 or Class I Div 1/2); maintain zoning drawings under `governance/COMPLIANCE/`.
- **Equipment** in classified zones must be rated/approved for the zone (e.g., ATEX/IECEx) or installed per intrinsically safe/barrier design.
- **Vent/relief stacks**: exhaust to a safe height/location away from intakes, doors, and occupied areas; include flame arrestors where required.
- **Bonding/grounding**: permanent bonding for skids, temporary braids for vehicles/tankers; verify continuity before operations.

> **Deliverable:** Zoning map (PDF + native CAD) + UTCS record linking the revision and reviewer sign‑offs.

---

## 2) Instrumentation & Setpoints

**Gas detection** *(H₂ specific)*
- Mount H₂ detectors **high** (H₂ rises), within expected accumulation zones (ceilings, roofs, top corners, around vent terminations).
- Coverage must address: storage bay, fill connections, valve manifolds, test article enclosures, ceilings/voids.
- **Suggested setpoints** *(configure in `qox/metrics.yaml` and cite in UTCS)*:
  - **Warn:** 10% LFL → **0.4% vol H₂** in air
  - **Alarm:** 25% LFL → **1.0% vol H₂**
  - **Trip/Shutdown:** 50% LFL → **2.0% vol H₂**

**ODH (oxygen deficiency hazard)** *(cryo releases)*
- Place O₂ sensors at **breathing height** and near potential pooling zones.
- **Suggested setpoints**: **Warn:** 19.5% O₂ · **Alarm:** 18.0% O₂ → evacuate.

**Calibration & tests**
- **Bump test** before each shift; **calibrate** at least **monthly** or per manufacturer. Log to `.evidence/calibration/`.
- Record sensor IDs, setpoints, calibration gas lot, and due dates in UTCS.

---

## 3) Storage

**Cylinders (GH₂)**
- Secure upright; caps on when not connected; segregate by full/empty.
- Keep away from oxidizers; post “No Smoking / No Ignition Sources.”
- Manifolds with non‑return valves; leak check at every connection.

**Cryogenic tanks (LH₂)**
- Insulation intact; periodic IR scans for cold spots/boil‑off anomalies.
- **Relief devices** sized and tested per design; relief routed to safe vent stacks.
- **ODH monitoring** active; drainage to prevent pooling/ice hazards.

**Checklists** *(file under `docs/PLAYBOOKS/checklists/` and link in UTCS)*
- Storage daily walkdown (pressure, frost/ice, relief valves, sensors “OK”).
- Weekly bonding/grounding continuity check; signage/egress clear.

---

## 4) Handling

**Purge/inerting (lines & vessels)**
1. Verify permit (line break / cold work) approved by **SO**.
2. Bond/ground connected.
3. **Purge with dry N₂**, verify O₂ < threshold before admitting H₂.
4. Leak‑check with detector; keep purge exhaust vented to safe area.
5. Update UTCS with purge volumes, endpoints, and gas lots.

**Connections & leak checks**
- Use clean, compatible fittings; torque per spec; new seals/gaskets as specified.
- Prohibit PTFE tape shedding into lines; use approved thread types only.
- Leak check with certified detectors; avoid soap on cryogenic surfaces.

**Tools & ESD**
- Non‑sparking tools in zones; ESD wrist/heel grounds where required.
- No personal devices in classified areas unless rated.

---

## 5) Operations — Fueling / Defueling

**Pre‑Ops (Checklist)**
- [ ] Work permit(s) approved (hot/cold, line break).
- [ ] **E‑stop** locations briefed; comms tree tested (primary/secondary).
- [ ] Detector status **OK** (bump tested today); alarms audible/visible.
- [ ] Vent paths clear; winds acceptable per site limits.
- [ ] Fire protection on site (extinguishers, hydrants) and clear egress.
- [ ] **PPE:** cryo gloves/apron/face shield as applicable; safety glasses; hearing protection near e‑fans/pumps.
- [ ] UTCS record ID in header; hazard IDs referenced.

**Fueling steps (generic)**
1. **Isolate & depressurize** target volume; verify zero energy state.
2. Connect bonding/grounding; verify continuity.
3. Pre‑cool (for LH₂) as required; control cooldown rate to prevent shock.
4. Start **inert purge**; verify O₂ below threshold.
5. Admit H₂ at **controlled rate**; monitor differential pressures & temperatures.
6. Observe detector trends; maintain comms cadence; log key parameters.
7. Reach target fill; **stabilize**; check for leaks/frost; update gauges.
8. Isolate, bleed down lines; cap/secure; update UTCS & hazard log.

**Defueling**
- Reverse flow into qualified receiver; control boil‑off/venting; maintain ODH monitoring; complete post‑ops checks.

**Post‑Ops**
- [ ] Leak‑free verified; lines inerted or safe‑stored.
- [ ] Inventory updated; waste/vent logs filed.
- [ ] UTCS record updated with **structure** paths (logs, photos, data).

---

## 6) Emergencies

**Alarm triggers** *(configure via `qox/metrics.yaml`)*
- H₂ **Alarm ≥ 1.0% vol** or rapid rise **> set slope** → **E‑stop**, **evacuate**, activate comms tree.
- O₂ **≤ 18.0%** → **evacuate**; do **not** re‑enter until cleared.
- Visible leak/jet/venting anomaly; cryogenic spill; uncontrolled ice growth.

**Immediate actions**
1. **TC** calls **E‑stop**; isolate via remote valves if safe.
2. **SO** orders **evacuation** to muster points; roll call.
3. **HC** secures sources if safe; otherwise stand clear.
4. Notify emergency services; provide MSDS/SDS and site plan.

**Fire**
- Do **not** extinguish jet flame unless source can be isolated.
- Cool exposures with water fog; protect escape routes.

**ODH response**
- No entry without oxygen‑supplied respirators and authorization.
- Ventilate from **high points**; monitor O₂ until normal.

**Re‑entry criteria** *(document in UTCS)*
- Gas readings stable below **warn** for ≥ 30 min.
- Equipment inspected; incident log captured; SO authorizes entry.

---

## 7) Training, Drills, & Maintenance

- **Induction training** for all new staff; annual refresh.
- **Drills**: evacuation & comms tree **quarterly**; spill/leak tabletop **bi‑annually**.
- **Maintenance**: detector **bump test daily**, **cal monthly**; relief valve inspection per schedule; bonding/grounding checks weekly.
- Record all training & maintenance in UTCS and retain certificates.

---

## 8) Documentation & Records

- **Permits & checklists** stored alongside run logs in `.evidence/` with date/time, signatures, and photos.
- **UTCS linkage** mandatory: include `utcs_record_id`, `structure` artifact paths, `sheet` main doc, and **MAL‑EEM** fields.
- **Hazard log** entries updated (hazard id, severity/likelihood, mitigations, owner, status).

---

## 9) Configuration (project‑specific thresholds)

Maintain setpoints and limits in `qox/metrics.yaml` and reference them here. Example snippet:

```yaml
h2_safety:
  detectors:
    h2_warn_lfl_fraction: 0.10      # 10% LFL ≈ 0.4% vol
    h2_alarm_lfl_fraction: 0.25     # 25% LFL ≈ 1.0% vol
    h2_trip_lfl_fraction: 0.50      # 50% LFL ≈ 2.0% vol
    o2_warn_percent: 19.5
    o2_alarm_percent: 18.0
  wind_min_knots_for_venting: 3      # example; set per site
  vent_exclusion_radius_m: 10        # example; set per site
  cooldown_rate_k_per_min_max: 5     # example; set per hardware
```

Note: Regulatory codes/standards and authority requirements take precedence. Always align with site‑specific regulations and manufacturer instructions.

---

## 10) Checklists (printable)

### A) Storage Walkdown (daily)

- [ ] Cylinders secured, caps on, segregated (full/empty).
- [ ] LH₂ vessel pressures/temps normal; no abnormal frost/ice.
- [ ] Relief piping/vents unobstructed; signage visible.
- [ ] Detectors healthy; last calibration within interval.
- [ ] Egress routes clear; extinguishers present and within date.

### B) Pre‑Fueling

- [ ] Permits approved; roles assigned (SO/TC/HC/IL).
- [ ] Bonding/grounding verified; comms check OK.
- [ ] Detectors bump‑tested today; setpoints confirmed.
- [ ] Vent paths clear; winds acceptable; no ignition sources.
- [ ] UTCS record referenced in header; hazards updated.

### C) Post‑Ops

- [ ] Leak‑free; lines inert/safe‑stored.
- [ ] Inventory & logs updated; photographs stored.
- [ ] UTCS record updated with artifacts; hazard log entries completed.

### D) Emergency Muster

- [ ] E‑stop activated (if required) and sources isolated.
- [ ] Headcount at muster points completed.
- [ ] Gas readings trend to safe; re‑entry criteria documented.
- [ ] Incident UTCS record completed; lessons learned captured.

---

## Appendix — Properties of Hydrogen (quick reference)

**LFL (Lower Flammable Limit):** ~4% vol in air (at 1 atm).

**UFL (Upper Flammable Limit):** up to ~75% vol (wide range).

**Buoyancy:** rises quickly; accumulates at ceiling/high points.

**Cryo hazards (LH₂):** extreme cold → embrittlement; ODH potential from boil‑off.

**Ignition:** low energy; control static and eliminate sparks/open flames.

Treat all values as engineering references; confirm for your environment and hardware, and capture the final numbers in UTCS and `qox/metrics.yaml`.

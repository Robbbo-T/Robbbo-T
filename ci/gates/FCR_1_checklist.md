# ✅ FCR‑1 · Valid Inputs/Paths

**Purpose:** Ensure all contributions under `products/` adhere to canonical structure, traceability, and naming integrity within IDEALE.eu.

---

## 📁 Canonical Layer Enforcement

- Files under `products/*/**` must reside only within one of the six canonical TFA layer folders:
  - `QS` (Quantum Signature)
  - `FWD` (Forward Design)
  - `UE` (User Environment)
  - `FE` (Field Execution)
  - `CB` (Compliance Bridge)
  - `QB` (Quantum Bridge)

- No orphan artifacts or ad-hoc folders allowed under `products/`.

---

## 🧩 Metadata & Structure

- Every new file under `products/` must include a valid `layer:` field in its metadata or header block.
- If referencing a component UID, it must follow the canonical format:
  ```
  urn:ideale:component:<DOMAIN>:<MIC>:<PART>:<SN>
  ```

- Layer folders must not contain mixed product families unless explicitly declared via `bridge:` in UTCS.

---

## 🔗 Traceability Requirements

- All added files must be referenced in at least one UTCS record.
- UTCS record must pass schema validation (`governance/UTCS/SCHEMA.json`).
- No duplicate asset paths or UID collisions across layers.
- All referenced inputs must pass hash reproducibility check (e.g. SHA256 match).

---

## 🎖️ Badge Logic Placement

- If a file contains badge issuance logic, it must reside in the layer responsible for that badge’s origin.
- Badge deltas must be declared in the corresponding UTCS record under `calc.badge_delta`.

---

## 🛡️ NAME‑LOCK Compliance

- Canonical product names must be used exactly as defined:
  - `AMPEL360‑AIR‑T`
  - `AMPEL360‑SPACE‑T`

- Disallowed variants (e.g. `AMPEL360-Air-T`, `AMPEL360 T Space`) will trigger CI gate failure.
- Soft warning issued if canonical names are absent from changed text files.

---

## 🧠 CI Enforcement Summary

- ✅ Canonical layer path check
- ✅ UTCS record presence and schema validation
- ✅ NAME‑LOCK variant detection
- ✅ Badge delta preview (if present)
- ✅ TFA layer impact summary

---

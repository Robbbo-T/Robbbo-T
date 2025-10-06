# ✅ FCR‑2 · QS/UTCS Traceability

**Purpose:** Ensure every contribution is anchored to a valid UTCS record, enabling reproducibility, provenance, and badge issuance across layers.

---

## 📋 Checklist

| ID         | Rule                                                                 | Category        | Required     | Notes                                                                 |
|------------|----------------------------------------------------------------------|------------------|--------------|-----------------------------------------------------------------------|
| FCR‑2.1    | At least one UTCS record updated in this PR                         | Traceability     | ✅ Yes        | Located under `governance/UTCS/records/`                             |
| FCR‑2.2    | UTCS record lists all touched layers (QS/FWD/UE/FE/CB/QB)           | Traceability     | ✅ Yes        | Use `context.what.layer` or equivalent                               |
| FCR‑2.3    | UTCS schema must pass validation                                     | Compliance       | ✅ Yes        | Validated against `governance/UTCS/SCHEMA.json`                      |
| FCR‑2.4    | Artifacts must link back to UTCS record                              | Integrity        | ✅ Yes        | Fields: `sheet`, `structure`, `passport_ref`, `verify_log`           |
| FCR‑2.5    | UTCS record must include timestamp and actor                         | Provenance       | ✅ Yes        | Fields: `ts`, `actor_did`                                            |
| FCR‑2.6    | If `badge_delta` present, must be declared in `calc` section         | Governance       | ⚠️ Conditional | Used for badge issuance logic                                        |
| FCR‑2.7    | Replay must be possible with referenced inputs                       | Reproducibility  | ✅ Yes        | Inputs must include `path` and `sha256`                              |

---


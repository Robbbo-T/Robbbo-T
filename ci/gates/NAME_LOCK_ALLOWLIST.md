# ✅ NAME‑LOCK Allowlist

**Purpose:** Permit specific files to mention non‑canonical product name variants for documentation, educational, or illustrative purposes—without triggering CI gate failure.

---

## 📂 Allowed Paths

| Path Pattern       | Purpose                                  |
|--------------------|-------------------------------------------|
| `README.md`        | Top-level documentation and onboarding    |
| `docs/**.md`       | Extended documentation and guide examples  |
| `canon/**.md`      | Canonical references and naming guides       |

---

## 🛡️ Notes

- These paths are exempt from NAME‑LOCK enforcement regex.
- Use sparingly and only for illustrative or explanatory content.
- All other `.md`, `.py`, `.json`, `.yml` files must use **canonical product names**:
  - `AMPEL360‑AIR‑T`
  - `AMPEL360‑SPACE‑T`


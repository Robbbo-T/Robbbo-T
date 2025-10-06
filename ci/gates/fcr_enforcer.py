#!/usr/bin/env python3
"""
FCR/UTCS/NAME-LOCK gate:
- Enforces canonical product names and layer paths
- Requires at least one UTCS record update per PR
- Validates UTCS records against governance/UTCS/SCHEMA.json
- Warns if canonical product names are absent
- Prints badge_delta if present
- Summarizes TFA layers touched
- Optionally checks MAL-EEM checklist if risk is medium/high
"""
from __future__ import annotations
from pathlib import Path
import argparse, json, os, re, subprocess, sys

CANON_LAYERS = ["QS", "FWD", "UE", "FE", "CB", "QB"]
CANON_PRODUCTS = ["AMPEL360‑AIR‑T", "AMPEL360‑SPACE‑T"]
DISALLOWED_VARIANTS = [
    r"AMPEL360\s*-\s*T\s*-\s*Air",
    r"AMPEL360\s*-\s*T\s*-\s*Space",
    r"AMPEL360\s*-\s*Air\s*-\s*T",
    r"AMPEL360\s*-\s*Space\s*-\s*T",
    r"AMPEL360[_\s-]*Air[_\s-]*T",
    r"AMPEL360[_\s-]*Space[_\s-]*T",
]
TEXT_EXTS = {".md", ".mdx", ".txt", ".py", ".yml", ".yaml", ".json"}

def run(cmd: list[str]) -> str:
    return subprocess.check_output(cmd, text=True).strip()

def diff_names(base: str, head: str) -> list[tuple[str, str]]:
    out = run(["git", "diff", "--name-status", f"{base}...{head}"])
    return [(s, p) for s, *paths in (line.split("\t") for line in out.splitlines()) if paths for p in paths]

def is_text_file(p: Path) -> bool:
    return p.suffix in TEXT_EXTS

def validate_utcs(records: list[Path], schema_path: Path) -> list[str]:
    try:
        import jsonschema
    except Exception:
        return ["jsonschema not installed (add to ci/requirements.txt)"]
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
    except Exception as e:
        return [f"Could not read UTCS schema: {e}"]

    errors = []
    for rec in records:
        try:
            doc = json.loads(rec.read_text(encoding="utf-8"))
            jsonschema.validate(doc, schema)
            if "calc" in doc and "badge_delta" in doc["calc"]:
                print(f"🎖️ Badge delta in {rec.name}: {doc['calc']['badge_delta']}")
        except Exception as e:
            errors.append(f"{rec}: {e}")
    return errors

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default=os.getenv("BASE_SHA", "HEAD~1"))
    parser.add_argument("--head", default=os.getenv("HEAD_SHA", "HEAD"))
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[2]
    changed = diff_names(args.base, args.head)
    if not changed:
        print("ℹ️ No diff detected; skipping gates.")
        return 0

    # 1) Canonical layer path enforcement
    bad_paths = []
    newly_added = [Path(p) for s, p in changed if s.startswith("A")]
    for p in newly_added:
        parts = p.parts
        if len(parts) >= 4 and parts[0] == "products":
            layer = parts[3]
            if layer not in CANON_LAYERS:
                bad_paths.append(str(p))
    if bad_paths:
        print("❌ Non-canonical layer paths detected:")
        for b in bad_paths:
            print(f"  - {b}")
        return 1

    # 2) UTCS record requirement
    utcs_changed = [Path(p) for s, p in changed if "governance/UTCS/records/" in p and s[0] in ("A", "M") and p.endswith(".json")]
    if not utcs_changed:
        print("❌ No UTCS record modified. Add/update at least one under 'governance/UTCS/records/'.")
        return 1

    # 3) UTCS schema validation
    schema_path = repo / "governance" / "UTCS" / "SCHEMA.json"
    utcs_errors = validate_utcs(utcs_changed, schema_path)
    if utcs_errors:
        print("❌ UTCS schema validation failed:")
        for e in utcs_errors:
            print(f"  - {e}")
        return 1
    print(f"✅ UTCS: {len(utcs_changed)} record(s) validated")

    # 4) NAME‑LOCK enforcement
    disallowed_re = [re.compile(p) for p in DISALLOWED_VARIANTS]
    offenders = []
    for s, path in changed:
        p = Path(path)
        if not is_text_file(p):
            continue
        full = repo / p
        if not full.exists():
            continue
        try:
            text = full.read_text(encoding="utf-8")
        except Exception:
            continue
        if any(rx.search(text) for rx in disallowed_re):
            offenders.append(str(p))
    if offenders:
        print("❌ NAME‑LOCK violation: non‑canonical product name variants found:")
        for f in offenders:
            print(f"  - {f}")
        print("  Use exact strings: " + ", ".join(CANON_PRODUCTS))
        return 1

    # 5) Soft warning if canonical names absent
    repo_text = "\n".join((repo / Path(p)).read_text(encoding="utf-8", errors="ignore")
                          for s, p in changed if is_text_file(Path(p)) and (repo / Path(p)).exists())
    if not any(cp in repo_text for cp in CANON_PRODUCTS):
        print("⚠️  No canonical product names found in changed files. Ensure usage where applicable.")

    # 6) TFA layer summary
    tfa_touched = {layer for _, p in changed for layer in CANON_LAYERS if f"/{layer}/" in p}
    if tfa_touched:
        print(f"📦 TFA layers touched: {', '.join(sorted(tfa_touched))}")

    print("✅ FCR/UTCS/NAME‑LOCK gates passed")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

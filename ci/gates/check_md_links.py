#!/usr/bin/env python3
"""
Markdown Link Validator for IDEALE.eu

Scans all Markdown files for broken relative links.
Fails CI if any non-HTTP(S)/mailto/tel links point to missing files.
Skips image links and fragment-only anchors.
"""

from pathlib import Path
import re
import sys

RE_MD_LINK = re.compile(r'(?<!!)

\[[^\]

]+\]

\(([^)]+)\)')  # skip images
SKIP_SCHEMES = ("http://", "https://", "mailto:", "tel:")

def main() -> int:
    repo = Path(__file__).resolve().parents[2]
    md_files = [p for p in repo.rglob("*.md") if ".git" not in p.parts]
    missing = []

    for md in md_files:
        try:
            text = md.read_text(encoding="utf-8")
        except Exception as e:
            print(f"[WARN] Could not read {md}: {e}", file=sys.stderr)
            continue

        for match in RE_MD_LINK.finditer(text):
            raw = match.group(1).strip()
            if not raw or raw.startswith("#") or raw.startswith(SKIP_SCHEMES):
                continue
            target = raw.split("#", 1)[0]  # remove fragment
            if target.startswith("/"):  # absolute path outside repo
                continue
            candidate = (md.parent / target).resolve()
            if not candidate.exists():
                missing.append((md.relative_to(repo), raw))

    if missing:
        print("❌ Broken relative links detected:")
        for md, raw in missing:
            print(f"  - {md}: '{raw}'")
        return 1

    print("✅ All Markdown links resolved successfully")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

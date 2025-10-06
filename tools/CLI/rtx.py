#!/usr/bin/env python3
"""
rtx.py — ROBBBO‑T scaffolder for canonical products and TFA layers.
"""
from __future__ import annotations
from pathlib import Path
import argparse
import sys
from datetime import datetime
import json

CANON_LAYERS = ["QS", "FWD", "UE", "FE", "CB", "QB"]
CANON_PRODUCTS = ["ampel360-air-t", "ampel360-space-t"]

def write(p: Path, content: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    if not p.exists():
        p.write_text(content, encoding="utf-8")
        print(f" + {p}")
    else:
        print(f" = {p} (exists)")

def scaffold_product(root: Path, slug: str) -> None:
    if slug not in CANON_PRODUCTS:
        print(f"ERROR: product must be one of {CANON_PRODUCTS}")
        sys.exit(1)
    base = root / "products" / slug
    write(base / "README.md", f"# {slug.replace('-', ' ').title()} (placeholder)\n\nSee UTCS records.")
    for layer in CANON_LAYERS:
        (base / layer).mkdir(parents=True, exist_ok=True)
        write(base / layer / ".gitkeep", "")
    print("Scaffold complete.")

def scaffold_layer(path: Path, layer: str) -> None:
    layer = layer.upper()
    if layer not in CANON_LAYERS:
        print(f"ERROR: layer must be in {CANON_LAYERS}")
        sys.exit(1)
    (path / layer).mkdir(parents=True, exist_ok=True)
    write(path / layer / "README.md", f"# {layer}\n\nUTCS: add record for changes.")
    print(f"Layer {layer} ready at {path}")

def add_utcs_record(root: Path, product_canon: str, layers: list[str], summary: str) -> None:
    now = datetime.utcnow().isoformat() + "Z"
    rid = f"utcs-{now.replace(':','').replace('-','')[:15]}"
    doc = {
        "id": rid,
        "timestamp": now,
        "author": "dev",
        "pax_marker": "ONB",
        "product": product_canon,
        "layers_touched": layers,
        "structure": [],
        "style": "note",
        "sheet": "",
        "qs_context": {"problem": "", "assumptions": [], "dependencies": []},
        "content_summary": summary,
        "cache_refs": [],
        "mal_eem": {"ethics_reviewed": True, "safety_risk_level": "low", "notes": ""},
        "compliance_impacts": {"easa": "", "esa": "", "nasa": "", "moc_updates": False},
        "attachments": []
    }
    out = root / "governance" / "UTCS" / "records" / f"{rid}.json"
    write(out, json.dumps(doc, indent=2, ensure_ascii=False))

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("scaffold", help="Create product/layer scaffolds")
    sp.add_argument("kind", choices=["product", "layer"])
    sp.add_argument("target")
    sp.add_argument("maybe_layer", nargs="?")

    su = sub.add_parser("utcs", help="Add a UTCS record")
    su.add_argument("--product", required=True, choices=["AMPEL360‑AIR‑T", "AMPEL360‑SPACE‑T"])
    su.add_argument("--layers", required=True, help="Comma-separated list of layers (QS,FWD,UE,FE,CB,QB)")
    su.add_argument("--summary", required=True)

    args = ap.parse_args()
    root = Path(__file__).resolve().parents[2]

    if args.cmd == "scaffold":
        if args.kind == "product":
            scaffold_product(root, args.target)
        else:
            scaffold_layer(Path(args.target), args.maybe_layer or "QS")
    elif args.cmd == "utcs":
        add_utcs_record(root, args.product, [l.strip().upper() for l in args.layers.split(",")], args.summary)

if __name__ == "__main__":
    main()

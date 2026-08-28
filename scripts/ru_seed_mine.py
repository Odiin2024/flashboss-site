#!/usr/bin/env python3
"""Seed the fleet's draft cache from Claude's hand-written TSVs, so the
Chinese fleet audits Claude's own translations on the same footing as its own.
"""
import json, os, sys
CACHE = "update/ru/.fleet/draft"
os.makedirs(CACHE, exist_ok=True)
for page in sys.argv[1:]:
    tsv = f"update/ru/{page}.strings.tsv"
    if not os.path.exists(tsv):
        print(f"  {page}: no TSV"); continue
    out, i = {}, 0
    for ln in open(tsv, encoding="utf-8"):
        ln = ln.rstrip("\n")
        if not ln or ln.startswith("#") or "\t" not in ln: continue
        en, ru = ln.split("\t", 1)
        en, ru = en.replace("\\n", "\n"), ru.replace("\\n", "\n")
        if not en or not ru: continue
        out[str(i)] = {"en": en, "ru": ru, "kind": "claude"}
        i += 1
    json.dump(out, open(f"{CACHE}/{page}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"  {page}: seeded {i} pairs")

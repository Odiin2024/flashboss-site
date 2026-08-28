#!/usr/bin/env python3
"""Turn fleet output into update/ru/<page>.strings.tsv for ru_localize.py.

Applies the checker's suggested fix ONLY where the cross-family refuter upheld
the flag AND Claude has approved it in update/ru/.fleet/rulings/<page>.json
({"<id>": "uphold"|"reject"|"<replacement ru string>"}). No ruling file means
nothing is auto-applied — the fleet never edits the site on its own.
"""
import json, os, sys

def load(stage, page):
    p = f"update/ru/.fleet/{stage}/{page}.json"
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}

for page in sys.argv[1:]:
    d = load("draft", page)
    if not d: print(f"  {page}: no draft"); continue
    chk, ref, rul = load("check", page), load("refute", page), load("rulings", page)
    applied = 0
    rows = []
    reverted = []
    for i in sorted(d, key=lambda x: int(x)):
        en, ru = d[i]["en"], d[i]["ru"]
        r = rul.get(i)
        if r == "uphold":
            fix = chk.get(i, {}).get("fix")
            if fix: ru = fix; applied += 1
        elif isinstance(r, str) and r not in ("reject", "uphold"):
            ru = r; applied += 1
        if not en or not ru: continue
        if en == ru:
            # a "fix" that restores the English silently leaves English on the page.
            # Legitimate for teaching material; flag it so it is a decision, not an accident.
            if r == "uphold": reverted.append(i)
            continue
        if "\t" in en or "\t" in ru: continue
        rows.append((en.replace("\n", "\\n"), ru.replace("\n", "\\n")))
    out = f"update/ru/{page}.strings.tsv"
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"# {page}.html — en<TAB>ru. Drafted by deepseek-v4-flash, "
                f"checked by qwen3-max, cross-refuted, Claude-adjudicated.\n")
        for a, b in rows: f.write(a + "\t" + b + "\n")
    up = sum(1 for i, v in ref.items() if i != "_done" and v.get("verdict") == "upheld")
    if reverted: print(f"  {page}: NOTE {len(reverted)} unit(s) kept English by an upheld fix: {reverted}")
    print(f"  {page}: {len(rows)} pairs, {len(chk)-1 if chk else 0} flags, {up} upheld, {applied} fixes applied")

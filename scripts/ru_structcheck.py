#!/usr/bin/env python3
"""Deterministic structural check of every drafted unit.

An LLM checker notices dropped markup unreliably. This does not: it compares the
exact tag sequence and every href/src of the English unit against the Russian
one. Anything that differs is a real defect, no adjudication needed.
"""
import json, os, re, sys

def sig(html):
    tags = re.findall(r'<\s*(/?)\s*([a-zA-Z][a-zA-Z0-9]*)', html)
    return [f"{s}{t.lower()}" for s, t in tags]
def urls(html): return sorted(re.findall(r'(?:href|src)="([^"]*)"', html))
def ents(html): return sorted(re.findall(r'&[a-zA-Z#0-9]+;', html))

bad = {}
for p in sys.argv[1:]:
    f = f"update/ru/.fleet/draft/{p}.json"
    if not os.path.exists(f): continue
    d = json.load(open(f, encoding="utf-8"))
    for k, v in d.items():
        en, ru = v["en"], v["ru"]
        why = []
        if sig(en) != sig(ru): why.append(f"tags {sig(en)} -> {sig(ru)}")
        if urls(en) != urls(ru): why.append(f"links {urls(en)} -> {urls(ru)}")
        if ents(en) != ents(ru): why.append(f"entities {ents(en)} -> {ents(ru)}")
        if why: bad.setdefault(p, []).append((k, why, en, ru))
tot = sum(len(v) for v in bad.values())
for p, rows in bad.items():
    print(f"\n=== {p}: {len(rows)} structural break(s)")
    for k, why, en, ru in rows[:6]:
        print(f"  #{k}: {why[0][:120]}")
        print(f"    EN {en[:100]}")
        print(f"    RU {ru[:100]}")
print(f"\nTOTAL structural breaks: {tot}")

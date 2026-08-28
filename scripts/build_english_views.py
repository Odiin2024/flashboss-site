#!/usr/bin/env python3
"""Build the site's word-list views for the three English EFL packs.

English Core, Pareto 1 and Pareto 2 are the English-as-a-foreign-language packs.
knight deliberately ships no CORE_FINAL for English (build_set_views.py says so:
the Steam depot recipe excludes those artifacts), and English Core has no view
at all — so its cluster 1-1 does not exist anywhere the site can reach. This
builds the views the website needs, straight from the real cluster cards,
without touching the game repo.

SPELLING: the cards carry a full British twin layer (TargetWord_gb /
Translation_gb). knight's shipped English Pareto views are built from it — 26 of
27 differences against the base are exactly the _gb twin. So --spelling gb is
the default, to match those siblings. --spelling us builds from the American
base instead, which is what english.html claims is the base. One flag either
way; see the note in the session summary.

  python3 scripts/build_english_views.py            # gb, matching the siblings
  python3 scripts/build_english_views.py --spelling us
"""
import argparse, glob, json, os, re

REPO = "/home/odiin/Documents/Bootcamp/knight/flashcard_sets"
SETS = [("Core", "English/core", "core", 0),
        ("Pareto 1", "English_Extensions/pareto1", "p1", 1000),
        ("Pareto 2", "English_Extensions/pareto2", "p2", 2000)]

def ck(p):
    m = re.search(r'cluster(\d+)_(\d+)', os.path.basename(p))
    return (int(m.group(1)), int(m.group(2)))

def walk(setdir):
    root = os.path.join(REPO, setdir); out = []
    for td in sorted(glob.glob(root + "/tier_*"),
                     key=lambda x: int(re.search(r'tier_(\d+)', x).group(1))):
        for cd in sorted([c for c in glob.glob(td + "/*") if os.path.isdir(c)], key=ck):
            s = os.path.basename(cd); f = os.path.join(cd, s + ".json")
            if os.path.isfile(f):
                t, c = ck(cd)
                out.append({"cluster_id": f"T{t}-C{c}", "tier": t, "slug": s,
                            "raw": json.load(open(f, encoding="utf-8"))})
    return out

def card(raw, n, sp):
    w = raw.get(f"TargetWord_{sp}") or raw["TargetWord"] if sp == "gb" else raw["TargetWord"]
    t = raw.get(f"Translation_{sp}") or raw["Translation"] if sp == "gb" else raw["Translation"]
    o = {"n": n, "TargetWord": w, "TargetArticle": raw.get("TargetArticle", ""), "Translation": t}
    if raw.get("TriggerLesson"): o["TriggerLesson"] = raw["TriggerLesson"]
    return o

def serialize(language, setlabel, total, offset, clusters, sp):
    out = ["{", f'  "language": {json.dumps(language)},', f'  "set": {json.dumps(setlabel)},',
           f'  "total": {total},', f'  "offset": {offset},', '  "clusters": [']
    n = 0
    for ci, cl in enumerate(clusters):
        out.append("    {")
        out.append(f'      "cluster_id": {json.dumps(cl["cluster_id"])}, "tier": {cl["tier"]}, '
                   f'"slug": {json.dumps(cl["slug"])},')
        out.append('      "cards": [')
        lines = []
        for r in cl["raw"]:
            n += 1; lines.append(json.dumps(card(r, n, sp), ensure_ascii=False))
        for li, ln in enumerate(lines):
            out.append(f"        {ln}" + ("," if li < len(lines) - 1 else ""))
        out.append("      ]")
        out.append("    }" + ("," if ci < len(clusters) - 1 else ""))
    out += ["  ]", "}"]
    return "\n".join(out) + "\n"

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--spelling", choices=("gb", "us"), default="gb")
    a = ap.parse_args()
    for label, setdir, code, offset in SETS:
        cls = walk(setdir)
        total = sum(len(c["raw"]) for c in cls)
        txt = serialize("English", label, total, offset, cls, a.spelling)
        d = os.path.join("data", "english", code); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "CORE_FINAL.json"), "w", encoding="utf-8").write(txt)
        first = cls[0]
        print(f"  data/english/{code}/CORE_FINAL.json  {label:<9} {total} cards, "
              f"{len(cls)} clusters, first={first['cluster_id']} {first['slug']}")

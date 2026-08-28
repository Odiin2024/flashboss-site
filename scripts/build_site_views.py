#!/usr/bin/env python3
"""Build the site's word-list views for the packs knight ships no view for.

English Core, Pareto 1 and Pareto 2 are the English-as-a-foreign-language packs.
knight deliberately ships no CORE_FINAL for English (build_set_views.py says so:
the Steam depot recipe excludes those artifacts), and English Core has no view
at all — so its cluster 1-1 does not exist anywhere the site can reach. This
builds the views the website needs, straight from the real cluster cards,
without touching the game repo.

SPELLING: the cards carry a full British twin layer (TargetWord_gb /
Translation_gb). knight's shipped English Pareto views are built from it — 26 of
27 differences against the base are exactly the _gb twin. Odiin's ruling 2026-08-28: the site default is US, matching english.html's
"American English base with a full British spelling option". --spelling gb
builds from the British twin instead.

  python3 scripts/build_english_views.py            # us (the default)
  python3 scripts/build_english_views.py --spelling gb
"""
import argparse, glob, json, os, re

REPO = "/home/odiin/Documents/Bootcamp/knight/flashcard_sets"
# (language, set label, knight dir, site path, offset, mode)
#  mode "eng"  -> English EFL: TargetWord + Translation, honours the gb/us twin
#  mode "lang" -> language pack: TargetWord + TargetArticle + Translation
SETS = [("English", "Core",     "English/core",               "data/english/core/CORE_FINAL.json",   0,    "eng"),
        ("English", "Pareto 1", "English_Extensions/pareto1", "data/english/p1/CORE_FINAL.json",     1000, "eng"),
        ("English", "Pareto 2", "English_Extensions/pareto2", "data/english/p2/CORE_FINAL.json",     2000, "eng"),
        # Latin ships no CORE_FINAL either (same depot ruling). Core + Pareto 1 only.
        ("Latin",   "Core",     "Latin/core",                 "data/latin/CORE_FINAL.json",          0,    "lang"),
        ("Latin",   "Pareto 1", "Latin/pareto1",              "data/latin/PARETO1_FINAL.json",       1000, "lang")]

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

def card(raw, n, sp, mode):
    w, t = raw["TargetWord"], raw["Translation"]
    if mode == "eng" and sp == "gb":
        w = raw.get("TargetWord_gb") or w
        t = raw.get("Translation_gb") or t
    o = {"n": n, "TargetWord": w, "TargetArticle": raw.get("TargetArticle", ""), "Translation": t}
    if raw.get("Elides"): o["Elides"] = True
    if raw.get("TriggerLesson"): o["TriggerLesson"] = raw["TriggerLesson"]
    return o

def serialize(language, setlabel, total, offset, clusters, sp, mode):
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
            n += 1; lines.append(json.dumps(card(r, n, sp, mode), ensure_ascii=False))
        for li, ln in enumerate(lines):
            out.append(f"        {ln}" + ("," if li < len(lines) - 1 else ""))
        out.append("      ]")
        out.append("    }" + ("," if ci < len(clusters) - 1 else ""))
    out += ["  ]", "}"]
    return "\n".join(out) + "\n"

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--spelling", choices=("gb", "us"), default="us")
    a = ap.parse_args()
    for lang, label, setdir, out, offset, mode in SETS:
        cls = walk(setdir)
        if not cls:
            print(f"  !! {setdir}: no clusters found — skipped"); continue
        total = sum(len(c["raw"]) for c in cls)
        txt = serialize(lang, label, total, offset, cls, a.spelling, mode)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(txt)
        first = cls[0]
        print(f"  {out:<36} {lang} {label:<9} {total} cards, "
              f"{len(cls)} clusters, first={first['cluster_id']} {first['slug']}")

#!/usr/bin/env python3
"""Build the site's word-list views straight from the real cluster cards.

Covers the three English EFL packs (Core, Pareto 1, Pareto 2) and Latin
(Core + Pareto 1). Latin still ships no view from the game repo; English did not
either until 2026-08-30, when the three packs were registered in knight's
build_set_views.py. The site keeps building its own regardless, because it needs
a different shape: the British twin inline (see below) and a per-pack folder
layout the word-list page fetches by code.

SPELLING: the cards carry a full British twin layer (TargetWord_gb /
Translation_gb). Odiin's ruling 2026-08-28 is that the site default is US,
matching english.html's "American English base with a full British spelling
option". --spelling gb builds from the British twin instead.

  python3 scripts/build_site_views.py              # us (the default)
  python3 scripts/build_site_views.py --spelling gb

SPELLING TWINS ARE NOT OPTIONAL. The English packs get their twin written
inline by card(), and this script then runs inject_english_gb.py itself for the
six standalone English packs it does not build. Running this script alone
therefore leaves the whole English set complete — losing the twins is a silent
failure (the page simply stops offering UK), and it happened once.
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
    """One lean card. English packs carry their spelling twin inline.

    The twin is written here, not bolted on afterwards, so a build can never
    ship English without it — that failure is silent (the page just stops
    offering UK) and it has happened once already.
    """
    base_w, base_t = raw["TargetWord"], raw["Translation"]
    gb_w = raw.get("TargetWord_gb") or base_w
    gb_t = raw.get("Translation_gb") or base_t
    w, t = (gb_w, gb_t) if (mode == "eng" and sp == "gb") else (base_w, base_t)
    o = {"n": n, "TargetWord": w, "TargetArticle": raw.get("TargetArticle", ""), "Translation": t}
    if raw.get("Elides"): o["Elides"] = True
    if raw.get("TriggerLesson"): o["TriggerLesson"] = raw["TriggerLesson"]
    if mode == "eng":
        # the OTHER spelling, recorded only where it actually differs
        other_w, other_t = (base_w, base_t) if sp == "gb" else (gb_w, gb_t)
        suf = "_us" if sp == "gb" else "_gb"
        if other_w != w: o["TargetWord" + suf] = other_w
        if other_t != t: o["Translation" + suf] = other_t
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
        gb = sum(1 for c in cls for r in c["raw"]
                 if r.get("TargetWord_gb") or r.get("Translation_gb"))
        print(f"  {out:<36} {lang} {label:<9} {total} cards, "
              f"{len(cls)} clusters, first={first['cluster_id']} {first['slug']}"
              + (f", {gb} spelling twins" if mode == "eng" else ""))

    # The six standalone English packs (Adept/Advance/Roots) are built upstream,
    # not here, so their twins still come from the injector. Run it automatically:
    # one command must leave the whole English set canonical, or the twins rot.
    #
    # Only for a US build. The injector's whole job is "base is American, twin is
    # British", so running it after --spelling gb would immediately undo the gb
    # base it had just written.
    if a.spelling == "us":
        print("  — canonicalizing the standalone English packs —")
        import subprocess, sys as _sys
        r = subprocess.run([_sys.executable, os.path.join(os.path.dirname(__file__), "inject_english_gb.py")],
                           capture_output=True, text=True)
        print("\n".join("  " + l for l in r.stdout.strip().split("\n") if l.strip()))
        if r.returncode != 0:
            print("  !! inject_english_gb.py failed — the English packs may be missing twins")
            raise SystemExit(1)
    else:
        print("  — skipped inject_english_gb.py (it would flip the base back to US) —")
        print("  !! --spelling gb is a NON-CANONICAL build: Odiin's ruling is a US base with")
        print("     a British twin, and the site's UK/US toggle reads that twin at runtime.")
        print("     The six standalone English packs are untouched and remain US, so the site")
        print("     is now mixed. Re-run without --spelling to put it back.")

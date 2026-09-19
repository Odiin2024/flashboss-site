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

NEITHER ARE THE LOCALE GLOSSES. card() emits no Translation_de/_es/_ja/_zh/_ru
and no ExampleSentence, but five of the files it regenerates now carry ~23,000
of the former and 3,000 of the latter, put there by inject_gloss_fields.py after
English Core/P1/P2 and Latin were added to its mapping (2026-08-31). A bare run
of this script wiped every one of them, silently — the localized word lists just
fell back to English. So this script now runs that injector too, and the order is
load-bearing: inject_english_gb.py first, because it settles the American base
that inject_gloss_fields.py then reads Translation_ru from.

The test that catches a regression here is destructive and worth keeping: run
this script alone on a clean tree and confirm `git status -- data/` is empty.
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
        ("Latin",   "Pareto 1", "Latin/pareto1",              "data/latin/PARETO1_FINAL.json",       1000, "lang"),
        # Swahili Core shipped 2026-09-16 and its own store page promises the word
        # list is on the website; it was not. Pareto 1 and 2 are authored but not
        # released, so they are deliberately not built here.
        ("Swahili", "Core",     "Swahili/core",               "data/swahili/CORE_FINAL.json",        0,    "lang"),
        # The four Roots packs. Rebuilt upstream 2026-09-19 (new clusters, renumbered
        # folders, new lessons, a new Notes line carrying the twin/Related labels), and
        # the site's copies were 2026-08-28 artifacts. mode "roots": the pair is
        # TargetWord <-> definition (knight's ExampleTranslation), and pos/syn/ant are
        # lifted out of Notes here rather than re-parsed in the browser — the word-list
        # page prints them on the printed card's front face and its own Notes fallback
        # cannot see a Notes field the lean view does not carry.
        ("English", "German Roots", "German_Roots/core",        "data/english/gr/CORE_FINAL.json",     0,    "roots"),
        ("English", "Greek Roots",  "Greek_Roots/core",         "data/english/gkr/CORE_FINAL.json",    0,    "roots"),
        ("English", "Norman Roots", "Norman_Roots/core",        "data/english/nr/CORE_FINAL.json",     0,    "roots"),
        ("English", "Latin Roots",  "Latin_Roots/core",         "data/english/lr/CORE_FINAL.json",     0,    "roots"),
        # Adept and Advance are the same shape — TargetWord <-> definition, pos/syn/ant
        # in Notes — so they build in "roots" mode too. Registered 2026-09-21; until then
        # their views were 2026-08-28 hand drops with nothing keeping them in step.
        ("English", "Adept",        "English_Adept/core",       "data/english/ad/CORE_FINAL.json",     0,    "roots"),
        ("English", "Advance",      "English_Advance/core",     "data/english/adv/CORE_FINAL.json",    0,    "roots")]

# Notes shape on a Roots card, one line:
#   "noun | Old English freodom (...). Norman twin: liberty, ... syn: independence | ant: captivity | Related: free"
# The part of speech is everything before the first pipe. "Norman twin:", "Germanic
# twin:", "Latin twin:" and "Related:" are the 2026-09 additions; none is mistaken for a
# pos (anchored at the start) or for syn/ant (anchored to their own label).
#
# "phrasal verb" is two words (188 German Roots cards), so one space is allowed inside.
POS_RE = re.compile(r'^\s*([a-z][a-z/]*(?: [a-z]+)?)\s*\|')

# "syn:" is NOT pipe-anchored — it ends the etymology sentence ("... = sight carried
# from a distance. syn: TV"), while "ant:" and "Related:" do open their own pipe run.
# So match the label wherever it stands and stop at the next pipe. Anchoring syn to a
# pipe cost every synonym in the first run of this builder.
def _labelled(notes, label):
    m = re.search(r'\b' + label + r':\s*([^|]+)', notes)
    return m.group(1).strip().rstrip('.') if m else ""

def ck(p):
    m = re.search(r'cluster(\d+)_(\d+)', os.path.basename(p))
    return (int(m.group(1)), int(m.group(2)))

NAME_LOCALES = ("", "_de", "_es", "_ja", "_zh", "_ru")

def cluster_names(setdir):
    """The authored cluster labels, keyed by folder slug, per locale.

    Every pack in flashcard_sets carries cluster_names.json and a file per
    locale beside it; they are written, translated and checked upstream, and
    until now the site threw them away and humanised the folder slug instead.
    Returns {"": {slug: name}, "_de": {...}, ...} with missing files simply
    absent, so a pack that has only English names still gets them. The
    "_comment" key every one of these files carries is dropped."""
    root = os.path.join(REPO, setdir)
    names = {}
    for loc in NAME_LOCALES:
        f = os.path.join(root, f"cluster_names{loc}.json")
        if not os.path.isfile(f):
            continue
        try:
            d = json.load(open(f, encoding="utf-8"))
        except (ValueError, OSError):
            continue
        names[loc] = {k: v for k, v in d.items()
                      if k != "_comment" and isinstance(v, str) and v.strip()}
    return names

def walk(setdir):
    root = os.path.join(REPO, setdir); out = []
    names = cluster_names(setdir)
    for td in sorted(glob.glob(root + "/tier_*"),
                     key=lambda x: int(re.search(r'tier_(\d+)', x).group(1))):
        for cd in sorted([c for c in glob.glob(td + "/*") if os.path.isdir(c)], key=ck):
            s = os.path.basename(cd); f = os.path.join(cd, s + ".json")
            if os.path.isfile(f):
                t, c = ck(cd)
                out.append({"cluster_id": f"T{t}-C{c}", "tier": t, "slug": s,
                            "names": {loc: m[s] for loc, m in names.items() if s in m},
                            "raw": json.load(open(f, encoding="utf-8"))})
    return out

def roots_card(raw, n):
    """One Roots card: the definition IS the gloss (the immersion ruling), with the
    part of speech and the synonym/antonym runs pulled out of Notes."""
    o = {"n": n, "TargetWord": raw["TargetWord"],
         "definition": raw.get("ExampleTranslation", "")}
    notes = raw.get("Notes", "") or ""
    m = POS_RE.match(notes)
    if m: o["pos"] = m.group(1)
    for k in ("syn", "ant"):
        v = _labelled(notes, k)
        if v: o[k] = v
    if raw.get("TriggerLesson"): o["TriggerLesson"] = raw["TriggerLesson"]
    return o

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
        nm = cl.get("names") or {}
        # "name" is the authored English label; "name_de" … the locale twins.
        # A locale the pack does not carry is simply absent and the page falls
        # back to the English name, then to the humanised slug, exactly as before.
        namebits = "".join(
            f' "name{loc}": {json.dumps(nm[loc], ensure_ascii=False)},'
            for loc in NAME_LOCALES if loc in nm)
        out.append(f'      "cluster_id": {json.dumps(cl["cluster_id"])}, "tier": {cl["tier"]}, '
                   f'"slug": {json.dumps(cl["slug"])},{namebits}')
        out.append('      "cards": [')
        lines = []
        for r in cl["raw"]:
            n += 1
            obj = roots_card(r, n) if mode == "roots" else card(r, n, sp, mode)
            lines.append(json.dumps(obj, ensure_ascii=False))
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
              + (f", {gb} spelling twins" if mode == "eng" else "")
              + (f", {sum(1 for c in cls if c.get('names'))}/{len(cls)} named" ))

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

        # Put back what card() cannot emit. MUST follow inject_english_gb.py:
        # that settles the American base, and inject_gloss_fields.py sources
        # Translation_ru from the card's English Translation.
        print("  — restoring the locale glosses and example sentences —")
        g = subprocess.run([_sys.executable, os.path.join(os.path.dirname(__file__), "inject_gloss_fields.py")],
                           capture_output=True, text=True)
        print("\n".join("  " + l for l in g.stdout.strip().split("\n")[-6:] if l.strip()))
        if g.returncode != 0:
            print("  !! inject_gloss_fields.py failed — the localized word lists have fallen back to English")
            raise SystemExit(1)

        # Field-level assertion. The destructive git test only catches this if
        # someone remembers to run it on a clean tree; this catches it always.
        # Every layer card() cannot emit is checked back into place before the
        # script is allowed to exit 0.
        import json as _json
        EXPECT = [("data/english/core/CORE_FINAL.json", ("de", "es", "ja", "zh"), True),
                  ("data/english/p1/CORE_FINAL.json",   ("de", "es", "ja", "zh"), True),
                  ("data/english/p2/CORE_FINAL.json",   ("de", "es", "ja", "zh"), True),
                  ("data/latin/CORE_FINAL.json",        ("de", "es", "ja"),       False),
                  ("data/latin/PARETO1_FINAL.json",     ("de", "es", "ja"),       False)]
        holes = []
        for rel, locs, wants_example in EXPECT:
            cards = [c for cl in _json.load(open(rel, encoding="utf-8"))["clusters"]
                     for c in cl["cards"]]
            for loc in locs:
                n = sum(1 for c in cards if (c.get("Translation_" + loc) or "").strip())
                if n < len(cards):
                    holes.append(f"{rel}: Translation_{loc} on {n}/{len(cards)}")
            if wants_example:
                n = sum(1 for c in cards if (c.get("ExampleSentence") or "").strip())
                if n < len(cards):
                    holes.append(f"{rel}: ExampleSentence on {n}/{len(cards)}")
        if holes:
            print("  !! a layer did not survive the build:")
            for h in holes:
                print("     " + h)
            raise SystemExit(1)
        print(f"  — verified: every locale gloss and example sentence back in place —")
    else:
        print("  — skipped inject_english_gb.py (it would flip the base back to US) —")
        print("  !! --spelling gb is a NON-CANONICAL build: Odiin's ruling is a US base with")
        print("     a British twin, and the site's UK/US toggle reads that twin at runtime.")
        print("     The six standalone English packs are untouched and remain US, so the site")
        print("     is now mixed. Re-run without --spelling to put it back.")

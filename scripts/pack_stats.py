#!/usr/bin/env python3
"""Measure words-in-context per pack, and check the figures the site states.

The site quotes a floor for each course — "more than 9,000 words of German in
context" — and those floors are only honest while the packs behind them stay
put. They do not: knight's flashcard_sets is edited continuously, and two runs
of this measurement an hour apart on 2026-08-30 differed by six words because
Esperanto Pareto 1 was being rewritten between them.

So the figures are not transcribed, they are checked:

  python3 scripts/pack_stats.py            # measure every pack
  python3 scripts/pack_stats.py --check    # verify every figure the site states

--check exits non-zero if any page now claims a floor the data no longer
supports. Run it before pushing anything that touches a language page, and after
knight lands pack edits.

WHAT IS COUNTED: whitespace-separated tokens of ExampleSentence, with any
"— Caes. BG 5.44.5" source citation stripped first (Latin and Ancient Greek
carry them; nothing else does). Headwords, translations and notes are NOT
counted — this is the target-language text a learner reads in context.
"""
import argparse, glob, json, os, re, sys

KNIGHT = "/home/odiin/Documents/Bootcamp/knight/flashcard_sets"

# course -> the packs that make it up, in order
COURSES = {
    "English":   [("Core", "English/core"), ("Pareto 1", "English_Extensions/pareto1"),
                  ("Pareto 2", "English_Extensions/pareto2")],
    "German":    [("Core", "German/core"), ("Pareto 1", "German_Extensions/pareto1"),
                  ("Pareto 2", "German_Extensions/pareto2")],
    "Spanish":   [("Core", "Spanish/core"), ("Pareto 1", "Spanish_Extensions/pareto1"),
                  ("Pareto 2", "Spanish_Extensions/pareto2")],
    "Italian":   [("Core", "Italian/core"), ("Pareto 1", "Italian_Extensions/pareto1"),
                  ("Pareto 2", "Italian_Extensions/pareto2")],
    "Esperanto": [("Core", "Esperanto/core"), ("Pareto 1", "Esperanto_Extensions/pareto1"),
                  ("Pareto 2", "Esperanto_Extensions/pareto2")],
    "French":    [("Core", "French/core"), ("Pareto 1", "French_Extensions/pareto1"),
                  ("Pareto 2", "French_Extensions/pareto2")],
    "Latin":     [("Core", "Latin/core"), ("Pareto 1", "Latin/pareto1")],
    "Toki Pona": [("Core", "Toki_Pona/core")],
}

# (page, figure, what it counts) — every words-in-context floor the site states.
# "core" = that course's Core pack; "all" = every released pack in the course.
CLAIMS = [
    ("german.html",     9000,  "German",    "core"), ("german.html",    42000, "German",    "all"),
    ("spanish.html",    9000,  "Spanish",   "core"), ("spanish.html",   39000, "Spanish",   "all"),
    ("italian.html",   12000,  "Italian",   "core"), ("italian.html",   48000, "Italian",   "all"),
    ("esperanto.html",  7000,  "Esperanto", "core"), ("esperanto.html", 46000, "Esperanto", "all"),
    ("english.html",    7000,  "English",   "core"),
    ("toki-pona.html",  2800,  "Toki Pona", "core"),
    ("french.html",     7000,  "French",    "core"),
    ("update/latin.html", 17007, "Latin",   "all"),   # exact, not a floor — Latin is frozen
]
EXACT = {("update/latin.html", 17007)}

CITE = re.compile(r"—.*$")

def words(setdir):
    """Target-language words in a pack's example sentences."""
    total = 0
    root = os.path.join(KNIGHT, setdir)
    for f in glob.glob(root + "/tier_*/cluster*/*.json"):
        if not os.path.basename(f).startswith("cluster"):
            continue
        for card in json.load(open(f, encoding="utf-8")):
            total += len(CITE.sub("", card.get("ExampleSentence", "")).strip().split())
    return total

def measure():
    out = {}
    for course, packs in COURSES.items():
        out[course] = {label: words(d) for label, d in packs}
    return out

def report(m):
    print(f"{'course':11}" + "".join(f"{p:>11}" for p in ("Core", "Pareto 1", "Pareto 2")) + f"{'whole':>11}")
    for course, packs in m.items():
        row = "".join(f"{packs.get(p, 0):>11,}" if packs.get(p) else f"{'—':>11}"
                      for p in ("Core", "Pareto 1", "Pareto 2"))
        print(f"{course:11}{row}{sum(packs.values()):>11,}")

def check(m, root="."):
    bad = 0
    for page, figure, course, scope in CLAIMS:
        actual = m[course]["Core"] if scope == "core" else sum(m[course].values())
        path = os.path.join(root, page)
        on_page = f"{figure:,}" in open(path, encoding="utf-8").read() if os.path.exists(path) else False
        if (page, figure) in EXACT:
            ok = actual == figure
            note = f"exact, is {actual:,}"
        else:
            ok = actual > figure
            note = f"actual {actual:,}, headroom {actual - figure:+,}"
        if not on_page:
            print(f"  MISSING  {page:20} {figure:>7,} — not found on the page"); bad += 1
        elif not ok:
            print(f"  STALE    {page:20} {figure:>7,} — {note}"); bad += 1
        else:
            flag = "  (tight)" if not (page, figure) in EXACT and actual - figure < 200 else ""
            print(f"  ok       {page:20} {figure:>7,} — {note}{flag}")
    return bad

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="verify the figures the site states")
    a = ap.parse_args()
    m = measure()
    if a.check:
        here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        n = check(m, here)
        print(f"\n{'all figures hold' if not n else str(n) + ' figure(s) need attention'}")
        sys.exit(1 if n else 0)
    report(m)

#!/usr/bin/env python3
"""Copy lesson files from the game repo into the site's data tree.

The site fetches data/<lang>/tier<N>_lessons<_loc>.json; the game repo keeps
them per tier directory. Only packs the site does not already carry are listed
here — the older language packs were synced before this script existed.

Locale twins are copied when they exist; a missing twin is not an error, the
localized lesson pages fall back to the English file.
"""
import glob, os, re, shutil, sys

REPO = "/home/odiin/Documents/Bootcamp/knight/flashcard_sets"
LOCALES = ("", "_de", "_es", "_ja", "_zh", "_ru", "_gb")   # _gb is the British lesson twin, used by the UK/US toggle
# _ru added 2026-09-19: every foreign pack has carried Russian lesson twins upstream
# for a while, and none of them were being copied, so lessons.ru.html showed the
# English lessons to a Russian reader. It asks for the twin now.

# knight set dir -> site data dir
MAP = [("English/core",               "data/english/core"),
       ("English_Extensions/pareto1", "data/english/p1"),
       ("English_Extensions/pareto2", "data/english/p2"),
       ("Latin/core",                 "data/latin"),
       ("Latin/pareto1",              "data/latin"),
       # Swahili Core (released 2026-09-16). Its 20 lessons carry de/es/ja/ru/zh
       # twins upstream and they are copied with the English ones.
       ("Swahili/core",               "data/swahili"),
       # The six foreign courses. Their lesson files were dropped into data/ by hand
       # in an earlier pass and were never in this map, so nothing refreshed them and
       # none of them ever gained the Russian twin that has existed upstream for a
       # while — lessons.ru.html showed a Russian reader the English lessons. Same
       # naming on both sides (tier<N>_lessons[_loc].json), so they simply join.
       ("German/core",                "data/german"),
       ("German_Extensions/pareto1",  "data/german"),
       ("German_Extensions/pareto2",  "data/german"),
       ("Spanish/core",               "data/spanish"),
       ("Spanish_Extensions/pareto1", "data/spanish"),
       ("Spanish_Extensions/pareto2", "data/spanish"),
       ("Italian/core",               "data/italian"),
       ("Italian_Extensions/pareto1", "data/italian"),
       ("Italian_Extensions/pareto2", "data/italian"),
       ("French/core",                "data/french"),
       ("French_Extensions/pareto1",  "data/french"),
       ("French_Extensions/pareto2",  "data/french"),
       ("Esperanto/core",             "data/esperanto"),
       ("Esperanto_Extensions/pareto1","data/esperanto"),
       ("Esperanto_Extensions/pareto2","data/esperanto"),
       ("Toki_Pona/core",             "data/toki_pona"),
       # The four Roots packs (added 2026-09-19 with the rebuild: new lessons, lesson
       # 000 GETTING STARTED, lessons_mandatory). They ship the English lesson and its
       # _gb twin only — no _de/_es/_ja/_zh, by the Roots immersion ruling, and the
       # localized lesson pages know not to ask for one (lessons.<loc>.html passes
       # LESSON_LOC for foreign packs only).
       ("German_Roots/core",           "data/english/gr"),
       ("Greek_Roots/core",            "data/english/gkr"),
       ("Norman_Roots/core",           "data/english/nr"),
       ("Latin_Roots/core",            "data/english/lr"),
       # Adept and Advance, the other two standalone English packs (added 2026-09-21 so
       # they cannot drift the way the Roots lessons did). Adept ships English + _gb;
       # Advance also carries _de/_es/_ja/_zh lesson twins upstream (the A1/A2
       # bureaucracy guide) and they are copied, though the lessons page does not yet
       # ask for them: it passes LESSON_LOC for foreign packs only.
       ("English_Adept/core",          "data/english/ad"),
       ("English_Advance/core",        "data/english/adv")]

def main():
    total = 0
    for setdir, out in MAP:
        os.makedirs(out, exist_ok=True)
        found = {}
        for f in glob.glob(os.path.join(REPO, setdir, "tier_*", "tier*_lessons*.json")):
            b = os.path.basename(f)
            m = re.match(r'tier(\d+)_lessons(_[a-z]{2})?\.json$', b)
            if not m: continue
            if (m.group(2) or "") not in LOCALES: continue
            found[b] = f
        for b in sorted(found):
            shutil.copy2(found[b], os.path.join(out, b))
        total += len(found)
        tiers = sorted({int(re.match(r'tier(\d+)', b).group(1)) for b in found})
        locs = sorted({(re.match(r'tier\d+_lessons(_[a-z]{2})?', b).group(1) or "base") for b in found})
        print(f"  {setdir:<30} -> {out:<20} {len(found):>3} files  tiers={tiers}  {locs}")
    print(f"\n  {total} lesson files synced")

if __name__ == "__main__":
    sys.exit(main())

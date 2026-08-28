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
LOCALES = ("", "_de", "_es", "_ja", "_zh", "_gb")   # _gb is the British lesson twin, used by the UK/US toggle

# knight set dir -> site data dir
MAP = [("English/core",               "data/english/core"),
       ("English_Extensions/pareto1", "data/english/p1"),
       ("English_Extensions/pareto2", "data/english/p2"),
       ("Latin/core",                 "data/latin"),
       ("Latin/pareto1",              "data/latin")]

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

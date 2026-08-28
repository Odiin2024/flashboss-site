#!/usr/bin/env python3
"""What exists, in which language. Run it any time: python3 scripts/coverage.py

Reads the filesystem — not a list someone has to remember to update — and
cross-checks it against the AVAIL map in lang-redirect.js and each page's
hreflang block, so drift between the three shows up as a warning.
"""
import re, glob, os, sys

LOC = ["en", "de", "es", "ja", "zh", "ru"]

def scan():
    pages = {}
    for f in sorted(glob.glob("*.html")):
        m = re.match(r'^([a-z0-9-]+)(?:\.(de|es|ja|zh|ru))?\.html$', f)
        if m:
            pages.setdefault(m.group(1), set()).add(m.group(2) or "en")
    return pages

def avail_map():
    try:
        s = open("lang-redirect.js", encoding="utf-8").read()
    except OSError:
        return {}
    return {k: set(re.findall(r"'(\w+)'", v))
            for k, v in re.findall(r"'([a-z-]+)':\s*\[([^\]]*)\]", s)}

def hreflangs(fn):
    try:
        return set(re.findall(r'hreflang="([a-z-]+)"', open(fn, encoding="utf-8").read())) - {"x-default"}
    except OSError:
        return set()

def main():
    pages, avail = scan(), avail_map()
    warn = []
    groups = {"COMPLETE (all 6)": [], "PARTIAL": [], "ENGLISH ONLY": []}
    for base, have in sorted(pages.items()):
        g = "COMPLETE (all 6)" if len(have) == 6 else ("ENGLISH ONLY" if have == {"en"} else "PARTIAL")
        groups[g].append((base, have))
        a = avail.get(base)
        if a is not None:
            for l in (have - {"en"}) - a:
                warn.append(f"{base}: {l}.html exists but AVAIL doesn't list it -> no auto-redirect")
            for l in a - have:
                warn.append(f"{base}: AVAIL claims {l} but {base}.{l}.html is missing -> redirect to 404")
        elif len(have) > 1:
            warn.append(f"{base}: localized but absent from the AVAIL map")
        for l in sorted(have):
            fn = f"{base}.html" if l == "en" else f"{base}.{l}.html"
            hl = hreflangs(fn)
            if hl and (have - {"en"}) - hl:
                warn.append(f"{fn}: hreflang missing {sorted((have - {'en'}) - hl)}")

    print("    " + "  ".join(f"{l:>2}" for l in LOC))
    for g, rows in groups.items():
        if not rows:
            continue
        print(f"\n{g}  ({len(rows)})")
        for base, have in rows:
            print(f"  {base:<19} " + "   ".join(("Y" if l in have else "·") for l in LOC))
    print(f"\n{len(pages)} base pages, {sum(len(v) for v in pages.values())} files")
    print("per locale: " + ",  ".join(f"{l}={sum(1 for v in pages.values() if l in v)}" for l in LOC))
    if warn:
        print(f"\n{len(warn)} WARNING(S):")
        for w in warn:
            print("  !", w)
    else:
        print("\nfilesystem, AVAIL map and hreflang blocks all agree.")
    return 0

sys.exit(main())

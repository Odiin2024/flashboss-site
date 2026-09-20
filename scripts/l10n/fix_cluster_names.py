#!/usr/bin/env python3
"""Replace coined cluster names in a strings module with the ones the game ships.

    python3 scripts/l10n/fix_cluster_names.py latin de es ja zh ru

A cluster name is not free prose. The player sees it in the game, and the packs
carry an authoritative translation of every one: `cluster_names_<loc>.json` beside
`cluster_names.json` in each pack directory. A translator working from the page
alone cannot know that, and the first one coined six German names that the game
renders differently — "Die ersten Beweger" for what the game calls
"Die Triebkräfte", "Die Musterrolle" for "Die Stammrolle".

The page writes them as `·`-separated runs, one run per tier, so this walks every
STRINGS value, finds the runs whose English side is entirely shipped cluster
names, and rewrites the translation from the pack files. Anything else is left
exactly as the translator wrote it.

PACKS names the flashcard-set directories a page draws on. Add a page here when
it starts listing cluster names.
"""
import html as H
import importlib.util
import json
import pathlib
import re
import sys

KNIGHT = pathlib.Path.home() / "Documents/Bootcamp/knight/flashcard_sets"
PACKS = {"latin": [("Latin", "core"), ("Latin", "pareto1")],
         # swahili.html lists no cluster names today, but the packs carry them
         # and the extensions live in their own set directory.
         "swahili": [("Swahili", "core"), ("Swahili_Extensions", "pareto1"),
                     ("Swahili_Extensions", "pareto2")]}
SEP = " · "


def shipped(page, loc):
    """{english cluster name: this locale's name}, from the packs themselves."""
    en, tr = {}, {}
    for set_name, pack in PACKS[page]:
        d = KNIGHT / set_name / pack
        base, other = d / "cluster_names.json", d / f"cluster_names_{loc}.json"
        if not base.exists() or not other.exists():
            continue
        for src, into in ((base, en), (other, tr)):
            into.update({k: v for k, v in json.load(open(src, encoding="utf-8")).items()
                         if not k.startswith("_")})
    return {en[k]: tr[k] for k in en if k in tr}


def main():
    page, locs = sys.argv[1], sys.argv[2:]
    for loc in locs:
        f = pathlib.Path(__file__).with_name(f"{page}_{loc}.py")
        if not f.exists():
            print(f"  {loc}: no strings module"); continue
        table = shipped(page, loc)
        if not table:
            print(f"  {loc}: no shipped cluster names for this pack"); continue

        spec = importlib.util.spec_from_file_location("m", f)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

        text = f.read_text(encoding="utf-8")
        runs = changed = 0
        for key, val in m.STRINGS.items():
            parts = [H.unescape(p) for p in key.split(SEP)]
            if len(parts) < 2 or not all(p in table for p in parts):
                continue
            runs += 1
            want = SEP.join(table[p].replace("&", "&amp;") for p in parts)
            if want == val:
                continue
            # rewrite just this value, matching however the module quoted it
            pat = re.compile(r"(\"" + re.escape(key) + r"\"\s*:\s*\n?\s*)([\"'])(?:(?!\2).)*\2",
                             re.S)
            new, n = pat.subn(lambda mm: mm.group(1) + '"' + want + '"', text, count=1)
            if n:
                text, changed = new, changed + 1
            else:
                print(f"    ! could not rewrite: {key[:60]}…")
        if changed:
            f.write_text(text, encoding="utf-8")
        print(f"  {loc}: {runs} cluster-name runs, {changed} rewritten from the packs")


if __name__ == "__main__":
    main()

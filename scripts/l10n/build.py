#!/usr/bin/env python3
"""Build one locale sibling from a strings module.

    python3 scripts/l10n/build.py immersion de

Reads scripts/l10n/<page>_<loc>.py, which must define TITLE, DESCRIPTION and
STRINGS, and writes <page>.<loc>.html next to the English original. Any key in
STRINGS that is not present in the English page is reported as a MISS: that
means the English page moved and the string is stale, not that it is optional.
"""
import importlib.util, sys, pathlib

root = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(root / "scripts"))
import localize_new_pages as L


def load(page, loc):
    p = pathlib.Path(__file__).with_name(f"{page}_{loc}.py")
    spec = importlib.util.spec_from_file_location(f"{page}_{loc}", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    page, loc = sys.argv[1], sys.argv[2]
    m = load(page, loc)
    import os
    os.chdir(root)
    html = L.build(page, loc, m.STRINGS, m.TITLE, m.DESCRIPTION)
    out = root / L.page_name(page, loc)
    out.write_text(html, encoding="utf-8")
    print(f"  wrote {out.name}  ({len(html):,} bytes, {len(m.STRINGS)} strings)")


if __name__ == "__main__":
    main()

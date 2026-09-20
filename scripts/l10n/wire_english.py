#!/usr/bin/env python3
"""Point an English page at the locale siblings that now exist.

    python3 scripts/l10n/wire_english.py immersion latin swahili the-guide in-development

`localize_new_pages.py` builds the siblings and gives each one a full hreflang
block and a full switcher. The ENGLISH original is not rebuilt by anything, so
it keeps whatever it shipped with — for these five pages, an hreflang block of
`en` plus `x-default` and a switcher holding one entry. Until that is fixed the
translations are invisible to a search engine and unreachable from the page.

This script does only that, and only for locales whose file is actually on disk,
so it can be run again after each batch lands. It also keeps
`lang-redirect.js`'s AVAIL map in step — that map is what lets the browser send
a German visitor to the German page, and a page listed there without a real file
would send them to a 404.

Nothing here touches prose.
"""
import re, sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from localize_new_pages import BASE, LOCALES, NATIVE, page_name

ROOT = pathlib.Path(__file__).resolve().parents[2]


def have(base):
    """The locales, in canonical order, whose sibling of this page exists."""
    return [l for l in LOCALES if l != "en" and (ROOT / page_name(base, l)).exists()]


def wire_page(base):
    p = ROOT / f"{base}.html"
    s = p.read_text(encoding="utf-8")
    locs = have(base)
    if not locs:
        print(f"  {base}: no siblings yet, left alone")
        return []

    # ---- hreflang: en, then every sibling, then x-default ----
    rows = [f'<link rel="alternate" hreflang="en" href="{BASE}{page_name(base,"en")}">']
    rows += [f'<link rel="alternate" hreflang="{l}" href="{BASE}{page_name(base,l)}">'
             for l in locs]
    rows += [f'<link rel="alternate" hreflang="x-default" href="{BASE}{page_name(base,"en")}">']
    s, n = re.subn(r'<link rel="alternate" hreflang="en"[^>]*>\n(?:<link rel="alternate"[^>]*>\n)*',
                   "\n".join(rows) + "\n", s, count=1)
    if not n:
        raise SystemExit(f"{base}.html: no hreflang block to replace")

    # ---- the switcher: English current, then every sibling ----
    items = [f'      <li><a href="{page_name(base,"en")}" aria-current="true">English</a></li>']
    items += [f'      <li><a href="{page_name(base,l)}">{NATIVE[l]}</a></li>' for l in locs]
    s, n = re.subn(r'(<ul class="lang-menu" hidden>).*?(</ul>)',
                   lambda m: m.group(1) + "\n" + "\n".join(items) + "\n    " + m.group(2),
                   s, count=1, flags=re.S)
    if not n:
        raise SystemExit(f"{base}.html: no language menu to replace")

    p.write_text(s, encoding="utf-8")
    print(f"  {base}: {len(locs)} siblings wired — {', '.join(locs)}")
    return locs


def wire_redirect(pages):
    """Add each page to AVAIL, listing only the locales that really exist."""
    p = ROOT / "lang-redirect.js"
    s = p.read_text(encoding="utf-8")
    for base, locs in pages.items():
        if not locs:
            continue
        row = "    '%s':%s[%s]," % (base, " " * max(1, 17 - len(base)),
                                   ", ".join(f"'{l}'" for l in locs))
        if re.search(rf"^\s*'{re.escape(base)}':", s, re.M):
            s = re.sub(rf"^\s*'{re.escape(base)}':.*$", row, s, count=1, flags=re.M)
        else:
            # insert before the closing brace of the AVAIL object
            s = re.sub(r"(\n)(\s*\};\n\s*try \{)", r"\n" + row.rstrip(",") + r"\1\2", s, count=1)
    # a trailing comma before the closing brace is legal in modern browsers but
    # the file predates that assumption; normalise it away
    s = re.sub(r",(\s*//[^\n]*)?(\s*\};)", r"\1\2", s, count=1)
    p.write_text(s, encoding="utf-8")


def main():
    bases = sys.argv[1:]
    if not bases:
        raise SystemExit(__doc__)
    print("wiring the English originals:")
    pages = {b: wire_page(b) for b in bases}
    wire_redirect(pages)
    print("lang-redirect.js AVAIL updated")


if __name__ == "__main__":
    main()

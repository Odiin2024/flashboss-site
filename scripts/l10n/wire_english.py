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

With --siblings it also rewires every locale sibling already on disk the same
way (each keeps aria-current on its own entry), which is how a NEW locale
reaches the switchers of the pages that were translated before it (Arabic,
2026-11-02):

    python3 scripts/l10n/wire_english.py --siblings index home about voices

Nothing here touches prose.
"""
import re, sys, pathlib
from collections import OrderedDict

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from localize_new_pages import BASE, LOCALES, NATIVE, page_name, page_url, switch_attrs

ROOT = pathlib.Path(__file__).resolve().parents[2]


def have(base):
    """The locales, in canonical order, whose sibling of this page exists."""
    return [l for l in LOCALES if l != "en" and (ROOT / page_name(base, l)).exists()]


def wire_page(base, cur="en"):
    p = ROOT / page_name(base, cur)
    s = p.read_text(encoding="utf-8")
    locs = have(base)
    if not locs:
        print(f"  {base}: no siblings yet, left alone")
        return []

    # ---- hreflang: en, then every sibling, then x-default ----
    rows = [f'<link rel="alternate" hreflang="{l}" href="{page_url(base,l)}">'
            for l in ["en"] + locs]
    rows += [f'<link rel="alternate" hreflang="x-default" href="{page_url(base,"en")}">']
    s, n = re.subn(r'<link rel="alternate" hreflang="en"[^>]*>\n(?:<link rel="alternate"[^>]*>\n)*',
                   "\n".join(rows) + "\n", s, count=1)
    if not n:
        raise SystemExit(f"{p.name}: no hreflang block to replace")

    # ---- the switcher: English current, then every sibling ----
    items = [f'      <li><a href="{page_name(base,l)}"'
             + (' aria-current="true"' if l == cur else '') + switch_attrs(l) + f'>{NATIVE[l]}</a></li>'
             for l in ["en"] + locs]
    s, n = re.subn(r'(<ul class="lang-menu" hidden>).*?(</ul>)',
                   lambda m: m.group(1) + "\n" + "\n".join(items) + "\n    " + m.group(2),
                   s, count=1, flags=re.S)
    if not n:
        raise SystemExit(f"{p.name}: no language menu to replace")

    p.write_text(s, encoding="utf-8")
    print(f"  {p.name}: {len(locs)} siblings wired — {', '.join(locs)}")
    return locs


def wire_redirect(pages):
    """Rewrite AVAIL so it lists exactly the locales that exist on disk.

    The whole object is re-emitted rather than patched line by line. An earlier
    version inserted each row before the closing brace and stripped the trailing
    comma as it went, which produced three consecutive rows with no comma between
    them -- a syntax error that would have taken the redirect script out
    entirely, silently, for every page on the site.
    """
    p = ROOT / "lang-redirect.js"
    s = p.read_text(encoding="utf-8")
    m = re.search(r"(var AVAIL = \{\n)(.*?)(\n\s*\};)", s, re.S)
    if not m:
        raise SystemExit("lang-redirect.js: no AVAIL object found")

    rows = OrderedDict(re.findall(r"'([A-Za-z0-9_-]+)':\s*\[([^\]]*)\]", m.group(2)))
    for base, locs in pages.items():
        if locs:
            rows[base] = ", ".join(f"'{l}'" for l in locs)

    width = max(len(b) for b in rows) + 3
    body = ",\n".join(f"    {('%r:' % b).replace(chr(34), chr(39)):<{width}} [{v.strip()}]"
                       for b, v in rows.items())
    s = s[:m.start(2)] + body + s[m.end(2):]
    p.write_text(s, encoding="utf-8")
    return list(rows)


def main():
    siblings = "--siblings" in sys.argv
    bases = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not bases:
        raise SystemExit(__doc__)
    print("wiring the English originals:")
    pages = {b: wire_page(b) for b in bases}
    if siblings:
        print("wiring the locale siblings:")
        for b in bases:
            for l in have(b):
                wire_page(b, l)
    listed = wire_redirect(pages)
    print(f"lang-redirect.js AVAIL rewritten: {len(listed)} pages")


if __name__ == "__main__":
    main()

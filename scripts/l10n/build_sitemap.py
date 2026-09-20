#!/usr/bin/env python3
"""Rebuild sitemap.xml so every locale sibling that exists is listed.

    python3 scripts/l10n/build_sitemap.py [--check]

**This does not crawl the directory.** Several pages on disk are deliberately
out of the sitemap — activate-key, beta-key, beta-key-creator, affiliate-apply,
affiliate-metrics, report, phone-layout-test, tiers-and-clusters — and a crawler
would put them all back and get them indexed. So the set of PUBLIC pages is
taken from the sitemap that is already there, and this script only:

  * recomputes each page's locale alternates from the files actually on disk,
  * adds a <url> for every sibling that now exists and was missing,
  * leaves the priority the page already had, and leaves non-root entries
    (the bare directory URL, and everything under manual/) exactly as they were.

So a page becomes public by being added to sitemap.xml by hand, once. After
that this keeps its translations in step.

`--check` reports what would change and writes nothing.
"""
import re, sys, pathlib, datetime
from collections import OrderedDict

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from localize_new_pages import BASE, LOCALES

ROOT = pathlib.Path(__file__).resolve().parents[2]
SITEMAP = ROOT / "sitemap.xml"
# index.html is served at the bare directory URL, which is already in the file as
# its own entry, so listing both would offer a search engine two URLs for one page.
# Only the English one: index.de.html and its siblings have no bare URL of their own
# and stay listed.
SKIP_EN = {"index"}

HEAD = ('<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n')


def split_page(name):
    """'immersion.de.html' -> ('immersion', 'de');  'immersion.html' -> ('immersion','en')"""
    stem = name[:-5]
    bits = stem.rsplit(".", 1)
    if len(bits) == 2 and bits[1] in LOCALES and bits[1] != "en":
        return bits[0], bits[1]
    return stem, "en"


def page_file(base, loc):
    return f"{base}.html" if loc == "en" else f"{base}.{loc}.html"


def parse():
    s = SITEMAP.read_text(encoding="utf-8")
    urls = re.findall(r"  <url>.*?</url>\n", s, re.S)
    root, other = OrderedDict(), []
    for u in urls:
        loc = re.search(r"<loc>([^<]*)</loc>", u).group(1)
        rel = loc.split("flashboss-site/", 1)[1] if "flashboss-site/" in loc else ""
        if not rel.endswith(".html") or "/" in rel:
            other.append(u)                       # the bare directory URL, manual/*
            continue
        pr = re.search(r"<priority>([^<]*)</priority>", u)
        lm = re.search(r"<lastmod>([^<]*)</lastmod>", u)
        base, _ = split_page(rel)
        root.setdefault(base, {"priority": pr.group(1) if pr else "0.5",
                               "lastmod": lm.group(1) if lm else None})
    return root, other


def entry(base, loc, locs, priority, lastmod):
    out = [f"    <loc>{BASE}{page_file(base, loc)}</loc>"]
    for l in sorted(locs):
        out.append(f'    <xhtml:link rel="alternate" hreflang="{l}" '
                   f'href="{BASE}{page_file(base, l)}"/>')
    out.append(f'    <xhtml:link rel="alternate" hreflang="x-default" '
               f'href="{BASE}{page_file(base, "en")}"/>')
    out.append(f"    <lastmod>{lastmod}</lastmod>")
    out.append(f"    <priority>{priority}</priority>")
    return "  <url>\n" + "\n".join(out) + "\n  </url>\n"


def main():
    check = "--check" in sys.argv
    root, other = parse()
    today = datetime.date.today().isoformat()
    body, added = [], []
    for base, meta in root.items():
        locs = [l for l in LOCALES if (ROOT / page_file(base, l)).exists()]
        if "en" not in locs:
            print(f"  ! {base}.html is in the sitemap but not on disk — skipped")
            continue
        for l in locs:
            if l == "en" and base in SKIP_EN:
                continue
            fresh = not re.search(rf"<loc>{re.escape(BASE + page_file(base, l))}</loc>",
                                  SITEMAP.read_text(encoding="utf-8"))
            if fresh:
                added.append(page_file(base, l))
            body.append(entry(base, l, locs,
                              meta["priority"],
                              today if fresh else (meta["lastmod"] or today)))
    out = HEAD + "".join(other) + "".join(body) + "</urlset>\n"
    print(f"  {len(body) + len(other)} urls, {len(added)} new")
    for a in added:
        print(f"    + {a}")
    if check:
        print("  --check: nothing written")
        return
    SITEMAP.write_text(out, encoding="utf-8")


if __name__ == "__main__":
    main()

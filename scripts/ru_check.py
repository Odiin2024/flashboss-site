#!/usr/bin/env python3
"""Verify a .ru.html page: find untranslated English text and broken wiring.

Extracts visible text (and the human-facing attributes: title, alt, aria-label,
placeholder, meta description/og/twitter) and flags any run of Latin letters
that is not an allow-listed brand/technical token.
"""
import re, sys, os, html as _html

ALLOW = {
 # brand + product tokens that stay Latin by canon
 "flashboss","pareto","odiin","steam","windows","mac","linux","dlc",
 "english","advance","adept","core","roots","german","norman","latin","greek",
 "toki","pona","esperanto","x","facebook","reddit","whatsapp","messenger",
 "scientia","est","potentia","die","ehefrau","read","in",
 # words that legitimately appear in Russian copy
 "a1","a2","b1","b2","tts","id","ok","css","html","http","https","utm","ru","en",
 "terminal",                                  # "Windows Terminal" — product name
 "shift","ctrl","enter","alt","tab","esc",    # key names stay Latin on RU keyboards
 "listen","piper","eo",                       # in-game cue, TTS engine, language code
}
SKIP_TAGS = re.compile(r'<(script|style)\b.*?</\1>', re.S | re.I)
COMMENT = re.compile(r'<!--.*?-->', re.S)
ATTRS = re.compile(r'\b(?:alt|aria-label|placeholder|title)="([^"]*)"')
META = re.compile(r'<meta[^>]*(?:name="(?:description|twitter:(?:title|description))"|property="og:(?:title|description)")[^>]*content="([^"]*)"')
TITLE = re.compile(r'<title>(.*?)</title>', re.S)

LANGMENU = re.compile(r'<ul class="lang-menu".*?</ul>', re.S)
URLISH = re.compile(r'https?://\S+|\b[\w.-]+\.(?:html|png|gif|jpg|svg|js|css|pdf)\b')

def visible(s):
    s = SKIP_TAGS.sub(" ", s)
    s = COMMENT.sub(" ", s)
    s = LANGMENU.sub(" ", s)          # Deutsch / Español / 日本語 are meant to be foreign
    chunks = ATTRS.findall(s) + META.findall(s) + TITLE.findall(s)
    body = re.sub(r'<[^>]+>', " ", s)
    out = []
    for c in chunks + [body]:
        c = _html.unescape(c)          # &nbsp; &mdash; &rarr; are not English words
        out.append(URLISH.sub(" ", c))
    return out

def check(fn):
    s = open(fn, encoding="utf-8").read()
    bad = {}
    for chunk in visible(s):
        for w in re.findall(r"[A-Za-z][A-Za-z'’-]{1,}", chunk):
            if w.lower() in ALLOW:
                continue
            bad[w] = bad.get(w, 0) + 1
    problems = []
    base = os.path.basename(fn).split(".")[0]
    if 'lang="ru"' not in s: problems.append("html lang is not ru")
    if 'hreflang="ru"' not in s: problems.append("missing ru hreflang")
    if "Русский" not in s: problems.append("switcher missing Русский")
    if "beta-note" not in s: problems.append("missing beta banner")
    if "lang-redirect.js" in s: problems.append("lang-redirect.js still present")
    for m in re.findall(r'https://store\.steampowered\.com/[^"\']*', s):
        if "l=russian" not in m: problems.append(f"steam link missing l=russian: {m[:70]}")
    # switcher must point at real per-locale files
    menu = re.search(r'<ul class="lang-menu".*?</ul>', s, re.S)
    if menu:
        hrefs = re.findall(r'href="([^"]+)"', menu.group(0))
        if f"{base}.html" not in hrefs:
            problems.append(f"switcher has no English entry ({base}.html)")
    return bad, problems

for fn in sys.argv[1:]:
    bad, problems = check(fn)
    print(f"\n=== {fn} ===")
    for p in problems: print("  WIRING:", p)
    if bad:
        print("  leftover Latin words:", len(bad))
        for w, n in sorted(bad.items(), key=lambda x: -x[1])[:40]:
            print(f"    {n:3d}  {w}")
    if not bad and not problems:
        print("  clean")

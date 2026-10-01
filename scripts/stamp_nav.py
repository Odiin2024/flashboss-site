#!/usr/bin/env python3
"""Stamp the one shared menu into every page that has a site <nav>.

Odiin, 2026-10-01: one menu everywhere — home · packs · word lists · lessons ·
manual · steam — one name per page, Steam always gold. Until then every page had
its own menu (home had no packs or Steam, the Guide had no home, the manual was
"walkthrough (beta)", "walkthrough" and "Playthrough Manual").

What it does, per page:
  * replaces the nav's contents, keeping the page's own language switcher
    (<div class="lang-switch">…</div>) verbatim;
  * keeps the page's own Steam link if its nav had one (a course page sends you to
    its pack), otherwise the base game, tagged website-<page> (+ l= on locales);
  * marks the current section with aria-current (course, Roots, Guide, immersion
    and in-development pages count as "packs");
  * writes one style block between FBNAV markers before </head>. The classes are
    fb-* so no page's older `nav .links` rules (including the phone rules that
    hid them) can reach the new menu.

Idempotent: a second run changes nothing. Re-run after adding a page.

  python3 scripts/stamp_nav.py
"""
import glob, os, re, sys

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCS = ("de", "es", "ja", "zh", "ru")
STEAM_L = {"de": "german", "es": "spanish", "ja": "japanese", "zh": "schinese", "ru": "russian"}

# label per locale, copied from what each locale's pages already called these
LABELS = {
    "":   ["home", "packs", "word lists", "lessons", "manual", "steam"],
    "de": ["Start", "Packs", "Wortlisten", "Lektionen", "Anleitung", "Steam"],
    "es": ["inicio", "paquetes", "vocabulario", "lecciones", "manual", "steam"],
    "ja": ["ホーム", "パック", "単語リスト", "レッスン", "マニュアル", "Steam"],
    "zh": ["主页", "卡包", "单词列表", "课程", "手册", "Steam"],
    "ru": ["главная", "наборы", "списки слов", "уроки", "руководство", "steam"],
}
SECTION = {"home": 0, "packs": 1, "wordlists": 2, "lessons": 3}
UNDER_PACKS = {"english", "esperanto", "french", "german", "italian", "latin", "spanish",
               "swahili", "toki-pona", "the-guide", "german-roots", "greek-roots",
               "latin-roots", "norman-roots", "immersion", "in-development"}
SKIP = {"tiers-and-clusters"}          # its <nav> is a table of contents, not the site menu

CSS = """<!-- FBNAV:start (scripts/stamp_nav.py — edit there, not here) -->
<style>
nav.fbnav{display:flex; align-items:center; gap:10px 22px; flex-wrap:wrap;}
nav.fbnav .fb-logo{color:inherit; text-decoration:none; font-weight:800; letter-spacing:.18em;}
nav.fbnav .fb-links{display:flex; align-items:center; gap:8px 20px; flex-wrap:wrap; margin-left:auto;}
nav.fbnav .fb-links a{color:inherit; text-decoration:none; opacity:.72; font-size:13px; letter-spacing:.04em; white-space:nowrap;}
nav.fbnav .fb-links a:hover{opacity:1;}
nav.fbnav .fb-links a[aria-current]{opacity:1; text-decoration:underline; text-underline-offset:5px;}
nav.fbnav a.fb-steam{opacity:1; text-decoration:none; font-size:13px; letter-spacing:.04em; color:#100d08; background:#e0a93f; padding:4px 11px; border-radius:3px; font-weight:700;}
nav.fbnav a.fb-steam:hover{background:#ecbd5c;}
nav.fbnav .fb-steam-m{display:none;}
nav.fbnav .lang-switch{margin-left:0;}
@media (max-width:700px){
  nav.fbnav .fb-links{order:3; width:100%; margin-left:0; gap:6px 16px;}
  nav.fbnav .fb-links .fb-steam{display:none;}
  nav.fbnav .fb-steam-m{display:inline-block; margin-left:auto;}
}
</style>
<!-- FBNAV:end -->
"""


def page_parts(path):
    name = os.path.basename(path)
    m = re.match(r"(.+?)(?:\.(%s))?\.html$" % "|".join(LOCS), name)
    return m.group(1), (m.group(2) or "")


def stamp(path):
    base, loc = page_parts(path)
    if base in SKIP:
        return None
    s = open(path, encoding="utf-8").read()
    m = re.search(r"<nav(?:\s[^>]*)?>(.*?)</nav>", s, re.S)
    if not m:
        return None
    inner = m.group(1)
    ls = re.search(r'\n?[ \t]*<div class="lang-switch">.*?</ul>\s*</div>', inner, re.S)
    langsw = ls.group(0).strip("\n") if ls else ""
    steam = re.search(r'href="(https://store\.steampowered\.com/[^"]+)"', inner)
    sfx = f".{loc}" if loc else ""
    if steam:
        steam_url = steam.group(1)
    else:
        steam_url = f"https://store.steampowered.com/app/4134440/FlashBoss/?utm_source=website-{base}"
        if loc:
            steam_url += f"&l={STEAM_L[loc]}"
    lab = LABELS[loc]
    targets = [f"home{sfx}.html", f"packs{sfx}.html", f"wordlists{sfx}.html", f"lessons{sfx}.html", "manual/"]
    cur = SECTION.get(base, 1 if base in UNDER_PACKS else None)
    links = []
    for i, (t, l) in enumerate(zip(targets, lab)):
        links.append(f'    <a href="{t}"' + (' aria-current="page"' if i == cur else "") + f">{l}</a>")
    links.append(f'    <a class="fb-steam" href="{steam_url}" target="_blank" rel="noopener">{lab[5]}</a>')
    new_inner = ("\n  <a class=\"fb-logo\" href=\"index%s.html\">FLASHBOSS</a>\n  <span class=\"fb-links\">\n%s\n  </span>\n"
                 % (sfx, "\n".join(links)))
    # phones: Steam sits up top beside the language switch, the five links wrap below
    new_inner += (f'  <a class="fb-steam fb-steam-m" href="{steam_url}" target="_blank" rel="noopener">{lab[5]}</a>\n')
    if langsw:
        new_inner += "  " + langsw.strip() + "\n"
    open_tag = re.match(r"<nav(?:\s[^>]*)?>", m.group(0)).group(0)
    if 'class="' in open_tag:
        if "fbnav" not in open_tag:
            open_tag = open_tag.replace('class="', 'class="fbnav ', 1)
    else:
        open_tag = open_tag[:-1] + ' class="fbnav">'
    s2 = s[:m.start()] + open_tag + new_inner + "</nav>" + s[m.end():]
    s2 = re.sub(r"<!-- FBNAV:start.*?<!-- FBNAV:end -->\n", "", s2, flags=re.S)
    s2 = s2.replace("</head>", CSS + "</head>", 1)
    if s2 != s:
        open(path, "w", encoding="utf-8").write(s2)
        return True
    return False


if __name__ == "__main__":
    changed = skipped = 0
    for p in sorted(glob.glob(os.path.join(SITE, "*.html"))):
        r = stamp(p)
        if r is None:
            skipped += 1
        elif r:
            changed += 1
    print(f"stamped {changed} pages ({skipped} without a site nav left alone)")

#!/usr/bin/env python3
"""Put one gold "Get it on Steam" button first in every landing-page hero.

Odiin, 2026-10-01: a newcomer should learn what FlashBoss is and where to get it in
the first five seconds. The course pages' heroes offered Word Lists / Lessons /
Demo and no Steam at all; home had Steam fourth of four equal buttons. No prices
(Odiin's ruling), so the button carries none.

For every page whose hero has <div class="actions…">: any Steam button already in
it is removed, and the gold one goes first, pointing where the page's menu Steam
button points (a course page's own pack; run stamp_nav.py first). Styles live in
one marked block. Idempotent.

  python3 scripts/stamp_hero_steam.py
"""
import glob, os, re

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCS = ("de", "es", "ja", "zh", "ru")
LABEL = {"": "Get it on Steam", "de": "Jetzt auf Steam", "es": "Consíguelo en Steam",
         "ja": "Steamで入手", "zh": "在 Steam 获取", "ru": "Получить в Steam"}
CSS = """<!-- HEROSTEAM:start (scripts/stamp_hero_steam.py) -->
<style>
.actions a.btn-steam{background:#e0a93f; color:#100d08; border-color:#e0a93f; font-weight:800;}
.actions a.btn-steam:hover{background:#ecbd5c; border-color:#ecbd5c; color:#100d08;}
.hero .actions a.btn-steam{grid-column:1/-1;}  /* grid heroes (home): the whole first row, so the label is never clipped */
</style>
<!-- HEROSTEAM:end -->
"""


def run(path):
    name = os.path.basename(path)
    m = re.match(r"(.+?)(?:\.(%s))?\.html$" % "|".join(LOCS), name)
    loc = m.group(2) or ""
    s = open(path, encoding="utf-8").read()
    hero = re.search(r'<(header|section)[^>]*class="[^"]*\bhero\b[^"]*"[^>]*>.*?</\1>', s, re.S)
    if not hero:
        return None
    h = hero.group(0)
    act = re.search(r'(<div class="actions[^"]*">)(.*?)(\n?\s*</div>)', h, re.S)
    if not act:
        return None
    steam = re.search(r'<a class="fb-steam" href="([^"]+)"', s)
    if not steam:
        return None
    body = act.group(2)
    body = re.sub(r'\s*<a class="btn btn-steam"[^>]*>.*?</a>', "", body, flags=re.S)
    body = re.sub(r'\s*<a class="btn(?: warm)?" href="https://store\.steampowered\.com/[^"]*"[^>]*>.*?</a>', "", body, flags=re.S)
    indent = re.match(r"\s*", act.group(2)).group(0) or "\n      "
    btn = f'{indent}<a class="btn btn-steam" href="{steam.group(1)}" target="_blank" rel="noopener">{LABEL[loc]}</a>'
    h2 = h[:act.start()] + act.group(1) + btn + body + act.group(3) + h[act.end():]
    s2 = s[:hero.start()] + h2 + s[hero.end():]
    s2 = re.sub(r"<!-- HEROSTEAM:start.*?<!-- HEROSTEAM:end -->\n", "", s2, flags=re.S)
    s2 = s2.replace("</head>", CSS + "</head>", 1)
    if s2 != s:
        open(path, "w", encoding="utf-8").write(s2)
        return True
    return False


if __name__ == "__main__":
    done = []
    for p in sorted(glob.glob(os.path.join(SITE, "*.html"))):
        if run(p):
            done.append(os.path.basename(p))
    print(f"{len(done)} heroes:", " ".join(sorted({re.sub(r'\.(de|es|ja|zh|ru)\.html$|\.html$', '', d) for d in done})))

#!/usr/bin/env python3
"""
localize_voices.py — build voices.{de,es,ja,zh}.html from voices.html.

English is the single source. Translations live in data/voices_i18n.json, one
entry per translatable block; the English page keeps every such block on ONE
line so the match can be exact rather than fuzzy. If a unit's 'en' string is not
found, the script says so and writes nothing — a silently skipped sentence would
ship an English line into a German page and nobody would notice for weeks.

    python3 scripts/localize_voices.py            # all locales
    python3 scripts/localize_voices.py de ja      # just these

Re-run it after every edit to voices.html. Anything you change only in a locale
file will be overwritten.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "voices.html")
I18N = os.path.join(ROOT, "data", "voices_i18n.json")

# Pages that have locale siblings. manual/ is English-only and stays as it is.
LOCAL_PAGES = ("index", "home", "packs", "about", "resources")

LANG_SWITCH = """<div class="lang-switch">
    <button class="lang-toggle" type="button" aria-haspopup="true" aria-expanded="false" aria-label="{choose}">{code}<span class="lang-caret">▾</span></button>
    <ul class="lang-menu" hidden>
      <li><a href="voices.html"{cur_en}>English</a></li>
      <li><a href="voices.de.html"{cur_de}>Deutsch</a></li>
      <li><a href="voices.es.html"{cur_es}>Español</a></li>
      <li><a href="voices.ja.html"{cur_ja}>日本語</a></li>
      <li><a href="voices.zh.html"{cur_zh}>简体中文</a></li>
    </ul>
  </div>"""


def build(locale, cfg, units, src):
    out = src
    misses = []

    # 1. the language switcher is rebuilt whole, so link rewriting below can
    #    never touch the one place that must point at every locale at once.
    switch = re.search(r'<div class="lang-switch">.*?</div>', out, re.S)
    if not switch:
        return None, ["lang-switch block not found"]
    cur = {f"cur_{k}": (' aria-current="true"' if k == locale else "")
           for k in ("en", "de", "es", "ja", "zh")}
    out = out.replace(switch.group(0), "@LANGSWITCH@")

    # 2. translated blocks
    for unit in units:
        en = unit["en"]
        if en not in out:
            misses.append(en[:70])
            continue
        out = out.replace(en, unit[locale])

    # 3. head
    out = out.replace('<html lang="en">', f'<html lang="{locale}">', 1)
    out = re.sub(r"<title>.*?</title>", f"<title>{cfg['title']}</title>", out, count=1, flags=re.S)
    out = re.sub(r'(<meta name="description" content=")[^"]*(">)',
                 lambda m: m.group(1) + cfg["description"] + m.group(2), out, count=1)
    # only the English pages carry the redirect script
    out = out.replace('<script src="lang-redirect.js"></script>\n', "")

    # 4. internal links to pages that have siblings
    for page in LOCAL_PAGES:
        out = out.replace(f'href="{page}.html"', f'href="{page}.{locale}.html"')

    # 5. Steam links keep their per-locale campaign tag and interface language
    out = out.replace("utm_source=website-voices", f"utm_source={cfg['steam_utm']}")

    out = out.replace("@LANGSWITCH@",
                      LANG_SWITCH.format(choose=cfg["choose_language"],
                                         code=cfg["code"], **cur))
    return out, misses


def main():
    data = json.load(open(I18N, encoding="utf-8"))
    src = open(SRC, encoding="utf-8").read()
    wanted = sys.argv[1:] or list(data["locales"])
    failed = False
    for locale in wanted:
        cfg = data["locales"].get(locale)
        if not cfg:
            print(f"{locale}: no such locale in voices_i18n.json")
            failed = True
            continue
        out, misses = build(locale, cfg, data["units"], src)
        if misses:
            failed = True
            print(f"{locale}: NOT WRITTEN — {len(misses)} source string(s) not found:")
            for m in misses:
                print(f"    {m}…")
            continue
        path = os.path.join(ROOT, f"voices.{locale}.html")
        open(path, "w", encoding="utf-8").write(out)
        left = len(re.findall(r"[A-Za-z]{4,}", out))
        print(f"{locale}: wrote {os.path.basename(path)}  "
              f"({len(data['units'])} blocks translated)")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()

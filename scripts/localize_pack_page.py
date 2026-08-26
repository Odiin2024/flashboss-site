#!/usr/bin/env python3
"""Apply FlashBoss localization conventions to pack/landing pages.

Run this on freshly-translated localized pages (or any page) and it will,
idempotently:
  1. turn the hero action row into the 3-up grid that holds one line in
     portrait, and ensure a "try the demo" button exists;
  2. set the demo button's label to the page's language (Demo testen /
     Probar demo / デモを試す / Try the demo);
  3. drop the ` →` arrows from the hero buttons;
  4. shorten the long Spanish "Listas de vocabulario" label to "Vocabulario";
  5. give every store.steampowered.com link the right ?l=<lang> param
     (added if missing, corrected if a wrong locale was copied in),
     preserving any existing ?utm_source=.

Locale is taken from the filename: *.de.html -> german, *.es.html -> spanish,
*.ja.html -> japanese, anything else -> English (no l= added).

Usage:
    python3 scripts/localize_pack_page.py german-roots.de.html norman-roots.de.html
    python3 scripts/localize_pack_page.py *.de.html      # sweep a whole locale

Safe to re-run; a page already in the target shape reports "no change".
A page with no hero ".actions reveal" block (e.g. home, about) just gets the
?l= sweep — pass those too and only their Steam links change.
"""
import re, sys

DEMO_URL = "https://flashboss-demo.pages.dev/"
DEMO_LABEL = {"en": "Try the demo", "de": "Demo testen", "es": "Probar demo", "ja": "デモを試す", "zh": "试玩演示"}
STEAM_LANG = {"de": "german", "es": "spanish", "ja": "japanese", "zh": "schinese"}

def lang_of(fn):
    for suf, code in (("de", "de"), ("es", "es"), ("ja", "ja"), ("zh", "zh")):
        if fn.endswith(f".{suf}.html"):
            return code
    return "en"

# ---- hero action row: flex 2-up -> grid 3-up that never wraps ----
_css_container = re.compile(r'\.hero \.actions\{display:flex;[^}]*\}')
_css_btn = re.compile(r'\.hero \.actions \.btn\{[^}]*\}')

def fix_css(s):
    def repl(m):
        mt = re.search(r'margin-top:(\d+)px', m.group(0))
        return (".hero .actions{display:grid; grid-template-columns:repeat(3,1fr); "
                f"gap:9px; margin-top:{mt.group(1) if mt else '40'}px; max-width:520px;}}")
    s, n = _css_container.subn(repl, s, count=1)
    if not n:
        return s   # not a flex 2-up row (e.g. home is already grid) — leave CSS alone
    return _css_btn.sub(
        ".hero .actions .btn{margin-top:0; width:100%; padding:13px 6px; text-align:center; "
        "font-size:clamp(11px,3.2vw,14px); letter-spacing:.01em; white-space:nowrap;}",
        s, count=1)

# ---- the hero buttons ----
_block = re.compile(r'(<div class="actions reveal">)(.*?)(</div>)', re.S)
_demo_label = re.compile(r'(href="' + re.escape(DEMO_URL) + r'">)[^<]*(</a>)')

def fix_actions(s, lang):
    label = DEMO_LABEL[lang]
    def repl(m):
        head, body, tail = m.groups()
        body = body.replace(" &rarr;", "")
        if lang == "es":
            body = body.replace("Listas de vocabulario", "Vocabulario")
            body = body.replace("Lista de vocabulario", "Vocabulario")
        if DEMO_URL in body:                       # already has it — just fix the label
            body = _demo_label.sub(r"\1" + label + r"\2", body)
        elif ("wordlists" in body and "lessons" in body
              and "steampowered" not in body and body.count("<a ") == 2):
            i = body.rfind("</a>")               # genuine 2-up pack row — add the demo button
            nl = body.find("\n", i)
            line = f'        <a class="btn" href="{DEMO_URL}">{label}</a>\n'
            body = body[:nl + 1] + line + body[nl + 1:]
        # otherwise (e.g. home's word-lists/lessons/steam row) leave the buttons alone
        return head + body + tail
    return _block.sub(repl, s, count=1)

# ---- Steam ?l=<lang> ----
_steam = re.compile(r'https://store\.steampowered\.com/[^"\'\s]+')

def fix_steam(s, lang):
    if lang == "en":
        return s
    code = STEAM_LANG[lang]
    def repl(m):
        url = m.group(0)
        if re.search(r'[?&]l=[a-z]+', url):                       # correct a wrong/old one
            return re.sub(r'([?&])l=[a-z]+', r'\1l=' + code, url)
        return url + ("&" if "?" in url else "?") + "l=" + code   # or append
    return _steam.sub(repl, s)

def main(paths):
    if not paths:
        print(__doc__); return 1
    for fn in paths:
        with open(fn, encoding="utf-8") as f:
            before = f.read()
        lang = lang_of(fn)
        after = fix_steam(fix_actions(fix_css(before), lang), lang)
        if after == before:
            print(f"  ok (no change)  {fn}  [{lang}]")
            continue
        with open(fn, "w", encoding="utf-8") as f:
            f.write(after)
        print(f"  PATCHED         {fn}  [{lang}]")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

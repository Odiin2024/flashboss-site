#!/usr/bin/env python3
"""Build a locale sibling of one of the new English-only pages.

The translator fleet does prose for the established pages; these five pages
(immersion, latin, swahili, the-guide, in-development) were written after the
last batch and had no siblings at all. Odiin, 2026-09-20: *"I want this done by
opus with a good understanding of what's canon. it will be good enough for right
now. flag all translations we make ourselves for consideration by a
translation/adversarial pass another day."*

So: the prose here is MINE, not a translator's, and every page this builds
carries the beta-translation notice the Russian pages already established — in
its own language — so a reader knows, and so the next pass can find them.

WHAT IS MECHANICAL (this file owns it):
  * <html lang>, the canonical, the absolute hreflang block for all six
  * the language switcher <ul>, with aria-current on the page's own locale
  * the beta-translation notice and its styling
  * a head comment recording that the prose is self-made

WHAT IS NOT (the caller's STRINGS map owns it):
  * every word of prose, longest-first so a short string cannot eat a long one

CANON, and it is not negotiable:
  * pack names stay English in every locale — English Advance, German Roots,
    Norman Roots, English Adept, Latin Roots, Greek Roots — per
    LOCALIZATION_CANON and the bundle paste sheets
  * FlashBoss stays Latin everywhere
  * NUMBERS ARE NEVER RETRANSLATED, only reformatted to the locale's own
    separator, the way the existing sibling pages already write them
  * banned on these surfaces: any hours figure, any CEFR code, any price
"""
import re, sys, pathlib

BASE = "https://odiin2024.github.io/flashboss-site/"
LOCALES = ["en", "de", "es", "ja", "zh", "ru", "ar"]
NATIVE = {"en": "English", "de": "Deutsch", "es": "Español",
          "ja": "日本語", "zh": "简体中文", "ru": "Русский", "ar": "العربية"}
# Right-to-left locales: <html dir="rtl">, an Arabic-capable font and the RTL
# overrides below. Odiin 2026-11-01: Arabic is a fully supported site language.
RTL = {"ar"}

# The beta-translation notice, in each language, matching the Russian original's
# wording and its markup exactly (see home.ru.html).
BETA = {
 "de": '<b>BETA-ÜBERSETZUNG</b> — die deutsche Fassung dieser Seite ist ein Entwurf und noch nicht lektoriert. Einen Fehler im Text gefunden? <a href="report.html">Sag uns Bescheid</a> · <a href="{en}">Read in English</a>',
 "es": '<b>TRADUCCIÓN BETA</b> — la versión en español de esta página es un borrador y aún no ha pasado revisión. ¿Encontraste un error en el texto? <a href="report.html">Avísanos</a> · <a href="{en}">Read in English</a>',
 "ja": '<b>ベータ翻訳</b> — このページの日本語版は下書きで、まだ校正を経ていません。文章の誤りを見つけたら <a href="report.html">お知らせください</a> · <a href="{en}">Read in English</a>',
 "zh": '<b>测试版翻译</b> — 本页的简体中文版仍是草稿，尚未经过校对。发现文字错误？ <a href="report.html">告诉我们</a> · <a href="{en}">Read in English</a>',
 "ru": '<b>БЕТА-ПЕРЕВОД</b> — русская версия этой страницы черновая и ещё не прошла редактуру. Нашли ошибку в тексте? <a href="report.html">Сообщите нам</a> · <a href="{en}">Read in English</a>',
 # Arabic also says where its interface lives: the FlashBoss window only, never
 # the terminal version (which cannot draw right-to-left text).
 "ar": '<b>ترجمة تجريبية</b> — النسخة العربية من هذه الصفحة مسودة لم تخضع للمراجعة بعد. وجود خطأ في النص؟ <a href="report.html">يسعدنا الإبلاغ عنه</a> · <a href="{en}">Read in English</a><br>الواجهة العربية تعمل في نافذة FlashBoss الجديدة فقط، لا في إصدار الطرفية.',
}
# How each locale writes a thousand, read off the sibling pages that already
# exist rather than assumed: de/es "1.000", ja/zh "1,000", ru "1000" (67 plain
# occurrences across the Russian pages against 3 stray comma forms). NOTHING IS
# RECOUNTED — this only reshapes a separator the English page already wrote.
THOUSANDS = {"en": ",", "de": ".", "es": ".", "ja": ",", "zh": ",", "ru": "", "ar": ","}  # ar: ASCII digits, 3,000 (house rule)

# The language button's accessible name, lifted from the home page of each
# locale so the new pages say what the established ones already say.
# The <html lang> attribute is not always the locale code. The site writes
# zh-Hans, the script subtag, on 18 pages against 4 stragglers that write plain
# zh; the FILE NAME and the hreflang stay "zh" either way.
HTML_LANG = {"en": "en", "de": "de", "es": "es", "ja": "ja", "zh": "zh-Hans", "ru": "ru", "ar": "ar"}

SWITCH_LABEL = {"en": "Choose language", "de": "Sprache wählen", "es": "Elegir idioma",
                "ja": "言語を選択", "zh": "选择语言", "ru": "Выбрать язык", "ar": "اختيار اللغة"}
# Steam's own l= value per locale, so a store link opens in the reader's language
# (the same map scripts/stamp_nav.py uses for the menu's Steam button).
STEAM_L = {"de": "german", "es": "spanish", "ja": "japanese", "zh": "schinese",
           "ru": "russian", "ar": "arabic"}


def assets(s, loc):
    """Point image and GIF references at the locale's own file where one exists.

    The boss-fight GIFs are shot per interface language, so immersion.de.html
    must show the German fight, not the English one. Anything without a sibling
    on disk is left exactly as it is.
    """
    def swap(m):
        attr, stem, ext = m.group(1), m.group(2), m.group(3)
        cand = f"{stem}.{loc}.{ext}"
        return f'{attr}="{cand}"' if pathlib.Path(cand).exists() else m.group(0)
    return re.sub(r'\b(src|data-gif|poster|content)="([A-Za-z0-9_-]+)\.(png|jpg|gif|webp|svg)"',
                  swap, s)


def numerals(s, loc):
    """Reformat English thousands separators for the locale.

    TEXT NODES ONLY. An earlier version worked on whole markup spans and turned
    the JetBrains Mono request into `wght@0.400;0.500;…`, which is not a font
    axis list any more — so a tag is never touched, only what sits between tags,
    and never inside <style> or <script>.
    """
    sep = THOUSANDS[loc]
    if sep == ",":
        return s
    sub = lambda t: re.sub(r"\b(\d{1,3}),(\d{3})\b",
                           lambda m: m.group(1) + sep + m.group(2), t)
    out = []
    # first hold the code blocks aside whole, then walk the rest tag by tag
    for i, block in enumerate(re.split(r"(<style\b.*?</style>|<script\b.*?</script>)",
                                       s, flags=re.S | re.I)):
        if i % 2:
            out.append(block)
            continue
        out.append("".join(part if j % 2 else sub(part)
                           for j, part in enumerate(re.split(r"(<[^>]*>)", block))))
    return "".join(out)


def links(s, loc):
    """Point internal links at the locale's own sibling where one exists.

    Caught by the Swahili translator, 2026-09-20: swahili.de.html was sending a
    German reader to lessons.html and wordlists.html in English, because an href
    is an attribute and the prose pass never touches attributes. The
    fleet-translated pages have always pointed at their own locale, so this is
    the new pages being out of step, not a new policy.

    Query strings and fragments are carried through untouched — the word-list
    and lesson pages are driven by ?lang= and ?set=. A page with no sibling on
    disk is left alone, so this is safe to run before every sibling exists.
    """
    def swap(m):
        base, rest = m.group(1), m.group(2)
        cand = f"{base}.{loc}.html"
        return f'href="{cand}{rest}"' if pathlib.Path(cand).exists() else m.group(0)
    return re.sub(r'href="([A-Za-z0-9_-]+)\.html([^"]*)"', swap, s)


def steam_lang(s, loc):
    """Tag every Steam store link with the locale's l=, keeping utm_source."""
    l = STEAM_L.get(loc)
    if not l:
        return s
    def repl(m):
        url = re.sub(r'([?&])l=[a-z]+&?', r'\1', m.group(0)).rstrip("?&")
        return url + ("&" if "?" in url else "?") + "l=" + l
    return re.sub(r'https://store\.steampowered\.com/[^"\'\s]*', repl, s)


# Arabic-capable face for RTL pages: the site's Latin faces stay first (JetBrains
# Mono / Inter carry the Latin, the brand and the digits), Noto Kufi Arabic takes
# every Arabic glyph by per-glyph fallback.
RTL_FONT = ('<link href="https://fonts.googleapis.com/css2?family=Noto+Kufi+Arabic:'
            'wght@400;500;700;800&display=swap" rel="stylesheet">')

# Shared RTL overrides, written as html[dir="rtl"] rules so they outrank the page
# and FBNAV blocks whatever order stamp_nav.py leaves them in, and so no other
# locale can ever match them. Page-specific mirroring lives in the strings module
# (RTL_CSS) next to the prose.
RTL_CSS = """html[dir="rtl"]{--mono:'JetBrains Mono','Noto Kufi Arabic',ui-monospace,'SF Mono',Menlo,Consolas,monospace; --sans:'Inter','Noto Kufi Arabic',-apple-system,BlinkMacSystemFont,sans-serif;}
/* Arabic is cursive: tracking pulls the joined letters apart; and there is no true Arabic italic */
html[dir="rtl"] body *:not(.fb-logo){letter-spacing:0 !important;}
html[dir="rtl"] :is(em,i,cite,figcaption,.gloss){font-style:normal;}
html[dir="rtl"] .beta-note{font-family:'Noto Kufi Arabic',system-ui,sans-serif;}
/* the shared menu (scripts/stamp_nav.py): links push to the far (left) side, dropdown opens inward */
html[dir="rtl"] nav.fbnav .fb-links{margin-left:0; margin-right:auto;}
html[dir="rtl"] nav .lang-switch{margin-left:0;}
html[dir="rtl"] .lang-menu{right:auto; left:0;}
@media (max-width:700px){
  html[dir="rtl"] nav.fbnav .fb-links{margin-right:0;}
  html[dir="rtl"] nav.fbnav .fb-steam-m{margin-left:0; margin-right:auto;}
}
"""


BETA_CSS = (".beta-note{background:#1b1508; border-bottom:1px solid #6b5a2a; color:#e8d9b0; "
            "font:500 12.5px/1.55 system-ui,-apple-system,'Segoe UI',Roboto,sans-serif; "
            "text-align:center; padding:9px 16px; margin:0;}\n"
            ".beta-note b{color:#e0a93f; font-weight:700; letter-spacing:.09em;}\n"
            ".beta-note a{color:#e0a93f; text-decoration:underline; text-underline-offset:2px;}\n")


def page_name(base, loc):
    return f"{base}.html" if loc == "en" else f"{base}.{loc}.html"


def switch_attrs(l):
    """A right-to-left language name in the switcher carries its own lang/dir."""
    return f' lang="{l}" dir="rtl"' if l in RTL else ""


def page_url(base, loc):
    """Absolute URL. English index.html is served, and declared everywhere, as the bare directory."""
    return BASE if (base == "index" and loc == "en") else BASE + page_name(base, loc)


def build(base, loc, strings, title, description, rtl_css=""):
    """Return the finished HTML for <base>.<loc>.html."""
    src = open(f"{base}.html", encoding="utf-8").read()
    s = src

    # ---- prose, longest first so a short key cannot eat part of a long one ----
    for en in sorted(strings, key=len, reverse=True):
        tr = strings[en]
        if tr is None or tr == en:
            continue
        if en not in s:
            print(f"    MISS [{loc}] {en[:70]}")
            continue
        s = s.replace(en, tr)

    # ---- assets: the locale's own gif/poster where one has been shot ----
    s = assets(s, loc)

    # ---- internal links: this locale's sibling where one exists ----
    s = links(s, loc)

    # ---- lang-redirect.js belongs to the English pages only ----
    s = re.sub(r'<script src="lang-redirect\.js"></script>\n?', '', s)

    # ---- Steam: the store in the reader's language ----
    s = steam_lang(s, loc)

    # ---- numerals: the page's own numbers, this locale's separator ----
    s = numerals(s, loc)

    # ---- head: lang, title, description, canonical, hreflang ----
    s = s.replace('<html lang="en">', f'<html lang="{HTML_LANG[loc]}"'
                  + (' dir="rtl"' if loc in RTL else '') + '>', 1)
    s = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", s, count=1, flags=re.S)
    s = re.sub(r'(<meta name="description" content=")[^"]*(">)',
               lambda m: m.group(1) + description + m.group(2), s, count=1)
    s = re.sub(r'(<meta property="og:url" content=")[^"]*(">)',
               lambda m: m.group(1) + BASE + page_name(base, loc) + m.group(2), s, count=1)
    s = re.sub(r'<link rel="canonical" href="[^"]*">',
               f'<link rel="canonical" href="{BASE}{page_name(base, loc)}">', s, count=1)
    # only locales whose page exists (plus this one): a newly added locale must not
    # send readers of every other page to a 404
    present = [l for l in LOCALES if l in ("en", loc) or pathlib.Path(page_name(base, l)).exists()]
    alts = "\n".join(
        f'<link rel="alternate" hreflang="{l}" href="{page_url(base, l)}">'
        for l in present)
    alts += f'\n<link rel="alternate" hreflang="x-default" href="{page_url(base, "en")}">'
    s = re.sub(r'<link rel="alternate" hreflang="en"[^>]*>\n(?:<link rel="alternate"[^>]*>\n)*',
               alts + "\n", s, count=1)

    # ---- the switcher ----
    items = "\n".join(
        f'      <li><a href="{page_name(base, l)}"'
        + (' aria-current="true"' if l == loc else "") + switch_attrs(l)
        + f'>{NATIVE[l]}</a></li>' for l in present)
    s = re.sub(r'(<ul class="lang-menu" hidden>).*?(</ul>)',
               lambda m: m.group(1) + "\n" + items + "\n    " + m.group(2),
               s, count=1, flags=re.S)
    s = s.replace('aria-label="Choose language"', f'aria-label="{SWITCH_LABEL[loc]}"')
    s = re.sub(r'(aria-label="[^"]*">)[A-Z]{2}<span class="lang-caret">',
               lambda m: m.group(1) + loc.upper() + '<span class="lang-caret">', s, count=1)

    # ---- the beta notice, and the style it needs ----
    s = s.replace("</style>", BETA_CSS + "</style>", 1)
    note = BETA[loc].format(en=page_name(base, "en"))
    s = s.replace("<body>", f'<body>\n<div class="beta-note" role="status">{note}</div>', 1)

    # ---- say in the file that the prose is self-made ----
    s = s.replace("<title>", (
        "<!-- SELF-TRANSLATED, %s. The prose on this page was written by Claude\n"
        "     (Opus), not by the translation fleet, on Odiin's word of 2026-09-20:\n"
        "     good enough for now, and flagged for a translation/adversarial pass\n"
        "     another day. The page carries the beta-translation notice so a reader\n"
        "     knows and so that pass can find it.\n"
        "     Canon held here: the six pack names stay English, FlashBoss stays\n"
        "     Latin, and every number is the English page's number in this locale's\n"
        "     separator — nothing was recounted. -->\n<title>") % loc, 1)
    if loc == "ar":
        s = s.replace("on Odiin's word of 2026-09-20:", "on Odiin's word of 2026-11-01\n     (Arabic is a fully supported site language):", 1)

    # ---- right-to-left: direction, an Arabic face, the mirrored layout ----
    if loc in RTL:
        s = re.sub(r'(<link href="https://fonts\.googleapis\.com/css2\?[^"]*" rel="stylesheet">)',
                   lambda m: m.group(1) + "\n" + RTL_FONT, s, count=1)
        # before the FBNAV block when there is one: stamp_nav.py re-appends that block just
        # before </head>, so this order is the one a re-stamp leaves (the build stays idempotent)
        block = '<style id="fb-rtl">\n' + RTL_CSS + rtl_css + "</style>\n"
        at = s.find("<!-- FBNAV:start")
        s = s[:at] + block + s[at:] if at != -1 else s.replace("</head>", block + "</head>", 1)
    return s

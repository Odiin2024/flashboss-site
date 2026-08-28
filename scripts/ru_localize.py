#!/usr/bin/env python3
"""Mechanical Russian localization for FlashBoss site pages.

Prose is NOT translated here — that lives in update/ru/<base>.strings.tsv
(tab-separated en<TAB>ru), applied longest-first so short strings never
clobber longer ones that contain them.

This script owns the wiring, idempotently:
  1. <html lang>, canonical + og:url -> the .ru.html URL
  2. hreflang block gains a ru line (added to EVERY sibling locale too)
  3. language switcher gains a Русский entry (ditto), aria-current on ru
  4. internal links -> .ru.html, but ONLY for pages that have a ru file
     (RU_PAGES); every other link honestly stays English
  5. Steam links get &l=russian, preserving utm_source
  6. drops lang-redirect.js (English-only script)
  7. injects the beta banner

Usage:
    python3 scripts/ru_localize.py build index home wordlists lessons english
    python3 scripts/ru_localize.py wire          # siblings: hreflang+switcher
"""
import re, sys, os, html

SITE = "https://odiin2024.github.io/flashboss-site/"
RU_PAGES = ["index", "home", "wordlists", "lessons", "english", "french",
            "about", "packs", "voices", "resources", "italian", "german",
            "spanish", "esperanto", "toki-pona", "latin-roots", "german-roots",
            "norman-roots", "greek-roots", "affiliate", "in-development"]
LOCALES = ["de", "es", "ja", "zh"]

BANNER_CSS = (
".beta-note{background:#1b1508; border-bottom:1px solid #6b5a2a; color:#e8d9b0;"
" font:500 12.5px/1.55 system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;"
" text-align:center; padding:9px 16px; margin:0;}\n"
".beta-note b{color:#e0a93f; font-weight:700; letter-spacing:.09em;}\n"
".beta-note a{color:#e0a93f; text-decoration:underline; text-underline-offset:2px;}\n")

BANNER_CSS_FIXED = BANNER_CSS + ".beta-note{position:fixed; inset:0 auto auto 0; width:100%; z-index:30;}\n"

BANNER = (
'<div class="beta-note" role="status"><b>БЕТА-ПЕРЕВОД</b> — русская версия сайта '
'черновая и ещё не прошла редактуру. Нашли ошибку в тексте? '
'<a href="report.html">Сообщите нам</a> · <a href="{en}">Read in English</a></div>')


def load_strings(base):
    path = f"update/ru/{base}.strings.tsv"
    pairs = []
    if os.path.exists(path):
        for ln in open(path, encoding="utf-8"):
            ln = ln.rstrip("\n")
            if not ln or ln.startswith("#") or "\t" not in ln:
                continue
            en, ru = ln.split("\t", 1)
            # multi-line pairs are stored with literal \n
            en, ru = en.replace("\\n", "\n"), ru.replace("\\n", "\n")
            if en and ru:
                pairs.append((en, ru))
    # longest first: protects substrings
    pairs.sort(key=lambda p: -len(p[0]))
    return pairs


def apply_strings(s, pairs):
    misses = []
    for en, ru in pairs:
        if en in s:
            s = s.replace(en, ru)
        else:
            misses.append(en)
    return s, misses


def ru_url(base):
    return SITE + ("index.ru.html" if base == "index" else f"{base}.ru.html")


def en_href(base):
    return "index.html" if base == "index" else f"{base}.html"


# ---------- hreflang ----------
def add_hreflang(s, base):
    if 'hreflang="ru"' in s:
        return s
    line = f'<link rel="alternate" hreflang="ru" href="{ru_url(base)}">'
    m = list(re.finditer(r'<link rel="alternate" hreflang="(?!x-default)[a-z-]+"[^>]*>', s))
    if not m:
        return s
    last = m[-1]
    return s[:last.end()] + "\n" + line + s[last.end():]


# ---------- switcher ----------
_LI_RU = '<li><a href="{href}"{cur}>Русский</a></li>'

def add_switcher(s, base, is_ru):
    """Add the Русский entry; on a ru page also move aria-current onto it.

    The entry may already be present — the English source gets wired too — so
    the aria-current relocation must run whether or not we just added it.
    """
    href = f"{base}.ru.html"
    if "Русский" not in s:
        m = re.search(r'(<ul class="lang-menu"[^>]*>)(.*?)(</ul>)', s, re.S)
        if not m:
            return s
        entry = "\n            " + _LI_RU.format(href=href, cur='')
        new = m.group(1) + m.group(2).rstrip() + entry + "\n        " + m.group(3)
        s = s[:m.start()] + new + s[m.end():]
    if is_ru:
        menu = re.search(r'<ul class="lang-menu".*?</ul>', s, re.S)
        if menu:
            block = menu.group(0).replace(' aria-current="true"', '')
            block = block.replace(f'<a href="{href}">Русский</a>',
                                  f'<a href="{href}" aria-current="true">Русский</a>')
            s = s[:menu.start()] + block + s[menu.end():]
    return s


# ---------- internal links ----------
def rewrite_links(s):
    """Point internal links at .ru.html, but ONLY for pages that have one.

    The language menu is held out: its hrefs are the per-locale files and must
    stay exactly as written, or the ru page links "English" back to itself.
    """
    def repl(m):
        base = m.group(1)
        if base in RU_PAGES:
            return f'href="{base}.ru.html"'
        return m.group(0)

    menu = re.search(r'<ul class="lang-menu".*?</ul>', s, re.S)
    if not menu:
        return re.sub(r'href="([a-z0-9-]+)\.html"', repl, s)
    head, block, tail = s[:menu.start()], menu.group(0), s[menu.end():]
    pat = r'href="([a-z0-9-]+)\.html"'
    return re.sub(pat, repl, head) + block + re.sub(pat, repl, tail)


# ---------- steam ----------
def steam_lang(s):
    def repl(m):
        url = m.group(0)
        if "l=russian" in url:
            return url
        url = re.sub(r'[?&]l=[a-z]+', '', url)
        sep = "&" if "?" in url else "?"
        return url + sep + "l=russian"
    return re.sub(r'https://store\.steampowered\.com/[^"\']*', repl, s)


# ---------- banner ----------
def inject_banner(s, base, fixed):
    if "beta-note" in s:
        return s
    css = BANNER_CSS_FIXED if fixed else BANNER_CSS
    s = s.replace("</style>", css + "</style>", 1)
    s = re.sub(r'(<body[^>]*>)', r'\1\n' + BANNER.format(en=en_href(base)), s, count=1)
    return s


def build(base):
    src = f"{base}.html"
    dst = f"{base}.ru.html"
    s = open(src, encoding="utf-8").read()

    pairs = load_strings(base)
    s, misses = apply_strings(s, pairs)

    s = re.sub(r'<html lang="[^"]*"', '<html lang="ru"', s, count=1)
    s = s.replace(f'<link rel="canonical" href="{SITE}">',
                  f'<link rel="canonical" href="{ru_url(base)}">')
    s = s.replace(f'<meta property="og:url" content="{SITE}">',
                  f'<meta property="og:url" content="{ru_url(base)}">')
    s = re.sub(r'(<link rel="canonical" href=")' + re.escape(SITE) + r'[a-z0-9.-]+\.html(">)',
               r'\g<1>' + ru_url(base) + r'\g<2>', s)
    s = re.sub(r'(<meta property="og:url" content=")' + re.escape(SITE) + r'[a-z0-9.-]+\.html(">)',
               r'\g<1>' + ru_url(base) + r'\g<2>', s)
    s = add_hreflang(s, base)
    s = rewrite_links(s)
    s = add_switcher(s, base, True)
    s = s.replace('<script src="lang-redirect.js"></script>\n', '')
    s = s.replace('<script src="lang-redirect.js"></script>', '')
    s = steam_lang(s)
    s = inject_banner(s, base, fixed=(base == "index"))
    if base == "index":
        # banner is fixed at y=0; move the fixed switcher below it
        s = s.replace(".lang-switch{position:fixed; top:14px;",
                      ".lang-switch{position:fixed; top:52px;")
    # switcher button label
    s = re.sub(r'(<button class="lang-toggle"[^>]*>)[A-Z]{2}', r'\g<1>RU', s)
    s = re.sub(r'aria-label="(Choose language|Sprache wählen|[^"]*)"(\s*>(?:EN|RU))',
               r'aria-label="Выбрать язык"\2', s)

    open(dst, "w", encoding="utf-8").write(s)
    return dst, len(pairs), misses


def wire():
    """Add the ru hreflang + switcher entry to every sibling locale."""
    touched = []
    for base in RU_PAGES:
        for fn in [f"{base}.html"] + [f"{base}.{l}.html" for l in LOCALES]:
            if not os.path.exists(fn):
                continue
            s0 = open(fn, encoding="utf-8").read()
            s = add_hreflang(s0, base)
            s = add_switcher(s, base, False)
            if s != s0:
                open(fn, "w", encoding="utf-8").write(s)
                touched.append(fn)
    return touched


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    if cmd == "wire":
        t = wire()
        print(f"wired {len(t)} sibling files:" if t else "wire: no change")
        for f in t:
            print("  ", f)
    else:
        for base in sys.argv[2:] or RU_PAGES:
            dst, n, misses = build(base)
            print(f"{dst}: {n} strings applied, {len(misses)} unmatched")
            for m in misses[:12]:
                print("    MISS:", m[:90])

#!/usr/bin/env python3
"""Check a locale sibling against its English original.

    python3 scripts/l10n/verify.py immersion            # every locale that exists
    python3 scripts/l10n/verify.py immersion de es       # just these

Exits non-zero if any check fails, so it can gate a commit.

WHAT IT CHECKS, and why each one is here:

  lang/canonical/hreflang/switcher/beta
      the mechanical plumbing localize_new_pages.py owns. Cheap to get wrong,
      invisible on the page, and the whole point of the translation.

  leftover English
      a key written as a FRAGMENT rather than a whole sentence leaves the
      English article or conjunction stranded mid-sentence — "the Stichwort",
      "begin and commence". Scanning the visible text for English function
      words catches exactly that. English words quoted as examples of English
      (begin, catch, aquarium, the prefix lists) carry no function words and do
      not trip it.

  tag balance
      every element opened is closed, and the counts differ from the English
      page only by the language switcher and the beta notice. A key that ate a
      closing tag shows up here.

  pack names
      the six immersion pack names must survive in English in every locale.

  numerals
      the page must not invent, drop or recount a number. Every digit run in
      the English page must still be there, allowing only for the locale's
      thousands separator.

  banned claims
      no CEFR code, no hours figure, no price. These are banned on every
      surface of the site and a translator reaching for a familiar frame is
      exactly how one gets in.
"""
import re, sys, pathlib, html as H
from collections import Counter

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from localize_new_pages import BASE, LOCALES, NATIVE, THOUSANDS, HTML_LANG, page_name

ROOT = pathlib.Path(__file__).resolve().parents[2]
PACKS = ["English Advance", "German Roots", "Norman Roots",
         "English Adept", "Latin Roots", "Greek Roots"]
# Product names stay English in every locale, so they must not count as leftover
# English. "The Guide" and "The Guide Part II" carry an article and would
# otherwise trip the scan on every page that names them. Longest first.
KEEP_EN = sorted(["The Guide Part II", "The Guide", "The Complete Series",
                  "FlashBoss", "Latin Pareto", "Latin Core", "Swahili Core",
                  "Swahili Pareto 1", "Swahili Pareto 2", "English Core",
                  "Bahasa Indonesia", "System Reference Document", "FlashBoss Roots"]
                 + PACKS, key=len, reverse=True)
# NOT \b after the group: \b does not fire between "0" and a CJK character, so
# "1,000枚" stayed unnormalised and counted as 1 and 000 rather than 1000.
# A thousands group, and ONLY a thousands group. The lookbehind for a dot or a
# digit is what keeps a dotted citation intact: without it "Cic. Verr. 2.2.108"
# collapsed to "2.2108" and the Latin page was reported as losing the number 108.
THOUSAND_COMMA = re.compile(r"(?<![\d.,])(\d{1,3}),(\d{3})(?!\d)")
# The same shape for a dot locale. A blanket .replace(".","") turned the German
# page's "System Reference Document 5.2" into "52" and reported three numbers
# missing that were never missing.
THOUSAND_DOT = re.compile(r"(?<![\d.,])(\d{1,3})\.(\d{3})(?!\d)")
# Not \b on the left: a Latin dictionary entry writes its genitive as "-is", and
# \b fires after the hyphen, so "virtūs, f., -is" was reported as English and a
# translator changed the Latin to dodge it. A hyphen-attached token is a suffix,
# not a word.
FUNC = re.compile(r"(?<![-\w])(the|and|with|from|that|this|which|every|your|you|are|is|of|for)(?![-\w])", re.I)
# A key written as a fragment starting after the article leaves "a", "an" or
# "the" alone at the head of a bullet. Two <li>s on the immersion page shipped
# that way. "a" and "an" are real words in some target languages, so this only
# fires at the very start of a line, where an English article is what it is.
STRANDED = re.compile(r"^(an?|the)\s", re.I)
BANNED = [(re.compile(r"\b[ABC][12]\b"), "CEFR level code"),
          (re.compile(r"\b\d+\s*(hours?|hrs?|Stunden|horas|時間|小时|часов)\b", re.I), "hours figure"),
          (re.compile(r"[$€£¥]\s?\d"), "price")]


def strip(s):
    s = re.sub(r"<(style|script)\b.*?</\1>", " ", s, flags=re.S | re.I)
    return re.sub(r"<!--.*?-->", " ", s, flags=re.S)


def text_lines(s):
    return [H.unescape(x).strip() for x in re.sub(r"<[^>]*>", "\n", strip(s)).splitlines()]


def without_product_names(line):
    for name in KEEP_EN:
        line = line.replace(name, " ")
    return line


def tags(s):
    return Counter(m.group(1).lower() for m in re.finditer(r"<(/?[a-zA-Z][a-zA-Z0-9]*)", strip(s)))


def digits(s, loc):
    """Every number in the visible text, with the locale separator normalised out."""
    sep = THOUSANDS[loc]
    body = " ".join(text_lines(s))
    body = re.sub(THOUSAND_DOT if sep == "." else THOUSAND_COMMA, r"\1\2", body)
    return Counter(re.findall(r"\d+", body))


def declared_number_changes(base, loc):
    """Numbers a strings module says it deliberately does not reproduce.

    Almost always a translation must carry the English page's figures through
    untouched. The exception is a figure that is genuinely different in the
    localised product — the German edition of The Guide cites the German rules
    book, so its sample card names a different page. A module records those in
    NUMBERS_CHANGED, with the reason, and nothing else is forgiven.
    """
    f = pathlib.Path(__file__).with_name(f"{base}_{loc}.py")
    if not f.exists():
        return {}
    ns = {}
    try:
        exec(compile(f.read_text(encoding="utf-8"), str(f), "exec"), ns)
    except Exception:
        return {}
    return ns.get("NUMBERS_CHANGED", {}) or {}


def check(base, loc):
    ep, lp = ROOT / page_name(base, "en"), ROOT / page_name(base, loc)
    en, lo = ep.read_text(encoding="utf-8"), lp.read_text(encoding="utf-8")
    bad = []

    m = re.search(r'<html lang="([^"]*)"', lo)
    if not m or m.group(1) != HTML_LANG[loc]:
        bad.append(f"html lang is {m.group(1) if m else 'absent'}, expected {HTML_LANG[loc]}")
    if f'<link rel="canonical" href="{BASE}{page_name(base, loc)}">' not in lo:
        bad.append("canonical does not point at this page")
    langs = set(re.findall(r'hreflang="([^"]*)"', lo))
    missing = {l for l in LOCALES if (ROOT / page_name(base, l)).exists()} - langs
    if missing:
        bad.append(f"hreflang missing {sorted(missing)}")
    for l in LOCALES:
        if (ROOT / page_name(base, l)).exists() and f'>{NATIVE[l]}</a>' not in lo:
            bad.append(f"switcher missing {NATIVE[l]}")
    if 'class="beta-note"' not in lo:
        bad.append("beta-translation notice absent")

    left = [x for x in text_lines(lo)
            if len(x) > 3 and FUNC.search(without_product_names(x))]
    if left:
        bad.append(f"{len(left)} lines still English, first: {left[0][:70]!r}")
    strand = [x for x in text_lines(lo)
              if len(x) > 3 and STRANDED.match(without_product_names(x).lstrip())]
    if strand:
        bad.append(f"{len(strand)} lines open with a stranded English article, "
                   f"first: {strand[0][:60]!r}")

    te, tl = tags(en), tags(lo)
    for t, n in tl.items():
        if not t.startswith("/") and tl.get("/" + t, n) != n and t not in ("br", "img", "link", "meta", "input"):
            bad.append(f"<{t}> opened {n} times, closed {tl.get('/' + t, 0)}")
    for t in ("section", "table", "ul", "p", "h2", "h3"):
        if te.get(t, 0) != tl.get(t, 0):
            bad.append(f"<{t}> count {te.get(t,0)} in English, {tl.get(t,0)} here")

    body = " ".join(text_lines(lo))
    for p in PACKS:
        if p in " ".join(text_lines(en)) and p not in body:
            bad.append(f"pack name {p!r} did not survive")

    allowed = declared_number_changes(base, loc)
    de_, dl = digits(en, "en"), digits(lo, loc)
    for n, c in de_.items():
        if dl.get(n, 0) < c and n not in allowed:
            bad.append(f"number {n} appears {c}x in English, {dl.get(n,0)}x here")
    for pat, what in BANNED:
        if pat.search(body):
            bad.append(f"banned {what}: {pat.search(body).group(0)!r}")
    return bad


def main():
    base = sys.argv[1]
    locs = sys.argv[2:] or [l for l in LOCALES if l != "en" and (ROOT / page_name(base, l)).exists()]
    if not locs:
        print(f"{base}: no siblings on disk")
        return 0
    fails = 0
    for loc in locs:
        bad = check(base, loc)
        if bad:
            fails += 1
            print(f"  {page_name(base, loc)}  FAIL")
            for b in bad:
                print(f"      {b}")
        else:
            print(f"  {page_name(base, loc)}  ok")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())

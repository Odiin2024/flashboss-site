#!/usr/bin/env python3
"""Inject localized gloss fields (Translation_de/_es/_ja/_zh/_ru) into the site's
word-list data files, sourced from the game repo's per-cluster card files.

One source of truth: flashcard_sets/<Pack>/{core|pareto1|pareto2}/tier_N/<slug>/<slug>.json
in the knight repo. The site FINAL files keep their exact byte layout (one card
per line, compact objects) — only card lines that gain/refresh a localized
field are rewritten, with json.dumps default separators which reproduce the
existing style. Idempotent: a re-run after the repo gains more localized
layers picks up only the new fields.

English packs are skipped: per the Roots/Adept immersion ruling they carry no
localized Translation fields (verified — English_Advance included; only
Translation_gb spelling twins exist, which are a spelling variant, not a gloss).

Usage: python3 scripts/inject_gloss_fields.py [--repo /path/to/knight/flashcard_sets]
"""
import argparse
import json
import os
import sys

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_REPO = "/home/odiin/Documents/Bootcamp/knight/flashcard_sets"

LOCALES = ("de", "es", "ja", "zh", "ru")

# Russian has no gloss layer upstream yet. Per Odiin's ruling it DEFAULTS TO
# ENGLISH: Translation_ru takes the card's English Translation verbatim, so the
# Russian word lists read English until a real ru layer is authored. English
# packs are untouched — they are English-to-English already, through the site's
# definition field (the Roots/Adept immersion ruling).
SOURCE_KEY = {"ru": "Translation"}

# site data file (relative to site root) -> repo set dir (relative to flashcard_sets)
MAPPING = [
    ("data/german/CORE_FINAL.json", "German/core"),
    ("data/german/PARETO1_FINAL.json", "German_Extensions/pareto1"),
    ("data/german/PARETO2_FINAL.json", "German_Extensions/pareto2"),
    ("data/spanish/CORE_FINAL.json", "Spanish/core"),
    ("data/spanish/PARETO1_FINAL.json", "Spanish_Extensions/pareto1"),
    ("data/spanish/PARETO2_FINAL.json", "Spanish_Extensions/pareto2"),
    ("data/italian/CORE_FINAL.json", "Italian/core"),
    ("data/italian/PARETO1_FINAL.json", "Italian_Extensions/pareto1"),
    ("data/italian/PARETO2_FINAL.json", "Italian_Extensions/pareto2"),
    ("data/esperanto/CORE_FINAL.json", "Esperanto/core"),
    ("data/esperanto/PARETO1_FINAL.json", "Esperanto_Extensions/pareto1"),
    ("data/esperanto/PARETO2_FINAL.json", "Esperanto_Extensions/pareto2"),
    ("data/french/CORE_FINAL.json", "French/core"),
    ("data/french/PARETO1_FINAL.json", "French_Extensions/pareto1"),
    ("data/french/PARETO2_FINAL.json", "French_Extensions/pareto2"),
    ("data/toki_pona/CORE_FINAL.json", "Toki_Pona/core"),
]


def load_repo_cluster(repo_set_dir, tier, slug):
    path = os.path.join(repo_set_dir, f"tier_{tier}", slug, f"{slug}.json")
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as f:
        cards = json.load(f)
    return cards if isinstance(cards, list) else None


def norm_word(w):
    """Strip the separable-prefix pipe marker (ab|biegen -> abbiegen)."""
    return (w or "").replace("|", "")


def norm_variants(site_word):
    """Deterministic repo-side spellings of a site word: pipe-stripped equal,
    or the sich-reflexive twin (repo 'sich ein|loggen' for site 'einloggen')."""
    n = norm_word(site_word)
    return {n, "sich " + n}


def build_set_index(repo_set_dir):
    """word -> [cards] across every cluster of the set (for cards that moved
    clusters during repo regrooming). Deterministic exact-word lookups only."""
    index = {}
    for tier_d in sorted(os.listdir(repo_set_dir)):
        if not tier_d.startswith("tier_"):
            continue
        tp = os.path.join(repo_set_dir, tier_d)
        for slug in sorted(os.listdir(tp)):
            cf = os.path.join(tp, slug, slug + ".json")
            if not os.path.isfile(cf):
                continue
            try:
                cards = json.load(open(cf, encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            if isinstance(cards, list):
                for c in cards:
                    index.setdefault(c.get("TargetWord"), []).append(c)
    return index


def ru_self_fill(c, patched, stats):
    """Give an unmatched site card its Translation_ru anyway.

    Russian defaults to English, and this card's own English Translation IS
    that value, so writing it is a visual no-op — the page would have fallen
    back to Translation regardless. It keeps the ru layer complete instead of
    ragged, so "does this card have Russian?" stays a straight yes/no.
    """
    if c.get("Translation_ru"):
        return
    v = c.get("Translation")
    if isinstance(v, str) and v.strip():
        c["Translation_ru"] = v
        patched[id(c)] = True
        stats["added"]["ru"] = stats["added"].get("ru", 0) + 1


def unique(cands):
    return cands[0] if len(cands) == 1 else None


def match_repo_card(site_card, idx, repo_cards, by_word, set_index):
    """Match a site card to its repo twin, most-constrained rule first.
    Every rule is an exact deterministic criterion — never fuzzy, never a
    guess; ambiguity or absence -> (None, reason).
      1 positional TargetWord equality within the cluster
      2 unique TargetWord within the cluster
      3 unique (TargetWord, TargetArticle) within the cluster
      4 unique pipe/sich-normalized TargetWord within the cluster
      5 unique exact TargetWord anywhere in the set (card moved clusters)
      6 unique pipe/sich-normalized set-wide
    Case-insensitive matching is allowed ONLY positionally (same cluster, same
    index): German capitalizes nouns, so a set-wide caseless rule would pair
    verb/noun homographs of different senses (braten 'to roast' vs Braten
    'oven roast').
    """
    w = site_card.get("TargetWord")
    if idx < len(repo_cards) and repo_cards[idx].get("TargetWord") == w:
        return repo_cards[idx], "positional"
    if idx < len(repo_cards) and \
            norm_word(repo_cards[idx].get("TargetWord")).lower() in \
            {v.lower() for v in norm_variants(w)}:
        return repo_cards[idx], "positional-caseless"
    cands = by_word.get(w, [])
    if len(cands) == 1:
        return cands[0], "cluster-word"
    if len(cands) > 1:
        art = site_card.get("TargetArticle", "")
        m = unique([c for c in cands if c.get("TargetArticle", "") == art])
        if m:
            return m, "cluster-word+article"
    variants = norm_variants(w)
    m = unique([c for c in repo_cards if norm_word(c.get("TargetWord")) in variants])
    if m:
        return m, "cluster-normalized"
    m = unique(set_index.get(w, []))
    if m:
        return m, "set-wide"
    m = unique([c for cs in set_index.values() for c in cs
                if norm_word(c.get("TargetWord")) in variants])
    if m:
        return m, "set-normalized"
    return None, "unmatched"


def process_file(site_path, repo_set_dir):
    rel = os.path.relpath(site_path, SITE_ROOT)
    if not os.path.isfile(site_path):
        return {"file": rel, "status": "absent"}
    if not os.path.isdir(repo_set_dir):
        return {"file": rel, "status": "repo dir missing: " + repo_set_dir}

    with open(site_path, encoding="utf-8") as f:
        text = f.read()
    data = json.loads(text)

    # Build the patch plan: document-order list of (site_card, patched_dict|None)
    stats = {"file": rel, "status": "ok", "cards": 0, "matched": 0,
             "unmatched": 0, "missing_clusters": [], "added": {}, "updated": {},
             "unmatched_words": [], "rules": {}, "fallback_examples": []}
    set_index = build_set_index(repo_set_dir)
    doc_cards = []          # cards in document order (parsed dicts)
    patched = {}            # id(card) -> True if changed
    for cl in data.get("clusters", []):
        repo_cards = load_repo_cluster(repo_set_dir, cl.get("tier"), cl.get("slug"))
        if repo_cards is None:
            stats["missing_clusters"].append(cl.get("slug"))
            for c in cl.get("cards", []):
                doc_cards.append(c)
                stats["cards"] += 1
                stats["unmatched"] += 1
                ru_self_fill(c, patched, stats)
                if len(stats["unmatched_words"]) < 8:
                    stats["unmatched_words"].append(c.get("TargetWord"))
            continue
        by_word = {}
        for rc in repo_cards:
            by_word.setdefault(rc.get("TargetWord"), []).append(rc)
        for i, c in enumerate(cl.get("cards", [])):
            doc_cards.append(c)
            stats["cards"] += 1
            rc, rule = match_repo_card(c, i, repo_cards, by_word, set_index)
            if rc is None:
                stats["unmatched"] += 1
                ru_self_fill(c, patched, stats)
                if len(stats["unmatched_words"]) < 12:
                    stats["unmatched_words"].append(c.get("TargetWord"))
                continue
            stats["matched"] += 1
            stats["rules"][rule] = stats["rules"].get(rule, 0) + 1
            if rule not in ("positional", "cluster-word", "cluster-word+article") \
                    and len(stats["fallback_examples"]) < 8:
                stats["fallback_examples"].append(
                    f"{c.get('TargetWord')}→{rc.get('TargetWord')} [{rule}]")
            for loc in LOCALES:
                key = f"Translation_{loc}"
                val = rc.get(SOURCE_KEY.get(loc, key))
                if not isinstance(val, str) or not val.strip():
                    continue
                if key not in c:
                    c[key] = val
                    patched[id(c)] = True
                    stats["added"][loc] = stats["added"].get(loc, 0) + 1
                elif c[key] != val:
                    c[key] = val
                    patched[id(c)] = True
                    stats["updated"][loc] = stats["updated"].get(loc, 0) + 1

    if not patched:
        stats["status"] = "ok (no changes)"
        return stats

    # Rewrite: walk lines; the k-th card-looking line is the k-th card in
    # document order. Only patched card lines change; everything else is
    # byte-identical.
    lines = text.split("\n")
    out = []
    k = 0
    fmt_warn = 0
    for line in lines:
        body = line.strip()
        is_card = False
        if body.startswith("{") and (body.endswith("}") or body.endswith("},")):
            trail = "," if body.endswith(",") else ""
            core = body[:-1] if trail else body
            try:
                obj = json.loads(core)
                is_card = isinstance(obj, dict) and "TargetWord" in obj
            except json.JSONDecodeError:
                is_card = False
        if not is_card:
            out.append(line)
            continue
        if k >= len(doc_cards):
            print(f"  !! {rel}: more card lines than parsed cards — aborting file", file=sys.stderr)
            return {"file": rel, "status": "ABORT: card line/parse mismatch"}
        card = doc_cards[k]
        if obj.get("TargetWord") != card.get("TargetWord"):
            print(f"  !! {rel}: card order mismatch at #{k} ({obj.get('TargetWord')!r} vs {card.get('TargetWord')!r}) — aborting file", file=sys.stderr)
            return {"file": rel, "status": "ABORT: card order mismatch"}
        if patched.get(id(card)):
            indent = line[: len(line) - len(line.lstrip())]
            if json.dumps(obj, ensure_ascii=False) != core:
                fmt_warn += 1
            out.append(indent + json.dumps(card, ensure_ascii=False) + trail)
        else:
            out.append(line)
        k += 1
    if k != len(doc_cards):
        print(f"  !! {rel}: card line count {k} != parsed cards {len(doc_cards)} — aborting file", file=sys.stderr)
        return {"file": rel, "status": "ABORT: card count mismatch"}

    new_text = "\n".join(out)
    with open(site_path, "w", encoding="utf-8") as f:
        f.write(new_text)
    json.load(open(site_path, encoding="utf-8"))  # verify parse
    if fmt_warn:
        stats["status"] += f" ({fmt_warn} lines format-normalized)"
    return stats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=DEFAULT_REPO,
                    help="path to the knight repo's flashcard_sets dir")
    args = ap.parse_args()

    reports = []
    for site_rel, repo_rel in MAPPING:
        r = process_file(os.path.join(SITE_ROOT, site_rel),
                         os.path.join(args.repo, repo_rel))
        reports.append(r)

    print(f"{'file':44} {'cards':>5} {'match':>5} {'unmat':>5}  added/updated per locale")
    for r in reports:
        if "cards" not in r:
            print(f"{r['file']:44} -- {r['status']}")
            continue
        adds = " ".join(f"{k}+{v}" for k, v in sorted(r["added"].items())) or "-"
        upds = " ".join(f"{k}~{v}" for k, v in sorted(r["updated"].items()))
        line = f"{r['file']:44} {r['cards']:>5} {r['matched']:>5} {r['unmatched']:>5}  {adds}"
        if upds:
            line += f"  upd: {upds}"
        if r["status"] != "ok":
            line += f"  [{r['status']}]"
        print(line)
        fb = {k: v for k, v in r["rules"].items()
              if k not in ("positional", "cluster-word", "cluster-word+article")}
        if fb:
            print(f"    fallback matches: {fb}")
            print(f"    e.g.: {'; '.join(r['fallback_examples'])}")
        if r["missing_clusters"]:
            print(f"    missing repo clusters: {', '.join(r['missing_clusters'])}")
        if r["unmatched_words"]:
            print(f"    unmatched e.g.: {', '.join(map(str, r['unmatched_words']))}")


if __name__ == "__main__":
    main()

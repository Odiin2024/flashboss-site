#!/usr/bin/env python3
"""Add Translation_ru to the word-list data, via the same three-stage fleet.

The site's word lists fall back to the English gloss when a locale field is
missing, so the Russian page currently shows Russian chrome over English
meanings. This fills data/<lang>/<SET>_FINAL.json with Translation_ru.

The pilot's lesson governs the prompt: bare glosses are the failure zone, so
each card goes to the drafter WITH its context — the target word, its article,
the English gloss, and the shipped de/es glosses to triangulate the sense.

  python3 scripts/ru_glosses.py draft  data/german/CORE_FINAL.json
  python3 scripts/ru_glosses.py check  data/german/CORE_FINAL.json
  python3 scripts/ru_glosses.py refute data/german/CORE_FINAL.json
  python3 scripts/ru_glosses.py merge  data/german/CORE_FINAL.json
"""
import sys, os, json, re
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, "scripts")
from ru_fleet import call, jparse, DRAFTER, CHECKER

CACHE = "update/ru/.glosses"

RULES = """You are producing Russian dictionary glosses for a vocabulary-learning
game. Each card teaches ONE word in a foreign language. You are given the target
word, its article/part-of-speech if any, the English gloss, and the shipped
German/Spanish glosses for triangulation.

RULES (these are where machine translation usually fails — obey them exactly):
1. Gloss the TARGET WORD, not the English gloss's surface form. If English is
   ambiguous, the German/Spanish glosses disambiguate — use them.
2. NEVER include an article or determiner in the gloss. "der Apfel" -> яблоко,
   never "это яблоко" or "the apple".
3. Keep the part of speech. A verb glosses as an infinitive (идти, не «ходьба»).
   An adjective glosses as an adjective in masculine nominative singular.
4. Lowercase unless it is a proper noun.
5. Short. A gloss, not a definition. Two or three words at most; use a comma to
   separate close senses (e.g. "работа, труд"). No explanations, no parentheses
   unless disambiguating a homonym.
6. Watch false friends. Translate the SENSE the card teaches.
7. Russian only in the output — no transliteration, no English."""

DRAFT_SYS = RULES + """

Return ONLY a JSON array: [{"n":<card n>,"ru":"<gloss>"}]"""

CHECK_SYS = RULES + """

TASK: adversarially review these Russian glosses. Flag only real defects: wrong
sense, false friend, article/determiner contamination, wrong part of speech,
an English or transliterated word, or a gloss so long it is a definition.
Return ONLY a JSON array, entries for defective cards only:
[{"n":<n>,"issue":"<what is wrong, English>","fix":"<corrected gloss>"}]
Return [] if all are sound."""

REFUTE_SYS = RULES + """

TASK: another model flagged these glosses. REFUTE each flag by default. Uphold
only if the gloss is genuinely wrong for a Russian learner. A different but
valid synonym is NOT a defect.
Return ONLY: [{"n":<n>,"verdict":"refuted|upheld","why":"<one sentence>"}]"""

def slug(path): return path.replace("/", "_").replace(".json", "")
def cp(stage, path): return f"{CACHE}/{stage}/{slug(path)}.json"
def load(stage, path):
    p = cp(stage, path)
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}
def save(stage, path, o):
    os.makedirs(f"{CACHE}/{stage}", exist_ok=True)
    json.dump(o, open(cp(stage, path), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

def cards(path):
    d = json.load(open(path, encoding="utf-8"))
    out = []
    for c in d["clusters"]:
        for k in c["cards"]:
            if k.get("TargetWord"):
                out.append(k)
    return d, out

def ctx(k):
    bits = [f'n={k["n"]}', f'word={k.get("TargetArticle","")} {k["TargetWord"]}'.strip()]
    if k.get("Translation"):    bits.append(f'en={k["Translation"]}')
    if k.get("Translation_de"): bits.append(f'de={k["Translation_de"]}')
    if k.get("Translation_es"): bits.append(f'es={k["Translation_es"]}')
    return " | ".join(bits)

def stage_run(path, stage, batch, sys_prompt, model, payload_fn, keyfn):
    _, ks = cards(path)
    done = load(stage, path)
    todo = [k for k in ks if str(k["n"]) not in done] if stage == "draft" else ks
    if stage == "draft" and not todo:
        print(f"  {os.path.basename(path)}: {stage} cached"); return done
    items = todo if stage == "draft" else ks
    groups = [items[i:i+batch] for i in range(0, len(items), batch)]
    def run(g):
        return jparse(call(model, sys_prompt, payload_fn(g), temp=0.15)) or []
    with ThreadPoolExecutor(6) as ex:
        for out in ex.map(run, groups):
            for r in out:
                if isinstance(r, dict) and r.get("n") is not None:
                    done[str(r["n"])] = keyfn(r)
    save(stage, path, done)
    return done

def draft(path):
    d = stage_run(path, "draft", 40, DRAFT_SYS, DRAFTER,
                  lambda g: "\n".join(ctx(k) for k in g), lambda r: r.get("ru"))
    _, ks = cards(path)
    print(f"  {os.path.basename(path)}: drafted {len(d)}/{len(ks)}")

def check(path):
    dr = load("draft", path)
    if not dr: sys.exit("draft first")
    _, ks = cards(path)
    have = [k for k in ks if str(k["n"]) in dr]
    groups = [have[i:i+30] for i in range(0, len(have), 30)]
    flags = {}
    def run(g):
        p = "\n".join(f'{ctx(k)} | RU={dr[str(k["n"])]}' for k in g)
        return jparse(call(CHECKER, CHECK_SYS, p, temp=0.15)) or []
    with ThreadPoolExecutor(6) as ex:
        for out in ex.map(run, groups):
            for r in out:
                if isinstance(r, dict) and r.get("n") is not None: flags[str(r["n"])] = r
    save("check", path, flags)
    print(f"  {os.path.basename(path)}: {len(flags)} flags / {len(have)} cards")

def refute(path):
    dr, fl = load("draft", path), load("check", path)
    if not fl: save("refute", path, {}); print("  no flags"); return
    _, ks = cards(path); byn = {str(k["n"]): k for k in ks}
    items = [(n, v) for n, v in fl.items() if n in byn]
    groups = [items[i:i+20] for i in range(0, len(items), 20)]
    out_all = {}
    def run(g):
        p = "\n".join(f'{ctx(byn[n])} | RU={dr.get(n)} | FLAG: {v.get("issue")}' for n, v in g)
        return jparse(call(DRAFTER, REFUTE_SYS, p, temp=0.15)) or []
    with ThreadPoolExecutor(6) as ex:
        for out in ex.map(run, groups):
            for r in out:
                if isinstance(r, dict) and r.get("n") is not None: out_all[str(r["n"])] = r
    save("refute", path, out_all)
    up = sum(1 for v in out_all.values() if v.get("verdict") == "upheld")
    print(f"  {os.path.basename(path)}: {up} upheld of {len(items)}")

def merge(path):
    """Write Translation_ru in, surgically — key order preserved, no JSON churn."""
    dr, fl, rf = load("draft", path), load("check", path), load("refute", path)
    d = json.load(open(path, encoding="utf-8"))
    n_set = 0
    for c in d["clusters"]:
        for k in c["cards"]:
            key = str(k.get("n"))
            ru = dr.get(key)
            if not ru: continue
            if rf.get(key, {}).get("verdict") == "upheld" and fl.get(key, {}).get("fix"):
                ru = fl[key]["fix"]
            k["Translation_ru"] = ru
            n_set += 1
    json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"  {os.path.basename(path)}: Translation_ru on {n_set} cards")

if __name__ == "__main__":
    cmd = sys.argv[1]
    for p in sys.argv[2:]:
        {"draft": draft, "check": check, "refute": refute, "merge": merge}[cmd](p)

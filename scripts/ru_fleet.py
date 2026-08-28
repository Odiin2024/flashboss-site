#!/usr/bin/env python3
"""Chinese-fleet translation pipeline for FlashBoss Russian pages.

Three stages, after knight/resources/questions/QWEN_DRAFTER_JUDGE_PILOT_2026-08-21.md:
  draft   deepseek-v4-flash  writes the Russian (it sees the whole unit, so it
                             keeps context — the pilot's lesson: MT dies on
                             bare glosses, instruction models don't)
  check   qwen3-max          adversarial pass, runs hot on purpose
  refute  deepseek-v4-flash  the OTHER family re-examines every flag and is
                             default-refuted; cross-model agreement is the
                             load-bearing filter (kills ~96% of flags)
Survivors go to Claude. Never let a model judge its own draft.

Results cache to update/ru/.fleet/<stage>/<page>.json — reruns are free.

  python3 scripts/ru_fleet.py draft  packs about voices
  python3 scripts/ru_fleet.py check  packs
  python3 scripts/ru_fleet.py refute packs
  python3 scripts/ru_fleet.py survivors packs      # what Claude must rule on
"""
import sys, os, json, re, time, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

BASE = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions"
DRAFTER, CHECKER = "deepseek-v4-flash", "qwen3-max"
CACHE = "update/ru/.fleet"

def key():
    k = os.environ.get("QWEN_KEY")
    if k: return k
    for p in (os.path.expanduser(os.environ.get("QWEN_KEY_FILE", "")),
              os.path.join(os.environ.get("SCRATCH", ""), ".qwen_key")):
        if p and os.path.exists(p):
            return open(p).read().strip()
    sys.exit("no API key: set QWEN_KEY or QWEN_KEY_FILE")

HOUSE = """FlashBoss house conventions for Russian (ru). These are binding.

KEEP EXACTLY AS-IS, never translate:
- All HTML: tags, attribute names, href/src/class/id/style values, entities
  (&nbsp; &mdash; &rarr; &amp; &ldquo;), inline markup <b> <i> <a> <span>.
- Brand tokens: FlashBoss, Pareto, Master Odiin, Steam, Piper, Windows, Mac,
  Linux, DLC.
- Registered pack names: English Core, English Advance, English Adept, Core,
  Pareto 1, Pareto 2, German Roots, Norman Roots, Latin Roots, Greek Roots,
  French Core, Spanish Core, Italian Core, Toki Pona.
- Key names: Shift, Ctrl, Enter, Alt, Tab, Esc. Language codes: EO, EN.
- The in-game audio cue LISTEN.
- Any word or sentence in a language BEING TAUGHT (French, German, Spanish,
  Italian, Esperanto, Toki Pona, Latin, Greek) — those are teaching material.
  Translate only the English gloss/explanation around them.

HOUSE TERMINOLOGY (use these exact renderings):
  boss fight -> босс-файт        cluster -> блок           tier -> уровень
  flashcard/card -> карточка     word list -> список слов  lesson -> урок
  pack -> набор                  voice -> голос            duel -> дуэль
  spaced repetition -> интервальное повторение
  home -> главная                voices -> голоса          resources -> материалы
  packs -> наборы                walkthrough -> руководство
  Listen · Read · Repeat · Rate · Fight ->
      Слушай · Читай · Повторяй · Оценивай · Сражайся
  Try the demo -> Попробовать демо      Live on Steam -> Уже в Steam
  Get X on Steam -> Купить X в Steam    Report Errors -> Сообщить об ошибке
  out now -> уже вышел                  free -> бесплатно
  graduate (a card) -> считается освоенной

STYLE:
- Address the reader as вы (lowercase, not capitalised).
- Russian prose drops the thousands comma: 1,000 -> 1000; 3,000 -> 3000.
- Match the source's register: terse marketing copy stays terse. Do not pad.
- Keep the source's punctuation rhythm (em dashes, middots) where Russian allows.
- Never add or drop information. Never add a claim the English does not make."""

def call(model, system, user, temp=0.2, tries=4):
    body = json.dumps({"model": model, "temperature": temp,
        "messages": [{"role":"system","content":system},{"role":"user","content":user}]}).encode()
    req = urllib.request.Request(BASE, data=body, headers={
        "Authorization": f"Bearer {key()}", "Content-Type": "application/json"})
    for a in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                return json.load(r)["choices"][0]["message"]["content"]
        except Exception as e:
            if a == tries - 1: return f"__ERROR__ {e}"
            time.sleep(2 * (a + 1))

def jparse(txt):
    if txt.startswith("__ERROR__"): return None
    m = re.search(r'```(?:json)?\s*(.*?)```', txt, re.S)
    if m: txt = m.group(1)
    i, j = txt.find("["), txt.rfind("]")
    if i < 0 or j < 0: i, j = txt.find("{"), txt.rfind("}")
    try: return json.loads(txt[i:j+1])
    except Exception: return None

def cpath(stage, page): return f"{CACHE}/{stage}/{page}.json"
def load(stage, page):
    p = cpath(stage, page)
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else None
def save(stage, page, obj):
    os.makedirs(f"{CACHE}/{stage}", exist_ok=True)
    json.dump(obj, open(cpath(stage, page), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

def units_of(page):
    sys.path.insert(0, "scripts")
    from ru_extract import extract
    return extract(f"{page}.html")

# ---------------- stage 1: draft ----------------
DRAFT_SYS = HOUSE + """

TASK: translate each numbered unit from English into Russian.
Return ONLY a JSON array: [{"id":<int>,"ru":"<translated unit>"}]
The "ru" value must be the COMPLETE unit with identical HTML structure —
same tags, same attributes, same order. Only human-visible text changes."""

def draft(page, batch=8, workers=6):
    us = units_of(page)
    done = load("draft", page) or {}
    todo = [u for u in us if str(u["id"]) not in done]
    if not todo:
        print(f"  {page}: draft cached ({len(done)})"); return
    groups = [todo[i:i+batch] for i in range(0, len(todo), batch)]
    def run(g):
        payload = "\n\n".join(f'#{u["id"]}\n{u["text"]}' for u in g)
        out = jparse(call(DRAFTER, DRAFT_SYS, payload))
        return g, (out or [])
    with ThreadPoolExecutor(workers) as ex:
        for g, out in ex.map(run, groups):
            got = {str(r.get("id")): r.get("ru") for r in out if isinstance(r, dict)}
            for u in g:
                v = got.get(str(u["id"]))
                if v: done[str(u["id"])] = {"en": u["text"], "ru": v, "kind": u["kind"]}
    save("draft", page, done)
    print(f"  {page}: drafted {len(done)}/{len(us)}")

# ---------------- stage 2: check ----------------
CHECK_SYS = HOUSE + """

TASK: you are an ADVERSARIAL reviewer of an English->Russian translation for
this website. For each pair, hunt for real defects:
 - meaning changed, reversed, added or dropped
 - a claim the English does not make (numbers, availability, features)
 - HTML damaged: a tag, attribute, href or entity altered or lost
 - a house-convention breach from the list above
 - something left in English that should be Russian, or vice versa
 - unnatural Russian, wrong case/agreement, calque, wrong register

Return ONLY a JSON array. Include an entry ONLY for units with a defect:
[{"id":<int>,"severity":"high|medium|low","issue":"<what is wrong, in English>","fix":"<corrected full Russian unit>"}]
Return [] if everything is sound. Do not flag mere style preference."""

def check(page, batch=6, workers=6):
    d = load("draft", page)
    if not d: sys.exit(f"{page}: draft first")
    prev = load("check", page) or {}
    items = [(i, v) for i, v in sorted(d.items(), key=lambda kv: int(kv[0]))]
    if prev.get("_done"): print(f"  {page}: check cached ({len(prev)-1} flags)"); return
    groups = [items[i:i+batch] for i in range(0, len(items), batch)]
    flags = {}
    def run(g):
        payload = "\n\n".join(f'#{i}\nEN: {v["en"]}\nRU: {v["ru"]}' for i, v in g)
        return jparse(call(CHECKER, CHECK_SYS, payload)) or []
    with ThreadPoolExecutor(workers) as ex:
        for out in ex.map(run, groups):
            for r in out:
                if isinstance(r, dict) and r.get("id") is not None:
                    flags[str(r["id"])] = r
    flags["_done"] = True
    save("check", page, flags)
    print(f"  {page}: {len(flags)-1} flags from {len(items)} units")

# ---------------- stage 3: cross-family refute ----------------
REFUTE_SYS = HOUSE + """

TASK: a different model flagged these translations as defective. Your job is to
REFUTE each flag. Default to refuting: only uphold a flag if the defect is
real and would matter to a Russian reader or break the page. Style preference,
a synonym you would have chosen differently, or a defensible paraphrase are
NOT defects — refute those.

Return ONLY a JSON array:
[{"id":<int>,"verdict":"refuted|upheld","why":"<one sentence, English>"}]"""

def refute(page, batch=5, workers=6):
    d, f = load("draft", page), load("check", page)
    if not d or not f: sys.exit(f"{page}: need draft + check")
    fl = [(i, v) for i, v in f.items() if i != "_done"]
    if not fl:
        save("refute", page, {"_done": True}); print(f"  {page}: no flags to refute"); return
    groups = [fl[i:i+batch] for i in range(0, len(fl), batch)]
    out_all = {}
    def run(g):
        payload = "\n\n".join(
            f'#{i}\nEN: {d[i]["en"]}\nRU: {d[i]["ru"]}\nFLAG ({v.get("severity")}): {v.get("issue")}'
            for i, v in g if i in d)
        return jparse(call(DRAFTER, REFUTE_SYS, payload)) or []
    with ThreadPoolExecutor(workers) as ex:
        for out in ex.map(run, groups):
            for r in out:
                if isinstance(r, dict) and r.get("id") is not None:
                    out_all[str(r["id"])] = r
    out_all["_done"] = True
    save("refute", page, out_all)
    up = [i for i, v in out_all.items() if i != "_done" and v.get("verdict") == "upheld"]
    print(f"  {page}: {len(up)} upheld of {len(fl)} flags -> Claude")

def survivors(page):
    d, f, r = load("draft", page), load("check", page), load("refute", page)
    out = []
    for i, v in (f or {}).items():
        if i == "_done": continue
        rv = (r or {}).get(i, {})
        if rv.get("verdict") == "upheld":
            out.append({"id": i, "en": d[i]["en"], "ru": d[i]["ru"],
                        "severity": v.get("severity"), "issue": v.get("issue"),
                        "fix": v.get("fix"), "why": rv.get("why")})
    return out

if __name__ == "__main__":
    cmd, pages = sys.argv[1], sys.argv[2:]
    for p in pages:
        {"draft": draft, "check": check, "refute": refute}.get(cmd, lambda x: None)(p)
    if cmd == "survivors":
        allv = []
        for p in pages: allv += [dict(s, page=p) for s in survivors(p)]
        json.dump(allv, sys.stdout, ensure_ascii=False, indent=1)

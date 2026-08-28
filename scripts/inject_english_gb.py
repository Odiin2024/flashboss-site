#!/usr/bin/env python3
"""Add the British spelling twin to the site's English word-list data.

The site ships American English (Odiin's ruling), and the pages offer a UK/US
toggle. Rather than ship two files per pack, each card carries its British twin
inline and ONLY where it actually differs — 156 cards across nine packs — so the
toggle is instant and the files stay lean.

It also CANONICALIZES: some views were built from the British layer (Norman
Roots was; knight's own English Pareto views are), so where a site card holds
the British form it is flipped back to the American base and the British form
moves into the _gb twin.

Fields added when they differ from the base:
  TargetWord_gb   the headword          (defense / defence)
  Translation_gb  the gloss             (EFL packs: Core, Pareto 1, Pareto 2)
  definition_gb   the definition        (standalone packs, from ExampleTranslation_gb)

Byte layout is preserved: only card lines that gain a field are rewritten.
Idempotent.
"""
import glob, json, os, re, sys

REPO = "/home/odiin/Documents/Bootcamp/knight/flashcard_sets"
MAP = [("data/english/core/CORE_FINAL.json", "English/core"),
       ("data/english/p1/CORE_FINAL.json",   "English_Extensions/pareto1"),
       ("data/english/p2/CORE_FINAL.json",   "English_Extensions/pareto2"),
       ("data/english/ad/CORE_FINAL.json",   "English_Adept/core"),
       ("data/english/adv/CORE_FINAL.json",  "English_Advance/core"),
       ("data/english/gr/CORE_FINAL.json",   "German_Roots/core"),
       ("data/english/gkr/CORE_FINAL.json",  "Greek_Roots/core"),
       ("data/english/nr/CORE_FINAL.json",   "Norman_Roots/core"),
       ("data/english/lr/CORE_FINAL.json",   "Latin_Roots/core")]

def repo_cards(setdir):
    """TargetWord -> card, plus document order, across the set."""
    def ck(p):
        m = re.search(r'cluster(\d+)_(\d+)', os.path.basename(p)); return (int(m.group(1)), int(m.group(2)))
    root = os.path.join(REPO, setdir); order = []
    for td in sorted(glob.glob(root + "/tier_*"), key=lambda x: int(re.search(r'tier_(\d+)', x).group(1))):
        for cd in sorted([c for c in glob.glob(td + "/*") if os.path.isdir(c)], key=ck):
            s = os.path.basename(cd); f = os.path.join(cd, s + ".json")
            if os.path.isfile(f):
                order += json.load(open(f, encoding="utf-8"))
    by = {}
    for c in order:
        by.setdefault(c.get("TargetWord"), []).append(c)
        if c.get("TargetWord_gb"): by.setdefault(c["TargetWord_gb"], []).append(c)
    return order, by

def main():
    grand = 0
    for rel, setdir in MAP:
        if not os.path.isfile(rel):
            print(f"  {rel}: absent — skipped"); continue
        text = open(rel, encoding="utf-8").read()
        data = json.loads(text)
        order, by = repo_cards(setdir)
        site = [c for cl in data["clusters"] for c in cl["cards"]]
        added = {}
        for i, c in enumerate(site):
            w = c.get("TargetWord")
            rc = order[i] if i < len(order) and order[i].get("TargetWord") == w else None
            if rc is None:
                cand = by.get(w, [])
                rc = cand[0] if len(cand) == 1 else None
            if rc is None: continue
            new = {}
            # Some site views were built from the British layer (Norman Roots was,
            # and knight's own English Pareto views are). Canonicalize: the base
            # field is American, the _gb field is the British twin.
            for base_key, rb, rg in (("TargetWord",  "TargetWord",         "TargetWord_gb"),
                                     ("Translation", "Translation",        "Translation_gb"),
                                     ("definition",  "ExampleTranslation", "ExampleTranslation_gb")):
                if base_key not in c: continue
                bv, gv = rc.get(rb), rc.get(rg)
                if not bv: continue
                if c[base_key] == gv and gv != bv:
                    new[base_key] = bv                     # site held the British form — flip to US
                cur = new.get(base_key, c[base_key])
                if gv and gv != cur:
                    new[base_key + "_gb"] = gv
            new = {k: v for k, v in new.items() if c.get(k) != v}
            if new: added[i] = new
        if not added:
            print(f"  {rel:<38} no change"); continue
        # rewrite only the card lines that gain fields; everything else byte-identical
        lines = text.split("\n"); out = []; k = 0
        for ln in lines:
            st = ln.strip().rstrip(",")
            if st.startswith('{"n":'):
                if k in added:
                    obj = json.loads(st); obj.update(added[k])
                    ind = ln[:len(ln) - len(ln.lstrip())]
                    ln = ind + json.dumps(obj, ensure_ascii=False) + ("," if ln.rstrip().endswith(",") else "")
                k += 1
            out.append(ln)
        if k != len(site):
            print(f"  !! {rel}: card line count {k} != {len(site)} — aborting"); continue
        open(rel, "w", encoding="utf-8").write("\n".join(out))
        n = sum(len(v) for v in added.values())
        print(f"  {rel:<38} {len(added)} cards, {n} gb fields")
        grand += n
    print(f"\n  {grand} British twin fields injected")

if __name__ == "__main__":
    sys.exit(main())

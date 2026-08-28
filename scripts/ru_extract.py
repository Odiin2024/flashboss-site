#!/usr/bin/env python3
"""Extract translatable units from a FlashBoss page.

A unit is the FULL outer HTML of a leaf prose element (one with no block-level
child), so the translator sees a whole sentence with its inline links intact —
never a fragment. Plus <title>, the human-facing meta tags, and the
human-facing attributes.

The unit text doubles as the replacement key for scripts/ru_localize.py, which
applies pairs longest-first, so a repeated element translates consistently.

Usage: python3 scripts/ru_extract.py packs.html > update/ru/packs.units.json
"""
import sys, json, re
from html.parser import HTMLParser

PROSE = {"p","h1","h2","h3","h4","h5","h6","li","dt","dd","summary","button",
         "figcaption","caption","th","td","label","option","legend"}
# leaf-prose containers: only counted when they hold no block child
SOFT  = {"div","span","a"}
BLOCK = PROSE | {"div","section","header","footer","nav","main","ul","ol","dl",
                 "table","tr","form","details","article","aside","figure"}
INLINE_OK = {"a","b","i","em","strong","span","br","code","small","sup","sub","u","abbr","wbr"}
SKIP_CONTAINER = {"script","style"}
ATTRS = ("alt","aria-label","placeholder","title")
META_NAMES = ("description","twitter:title","twitter:description")
META_PROPS = ("og:title","og:description")

class Ex(HTMLParser):
    def __init__(self, src):
        super().__init__(convert_charrefs=False)
        self.src = src; self.stack = []; self.hits = []; self.skip = 0
        self.lineoff = [0]
        for ln in src.split("\n"):
            self.lineoff.append(self.lineoff[-1] + len(ln) + 1)
    def handle_starttag(self, tag, attrs):
        if tag in SKIP_CONTAINER: self.skip += 1
        if tag in ("br","img","meta","link","input","hr","wbr"): return
        self.stack.append((tag, self.getpos(), dict(attrs)))
    def handle_startendtag(self, tag, attrs): pass
    def handle_endtag(self, tag):
        if tag in SKIP_CONTAINER:
            self.skip = max(0, self.skip - 1); return
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                t, pos, at = self.stack.pop(i)
                del self.stack[i:]
                if not self.skip:
                    self.record(t, pos, at)
                return
    def _off(self, pos):
        line, col = pos
        return self.lineoff[line - 1] + col
    def record(self, tag, pos, at):
        if tag not in PROSE and tag not in SOFT: return
        start = self._off(pos)
        end = self._off(self.getpos()) + len(f"</{tag}>")
        outer = self.src[start:end]
        if not outer.startswith("<" + tag): return
        inner = outer[outer.find(">") + 1: outer.rfind("</")]
        # leaf only: no block-level child
        for m in re.findall(r'<\s*([a-zA-Z][a-zA-Z0-9]*)', inner):
            if m.lower() in BLOCK: return
            if m.lower() not in INLINE_OK: return
        text = re.sub(r'<[^>]+>', '', inner)
        text = re.sub(r'&[a-zA-Z#0-9]+;', ' ', text).strip()
        if not text: return
        if not re.search(r'[A-Za-z]{2}', text): return          # no words -> nothing to translate
        self.hits.append((start, end, outer))

def extract(fn):
    src = open(fn, encoding="utf-8").read()
    # hold out regions that must never be translated
    holes = []
    for pat in (r'<ul class="lang-menu".*?</ul>', r'<div class="beta-note".*?</div>',
                r'<button class="lang-toggle".*?</button>',
                r'<script\b.*?</script>', r'<style\b.*?</style>', r'<!--.*?-->'):
        for m in re.finditer(pat, src, re.S): holes.append((m.start(), m.end()))
    def in_hole(a, b): return any(h0 <= a and b <= h1 for h0, h1 in holes)

    p = Ex(src); p.feed(src)
    units, seen = [], set()
    # drop nested hits: keep the outermost only when spans overlap
    p.hits.sort(key=lambda h: (h[0], -(h[1] - h[0])))
    taken = []
    for a, b, outer in p.hits:
        if in_hole(a, b): continue
        if any(a >= x and b <= y for x, y in taken): continue
        taken.append((a, b))
        if outer in seen: continue
        seen.add(outer)
        units.append({"kind": "element", "text": outer})
    # <title>
    m = re.search(r'<title>(.*?)</title>', src, re.S)
    if m: units.append({"kind": "title", "text": m.group(0)})
    # meta
    for m in re.finditer(r'<meta[^>]+>', src):
        tag = m.group(0)
        n = re.search(r'name="([^"]+)"', tag); pr = re.search(r'property="([^"]+)"', tag)
        c = re.search(r'content="([^"]*)"', tag)
        if not c or not c.group(1).strip(): continue
        if (n and n.group(1) in META_NAMES) or (pr and pr.group(1) in META_PROPS):
            units.append({"kind": "meta", "text": f'content="{c.group(1)}"'})
    # human-facing attributes
    for a in ATTRS:
        for m in re.finditer(rf'{a}="([^"]*)"', src):
            v = m.group(1)
            if not re.search(r'[A-Za-z]{2}', v): continue
            if in_hole(m.start(), m.end()): continue
            if v in ("Choose language",): continue      # ru_localize.py owns this one
            u = f'{a}="{v}"'
            if u in seen: continue
            seen.add(u); units.append({"kind": "attr", "text": u})
    out, seen2 = [], set()
    for i, u in enumerate(units):
        if u["text"] in seen2: continue
        seen2.add(u["text"]); u["id"] = i; out.append(u)
    return out

if __name__ == "__main__":
    fn = sys.argv[1]
    u = extract(fn)
    json.dump({"file": fn, "units": u}, sys.stdout, ensure_ascii=False, indent=1)
    print(f"\n<!-- {len(u)} units -->", file=sys.stderr)

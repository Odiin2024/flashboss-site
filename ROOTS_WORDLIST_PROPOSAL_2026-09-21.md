# Roots word lists: locale cluster names, and the twin line — PROPOSAL

2026-09-21. Nothing in here is built. Two changes are proposed to the word-list
pages for the four Roots packs (and, where noted, for Adept and Advance):

* **(a)** show the authored cluster names from `cluster_names_<loc>.json` instead of a
  humanised folder slug, in every locale;
* **(b)** show the twin / etymology line from the card's `Notes` under each word.

Both are cheap. (a) is unambiguously a bug fix — the names are authored, translated and
checked upstream, and the site throws them away. (b) is a product decision: it is the
line that makes a Roots pack a Roots pack, and no page on the site shows it.

---

## (a) Authored cluster names

### What exists now

Each pack carries the names, already translated, in
`knight/flashcard_sets/<Pack>/core/`:

| pack | clusters | `cluster_names.json` | de | es | ja | zh | ru |
|---|---|---|---|---|---|---|---|
| Greek Roots | 56 | 4.3 KB | 5.0 | 4.9 | 5.0 | 5.0 | 5.4 |
| Latin Roots | 30 | 1.9 KB | 2.2 | 2.2 | 2.2 | 2.1 | 2.5 |
| German Roots | 47 | 2.6 KB | 2.7 | 2.7 | 2.7 | 2.8 | 3.4 |
| Norman Roots | 48 | 2.6 KB | 2.7 | 2.6 | 2.7 | 2.7 | 3.4 |

Every locale is complete — 56/56, 30/30, 47/47, 48/48 keys, keyed by folder slug.
(Greek also has a `cluster_names_gb.json` with 2 keys, spelling twins only.)

The site never reads any of them. `wordlists*.html` builds every cluster label from the
folder name:

```js
function humanize(slug){ return slug.replace(/^cluster\d+_\d+_?/,'').replace(/_/g,' ')
                             .replace(/\b\w/g,c=>c.toUpperCase()).trim() || slug; }
function clusterLabel(c){ return humanize(c.slug) || c.cluster_id || 'Cluster'; }
```

So `cluster1_3_root_tele_auto_cycl_dynam_far_self_wheel_power` shows as
**"Root Tele Auto Cycl Dynam Far Self Wheel Power"** in all six locales, where the
authored English name is **"tele-, auto-, cycl-, dynam-"** and the German one is its
checked twin. This is the same in `wordlists.de/es/ja/zh/ru.html`: the localized pages
show slug-English.

### The change

**Generator** — `scripts/build_site_views.py`, in `serialize()`, emit the names on the
cluster object alongside `cluster_id`/`tier`/`slug`, loading the six name files once per
pack:

```js
"cluster_id": "T1-C3", "tier": 1, "slug": "cluster1_3_root_tele_...",
"name": "tele-, auto-, cycl-, dynam-",
"name_de": "...", "name_es": "...", "name_ja": "...", "name_zh": "...", "name_ru": "...",
```

Inline, not a sidecar file: the cluster dropdown is already built from `CORE_FINAL.json`,
so this adds no second request and cannot arrive late. A missing key falls through to the
English name, and a missing English name falls through to `humanize(slug)` exactly as
today — the page never regresses below what it shows now.

**Page** — one line per file. In `wordlists.html`:

```js
function clusterLabel(c){ return c.name || humanize(c.slug) || c.cluster_id || 'Cluster'; }
```

and in each localized sibling, the locale first (the same shape the word glosses already
use — `Translation_de` first, English fallback):

```js
function clusterLabel(c){ return c.name_de || c.name || humanize(c.slug) || c.cluster_id || 'Cluster'; }
```

Six files, one line each: `wordlists.html`, `.de`, `.es`, `.ja`, `.zh`, `.ru`. Nothing
else moves — the print header, the `#pack/set/cluster` share URL and the multi-select all
key off `cluster_id`, not the label.

**Applies beyond Roots.** Every language pack in `flashcard_sets` carries
`cluster_names*.json`, so the same generator step fixes Italian, German, Spanish, French,
Esperanto, Toki Pona, Latin, English Core/P1/P2, Adept and Advance in one pass. Proposed
as one change, all packs, because a half-applied rule is worse than the slug.

**Size cost:** +25 KB Greek, +13 KB each for the others, on views of 198/103/173/161 KB —
between +8% and +13% raw, and these files gzip at about 4:1 over Pages, so roughly
+6 KB, +3 KB, +3 KB, +3 KB on the wire. Per locale it is a quarter of that if we ever
decide to split the names out per page locale; inline-all is recommended for now because
one file per pack cannot go stale against another.

---

## (b) The twin line

### What exists now

The card's `Notes` in knight is one line with a fixed grammar:

```
noun | Old French compaignon, from Late Latin companionem, com- + panis (one who shares
bread). Germanic twin: friend. syn: comrade, fellow | ant: stranger
```

The site's lean view keeps `pos`, `syn` and `ant` (pulled out by `roots_card()` on
2026-09-19) and drops everything between them — the etymology formula and the twin. On
the page a Roots card is therefore indistinguishable from an Adept card: a headword, a
definition, a synonym pair.

How much of the middle exists, per pack:

| pack | cards | cards with an explicit `… twin:` | twin clauses | whole middle segment |
|---|---|---|---|---|
| Greek Roots | 1,000 | 0 | — | 144 KB |
| Latin Roots | 500 | 0 | — | 75 KB |
| German Roots | 1,000 | 482 | 35 KB | 96 KB |
| Norman Roots | 1,000 | 998 | 95 KB | 169 KB |

Greek and Latin Roots carry **no** `twin:` label — their middle is the root formula
("NEO- (νέος, new, young). The neuter of neos, the name given to a gas found unlooked-for
in the air."), which is the same pedagogic payload under a different shape. A twin-only
field would therefore light up two packs of four and leave the two oldest Roots packs
looking empty, which is why the recommendation below is the whole segment.

### The change

**Generator** — one line in `roots_card()` in `scripts/build_site_views.py`, beside the
existing `pos`/`syn`/`ant` extraction:

```python
    o["etym"] = _segment(notes)   # everything between the pos pipe and "syn:" — the
                                  # root formula and the Germanic/Norman/Latin twin
```

with `_segment()` taking `notes.split('|', 1)[1]` up to the first `syn:`, stripped. It
needs the same care the syn extraction did: `syn:` is not pipe-anchored, while `ant:` and
`Related:` open their own pipe run. `Related:` is deliberately left out — it is a
cross-reference for the game's drill, not reading matter.

**Page** — the word row in `wordlists*.html` is built in `normCards()` and rendered in the
`.def` branch of `loadAndRender()`. Add `etym: c.etym || ''` to `normCards()`, and one
element under the definition:

```js
${etym ? `<div class="ety">${esc(etym)}</div>` : ''}
```

plus a rule next to the existing `.def .dw .sa`:

```css
.ety{font-size:.86em; opacity:.72; margin-top:2px;}
@media print{ .ety{display:none;} }   /* the printed fold card keeps its two-line back */
```

Print is the reason for the media query: the printed card's back face is budgeted at two
lines of definition, and an etymology sentence would overflow it. Screen only, for now.
Same six files.

**Size cost:** +144 KB Greek (198 → 342 KB raw, 49 → ~95 KB gzipped), +75 KB Latin,
+96 KB German, +169 KB Norman. That is roughly a doubling. It is the largest single item
in this proposal and the one worth a ruling: a word list is fetched once per pack
selection and cached, and the gzipped delta is 30–45 KB per pack, but the page currently
loads in one breath and this is the first change that would make a Roots pack noticeably
heavier than an EFL pack.

Two cheaper variants, if the cost is judged too high:

* **twin clause only** (`Germanic twin: friend.`) — +35 KB German, +95 KB Norman, nothing
  for Greek and Latin. Cheapest, but leaves half the series unserved.
* **etym on demand** — keep `CORE_FINAL.json` as it is and emit a second per-pack file,
  `ETYM.json` (`{n: "…"}`), fetched only when the reader turns on an "etymology" toggle.
  Costs one request and a little state; costs nothing to a reader who never asks.

---

## Mock — one card row, Norman Roots, cluster T1-C1 "Everyday verbs"

Today (screen):

```
  catch                          to grab or capture something in motion
                                 (seize, snatch : release)
```

With (a) and (b), English page:

```
  1-1  Catch, carry, change

  catch                          to grab or capture something in motion
                                 Old French cachier (to hunt), from Latin captare
                                 (to grasp at). Germanic twin: grab. Latin twin:
                                 capture, the same captare taken straight from Latin.
                                 (seize, snatch : release)
```

With (a) and (b), `wordlists.de.html` — the cluster name in German, the card in English,
per the Roots immersion ruling:

```
  1-1  Verben: fangen, tragen

  catch                          to grab or capture something in motion
                                 Old French cachier (to hunt), from Latin captare
                                 (to grasp at). Germanic twin: grab. Latin twin:
                                 capture, the same captare taken straight from Latin.
                                 (seize, snatch : release)
```

And what (a) alone fixes on the Greek page, in the cluster dropdown:

```
  before   Tier 1 ▸ 1-3 Root Tele Auto Cycl Dynam Far Self Wheel Power
  after    Tier 1 ▸ 1-3 tele-, auto-, cycl-, dynam-
  after (de) Tier 1 ▸ 1-3 Fern, selbst, Rad, Kraft
```

---

## Recommendation

Take (a) now, for every pack, not just Roots — the names are authored and translated and
the site is discarding them, and the change is one line per page plus a generator step.

Take (b) as the full `etym` segment if the ~35 KB gzipped per pack is acceptable; if not,
take the on-demand variant rather than the twin-only one, so Greek and Latin Roots are not
left out of their own series.

Files that would change, for the record:

* `scripts/build_site_views.py` — name loading in `serialize()`, one line in `roots_card()`
* `wordlists.html`, `wordlists.de.html`, `wordlists.es.html`, `wordlists.ja.html`,
  `wordlists.zh.html`, `wordlists.ru.html` — `clusterLabel()`, `normCards()`, one row
  element, one CSS rule
* regenerated: `data/english/{gkr,lr,gr,nr,ad,adv}/CORE_FINAL.json` and, for (a), every
  other `*_FINAL.json` under `data/`

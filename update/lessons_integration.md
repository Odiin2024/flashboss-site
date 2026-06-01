# Integrating `lessons.html` with the existing lesson files

A drop-in reader for the FlashBoss reference lessons. It renders the existing
`tierN_lessons.json` files **verbatim** — the same content the game shows — so the
website never reinterprets a lesson, it just displays it. This is the twin of
`wordlists.html`: same conventions, same `?lang=` deep-links, same preview fallback.

---

## 1. Where it goes

Put `lessons.html` at the site root (it's linked as `lessons.html` from `resources.html`
and from each language page's "Resources" link). No build step required to ship it.

## 2. Where the data goes — one function to edit

The page loads lesson files by convention. Edit the single function at the top of the
script if Code places the files anywhere else:

```js
function lessonUrl(lang, tier){ return `data/${lang.toLowerCase()}/tier${tier}_lessons.json`; }
```

Default layout:

```
data/
  italian/   tier1_lessons.json … tier5_lessons.json
  german/    tier1_lessons.json … tier5_lessons.json
  spanish/   …
  esperanto/ …
```

Each `tierN_lessons.json` is exactly the existing shape: an **array of lesson objects**
for that tier. On selecting a language the page fetches tiers 1–5, tags each lesson with
its tier, concatenates them in order, and groups the lesson rail by tier. Missing tiers
are skipped silently; a language with no files shows "not published yet."

## 3. The JSON contract (the render is verbatim — keep to this)

Per lesson:

```
lesson_id, trigger_word, trigger_card_number, title, header_color, pages[]
```

Per page:

```
page, total_pages, content[], pronunciation (optional), pronunciation_mappings { "N": "spoken text" }
```

Hard constraints the renderer depends on:

1. **Line width** — every `content` line is hand-wrapped to **≤ 48 columns**. The page
   renders fixed-width with no reflow (a fit-to-width sizer scales the font so the widest
   line fits the screen on any device). A 49-char line breaks the alignment.
2. **Press-N integrity** — every `Press N` token in `content` must have a matching key in
   that page's `pronunciation_mappings`, and vice versa. The reader binds them by number.
3. **`header_color`** — one of: `green`, `blue`, `gold`/`amber`, `rose`, `purple`, `cyan`.
   It tints the lesson's screen frame.
4. **Field names are frozen** — the reader keys off the names above exactly.

These are the same constraints in SPEC B; nothing new.

## 4. Navigation, params, deep-links

- **Language** select → loads that language's tiers.
- **Lesson rail** → grouped by tier (`Tier 1  L1 L2 L3 L4   Tier 2  L5 …`), click to open.
- **Within a lesson** → `‹ prev` / `next ›` (or ← / → arrows) page through.
- **URL params**: `?lang=Italian` (the jump-links from `resources.html` use this) and an
  optional `?lesson=003` to deep-link a specific lesson. The page writes the current
  selection back into the URL, so any view is a shareable link.

## 5. Audio

Tapping a `Press N` line speaks that line's `pronunciation_mappings` text and shows it
below the screen. Today it uses the **browser's built-in voice** for the language
(`it-IT`, `de-DE`, `es-ES`; Esperanto has no system voice, so it shows the text only).
Zero hosting, works immediately, but it is not the game's Piper voice.

**Piper upgrade path (later):** pre-render each `pronunciation_mappings` entry through
Piper and host the clips under a predictable key, e.g.
`audio/<lang>/<lesson_id>/p<page>_<N>.mp3`. Then swap the `speak()` function to play the
clip when present and fall back to the browser voice when not. No change to the lesson
JSON is needed — the mapping text stays the source of truth.

## 6. Remove the preview fallback before/after launch (optional)

`lessons.html` embeds one `SAMPLE` object — the real Italian Tier 1 — used **only** when a
fetch fails (so the artifact preview and a fresh checkout still demonstrate the reader).
Once the real files are hosted, fetch wins and the sample is never seen. It's safe to
leave, or delete the `const SAMPLE = …` block to slim the file.

## 7. Adding a language or a tier

No code change. Drop a `tierN_lessons.json` into the right `data/<lang>/` folder matching
the convention, conforming to the contract in §3. It appears on next load.

## 8. SEO — the real win is static pre-render

This page is the inviting front door, but the lesson text is fetched by JS, so crawlers
won't index the lessons from here. The multiplier — same idea as the word lists — is to
**pre-render one static HTML page per lesson** (or per language/tier) from the same
`tierN_lessons.json`, with the lesson content in the HTML source and titles like
*"Italian: Articles & Elision — pronunciation and usage"*. That's where the long-tail
searches live ("italian passato prossimo explained", "german article rules"). Same data,
a small render script, dozens of indexable pages funnelling to the store.

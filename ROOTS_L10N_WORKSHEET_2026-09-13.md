# Roots pages — strings added 2026-09-13, awaiting localisation

The four English pages (`german-roots.html`, `norman-roots.html`, `latin-roots.html`,
`greek-roots.html`) gained one new section and one amended line. The `.de .es .ja .ru .zh`
variants are **untouched** — they still lack both. Below is every string that needs translating,
and nothing else. Drop the translations in and the localized pages match.

Brand tokens stay Latin per canon: **FlashBoss**. The six interface languages are named in the
reader's own language, as the store pages do it.

---

## A. New section — identical on all four pages

Insert immediately before the `<!-- ROOTS SERIES -->` comment, same markup as the English:

```html
  <!-- ENGLISH IN ENGLISH -->
  <section class="wrap">
    <div class="frame reveal">
      <span class="tag">Immersion</span>
      <h2>English taught in English</h2>
      <dl>
        <dt>The cards</dt><dd>…</dd>
        <dt>The interface</dt><dd>…</dd>
        <dt>British or American</dt><dd>…</dd>
      </dl>
    </div>
  </section>
```

| slot | English |
|---|---|
| tag | Immersion |
| h2 | English taught in English |
| dt 1 | The cards |
| dd 1 | English throughout — headword, definition, example sentence and usage note. You meet English in English, the way you will meet it everywhere else. |
| dt 2 | The interface |
| dd 2 | FlashBoss itself speaks **English, German, Japanese, Russian, Simplified Chinese and Spanish**. Navigate the game in your own language while the English on the card stays English. |
| dt 3 | British or American |
| dd 3 | The **British English Layer** covers every English pack. Take this one in British voice and British spelling if you prefer — the cards carry both. |

Note for dd 2: in a non-English locale this sentence is the selling point, so the reader's own
language should be the one they notice in the list.

---

## B. Amended line — the Roots Series subheading

Was, on all four:

> The shape of English and its neighbours, made visible.

Now, on **Latin Roots** and **Greek Roots**:

> The shape of English and its neighbours, made visible. Four packs, **no order** — start with the layer closest to a language you already speak.

On **German Roots**, with the origin hint:

> …start with the layer closest to a language you already speak, which for you may be Dutch, German, Frisian or a Scandinavian language.

On **Norman Roots**:

> …start with the layer closest to a language you already speak, which for you may be French, Spanish, Italian, Portuguese or Romanian.

**The origin hint is the point, and it should be re-aimed per locale rather than translated
literally.** On the German-language page the reader already speaks German, so "which for you may
be Dutch, German…" is nearly tautological; the useful hint there is that German Roots is their
shortest way in. Same for the Spanish page and Norman Roots. Worth a judgement call per locale
rather than a straight translation.

---

## C. Latin Roots only — one factual line

`<dt>Paired cards</dt>` gained its cluster count, to match Greek's 55 and German's 48:

> 500 cards, 1,000 words, **in 50 root clusters across five tiers** — …

---

## D. Hero image — no translation needed, but it affects all locales

All four English pages now read:

```css
background:url('roots-hero.png') center 30% / cover no-repeat,
  #0d120c url('english.png') center 30% / cover no-repeat;
```

Two layers, so an absent `roots-hero.png` changes nothing — `english.png` shows as before. When
the school image exists, drop it in the site root as `roots-hero.png` and all four English heroes
pick it up. **The localized variants still point at `english.png` alone** and will need the same
two-layer line if they are to share the new hero.

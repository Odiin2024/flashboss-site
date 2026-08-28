# Russian terminology — DRAFT, needs Odiin's ruling

Proposed `ru` column for the localization canon, which currently covers only
en / de / ja / es-419. This is a **proposal, not an amendment**: per the banner
on `LOCALIZATION_CANON.md`, that file is a downstream copy and amendments are
ratified upstream in `knight/docs/store_pages/drafts/LOCALIZATION_CANON.md`
(see `knight/docs/CANON_SYNC.md`), then synced down with
`tools/canon_sync.py --adopt --only localization`. Nothing below should be
written into the site copy by hand.

Every choice below was applied consistently across
`index.ru.html`, `home.ru.html`, `wordlists.ru.html`, `lessons.ru.html`,
`english.ru.html`.

## Brand tokens — kept Latin
`FlashBoss`, `Pareto`, `Master Odiin`, and the registered DLC names
(`English Core`, `Adept`, `Advance`, `German Roots`, `Greek Roots`,
`Norman Roots`, `Latin Roots`) stay Latin, per the canon's Scope section.

**OPEN RULING — Pareto.** The 2026-08-19 amendment made ja an exception
(パレート) because Japanese has an established native rendering. Russian is in
exactly the same position: **Парето** is standard (принцип Парето, диаграмма
Парето) and carries the same 80/20 resonance. I defaulted to Latin `Pareto`
because that is what the canon says today. Your call whether ru joins ja.

## Descriptor vocabulary

| en | ru | note |
|---|---|---|
| words | слова | takes 3 plural forms — handled by `plu()` in the page JS |
| voice | голос | |
| Core | **Core** (unchanged) | CORRECTED 2026-08-28: on the *website* all four other locales keep `German Core` / `Esperanto Core` / the `Core` selector verbatim. The canon's localized «Основа» governs capsule ART only — the two contexts differ. |
| spaced repetition | интервальное повторение | standard Russian term |
| boss fight | **босс-файт** | gamer register, matches de/es keeping "Bossfight". Alternative: «бой с боссом» (plainer, longer) |
| flashcards / cards | карточки | |
| cluster | **блок** | «кластер» is available but reads technical; «блок» is what a learner would say |
| tier | уровень | |
| pack | набор | |
| duel | дуэль | |
| master (teacher persona) | наставник | not yet used on these five pages |
| graduate (a card) | считается освоенной | |
| boss rush | — | not yet used on these five pages |

## Site chrome

| en | ru |
|---|---|
| home | главная |
| voices | голоса |
| resources | материалы |
| packs | наборы |
| word lists | списки слов |
| lessons | уроки |
| walkthrough (beta) | руководство (бета) |
| Live on Steam | Уже в Steam |
| Get FlashBoss on Steam | Купить FlashBoss в Steam |
| Report Errors | Сообщить об ошибке |
| Try the demo | Попробовать демо |
| share / copy link | поделиться / скопировать ссылку |
| Pack / Set (selectors) | Набор / Раздел |
| Listen · Read · Repeat · Rate · Fight | Слушай · Читай · Повторяй · Оценивай · Сражайся |

## Deliberately NOT translated
- `LISTEN` — the in-game audio cue. ja and zh keep it; es alone translates it
  (ESCUCHA). Kept, and the lessons lede names it so the cue reads.
- `Piper` — the TTS engine.
- `Shift` / `Ctrl` / `Enter` — key names.
- `EO` / `EN` — language codes on the lesson toggle.
- The four sample cards on `english.ru.html` — they show the actual shipped
  German/Spanish/Japanese/Chinese card content and must stay verbatim.
- The `english.ru.html` epigraph — an English Core card, quoted in English with
  a Russian gloss appended to the citation.

## Numbers
Russian prose drops the thousands comma: `1,000` → `1000`, `3,000` → `3000`.


## Corrections the Chinese fleet found in Claude's first pass (2026-08-28)

Run through the `knight` adversarial pipeline (deepseek-v4-flash draft →
qwen3-max check → deepseek refute → Claude adjudication). These were real:

| was | now | why |
|---|---|---|
| столичный французский | **континентальный французский** | "Metropolitan French" means mainland France, not the capital. ja/zh both use 本土 (mainland). A false friend. |
| «работа — … Мужской род» | «работа — … **Во французском** — мужской род» | the gender belongs to the FRENCH word; as written it asserted that *работа* (feminine in Russian) is masculine. Same bug found independently on the Italian page. |
| Немецкий: Основа | **German Core** | pack names stay English on the website — see the Core row above |
| промоute → «партнёрам» | «продвигать» | de/es/ja/zh all use a verb (bewerben / promocionar / 紹介 / 推广) |
| «почему это запоминается» | «как это запоминается» | "How it sticks" is the mechanism, not the reason |
| «кластер» | «блок» | house term, applied inconsistently in the first pass |

**Rules confirmed by the sweep, worth keeping:**
- Address the reader as **вы** throughout. The imperative tagline
  (Слушай · Читай · Повторяй…) is the one deliberate exception.
- Quotation marks: `&ldquo;/&rdquo;` become `&laquo;/&raquo;` (« ») in Russian
  body copy — this is correct typography, not a defect.
- `&amp;` legitimately disappears when the ampersand becomes the word «и».
- Field names in `<code>` (TargetWord, Translation, Notes) stay English:
  es/ja/zh all keep them; German is the outlier.
- Page `<title>` for a Roots pack stays `<Lang> Roots — FlashBoss`, as in de/es/zh.
- Teaching material stays in its own language — English morphology examples on
  the Roots pages, the voice-sample sentences, and academic citations in
  `about`. Six units on norman-roots/greek-roots are English **by decision**;
  `scripts/ru_emit.py` now prints them rather than dropping them silently.

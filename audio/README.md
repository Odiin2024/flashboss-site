# Pronunciation audio

Clips played by the LISTEN cue in lessons.html. Opus-in-Ogg (`.ogg`), mono,
~24–32 kbps is ideal. The page lazy-loads one file per tap and falls back to
browser TTS when a file is absent — so you can add them incrementally.

## Layout & names

    audio/<language>/<lesson_id>_<page>_<cue>.ogg          (foreign languages)
    audio/english/<pack>/<lesson_id>_<page>_<cue>.ogg      (English packs: ad adv gr nr lr)

- `lesson_id`  the JSON `lesson_id`, zero-padded as stored (e.g. 001, 052)
- `page`       the page number within the lesson (1-based)
- `cue`        the `pronunciation_mappings` key — the digit behind each LISTEN button

Example: `audio/german/005_3_4.ogg` = German lesson 005, page 3, cue 4.

Only the lesson LISTEN cues are consumed today (word lists have no audio UI,
and page-level `pronunciation` fields aren't wired to a control). Each language's
expected file list is in `audio/<lang>/MANIFEST.tsv`.

The extension is set once in lessons.html: `AUDIO_EXT`.

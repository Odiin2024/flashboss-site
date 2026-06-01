# Self-hosted webfonts

`wordlists.html` uses **Fantasque Sans Mono** — but *only* for the printed
flashcards (`@media print` on the `.word` cells). The screen UI stays on
JetBrains Mono.

Drop these `.woff2` files in this folder to activate it:

- `FantasqueSansMono-Regular.woff2`  (weight 400 — translations)
- `FantasqueSansMono-Bold.woff2`     (weight 700 — target words)

Get them from the **webfont kit** in the official release:
https://github.com/belluzj/fantasque-sans/releases (SIL OFL — free to embed).

Until the files are present, printed cards fall back to JetBrains Mono, so
nothing breaks.

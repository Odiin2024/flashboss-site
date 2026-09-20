# Boss-fight GIFs

The fights on `home*.html` and `immersion.html` are captured from the web demo
(`~/Programs/flashboss-demo`) **headless** — no monitor, no kit seating, nothing
that needs Odiin's screen.

    cd scripts/bossfight
    python3 shoot_fight.py --url /english/german-roots/ --lang ja --out gr_ja
    ./assemble.sh gr_ja 540          # -> out/gr_ja.gif

`--url` is a path on the demo; `--lang` is the interface language (`en de es ja
zh ru`). Every run needs its own `--port` and `--cdp` if you run them back to
back, or the previous Chrome is still holding the socket.

## What the capture does

Drives the demo over the Chrome DevTools Protocol and screenshots the
`#terminal` plate after each beat, reading the engine's own `S` state to find
the correct option — so a run is always winnable and a wrong answer is never
shown as correct.

The fight is **scripted, not random**, so every GIF tells the story the site's
copy promises: forward on a right answer, two steps back on a wrong one, the
recovery, the killstroke. **The miss is taken at position 3 or later**, because
at position 1 or 2 a wrong answer is a *fall* and the run ends
(`engine.js:110`) — which is not the story we are selling.

It stops after the first boss falls. A full run is three bosses and makes a GIF
far too long.

## Three traps, all of which cost time once

1. Chrome refuses the CDP websocket without `--remote-allow-origins=*`.
2. The demo asks "enable sound?" on first visit and its backdrop blurs the whole
   plate. The script answers it in `localStorage` before the pack page loads.
3. Clip `#terminal`, not `#terminal-wrap` — the wrapper is full viewport width.

## Packs available

`/english/{german-roots,norman-roots,latin-roots,adept,advance}/` and
`/german/ /spanish/ /italian/ /esperanto/`.

**The Guide is not in the demo**, so its fight cannot be captured this way. It
needs the desktop shoot bench (`knight/tools/shoot/`) and a real monitor.

## Naming on the site

    bossfight.gif            a foreign-language fight, English interface   home.html
    bossfight.<loc>.gif      English cards, that locale's interface        home.<loc>.html
    bossfight-immersion.gif  an English Roots fight                        immersion.html

Posters are the `01_intro` frame at the same width, so the swap does not jump.

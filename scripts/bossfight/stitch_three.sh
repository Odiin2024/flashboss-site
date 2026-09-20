#!/usr/bin/env bash
# Stitch several captured fights into ONE gif: a clapboard, the fight, the
# victory it ends on, then the next clapboard.
#
#   ./stitch_three.sh out.gif "dir:stem:lang:Name:strapline" "…" "…"
#
# FORMAT, set by Odiin 2026-09-20: "I want a capture only of the inside of the
# terminal, bordered, floating in black. no title bar, no scrollbar." So the
# crop is the terminal's INTERIOR — not the window, not its decoration, not the
# desktop behind it — and the result floats on black inside a hairline border.
# The earlier format kept the whole window and its title bar; it is superseded.
#
# THE CROP IS MEASURED, NOT GUESSED. The terminal paints #171421; the window
# border is black and the wallpaper is neither. Walking in from both axes until
# that colour starts and stops gives x 357..928, y 39..682 on the 1280x720
# capture monitor — 572x644+357+39. Re-measure if the bench moves the window.
#
# STRUCTURE, also Odiin's: "I want the first frame to be our home made bossfight
# screen with the pack name, then the last scene is the second victory screen if
# there is one, or the first one if that's the only one, then new bossfight
# clapboard, and away." An ESL pack ends on the word list toggled into English;
# an immersion pack has no toggle and ends on its cluster victory.
#
# EVERY FRAME IS LOOKED AT BEFORE IT GETS HERE. Odiin: "go over the captured
# images one by one for anomolies before making the gif. broken borders are the
# big one, and we don't want the sanctum scene." The routes no longer produce
# either, and a contact sheet of each set is read by eye before assembly.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUT="$1"; shift
F=/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf
[ -f "$F" ] || F=/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf
CROP="${FB_CROP:-572x644+357+39}"
W="${FB_W:-500}"                 # width of the terminal image itself
LINE="${FB_LINE:-#3a3120}"       # the site's own rule colour
PAD="${FB_PAD:-16}"              # black it floats in
work="$(mktemp -d)"; trap 'rm -rf "$work"' EXIT

# every panel is built at the same size, so the border never jumps
probe="$(mktemp -u).png"
n=0; delays=()
finish() {  # $1 = source png, $2 = destination
  convert "$1" -resize "${W}x" -bordercolor "$LINE" -border 1 \
          -bordercolor black -border "$PAD" "$2"
}

for spec in "$@"; do
  IFS=':' read -r dir stem lang name strap <<< "$spec"
  mapfile -t frames < <(ls "$dir"/${stem}_${lang}_frame*.png | sort)
  total=${#frames[@]}
  [ "$total" -ge 2 ] || { echo "only $total frames for $stem/$lang" >&2; exit 1; }

  # ── the clapboard: our own, on the game's own black ──────────────────────
  n=$((n+1)); p="$(printf '%s/%03d.png' "$work" $n)"
  convert -size "$(echo "$CROP" | cut -dx -f1)x$(echo "$CROP" | cut -dx -f2 | cut -d+ -f1)" \
          xc:'#0b0a10' \
    -font "$F" -fill '#d9a6e0' -pointsize 30 -gravity north -annotate +0+232 'BOSS FIGHT' \
    -fill '#ecdcb6' -pointsize 38 -gravity north -annotate +0+292 "$name" \
    -fill '#8a7a5c' -pointsize 18 -gravity north -annotate +0+368 "$strap" "$work/plate.png"
  finish "$work/plate.png" "$p"
  delays+=( -delay 175 "$p" )

  for i in "${!frames[@]}"; do
    n=$((n+1)); p="$(printf '%s/%03d.png' "$work" $n)"
    convert "${frames[$i]}" -crop "$CROP" +repage "$work/raw.png"
    finish "$work/raw.png" "$p"
    fromend=$(( total - 1 - i ))
    if   [ "$i" -eq 0 ];        then d=190      # the opening question: read it
    elif [ "$i" -eq 4 ];        then d=230      # "Wrong! Pushed back!" — the setback has to land
    elif [ "$fromend" -eq 0 ];  then d=430      # the screen the fight ends on
    elif [ "$fromend" -eq 1 ];  then d=330
    elif [ "$fromend" -eq 2 ];  then d=210      # VICTORY
    else d=145; fi
    delays+=( -delay "$d" "$p" )
  done
done

convert -dispose Background "${delays[@]}" -layers Optimize -colors 96 -loop 0 "$OUT"
identify -format '%f %wx%h %n frames  ' "$OUT"; du -h "$OUT" | cut -f1

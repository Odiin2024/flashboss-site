#!/usr/bin/env bash
# Stitch several captured fights into ONE gif, each announced by a title plate.
#
#   ./stitch_three.sh out.gif  "dir:stem:lang:Name:strapline[:tail]"  "…"  "…"
#
# Odiin, 2026-09-20: "I'm attracted to the three gifs stitched together for English.
# Maybe a bossfight screen before each one starts to make sure they get the attention
# they require." The game's own "Engaging Boss" splash cannot be captured — it is a
# timed hold and a SHOT there costs the rest of the run — so the plate is drawn here,
# inside the real window chrome, on the game's own #171421.
#
# Name and strapline must not contain a colon. The optional 6th field is that
# fight's tail hold in centiseconds, listed from its LAST frame backwards; it
# defaults to a Roots tail (VICTORY, then the two cluster-victory word lists).
# A pack with a single victory frame, like The Guide, wants just "380".
#
# WHICH FRAMES: clean_frames.py, never the raw glob — it drops the bench's
# rejects, the invalid-input frames the old route's stray KEY ENTER produced,
# and exact duplicates. See that script for why.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUT="$1"; shift
F=/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf
[ -f "$F" ] || F=/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf
CROP="${FB_CROP:-588x696+349+0}"
work="$(mktemp -d)"; trap 'rm -rf "$work"' EXIT
n=0; delays=()
for spec in "$@"; do
  IFS=':' read -r dir stem lang name strap tail <<< "$spec"
  IFS=',' read -r -a tl <<< "${tail:-380,300,200}"

  mapfile -t frames < <("$here/clean_frames.py" "$dir" "$stem" "$lang")
  total=${#frames[@]}
  [ "$total" -ge 2 ] || { echo "only $total usable frames for $stem/$lang" >&2; exit 1; }

  # the plate, drawn into the real window chrome of this fight's first frame
  n=$((n+1)); p="$(printf '%s/%03d.png' "$work" $n)"
  convert "${frames[0]}" -crop "$CROP" +repage -fill '#171421' -draw 'rectangle 9,37 579,687' \
    -font "$F" -fill '#d9a6e0' -pointsize 30 -gravity north -annotate +0+262 'BOSS FIGHT' \
    -fill '#ecdcb6' -pointsize 36 -gravity north -annotate +0+320 "$name" \
    -fill '#8a7a5c' -pointsize 17 -gravity north -annotate +0+390 "$strap" "$p"
  delays+=( -delay 170 "$p" )

  for i in "${!frames[@]}"; do
    n=$((n+1)); p="$(printf '%s/%03d.png' "$work" $n)"
    convert "${frames[$i]}" -crop "$CROP" +repage "$p"
    fromend=$(( total - 1 - i ))
    if   [ "$i" -eq 0 ];                 then d=185
    elif [ "$fromend" -lt "${#tl[@]}" ]; then d="${tl[$fromend]}"
    else d=140; fi
    delays+=( -delay "$d" "$p" )
  done
done
convert -dispose Background "${delays[@]}" -resize 500x -layers Optimize -colors 96 -loop 0 "$OUT"
identify -format '%f %wx%h %n frames  ' "$OUT"; du -h "$OUT" | cut -f1

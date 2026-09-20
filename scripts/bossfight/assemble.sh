#!/usr/bin/env bash
# Assemble a captured fight into a web-sized GIF.
# Per-frame timing: the card holds long enough to read, the reveal is quick,
# the killstroke holds so the loop lands on it.
set -euo pipefail
STEM="$1"; W="${2:-540}"
D="frames/$STEM"; OUT="out/${STEM}.gif"
mkdir -p out
args=()
for f in "$D"/*.png; do
  b=$(basename "$f")
  case "$b" in
    *arena*)   continue ;;                 # the arena is not the fight
    *intro*)   d=160 ;;
    *card*)    d=150 ;;
    *reveal*)  d=95  ;;
    *kill*)    d=320 ;;
    *)         d=120 ;;
  esac
  args+=( -delay "$d" "$f" )
done
convert "${args[@]}" -resize "${W}x" -layers OptimizeTransparency -colors 128 -loop 0 "$OUT"
identify -format "%f  %wx%h  %n frames  " "$OUT"; du -h "$OUT" | cut -f1

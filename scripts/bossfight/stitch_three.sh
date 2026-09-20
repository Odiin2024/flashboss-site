#!/usr/bin/env bash
# Stitch several captured fights into ONE gif, each announced by a title plate.
#
#   ./stitch_three.sh out.gif  "dir:stem:lang:Name:strapline"  "…"  "…"
#
# Odiin, 2026-09-20: "I'm attracted to the three gifs stitched together for English.
# Maybe a bossfight screen before each one starts to make sure they get the attention
# they require." The game's own "Engaging Boss" splash cannot be captured — it is a
# timed hold and a SHOT there costs the rest of the run — so the plate is drawn here,
# inside the real window chrome, on the game's own #171421.
set -euo pipefail
OUT="$1"; shift
F=/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf
[ -f "$F" ] || F=/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf
CROP="${FB_CROP:-586x672+350+0}"
work="$(mktemp -d)"; trap 'rm -rf "$work"' EXIT
n=0; delays=()
for spec in "$@"; do
  IFS=':' read -r dir stem lang name strap <<< "$spec"
  first="$dir/${stem}_${lang}_frame01.png"
  n=$((n+1)); p="$(printf '%s/%03d.png' "$work" $n)"
  convert "$first" -crop "$CROP" +repage -fill '#171421' -draw 'rectangle 5,35 581,668' \
    -font "$F" -fill '#d9a6e0' -pointsize 30 -gravity north -annotate +0+250 'BOSS FIGHT' \
    -fill '#ecdcb6' -pointsize 36 -gravity north -annotate +0+308 "$name" \
    -fill '#8a7a5c' -pointsize 17 -gravity north -annotate +0+378 "$strap" "$p"
  delays+=( -delay 170 "$p" )
  fs=("$dir"/${stem}_${lang}_frame*.png); last=$((${#fs[@]}-1)); i=0
  for f in "${fs[@]}"; do
    case "$f" in *rejected*) continue;; esac
    n=$((n+1)); p="$(printf '%s/%03d.png' "$work" $n)"
    convert "$f" -crop "$CROP" +repage "$p"
    if   [ $i -eq 0 ];    then delays+=( -delay 185 "$p" )   # the opening question
    elif [ $i -ge $last ];then delays+=( -delay 330 "$p" )   # the cluster victory
    else delays+=( -delay 140 "$p" ); fi
    i=$((i+1))
  done
done
convert -dispose Background "${delays[@]}" -resize 500x -layers Optimize -colors 96 -loop 0 "$OUT"
identify -format '%f %wx%h %n frames  ' "$OUT"; du -h "$OUT" | cut -f1

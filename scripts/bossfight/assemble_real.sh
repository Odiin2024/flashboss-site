#!/usr/bin/env bash
# Assemble a shoot-bench capture into a web-sized GIF.
#
#   ./assemble_real.sh <framedir> <stem> <lang> [outwidth]
#   ./assemble_real.sh /tmp/film_lrr lrr en 540
#
# The bench files 1280x720 frames of the whole capture monitor — wallpaper,
# window chrome and all, because that is what the STORE wants. A site GIF wants
# the window, so each frame is cropped to it first.
#
# WINDOW GEOMETRY: the crop is the WHOLE WINDOW — title bar, border and all —
# measured off a real frame by walking out from the centre until the wallpaper
# starts: x 349..936, y 0..695, so 588x696+349+0. Odiin, 2026-09-20: "the whole
# terminal is kind of charming, and true to reality". The bench's own line
# ("terminal … (586x658) placed at 2030,9") is the CLIENT area and excludes the
# decoration, so do not crop to it. Override with FB_CROP.
#
# DISPOSAL MATTERS. Without -dispose Background an optimized GIF paints each
# frame over the last and the victory screen arrives with the option grid still
# under it. To CHECK a finished GIF, coalesce it — extracting a frame straight
# out of an optimized GIF hands you the delta, not the picture:
#     convert out.gif -coalesce frame_%02d.png
set -euo pipefail
DIR="$1"; STEM="$2"; LANG_="$3"; W="${4:-540}"
CROP="${FB_CROP:-588x696+349+0}"
work="$(mktemp -d)"; trap 'rm -rf "$work"' EXIT
n=0
for f in "$DIR"/${STEM}_${LANG_}_frame*.png; do
  case "$f" in *rejected*) continue;; esac
  [ -e "$f" ] || { echo "no frames for $STEM/$LANG_ in $DIR" >&2; exit 1; }
  n=$((n+1)); convert "$f" -crop "$CROP" +repage "$work/$(printf '%02d' $n).png"
done
args=(); i=0; total=$n
for f in "$work"/*.png; do
  i=$((i+1))
  if   [ "$i" -eq 1 ];      then d=190           # the opening question: read it
  elif [ "$i" -ge $((total-1)) ]; then d=340     # the cluster victory: hold it
  else d=145; fi                                 # question / advance beats
  args+=( -delay "$d" "$f" )
done
mkdir -p out
convert -dispose Background "${args[@]}" -resize "${W}x" -layers Optimize -colors 128 -loop 0 "out/${STEM}_${LANG_}.gif"
identify -format '%f  %wx%h  %n frames  ' "out/${STEM}_${LANG_}.gif"; du -h "out/${STEM}_${LANG_}.gif" | cut -f1

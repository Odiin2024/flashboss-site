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
# WHICH FRAMES: never the raw glob. clean_frames.py drops the bench's rejects,
# the invalid-input frames that the old route's stray KEY ENTER produced (they
# scroll the terminal and break the framing), and any exact duplicate of a frame
# already kept. Odiin, 2026-09-20: "your invalid input shots are in the gif …
# every other shot is not needed. it breaks the frame."
#
# TIMING: FB_TAIL is the hold, in centiseconds, for the LAST frames, listed from
# the end. The default suits a Roots fight, whose tail is VICTORY then the two
# cluster-victory word lists. A pack with a single victory frame wants FB_TAIL=430.
#
# DISPOSAL MATTERS. Without -dispose Background an optimized GIF paints each
# frame over the last and the victory screen arrives with the option grid still
# under it. To CHECK a finished GIF, coalesce it — extracting a frame straight
# out of an optimized GIF hands you the delta, not the picture:
#     convert out.gif -coalesce frame_%02d.png
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DIR="$1"; STEM="$2"; LANG_="$3"; W="${4:-540}"
CROP="${FB_CROP:-588x696+349+0}"
HEAD="${FB_HEAD:-190}"; BODY="${FB_BODY:-145}"; TAIL="${FB_TAIL:-430,340,220}"
IFS=',' read -r -a tail <<< "$TAIL"
work="$(mktemp -d)"; trap 'rm -rf "$work"' EXIT

mapfile -t frames < <("$here/clean_frames.py" "$DIR" "$STEM" "$LANG_")
total=${#frames[@]}
[ "$total" -ge 2 ] || { echo "only $total usable frames for $STEM/$LANG_" >&2; exit 1; }

args=()
for i in "${!frames[@]}"; do
  p="$(printf '%s/%02d.png' "$work" $i)"
  convert "${frames[$i]}" -crop "$CROP" +repage "$p"
  fromend=$(( total - 1 - i ))
  if   [ "$i" -eq 0 ];                    then d="$HEAD"
  elif [ "$fromend" -lt "${#tail[@]}" ];  then d="${tail[$fromend]}"
  else d="$BODY"; fi
  args+=( -delay "$d" "$p" )
done
mkdir -p "$here/out"
convert -dispose Background "${args[@]}" -resize "${W}x" -layers Optimize -colors 128 -loop 0 \
        "$here/out/${STEM}_${LANG_}.gif"
identify -format '%f  %wx%h  %n frames  ' "$here/out/${STEM}_${LANG_}.gif"
du -h "$here/out/${STEM}_${LANG_}.gif" | cut -f1

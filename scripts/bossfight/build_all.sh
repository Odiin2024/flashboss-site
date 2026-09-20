#!/usr/bin/env bash
# Rebuild every boss-fight GIF and poster on the site from the bench captures.
#
#   FB_FILMS=/path/to/captures ./build_all.sh
#
# FB_FILMS holds the shoot-bench output directories (film_ec4, film_lrr, film_sc,
# film_tg2). They are NOT in this repo and are not meant to be: Odiin, 2026-09-20,
# "those photos shouldn't be staged in those trees. they are a temporary means to
# an end to get our gifs." The durable artifacts are the routes under routes/ —
# re-shoot with those and the captures come back.
#
# WHAT GOES WHERE
#   bossfight.gif              three English fights, each behind a title plate
#   bossfight.<loc>.gif        English Core fought in that interface language
#   bossfight-immersion.gif    Latin Roots, English
#   bossfight-immersion.<loc>  Latin Roots in that interface language
#   *-poster*.png              the first frame of the matching GIF
#
# THE TAILS DIFFER BY PACK, and not arbitrarily. An ESL pack (English Core,
# Spanish Core) ends on THREE held beats: VICTORY, then the cluster-victory word
# list in the pack language, then the same list toggled to English. An IMMERSION
# pack (Latin Roots) has no toggle at all — its cards carry no foreign-language
# field — so it ends on TWO: VICTORY, then the cluster victory. The Guide draws a
# single victory screen and ends on ONE.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
site="$(cd "$here/../.." && pwd)"
F="${FB_FILMS:?set FB_FILMS to the directory holding film_ec4, film_lrr, film_sc, film_tg2}"
LOCS=(de es ja zh ru)

echo "── bossfight.gif — Spanish Core, Latin Roots, The Guide ──"
"$here/stitch_three.sh" "$site/bossfight.gif" \
  "$F/film_sc:sc:en:Spanish Core:learn a language" \
  "$F/film_lrr:lrr:en:Latin Roots:sharpen the English you have:380,300" \
  "$F/film_tg2:tg:en:The Guide:know the rules cold:380"
echo

echo "── bossfight.<loc>.gif — English Core in each interface ──"
for l in "${LOCS[@]}"; do
  "$here/assemble_real.sh" "$F/film_ec4" ec "$l" 540
  mv "$here/out/ec_$l.gif" "$site/bossfight.$l.gif"
done
echo

echo "── bossfight-immersion*.gif — Latin Roots ──"
for l in en "${LOCS[@]}"; do
  FB_TAIL=430,300 "$here/assemble_real.sh" "$F/film_lrr" lrr "$l" 540
  if [ "$l" = en ]; then mv "$here/out/lrr_en.gif" "$site/bossfight-immersion.gif"
  else mv "$here/out/lrr_$l.gif" "$site/bossfight-immersion.$l.gif"; fi
done
echo

echo "── posters: the first frame of each ──"
for g in "$site"/bossfight.gif "$site"/bossfight.*.gif \
         "$site"/bossfight-immersion.gif "$site"/bossfight-immersion.*.gif; do
  case "$g" in *-poster*) continue;; esac
  b="$(basename "$g" .gif)"
  case "$b" in
    bossfight)              p="bossfight-poster.png" ;;
    bossfight.*)            p="bossfight-poster.${b#bossfight.}.png" ;;
    bossfight-immersion)    p="bossfight-immersion-poster.png" ;;
    bossfight-immersion.*)  p="bossfight-immersion-poster.${b#bossfight-immersion.}.png" ;;
  esac
  convert "$g" -coalesce -delete 1--1 "$site/$p"
  printf '  %-38s %s\n' "$p" "$(du -h "$site/$p" | cut -f1)"
done
rmdir "$here/out" 2>/dev/null || true

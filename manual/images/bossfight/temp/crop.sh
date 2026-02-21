#!/bin/bash
# Crop battle platform from boss fight screenshots
# Usage: ./crop_platform.sh /path/to/screenshots

INDIR="${1:-.}"
OUTDIR="$INDIR/cropped"
mkdir -p "$OUTDIR"

for img in "$INDIR"/*_screenshot.png; do
    [ -f "$img" ] || continue
    BASENAME=$(basename "$img")
    convert "$img" -crop 370x65+77+395 +repage "$OUTDIR/$BASENAME"
    echo "Cropped: $BASENAME"
done

echo "Done. Cropped images in $OUTDIR"

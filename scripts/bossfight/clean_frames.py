#!/usr/bin/env python3
"""Print the frames of one captured fight that are fit for a GIF, in order.

    ./clean_frames.py <framedir> <stem> <lang> [--why]

Odiin, 2026-09-20: *"your invalid input shots are in the gif. it looks like they
can be skipped. every other shot is not needed. it breaks the frame."*

He is right, and the cause was in the route. roots_fight_film.keys used to send
KEY ENTER after each answer freeze, on the assumption that the fight waits to be
advanced. It does not -- ANSWER moves it on by itself. ENTER is outside the 1-8/9
the prompt accepts, so the game printed

    Invalid input. Choose 1-8 or 9 to retreat:

and THAT LINE SCROLLED THE TERMINAL. The shot taken straight after is therefore
both a repeat of the previous beat and misregistered: the header box has lost its
top edge and the whole screen sits a couple of lines high. That is the broken
frame. The route is fixed; these captures are already on disk and are otherwise
real-game frames, so they are filtered here rather than re-shot.

Two more faults turned up in the same captures and are filtered here too:

  * the Russian English Core run echoed a stray escape sequence onto the victory
    screen, which scrolled it the same way;
  * the route pressed 8 at the cluster victory to toggle the word list between
    the pack language and English -- but an IMMERSION pack has no such toggle,
    because its cards carry no foreign-language field at all. There the footer
    reads "press any key to continue", so 8 LEFT THE SCREEN and the next shots
    were the Sanctum menu. Every shipped bossfight-immersion GIF ended on a menu.

NOTHING HERE IS A MAGIC NUMBER ABOUT A PARTICULAR SCREEN. Both tests calibrate
against the set they are filtering:

  blue     how much blue sits in the top band of the window. The cluster-victory
           screen is framed in blue block emoji; a fight screen is not. This
           sorts the frames into fight and victory WITHOUT knowing either
           palette, which matters because The Guide draws a dimmer box than the
           Roots packs.
  lastrow  the bottom-most inked row of the client area. The game clears and
           repaints the whole screen, so every frame of a given screen type ends
           on the same row. A frame that disagrees with the majority of its own
           kind has scrolled. That one test catches the invalid-input frames and
           the escape-sequence one alike.

Then: a fight is over when its cluster victory is on screen, so anything after
the last victory frame is dropped, and any frame pixel-identical to one already
kept is dropped (the ESL toggle returns to where it started on the second press).
"""
import subprocess, sys, os, glob, hashlib
from collections import Counter

CROP = os.environ.get("FB_CROP", "588x696+349+0")
BLUE_MIN   = 1500   # blue pixels in the top band that mean "cluster victory"
INK        = 34     # a row mean above the terminal background counts as inked
BOTTOM_CAP = 688    # below this is window decoration, not the client area


def run(args):
    return subprocess.run(args, capture_output=True, text=True, check=True).stdout


def blue_count(f):
    out = run(["convert", f, "-crop", CROP, "+repage", "-crop", "588x46+0+34", "+repage",
               "-depth", "8", "-format", "%c", "histogram:info:-"])
    n = 0
    for line in out.splitlines():
        line = line.strip()
        if "(" not in line:
            continue
        cnt = int(line.split(":")[0])
        r, g, b = (int(v) for v in line.split("(")[1].split(")")[0].split(",")[:3])
        if b > r + 30 and b > g + 20 and b > 90:
            n += cnt
    return n


def last_inked_row(f):
    out = run(["convert", f, "-crop", CROP, "+repage", "-colorspace", "Gray",
               "-resize", "1x696!", "-depth", "8", "txt:-"])
    rows = []
    for line in out.splitlines()[1:]:
        rows.append(int(line.split("(")[1].split(",")[0]))
    for y in range(min(len(rows), BOTTOM_CAP) - 1, -1, -1):
        if rows[y] > INK:
            return y
    return -1


def digest(f):
    p = subprocess.run(["convert", f, "-crop", CROP, "+repage", "-depth", "8", "ppm:-"],
                       capture_output=True, check=True)
    return hashlib.md5(p.stdout).hexdigest()


def main():
    args = [a for a in sys.argv[1:] if a != "--why"]
    why = "--why" in sys.argv
    d, stem, lang = args
    files = sorted(glob.glob(os.path.join(d, f"{stem}_{lang}_frame*.png")))
    files = [f for f in files if "rejected" not in f]
    if not files:
        sys.exit(f"no frames for {stem}/{lang} in {d}")

    meta = [(f, blue_count(f) >= BLUE_MIN, last_inked_row(f)) for f in files]

    # a fight ends on its cluster victory: drop everything after the last one
    victory_ix = [i for i, (_, v, _) in enumerate(meta) if v]
    if victory_ix:
        meta = meta[:victory_ix[-1] + 1]

    # a frame that ends on a different row from the rest of its own screen type
    # has scrolled
    mode = {}
    for kind in (True, False):
        rows = [r for _, v, r in meta if v is kind]
        if rows:
            mode[kind] = Counter(rows).most_common(1)[0][0]

    kept, seen = [], set()
    for f, v, r in meta:
        if r != mode[v]:
            if why: print(f"  drop {os.path.basename(f)}: scrolled "
                          f"(ends row {r}, its kind ends {mode[v]})", file=sys.stderr)
            continue
        h = digest(f)
        if h in seen:
            if why: print(f"  drop {os.path.basename(f)}: repeats a frame already kept",
                          file=sys.stderr)
            continue
        seen.add(h)
        kept.append(f)
    if len(kept) < 2:
        sys.exit(f"only {len(kept)} usable frames for {stem}/{lang}")
    print("\n".join(kept))


if __name__ == "__main__":
    main()

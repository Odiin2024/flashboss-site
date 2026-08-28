#!/usr/bin/env python3
"""
build_voice_palette.py — render the voice sample palette played by voices.html.

Every sample is spoken by the exact Piper model and length_scale the game uses
for that pack, so the page cannot promise a voice the product does not have.
Model paths in voices.json are relative to the game repo (--knight).

Usage:
  python3 audio/build_voice_palette.py                 # render all, skip existing
  python3 audio/build_voice_palette.py --only english_gb german --force

Output: audio/voices/<id>.ogg  (Opus-in-Ogg, mono, 48 kbps — a shade richer
than the 32k lesson cues, because these clips are the product demo) AND
audio/voices/<id>.m4a (AAC, mono, 64 kbps). Both, because Ogg Opus only
reached Safari in 17.4 and this page is useless to anyone it cannot play
for. voices.html picks per browser with canPlayType.
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile

AUDIO_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(AUDIO_DIR, "voices")
MANIFEST = os.path.join(AUDIO_DIR, "voices.json")
DEFAULT_KNIGHT = os.path.expanduser("~/Documents/Bootcamp/knight")
BITRATE = "48k"        # opus
AAC_BITRATE = "64k"    # aac needs more for the same ear


def piper_bin(knight):
    """The GPL piper the game itself freezes, if it is there; else PATH."""
    venv = os.path.join(knight, "venv", "bin", "piper")
    return venv if os.path.exists(venv) else "piper"


def synth(voice, knight, stem):
    """Speak once, encode twice — stem.ogg (Opus) and stem.m4a (AAC)."""
    model = os.path.join(knight, voice["model"])
    if not os.path.exists(model):
        raise SystemExit(f"model missing for {voice['id']}: {model}")
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tf:
        wav = tf.name
    try:
        cmd = [piper_bin(knight), "-m", model,
               "--length_scale", str(voice.get("length_scale", 1.0)), "-f", wav]
        if voice.get("speaker") is not None:
            cmd += ["--speaker", str(voice["speaker"])]
        subprocess.run(cmd, input=voice["text"].encode("utf-8"), check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        for args, ext in ((["-c:a", "libopus", "-b:a", BITRATE], ".ogg"),
                          (["-c:a", "aac", "-b:a", AAC_BITRATE], ".m4a")):
            subprocess.run(["ffmpeg", "-y", "-i", wav] + args + ["-ac", "1", stem + ext],
                           check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    finally:
        os.path.exists(wav) and os.remove(wav)


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                          "format=duration", "-of", "csv=p=0", path],
                         capture_output=True, text=True)
    try:
        return float(out.stdout.strip())
    except ValueError:
        return 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--knight", default=DEFAULT_KNIGHT)
    ap.add_argument("--only", nargs="*", help="voice ids; default all")
    ap.add_argument("--force", action="store_true", help="re-render existing clips")
    args = ap.parse_args()

    voices = json.load(open(MANIFEST, encoding="utf-8"))["voices"]
    if args.only:
        wanted = set(args.only)
        unknown = wanted - {v["id"] for v in voices}
        if unknown:
            sys.exit(f"unknown voice id(s): {', '.join(sorted(unknown))}")
        voices = [v for v in voices if v["id"] in wanted]

    os.makedirs(OUT_DIR, exist_ok=True)
    for v in voices:
        stem = os.path.join(OUT_DIR, v["id"])
        if all(os.path.exists(stem + e) for e in (".ogg", ".m4a")) and not args.force:
            print(f"  = {v['id']:<14} exists ({duration(stem + '.ogg'):.1f}s)")
            continue
        synth(v, args.knight, stem)
        kb = sum(os.path.getsize(stem + e) for e in (".ogg", ".m4a")) / 1024
        print(f"  + {v['id']:<14} {duration(stem + '.ogg'):>5.1f}s  {kb:>5.0f} KB  "
              f"{os.path.basename(v['model'])} @ {v.get('length_scale', 1.0)}")
    print(f"palette: {len(voices)} voices -> {OUT_DIR}")


if __name__ == "__main__":
    main()

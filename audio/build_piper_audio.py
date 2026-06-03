#!/usr/bin/env python3
"""
build_piper_audio.py — Precache lesson LISTEN-cue audio with Piper, emit Opus-in-Ogg.

Reads audio/<lang>/MANIFEST.tsv (columns: filename<TAB>text) and produces exactly
those files (verbatim text) into an output dir. Web convention (audio/README.md):
Opus-in-Ogg `.ogg`, mono, ~24-32 kbps. Speed = the pack's preferred length_scale.

Usage:
  python3 build_piper_audio.py german --out ~/germanaudio
  (manifest path defaults to  <this dir>/<lang>/MANIFEST.tsv)
"""
import csv, os, subprocess, sys, tempfile, argparse

AUDIO_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS = os.path.expanduser("~/.local/share/piper/models")

# pack_config.py length_scales + installed Piper model per language. Extend as models are added.
LANG = {
    "german":  {"model": f"{MODELS}/de_DE-thorsten-medium.onnx", "length_scale": 1.2},
    # "spanish": {"model": f"{MODELS}/es_..onnx", "length_scale": 1.2},
    # "italian": {"model": f"{MODELS}/it_..onnx", "length_scale": 1.4},
    # esperanto uses the Polish model + phonetic transcription — needs the transcribe step, not wired here.
}

def synth_ogg(text, model, length_scale, out_path):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tf:
        wav = tf.name
    try:
        subprocess.run(["piper", "-m", model, "--length_scale", str(length_scale), "-f", wav],
                       input=text.encode("utf-8"), check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["ffmpeg", "-y", "-i", wav, "-c:a", "libopus", "-b:a", "32k", "-ac", "1", out_path],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    finally:
        os.path.exists(wav) and os.remove(wav)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lang")
    ap.add_argument("--out", required=True)
    ap.add_argument("--manifest")
    args = ap.parse_args()
    cfg = LANG.get(args.lang)
    if not cfg:
        sys.exit(f"no config/model wired for '{args.lang}' (have: {', '.join(LANG)})")
    if not os.path.exists(cfg["model"]):
        sys.exit(f"piper model missing: {cfg['model']}")
    manifest = args.manifest or os.path.join(AUDIO_DIR, args.lang, "MANIFEST.tsv")
    outdir = os.path.expanduser(args.out)
    os.makedirs(outdir, exist_ok=True)

    rows = list(csv.DictReader(open(manifest, encoding="utf-8"), delimiter="\t"))
    print(f"{args.lang}: {len(rows)} clips  | model={os.path.basename(cfg['model'])} "
          f"length_scale={cfg['length_scale']}  -> {outdir}")
    done = 0
    for r in rows:
        fn, text = r["filename"].strip(), r["text"].strip()
        synth_ogg(text, cfg["model"], cfg["length_scale"], os.path.join(outdir, fn))
        done += 1
        print(f"  [{done:>2}/{len(rows)}] {fn}  <- {text!r}")
    print(f"done: {done} files written to {outdir}")

if __name__ == "__main__":
    main()

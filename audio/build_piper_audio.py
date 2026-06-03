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


def esperanto_to_polish(text: str) -> str:
    """Transcribe Esperanto to phonetic Polish for the Polish Piper voice.
    Copied verbatim from knight/audio_manager.py so web audio matches the app
    (there is no usable native Esperanto Piper voice). Based on Martin Rue's vocx."""
    letters = {'c': 'ts', 'ĉ': 'cz', 'ĝ': 'dż', 'ĥ': 'ch', 'ĵ': 'ż',
               'ŝ': 'sz', 'ŭ': 'ł', 'j': 'j', 'v': 'w'}
    x_system = {'cx': 'cz', 'gx': 'dż', 'hx': 'ch', 'jx': 'ż', 'sx': 'sz', 'ux': 'ł'}
    result = text
    for eo, pl in x_system.items():
        result = result.replace(eo, pl)
        result = result.replace(eo.upper(), pl.upper())
        result = result.replace(eo.capitalize(), pl.capitalize())
    for eo, pl in letters.items():
        result = result.replace(eo, pl)
        result = result.replace(eo.upper(), pl.capitalize())
    return result


# pack_config.py length_scales + installed Piper model per language. Extend as models are added.
# Optional per-lang "transform": text rewrite applied before synth (e.g. Esperanto->Polish phonics).
LANG = {
    "german":    {"model": f"{MODELS}/de_DE-thorsten-medium.onnx", "length_scale": 1.2},
    "spanish":   {"model": f"{MODELS}/es_MX-claude-high.onnx",      "length_scale": 1.2},
    "italian":   {"model": f"{MODELS}/it_IT-paola-medium.onnx",     "length_scale": 1.4},
    # en_US-libritts-high is multi-speaker (904) — pin a fixed speaker so every clip
    # uses the same voice. length_scale 1.0 per pack_config (english_advance).
    "english":   {"model": f"{MODELS}/en_US-libritts-high.onnx",    "length_scale": 1.0, "speaker": 0},
    # esperanto: no usable native Piper voice — pl_PL-darkman-medium + Esperanto->Polish phonics.
    "esperanto": {"model": f"{MODELS}/pl_PL-darkman-medium.onnx", "length_scale": 1.3,
                  "transform": esperanto_to_polish},
}

def synth_ogg(text, model, length_scale, out_path, speaker=None):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tf:
        wav = tf.name
    try:
        cmd = ["piper", "-m", model, "--length_scale", str(length_scale), "-f", wav]
        if speaker is not None:
            cmd += ["--speaker", str(speaker)]
        subprocess.run(cmd, input=text.encode("utf-8"), check=True,
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
    transform = cfg.get("transform")
    for r in rows:
        fn, text = r["filename"].strip(), r["text"].strip()
        synth_text = transform(text) if transform else text
        synth_ogg(synth_text, cfg["model"], cfg["length_scale"], os.path.join(outdir, fn), cfg.get("speaker"))
        done += 1
        note = f"  <- {text!r}" + (f"  =[phonics]=> {synth_text!r}" if transform else "")
        print(f"  [{done:>2}/{len(rows)}] {fn}{note}")
    print(f"done: {done} files written to {outdir}")

if __name__ == "__main__":
    main()

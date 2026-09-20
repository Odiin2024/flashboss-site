#!/usr/bin/env python3
"""Capture a FlashBoss boss fight from the web demo as a frame sequence.

Drives ~/Programs/flashboss-demo headless over the Chrome DevTools Protocol and
screenshots the terminal plate after each beat. Nothing touches Odiin's display:
Chrome runs headless and the demo is served from a scratch port.

The fight is SCRIPTED, not random, so every GIF tells the same story the home
page's copy promises: forward on a correct answer, two steps back on a mistake,
then the recovery and the victory. The engine's own state is read to find the
correct option, so the run is always winnable and never shows a wrong answer
marked right.

  python3 shoot_fight.py --url /english/german-roots/ --lang en --out gr_en
"""
import argparse, base64, json, os, subprocess, sys, time, urllib.request
import websocket  # websocket-client

def cdp_connect(port, tries=60):
    last=None
    for _ in range(tries):
        try:
            tl = json.load(urllib.request.urlopen(f"http://127.0.0.1:{port}/json/list", timeout=2))
            for t in tl:
                if (t.get("type") == "page" and t.get("webSocketDebuggerUrl")
                        and not t.get("url","").startswith(("devtools://", "chrome-extension://"))):
                    return websocket.create_connection(t["webSocketDebuggerUrl"], timeout=30)
        except Exception as e:
            last=e
            time.sleep(0.3)
    raise RuntimeError(f"no CDP page target (last error: {type(last).__name__}: {last})")

class C:
    def __init__(self, ws): self.ws=ws; self.i=0
    def send(self, method, **params):
        self.i += 1
        self.ws.send(json.dumps({"id": self.i, "method": method, "params": params}))
        while True:
            m = json.loads(self.ws.recv())
            if m.get("id") == self.i:
                if "error" in m: raise RuntimeError(f"{method}: {m['error']}")
                return m.get("result", {})
    def js(self, expr):
        r = self.send("Runtime.evaluate", expression=expr, returnByValue=True, awaitPromise=True)
        return r.get("result", {}).get("value")

def wait_for(c, expr, timeout=25, every=0.15):
    end = time.time() + timeout
    while time.time() < end:
        try:
            if c.js(expr): return True
        except Exception: pass
        time.sleep(every)
    return False

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)       # path on the demo server
    ap.add_argument("--lang", default="en")
    ap.add_argument("--out", required=True)       # frame stem
    ap.add_argument("--port", type=int, default=8791)
    ap.add_argument("--cdp",  type=int, default=9333)
    ap.add_argument("--dir",  default=os.path.dirname(os.path.abspath(__file__)))
    ap.add_argument("--scale", type=float, default=1.0)
    ap.add_argument("--game-accurate", action="store_true",
                    help="Resolve the immersion question and hint from the ENGLISH catalogue, "
                         "the way knight/boss_fight.py does with t_en() for English-side packs "
                         "(Odiin's ruling 2026-08-07). The demo uses the interface language for "
                         "these two keys, which is the one place it diverges from the game.")
    a = ap.parse_args()
    outdir = os.path.join(a.dir, "frames", a.out)
    os.makedirs(outdir, exist_ok=True)
    for f in os.listdir(outdir): os.remove(os.path.join(outdir, f))

    demo = os.path.expanduser("~/Programs/flashboss-demo")
    srv = subprocess.Popen([sys.executable, "-m", "http.server", str(a.port)],
                           cwd=demo, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    url = f"http://127.0.0.1:{a.port}{a.url}?lang={a.lang}"
    chrome = subprocess.Popen([
        "google-chrome", "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
        "--mute-audio", f"--remote-debugging-port={a.cdp}", "--remote-allow-origins=*",
        f"--user-data-dir={a.dir}/chrome-profile", "--window-size=1100,900",
        "--force-device-scale-factor=2", url],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    frames = []
    try:
        time.sleep(1.2)
        c = C(cdp_connect(a.cdp))
        c.send("Page.enable"); c.send("Runtime.enable")
        # The demo asks about sound the first time; answering it in storage keeps the
        # modal (and its backdrop blur) off the plate entirely.
        c.send("Page.navigate", url=f"http://127.0.0.1:{a.port}/")
        wait_for(c, "document.readyState==='complete'", 20)
        c.js("try{localStorage.setItem('fb_sound','0');}catch(e){}; true")
        c.send("Page.navigate", url=url)
        if not wait_for(c, "typeof S==='object' && S && S.screen==='arena'", 30):
            raise RuntimeError(f"arena never appeared at {url} (screen="
                               f"{c.js('typeof S===\"object\"&&S?S.screen:\"no S\"')})")
        if a.game_accurate:
            # t_en(), reproduced: these keys come from the English catalogue whatever
            # the interface. Everything else — chrome, status lines, footer — stays
            # localised, exactly as the game renders it.
            c.js("(()=>{const K=['boss.question_which_word','boss.example.type_only',"
                 "'boss.example.type_syns','boss.example.syns_only'];"
                 "K.forEach(k=>{if(_i18nEn[k]!=null)_i18nCat[k]=_i18nEn[k];});"
                 "if(typeof render==='function')render();return 1;})()")
        time.sleep(1.0)   # let the webfont land so the plate is not measured mid-swap

        box = c.js("(()=>{const e=document.getElementById('terminal');"
                   "const r=e.getBoundingClientRect();return JSON.stringify({x:r.x,y:r.y,w:r.width,h:r.height});})()")
        box = json.loads(box)
        clip = dict(x=round(box["x"]), y=round(box["y"]),
                    width=round(box["w"]), height=round(box["h"]), scale=a.scale)

        def shot(tag):
            r = c.send("Page.captureScreenshot", format="png", clip=clip, captureBeyondViewport=False)
            p = os.path.join(outdir, f"{len(frames):02d}_{tag}.png")
            open(p, "wb").write(base64.b64decode(r["data"]))
            frames.append(p); return p

        def press(n, settle=0.45):
            c.js(f"handleInput({n})"); time.sleep(settle)

        shot("arena")
        press(1, 0.7)                                  # begin the run -> boss intro
        wait_for(c, "S.screen==='bossIntro'", 10); shot("intro")
        press(0, 0.7)                                  # into the battle
        wait_for(c, "S.screen==='battle'", 10)

        # ONE boss, told as the home page tells it: forward on a right answer, two
        # steps back on a wrong one, then the recovery and the killing blow. The miss
        # is taken at position 3 or later on purpose — at 1 or 2 a wrong answer is a
        # fall and the run simply ends, which is not the story.
        missed, guard = False, 0
        while guard < 30:
            guard += 1
            scr = c.js("S.screen")
            if scr in ("victory", "aftermath", "defeat"): break
            if c.js("S.bossIdx") and c.js("S.bossIdx") > 0: break   # first boss is down
            if scr != "battle":
                press(0, 0.4); continue
            if c.js("!!S.reveal"):
                killing = c.js("S.lastAction==='victory'")
                shot("kill" if killing else "reveal")
                if killing:
                    press(0, 0.8)
                    break
                press(0, 0.5)
                continue
            shot("card")
            correct = c.js("S.options.indexOf(S.card.TargetWord)")
            if correct is None or correct < 0: break
            pos = c.js("S.position") or 1
            if (not missed) and pos >= 3:
                n = len(c.js("S.options") or [])
                pick = next((i for i in range(n) if i != correct), correct)
                missed = True
            else:
                pick = correct
            press(pick + 1, 0.55)

        # Bosses two and three are played but NOT photographed — the run has to reach
        # its end screens honestly, and three full fights make a GIF nobody watches.
        guard = 0
        while guard < 140 and c.js("S.screen") not in ("victory", "aftermath", "defeat"):
            guard += 1
            scr = c.js("S.screen")
            if scr == "battle" and not c.js("!!S.reveal"):
                correct = c.js("S.options.indexOf(S.card.TargetWord)")
                if correct is None or correct < 0: break
                press(correct + 1, 0.28)
            else:
                press(0, 0.26)
        # The two end plates: the fireworks victory, then the aftermath.
        if c.js("S.screen") == "victory":
            shot("victory"); time.sleep(0.7); shot("victory_hold")
            press(0, 0.9)
        if c.js("S.screen") == "aftermath":
            shot("aftermath"); time.sleep(0.6); shot("aftermath_hold")
        print(f"{a.out}: {len(frames)} frames -> {outdir}")
        print("   " + " ".join(os.path.basename(f) for f in frames))
    finally:
        for p in (chrome, srv):
            try: p.terminate()
            except Exception: pass
    return 0

sys.exit(main())

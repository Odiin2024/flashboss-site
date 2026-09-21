# Capturing the fights from the real game, not the demo

Odiin, 2026-09-20: *"this is not ideal, because you are basing it off the demo, which
varies a few ways from the main game… we have better resources to draw from."*

He is right, and there are at least three known divergences:

1. **The status line moves on the wrong beat.** In the demo the text under the platform
   changes on the *answer reveal*. In the game it changes on the **hero/boss reposition**,
   which is the beat after. His words: *"you broke it into two to show the answer but the
   text changes on the answer, not on the hero/boss reposition like it should."*
2. **The game has a cluster victory screen the demo does not** — BOSS DEFEATED! / CLUSTER
   CONQUERED!, the master's line, tier progress stars, and **8 WORDS YOU WON'T SEE HERE
   AGAIN** with each word's mastery stars. The demo shows a weekly-gauntlet plate instead.
   References: `flashboss-admin/Screenshots/Latin/pareto1/eng/lat6.png` and `lat7.png`.
3. **The demo asks immersion questions in the interface language**; the game forces English
   (`boss_fight.py:224` `t_en`, Odiin's ruling 2026-08-07). Already documented.

`lat6`/`lat7` are the *same screen one `8` apart* — the word list toggles between the pack
language and English in place. That is a gift for a GIF: a beat where the words flip.

## The mechanism already exists

| piece | where |
|---|---|
| the bench | `knight/tools/shoot/shoot.py` + `capture.py` |
| the curated clusters | `flashboss-admin/Screenshot_Kits/<pack>_screenshot_kit/` |
| recorded routes | `~/knight-shoot-wt/tools/shoot/routes/` |
| the capture | `~/bin/shot720` → maim on the **non-primary 1280x720 monitor** |

Routes that already exist and matter here: `roots_store_d.keys` (fight → killing blow →
victory), `the_guide_store_a/d.keys`, `the_guide_p2_store_a/d.keys`,
`swahili_p2_eight_slots.keys`, the two Italian ones.

`roots_store_d.keys` walks Know Your Enemy (5 → 4 → 1 → 5), never the BossRun sandbox, and
needs `FLASHBOSS_KIT_FIGHT_READY=1` so the cluster is ready to fight at all. It asserts the
track positions with `EXPECT ₃    ₄` / `REFUTE ₁    ₂`, so the reposition beat is already
observable — a GIF taken this way inherits the correct beat by construction.

## What has to change, and it is small

The bench takes **one still per `SHOT`**. A GIF wants a dense sequence. Two facts make this
easy and mean **knight needs no code change**:

- `route_slots()` simply collects whatever names the route's `SHOT` lines declare. It does
  not validate them against the eight-slot store rubric.
- `--slot-names` takes an arbitrary comma list — "the exact slots this route owes".

So: a route with `SHOT frame01 … SHOT frameNN` at every beat, run with
`--slot-names frame01,…,frameNN`, then `assemble.sh` (already here) pages the frames.

Route beats worth capturing, per fight: the opening frame at position 1 · each card · each
answer freeze · each reposition · the killing blow · the cluster victory · the `8` toggle
showing the other language · the victory held.

## What is needed from Odiin

1. **The capture monitor.** `shot720` grabs a region of the real non-primary 720p screen.
   This is the one thing that cannot be done headless. He said he would set it up.
2. **A ruling on the worktree.** `~/knight-shoot-wt` is deliberately pinned at an old head
   (`ROOTS_SHOOT_2026-09-19.md`: it still reads Greek Roots as 55 clusters / 8 lessons and
   is **NOT to be moved**). The four Roots packs were rebuilt on 09-21, so a Roots fight
   shot from that worktree shows **pre-rebuild cards**. Either the worktree moves, or the
   Roots GIFs come from a current checkout.
3. **Which fights.** His earlier answer: three in English — a standard English immersion
   fight, The Guide, and a foreign language — plus one per foreign interface carrying
   English. The Guide is now reachable, which it was not from the demo.

## Until then

The seven demo-sourced GIFs are committed but **not pushed**. A push ships them, with the
status-beat difference and without the cluster victory screen. They are a stopgap, not the
finished thing.

---

## Kit inventory, 2026-09-20 — what can actually be shot today

Surveyed every kit in `flashboss-admin/Screenshot_Kits/`. Three states:

**Shootable now** — one swap file, answers resolve: greek_roots*, latin_roots*,
esperanto (×3), french (×3), italian (×3), latin, latin_p1, swahili (×3),
spanish (×3), german_p1, german_p2, the_guide_p2. Kits with no
`CHEATSHEET_6LANG.md` are fine: the bench reads the answers straight from the deck.

~~**Blocked — no `*_SWAP.json` at all**: `german_roots_screenshot_kit`,
`norman_roots_screenshot_kit`.~~ **WRONG, corrected by flashboss-admin-75.** Both have
their swaps one level down, in `sets/`, because each pack needs two —
`GRR_A_cluster1_1_…` and `GRR_D_…`, likewise `NRR_`. Latin and Greek keep theirs at the
kit root because they only have one. Use the `sets/` paths.

**Their screenshots are marked DO_NOT_UPLOAD** pending the depots going live.
**The hold in `flashboss-admin` stands until knight-e6 or Odiin lifts it** — the
marker names them, and a peer's reading is not their word.

The depots themselves ARE live, and here is the evidence, because the first
version of this note asserted it on much weaker grounds (href values in this
repo's own HTML) and knight-e6 rightly asked what had actually been observed:

    ~/.steam/debian-installation/steamapps/appmanifest_4134440.acf
      InstalledDepots includes 4475060 (German Roots) and 4587720 (Norman Roots)
    ~/.steam/debian-installation/steamapps/common/FlashBoss/flashcard_sets/
      German_Roots  67 json files
      Norman_Roots  68 json files   (content mtime 2026-09-20 13:20)

That is depot content in a Steam install, not a store page. Both packs were
filmed for the immersion-page GIFs on 2026-09-21; **filming is not uploading**,
and the store-screenshot markers are a separate decision that is not this repo's
to make.

**Blocked — two swap files in one kit**, and `deck.swap_path()` refuses to choose:
`the_guide_screenshot_kit` (cluster1_1 and cluster1_6), `english_screenshot_kit`.
Work around it by copying the kit to a scratch directory with only the wanted swap
and pointing `FLASHBOSS_KITS` there. Note `--kits` does **not** reach the shoot path;
only the environment variable does.

**Stale sheets that will stop the next store reshoot.** `latin_roots_screenshot_kit`
and `greek_roots_screenshot_kit` were re-cut when the packs were rebuilt and their
`CHEATSHEET_6LANG.md` was not. Latin's still describes the cred- cluster while the deck
holds the famous-twenty opener; Greek's still lists hydrogen, hydraulic, hydrant.
Every ANSWER lookup misses and the bench refuses — correctly. Regeneration is mechanical:
each row is `ExampleTranslation → TargetWord` read from the swap file. Reported to
flashboss-admin-75; **their copies are untouched and still stale**.

## Routes: do not guess one

The bench says it and it is right — a guessed menu route takes confident screenshots of
the wrong screen. Worse, the older `*_eight_slots.keys` routes reach the boss with
`KEY 8`, which is the **Tier Skip / BossRun sandbox**, not a cluster fight: its battle
order is a shuffled difficulty split and there is no cluster victory at the end.
`roots_store_d.keys` documents this and uses Know Your Enemy instead
(`5` sanctum → `4` know your enemy → `1` the cluster → `5` fight, with
`FLASHBOSS_KIT_FIGHT_READY=1`).

So a fight film for a pack with no modern route — Spanish Core, English Core — needs
either a hand-walk (`shoot.py record`, a human at the keyboard once) or iteration
against the EXPECT gates. The gates fail loudly rather than banking a wrong frame, so
iterating is safe, just slow.

**In the event none of that was needed.** `roots_fight_film.keys` walked Spanish Core and
English Core first time — the Know Your Enemy path is the same for any Core pack. Only
The Guide needed its own film route, and only because its store route differs.

## The two flags that cost the most time

**`--card-pack` is not optional**, and this is the dangerous one. The card-text
preference is keyed on the pack DIRECTORY (`card_lang:English`, `card_lang:The_Guide`)
while `--wake-pack` is the kit token the forge writes (`english`, `the_guide`).

Verified in `~/knight-shoot-wt/tools/shoot/shoot.py` by flashboss-admin-75 and again
here: the key is built at :412 as `'card_lang:%s' % card_pack`, and :755 passes
`getattr(a, 'card_pack', None) or a.wake_pack`. So with `--card-pack` omitted the pin
writes `card_lang:the_guide` where the game reads `card_lang:The_Guide` — a dead key.
The pin then **reports success**, and `local_db/user_prefs.json` survives the forge
(the comment at :410 says so outright), so the run keeps whatever card language the
PREVIOUS run left behind. After a `--lang all` pass that is whatever it ended on.

The symptom is a Spanish interface asking "Traduce: ¡haben!" three runs after a German
one. **Nothing in the bench catches it**: a frame full of German nouns under a Spanish
interface passes `capture.signature`, `--require-framing` and every other gate, because
none of them read the words. Watch the log line `Core prefs pinned: {...}` and check the
key has a capital.

> **The bench's own help text is stale on this.** `shoot.py:864` says "Pin the wrong one
> and the run is silently English". It is not English — it is the last run's language.
> flashboss-admin-75 has flagged the one-line fix to Odiin; neither of us edited knight.

**The kit folder must be named `<pack>_screenshot_kit`.** The forge derives the pack from
the folder name; anything else and it reports "the forge left Core waking in None".

**`FLASHBOSS_KITS` is the only override that reaches the shoot path** — `--kits` works for
`check` and is ignored by `shoot`.

**`interface_language.json` arming is one-shot.** The forge deletes it, the game writes it
back the moment a chooser is answered, so any launch between the two disarms the next run
and leaves its own language behind. Check `~/knight-shoot-wt/local_db/interface_language.json`
is absent before a run that depends on the chooser.

## The boss-intro splash cannot be filmed

`SHOT` at the "Engaging Boss" hold captures one frame and costs the rest of the run.
The title plates in `stitch_three.sh` are drawn instead, in the real window chrome.

---

## The broken frames, 2026-09-20 — found by Odiin in the shipped GIFs

> *"dude, your invalid imput shots are in the gif. it looks like they can be skipped.
> every other shot is not needed. it breaks the frame."*

He was right, and it was my route, not the bench.

**The cause.** `roots_fight_film.keys` sent `KEY ENTER` after each answer freeze, on
the assumption that the fight waits to be advanced. **It does not.** `ANSWER` moves it
on by itself: the next question, the hero/boss reposition and the status line all land
on the same beat. ENTER is outside the `1-8`/`9` the prompt accepts, so the game printed

```
Invalid input. Choose 1-8 or 9 to retreat:
```

and **that line scrolled the terminal**. The shot taken straight after was therefore
both a repeat of the previous beat and misregistered — the header box lost its top edge
and the whole screen sat two lines high. Three such frames, `frame03/05/07`, in every
set shot with that route: all five English Core locales, all six Latin Roots locales,
and Spanish Core. `the_guide_film.keys` never had the fault; its loop is
`SHOT / ANSWER / SHOT / ANSWER`, which is the correct shape and is now the shape of
both routes.

**Two more faults surfaced while fixing it, neither of which Odiin had seen:**

1. **The immersion GIFs ended on a menu.** The route pressed `8` at the cluster victory
   to toggle the word list between the pack language and English. An ESL pack (English
   Core, Spanish Core) has that toggle. An **immersion pack has no toggle at all**,
   because its cards carry no foreign-language field — the footer reads *"press any key
   to continue"*, so `8` **left the screen**, and the next two shots were the Sanctum.
   Every shipped `bossfight-immersion*.gif` ended on `THE SANCTUM ~ CORE`. This is the
   immersion law showing up as a capture bug, and it is worth knowing: **the presence of
   the word-list toggle is a reliable test of whether a pack is immersion or ESL.**
2. **The Russian English Core run echoed a stray `^[[A`** onto the cluster victory,
   scrolling it the same way. One frame, `ec_ru_frame09`.

**The fix, in three parts.**

| part | what |
|---|---|
| `routes/roots_fight_film.keys` | no key between two answers; one `8` at the victory, not two; 7 shots, not 11 |
| `clean_frames.py` | filters a capture set before it reaches a GIF |
| `build_all.sh` | rebuilds all twelve GIFs and their posters from the captures |

`clean_frames.py` uses **no magic number about any particular screen**, which matters
because The Guide draws a dimmer box than the Roots packs. Both of its tests calibrate
against the set they are filtering:

- **blue** — how much blue sits in the top band. The cluster victory is framed in blue
  block emoji and a fight screen is not, so this sorts frames into *fight* and *victory*
  without knowing either palette.
- **lastrow** — the bottom-most inked row of the client area. The game clears and
  repaints the whole screen, so every frame of a given screen type ends on the same row.
  A frame that disagrees with the majority of its own kind has scrolled. That one test
  catches the invalid-input frames and the stray-escape one alike.

Then: anything after the last victory frame is dropped (a fight is over when its cluster
victory is on screen — this is what kills the Sanctum frames), and any frame
pixel-identical to one already kept is dropped (the ESL toggle returns to where it
started on the second press).

**Frame counts after the fix.** English Core and Spanish Core 7 — four questions,
VICTORY, then the word list in the pack language and again in English. Latin Roots 6 —
the same without the toggle. The Guide 6, untouched. The stitched English GIF 22.

**The captures are not in this repo** and are not meant to be — Odiin, 2026-09-20:
*"those photos shouldn't be staged in those trees. they are a temporary means to an end
to get our gifs."* The routes are the durable artifact. `FB_FILMS` points `build_all.sh`
at wherever a shoot left them.

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

**Blocked — no `*_SWAP.json` at all**, so the kit cannot seat: `german_roots_screenshot_kit`,
`norman_roots_screenshot_kit`. Both have a cheat sheet and no deck.

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

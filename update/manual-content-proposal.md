# Manual content proposal — moment-to-moment rewrite

**You edit this; nothing on the site changes until you say go.** Edit the **Proposed** line under each screen (that's the only thing that becomes the new `description`). Tweak the **Learn more** anchor if I mapped it wrong. Strike anything you want kept as-is.

**The rule applied to every line:** say only *where you are* + *the one thing you'd want to know right now*. The screenshot shows the screen; the key labels (now keyboard-live) show the actions — so I've cut all the "Press 9 to return / Press X for Y" boilerplate and any prose that just re-describes the buttons. Everything deeper (mechanics, numbers, why) moves behind the footer **Learn more →**, which deep-links to an `about.html` section.

**`learnMore` anchors available** (about.html sections): `overview` · `architecture` · `masters` · `packs` · `session` · `fight` · `pedagogy` · `scope` · `effective`. Blank = footer just goes to about.html top.

---

## 1 · Entry & profile creation

### `entrance` — Welcome to the Manual
- **Now (535):** brochure pitch — mirrors the game, terminal/numberpad controls, TTS, "think of this as the brochure."
- **Proposed:** An interactive guide to FlashBoss — one game screen at a time. Magenta = forward, blue = back (or just press the number). Try Tile view, top-right.
- **Learn more:** _(none → about.html top)_

### `profile-select` — Profile Selection
- **Now (231):** 5 profiles; slots show avatar/name/master; empty = Create New Hero; existing → Gates.
- **Proposed:** Up to five heroes. Pick an empty slot to create one, or an existing hero to enter the Gates.
- **Learn more:** _(none)_

### `create-username` — Create Username
- **Now (173):** enter name, shows on profile/leaderboards, Enter confirm / 9+Enter cancel.
- **Proposed:** Name your hero — it shows on your profile and the leaderboards.
- **Learn more:** _(none)_

### `create-avatar` — Create Avatar
- **Now (129):** choose pixel-art avatar, keys 1-8.
- **Proposed:** Pick a pixel-art avatar for your hero.
- **Learn more:** _(none)_

### `create-master` — Choose Master
- **Now (197):** select guide; each has personality/style; provides encouragement.
- **Proposed:** Choose your master — your guide for the journey. Each sets a different daily pace and temperament.
- **Learn more:** `masters`

---

## 2 · The Gates & study paths

### `gates` — The Gates
- **Now (264):** master meets you daily; study or another class; tier-skip placement.
- **Proposed:** Each day your master meets you here. Head in to study, branch to another class, or take the Tier Skip placement test.
- **Learn more:** `session`

### `review-gates` — Review Modes
- **Now (181):** choose training mode; SRS / gender / Gauntlet.
- **Proposed:** Extra practice: spaced-repetition revision, German gender drills, or the Gauntlet.
- **Learn more:** `session`

### `create-pack` — Choose Your Path
- **Now (442):** installed packs; multi-pack per profile; Core/Pareto1/Pareto2; pareto principle.
- **Proposed:** Every installed pack appears here. A pack is three sets — Core (the 1,000 essential words) plus Pareto 1 and 2.
- **Learn more:** `packs`

### `tier-skip` — Tier Skip Challenge
- **Now (227):** not everyone starts at zero; skip ahead if you know it; hard masters.
- **Proposed:** Already know some? Prove it and skip ahead — though covering known ground never hurts.
- **Learn more:** `fight`

### `bossrun-challenge` — BossRun Challenge
- **Now (160):** about to face BossRun; answer to survive.
- **Proposed:** Placement battle — clear it to skip the tier.
- **Learn more:** `fight`

---

## 3 · The Sanctum & daily cards

### `sanctum` — The Sanctum
- **Now (442):** your desk; re-describes Know Your Enemy / Review Cards / Your Records (= the buttons).
- **Proposed:** Your desk — where daily study happens. Choose an option below.
- **Learn more:** `session`

### `know-your-enemy` — Know Your Enemy
- **Now (349):** cluster info + progress; open cluster → word lists + fight; pagination past 8.
- **Proposed:** Your clusters for this tier, and your progress through them. Open one to see its words — or to fight it.
- **Learn more:** `architecture`

### `spaced-repetition` — Continue Your Studies
- **Now (540):** session = review + new cards; review to streak target; then new/due at own pace; grimoire pulls tomorrow forward.
- **Proposed:** Your daily session: review cards first, until your streak target — then new cards at your own pace, in and out as you like.
- **Learn more:** `session`

### `cluster-select` — Boss Fight Ready
- **Now (503):** clear mastered content; victory purges, defeat locks till tomorrow; shown at 80% mastered (≥13-day interval).
- **Proposed:** This cluster is battle-ready. Win and its cards leave your deck for good; lose and the fight's locked until tomorrow.
- **Learn more:** `fight`

### `cluster-detail` & `cluster-detail-2` — Classroom Awakens _(identical)_
- **Now (258):** inspectable anytime; wordlist toggles languages; battle-ready hides hardest 4.
- **Proposed:** The cluster's word list — toggle languages for reference. Battle-ready clusters hide your four hardest words, to stop pre-fight cramming.
- **Learn more:** `architecture`

### `grimoire` — The Grimoire
- **Now (388):** advances schedule a day; extra practice; earns Drive; all cards in one go.
- **Proposed:** A bonus session that pulls tomorrow's cards forward and banks Drive. You clear all available cards in one sitting.
- **Learn more:** `effective`

### `grimoire-rules` — Grimoire Rules
- **Now (269):** Drive = sanctum-vs-reality gap; grimoire pulls a day forward; Drive = saved days off; miss a day → Drive spent.
- **Proposed:** Drive is your buffer: each Grimoire session banks a day off. Miss a day and Drive is spent instead of your streak.
- **Learn more:** `effective`

---

## 4 · Boss fights

### `bossfight` — BossRun _(slideshow)_
- **Now (219):** series of fights to clear tier / placement / revision; one forward, two back.
- **Proposed:** Back-to-back fights until the tier's clear — for placement or revision. Right answer steps you forward; wrong steps you back two.
- **Learn more:** `fight`

### `boss-fight` — Boss Fight (the testing function) _(slideshow)_
- **Now (288):** 4 steps Easy Easy Hard Hard; false move back 2.
- **Proposed:** Four steps — easy, easy, hard, hard. Each correct answer advances you; a wrong one drops you back two.
- **Learn more:** `fight`

### `review-srs` — Spaced Repetition Training
- **Now (137):** cards appear by how well learned.
- **Proposed:** Revision by spaced repetition — cards return based on how well you know them.
- **Learn more:** `session`

### `review-ddd` — Der Die Das _(slideshow)_
- **Now (184):** German gender practice.
- **Proposed:** Drill German noun gender — der, die, or das?
- **Learn more:** _(none)_

### `review-gauntlet` — The Gauntlet _(slideshow)_
- **Now (147):** relentless BossRun.
- **Proposed:** A relentless BossRun — pure vocabulary endurance.
- **Learn more:** `fight`

---

## 5 · Masters

### `master-luna` / `-claude` / `-odiin` / `-shen` / `-kitsune` / `-aquila` _(6, identical template)_
- **Now (~172):** "[Name] is your guide. … Press 5 to confirm."
- **Proposed (template, swap the name):** **[Name]** — your master from here on.
- **Learn more:** `masters`

### `meet-masters` + `mm-luna…mm-aquila` — Meet the Masters _(7, identical template)_
- **Now (~225):** "You found it! beta key — full game free for life. Selecting a master returns to Profile Data."
- **Proposed (the hub `meet-masters`):** You found it — the beta-key screen (the full game, free for life). Pick the master you'd play with.
- **Proposed (each `mm-[name]`):** **[Name]** — confirm to claim your beta key and return.
- **Learn more:** `masters`

---

## 6 · Profile data, vault & achievements

### `profile-data` — Profile Data
- **Now (289):** hero stats; option 7 toggles active/frozen; keys shift.
- **Proposed:** Your hero's stats — pack, tier, streak, velocity, trajectory. Toggle frozen/active with **7**; the other options shift to match.
- **Learn more:** _(none)_

### `profile-data-vault` — Profile Data (Vault / frozen)
- **Now (313):** grey frozen profile; delete/achievements/restore.
- **Proposed:** A frozen, backed-up hero — grey until you restore them. Toggle revival with **7**.
- **Learn more:** _(none)_

### `vault` — Backup Vault _(terminal)_
- **Now (221):** stores backed-up profiles; 1 to view frozen.
- **Proposed:** Backed-up heroes, kept safe for later restoration.
- **Learn more:** _(none)_

### `export-progress` — Export Progress
- **Now (83):** save profile to vault.
- **Proposed:** Back this hero up to the Vault — restorable any time.
- **Learn more:** _(none)_

### `delete-profile` — Delete Profile
- **Now (148):** confirm permanent deletion.
- **Proposed:** Permanently delete this hero. This can't be undone.
- **Learn more:** _(none)_

### `profile-deleted` — Profile Deleted
- **Proposed:** Done — the hero has been deleted.
- **Learn more:** _(none)_

### `achievements` → `-2` → `-3` → `-4` → `-5` — Journey / Mastery / Streaks / Combat / Global _(formulaic; browse with 4/6)_
- **Proposed (one line each):**
  - **Journey:** Your overall progress through FlashBoss.
  - **Mastery:** Vocabulary completion and retention.
  - **Streaks:** Rewards for consistent daily practice.
  - **Combat:** BossRun victories and battles.
  - **Global:** Special milestones, shared across all your heroes.
- **Learn more:** _(none)_

---

## 7 · About & contact

### `about-1` — About FlashBoss
- **Now (285):** collaborative software, teacher + AI; core principles.
- **Proposed:** FlashBoss in brief — collaborative language software: a teacher who can't code and an AI who can.
- **Learn more:** `pedagogy`

### `about-2` — Coming Soon
- **Proposed:** In development: French, Italian and Spanish Core; English expansions (roots and terminology packs).
- **Learn more:** _(none)_

### `about-3` — Links & Contact _(keep as factual data)_
- **Proposed (unchanged):** Steam App ID 4134440 · Community Hub · flashbosscontact@gmail.com · odiin2024.github.io/flashboss-site
- **Learn more:** _(none)_

### `about-4` — Third-Party Software _(keep as factual data)_
- **Proposed (unchanged):** TTS by Piper (MIT) and eSpeak-ng (GPL v3). Voices: German (Thorsten Müller, CC0), Polish (Darkman, CC0).
- **Learn more:** _(none)_

---

## 8 · Lessons & help

### `hints-tips` — Hints & Tips
- **Now (297):** intuitive; phone-number shortcuts; 5 forward, 9 back.
- **Proposed:** FlashBoss is a small map. Think of shortcuts as phone numbers — **555** for your daily session, **54** for boss fights. 5 forward, 9 back.
- **Learn more:** _(none)_  ·  _(note: this is also the "help menu" — the new Caching screen, §10, slots in here at key 2.)_

### `lesson-pack-select` — Select Lesson Pack
- **Proposed:** Search any lesson from any pack — by language, then set, then tier.
- **Learn more:** _(none)_

### `german-lessons` — German Core Lessons
- **Now (186):** pick a lesson; lessons trigger with flashcards, can be toggled off.
- **Proposed:** Pick a lesson to review. Lessons surface with their flashcards (and can be switched off).
- **Learn more:** _(none)_

### `lesson-content` — Lesson Content _(keep as example teaching content)_
- **Proposed (unchanged):** the modal-verbs example, as-is.
- **Learn more:** _(none)_

---

## 9 · Not reachable from `entrance` right now (address in a later batch)

These exist in `screens.json` but the BFS from entrance didn't hit them — they're reached via Tile view or pagination. Flagging so they're not forgotten; I'll propose copy when we get to them:
`terminal`, `terminal-audio`, `terminal-workshop` (the Terminal sub-tree, linked from Tile view) · `kye-page2`, `kye-list`, `kye-list2`, `kye-listeng`, `kye-list2eng` (Know-Your-Enemy pagination / word-list pages).

---

## 10 · NEW screen to create — Caching (help menu → 2)

Not in `screens.json` yet. From your description + shots `update/caching/06`–`13`. Slots under the help menu (`hints-tips`) at key **2**.

- **Title:** Caching · **Subheader:** Offline Audio
- **Proposed:** Cache a language's audio so it plays instantly, offline. Choose a language, then cache **all** or pick clusters — or delete what you've cached.
- **Note for the deeper text (Learn more / a second line, your call):** it caches in batches, so after you cancel it keeps finishing the current batch before it stops.
- **Learn more:** _(none, or `session`)_
- **Keys / flow:** _(I'll read 06–13 and fill the exact key labels + sub-steps once you've approved the copy.)_

---

### When you're happy
Tell me and I'll apply the approved **Proposed** lines as the new `description` for each screen, set each `learnMore` anchor, build the Caching screen, and verify — committing in reviewable batches.

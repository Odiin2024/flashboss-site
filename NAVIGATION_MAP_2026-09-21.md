# A navigation format, and the paths that are verified so far

Odiin, 2026-09-21: *"the interface is a bit hard to navigate… a formulaic
navigation from game start. CHOOSE HERO · ENTER HELP AND OPTIONS (8) · ENTER
PREFERENCES (3) · ETC. because changing language or doing the tier skip
challenge is hard. And, from anywhere, profile selection is the end of the back
road."* And: *"the gates, sanctum and profile menu, and help and options hold
most paths."*

He is right about the shape, and right about which four screens carry it. This
proposes the format, works the three paths he named, and marks clearly what is
**verified in the source** and what still needs mapping. Nothing below is from
memory; every screen is cited.

---

## The format

One line per step. The key you press, then the screen it puts you on.

> **See your achievements**
> `CHOOSE HERO` → `5` ENTER THE SANCTUM → `6` YOUR RECORDS → `6` ACHIEVEMENTS & STATISTICS

Rules that make it formulaic rather than prose:

* the **key** comes first and is the only thing in code font;
* the **destination** is the screen's own on-screen name, in its own words, so a
  reader can match it to what is in front of them;
* every path starts at the same place, `CHOOSE HERO`, because that is where the
  game starts and where 9 always lands you;
* `9` is never written in a path. It is the universal back key and belongs in
  the preamble, once.

The preamble the game already gives us, verbatim from `HELP & OPTIONS`:

> *FlashBoss is built around a simple principle: 5 leads you forward, and 9
> takes you back.*
> — `lang/en.json`, `help.principle_1` / `help.principle_2`

---

## The four hubs, verified

### CHOOSE HERO — `FLASHBOSS PROFILE SELECTION`
`profile_manager.py`, strings `profile_select.*`
Footer: **Choose 1-8 to continue • 9 to exit**
Heroes are numbered first, then `USER PROFILES` / `Create New Hero`, then
`SYSTEM OPTIONS`: Hero Archive, About & Links, Help & Options, Exit.
**The digits of the system options shift with how many heroes exist — NOT YET
MAPPED. See "for fable" below.**

### THE GATES — `BEGINNING SESSION FOR {username}`
`character_creation.py:2012-2021`, strings `welcome_back.menu.*`
Footer: **Press 5-8 to continue • 9 to go back**

| key | option | description |
|---|---|---|
| `5` | Enter the Sanctum | continue studies |
| `6` | Review Mode | vocabulary maintenance |
| `7` | Change Path | learn something else |
| `8` | Tier Skip Challenge | the gauntlet |

### THE SANCTUM — `THE SANCTUM ~ {username}`
`adaptive_coach.py:473-481`, strings `sanctum.menu.*`
Footer: **Choose 4-6 to continue • 9 to go back**

| key | option | description |
|---|---|---|
| `4` | Know Your Enemy | View clusters & battle |
| `5` | Review Cards | Continue your studies |
| `6` | Your Records | View and manage profile |

### HELP & OPTIONS — `HELP & OPTIONS`
`help_menu.py:117-129`, strings `help.*`
Footer: **Press 1-3 to continue • 9 to go back**

| key | option |
|---|---|
| `1` | Access All Lessons |
| `2` | Audio Cache Manager |
| `3` | Preferences |

### And the two screens those open onto

**YOUR RECORDS** — `show_profile_details`, `profile_manager.py:243`, options at
`:578-581`. Footer: **Choose 5-8 to continue • 9 to go back** (or *Tab switches
pack • 5-8 • 9 back* when the hero owns more than one pack).

| key | option | description |
|---|---|---|
| `5` | Delete Profile | Permanently erase |
| `6` | Achievements & Statistics | Your progress |
| `7` | Export Progress | Save profile backup |
| `8` | Meet the Masters | Change your guide |

**PREFERENCES** — `help_menu.py:722-730`, strings `prefs.*`

| key | option |
|---|---|
| `1` | Your languages |
| `2` | Change your master |
| `3` | Change language |
| `4` | Choose your tier |
| `5` | Lesson settings |
| `6` | Notes always on |
| `7` | Language preferences |
| `8` | Audio & Voice Settings |

---

## The three paths Odiin named

> **See your achievements**
> `CHOOSE HERO` → `5` ENTER THE SANCTUM → `6` YOUR RECORDS → `6` ACHIEVEMENTS & STATISTICS

> **Take the Tier Skip Challenge**
> `CHOOSE HERO` → `8` TIER SKIP CHALLENGE
>
> It is on the gates screen itself, one key from the start. It is hard to find
> because nothing on the way announces it, not because it is buried.

> **Change the interface language**
> `Ctrl+L` — from any screen, at any time.
>
> **This one has no menu path at all, and that is why it is hard.** It is a
> global hotkey, registered at `main.py:1492` and handled inside
> `input_utils.py`'s debounced reads *"so they fire from any screen"*
> (`main.py:1484-1486`). `HELP & OPTIONS` lists it as a hotkey
> (`help.hotkey_language`) and `PREFERENCES` prints **PRESS CTRL+L TO CHANGE THE
> INTERFACE LANGUAGE** (`prefs.ctrl_l_head` / `prefs.ctrl_l_tail`) — but there is
> no numbered option anywhere that reaches it.
>
> **Do not confuse it with Preferences `3` "Change language"**, which sets the
> **pack** you are studying, not the interface. The game says so itself:
> *"(Card-text language is set in Preferences)"* — `langpopup.prefs_note`.

Two more global hotkeys, same mechanism, same problem: `Ctrl+P` opens the Piper
text-to-speech window and `Ctrl+E` breaks an Esperanto word into roots
(`help.hotkey_piper`, `help.hotkey_esperanto`).

---

## Two findings worth acting on separately

**1. `the_gates.py` is dead code.** It looks exactly like the screen this
document calls THE GATES, and it is not: nothing imports it, its
`get_current_set_name()` returns the literal string `"German Core"`, and it
imports a `german_core` module. The live gates are in `character_creation.py`.
Anyone documenting navigation from the filename will document a screen that no
longer exists. I nearly did.

**2. The interface language has no navigable route.** A hotkey that appears in
no menu cannot be found by a player who does not already know it, and it is the
one setting a non-English speaker needs *first*, before they can read anything
that would tell them. Worth a ruling from Odiin on whether Preferences should
gain an entry, rather than only a sign pointing at the hotkey.

---

## For fable

The format above is proposed, not settled — Odiin: *"it might not be faqs, it
might. I haven't thought it through."* What is settled is that every path in it
is checked against the source.

Still to map, and each needs the same treatment:

* **CHOOSE HERO's system-option digits.** The footer says 1-8 and heroes take
  the low numbers, so Hero Archive / About & Links / Help & Options / Exit must
  shift with the hero count. Until that is read out of `profile_manager.py`,
  **"ENTER HELP AND OPTIONS (8)" in Odiin's sketch is not confirmed** and should
  not be written down as if it were.
* **Know Your Enemy onward.** `4` from the Sanctum reaches the cluster list; a
  digit picks a cluster and `5` starts the fight. Verified by the shoot routes
  in `scripts/bossfight/routes/`, not yet from the menu source.
* **Review Mode, Change Path, the Grimoire, Meet the Masters, Hero Archive.**
* **Where 9 actually stops.** Odiin says profile selection is the end of the
  back road; worth confirming it holds from every screen, including mid-fight.

Two things to preserve if the format is rewritten: keys in code font and
destinations in the screen's own words, and `9` explained once in the preamble
rather than repeated in every path.

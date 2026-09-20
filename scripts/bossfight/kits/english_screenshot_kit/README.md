# English Core kit for the website boss-fight films

`flashboss-admin/Screenshot_Kits/english_screenshot_kit` carries swaps for Pareto 1
(`cluster6_1`) and Pareto 2 (`cluster11_1`) and only an ORIGINAL_BACKUP for Core, so
there is no English Core deck to shoot. This kit is one, cut from the pack's own live
`English/core/tier_1/cluster1_1_core_engine`.

**Eight cards: have, can, come, want, think, let, take, say.** Real English Core tier-1
words, not invented.

## Why these eight and not the first eight

`ANSWER` reads the boss grid and presses the digit for the card the prompt describes. It
needs the eight clues to be **unambiguous in every interface language**, and the obvious
first eight are not:

- `have` = *haben* is a substring of `like` = *mögen, gern haben* → two options match,
  and the bench refuses: "the kit promises unique options".
- `be` = *быть (am, is, are)* → the parenthetical defeats the matcher entirely:
  "nothing known in the prompt".

So the selection excludes any card whose `Translation_<lang>` contains a parenthetical in
any of de/es/ja/zh/ru, then takes the first eight that are mutually non-substring across
all five. Exhaustive search over the cluster; these eight are the result.

## Running it

    FLASHBOSS_KITS=<dir holding only this kit> FLASHBOSS_KIT_FIGHT_READY=1 \
    python3 tools/shoot/shoot.py shoot \
      --route <site>/scripts/bossfight/routes/roots_fight_film.keys \
      --kit english_screenshot_kit --lang de --wake-pack english \
      --card-pack English --profile Core --stem ec --out <dir> \
      --slot-names frame01,…,frame11

**`--card-pack English` is not optional.** The card-text preference is keyed on the pack
DIRECTORY (`card_lang:English`) while the wake pack is the kit token (`english`). Without
it the pin misses and the run silently keeps whatever card language the *previous* run
left behind — a Spanish run asking "Traduce: ¡haben!" is what that looks like.
The kit folder must also be named `<pack>_screenshot_kit` or the forge wakes in `None`.

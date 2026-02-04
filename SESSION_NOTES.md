# FlashBoss Session Notes - December 2024

## Overview

This session covered business strategy, mobile porting, and website feedback systems for FlashBoss - a gamified spaced repetition language learning app releasing on Steam.

---

## Business Strategy

### Pricing Tiers
- **$5 tier (now):** Steam terminal version + Kivy Android port
- **$20 tier (future):** Godot rebuild with proper mobile UI (years away)

### Release Roadmap
1. Launch on Steam, get reviews, fix bugs (Month 1-2)
2. Start Kivy port once bugs stabilize (Month 2-3)
3. Pump out language packs (ongoing)
4. Godot premium version when revenue justifies it

### Language Pack Priorities
- **Already done:** German Core, Esperanto
- **Next:** French, Spanish
- **Then:** Russian + Ukrainian (bundle together)
- **Dropped:** Estonian, Latin (no Piper TTS support)

### Piper TTS Confirmed Languages
ar (Arabic), de (German), es (Spanish), fr (French), it (Italian), pt (Portuguese), ru (Russian), uk (Ukrainian), el (Greek), and 30+ others. Full list at: https://github.com/rhasspy/piper/blob/master/VOICES.md

### Audio Strategy (Simplified)
- **Desktop (good CPU):** Piper local TTS
- **Desktop (slow CPU):** Pre-bundled audio (~32MB per language pack)
- **Mobile:** Pre-bundled audio (works offline, third-world friendly)
- **Killed:** Online TTS option (adds complexity, server costs, latency)

---

## Steam Store Notes

- Game submitted for review (program + 4 DLC)
- AI disclosure corrected (reset queue position)
- Genre: Should be **Education**, currently Casual - fix via Steamworks if not already in tags
- Tags are set correctly, so discovery should work
- **Don't keep changing store page during review** - batches changes, let it through

---

## Kivy Mobile Port

### Project Location
`/home/odiin/Documents/Bootcamp/FlashBossKivy/`

### Files Created
```
FlashBossKivy/
├── main.py              # Working demo with 52x28 display + buttons
├── README.md            # Project notes, porting guide, checklist
├── requirements.txt     # Dependencies (kivy)
├── buildozer.spec       # Android build config
├── screens/
│   └── __init__.py      # Notes on screens to port
├── game/
│   └── __init__.py      # Notes on logic to port
└── assets/
    └── fonts/           # Put monospace font here
```

### Key Decisions
- **Landscape mode only** - 52x28 character display with buttons on right
- **Worst-case phone (360x640pt):** 11pt font, tight but readable
- **Tablet:** Comfortable at 17pt equivalent

### Input Widget Concept (NOT YET BUILT)
Slider from 0-9 where:
- Number displays above thumb as you drag
- Options magnify like macOS dock on hover
- Release to select
- Pull down to cancel
- Replaces 8 tiny buttons with one elegant gesture

### What's Automatable
- Color conversion (ANSI → Kivy markup): Regex script
- Screen content extraction: Parse print() statements
- Game logic (SRS, cards, tiers): Copy with minimal changes

### What Needs Manual Rebuild
- Slider input widget
- Swipe navigation
- Screen manager flow
- Keyboard for name entry
- Audio integration

### Time Estimate
- **With automation:** ~2 weeks
- **Without automation:** 4-5 weeks

### LEFT UNDONE - Kivy
1. Converter script (extracts screen content, converts colors)
2. Slider widget prototype
3. Actual porting of screens

---

## Website Feedback System

### Files Created
- `flashboss-site/report.html` - Report Issue page (styled, needs form embed)
- `flashboss-site/scripts/pull_corrections.py` - Python script to pull from Google Sheets
- Updated `index.html` - Added REPORT link next to MANUAL

### LEFT UNDONE - Feedback System
1. **Create Google Form** with fields:
   - Card / Word (short answer)
   - Language Pack (dropdown)
   - Issue Type (dropdown: Wrong translation, Typo, Audio issue, Grammar error, Other)
   - Description (paragraph)
   - Suggested Fix (short answer, optional)
   - Contact (short answer, optional)

2. **Get form embed URL** and update `report.html`:
   - Replace `YOUR_FORM_ID_HERE` with actual form ID (two places)

3. **Set up Google Cloud service account** for the Python script:
   - Create project at console.cloud.google.com
   - Enable Google Sheets API
   - Create service account, download JSON key
   - Save as `service_account.json` in scripts folder
   - Share Google Sheet with service account email
   - Update `SPREADSHEET_ID` in `pull_corrections.py`

---

## Phone Layout Test File

Created `flashboss-site/phone-layout-test.html` - Print on A4 to see:
1. Landscape comfortable (17pt) - tablet/large phone
2. Portrait cramped (9pt) - demonstrates why portrait won't work
3. Small phone worst case (11pt) - budget Android simulation

---

## Rejected/Reverted Ideas

- **OS autodetect on manual page** - Reverted. Three cards showing all platforms is cleaner.
- **Online TTS server** - Killed. Pre-bundled audio is simpler and works offline.
- **Meta MMS TTS** - NC license blocks commercial use, stick with Piper.

---

## Quick Reference

### Google Play Store Cut
- First $1M/year: **15%** (you keep $4.25 on $5 sale)
- Above $1M: **30%**

### Steam Cut
- Flat **30%** (you keep $3.50 on $5 sale)

### Pre-bundled Audio Size
- ~32KB per card (word + sentence, compressed)
- ~32MB per 1000-card language pack
- Totally reasonable for mobile

---

## Next Actions (Priority Order)

1. Wait for Steam review to complete
2. 60 beta keys → language communities → reviews
3. Fix bugs as they come in (Month 1-2)
4. Set up Google Form for feedback (when ready)
5. Start Kivy port when bugs stabilize
6. Build French pack, then Spanish

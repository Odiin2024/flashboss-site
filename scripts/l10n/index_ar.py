# Arabic strings for index.html (the title screen).
# House rules (Odiin 2026-11-01/02): gender-neutral (no masculine imperatives:
# verbal nouns, impersonal forms), no harakat, ASCII digits (3,000), product and
# proper names stay Latin. Terms follow the game's lang/ar.json and the Arabic
# Steam copy of the base game (storepage_1012416, "arabic"): boss fight = معركة
# زعيم, cluster = عنقود, tier = المرحلة, spaced repetition = التكرار المتباعد.
TITLE = "FlashBoss — بطاقات تعليمية بمعارك الزعماء"
DESCRIPTION = ("FlashBoss — بطاقات تعليمية بالتكرار المتباعد ومعارك زعماء حقيقية. ثماني دورات لغات: "
               "اللاتينية والفرنسية والسواحيلية والألمانية والإيطالية والإسبانية والإسبرانتو وToki Pona، "
               "إلى جانب الإنجليزية وسلسلة Roots وThe Guide لسادة اللعبة. متاحة الآن على Steam.")

STRINGS = {
 # ---- social cards ----
 "FlashBoss — Flashcards with Boss Fights": "FlashBoss — بطاقات تعليمية بمعارك الزعماء",
 "Spaced-repetition flashcards with real boss fights. Eight language courses: Latin, French, Swahili, German, Italian, Spanish, Esperanto and Toki Pona, plus English, the Roots Series, and The Guide for game masters. Now live on Steam.":
   "بطاقات تعليمية بالتكرار المتباعد ومعارك زعماء حقيقية. ثماني دورات لغات: اللاتينية والفرنسية والسواحيلية "
   "والألمانية والإيطالية والإسبانية والإسبرانتو وToki Pona، إلى جانب الإنجليزية وسلسلة Roots وThe Guide "
   "لسادة اللعبة. متاحة الآن على Steam.",

 # ---- the scene ----
 '<p class="descriptor">Flashcards with Boss Fights</p>': '<p class="descriptor">بطاقات تعليمية بمعارك الزعماء</p>',
 'aria-label="Enter FlashBoss"': 'aria-label="دخول FlashBoss"',
 'alt="Enter"': 'alt="دخول"',

 # ---- footer ----
 ">Voices<": ">الأصوات<",
 ">Packs<": ">الحزم<",
 ">Walkthrough (beta)<": ">الدليل (تجريبي)<",
 ">Live on Steam<": ">متاحة على Steam<",
 ">Report Errors<": ">الإبلاغ عن الأخطاء<",
 ">BossFight<": ">معركة الزعيم<",

 # the fixed beta notice wraps to several lines on a phone: keep the switch just below it
 "var sw=document.querySelector('.lang-switch'); if(!sw) return;":
   "var sw=document.querySelector('.lang-switch'); if(!sw) return;\n"
   "      var bn=document.querySelector('.beta-note'); function place(){ if(bn) sw.style.top=(bn.offsetHeight+12)+'px'; }\n"
   "      place(); window.addEventListener('resize', place);",
}

# The title screen pins everything with physical left/right; the switch moves to
# the top-left corner, and below the fixed two-line beta notice.
RTL_CSS = """html[dir="rtl"] .lang-switch{right:auto; left:16px; top:76px;}
html[dir="rtl"] .beta-note{position:fixed; inset:0 0 auto 0; width:100%; z-index:30;}
html[dir="rtl"] .descriptor{font-family:var(--sans);}
"""

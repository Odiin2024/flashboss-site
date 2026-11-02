# Arabic strings for voices.html.
# House rules (Odiin 2026-11-01/02): gender-neutral (no masculine imperatives or
# second-person verbs: verbal nouns, impersonal and passive forms), no harakat,
# ASCII digits, product and proper names stay Latin (FlashBoss, PiperTTS, Steam,
# the voices' names: Vitali, davefx, LibriTTS, SIWIS, paola, Thorsten Müller).
# The voice names a learner sees on the cards (Deutsch, Español, Français,
# Italiano, Latina, toki pona, Castellano, Русский) stay in their own language,
# as on every locale of this page; the sample sentences stay untranslated, the
# glosses under them are Arabic. Terms: voice = صوت, voice DLC = صوت DLC,
# pack = حزمة, Preferences → Audio and voice = التفضيلات ← الصوت وأصوات النطق
# (lang/ar.json), boss fight = معركة زعيم.
TITLE = "الأصوات — الاستماع إلى كل لغات FlashBoss | FlashBoss"
DESCRIPTION = ("الاستماع إلى الأصوات التي تنطق FlashBoss قبل شراء أي شيء. جمل حقيقية من البطاقات بالأصوات "
               "العصبية نفسها التي تأتي مع اللعبة — الإنجليزية (الأمريكية والبريطانية) والألمانية والإسبانية "
               "(الأمريكية اللاتينية والقشتالية) والفرنسية والإيطالية والإسبرانتو واللاتينية وToki Pona. "
               "يعمل تحويل النص إلى كلام دون اتصال، على الجهاز نفسه.")

STRINGS = {
 # ---- nav / chrome ----
 ">home<": ">الرئيسية<",
 ">packs<": ">الحزم<",
 ">word lists<": ">قوائم الكلمات<",
 ">lessons<": ">الدروس<",
 ">how it works<": ">كيف تعمل اللعبة<",
 ">steam<": ">Steam<",
 ">voices<": ">الأصوات<",
 ">walkthrough (beta)<": ">الدليل (تجريبي)<",

 # ---- hero ----
 '<div class="crumb">Voices</div>': '<div class="crumb">الأصوات</div>',
 ">What it sounds like<": ">كيف تبدو الأصوات<",
 "FlashBoss pronounces every card, and the built-in PiperTTS window (open with <b>Ctrl + P</b> in-game) allows you to type or paste any text for pronunciation in your target language. Scroll down to see examples for each voice.":
   "ينطق FlashBoss كل بطاقة، وتتيح نافذة PiperTTS المدمجة (تفتح بالضغط على <b>Ctrl + P</b> داخل اللعبة) "
   "كتابة أي نص أو لصقه لسماعه منطوقا باللغة المستهدفة. وفي الأسفل أمثلة لكل صوت.",
 ">Playthrough Manual<": ">دليل اللعب<",
 ">Technical Manual<": ">الدليل التقني<",

 # ---- included with FlashBoss ----
 ">Included with FlashBoss<": ">مضمنة في FlashBoss<",
 ">free · no purchase<": ">مجانا · دون شراء<",
 "These two come with the game itself. Install FlashBoss and they are already there.":
   "هذان الصوتان يأتيان مع اللعبة نفسها، ويكونان موجودين بمجرد تثبيت FlashBoss.",
 'aria-label="Play the American English sample"': 'aria-label="تشغيل عينة الإنجليزية الأمريكية"',
 ">American English<": ">الإنجليزية الأمريكية<",
 ">United States · female<": ">الولايات المتحدة · صوت نسائي<",
 "Speaks <b>every English pack</b> — Core, Pareto 1 and 2, Advance, Adept, and all four Roots courses.":
   "ينطق <b>كل حزم الإنجليزية</b> — Core وPareto 1 و2 وAdvance وAdept ودورات Roots الأربع كلها.",
 ">Two cards from English Core.<": ">بطاقتان من English Core.<",
 'aria-label="Play the Esperanto sample"': 'aria-label="تشغيل عينة الإسبرانتو"',
 ">Esperanto (F)<": ">الإسبرانتو (صوت نسائي)<",
 ">no country · female<": ">بلا بلد · صوت نسائي<",
 "Speaks <b>Toki Pona</b>, which is free in the base game, and the <b>Esperanto</b> courses. Trained for FlashBoss, because no good Esperanto voice existed.":
   "ينطق <b>Toki Pona</b>، المجانية في اللعبة الأساسية، ودورات <b>الإسبرانتو</b>. تم تدريبه خصيصا لـ "
   "FlashBoss، إذ لم يكن هناك صوت جيد للإسبرانتو.",
 ">The price of that book is very low, so I will buy it.<": ">سعر ذلك الكتاب منخفض جدا، لذا سأشتريه.<",
 "FlashBoss · CC0 1.0 · trained on Mozilla Common Voice": "FlashBoss · CC0 1.0 · مدرب على Mozilla Common Voice",

 # ---- included with a pack ----
 ">Included with a pack<": ">مضمنة في حزمة<",
 ">buy the course, get the voice<": ">شراء الدورة يشمل الصوت<",
 "Nothing extra to buy and nothing to configure. Install the pack and it speaks.":
   "لا شيء إضافي للشراء ولا شيء للضبط. بمجرد تثبيت الحزمة تبدأ بالكلام.",
 'aria-label="Play the German sample"': 'aria-label="تشغيل عينة الألمانية"',
 ">Germany · male<": ">ألمانيا · صوت رجالي<",
 "Comes with <b>German Core</b> and both <b>German Pareto</b> courses.":
   "يأتي مع <b>German Core</b> ودورتي <b>German Pareto</b> كلتيهما.",
 ">Your health is the most important thing in life — please always take good care of yourself.<":
   ">صحتكم أهم شيء في الحياة — يرجى الاعتناء بأنفسكم جيدا دائما.<",
 'aria-label="Play the Latin American Spanish sample"': 'aria-label="تشغيل عينة الإسبانية الأمريكية اللاتينية"',
 ">Latin America · female<": ">أمريكا اللاتينية · صوت نسائي<",
 "Comes with <b>Spanish Core</b> and both <b>Spanish Pareto</b> courses.":
   "يأتي مع <b>Spanish Core</b> ودورتي <b>Spanish Pareto</b> كلتيهما.",
 ">She managed to overcome all obstacles thanks to her perseverance and effort.<":
   ">تمكنت من تجاوز كل العقبات بفضل مثابرتها وجهدها.<",
 'aria-label="Play the French sample"': 'aria-label="تشغيل عينة الفرنسية"',
 ">France · female<": ">فرنسا · صوت نسائي<",
 "Comes with <b>French Core</b> and both <b>French Pareto</b> courses.":
   "يأتي مع <b>French Core</b> ودورتي <b>French Pareto</b> كلتيهما.",
 ">There are markets everywhere in the country, and the salt and pepper are on the table.<":
   ">في البلد أسواق في كل مكان، والملح والفلفل على الطاولة.<",
 'aria-label="Play the Italian sample"': 'aria-label="تشغيل عينة الإيطالية"',
 ">Italy · female<": ">إيطاليا · صوت نسائي<",
 "Comes with <b>Italian Core</b> and both <b>Italian Pareto</b> courses.":
   "يأتي مع <b>Italian Core</b> ودورتي <b>Italian Pareto</b> كلتيهما.",
 ">Every morning I have breakfast with my mother in the kitchen.<":
   ">كل صباح أتناول الفطور مع أمي في المطبخ.<",
 'aria-label="Play the Toki Pona sample"': 'aria-label="تشغيل عينة Toki Pona"',
 ">free in the base game<": ">مجانية في اللعبة الأساسية<",
 "Spoken by the <b>Esperanto voice</b> — every sound Toki Pona uses is already in Esperanto.":
   "ينطقها <b>صوت الإسبرانتو</b> — فكل صوت تستخدمه Toki Pona موجود أصلا في الإسبرانتو.",
 ">In the future, I want to learn Toki Pona.<": ">في المستقبل أريد أن أتعلم Toki Pona.<",
 'aria-label="Play the Latin sample"': 'aria-label="تشغيل عينة اللاتينية"',
 ">classical · male<": ">كلاسيكية · صوت رجالي<",
 'Comes with <a href="latin.html"><b>Latin Core</b></a> and <b>Latin Pareto</b>, both out now. Trained for FlashBoss, with restored classical pronunciation, and it honours the macrons as real vowel length.':
   'يأتي مع <a href="latin.html"><b>Latin Core</b></a> و<b>Latin Pareto</b>، وكلتاهما متاحة الآن. تم تدريبه '
   'خصيصا لـ FlashBoss بالنطق الكلاسيكي المستعاد، ويراعي علامات المد (macrons) طولا حقيقيا للحركات.',
 ">At first light the enemy’s cavalry approaches the camp. (after Caesar)<":
   ">عند أول ضوء يقترب فرسان العدو من المعسكر. (عن Caesar)<",

 # ---- voice DLC ----
 ">Voice DLC, sold on its own<": ">أصوات DLC تباع منفردة<",
 ">a different accent, everywhere<": ">لكنة مختلفة في كل مكان<",
 "A voice DLC replaces the included voice across every pack in that language — cards, lessons, boss fights, the lot. Switch back to the built-in voice whenever you like; nothing is lost. Each card below also plays <b>the voice it replaces</b>, saying the same sentence, so you can hear exactly what changes before you spend anything.":
   "يحل صوت DLC محل الصوت المضمن في كل حزم تلك اللغة — البطاقات والدروس ومعارك الزعماء، كل شيء. ويمكن "
   "العودة إلى الصوت المدمج في أي وقت دون أن يضيع شيء. وكل بطاقة أدناه تشغل أيضا <b>الصوت الذي تحل محله</b> "
   "وهو يقول الجملة نفسها، لسماع ما يتغير بالضبط قبل إنفاق أي شيء.",
 'aria-label="Play the British English sample"': 'aria-label="تشغيل عينة الإنجليزية البريطانية"',
 ">British English (F)<": ">الإنجليزية البريطانية (صوت نسائي)<",
 ">Southern England · female<": ">جنوب إنجلترا · صوت نسائي<",
 "Replaces the American voice across <b>every English pack</b>.":
   "يحل محل الصوت الأمريكي في <b>كل حزم الإنجليزية</b>.",
 "New to FlashBoss and want British? ": "لمن يبدأ مع FlashBoss ويريد الإنجليزية البريطانية: ",
 " is the game and this voice together — the one to buy first.":
   " تجمع اللعبة وهذا الصوت معا — وهي الخيار الأنسب للشراء أولا.",
 ">Listen to bottle, glass, water.<": ">الاستماع إلى bottle وglass وwater.<",
 'aria-label="Play the included American voice saying the same sentence"':
   'aria-label="تشغيل الصوت الأمريكي المضمن وهو يقول الجملة نفسها"',
 ">Hear the same sentence in the included American voice<": ">الجملة نفسها بالصوت الأمريكي المضمن<",
 'aria-label="Play the Castilian Spanish sample"': 'aria-label="تشغيل عينة الإسبانية القشتالية"',
 ">not yet released<": ">لم يصدر بعد<",
 ">Spain · male<": ">إسبانيا · صوت رجالي<",
 "Replaces the Latin American voice across <b>every Spanish pack</b>.":
   "يحل محل صوت أمريكا اللاتينية في <b>كل حزم الإسبانية</b>.",
 ">Listen to gracias and perseverancia.<": ">الاستماع إلى gracias وperseverancia.<",
 'aria-label="Play the included Latin American voice saying the same sentence"':
   'aria-label="تشغيل صوت أمريكا اللاتينية المضمن وهو يقول الجملة نفسها"',
 ">Hear the same sentence in the included Latin American voice<": ">الجملة نفسها بصوت أمريكا اللاتينية المضمن<",
 # Vitali (Voices: Russian (M), Steam item 1320017)
 'aria-label="Play the Russian male voice sample"': 'aria-label="تشغيل عينة الصوت الروسي الرجالي"',
 ">Russia · male<": ">روسيا · صوت رجالي<",
 "Replaces the female voice across <b>every Russian pack</b> — Russian Core, Pareto 1 and Pareto 2.":
   "يحل محل الصوت النسائي في <b>كل حزم الروسية</b> — Russian Core وPareto 1 وPareto 2.",
 "Installed, it becomes the reading voice for Russian. Switch back to the female voice any time: Preferences → Audio and voice.":
   "بعد تثبيته يصبح صوت القراءة للروسية. ويمكن العودة إلى الصوت النسائي في أي وقت: التفضيلات ← الصوت وأصوات النطق.",
 ">In the evening my sister shows us photos from her vacation.<": ">في المساء تعرض علينا أختي صور إجازتها.<",
 'aria-label="Play the included female Russian voice saying the same sentence"':
   'aria-label="تشغيل الصوت الروسي النسائي المضمن وهو يقول الجملة نفسها"',
 ">Hear the same sentence in the included female voice<": ">الجملة نفسها بالصوت النسائي المضمن<",
 "Vitali · FlashBoss · CC0 1.0 · trained on Mozilla Common Voice": "Vitali · FlashBoss · CC0 1.0 · مدرب على Mozilla Common Voice",

 # ---- the PiperTTS window ----
 ">The PiperTTS window — read anything<": ">نافذة PiperTTS — قراءة أي شيء<",
 'alt="The PiperTTS window: a voice picker set to English, a speed control at 1.0x, an empty text field with a Clear button, and Speak, Restart and Save buttons above the line &quot;Paste text in the field above.&quot;"':
   'alt="نافذة PiperTTS: منتقي صوت مضبوط على الإنجليزية، وأداة سرعة عند 1.0x، وحقل نص فارغ مع زر Clear، '
   'وأزرار Speak وRestart وSave فوق السطر &quot;Paste text in the field above.&quot;"',
 "<b>Press <span class=\"kbd\">Ctrl</span> + <span class=\"kbd\">P</span> anywhere in the game</b> and a pronunciation window opens. Paste in a word, a sentence, a paragraph of something you are reading — it speaks it in the voice you are learning with, and saves it to a file if you want to keep it. It works while a card is on screen, in the menus, in the middle of a boss fight.":
   "<b>بالضغط على <span class=\"kbd\">Ctrl</span> + <span class=\"kbd\">P</span> في أي مكان من اللعبة</b> "
   "تفتح نافذة النطق. يمكن لصق كلمة أو جملة أو فقرة من أي نص قيد القراءة — فتنطقه بالصوت المستخدم في التعلم، "
   "وتحفظه في ملف عند الرغبة في الاحتفاظ به. وتعمل والبطاقة على الشاشة، وفي القوائم، وفي منتصف معركة زعيم.",
 ">FlashBoss Home<": ">صفحة FlashBoss الرئيسية<",
 ">FlashBoss on Steam<": ">FlashBoss على Steam<",
 "Voices run locally with Piper. Every clip here is unedited output from the shipping models.":
   "تعمل الأصوات محليا بمحرك Piper. وكل مقطع هنا مخرجات غير معدلة من النماذج التي تأتي مع اللعبة.",
 # the clip player's failure label
 "'This clip could not be loaded'": "'تعذر تحميل هذا المقطع'",
}

# Page-specific mirroring (shared rules live in localize_new_pages.RTL_CSS).
# The sample sentences are German, Spanish, Russian…: each one takes its direction
# from its own first letter, so its punctuation stays where it belongs.
RTL_CSS = """html[dir="rtl"] .soon{margin-left:0; margin-right:6px;}
html[dir="rtl"] .tip{border-left:0; border-right:2px solid var(--accent); padding:12px 16px 12px 0;}
html[dir="rtl"] .vcard .say{unicode-bidi:plaintext; text-align:right;}
html[dir="rtl"] .btn{box-shadow:-6px 6px 0 color-mix(in oklab, var(--accent), #000 62%);}
html[dir="rtl"] .btn:hover{transform:translate(2px,-2px); box-shadow:-8px 8px 0 color-mix(in oklab, var(--accent), #000 62%);}
html[dir="rtl"] .btn:active{transform:translate(-3px,3px); box-shadow:-2px 2px 0 color-mix(in oklab, var(--accent), #000 62%);}
html[dir="rtl"] .btn.ghost, html[dir="rtl"] .btn.ghost:hover{box-shadow:none;}
"""

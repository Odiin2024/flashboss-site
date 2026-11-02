# Arabic strings for home.html.
# House rules (Odiin 2026-11-01/02): gender-neutral (no masculine imperatives:
# verbal nouns, impersonal and passive forms), no harakat, ASCII digits (3,000),
# product and proper names stay Latin (FlashBoss, Core, Pareto 1, Steam, the
# pack names). Terms follow the game's lang/ar.json and the Arabic Steam copy of
# the base game (storepage_1012416, "arabic"): boss fight = معركة زعيم,
# cluster = عنقود, spaced repetition = التكرار المتباعد, pack = حزمة,
# game master = سيد اللعبة, notes = الملاحظات, example sentence = جملة المثال.
# Arrows that point "onward" turn round for a right-to-left reader (&rarr; -> &larr;).
TITLE = "FlashBoss — بطاقات تعليمية بمعارك الزعماء"
DESCRIPTION = ("FlashBoss: بطاقات تعليمية بالتكرار المتباعد ومعارك الزعماء. بناء مفردات حقيقية في الإنجليزية "
               "أو اللاتينية أو الفرنسية أو السواحيلية أو الألمانية أو الإيطالية أو الإسبانية أو الإسبرانتو "
               "أو Toki Pona. خمس حزم مجانية، والبقية على Steam. استماع، وقراءة، وتكرار، وتقييم، وقتال.")

STRINGS = {
 # ---- nav / chrome ----
 ">home<": ">الرئيسية<",
 ">packs<": ">الحزم<",
 ">word lists<": ">قوائم الكلمات<",
 ">lessons<": ">الدروس<",
 ">manual<": ">الدليل<",
 ">english path<": ">مسار الإنجليزية<",
 ">voices<": ">الأصوات<",
 ">resources<": ">الموارد<",
 ">steam<": ">Steam<",

 # ---- the announcement strip ----
 '<a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows&nbsp;Terminal</a> required for Windows&nbsp;10':
   'يلزم <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows&nbsp;Terminal</a> على Windows&nbsp;10',
 " &mdash; Available on Steam &mdash; ": " &mdash; متاحة على Steam&rlm; &mdash; ",  # RLM: keeps Steam out of the Windows/Mac/Linux run

 # ---- hero ----
 # the brand + its terminal cursor read left to right; RTL_CSS keeps it on the right edge
 '<h1 class="reveal">FlashBoss<span class="cursor"></span></h1>':
   '<h1 class="reveal" dir="ltr">FlashBoss<span class="cursor"></span></h1>',
 ">spaced-repetition with boss fights<": ">التكرار المتباعد مع معارك الزعماء<",
 'Build a real vocabulary: <b><a href="packs.html">English</a>, <a href="latin.html">Latin</a>, <a href="french.html">French</a>, <a href="swahili.html">Swahili</a>, <a href="german.html">German</a>, <a href="italian.html">Italian</a>, <a href="spanish.html">Spanish</a>, <a href="esperanto.html">Esperanto</a>, or <a href="toki-pona.html">Toki Pona</a></b> — then prove it in a duel.':
   'بناء مفردات حقيقية: <b><a href="packs.html">الإنجليزية</a> أو <a href="latin.html">اللاتينية</a> أو '
   '<a href="french.html">الفرنسية</a> أو <a href="swahili.html">السواحيلية</a> أو <a href="german.html">الألمانية</a> '
   'أو <a href="italian.html">الإيطالية</a> أو <a href="spanish.html">الإسبانية</a> أو '
   '<a href="esperanto.html">الإسبرانتو</a> أو <a href="toki-pona.html">Toki Pona</a></b> — ثم إثباتها في مبارزة.',

 # ---- the approach ----
 ">Listen · read · repeat · rate · fight<": ">استماع · قراءة · تكرار · تقييم · قتال<",
 ">The FlashBoss approach<": ">نهج FlashBoss<",
 "The target vocabulary is grouped into thematic clusters with progressively longer, and more complex example sentences and explanatory notes. Each cluster ends in a boss fight.":
   "تتوزع المفردات المستهدفة على عناقيد موضوعية، بجمل أمثلة وملاحظات شارحة تزداد طولا وتعقيدا شيئا فشيئا. "
   "وينتهي كل عنقود بمعركة زعيم.",
 "Before you can defeat the boss, you must answer to the words you found most challenging. Win, and those cards graduate.":
   "ولا سبيل إلى هزيمة الزعيم قبل مواجهة الكلمات الأصعب. ومع الفوز تتخرج تلك البطاقات.",

 # ---- the card ----
 ">The cards themselves<": ">البطاقات نفسها<",
 ">Cascading display<": ">عرض متتابع<",
 "<p><b>Target word</b> — presented with visual cues to aid retention. Current review intervals are shown in stars.</p>":
   "<p><b>الكلمة المستهدفة</b> — تعرض مع إشارات بصرية تعين على الحفظ. وتظهر فترات المراجعة الحالية على هيئة نجوم.</p>",
 "<p><b>Example sentence</b> — about 90% built from language already learned.</p>":
   "<p><b>جملة المثال</b> — نحو 90% منها مبني من لغة سبق تعلمها.</p>",
 "<p><b>Example translation</b> — an idiomatic rendering of the sentence.</p>":
   "<p><b>ترجمة المثال</b> — صياغة اصطلاحية للجملة.</p>",
 "<p><b>Translation</b> — rate the word, view your notes, <b>7</b> to check the rating options.</p>":
   "<p><b>الترجمة</b> — تقييم الكلمة، وعرض الملاحظات، و<b>7</b> لعرض خيارات التقييم.</p>",
 "<p><b>Notes</b> — grammar, etymology, related language and examples. Press <b>8</b> to view notes. They are optional.</p>":
   "<p><b>الملاحظات</b> — القواعد، وأصل الكلمة، وما يتصل بها من اللغة، وأمثلة. الضغط على <b>8</b> يعرض الملاحظات، وهي اختيارية.</p>",
 "A FlashBoss flashcard for the German word die Ehefrau (wife): a colour-coded target word with mastery stars, an example sentence and its translation, the plain translation, and notes.":
   "بطاقة FlashBoss للكلمة الألمانية die Ehefrau (الزوجة): كلمة مستهدفة مرمزة بالألوان مع نجوم الإتقان، "
   "وجملة مثال وترجمتها، والترجمة المجردة، والملاحظات.",

 # ---- boss fight ----
 ">The Bossfight<": ">معركة الزعيم<",
 ">How we test<": ">كيف نختبر<",
 "<p>One step forward with a correct answer.</p>": "<p>خطوة إلى الأمام مع كل إجابة صحيحة.</p>",
 "<p>Two steps back with each mistake.</p>": "<p>وخطوتان إلى الوراء مع كل خطأ.</p>",
 "<p>Your easiest cards on positions 1 &amp; 2.</p>": "<p>أسهل البطاقات في الموضعين 1 و2.</p>",
 "<p>Your most difficult on positions 3 &amp; 4.</p>": "<p>وأصعبها في الموضعين 3 و4.</p>",
 ">Try the live demo &rarr;<": ">تجربة العرض الحي &larr;<",
 "Three FlashBoss boss fights in a row, each announced by its own title card. LatAm Spanish asks for the Spanish word for heart, Latin Roots asks which word means a glass tank for fish, and The Guide asks you to name the spell from its rules text. Each fight reaches the killstroke position, loses it to a wrong answer and is pushed two steps back, then climbs again and wins.":
   "ثلاث معارك زعماء في FlashBoss متتالية، تفتتح كلا منها بطاقة عنوان خاصة بها. تسأل الإسبانية "
   "الأمريكية اللاتينية عن الكلمة الإسبانية للقلب، وتسأل Latin Roots عن الكلمة التي تعني حوضا زجاجيا "
   "للأسماك، وتطلب The Guide تسمية التعويذة من نص قواعدها. تبلغ كل معركة موضع الضربة القاضية، ثم تخسره "
   "بإجابة خاطئة فتتراجع خطوتين، ثم تصعد من جديد وتفوز.",
 '<span class="bf-hint">try the demo</span>': '<span class="bf-hint">تجربة العرض</span>',

 # ---- what you get ----
 ">Five packs ship free<": ">خمس حزم مجانية مع اللعبة<",
 ">Add additional decks as you go.<": ">ويمكن إضافة مجموعات أخرى مع التقدم.<",
 ">Free in the base game<": ">مجانا في اللعبة الأساسية<",
 ">English Advance &amp; Adept<": ">English Advance وEnglish Adept<",
 ">The Roots Series<": ">سلسلة Roots<",
 'German, Norman, Latin and Greek Roots — the history <a href="packs.html">English</a> is built from, and four of the six steps on <a href="immersion.html">the immersion path</a>.':
   'German Roots وNorman Roots وLatin Roots وGreek Roots — التاريخ الذي بنيت منه <a href="packs.html">الإنجليزية</a>، '
   'وأربع من الخطوات الست على <a href="immersion.html">مسار الانغماس</a>.',
 ">Full language courses<": ">دورات لغات كاملة<",
 'Learn <a href="latin.html">Latin</a>, <a href="french.html">French</a>, <a href="swahili.html">Swahili</a>, <a href="german.html">German</a>, <a href="italian.html">Italian</a>, <a href="spanish.html">Spanish</a> or <a href="esperanto.html">Esperanto</a> with FlashBoss. Most run 3,000 words across Core, Pareto 1 and Pareto 2 — Latin is a 2,000-word reading course, and Swahili\'s Core is out with its Pareto packs to come.':
   'دورات FlashBoss في <a href="latin.html">اللاتينية</a> و<a href="french.html">الفرنسية</a> '
   'و<a href="swahili.html">السواحيلية</a> و<a href="german.html">الألمانية</a> و<a href="italian.html">الإيطالية</a> '
   'و<a href="spanish.html">الإسبانية</a> و<a href="esperanto.html">الإسبرانتو</a>. معظمها 3,000 كلمة موزعة على '
   'Core وPareto 1 وPareto 2 — أما اللاتينية فدورة قراءة من 2,000 كلمة، وقد صدرت Core السواحيلية وحزمتا Pareto في الطريق.',
 ">Not a language at all<": ">ليست لغة على الإطلاق<",
 '<a href="the-guide.html">The Guide</a> — the rules a game master needs in their head, as flashcards. 1,205 cards in 62 clusters, 5E compatible.':
   '<a href="the-guide.html">The Guide</a> — القواعد التي يلزم سيد اللعبة استحضارها دائما، على هيئة بطاقات تعليمية. '
   '1,205 بطاقة في 62 عنقودا، متوافقة مع 5E.',

 # ---- final CTA ----
 ">Get FlashBoss on Steam &rarr;<": ">FlashBoss على Steam &larr;<",
 '<p class="epi">Scientia est Potentia.<span class="epi-cite">Knowledge is power</span></p>':
   '<p class="epi"><bdi>Scientia est Potentia.</bdi><span class="epi-cite">المعرفة قوة</span></p>',

 # ---- footer + share ----
 ">how it works<": ">كيف تعمل اللعبة<",
 ">props<": ">التقدير<",
 'aria-expanded="false">share</button>': 'aria-expanded="false">مشاركة</button>',
 ">promote<": ">الترويج<",
 'aria-label="Share"': 'aria-label="مشاركة"',
 ">Share<": ">مشاركة<",
 'aria-label="Close"': 'aria-label="إغلاق"',
 "copy link": "نسخ الرابط",
 "'copied!'": "'تم النسخ!'",
 ">post on X<": ">النشر على X<",
 "var text='FlashBoss — spaced-repetition flashcards with boss fights.';":
   "var text='FlashBoss — بطاقات تعليمية بالتكرار المتباعد ومعارك الزعماء.';",
}

# Page-specific mirroring (shared rules live in localize_new_pages.RTL_CSS).
RTL_CSS = """html[dir="rtl"] .hero .wrap{transform:translateX(min(12vw, max(0px, (100vw - 900px) / 2)));}
html[dir="rtl"] .hero h1{text-align:right;}
html[dir="rtl"] .topbanner{text-align:right;}
@media(max-width:640px){ html[dir="rtl"] .topbanner{text-align:center;} }
html[dir="rtl"] .frame > .tag{left:auto; right:22px;}
html[dir="rtl"] .btn{box-shadow:-6px 6px 0 color-mix(in oklab, var(--accent), #000 62%);}
html[dir="rtl"] .btn:hover{transform:translate(2px,-2px); box-shadow:-8px 8px 0 color-mix(in oklab, var(--accent), #000 62%);}
html[dir="rtl"] .btn:active{transform:translate(-3px,3px); box-shadow:-2px 2px 0 color-mix(in oklab, var(--accent), #000 62%);}
html[dir="rtl"] .btn.ghost, html[dir="rtl"] .btn.ghost:hover{box-shadow:none;}
html[dir="rtl"] .gives::after{background:linear-gradient(270deg, var(--gold), var(--green) 52%, var(--blue));}
html[dir="rtl"] .give{border-right:0; border-left:1px solid var(--line);}
html[dir="rtl"] .give:last-child{border-left:0;}
@media(max-width:980px){ html[dir="rtl"] .give:nth-child(2n){border-left:0;} }
@media(max-width:680px){ html[dir="rtl"] .give{border-left:0;} }
html[dir="rtl"] .share-close{right:auto; left:12px;}
html[dir="rtl"] .epi{font-style:normal;}
html[dir="rtl"] .epi bdi{font-style:italic;}
"""

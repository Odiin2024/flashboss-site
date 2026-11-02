# Arabic strings for about.html (How FlashBoss Teaches — the technical reference).
# House rules (Odiin 2026-11-01/02): gender-neutral (no masculine imperatives or
# second-person verbs: verbal nouns, impersonal and passive forms, "المتعلم" as
# the generic learner), no harakat, ASCII digits (3,000), product and proper names
# stay Latin (FlashBoss, Core, Pareto 1, Piper, the masters' names, the pack
# names). Terms follow the game's lang/ar.json and the Arabic Steam copy of the
# base game: tier = المرحلة, cluster = عنقود, boss fight = معركة زعيم, spaced
# repetition = التكرار المتباعد, master = المعلم, bossy/advisory = حازم/استشاري,
# grimoire = كتاب التعاويذ, drive = الدافع, EPIC = يوم ملحمي, streak = السلسلة,
# foundation day = يوم حجر الأساس, mastered = متقنة, rating = التقييم.
# Bibliographic references stay in their original language; only the bracketed
# glosses after them are Arabic (isolated with <bdi dir="rtl">).
# Signed figures (−3, +1) carry an LRM so the sign stays in front of the digit.
TITLE = "كيف يعلم FlashBoss — مرجع تقني | FlashBoss"
DESCRIPTION = ("مرجع تقني عن FlashBoss — بنية المحتوى، وآليات الجلسات، ونظام التخرج عبر معارك الزعماء، "
               "وعناصر التصميم الفاعلة فيه.")

STRINGS = {
 # ---- social cards ----
 "How FlashBoss Teaches — Technical Reference": "كيف يعلم FlashBoss — مرجع تقني",
 "Content architecture, session mechanics, the boss-fight graduation system, and the design elements at play.":
   "بنية المحتوى، وآليات الجلسات، ونظام التخرج عبر معارك الزعماء، وعناصر التصميم الفاعلة فيه.",
 "The pedagogy and mechanics behind FlashBoss — comprehensible input, retrieval practice, spaced repetition, and the boss-fight graduation system.":
   "المنهج التربوي والآليات وراء FlashBoss — المدخلات المفهومة، وممارسة الاسترجاع، والتكرار المتباعد، "
   "ونظام التخرج عبر معارك الزعماء.",

 # ---- nav / chrome ----
 ">home<": ">الرئيسية<",
 ">packs<": ">الحزم<",
 ">word lists<": ">قوائم الكلمات<",
 ">lessons<": ">الدروس<",
 ">manual<": ">الدليل<",
 ">resources<": ">الموارد<",
 ">steam<": ">Steam<",
 ">about<": ">نبذة<",
 ">walkthrough (beta)<": ">الدليل (تجريبي)<",
 ">press<": ">الصحافة<",

 # ---- hero + contents ----
 ">Technical Reference<": ">مرجع تقني<",
 ">How FlashBoss Teaches<": ">كيف يعلم FlashBoss<",
 'aria-label="Table of contents"': 'aria-label="جدول المحتويات"',
 ">Contents<": ">المحتويات<",
 ">Overview<": ">نظرة عامة<",
 ">Content architecture<": ">بنية المحتوى<",
 ">Masters<": ">المعلمون<",
 ">Pack structure<": ">بنية الحزم<",
 ">Session structure and scheduling<": ">بنية الجلسة والجدولة<",
 ">The boss fight<": ">معركة الزعيم<",
 ">Pedagogical design<": ">التصميم التربوي<",
 ">Scope<": ">النطاق<",
 ">Using FlashBoss effectively<": ">استخدام FlashBoss بفعالية<",

 # ---- 1. overview ----
 "FlashBoss is a desktop terminal application for vocabulary acquisition. It combines a spaced-repetition scheduler, constructed example sentences with text-to-speech, themed content clusters, and a boss-fight graduation mechanic. The system is designed to develop receptive skills — reading, listening, and comprehension — in the target language.":
   "إن FlashBoss تطبيق طرفية لسطح المكتب لاكتساب المفردات. يجمع بين مجدول للتكرار المتباعد، وجمل أمثلة "
   "مصوغة مع تحويل النص إلى كلام، وعناقيد محتوى موضوعية، وآلية تخرج عبر معارك الزعماء. والنظام مصمم "
   "لتنمية المهارات الاستقبالية — القراءة والاستماع والفهم — في اللغة المستهدفة.",
 "A single Core pack contains 1,000 cards and delivers more than 5,000 words of target-language input in context. Pareto expansion packs add more than 10,000 words each, structured around the highest-frequency vocabulary not already covered. Supported languages are English, German, Spanish, Italian, French, Latin, Swahili, Esperanto and Toki Pona.":
   "تحتوي حزمة Core واحدة على 1,000 بطاقة، وتقدم أكثر من 5,000 كلمة من مدخلات اللغة المستهدفة في سياقها. "
   "وتضيف كل حزمة توسعة من حزم Pareto أكثر من 10,000 كلمة، مبنية حول أعلى المفردات تواترا مما لم يغط بعد. "
   "واللغات المدعومة هي الإنجليزية والألمانية والإسبانية والإيطالية والفرنسية واللاتينية والسواحيلية "
   "والإسبرانتو وToki Pona.",

 # ---- 2. content architecture ----
 "This section describes the internal structure common to FlashBoss packs. Pack-level organization — how packs combine, and how foreign-language packs differ from English packs — is documented in section 4.":
   "يصف هذا القسم البنية الداخلية المشتركة بين حزم FlashBoss. أما التنظيم على مستوى الحزم — كيف تتكامل "
   "الحزم، وكيف تختلف حزم اللغات الأجنبية عن حزم الإنجليزية — فموثق في القسم 4.",
 ">Card<": ">البطاقة<",
 "Each card carries up to five text fields and two audio assets. Only the target-language fields are voiced:":
   "تحمل كل بطاقة ما يصل إلى خمسة حقول نصية ومقطعين صوتيين. ولا ينطق إلا حقلا اللغة المستهدفة:",
 ">Field<": ">الحقل<",
 ">Content<": ">المحتوى<",
 ">Yes<": ">نعم<",
 ">No<": ">لا<",
 "The vocabulary item being trained. In gendered languages it carries its article, colour-coded to gender.":
   "المفردة قيد التدريب. وفي اللغات التي تميز الجنس النحوي تحمل أداة تعريفها، ملونة بحسب الجنس.",
 "The target word's meaning in the learner's native language.":
   "معنى الكلمة المستهدفة بلغة المتعلم الأم.",
 "A constructed sentence placing the target word in context, using only vocabulary the scheduler has already introduced.":
   "جملة مصوغة تضع الكلمة المستهدفة في سياقها، ولا تستخدم إلا مفردات سبق أن قدمها المجدول.",
 "An idiomatic rendering of the example sentence in the learner's native language.":
   "صياغة اصطلاحية لجملة المثال بلغة المتعلم الأم.",
 "Etymology, grammatical note, a second worked example, or a synonym set. Optional.":
   "أصل الكلمة، أو ملاحظة نحوية، أو مثال ثان مشروح، أو مجموعة مرادفات. اختيارية.",
 "Text-to-speech is applied only to the target-language fields. This asymmetry is deliberate: the goal is to saturate the learner in the target language's phonology while keeping the native-language scaffolding silent and unintrusive.":
   "لا يطبق تحويل النص إلى كلام إلا على حقول اللغة المستهدفة. وهذا التفاوت مقصود: الغاية إغراق المتعلم "
   "في أصوات اللغة المستهدفة، مع إبقاء سقالات اللغة الأم صامتة لا تزاحم.",
 ">Cluster<": ">العنقود<",
 "A cluster is a themed group of cards — the unit of progress in FlashBoss. Clusters are introduced together, trained together, and graduated together through a single boss fight. Cluster themes are concrete and narrow: <em>Numbers and time</em>, <em>Travel and accommodation</em>, <em>Regional cuisine</em>, <em>Social roles and people</em>.":
   "العنقود مجموعة بطاقات ذات موضوع واحد — وهو وحدة التقدم في FlashBoss. تقدم بطاقات العنقود معا، "
   "وتدرب معا، وتتخرج معا عبر معركة زعيم واحدة. وموضوعات العناقيد ملموسة وضيقة: <em>الأعداد والوقت</em>، "
   "و<em>السفر والإقامة</em>، و<em>المطبخ المحلي</em>، و<em>الأدوار الاجتماعية والناس</em>.",
 ">Tier<": ">المرحلة<",
 "Clusters sit inside tiers. A Core pack contains five tiers, each typically comprising around eight clusters. In foreign-language packs, tier membership is a difficulty gate: it governs which grammar structures may appear in a cluster's example sentences. Tier 3 example sentences are restricted to present, imperative, and preterite; tier 4 adds imperfect and conditional; tier 5 opens full grammar including subjunctive. In English packs the tier system is used thematically rather than syntactically — tier membership reflects topical domain (e.g. <em>Forms and documents</em>, <em>Social and email</em>, <em>Confusables</em>) rather than grammatical complexity.":
   "تقع العناقيد داخل المراحل. تضم حزمة Core خمس مراحل، في كل منها عادة نحو ثمانية عناقيد. وفي حزم "
   "اللغات الأجنبية تكون المرحلة بوابة صعوبة: فهي تحدد التراكيب النحوية المسموح بظهورها في جمل أمثلة "
   "العنقود. تقتصر جمل أمثلة المرحلة 3 على المضارع والأمر والماضي البسيط؛ وتضيف المرحلة 4 الماضي "
   "الاستمراري والشرط؛ وتفتح المرحلة 5 القواعد كاملة بما فيها صيغة الالتزام (subjunctive). أما في حزم "
   "الإنجليزية فيستخدم نظام المراحل موضوعيا لا نحويا — إذ تعكس المرحلة مجالا موضوعيا (مثل <em>الاستمارات "
   "والوثائق</em>، و<em>التواصل الاجتماعي والبريد الإلكتروني</em>، و<em>الكلمات الملتبسة</em>) لا درجة "
   "التعقيد النحوي.",
 ">Lesson<": ">الدرس<",
 "Lessons are reference pages pinned to specific cards — checkpoint material that accompanies a card through training. When a card with an attached lesson first appears, the lesson appears alongside. Each time the card resurfaces under the spaced-repetition schedule, the lesson resurfaces with it. Lessons are therefore persistent reference, not one-time exposures. A learner who has internalized a lesson's content can deactivate it individually: the card continues training, the lesson stops appearing.":
   "الدروس صفحات مرجعية مثبتة على بطاقات بعينها — مادة نقاط مراجعة ترافق البطاقة طوال تدريبها. فحين "
   "تظهر بطاقة مرفق بها درس أول مرة، يظهر الدرس معها. وكلما عادت البطاقة وفق جدول التكرار المتباعد، عاد "
   "الدرس معها. فالدروس إذن مرجع دائم، لا عرض لمرة واحدة. ومن استوعب محتوى درس ما يمكنه تعطيله وحده: "
   "فتواصل البطاقة تدريبها، ويتوقف الدرس عن الظهور.",

 # ---- 3. masters ----
 "Before training begins, the learner chooses a master — the guide who sets the daily pace. A master fixes the <em>streak requirement</em>: the number of cards owed each day to keep the streak alive, ranging from 8 to 34 cards, roughly 5 to 30 minutes of study.":
   "قبل بدء التدريب يختار المتعلم معلما — المرشد الذي يحدد الإيقاع اليومي. ويثبت المعلم <em>نصاب السلسلة</em>: "
   "عدد البطاقات المستحقة كل يوم لإبقاء السلسلة حية، من 8 إلى 34 بطاقة، أي نحو 5 إلى 30 دقيقة من الدراسة.",
 ">Master<": ">المعلم<",
 ">Temperament<": ">الطبع<",
 ">Cards / day<": ">بطاقات / يوم<",
 "🐺 Luna — gentle, encouraging": "🐺 Luna — لطف وتشجيع",
 "⚫ Claude — analytical, precise": "⚫ Claude — تحليل ودقة",
 "🐉 Shen — stern, direct": "🐉 Shen — صرامة ومباشرة",
 "🦉 Odiin — encouraging, kind": "🦉 Odiin — تشجيع وطيبة",
 "🦊 Kitsune — playful trickster": "🦊 Kitsune — مكر ومرح",
 "🦅 Aquila — noble, disciplined": "🦅 Aquila — نبل وانضباط",
 ">Bossy<": ">حازم<",
 ">Advisory<": ">استشاري<",
 "How demanding a master is comes down to that daily count. Odiin, at twenty-one cards, is the most demanding master recommended to a new learner — the high road. The two thirty-four-card masters, Kitsune and Aquila, sit beyond it: pacing for revision passes and for outliers who want the maximum.":
   "مدى صرامة المعلم يرجع إلى ذلك العدد اليومي. وOdiin، بإحدى وعشرين بطاقة، هو أكثر المعلمين صرامة "
   "مما يوصى به للمتعلم الجديد — الطريق الأعلى. ويقع وراءه المعلمان صاحبا الأربع والثلاثين بطاقة، "
   "Kitsune وAquila: إيقاع لجولات الاستذكار ولمن يريد الحد الأقصى.",
 "A master's <em>temperament</em> is a separate matter, and it governs one thing — the grimoire. A <strong>bossy</strong> master limits grimoire sessions, a guard against running too far ahead and burning out. An <strong>advisory</strong> master warns that another is unwise, then steps aside and lets it happen. The two are otherwise identical.":
   "أما <em>طبع</em> المعلم فأمر منفصل، ويتحكم في شيء واحد — كتاب التعاويذ. فالمعلم <strong>الحازم</strong> "
   "يحد من جلسات كتاب التعاويذ، احترازا من التقدم أبعد مما ينبغي ثم الإنهاك. والمعلم <strong>الاستشاري</strong> "
   "ينبه إلى أن جلسة أخرى ليست حكيمة، ثم يتنحى ويتركها تحدث. وفيما عدا ذلك فالطبعان متطابقان.",
 "The pairing is uneven. Both the thirteen- and thirty-four-card paces come in either temperament — Claude (advisory) or Shen (bossy) at thirteen, Kitsune (advisory) or Aquila (bossy) at thirty-four — so there, pace and style are chosen separately. The eight-card pace belongs to Luna alone (bossy) and the twenty-one to Odiin alone (advisory).":
   "والتوزيع غير متساو. فإيقاعا الثلاث عشرة والأربع والثلاثين بطاقة متاحان بالطبعين كليهما — Claude "
   "(استشاري) أو Shen (حازم) عند ثلاث عشرة، وKitsune (استشاري) أو Aquila (حازم) عند أربع وثلاثين — "
   "فهناك يختار الإيقاع والأسلوب كل على حدة. أما إيقاع الثماني بطاقات فلLuna وحدها (حازم)، وإيقاع "
   "الإحدى والعشرين لOdiin وحده (استشاري).",
 ">How long it takes<": ">كم يستغرق الأمر<",
 "The pace is the whole of it. A 1,000-card set runs to five tiers, so a tier averages 200 cards — individual tiers vary either side of that — and a full course is three sets. Doing the daily requirement and nothing more:":
   "الإيقاع هو كل شيء. تمتد المجموعة ذات الـ 1,000 بطاقة على خمس مراحل، فمتوسط المرحلة 200 بطاقة — "
   "وتزيد المراحل أو تنقص عن ذلك — والدورة الكاملة ثلاث مجموعات. مع أداء النصاب اليومي لا أكثر:",
 ">Pace<": ">الإيقاع<",
 ">A tier<": ">مرحلة<",
 ">A 1,000-word set<": ">مجموعة من 1,000 كلمة<",
 ">A 3,000-word course<": ">دورة من 3,000 كلمة<",
 ">8 / day<": ">8 / يوم<",
 ">13 / day<": ">13 / يوم<",
 ">21 / day<": ">21 / يوم<",
 ">34 / day<": ">34 / يوم<",
 ">~10 weeks<": ">~10 أسابيع<",
 ">~6 weeks<": ">~6 أسابيع<",
 ">~4 weeks<": ">~4 أسابيع<",
 ">~2–3 weeks<": ">~2–3 أسابيع<",
 ">~1 year<": ">~1 سنة<",
 ">~8 months<": ">~8 أشهر<",
 ">~5–6 months<": ">~5–6 أشهر<",
 ">~3 months<": ">~3 أشهر<",
 ">~3 years<": ">~3 سنوات<",
 ">~2 years<": ">~2 سنة<",
 ">~1½ years<": ">~1½ سنة<",
 "Rounded estimates, and a floor rather than a forecast: the streak requirement is the minimum owed each day, not a ceiling, and the grimoire is there for anyone who wants to go faster. Nor does every course run to three sets — Latin's trunk is two, and Toki Pona is a single 500-card pack.":
   "تقديرات مقربة، وهي حد أدنى لا توقع: فنصاب السلسلة هو أقل ما يستحق كل يوم لا سقفه، وكتاب التعاويذ "
   "موجود لمن يريد الإسراع. ولا تمتد كل الدورات إلى ثلاث مجموعات — فجذع اللاتينية مجموعتان، وToki Pona "
   "حزمة واحدة من 500 بطاقة.",

 # ---- 4. pack structure ----
 "A pack is FlashBoss's distribution unit: a standalone vocabulary set — typically 1,000 cards — with its own cluster structure, tier structure, and lesson library. Packs ship under two different paradigms depending on the language.":
   "الحزمة هي وحدة التوزيع في FlashBoss: مجموعة مفردات قائمة بذاتها — عادة 1,000 بطاقة — لها بنية "
   "عناقيدها وبنية مراحلها ومكتبة دروسها. وتصدر الحزم وفق نموذجين مختلفين بحسب اللغة.",
 ">Foreign-language packs: cumulative three-pack progression<": ">حزم اللغات الأجنبية: تدرج تراكمي من ثلاث حزم<",
 "English, German, French, Spanish, Italian, and Esperanto each ship as a three-pack sequence: <strong>Core</strong>, <strong>Pareto 1</strong>, and <strong>Pareto 2</strong>. The progression is cumulative — each pack assumes the vocabulary introduced in previous packs and constructs new example sentences on top. Example sentences in Pareto 1 draw from Core vocabulary plus the new Pareto 1 target words; Pareto 2 assumes both prior packs. A learner completing all three reaches a 3,000-card receptive vocabulary in the target language.":
   "تصدر كل من الإنجليزية والألمانية والفرنسية والإسبانية والإيطالية والإسبرانتو سلسلة من ثلاث حزم: "
   "<strong>Core</strong> و<strong>Pareto 1</strong> و<strong>Pareto 2</strong>. والتدرج تراكمي — فكل حزمة "
   "تفترض المفردات التي قدمتها الحزم السابقة وتبني فوقها جمل أمثلة جديدة. تستمد جمل أمثلة Pareto 1 من "
   "مفردات Core إضافة إلى الكلمات المستهدفة الجديدة في Pareto 1؛ وتفترض Pareto 2 الحزمتين السابقتين معا. "
   "ومن يتم الثلاث يبلغ حصيلة استقبالية من 3,000 بطاقة في اللغة المستهدفة.",
 "Tier numbering is continuous across the sequence. Core covers tiers 1–5. Pareto 1 and Pareto 2 between them extend the sequence by ten further tiers: tier 6 is the first Pareto tier, tier 15 is the last.":
   "ترقيم المراحل متصل عبر السلسلة. تغطي Core المراحل 1–5. وتمد Pareto 1 وPareto 2 معا السلسلة بعشر "
   "مراحل أخرى: المرحلة 6 أولى مراحل Pareto، والمرحلة 15 آخرها.",
 "CEFR targets by pack:": "أهداف CEFR لكل حزمة:",
 ">Pack<": ">الحزمة<",
 ">Cards<": ">البطاقات<",
 ">Target<": ">الهدف<",
 "A1–A2 grammar exposure; prepares a learner for A2 immersion instruction.":
   "التعرض لقواعد A1–A2؛ يهيئ المتعلم لدروس الانغماس في المستوى A2.",
 "High-frequency B1–B2 vocabulary; extends into registers absent from Core (travel, bureaucratic, social).":
   "مفردات B1–B2 عالية التواتر؛ تمتد إلى سجلات لغوية غائبة عن Core (السفر، والمعاملات الرسمية، والحياة الاجتماعية).",
 "B2–C1 vocabulary; formal connectors, abstract registers, cultural content.":
   "مفردات B2–C1؛ أدوات الربط الرسمية، والسجلات المجردة، والمحتوى الثقافي.",
 ">English packs: individual standalones<": ">حزم الإنجليزية: حزم مستقلة قائمة بذاتها<",
 "English ships differently. Each English pack is a self-contained 1,000-word vocabulary set, and learners select packs based on level and interest rather than completing them in order. There is no cumulative progression — completing one English pack does not presuppose another. English packs fall into two structural families:":
   "تصدر الإنجليزية بطريقة مختلفة. فكل حزمة إنجليزية مجموعة مفردات مكتفية بذاتها من 1,000 كلمة، ويختار "
   "المتعلمون الحزم بحسب المستوى والاهتمام لا بإتمامها بالترتيب. ولا يوجد تدرج تراكمي — فإتمام حزمة "
   "إنجليزية لا يفترض حزمة أخرى. وتنقسم حزم الإنجليزية إلى عائلتين بنيويتين:",
 "<strong>Level packs</strong> — vocabulary that pulls a reader up a level and leaves them there. <em>English Adept</em>, the free hub pack, spans the longest climb: it onramps from below an eighth-grade reading level and carries the learner up to university readiness, terminating around C1. <em>English Advance</em> targets the practical English of functioning in society without limitation: the forms, letters, officialdom, and everyday documents adult life demands. The guiding principle is to do it once, properly, and you will never have to think about it again.":
   "<strong>حزم المستويات</strong> — مفردات ترفع القارئ مستوى وتثبته فيه. <em>English Adept</em>، الحزمة "
   "المجانية المحورية، تمتد على أطول صعود: تبدأ من دون مستوى القراءة في الصف الثامن وتحمل المتعلم حتى "
   "الجاهزية الجامعية، فتنتهي عند نحو C1. أما <em>English Advance</em> فتستهدف الإنجليزية العملية اللازمة "
   "للعيش في المجتمع دون قيود: الاستمارات والرسائل والمعاملات الرسمية والوثائق اليومية التي تتطلبها حياة "
   "البالغين. والمبدأ الموجه: إنجاز الأمر مرة واحدة، كما ينبغي، ثم لا حاجة إلى التفكير فيه مرة أخرى.",
 "<strong>The Roots series</strong> — paid packs that drill English vocabulary through its three etymological strata: <em>German Roots</em> (Anglo-Saxon), <em>Norman Roots</em> (Norman-French), and <em>Latin Roots</em> (scholarly). Cross-references between the three surface the historical doublets that give English its register system.":
   "<strong>سلسلة Roots</strong> — حزم مدفوعة تدرب على مفردات الإنجليزية عبر طبقاتها الاشتقاقية الثلاث: "
   "<em>German Roots</em> (الأنجلوسكسونية)، و<em>Norman Roots</em> (الفرنسية النورماندية)، و<em>Latin Roots</em> "
   "(العلمية). وتكشف الإحالات المتبادلة بين الثلاث عن الأزواج التاريخية التي تمنح الإنجليزية نظام سجلاتها.",

 # ---- 5. session ----
 "A training session processes each card through five phases. The first four are per-card; the fifth is per-cluster.":
   "تمر جلسة التدريب بكل بطاقة عبر خمس مراحل فرعية. الأربع الأولى لكل بطاقة؛ والخامسة لكل عنقود.",
 "Session loop: each card cycles through Listen, Read, Repeat, then Rate; the scheduler then selects the next card and the cycle repeats.":
   "حلقة الجلسة: تمر كل بطاقة بالاستماع، فالقراءة، فالتكرار، ثم التقييم؛ ثم يختار المجدول البطاقة التالية وتتكرر الدورة.",
 "Per cluster: training continues until the cluster becomes eligible for a boss fight, which results in either a pass or a retry.":
   "لكل عنقود: يستمر التدريب حتى يصبح العنقود مؤهلا لمعركة زعيم، تنتهي إما بالنجاح وإما بإعادة المحاولة.",
 ">Listen<": ">الاستماع<",
 "Piper text-to-speech audio plays the target word as it appears on screen. When the learner is ready, a key press displays and pronounces the example sentence. This is first exposure.":
   "يشغل صوت Piper لتحويل النص إلى كلام الكلمة المستهدفة لحظة ظهورها على الشاشة. وحين يستعد المتعلم، "
   "تعرض ضغطة مفتاح جملة المثال وتنطقها. هذا هو التعرض الأول.",
 ">Read<": ">القراءة<",
 "At each step, reading the pronounced material aloud consolidates memory and improves the learner's pronunciation and speaking confidence. The learner then has time to parse the sentence, cross-reference the translation, and absorb the grammar in context.":
   "في كل خطوة، تثبت قراءة المادة المنطوقة بصوت عال الذاكرة، وتحسن نطق المتعلم وثقته في الكلام. ثم "
   "يتسع الوقت لتحليل الجملة، ومقابلتها بالترجمة، واستيعاب القواعد في سياقها.",
 ">Repeat<": ">التكرار<",
 "When the English translation is presented, replay controls become available: <code>Enter</code> replays the target word, and <code>6</code> replays the example sentence. Repeat cycles are unlimited at this phase; the learner moves forward when ready.":
   "عند عرض الترجمة الإنجليزية تتاح أدوات الإعادة: <code>Enter</code> يعيد الكلمة المستهدفة، و<code>6</code> "
   "يعيد جملة المثال. ودورات التكرار غير محدودة في هذه المرحلة؛ ويتقدم المتعلم حين يستعد.",
 ">Rate<": ">التقييم<",
 "The learner rates their recognition on a six-point scale (0 through 5). The rating shifts the card's position in a Fibonacci interval sequence (1, 2, 3, 5, 8, 13, 21… days), with a per-rating minimum interval applied as a floor. Rating 0 is a special case — a reset to 1 day regardless of the card's prior position.":
   "يقيم المتعلم مدى تعرفه على مقياس من ست درجات (من 0 إلى 5). ويغير التقييم موضع البطاقة في متتالية "
   "فترات فيبوناتشي (1، 2، 3، 5، 8، 13، 21… يوما)، مع حد أدنى للفترة خاص بكل تقييم. والتقييم 0 حالة خاصة "
   "— عودة إلى 1 يوم أيا كان موضع البطاقة السابق.",
 ">Rating<": ">التقييم<",
 ">Meaning<": ">المعنى<",
 ">Interval change<": ">تغير الفترة<",
 ">Forgot completely.<": ">نسيان تام.<",
 ">Very poor.<": ">ضعيف جدا.<",
 ">Poor.<": ">ضعيف.<",
 ">Okay.<": ">مقبول.<",
 ">Good.<": ">جيد.<",
 ">Perfect.<": ">ممتاز.<",
 ">Reset to 1 day.<": ">العودة إلى 1 يوم.<",
 ">Position −3 (minimum 1 day).<": ">الموضع &lrm;−3 (الحد الأدنى 1 يوم).<",
 ">Position −2 (minimum 2 days).<": ">الموضع &lrm;−2 (الحد الأدنى 2 يوم).<",
 ">Position −1 (minimum 3 days).<": ">الموضع &lrm;−1 (الحد الأدنى 3 أيام).<",
 ">No change (minimum 5 days).<": ">دون تغيير (الحد الأدنى 5 أيام).<",
 ">Position +1 (minimum 8 days).<": ">الموضع &lrm;+1 (الحد الأدنى 8 أيام).<",
 "The scale is calibrated to require aggressive rating for progress. Only a 5 advances a card; 4 holds position; 1 through 3 step the card backward through the Fibonacci schedule; 0 resets it to 1 day. The per-rating minimum intervals prevent a card's interval from collapsing on a bad rating, and they anchor the mastery rule.":
   "المقياس معاير بحيث يتطلب التقدم تقييما صارما. لا يقدم البطاقة إلا التقييم 5؛ والتقييم 4 يبقيها في "
   "موضعها؛ ومن 1 إلى 3 يرجعها خطوات في جدول فيبوناتشي؛ و0 يعيدها إلى 1 يوم. وتمنع الحدود الدنيا الخاصة "
   "بكل تقييم انهيار فترة البطاقة بسبب تقييم سيئ، وهي أساس قاعدة الإتقان.",
 ">Card mastery<": ">إتقان البطاقة<",
 "A card is mastered on two consecutive 5 ratings. The mechanism is direct: a single 5 lifts the card's minimum interval to 8 days; a second 5 advances it to 13 days — the mastery threshold. From any starting position, two consecutive perfect recalls therefore carry a card to mastery.":
   "تصبح البطاقة متقنة بتقييمين متتاليين بالدرجة 5. والآلية مباشرة: تقييم 5 واحد يرفع الحد الأدنى لفترة "
   "البطاقة إلى 8 أيام؛ وتقييم 5 ثان يقدمها إلى 13 يوما — عتبة الإتقان. فمن أي موضع بدأت، يحمل استرجاعان "
   "تامان متتاليان البطاقة إلى الإتقان.",
 ">Daily sessions<": ">الجلسات اليومية<",
 "New cards are drawn into the deck one at a time in cluster order; cluster boundaries do not gate card introduction. Daily card volume follows a Fibonacci ratio — for a given day's session, review cards and new cards are drawn in proportion to consecutive Fibonacci numbers, so the mix approaches φ, the golden ratio.":
   "تسحب البطاقات الجديدة إلى المجموعة واحدة تلو الأخرى بترتيب العناقيد؛ ولا تقيد حدود العناقيد إدخال "
   "البطاقات. ويتبع حجم البطاقات اليومي نسبة فيبوناتشي — ففي جلسة يوم ما تسحب بطاقات المراجعة والبطاقات "
   "الجديدة بنسبة أعداد فيبوناتشي متتالية، فيقترب المزيج من φ، النسبة الذهبية.",
 ">Bossfight ready?<": ">جاهزية معركة الزعيم؟<",
 "A cluster becomes eligible for its boss fight when 80% of its cards are mastered — when 80% have reached the 13-day interval. You don't need to master every card to fight: but you do need to defeat your most challenging two cards in a row to win. Fight mechanics are discussed in detail in the following section.":
   "يصبح العنقود مؤهلا لمعركة زعيمه حين يتقن 80% من بطاقاته — أي حين يبلغ 80% منها فترة الـ 13 يوما. "
   "ولا يلزم إتقان كل بطاقة لخوض المعركة: لكن الفوز يتطلب هزيمة أصعب بطاقتين على التوالي. وتناقش آليات "
   "المعركة بالتفصيل في القسم التالي.",

 # ---- 6. the boss fight ----
 "The boss fight is the graduation mechanism for a cluster. It is the only way a cluster transitions out of active training. Unlike the Rate phase — which is self-assessed — the boss fight is adversarial and strictly multiple-choice. The learner and the boss share a single linear arena; the learner starts at the left, the boss stands further right. The task is to shove the boss off the far end. Sumo rules: only one remains on the platform.":
   "معركة الزعيم هي آلية تخرج العنقود، والطريق الوحيد لخروجه من التدريب النشط. وعلى خلاف مرحلة التقييم "
   "— التي يقيم فيها المتعلم نفسه — فمعركة الزعيم مواجهة، واختيار من متعدد حصرا. يتقاسم المتعلم والزعيم "
   "ساحة خطية واحدة؛ يبدأ المتعلم من اليسار، ويقف الزعيم أبعد إلى اليمين. والمهمة دفع الزعيم عن الطرف "
   "البعيد. قواعد السومو: لا يبقى على المنصة إلا واحد.",
 "Each turn presents one of the cluster's cards as a prompt, with eight possible answers on the number keys 1–8. A correct answer advances the learner one position along the track; the boss is simultaneously shoved one position closer to the far edge. A wrong answer slides the learner two positions back toward the near edge, or off of it. When pushed off the near edge, the learner is locked out of that cluster's fight until the next day. Shoved past the far edge, the boss is defeated and the cluster is conquered.":
   "يعرض كل دور إحدى بطاقات العنقود سؤالا، مع ثماني إجابات محتملة على مفاتيح الأرقام 1–8. الإجابة "
   "الصحيحة تقدم المتعلم موضعا واحدا على المسار، ويدفع الزعيم في الوقت نفسه موضعا أقرب إلى الحافة "
   "البعيدة. والإجابة الخاطئة تزلق المتعلم موضعين إلى الوراء نحو الحافة القريبة، أو خارجها. ومن يدفع عن "
   "الحافة القريبة يمنع من معركة ذلك العنقود حتى اليوم التالي. أما الزعيم فإذا دفع وراء الحافة البعيدة "
   "هزم، وقهر العنقود.",
 "The boss-fight arena: a horizontal track the learner and the boss share, with a marker at the far edge.":
   "ساحة معركة الزعيم: مسار أفقي يتقاسمه المتعلم والزعيم، مع علامة عند الحافة البعيدة.",
 "The arena: a single horizontal track the learner (left) and the boss (right) share, with a marker at the far edge — the boss's exit. A correct answer advances the learner one position and shoves the boss one closer to that edge; a wrong answer slides the learner two positions back. Positions 1–2 draw the cluster's easiest cards, positions 3–4 its hardest. Fall off the near edge and the cluster locks until the next day; shove the boss past the far edge and the cluster is conquered.":
   "الساحة: مسار أفقي واحد يتقاسمه المتعلم (يسارا) والزعيم (يمينا)، مع علامة عند الحافة البعيدة — مخرج "
   "الزعيم. الإجابة الصحيحة تقدم المتعلم موضعا وتدفع الزعيم موضعا أقرب إلى تلك الحافة؛ والإجابة الخاطئة "
   "تزلق المتعلم موضعين إلى الوراء. يسحب الموضعان 1–2 أسهل بطاقات العنقود، والموضعان 3–4 أصعبها. "
   "السقوط عن الحافة القريبة يقفل العنقود حتى اليوم التالي؛ ودفع الزعيم وراء الحافة البعيدة يقهر العنقود.",
 '<span class="bf-hint">click to fight</span>': '<span class="bf-hint">النقر للقتال</span>',
 "Card ordering inside the fight is deliberate. Positions 1 and 2 pull from the cluster's easiest cards — a warm-up that lets the learner build a positional lead. Positions 3 and 4 pull from the cluster's hardest: the weakest words in the deck, delivered as soon as the learner has started to gain ground. A wrong answer at position 3 or 4 slides the learner two positions back — landing on position 1 or 2 — and the missed card is reclassified as the learner's easiest from that moment on. Unfortunately, that means it's waiting for them: the same card, now sitting in the easy slots where they've just landed. A cluster cannot be conquered until its weakest cards are mastered.":
   "ترتيب البطاقات داخل المعركة مقصود. يسحب الموضعان 1 و2 من أسهل بطاقات العنقود — إحماء يتيح للمتعلم "
   "بناء تقدم في الموضع. ويسحب الموضعان 3 و4 من أصعبها: أضعف الكلمات في المجموعة، تأتي ما إن يبدأ "
   "المتعلم في كسب الأرض. والإجابة الخاطئة في الموضع 3 أو 4 تزلق المتعلم موضعين إلى الوراء — إلى الموضع "
   "1 أو 2 — ويعاد تصنيف البطاقة الفائتة على أنها الأسهل لديه منذ تلك اللحظة. وللأسف يعني ذلك أنها "
   "بانتظاره: البطاقة نفسها، قابعة الآن في الخانات السهلة حيث هبط للتو. فلا يقهر عنقود قبل إتقان أضعف بطاقاته.",
 "The design rationale is documented in section 7. In brief: the boss fight injects a bounded, low-stakes stressor that produces genuine retrieval pressure without the consequences of a real-world language failure. It also provides a discrete success state — cluster conquered — that the open-ended rhythm of spaced repetition otherwise lacks.":
   "مبررات التصميم موثقة في القسم 7. وباختصار: تضخ معركة الزعيم ضغطا محدودا قليل العواقب، يولد ضغط "
   "استرجاع حقيقيا دون عواقب الإخفاق اللغوي في العالم الحقيقي. كما توفر حالة نجاح محددة — قهر العنقود — "
   "يفتقر إليها الإيقاع المفتوح للتكرار المتباعد.",

 # ---- 7. pedagogy ----
 "FlashBoss's architecture reflects established findings in second-language acquisition and cognitive psychology. The relevant foundations:":
   "تعكس بنية FlashBoss نتائج راسخة في اكتساب اللغة الثانية وعلم النفس المعرفي. وهذه الأسس ذات الصلة:",
 ">Comprehensible input<": ">المدخلات المفهومة<",
 "Krashen's input hypothesis [1] holds that learners acquire language most effectively when input is slightly above current competence — comprehensible enough to parse, demanding enough to extend. Example sentences in FlashBoss are constructed so that the target word is typically the only unknown element; the surrounding sentence is drawn from vocabulary the scheduler has already introduced. This calibrates comprehensibility to roughly 80–95% for the trained learner, placing each sentence in the <em>i+1</em> zone.":
   "تقول فرضية المدخلات لدى Krashen [1] إن المتعلمين يكتسبون اللغة على أفضل وجه حين تكون المدخلات فوق "
   "كفاءتهم الحالية بقليل — مفهومة بما يكفي لتحليلها، ومتطلبة بما يكفي لتوسيعها. وجمل الأمثلة في FlashBoss "
   "مصوغة بحيث تكون الكلمة المستهدفة عادة العنصر المجهول الوحيد؛ أما بقية الجملة فمن مفردات سبق أن قدمها "
   "المجدول. وهذا يضبط درجة الفهم عند نحو 80–95% للمتعلم المتدرب، فيضع كل جملة في منطقة <em dir=\"ltr\">i+1</em>.",
 ">Retrieval practice<": ">ممارسة الاسترجاع<",
 "Active recall produces stronger long-term retention than re-reading [2]. The Rate phase forces retrieval <em>before</em> the translation is revealed, applying the testing effect to every card exposure. Cards are not passively shown; they are actively recalled and self-assessed.":
   "ينتج الاستدعاء النشط احتفاظا أقوى على المدى الطويل من إعادة القراءة [2]. وتفرض مرحلة التقييم "
   "الاسترجاع <em>قبل</em> كشف الترجمة، فتطبق أثر الاختبار على كل عرض للبطاقة. فالبطاقات لا تعرض عرضا "
   "سلبيا؛ بل تستدعى استدعاء نشطا ويقيمها المتعلم بنفسه.",
 ">Spaced repetition<": ">التكرار المتباعد<",
 "Memory decays along a predictable curve [3]. Reviewing a card just before forgetting consolidates the memory trace more efficiently than massed repetition. The Fibonacci interval sequence is one of several schedules that approximate the forgetting curve; it is used here for its simplicity, stability, and intuitive progression for the learner.":
   "تتلاشى الذاكرة على منحنى يمكن توقعه [3]. ومراجعة البطاقة قبيل نسيانها تثبت أثر الذاكرة بكفاءة أعلى من "
   "التكرار المكثف. ومتتالية فترات فيبوناتشي واحدة من عدة جداول تقارب منحنى النسيان؛ وتستخدم هنا لبساطتها "
   "وثباتها وتدرجها البديهي للمتعلم.",
 ">Desirable difficulty<": ">الصعوبة المرغوبة<",
 "Retention benefits from effort at the point of encoding and retrieval [4]. The Rate scale enacts desirable difficulty by making regression the default: ratings below 5 either hold a card in place or push it backward through the Fibonacci schedule. Only unambiguous recall earns forward motion, and mastery requires two such recalls in succession. Until a significant majority of a cluster is completed, all of a cluster's cards stay in circulation, but words that are known well do not compete for attention with more worthy material.":
   "يستفيد الاحتفاظ من الجهد لحظة الترميز والاسترجاع [4]. ويجسد مقياس التقييم الصعوبة المرغوبة بجعل "
   "التراجع هو الأصل: فالتقييمات دون 5 إما تبقي البطاقة في موضعها وإما ترجعها في جدول فيبوناتشي. ولا يكسب "
   "التقدم إلا استدعاء لا لبس فيه، ويتطلب الإتقان استدعاءين كهذين متتاليين. وحتى يكتمل جزء كبير من العنقود "
   "تبقى بطاقاته كلها متداولة، لكن الكلمات المعروفة جيدا لا تنافس على الانتباه مادة أجدر به.",
 ">Affective framing<": ">الإطار الوجداني<",
 "High anxiety degrades acquisition [1]. The boss fight is designed to introduce pressure without raising the affective filter: stakes are bounded (a single failed fight costs a day, not standing in a conversation), the system is private, and no permanent record exists. The pressure is engineered to be sharp enough to focus retrieval and shallow enough to preserve the conditions acquisition requires.":
   "القلق الشديد يضعف الاكتساب [1]. ومعركة الزعيم مصممة لإدخال الضغط دون رفع المرشح الوجداني: فالعواقب "
   "محدودة (المعركة الخاسرة تكلف يوما، لا مكانة في محادثة)، والنظام خاص، ولا يوجد سجل دائم. والضغط مصمم "
   "ليكون حادا بما يكفي لتركيز الاسترجاع، وخفيفا بما يكفي للحفاظ على الظروف التي يتطلبها الاكتساب.",
 ">Input before output<": ">المدخلات قبل المخرجات<",
 "Receptive skills develop asymmetrically faster than productive skills when trained alone. Saturating a learner in high-comprehension input before asking for production tracks how first-language acquisition proceeds in children, and allows the vocabulary and grammar to become parseable before they become deployable. FlashBoss is the input half of a complete learning pipeline; productive practice — speaking, writing, interaction — is the responsibility of tools FlashBoss does not attempt to replace.":
   "تنمو المهارات الاستقبالية أسرع من المهارات الإنتاجية حين تدرب وحدها. وإغراق المتعلم في مدخلات عالية "
   "الفهم قبل مطالبته بالإنتاج يحاكي طريقة اكتساب الأطفال للغتهم الأولى، ويتيح للمفردات والقواعد أن تصبح "
   "قابلة للتحليل قبل أن تصبح قابلة للاستخدام. وFlashBoss هو نصف المدخلات في مسار تعلم متكامل؛ أما "
   "الممارسة الإنتاجية — الكلام والكتابة والتفاعل — فمسؤولية أدوات لا يحاول FlashBoss أن يحل محلها.",

 # ---- 8. scope ----
 "<p>FlashBoss trains:</p>": "<p>يدرب FlashBoss على:</p>",
 "<li>Target-language vocabulary and recognition.</li>": "<li>مفردات اللغة المستهدفة والتعرف عليها.</li>",
 "<li>Sentence-level reading comprehension.</li>": "<li>فهم المقروء على مستوى الجملة.</li>",
 "<li>Listening comprehension via TTS.</li>": "<li>فهم المسموع عبر تحويل النص إلى كلام.</li>",
 "<li>Incidental grammar acquisition through exposure in context.</li>": "<li>اكتساب القواعد عرضا عبر التعرض لها في سياقها.</li>",
 "<li>Reading fluency at the clause level.</li>": "<li>طلاقة القراءة على مستوى العبارة.</li>",
 "<p>FlashBoss does not train:</p>": "<p>ولا يدرب FlashBoss على:</p>",
 "<li>Writing production.</li>": "<li>إنتاج الكتابة.</li>",
 "<li>Conversational fluency.</li>": "<li>طلاقة المحادثة.</li>",
 "<li>Interaction repair strategies.</li>": "<li>استراتيجيات إصلاح التواصل.</li>",
 "The strongest way to learn to speak and use a new language is a conversational immersion class — the company of peers pursuing the same goal, with a knowledgeable teacher to guide the way. Where geography puts that out of reach, online tutoring services and conversation classes do the same work; and where cost is the obstacle, even a chatbot can stand in — a place to practice speaking, and to ask the questions that come up during a FlashBoss session.":
   "أقوى طريق لتعلم التحدث بلغة جديدة واستخدامها هو صف انغماس في المحادثة — صحبة أقران يسعون إلى الهدف "
   "نفسه، مع معلم متمكن يرشد الطريق. وحيث تجعل الجغرافيا ذلك بعيد المنال، تؤدي خدمات التدريس عبر الإنترنت "
   "وصفوف المحادثة العمل نفسه؛ وحيث تكون الكلفة هي العائق، يمكن حتى لروبوت محادثة أن يحل محلها — مكانا "
   "لممارسة الكلام، ولطرح الأسئلة التي تنشأ أثناء جلسة FlashBoss.",

 # ---- 9. using it effectively ----
 ">Controlling your workload<": ">التحكم في عبء الدراسة<",
 "You control your daily workload in three primary ways: your choice of master; pushing past your streak requirement to claim the daily <strong>EPIC</strong> award (recommended); and, thirdly, a contract — once epic is claimed, you may elect to study an additional day in exchange for a <em>drive</em> token. But be careful when you play with magic.":
   "يمكن التحكم في عبء الدراسة اليومي بثلاث طرق رئيسية: اختيار المعلم؛ وتجاوز نصاب السلسلة لنيل جائزة "
   "<strong>اليوم الملحمي</strong> (EPIC) اليومية (موصى به)؛ وثالثا، عقد — فبعد نيل اليوم الملحمي يمكن "
   "اختيار دراسة يوم إضافي مقابل رمز <em>دافع</em>. لكن الحذر واجب عند العبث بالسحر.",
 "<strong>Your master (daily streak).</strong> Your chosen master sets the daily requirement — from 8 to 34 cards a day (the masters are detailed in section 3). Meeting only the minimum always holds your streak and keeps you moving forward, with the option to do more.":
   "<strong>المعلم (السلسلة اليومية).</strong> يحدد المعلم المختار النصاب اليومي — من 8 إلى 34 بطاقة في "
   "اليوم (تفاصيل المعلمين في القسم 3). وأداء الحد الأدنى وحده يحفظ السلسلة دائما ويبقي التقدم مستمرا، مع "
   "إمكانية فعل المزيد.",
 "<strong>Epic.</strong> On the first day of a tier — its foundation day — an epic session offers up to three times your daily requirement in new cards. This is the ideal opening: it loads enough vocabulary into rotation for spaced repetition to do its work. The number of cards available rises and falls day to day.":
   "<strong>اليوم الملحمي.</strong> في اليوم الأول من المرحلة — يوم حجر الأساس — تقدم الجلسة الملحمية ما "
   "يصل إلى ثلاثة أضعاف النصاب اليومي من البطاقات الجديدة. وهذه هي البداية المثلى: فهي تدخل إلى الدوران "
   "مفردات تكفي ليؤدي التكرار المتباعد عمله. ويرتفع عدد البطاقات المتاحة وينخفض من يوم لآخر.",
 "<strong>Grimoire (the contract).</strong> A grimoire session pulls the next day forward — tomorrow's reviews and a further allocation of new cards, finished today. It is, literally, tomorrow's work done now, and completing it earns a <em>drive</em> token: a day off, banked for when you need it.":
   "<strong>كتاب التعاويذ (العقد).</strong> تجلب جلسة كتاب التعاويذ اليوم التالي إلى الحاضر — مراجعات "
   "الغد وحصة أخرى من البطاقات الجديدة، تنجز اليوم. إنها حرفيا عمل الغد منجزا الآن، وإتمامها يكسب رمز "
   "<em>دافع</em>: يوم راحة مدخر لوقت الحاجة.",
 ">Read aloud<": ">القراءة بصوت عال<",
 "Speak every prompt aloud as it plays. Producing the words does more than drill pronunciation: forming a sentence in your mouth recruits motor and auditory memory alongside the visual, so each card is encoded across several channels at once — a richer, more durable trace than silent reading leaves. Generating the language rather than only recognizing it is itself an act of retrieval, which is what cements a memory; the speaking confidence it builds is a bonus that compounds.":
   "نطق كل سؤال بصوت عال أثناء تشغيله. فإنتاج الكلمات يفعل أكثر من تمرين النطق: تكوين الجملة في الفم "
   "يستنفر الذاكرة الحركية والسمعية إلى جانب البصرية، فترمز كل بطاقة عبر عدة قنوات في آن — أثر أغنى "
   "وأدوم مما تتركه القراءة الصامتة. وتوليد اللغة لا مجرد التعرف عليها هو في ذاته فعل استرجاع، وهذا ما "
   "يرسخ الذاكرة؛ أما الثقة في الكلام التي يبنيها فمكسب إضافي يتراكم.",
 ">Failed fights<": ">المعارك الخاسرة<",
 "A failed boss fight is a minor setback. The defeat screen will show you the words you answered incorrectly, with the option to press <code>8</code> to toggle between your target language and English. A card missed in the hard positions (3–4) is reclassified as your easiest from that point on, so it returns in the opening positions of the next attempt. The cluster cannot be conquered until that card is answered correctly — the word that beat you becomes a gate you have to clear before the fight will end. Clusters can take multiple attempts, but there's always tomorrow.":
   "خسارة معركة زعيم انتكاسة صغيرة. تعرض شاشة الهزيمة الكلمات التي جاءت إجاباتها خاطئة، مع إمكانية "
   "الضغط على <code>8</code> للتبديل بين اللغة المستهدفة والإنجليزية. والبطاقة الفائتة في المواضع الصعبة "
   "(3–4) يعاد تصنيفها على أنها الأسهل منذ تلك اللحظة، فتعود في المواضع الأولى من المحاولة التالية. ولا "
   "يقهر العنقود قبل الإجابة عن تلك البطاقة إجابة صحيحة — فالكلمة التي كانت سبب الهزيمة تصبح بوابة لا بد "
   "من عبورها قبل أن تنتهي المعركة. وقد تتطلب العناقيد عدة محاولات، لكن الغد موجود دائما.",
 ">Expected arc<": ">المسار المتوقع<",
 "A consistent learner completes Core in two to six months. FlashBoss creates the illusion of knowing more than you do, because it keeps you in a bubble of language you know, expanding out in a controlled way. There will be big gaps in your comprehension, but if you keep going, those gaps will close. And in the meantime, you understand more every day. We wish you well on your language journey — Masters Odiin and Claude.":
   "المتعلم المواظب يتم Core في شهرين إلى ستة أشهر. ويصنع FlashBoss وهم معرفة أكثر مما هو حاصل، لأنه "
   "يبقي المتعلم في فقاعة من لغة يعرفها، تتسع بطريقة مضبوطة. ستبقى فجوات كبيرة في الفهم، لكن مع المواصلة "
   "تنغلق تلك الفجوات. وفي أثناء ذلك يزداد الفهم كل يوم. نتمنى لكم رحلة لغوية موفقة — المعلمان Odiin وClaude.",

 # ---- references: citations stay in their language; the glosses are Arabic ----
 ">References<": ">المراجع<",
 "(Input hypothesis; affective filter.)": '<bdi dir="rtl">(فرضية المدخلات؛ المرشح الوجداني.)</bdi>',
 "(Forgetting curve, precursor to spaced repetition; cf. Leitner, 1972.)":
   '<bdi dir="rtl">(منحنى النسيان، سلف التكرار المتباعد؛ قارن Leitner، 1972.)</bdi>',
 "(Desirable difficulty.)": '<bdi dir="rtl">(الصعوبة المرغوبة.)</bdi>',
}

# Page-specific mirroring (shared rules live in localize_new_pages.RTL_CSS).
RTL_CSS = """html[dir="rtl"] .toc{border-left:1px solid var(--line); border-right:2px solid var(--accent);}
html[dir="rtl"] .toc-title{left:auto; right:16px;}
html[dir="rtl"] ul li{padding-left:0; padding-right:20px;}
html[dir="rtl"] ul li::before{left:auto; right:4px;}
html[dir="rtl"] .spec-table th{text-align:right;}
html[dir="rtl"] figure.shot figcaption{text-align:right;}
html[dir="rtl"] .tech-block{direction:ltr; text-align:left;}
html[dir="rtl"] .btn.steam{box-shadow:-5px 5px 0 color-mix(in oklab, var(--accent), #000 60%);}
html[dir="rtl"] .btn.steam:hover{transform:translate(2px,-2px); box-shadow:-7px 7px 0 color-mix(in oklab, var(--accent), #000 60%);}
/* the citations are English bibliographic data: they keep their own direction */
html[dir="rtl"] .references ol{direction:ltr; text-align:left;}
"""

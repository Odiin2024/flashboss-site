# Russian strings for latin.html — the Latin LANGUAGE COURSE page
# (Latin Core + Latin Pareto), not the Latin Roots English pack.
#
# Keys are the key set of scripts/l10n/latin_de.py, in the same order — that
# module is the spec for this page.
#
# WHERE THE WORDING COMES FROM, in order of authority:
#   * the CLUSTER NAMES are the ones the game ships for ru, copied from the
#     authoritative list, not coined here. Where the English joins two halves
#     with "&amp;" the shipped Russian name joins them with "и" ("Сенат и меч"),
#     so the ampersand entity goes with it — the player has to read the same
#     words on the page and in the game.
#   * the bundle name is the ratified Russian one from the Latin paste sheet
#     (flashboss-admin/BUNDLE_COPY_LATIN_2026-09-08.md): "FlashBoss Латинский —
#     Полный курс". The Steam URLs and app IDs are untouched.
#   * "Уже владеете частью? Steam возьмёт плату только за остальное." is the
#     ratified Russian bundle sentence.
#   * shared page furniture follows french.ru.html, the fleet-translated sibling
#     of this same template: "вся карта", "видно с первого взгляда", "смотрите,
#     как оно взрослеет", "не просто список слов", "как это запоминается",
#     "Карточки как единая система", "нажмите, чтобы перевернуть", "Интервалы по
#     Фибоначчи", "Выпуск", "Озвучка", "Ваш язык", "Вопросы", "Уровень N",
#     the Windows Terminal answer and the demo answer, and the page title shape
#     "<Язык> — FlashBoss". The hero alt is the string the other Russian pages
#     already carry.
#   * site vocabulary follows the immersion glossary and the live Russian pages:
#     набор (pack, never «пакет»), базовая игра, карточка, заглавное слово,
#     справочный урок, кластер, бой с боссом, списки слов, главная, материалы.
#
# THREE DELIBERATE DEPARTURES from french.ru.html, all toward the settled
# glossary and the ratified Latin sheet, flagged for the owner:
#   * "кластер", not french.ru's "блок" — the ratified Russian Latin copy says
#     кластер, and so do immersion.ru and swahili.ru.
#   * "бой с боссом", not french.ru's "босс-файт" — the settled glossary word.
#   * the sig line is infinitives ("Слушать · Читать · …"), as swahili.ru does,
#     rather than french.ru's ты-imperatives, because the rest of this page
#     addresses the reader with вы.
#
# PAGE CANON, held here:
#   * LATIN IS NEVER TRANSLATED. Every Latin sentence, every headword and its
#     dictionary shorthand (virtūs, f., -is / faciō, -iō, -ere / malum, n., -ī),
#     the minimal pairs, the epigraph and every siglum (Caes. BG 5.44.5,
#     Cic. Verr. 2.2.108, Sall. Cat. 60.7) stay byte-identical. Only the
#     surrounding explanation and the glosses become Russian.
#   * pack names stay English and are never declined: Latin Core, Latin Pareto,
#     Core, Pareto. So does FlashBoss. "Latin Pareto" is the store name — never
#     "Pareto 1", which is what the ratified sheet still calls it.
#   * the counts are the 2026-09-19 recount the English page carries: Core 26
#     reference lessons, Pareto 18, 44 in all, 80 clusters, 2000 cards, ten
#     уровней. Nothing here is recounted, and where the bundle sheet disagrees
#     the page wins.
#   * Russian writes a thousand with no separator (2000, 17007, 30000) — the
#     value the build would produce from the English page's comma, written out
#     directly.
#   * banned and absent: hours, CEFR codes, prices, discounts, and a release
#     date for anything already on sale.
TITLE = "Латинский — FlashBoss"
DESCRIPTION = ("FlashBoss Латинский: курс чтения на 2000 слов в десяти уровнях и восьмидесяти "
               "кластерах, 44 справочных урока, заглавные слова с макронами и примеры предложений, "
               "которые заканчиваются неадаптированными Цезарем, Цицероном, Саллюстием, Непотом и "
               "Ливием. Latin Core и Latin Pareto уже в Steam.")

STRINGS = {
 # ---- nav / chrome ----
 ">home<": ">главная<",
 ">packs<": ">наборы<",
 ">resources<": ">материалы<",
 ">walkthrough (beta)<": ">руководство (бета)<",
 '<span class="here">Latin</span>': '<span class="here">Латинский</span>',

 # ---- hero ----
 "FlashBoss — the moonlit school that fronts every FlashBoss course":
   "FlashBoss — залитая лунным светом школа, с которой начинается каждый курс",
 "Two packs · <b>2,000 words</b> · ten tiers · 44 lessons · out now on Steam":
   "Два набора · <b>2000 слов</b> · десять уровней · 44 урока · уже в Steam",
 "Read real Latin. Not books about it.": "Читайте настоящую латынь. Не книги о ней.",
 "Listen · Read · Repeat · Rate · Fight": "Слушать · Читать · Повторять · Оценивать · Сражаться",
 "Two thousand words, ten tiers, one skill. The sentences start built for you and end as <b>Caesar, Cicero, Sallust, Nepos and Livy actually wrote them</b> — nothing trimmed but length, nothing invented.":
   "Две тысячи слов, десять уровней, один навык. Предложения начинаются построенными под вас и заканчиваются так, <b>как их на самом деле написали Цезарь, Цицерон, Саллюстий, Непот и Ливий</b> — урезана только длина, не выдумано ничего.",
 ">Word Lists<": ">Списки слов<",
 ">Lessons<": ">Уроки<",
 ">Try the demo<": ">Попробовать демо<",

 # ---- the argument: one skill, and the order that teaches it ----
 "Latin course design": "устройство латинского курса",
 "One skill: reading": "Один навык: чтение",
 "Legendō discitur — it is learned by reading.":
   "Legendō discitur — этому учатся, читая.",
 "Nothing here asks you to compose Latin of your own. The whole course is built so that you can look at a printed line and know what it says — and it gets you there by putting you in front of sentences from the very first tier, not by making you wait until the grammar is finished.":
   "Здесь никто не просит вас сочинять латынь самостоятельно. Весь курс построен так, чтобы вы могли взглянуть на печатную строку и понять, что в ней сказано, — и ведёт он к этому, ставя перед вами предложения с самого первого уровня, а не заставляя ждать, пока закончится грамматика.",
 "The order is the argument. Two thousand lemmas are laid down in ten tiers, each tier eight clusters of twenty-five cards, and the grammar arrives one lesson at a time at the exact card that first needs it. No example sentence ever uses grammar you have not been taught. By Tier 10 the ladder has nothing left to teach and you are reading Cicero unadapted — <b>17,007 words of Latin read in context</b> along the way.":
   "Порядок и есть довод. Две тысячи лемм уложены в десять уровней, в каждом уровне восемь кластеров по двадцать пять карточек, а грамматика приходит по одному уроку за раз — ровно на той карточке, которой она впервые нужна. Ни один пример предложения не пользуется грамматикой, которой вас ещё не учили. К уровню 10 лестнице больше нечему учить, и вы читаете Цицерона без адаптации — <b>17007 слов латыни, прочитанных в контексте</b> по дороге.",

 "Latin Core — tiers 1 to 5": "Latin Core — уровни с 1 по 5",
 "Latin Pareto — tiers 6 to 10": "Latin Pareto — уровни с 6 по 10",
 "The alphabet as Rome said it, the pointing words, the connectives, the prime movers, the first nouns of senate and sword.":
   "Алфавит так, как его произносил Рим, указательные слова, соединительные слова, движущие силы, первые существительные сената и меча.",
 "The accusative, the present tense, the imperative. The daily round, the forum, the body, counting and worth.":
   "Винительный падеж, настоящее время, повелительное наклонение. Ежедневный круг, форум, тело, счёт и достоинство.",
 "Genitive and dative, the full plural, two more conjugations, the imperfect. The road, the household, the turning year.":
   "Родительный и дательный падежи, полное множественное число, ещё два спряжения, имперфект. Путь, дом, год перемен.",
 "The ablative, the third declension, prepositions and case — and the first real Caesar, lightly adapted.":
   "Аблатив, третье склонение, предлоги и падеж — и первый настоящий Цезарь, слегка адаптированный.",
 "The perfect and its family, principal parts, relative clauses. Caesar is now on 86 of the 200 cards, and unadapted on 26 of them.":
   "Перфект и его семья, основные формы глагола, относительные придаточные. Цезарь теперь на 86 из 200 карточек, и на 26 из них — без адаптации.",
 "Participles, all three of them, and the passive. Caesar continues, and Nepos comes into his own.":
   "Причастия, все три, и пассив. Цезарь продолжается, а Непот входит в силу.",
 "The ablative absolute, the passive complete, deponents. Cicero's letters open the informal register.":
   "Ablativus absolutus, пассив целиком, отложительные глаголы. Письма Цицерона открывают неофициальный регистр.",
 "The infinitive family and reported speech. Sallust arrives; 192 of 200 cards are now unadapted.":
   "Семья инфинитивов и косвенная речь. Приходит Саллюстий; 192 из 200 карточек теперь без адаптации.",
 "The subjunctive, cum-clauses, purpose and result, indirect questions. Livy joins the roll.":
   "Конъюнктив, придаточные с cum, цель и следствие, косвенные вопросы. В строй встаёт Ливий.",
 "Gerund and gerundive, and how to read a citation. Cicero's speeches and philosophy close the trunk.":
   "Герундий и герундив, и как читать ссылку на источник. Речи и философия Цицерона замыкают ствол.",

 # ---- the sentence ladder: Latin stays Latin, the gloss becomes Russian ----
 "Watch it grow up": "смотрите, как оно взрослеет",
 "From made for you to written by Cicero": "От «построено для вас» до «написано Цицероном»",
 "One card's example sentence from each of the ten tiers, in order. Nothing below is a paraphrase: from Tier 4 the citations are real, and the unmarked ones are the author's own words.":
   "Пример предложения с одной карточки каждого из десяти уровней, по порядку. Ниже нет ни одного пересказа: с уровня 4 ссылки настоящие, а неотмеченные — собственные слова автора.",
 "<span class=\"en\">As you see, Caesar is one of ours.</span>":
   "<span class=\"en\">Как видишь, Цезарь — из наших.</span>",
 "<span class=\"en\">While Caesar is in Gaul, the senate approves the law.</span>":
   "<span class=\"en\">Пока Цезарь в Галлии, сенат одобряет закон.</span>",
 "<span class=\"en\">Our troops were already departing and abandoning the camp.</span>":
   "<span class=\"en\">Наши войска уже уходили и оставляли лагерь.</span>",
 "<span class=\"en\">The storms both kept our men in camp and held the enemy back from battle.</span>":
   "<span class=\"en\">Бури и наших удерживали в лагере, и врага не пускали в бой.</span>",
 "<span class=\"en\">There he reached the furthest ridge and drew up his line in that place.</span>":
   "<span class=\"en\">Там он вышел к самому дальнему хребту и на этом месте построил боевую линию.</span>",
 "<span class=\"en\">Not even Vorenus keeps himself behind the rampart then; fearing what everyone would think, he follows after.</span>":
   "<span class=\"en\">Даже Ворен не остаётся тогда за валом: боясь того, что подумают все, он идёт следом.</span>",
 "<span class=\"en\">All the ties of the closest friendship hold between him and me.</span>":
   "<span class=\"en\">Между ним и мной существуют все узы теснейшей близости.</span>",
 "<span class=\"en\">At home we have want, abroad debt, a bad case and a prospect much harsher still.</span>":
   "<span class=\"en\">Дома у нас нужда, за порогом долги, положение скверное, а виды на будущее куда суровее.</span>",
 "<span class=\"en\">Seeing his forces routed and himself left with a few, mindful of his birth and former standing, Catiline charges into the thickest of the enemy and there, fighting, is run through.</span>":
   "<span class=\"en\">Видя, что войска его разбиты, а сам он остался с немногими, Катилина, помня о своём роде и прежнем достоинстве, бросается в самую гущу врагов и там, сражаясь, гибнет пронзённый.</span>",
 "<span class=\"en\">You see that man with the rather curly hair, the dark one, who watches us with a look that makes him seem very sharp to himself.</span>":
   "<span class=\"en\">Видите вон того, с чуть вьющимися волосами, смуглого, который смотрит на нас с таким видом, будто сам себе кажется чрезвычайно проницательным.</span>",
 ">built for the tier<": ">построено под уровень<",
 ">adapted from Caes. BG 4.34.4<": ">адаптировано из Caes. BG 4.34.4<",

 # ---- whose Latin: the source arc ----
 "Whose Latin": "чья латынь",
 "The authors arrive in order": "Авторы появляются по порядку",
 "Tiers 1 to 3 have no citations at all, and say so: those sentences are built to a grammar ceiling, because real Latin has no register that simple. Caesar enters at Tier 4 and the scaffolding is gone by Tier 8.":
   "У уровней с 1 по 3 ссылок нет вовсе, и об этом сказано прямо: эти предложения построены под потолок грамматики, потому что у настоящей латыни нет такого простого регистра. Цезарь входит на уровне 4, а к уровню 8 строительные леса убраны.",
 ">Tiers 1–3<": ">Уровни 1–3<",
 "Sentences constructed to the tier's grammar — no author claimed, none implied":
   "Предложения, построенные под грамматику уровня, — автор не назван и не подразумевается",
 ">0 of 600 cited<": ">0 из 600 со ссылкой<",
 "Caesar, <i>Gallic War</i> — mostly clause-trimmed for length":
   "Цезарь, <i>Записки о Галльской войне</i> — в основном урезаны придаточные ради длины",
 ">62 cited · 13 unadapted<": ">62 со ссылкой · 13 без адаптации<",
 "Caesar throughout, Nepos beginning": "Цезарь повсюду, Непот начинается",
 ">86 cited · 26 unadapted<": ">86 со ссылкой · 26 без адаптации<",
 "Caesar and Nepos, <i>Lives</i>": "Цезарь и Непот, <i>Жизнеописания</i>",
 ">145 cited · 84 unadapted<": ">145 со ссылкой · 84 без адаптации<",
 "Cicero's letters — <i>ad Atticum</i>, <i>ad Familiares</i> — beside Caesar and Nepos":
   "Письма Цицерона — <i>ad Atticum</i>, <i>ad Familiares</i> — рядом с Цезарем и Непотом",
 ">170 cited · 109 unadapted<": ">170 со ссылкой · 109 без адаптации<",
 "Sallust joins; the adapting effectively stops":
   "Присоединяется Саллюстий; адаптация фактически прекращается",
 ">196 cited · 192 unadapted<": ">196 со ссылкой · 192 без адаптации<",
 "Livy Book 1 joins Sallust, Cicero and Caesar":
   "Ливий, книга 1, присоединяется к Саллюстию, Цицерону и Цезарю",
 ">197 cited · 195 unadapted<": ">197 со ссылкой · 195 без адаптации<",
 "Cicero's speeches and philosophy — the hardest band the trunk reaches":
   "Речи и философия Цицерона — самая трудная полоса, до которой доходит ствол",
 ">196 cited · 194 unadapted<": ">196 со ссылкой · 194 без адаптации<",
 "Across the two packs, <b>1,052 of the 2,000 example sentences carry a citation</b>, and 813 of those are the author's own unaltered words. Every citation on every card names its book, chapter and section, and Lesson 41 teaches you how to read one.":
   "На два набора <b>1052 из 2000 примеров предложений несут ссылку</b>, и 813 из них — неизменённые слова самого автора. Каждая ссылка на каждой карточке называет книгу, главу и раздел, а урок 41 учит её читать.",

 # ---- the tier and cluster ledger; cluster names are the ones the game ships ----
 "The whole map": "вся карта",
 "Ten tiers, eighty clusters": "Десять уровней, восемьдесят кластеров",
 "Every cluster is 25 cards and ends in a boss fight. Nothing is hidden — the full list is on the <a href=\"wordlists.html?lang=Latin&amp;set=Core\">word lists page</a>, free to read before you buy.":
   "В каждом кластере 25 карточек, и кончается он боем с боссом. Ничего не спрятано — полный список лежит на <a href=\"wordlists.html?lang=Latin&amp;set=Core\">странице списков слов</a>, и его можно бесплатно прочесть до покупки.",
 ">Tier 1<": ">Уровень 1<",
 ">Tier 2<": ">Уровень 2<",
 ">Tier 3<": ">Уровень 3<",
 ">Tier 4<": ">Уровень 4<",
 ">Tier 5<": ">Уровень 5<",
 ">Tier 6<": ">Уровень 6<",
 ">Tier 7<": ">Уровень 7<",
 ">Tier 8<": ">Уровень 8<",
 ">Tier 9<": ">Уровень 9<",
 ">Tier 10<": ">Уровень 10<",
 "The Pointing Words · The Joints · The Links · The Prime Movers · Senate &amp; Sword · Many &amp; Mighty · The Lay of Things · The Marshalling":
   "Указательные слова · Соединительные слова · Связующие элементы · Движущие силы · Сенат и меч · Множество и мощь · Порядок вещей · Упорядочение",
 "The Daily Round · Arms &amp; the Man · The Forum · Flesh &amp; Breath · Tally &amp; Measure · Worth &amp; Honor · Time &amp; Tide · The Rally":
   "Ежедневный круг · Оружие и воин · Форум · Тело и дух · Счёт и мера · Достоинство и честь · Время и течение времени · Сбор",
 "To &amp; Fro · The Long Road · Flesh &amp; Frame · The Fathers · House &amp; Hearth · Hopes &amp; Fears · The Turning Year · The Waystation":
   "Туда и сюда · Долгий путь · Тело и основа · Отцы · Дом и очаг · Надежды и страхи · Год перемен · Остановка в пути",
 "Moods &amp; Moments · The Turning Hand · The Living Frame · The Curia · By Land &amp; Sea · More &amp; Most · The Winter Camp · The Muster Roll":
   "Настроения и мгновения · Поворот руки · Живая основа · Курия · По суше и морю · Больше и наибольшее · Зимний лагерь · Список призыва",
 "What Was Done · The Perfect Stems · The Pitched Battle · The Work in Hand · Life &amp; Limb · Praise &amp; Blame · The Appointed Hour · The Full Account":
   "Совершённое · Перфектные основы · Генеральное сражение · Текущее дело · Жизнь и конечности · Хвала и порицание · Назначенный час · Полный отчёт",
 "The Life of the Mind · Hours &amp; Days · A Soldier&#x27;s Life · The Full Tally · The Family Estate · The Mortal Frame · Treaties &amp; Powers · The Loose Ends":
   "Жизнь разума · Часы и дни · Солдатская жизнь · Полный учёт · Родовое поместье · Бренная плоть · Договоры и полномочия · Незаконченные дела",
 "Comings &amp; Partings · The Ready Hand · The Head Count · Wounds &amp; Toil · Kin &amp; Neighbor · Rank &amp; Office · The Sea Road · The Middle Way":
   "Приход и уход · Умелая рука · Перепись · Раны и тяготы · Родня и соседи · Чин и должность · Морская дорога · Срединный путь",
 "True &amp; False · The Bidding · Sound &amp; Sick · Weight &amp; Worth · The Present Hour · The Tide of Battle · The Household Store · The Last Ditch":
   "Истинное и ложное · Приказ · Здоровый и больной · Вес и достоинство · Настоящий час · Перелом битвы · Домашний склад · Последний рубеж",
 "Hopes &amp; Vows · By the Numbers · Right &amp; Wrong · The Broken Line · Dust &amp; Ashes · The Sacred Rites · Fraud &amp; Force · What Remains":
   "Надежды и обеты · По порядку · Правильное и неправильное · Прерванная линия · Прах и пепел · Священные обряды · Обман и сила · Остатки",
 "The Open Book · The Final Battle · Blood &amp; Bone · Honor &amp; Shame · Envoys &amp; Treaties · Hearth &amp; Heir · The Last Measure · The Closing Page":
   "Открытая книга · Последняя битва · Кровь и кости · Честь и стыд · Посланники и договоры · Очаг и наследник · Последняя мера · Последняя страница",
 ">8 clusters · 200 cards<": ">8 кластеров · 200 карточек<",
 "<span>Core: 5 tiers · 40 clusters · <b>1,000 cards</b></span><span>26 reference lessons</span><span>the reading foundation</span>":
   "<span>Core: 5 уровней · 40 кластеров · <b>1000 карточек</b></span><span>26 справочных уроков</span><span>основа чтения</span>",
 "<span>Pareto: 5 tiers · 40 clusters · <b>1,000 cards</b></span><span>18 reference lessons</span><span>the trunk complete</span>":
   "<span>Pareto: 5 уровней · 40 кластеров · <b>1000 карточек</b></span><span>18 справочных уроков</span><span>ствол целиком</span>",

 # ---- the card: the macron ----
 "Read it by sight": "видно с первого взгляда",
 "The macron is data, not decoration": "Макрон — это данные, а не украшение",
 "Every headword is printed as a dictionary prints it — long vowels marked, gender and genitive stem for a noun, conjugation for a verb. 1,320 of the 2,000 headwords carry a macron. Tap a card to flip it.":
   "Каждое заглавное слово напечатано так, как его печатает словарь: долгие гласные отмечены, у существительного — род и основа родительного падежа, у глагола — спряжение. Макрон стоит на 1320 из 2000 заглавных слов. Нажмите на карточку, чтобы перевернуть её.",
 # the dictionary shorthand is Latin lexicography, not English: it stands
 ">f., -is<": ">f., -is<",
 '''courage, manliness; virtue — &ldquo;Roman courage is great.&rdquo;<span class="nb">noun | gen sg virtūtis — the stem is virtūt-
long ū: vir-tūs
From vir &lsquo;man&rsquo;: the quality of a man.</span>''':
   '''мужество, мужественность; доблесть — &ldquo;Римское мужество велико.&rdquo;<span class="nb">существительное | род. ед. virtūtis — основа virtūt-
долгое ū: vir-tūs
От vir &lsquo;мужчина&rsquo;: качество мужчины.</span>''',
 '''make, do — &ldquo;We are doing the same thing.&rdquo;<span class="nb">verb | 1st pl facimus = &lsquo;we make, we do&rsquo;
long ō: fa-ci-ō; a and i stay short
idem = &lsquo;the same thing&rsquo; (object role)</span>''':
   '''делать, совершать — &ldquo;Мы делаем то же самое.&rdquo;<span class="nb">глагол | 1-е л. мн. facimus = &lsquo;мы делаем&rsquo;
долгое ō: fa-ci-ō; a и i остаются краткими
idem = &lsquo;то же самое&rsquo; (роль дополнения)</span>''',
 '''evil, misfortune — &ldquo;The state sees the shared misfortune.&rdquo;<span class="nb">noun | acc sg malum = nom sg in form
no macron: ma-lum, both vowels short
mālum, with a long ā, is an apple.</span>''':
   '''зло, беда — &ldquo;Государство видит общую беду.&rdquo;<span class="nb">существительное | вин. ед. malum = по форме им. ед.
макрона нет: ma-lum, оба гласных кратки
mālum, с долгим ā, — это яблоко.</span>''',
 ">tap to flip<": ">нажмите, чтобы перевернуть<",

 # ---- the two minimal pairs ----
 ">Tier 1 · Tier 3<": ">Уровень 1 · Уровень 3<",
 ">Tier 10 · Tier 4<": ">Уровень 10 · Уровень 4<",
 "<b>this one</b> against <b>here</b>. One letter apart in print, and the line over the vowel is the only thing that separates them.":
   "<b>этот</b> против <b>здесь</b>. В печати разница в один знак, и только черта над гласной их и разделяет.",
 "<b>bone</b> against <b>mouth</b>. Same three letters, same neuter third declension, six tiers apart — and the card that teaches the second one says so.":
   "<b>кость</b> против <b>рот</b>. Те же три буквы, то же третье склонение среднего рода, шесть уровней врозь — и карточка, которая учит второму, об этом говорит.",
 "The macrons stop at the headword. Example sentences are printed unmarked, the way every real Latin text you will ever open is printed — so what you practise reading is the thing itself, not a teaching aid. The card tells you the vowel length; the sentence makes you carry it.":
   "Макроны кончаются на заглавном слове. Примеры предложений печатаются без пометок — так, как напечатан любой настоящий латинский текст, который вы когда-либо откроете, — и читать вы упражняетесь на самой вещи, а не на учебном пособии. Карточка называет вам долготу гласного; предложение заставляет нести её в голове.",

 # ---- reference lessons ----
 "Not just a word list": "не просто список слов",
 "Forty-four lessons, fired in sequence": "Сорок четыре урока, срабатывающих по порядку",
 "A reference lesson unlocks at the exact card where you first need it, and stays available afterwards. Core's twenty-six and Pareto's eighteen are all free to read on the <a href=\"lessons.html?lang=Latin\">lessons page</a>.":
   "Справочный урок открывается ровно на той карточке, где он вам впервые нужен, и остаётся доступным потом. Двадцать шесть уроков Core и восемнадцать уроков Pareto можно бесплатно прочесть на <a href=\"lessons.html?lang=Latin\">странице уроков</a>.",

 # whole <li> each, so no English article is stranded in front of a Russian noun
 "<li><span class=\"no\">01</span>Welcome to Latin<span class=\"d\">The four letters an English reader gets wrong — c, g, v, qu — in the restored sounds, and what a macron is for.</span></li>":
   "<li><span class=\"no\">01</span>Добро пожаловать в латынь<span class=\"d\">Четыре буквы, в которых ошибается англоязычный читатель — c, g, v, qu — в восстановленном звучании, и зачем нужен макрон.</span></li>",
 "<li><span class=\"no\">10</span>The accusative<span class=\"d\">The first case that changes what a sentence means, met on the card that first needs it.</span></li>":
   "<li><span class=\"no\">10</span>Винительный падеж<span class=\"d\">Первый падеж, который меняет смысл предложения; встречается на той карточке, которой он впервые нужен.</span></li>",
 "<li><span class=\"no\">14</span>Genitive and dative<span class=\"d\">Of and to, and why the genitive singular is printed on every noun card.</span></li>":
   "<li><span class=\"no\">14</span>Родительный и дательный<span class=\"d\">«Кого» и «кому», и почему родительный падеж единственного числа напечатан на каждой карточке существительного.</span></li>",
 "<li><span class=\"no\">18</span>The ablative<span class=\"d\">The case English has no name for, and the six jobs it does.</span></li>":
   "<li><span class=\"no\">18</span>Аблатив<span class=\"d\">Падеж, для которого у английского нет названия, и шесть работ, которые он выполняет.</span></li>",
 "<li><span class=\"no\">23</span>Principal parts<span class=\"d\">Why a Latin verb is quoted four ways, and how to get from any of them to the rest.</span></li>":
   "<li><span class=\"no\">23</span>Основные формы глагола<span class=\"d\">Почему латинский глагол приводится в четырёх формах и как от любой из них добраться до остальных.</span></li>",
 "<li><span class=\"no\">30</span>The ablative absolute<span class=\"d\">The construction that makes Caesar readable at speed.</span></li>":
   "<li><span class=\"no\">30</span>Ablativus absolutus<span class=\"d\">Конструкция, которая делает Цезаря читаемым на скорости.</span></li>",
 "<li><span class=\"no\">34</span>Reported speech<span class=\"d\">Accusative and infinitive: how a Roman writes &lsquo;he said that&hellip;&rsquo;.</span></li>":
   "<li><span class=\"no\">34</span>Косвенная речь<span class=\"d\">Винительный с инфинитивом: как римлянин пишет &lsquo;он сказал, что&hellip;&rsquo;.</span></li>",
 "<li><span class=\"no\">41</span>Reading the citation<span class=\"d\">What <i>Caes. BG 5.44.5</i> means, and how to go and find the rest of the page.</span></li>":
   "<li><span class=\"no\">41</span>Как читать ссылку<span class=\"d\">Что означает <i>Caes. BG 5.44.5</i> и как пойти и найти остальную страницу.</span></li>",

 "Also inside: i acting as y, ch and ae/oe, the connectives, the prime movers, the present tense, the imperative, the sound system, the full plural, two more conjugations, the imperfect, the third declension, prepositions and case, the perfect and its family, relative clauses, connectives at speed, all three participles and their two jobs, the passive twice over, deponents, the infinitive family, the subjunctive mood, cum-clauses, purpose and result, indirect questions, the gerund, the gerundive — and a closing lesson on where to go next.":
   "Внутри ещё: i в роли согласного, ch и ae/oe, соединительные слова, движущие силы, настоящее время, повелительное наклонение, звуковой строй, полное множественное число, ещё два спряжения, имперфект, третье склонение, предлоги и падеж, перфект и его семья, относительные придаточные, соединительные слова на скорости, все три причастия и две их работы, пассив дважды, отложительные глаголы, семья инфинитивов, сослагательное наклонение, придаточные с cum, цель и следствие, косвенные вопросы, герундий, герундив — и заключительный урок о том, куда идти дальше.",

 # ---- the two packs, and the fork past them ----
 "Two packs to literacy": "Два набора до грамотности",
 "Latin is a trunk, not a staircase of three. Core and Pareto together are the whole 2,000-word reading course, grammar-complete at the end of it.":
   "Латынь — это ствол, а не лестница из трёх ступеней. Core и Pareto вместе — весь курс чтения на 2000 слов, и к его концу грамматика пройдена целиком.",
 ">Tiers 1–5 · 1,000 words · 26 lessons<": ">Уровни 1–5 · 1000 слов · 26 уроков<",
 "The reading foundation. Sentences built to the tier at first, real Caesar by the end. Requires the base game.":
   "Основа чтения. Сначала предложения, построенные под уровень, к концу — настоящий Цезарь. Требуется базовая игра.",
 ">Tiers 6–10 · 1,000 words · 18 lessons<": ">Уровни 6–10 · 1000 слов · 18 уроков<",
 "The second thousand, and the end of the scaffolding: Nepos, Cicero's letters, Sallust, Livy, Cicero's speeches. Requires Core.":
   "Вторая тысяча и конец строительных лесов: Непот, письма Цицерона, Саллюстий, Ливий, речи Цицерона. Требуется Core.",
 ">On Steam<": ">В Steam<",

 "Then choose your third thousand": "Потом выберите свою третью тысячу",
 "Basic literacy is the fork, not the finish. The trunk stops at 2,000 words on purpose: past that, Latin genuinely divides, and which 1,000 words come next depends on what you want to read. Neither branch is built yet.":
   "Базовая грамотность — это развилка, а не финиш. Ствол останавливается на 2000 слов намеренно: дальше латынь действительно расходится, и то, какие 1000 слов придут следующими, зависит от того, что вы хотите читать. Ни одна ветвь ещё не построена.",
 ">Classical Poetry<": ">Классическая поэзия<",
 ">Vergil · Ovid · Catullus · Horace<": ">Вергилий · Овидий · Катулл · Гораций<",
 "Verse word order, metre, and the vocabulary that only ever shows up in poets. The trunk's prose ladder is the prerequisite, not a substitute.":
   "Стихотворный порядок слов, метрика и та лексика, которая встречается только у поэтов. Прозаическая лестница ствола — это условие входа, а не то, чем её можно заменить.",
 ">planned · not yet built<": ">запланировано · ещё не построено<",
 ">Ecclesiastical Latin<": ">Церковная латынь<",
 ">the Vulgate · the hymns · the liturgy<": ">Вульгата · гимны · литургия<",
 "Church Latin is its own register — different syntax, different vocabulary, and its own pronunciation, which is why it is a branch and not a chapter of the trunk.":
   "Церковная латынь — это собственный регистр: другой синтаксис, другая лексика и своё произношение; поэтому она ветвь, а не глава ствола.",
 "Both branches take Core and Pareto as their entry requirement. Neither has a date; both are inventoried and reserved rather than promised.":
   "Обе ветви требуют на входе Core и Pareto. Ни у одной нет даты; обе учтены и зарезервированы, а не обещаны.",

 # ---- method ----
 "How it sticks": "как это запоминается",
 "Flashcards as an integrated system": "Карточки как единая система",
 "<dt>Fibonacci SRS</dt>": "<dt>Интервалы по Фибоначчи</dt>",
 "Rate each card 0–5. The better you know a word, the longer before it returns — spaced repetition on Fibonacci intervals.":
   "Оценивайте каждую карточку 0–5. Чем лучше вы знаете слово, тем дольше оно не вернётся — интервальное повторение по Фибоначчи.",
 "<dt>Boss fights</dt>": "<dt>Бои с боссами</dt>",
 "Each of the 80 clusters is gated by a duel you can't win without confronting and overcoming your most difficult words.":
   "Каждый из 80 кластеров закрыт поединком, который не выиграть, не встретившись лицом к лицу со своими самыми трудными словами и не одолев их.",
 "<dt>Graduation</dt>": "<dt>Выпуск</dt>",
 "Beat a cluster and its cards leave your daily deck for good. The deck gets smaller as you learn.":
   "Победите кластер — и его карточки навсегда покинут вашу ежедневную колоду. Колода становится меньше по мере учёбы.",
 "<dt>Audio</dt>": "<dt>Озвучка</dt>",
 "A Latin neural voice on every headword and every example sentence — <i>la_LA-flashboss_m</i>, fine-tuned for FlashBoss and released CC0, reading Classical (restored) pronunciation and honouring the macrons as real vowel length. It is synthesis, not a recording of a speaker.":
   "Латинский нейронный голос на каждом заглавном слове и каждом примере предложения — <i>la_LA-flashboss_m</i>, дообученный для FlashBoss и выпущенный под CC0; он читает классическое (восстановленное) произношение и соблюдает макроны как настоящую долготу гласных. Это синтез, а не запись живого диктора.",
 "<dt>Your language</dt>": "<dt>Ваш язык</dt>",
 "All 2,000 cards carry their translation, their example translation <i>and</i> their notes in <b>German, Spanish, Japanese, Russian and Simplified Chinese</b> as well as English — 30,000 fields, with no gaps. All 44 reference lessons carry the same five, and so does the game's interface. Latin is fully playable without a word of English.":
   "Все 2000 карточек несут свой перевод, перевод примера <i>и</i> свои заметки на <b>немецком, испанском, японском, русском и упрощённом китайском</b>, а не только на английском — 30000 полей, без пропусков. Все 44 справочных урока идут на тех же пяти языках, и интерфейс игры тоже. В латынь можно играть полностью, не зная ни слова по-английски.",
 "<dt>Macrons</dt>": "<dt>Макроны</dt>",
 "Long vowels marked on 1,320 of the 2,000 headwords, left off the sentences — dictionary convention where it teaches, print convention where you read.":
   "Долгие гласные отмечены на 1320 из 2000 заглавных слов и не отмечены в предложениях — словарное соглашение там, где оно учит, печатное — там, где вы читаете.",
 "<dt>Real sources</dt>": "<dt>Настоящие источники</dt>",
 "1,052 example sentences cite the book, chapter and section they came from; 813 are unaltered. Everything is drawn from public-domain editions.":
   "1052 примера предложений называют книгу, главу и раздел, откуда они взяты; 813 из них не изменены. Всё взято из изданий в общественном достоянии.",
 "Forty-four reference lessons across the two packs fire at the point in the sequence where they unlock what you are about to read.":
   "Сорок четыре справочных урока на два набора срабатывают ровно в той точке последовательности, где открывают то, что вы вот-вот прочтёте.",

 # ---- FAQ ----
 ">Questions<": ">Вопросы<",
 "The things people ask before they buy.": "То, о чём спрашивают перед покупкой.",

 ">Where do I buy it?<": ">Где это купить?<",
 """Both packs are on Steam now: <a href="https://store.steampowered.com/app/5063240/?utm_source=website-latin-faq" target="_blank" rel="noopener">Latin Core</a> and <a href="https://store.steampowered.com/app/5063250/?utm_source=website-latin-faq" target="_blank" rel="noopener">Latin Pareto</a>. Both word lists and all forty-four lessons are readable here, free, if you want to judge the course before you buy either one.""":
   """Оба набора уже в Steam: <a href="https://store.steampowered.com/app/5063240/?utm_source=website-latin-faq" target="_blank" rel="noopener">Latin Core</a> и <a href="https://store.steampowered.com/app/5063250/?utm_source=website-latin-faq" target="_blank" rel="noopener">Latin Pareto</a>. Оба списка слов и все сорок четыре урока читаются здесь бесплатно, если вы хотите оценить курс до того, как купите хоть один из них.""",

 ">Which pronunciation is this?<": ">Какое это произношение?<",
 "Classical — the restored pronunciation of Caesar's Rome, in the lessons and in the voice alike: c and g always hard, v as English w, <i>Caesar</i> said as the German <i>Kaiser</i>. An ecclesiastical voice is planned separately, and Church Latin proper is a branch of its own rather than an option inside this course.":
   "Классическое — восстановленное произношение Рима времён Цезаря, и в уроках, и в голосе: c и g всегда твёрдые, v как английское w, <i>Caesar</i> звучит как немецкое <i>Kaiser</i>. Церковный голос запланирован отдельно, а собственно церковная латынь — это отдельная ветвь, а не опция внутри этого курса.",

 ">Do I need anything else to play it?<": ">Нужно ли что-то ещё, чтобы играть?<",
 """Yes. Latin Core is a DLC for the FlashBoss base game, so you need the base game as well. Latin Pareto requires Core — the packs build on each other in order. Everything else — the lessons, the audio, the boss fights — is inside the pack. On Windows 10 you also need <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a> — a free, secure download from the Microsoft Store.""":
   """Да. Latin Core — это DLC к базовой игре FlashBoss, поэтому нужна и она. Latin Pareto требует Core: наборы надстраиваются друг над другом по порядку. Всё остальное — уроки, озвучка, бои с боссами — уже внутри набора. На Windows 10 также нужен <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a> — бесплатная и безопасная загрузка из Microsoft Store.""",

 ">Is the Latin real, or written for the course?<": ">Латынь настоящая или написана для курса?<",
 "Both, in a stated order. Tiers 1 to 3 are constructed to the grammar you have been taught — no real author writes at that ceiling, and the cards claim none. Caesar enters at Tier 4, lightly trimmed. From Tier 8 on, almost every sentence is an author's own unaltered words. Across the two packs 1,052 of 2,000 sentences carry a citation and 813 of those are unadapted.":
   "И то и другое, в заявленном порядке. Уровни с 1 по 3 построены под ту грамматику, которой вас уже научили: ни один настоящий автор не пишет на таком потолке, и карточки никого не называют. Цезарь входит на уровне 4, слегка урезанный. С уровня 8 почти каждое предложение — неизменённые слова автора. На два набора 1052 из 2000 предложений несут ссылку, и 813 из них — без адаптации.",

 ">Can I play it in my own language?<": ">Можно ли играть на своём языке?<",
 "Fully. Every one of the 2,000 cards carries its translation, its example translation and its study notes in <b>German, Spanish, Japanese, Russian and Simplified Chinese</b> as well as English, with no gaps anywhere. All forty-four reference lessons carry the same five, and the game's own interface speaks all six.":
   "Полностью. Каждая из 2000 карточек несёт свой перевод, перевод примера и учебные заметки на <b>немецком, испанском, японском, русском и упрощённом китайском</b>, а не только на английском, и нигде нет пропусков. Все сорок четыре справочных урока идут на тех же пяти языках, а интерфейс самой игры говорит на всех шести.",

 ">What does the course get me to?<": ">К чему приводит курс?<",
 "Reading unadapted classical prose with a dictionary beside you. Two thousand of the highest-frequency lemmas, the whole grammar of the indicative and subjunctive, participles, the infinitive constructions, the gerund and gerundive — and 17,007 words of Latin read in context on the way there. Not speaking Latin, and not writing it: the course is honest that it teaches one skill.":
   "К чтению неадаптированной классической прозы со словарём под рукой. Две тысячи самых частотных лемм, вся грамматика изъявительного и сослагательного наклонений, причастия, инфинитивные обороты, герундий и герундив — и 17007 слов латыни, прочитанных в контексте по дороге. Не к тому, чтобы говорить на латыни, и не к тому, чтобы на ней писать: курс честно говорит, что учит одному навыку.",

 ">Why is there no Pareto 2?<": ">Почему нет Pareto 2?<",
 "Because Latin forks instead. Core plus Pareto is a complete 2,000-word trunk, grammar-complete at Tier 10. The third thousand depends on where you are going — classical poetry or ecclesiastical Latin — so it is planned as two branches rather than one more staircase. Neither is built yet.":
   "Потому что латынь вместо этого расходится. Core плюс Pareto — это полный ствол на 2000 слов, грамматически завершённый на уровне 10. Третья тысяча зависит от того, куда вы идёте — классическая поэзия или церковная латынь, — поэтому она запланирована как две ветви, а не как ещё одна лестница. Ни одна пока не построена.",

 ">Can I see the words before I buy?<": ">Можно ли посмотреть слова до покупки?<",
 """All of them. The complete word lists for Core and Pareto are on the <a href="wordlists.html?lang=Latin&amp;set=Core">word lists page</a>, and all forty-four reference lessons are on the <a href="lessons.html?lang=Latin">lessons page</a> — free, printable, no account.""":
   """Все до одного. Полные списки слов для Core и Pareto лежат на <a href="wordlists.html?lang=Latin&amp;set=Core">странице списков слов</a>, а все сорок четыре справочных урока — на <a href="lessons.html?lang=Latin">странице уроков</a>: бесплатно, можно распечатать, без учётной записи.""",

 ">Is there a demo?<": ">Есть ли демоверсия?<",
 """There's a playable boss fight in the browser, if you want to know what the fight feels like before you commit: <a href="https://flashboss-demo.pages.dev/">try the demo</a>.""":
   """В браузере доступен играбельный бой с боссом — если хотите почувствовать бой до того, как решитесь: <a href="https://flashboss-demo.pages.dev/">попробовать демо</a>.""",

 # ---- closing call to action ----
 "Start with <i>Roma est.</i>": "Начните с <i>Roma est.</i>",
 "Two words on the first card of the first cluster. Two thousand words later, Cicero.":
   "Два слова на первой карточке первого кластера. Две тысячи слов спустя — Цицерон.",
 "— both on Steam": "— оба в Steam",
 """Or read the <a href="wordlists.html?lang=Latin&amp;set=Core">word list</a> and the <a href="lessons.html?lang=Latin">lessons</a> first — they're free, and they're the whole course.""":
   """Или сначала прочтите <a href="wordlists.html?lang=Latin&amp;set=Core">список слов</a> и <a href="lessons.html?lang=Latin">уроки</a> — они бесплатны, и это весь курс.""",
 # the bundle name is the ratified Russian one from the Latin paste sheet
 """Everything here in one purchase: <a href="https://store.steampowered.com/bundle/87746/?utm_source=website-bundle" target="_blank" rel="noopener"><b>FlashBoss Latin — The Complete Course</b></a>. Already own part of it? Steam charges you only for the rest.""":
   """Всё это одной покупкой: <a href="https://store.steampowered.com/bundle/87746/?utm_source=website-bundle" target="_blank" rel="noopener"><b>FlashBoss Латинский — Полный курс</b></a>. Уже владеете частью? Steam возьмёт плату только за остальное.""",

 # ---- footer epigraph: the Latin stands, the gloss and the cite become Russian ----
 "<span class=\"tr\">Chance counts for much in everything, and most of all in warfare.</span>":
   "<span class=\"tr\">Случай многое значит во всех делах, а больше всего — на войне.</span>",
 "Latin Core · Tier 4 · Caes. BG 6.30.2": "Latin Core · Уровень 4 · Caes. BG 6.30.2",
}

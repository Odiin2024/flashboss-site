# Russian strings for swahili.html.
# Keys are the key set of scripts/l10n/swahili_de.py, in the same order — that
# module is the spec for this page.
#
# The store-facing sentences follow the ratified Russian bundle copy
# (flashboss-admin/BUNDLE_COPY_SWAHILI_2026-09-08.md) wherever that sheet has
# them — the six-language list ("на английском, немецком, японском, русском,
# упрощённом китайском и испанском"), "уровни" for tiers, "справочные уроки",
# "бой с боссом", "кластер". The site vocabulary follows the live Russian pages
# and the immersion page's glossary: набор (pack, never «пакет»), базовая игра,
# карточка, урок, заглавное слово, кластер, упражнения на повторение, списки
# слов, главная, голоса. "Core уже вышел" is lifted from packs.ru.html.
# Register: direct imperatives, вы where the sentence needs it — immersion.ru.
#
# PAGE CANON, held here:
#   * every Swahili word, form and example SENTENCE is left byte-identical —
#     anaendesha, tulisafiri, walipanda, the three pack sentences, gari's card,
#     the ten noun-class names (m/wa, ji/ma, ku, pa …). Only the gloss after the
#     em dash becomes Russian, because the card carries a Russian gloss too.
#   * pack names stay English: Swahili Core, Swahili Pareto 1, Swahili Pareto 2,
#     Core, Pareto 1, Pareto 2. So does FlashBoss. Neither is declined.
#   * grammar terms are the standard Russian ones: именной класс, согласование,
#     время, подлежащее, дополнение, каузатив, настоящее/прошедшее. A verb slot
#     is «ячейка», so it never collides with the boss track's «позиция».
#   * the page's counts (1000 / 40 / 20 / 14 / five уровней) are the recount of
#     2026-09-19 and are reproduced exactly; the 2026-09-08 bundle sheet's
#     "49 справочных уроков" predates it and does not win.
#   * Russian writes a thousand with no separator (1000) — the value the build
#     would produce from the English page's "1,000", written out here directly.
#   * banned and absent: hours, CEFR codes, prices, discounts, and a date for
#     anything already out.
TITLE = "Суахили — FlashBoss"
DESCRIPTION = ("FlashBoss Суахили: 1000 слов в 40 кластерах и 20 справочных уроков, именной класс "
               "назван на каждом существительном, нейронный голос кисуахили и бой с боссом у каждых "
               "ворот. Переводы и учебные заметки на шести языках. Swahili Core уже в Steam.")

STRINGS = {
 # ---- nav / chrome / footer ----
 ">packs<": ">наборы<",
 ">word list<": ">список слов<",
 ">lessons<": ">уроки<",
 ">voices<": ">голоса<",
 ">home<": ">главная<",

 # ---- hero ----
 "The newest course · <b>1,000 words out now</b>":
   "Новейший курс · <b>1000 слов уже вышли</b>",
 "The most regular language you will ever learn the hard way.":
   "Самый регулярный язык из всех, что вы когда-либо выучите трудным путём.",
 "Listen · read · repeat · rate · fight":
   "слушать · читать · повторять · оценивать · сражаться",
 "Swahili does not conjugate so much as <b>assemble</b>. A verb is built from slots in a fixed order, and every noun belongs to a class that the rest of the sentence agrees with. Learn those two machines and the vocabulary stops being a list. <b>1,000 words, 40 clusters, 20 reference lessons</b> — with the class named on every noun.":
   "Суахили не столько спрягает, сколько <b>собирает</b>. Глагол строится из ячеек в неизменном порядке, а каждое существительное принадлежит к классу, с которым согласуется всё остальное в предложении. Выучите эти две машины — и лексика перестанет быть списком. <b>1000 слов, 40 кластеров, 20 справочных уроков</b> — и класс назван на каждом существительном.",

 # ---- the argument ----
 "Why Swahili is learnable": "Почему суахили поддаётся изучению",
 "A language with no irregular verbs to speak of":
   "Язык, в котором неправильных глаголов почти нет",
 "Swahili is the working language of East Africa — Tanzania, Kenya, Uganda, Rwanda, Burundi and the eastern Congo — and it is spoken by far more people who learned it than by people born to it. That has worn it smooth. Spelling is exactly as it sounds, stress is always the second-to-last syllable, and there is no tone and no grammatical gender.":
   "Суахили — рабочий язык Восточной Африки: Танзания, Кения, Уганда, Руанда, Бурунди и восток Конго — и на нём говорит куда больше людей, которые его выучили, чем тех, кто с ним родился. Это его сгладило. Написание в точности отвечает звучанию, ударение всегда на предпоследнем слоге, и нет ни тонов, ни грамматического рода.",
 "What it has instead is <b>structure you can see</b>. The verb is a train of slots. The noun carries a class, and the class rides through the whole sentence. Neither is hidden, and neither has a list of exceptions waiting for you at intermediate level.":
   "Зато у него есть <b>видимая структура</b>. Глагол — это состав из ячеек. Существительное несёт класс, и класс едет через всё предложение. Ни то ни другое не спрятано, и ни у того ни у другого нет списка исключений, который ждёт вас на середине пути.",
 "This course teaches ordinary Swahili — the language of the market, the school and the news. The frequency backbone it is built from was made for that, not for subtitles.":
   "Этот курс учит обычному суахили — языку рынка, школы и новостей. Частотная основа, из которой он собран, сделана именно для этого, а не для субтитров.",

 # ---- the verb train. The three Swahili sentences are quoted from the pack's
 #      own cards: they stay byte-identical, only the gloss becomes Russian. ----
 "The verb is an assembly": "Глагол — это сборка",
 "Slots, in a fixed order": "Ячейки в неизменном порядке",
 "Three sentences from the pack's own cards, taken apart. The order never changes: who, when, whom, what.":
   "Три предложения с карточек самого набора, разобранные на части. Порядок не меняется никогда: кто, когда, кого, что.",
 '<i class="ls"></i> who — the subject': '<i class="ls"></i> кто — подлежащее',
 '<i class="lt"></i> when — the tense': '<i class="lt"></i> когда — время',
 '<i class="lo"></i> whom — the object': '<i class="lo"></i> кого — дополнение',
 '<i class="lr"></i> what — the root': '<i class="lr"></i> что — корень',

 "Baba yangu <b>anaendesha</b> basi la shule kila asubuhi, na mama anaendesha gari. — My father drives the school bus every morning, and my mother drives the car.":
   "Baba yangu <b>anaendesha</b> basi la shule kila asubuhi, na mama anaendesha gari. — Мой отец каждое утро водит школьный автобус, а мама водит машину.",
 '<span class="m s">a-<i>he / she</i></span>': '<span class="m s">a-<i>он / она</i></span>',
 '<span class="m t">na-<i>present</i></span>': '<span class="m t">na-<i>настоящее</i></span>',
 '<span class="m r">endesha<i>drive, make go</i></span>':
   '<span class="m r">endesha<i>вести, заставлять ехать</i></span>',
 "Three pieces, read left to right: <b>he · now · drives</b>. The root itself is built — <i>endesha</i> is the causative of <i>kwenda</i>, to go, so it means to make something go.":
   "Три части, читаются слева направо: <b>он · сейчас · ведёт</b>. Сам корень тоже собран — <i>endesha</i> это каузатив от <i>kwenda</i>, «идти», то есть «заставить что-то идти».",

 "<b>Tulisafiri</b> kwa treni kutoka jijini hadi kijijini kwetu wakati wa likizo. — We travelled by train from the city to our village during the holiday.":
   "<b>Tulisafiri</b> kwa treni kutoka jijini hadi kijijini kwetu wakati wa likizo. — В каникулы мы ехали на поезде из города в нашу деревню.",
 '<span class="m s">tu-<i>we</i></span>': '<span class="m s">tu-<i>мы</i></span>',
 '<span class="m t">li-<i>past</i></span>': '<span class="m t">li-<i>прошедшее</i></span>',
 '<span class="m r">safiri<i>travel</i></span>': '<span class="m r">safiri<i>ехать, путешествовать</i></span>',
 "Change one letter in the middle slot and you change the tense. <b>tuna</b>safiri is we are travelling; <b>tuta</b>safiri is we will travel. Nothing else in the word moves.":
   "Измените одну букву в средней ячейке — и изменится время. <b>tuna</b>safiri значит «мы едем сейчас», <b>tuta</b>safiri — «мы поедем». Больше в слове ничто не сдвигается.",

 "Watu wengi <b>walipanda</b> basi hilo kubwa mapema asubuhi ya leo. — Many people boarded that big bus early this morning.":
   "Watu wengi <b>walipanda</b> basi hilo kubwa mapema asubuhi ya leo. — Много людей сели в тот большой автобус сегодня рано утром.",
 '<span class="m s">wa-<i>they, class m/wa</i></span>':
   '<span class="m s">wa-<i>они, класс m/wa</i></span>',
 '<span class="m r">panda<i>climb, board, plant</i></span>':
   '<span class="m r">panda<i>взбираться, садиться, сажать</i></span>',
 "The subject slot is not just a pronoun: it agrees with the <b>class</b> of the noun. <i>Watu</i> is class m/wa, so the verb starts wa-. That is the second machine.":
   "Ячейка подлежащего — это не просто местоимение: она согласуется с <b>классом</b> существительного. <i>Watu</i> — класс m/wa, поэтому глагол начинается с wa-. Это вторая машина.",
 "The pack drills this directly. One of Swahili's three revision drills is the verb train, built slot by slot — you assemble the form rather than recall it whole.":
   "Набор тренирует это напрямую. Одно из трёх упражнений на повторение в наборе — глагольный состав, который собирают ячейка за ячейкой: форму вы складываете сами, а не вспоминаете целиком.",

 # ---- noun classes: whole cells, so no English label survives next to a
 #      class name. The class names themselves are Swahili and stay. ----
 "The engine": "Мотор",
 "Every noun carries its class": "Каждое существительное несёт свой класс",
 "Swahili has no gender. It has classes — and the class of the noun decides the shape of its plural, its adjectives, its verb and its possessives. Get the class and the agreement comes free.":
   "В суахили нет рода. В нём есть классы — и класс существительного задаёт форму его множественного числа, его прилагательных, его глагола и его притяжательных. Знаете класс — согласование достаётся даром.",
 '<div class="k">m/wa</div><div class="v">people — <i>mtu / watu</i></div>':
   '<div class="k">m/wa</div><div class="v">люди — <i>mtu / watu</i></div>',
 '<div class="k">m/mi</div><div class="v">trees, living things, body parts</div>':
   '<div class="k">m/mi</div><div class="v">деревья, живое, части тела</div>',
 '<div class="k">ji/ma</div><div class="v">large things, pairs, groups</div>':
   '<div class="k">ji/ma</div><div class="v">крупные вещи, пары, группы</div>',
 '<div class="k">ki/vi</div><div class="v">objects, tools, languages</div>':
   '<div class="k">ki/vi</div><div class="v">предметы, орудия, языки</div>',
 '<div class="k">n/n</div><div class="v">loans, animals, many abstracts</div>':
   '<div class="k">n/n</div><div class="v">заимствования, животные, многие абстракции</div>',
 '<div class="k">u/n</div><div class="v">abstract nouns, mass nouns</div>':
   '<div class="k">u/n</div><div class="v">абстрактные и вещественные имена</div>',
 '<div class="k">u/ma</div><div class="v">long thin things</div>':
   '<div class="k">u/ma</div><div class="v">длинные тонкие предметы</div>',
 '<div class="k">u/u</div><div class="v">a smaller set, no plural shift</div>':
   '<div class="k">u/u</div><div class="v">группа поменьше, множественное не меняет формы</div>',
 '<div class="k">ku</div><div class="v">the infinitive used as a noun</div>':
   '<div class="k">ku</div><div class="v">инфинитив в роли имени</div>',
 '<div class="k">pa</div><div class="v">place</div>':
   '<div class="k">pa</div><div class="v">место</div>',
 "Those are the ten classes this pack actually uses, taken from its cards rather than from a grammar. The class is printed on every single noun in the deck, where another course would leave you to infer it.":
   "Это те десять классов, которые набор действительно использует, взятые с его карточек, а не из грамматики. Класс напечатан на каждом без исключения существительном колоды — там, где другой курс оставил бы вас догадываться.",

 # ---- the card. gari and its Swahili example sentence stay. ----
 "What a card holds": "Что несёт карточка",
 "A real one, from tier 2. The class sits beside the headword; the notes say the thing a dictionary would not.":
   "Настоящая, с уровня 2. Класс стоит рядом с заглавным словом, а заметки говорят то, чего не скажет словарь.",
 '<div class="tr">a car, or any road vehicle</div>':
   '<div class="tr">машина или любое дорожное транспортное средство</div>',
 '<div class="exx">Our car has no fuel, so we have stopped near the bridge.</div>':
   '<div class="exx">В нашей машине кончилось топливо, поэтому мы остановились у моста.</div>',
 "The same card carries its translation, its example translation <b>and</b> its notes in German, Japanese, Russian, Simplified Chinese and Spanish as well as English — full coverage, every card, no gaps.":
   "Та же карточка несёт свой перевод, перевод примера <b>и</b> свои заметки на немецком, японском, русском, упрощённом китайском и испанском, а не только на английском — полное покрытие, каждая карточка, без пропусков.",

 # ---- method: whole <dt>/<dd> pairs, so no English term is left stranded ----
 "How it sticks": "Как это запоминается",
 "Flashcards as an integrated system": "Карточки как единая система",
 "<dt>Cards</dt><dd><b>1,000 words across 40 clusters</b> and five tiers — greetings and family, the town, work and health, government, the news, and the small words that join sentences together. An example sentence on every card.</dd>":
   "<dt>Карточки</dt><dd><b>1000 слов в 40 кластерах</b> и пять уровней — приветствия и семья, город, работа и здоровье, государство, новости и те маленькие слова, что связывают предложения. На каждой карточке пример предложения.</dd>",
 "<dt>Noun class</dt><dd>Named on <b>every noun</b>, on the card itself: <i>ji/ma</i>, <i>ki/vi</i>, <i>m/wa</i>. The engine the whole language runs on, never left implicit.</dd>":
   "<dt>Именной класс</dt><dd>Назван у <b>каждого существительного</b>, прямо на карточке: <i>ji/ma</i>, <i>ki/vi</i>, <i>m/wa</i>. Мотор, на котором работает весь язык, и его никогда не оставляют додумывать.</dd>",
 "<dt>Your language</dt><dd>Translations and study notes in <b>English, German, Japanese, Russian, Simplified Chinese and Spanish</b> — full coverage on every card. Study Swahili through whichever you call home.</dd>":
   "<dt>Ваш язык</dt><dd>Переводы и учебные заметки на <b>английском, немецком, японском, русском, упрощённом китайском и испанском</b> — полное покрытие на каждой карточке. Учите суахили через тот язык, который зовёте своим.</dd>",
 '<dt>Lessons</dt><dd><b>20 reference lessons</b> — the sound system, the noun-class families, the verb slot machine, the Swahili clock, and concord tier by tier. Readable in all six languages, and <a href="lessons.html?lang=Swahili">free to read here</a>.</dd>':
   '<dt>Уроки</dt><dd><b>20 справочных уроков</b> — звуковой строй, семьи именных классов, устройство глагольных ячеек, часы суахили и согласование уровень за уровнем. Читаются на всех шести языках, и <a href="lessons.html?lang=Swahili">здесь их можно прочесть бесплатно</a>.</dd>',
 "<dt>Drills</dt><dd>Three, shaped to Swahili rather than borrowed: the <b>verb train</b> built slot by slot, <b>plurals by noun class</b>, and <b>dictation</b>.</dd>":
   "<dt>Упражнения</dt><dd>Три, скроенные под суахили, а не одолженные: <b>глагольный состав</b>, который собирают ячейка за ячейкой, <b>множественное число по именным классам</b> и <b>диктант</b>.</dd>",
 "<dt>Audio</dt><dd>Text-to-speech on every word and every example sentence, in a neural standard Kiswahili voice. Synthesis, not a recording of a speaker.</dd>":
   "<dt>Озвучка</dt><dd>Синтез речи на каждом слове и каждом примере, нейронным голосом стандартного кисуахили. Это синтез, а не запись живого диктора.</dd>",
 "<dt>Fibonacci SRS</dt><dd>Rate each card 0–5. The better you know a word, the longer before it returns.</dd>":
   "<dt>Повторение по Фибоначчи</dt><dd>Оценивайте каждую карточку 0–5. Чем лучше вы знаете слово, тем дольше оно не вернётся.</dd>",
 "<dt>Boss fights</dt><dd>No cluster is cleared until its hardest words are answered. Beat it and its cards leave your daily deck for good.</dd>":
   "<dt>Бои с боссами</dt><dd>Кластер не пройден, пока не отвечены его самые трудные слова. Победите его — и его карточки навсегда покинут вашу ежедневную колоду.</dd>",

 # ---- the three packs. Pack names stay English; no date on the unreleased two. ----
 "Three packs, three thousand words": "Три набора, три тысячи слов",
 "Core is out. The two that follow are written and are not on sale yet; neither carries a date until it is.":
   "Core уже вышел. Два следующих написаны и пока не в продаже; ни один не получит даты, пока не выйдет.",
 '<div class="lvl">Tiers 1–5 · 1,000 words · 20 lessons</div>':
   '<div class="lvl">Уровни 1–5 · 1000 слов · 20 уроков</div>',
 "<p>The foundation: greetings and the family through the town, work and health to government and the news.</p>":
   "<p>Основа: от приветствий и семьи через город, работу и здоровье к государству и новостям.</p>",
 '<span class="here">On Steam</span>': '<span class="here">В Steam</span>',
 '<div class="lvl">Tiers 6–10 · 1,000 words · 14 lessons</div>':
   '<div class="lvl">Уровни 6–10 · 1000 слов · 14 уроков</div>',
 "<p>The working vocabulary: money and the bank, the contract, the ministry, elections, the court, the press, the hospital.</p>":
   "<p>Рабочая лексика: деньги и банк, договор, министерство, выборы, суд, пресса, больница.</p>",
 '<span class="soon">Written, not yet out</span>':
   '<span class="soon">Написан, ещё не вышел</span>',
 '<div class="lvl">Tiers 11–15 · 1,000 words · 14 lessons</div>':
   '<div class="lvl">Уровни 11–15 · 1000 слов · 14 уроков</div>',
 "<p>Where derivation opens up — one root becomes six verbs — and the vocabulary follows it into public life and register.</p>":
   "<p>Здесь раскрывается словообразование — из одного корня выходит шесть глаголов — и лексика идёт за ним в общественную жизнь и в регистры речи.</p>",
 "Each pack is 1,000 words and five tiers, and each takes the one before it as read. The end of Pareto 1 is the hump: not finished, but the language has stopped being a wall.":
   "В каждом наборе 1000 слов и пять уровней, и каждый считает предыдущий пройденным. Конец Pareto 1 — это перевал: не финиш, но язык перестал быть стеной.",

 # ---- FAQ ----
 "Questions": "Вопросы",
 "Before you buy": "Перед покупкой",
 "<summary>Do I need the base game?</summary>": "<summary>Нужна ли базовая игра?</summary>",
 'Yes. Swahili Core is DLC for FlashBoss, so you need the base game as well. Everything else — the lessons, the audio, the drills, the boss fights — is inside the pack. On Windows 10 you also need <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a>, a free download from the Microsoft Store.':
   'Да. Swahili Core — это DLC для FlashBoss, так что базовая игра тоже нужна. Всё остальное — уроки, озвучка, упражнения, бои с боссами — уже внутри набора. На Windows 10 понадобится ещё <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a>, бесплатная загрузка из Microsoft Store.',
 "<summary>Can I study it in my own language?</summary>":
   "<summary>Можно ли учить его на своём языке?</summary>",
 "Fully. Every card carries its translation, its example translation and its study notes in <b>German, Japanese, Russian, Simplified Chinese and Spanish</b> as well as English, with no gaps, and all 20 reference lessons carry the same six. The game's own interface speaks them too.":
   "Полностью. Каждая карточка несёт свой перевод, перевод примера и учебные заметки на <b>немецком, японском, русском, упрощённом китайском и испанском</b>, а не только на английском, без пропусков, и все 20 справочных уроков идут на тех же шести языках. Интерфейс самой игры тоже говорит на них.",
 "<summary>Which Swahili is this?</summary>": "<summary>Какой это суахили?</summary>",
 "Standard Kiswahili — the one taught in schools and used by the press across East Africa, based on the Zanzibar dialect. The voice is a neural standard Kiswahili voice.":
   "Стандартный кисуахили — тот, которому учат в школах и которым пользуется пресса по всей Восточной Африке, на основе занзибарского диалекта. Голос — нейронный голос стандартного кисуахили.",
 "<summary>Can I see the words before I buy?</summary>":
   "<summary>Можно ли посмотреть слова до покупки?</summary>",
 'All of them. The complete <a href="wordlists.html?lang=Swahili&amp;set=Core">word list</a> and all twenty <a href="lessons.html?lang=Swahili">reference lessons</a> are on this site — free, printable, no account. There is also a <a href="https://flashboss-demo.pages.dev/">playable boss fight</a>.':
   'Все до одного. Полный <a href="wordlists.html?lang=Swahili&amp;set=Core">список слов</a> и все двадцать <a href="lessons.html?lang=Swahili">справочных уроков</a> лежат на этом сайте — бесплатно, можно распечатать, без учётной записи. Есть и <a href="https://flashboss-demo.pages.dev/">играбельный бой с боссом</a>.',
 "<summary>Is there a British or American spelling layer?</summary>":
   "<summary>Есть ли слой британского и американского написания?</summary>",
 "That layer covers the English packs. Swahili's English is the translation side of the card, and the pack ships one edition of it.":
   "Этот слой относится к английским наборам. Английский здесь — переводная сторона карточки, и набор поставляет одну её редакцию.",

 # ---- final ----
 "Start with <i>Habari?</i>": "Начните с <i>Habari?</i>",
 "Two machines and a thousand words. The rest of Swahili agrees with them.":
   "Две машины и тысяча слов. Весь остальной суахили с ними согласуется.",
 "Swahili Core on Steam &rarr;": "Swahili Core в Steam &rarr;",
}

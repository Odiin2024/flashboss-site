# Russian strings for the-guide.html.
#
# Sources, in the order they win:
#   1. IP CARE, from the English page's own head comment. The trademarked game
#      name appears NOWHERE on this page and appears nowhere here either, in any
#      language or spelling — no Cyrillic rendering of it, no gloss, nothing.
#      The licence framing is the store page's and must not drift: "5E", "SRD"
#      and "System Reference Document 5.2" stay in their English/technical form
#      and only the words around them are Russian ("Совместимо с 5E, собрано по
#      System Reference Document 5.2"). The footer's no-affiliation line is
#      translated in full, all three prongs kept: not affiliated / not endorsed
#      / not sponsored.
#   2. The ratified Russian bundle copy
#      (flashboss-admin/BUNDLE_COPY_THE_GUIDE_COMPLETE_2026-09-17.md) wherever
#      it has the sentence. The hero lede's five clauses are its wording word
#      for word: "что делает состояние, какой кубик требует проверка, что
#      означает Сл 15, о чём говорит блок характеристик". Its terms are taken
#      over wholesale: мастер, состояние, Сл, показатель опасности, кластер,
#      справочный урок, бой с боссом, ступень for tier.
#   3. The shipped deck itself, knight/flashcard_sets/The_Guide/core, for rules
#      jargon a Russian table actually says: состояние, спасбросок, статблок,
#      вид, черта, ячейка заклинаний, концентрация, типы урона, бонус
#      мастерства, отряд, столкновение, опыт. The sample card (Dim Light,
#      cluster1_10) is quoted from its OWN Russian twin — Translation_ru,
#      ExampleSentence_ru, ExampleTranslation_ru, Notes_ru — so the page shows
#      the card as the Russian edition really ships it.
#
# THE HEADWORD ON THE SAMPLE CARD STAYS ENGLISH, deliberately. German swapped in
# the German headword because German is the full edition; Russian is the mixed
# one, and this very page says so two sections later: "the headword you answer
# with, and the word you hear, are English". The deck agrees — TargetWord_ru
# ("Тусклый свет") is what the on-card toggle reveals, not what the card asks
# you to produce. So the card face here reads exactly as a Russian player sees
# it: English term, Russian scene, definition, rule line and notes.
#
# NUMBERS: the English page's figures, untouched. "SRD p. 11" is page eleven and
# stays eleven — and no departure is needed, because Notes_ru on this very card
# cites "SRD p. 11" too. No NUMBERS_CHANGED here; nothing was recounted. The
# build writes Russian thousands with no separator, so the values below keep the
# English page's comma (1,205) and the build strips it to 1205.
#
# Pack name stays English: The Guide. FlashBoss stays Latin script and is never
# declined. Banned and absent: hours, CEFR codes, prices, dates.
#
# TIER is ступень here, not уровень. immersion_ru.py calls T1–T5 "уровни", but
# this page also talks about character level ("what a party can actually do at
# level 5", "5 уровень"), and the two would collide on the same screen. The
# ratified Russian sheet for this product already says "на восьми ступенях", so
# ступень for the tier and уровень for the character level.
#
# Register: вы, direct imperatives, the register the other Russian pages use.
TITLE = "The Guide — FlashBoss"
DESCRIPTION = ("FlashBoss The Guide: правила, которые мастер должен держать в голове, в виде "
               "карточек. 1205 карточек в 62 кластерах, 62 справочных урока, бой с боссом у "
               "каждых ворот. Полное немецкое издание; японский, китайский, русский и испанский "
               "играются на вашем языке, а отвечаете вы по-английски. Совместимо с 5E, собрано "
               "по SRD 5.2.")

STRINGS = {
 # ---- nav / chrome ----
 ">packs<": ">наборы<",
 ">card lists<": ">списки карточек<",
 ">lessons<": ">уроки<",
 ">voices<": ">голоса<",
 ">home<": ">главная<",

 # ---- hero ----
 "For the person running the table · <b>out now</b>":
   "Для того, кто водит игру · <b>уже вышло</b>",
 "1,205 cards · 62 clusters": "1,205 карточек · 62 кластера",
 "The rules a game master needs in their head — not on the page they are turning to.":
   "Правила, которые мастер держит в голове, — а не на странице, которую он сейчас листает.",
 "Listen · read · repeat · rate · fight": "Слушайте · читайте · повторяйте · оценивайте · сражайтесь",
 # the five clauses are the ratified Russian store line, word for word
 "Every card is one thing you should know cold rather than stop to look up: what a condition does, which die a check calls for, what a DC of 15 is meant to mean, what a stat block is telling you, what a party can actually do at level 5. <b>5E compatible, built from the System Reference Document 5.2.</b>":
   "Каждая карточка — это одна вещь, которую стоит знать назубок, а не идти смотреть: что делает состояние, какой кубик требует проверка, что означает Сл 15, о чём говорит блок характеристик, что на самом деле может отряд на 5 уровне. <b>Совместимо с 5E, собрано по System Reference Document 5.2.</b>",
 ">what a card holds</a>": ">что на карточке</a>",
 ">languages</a>": ">языки</a>",

 # ---- the argument ----
 ">Why drill the rules at all<": ">Зачем вообще зубрить правила<",
 "<h2>Looking it up is the thing that breaks the table</h2>":
   "<h2>Игру за столом ломает именно поиск по книге</h2>",
 "A game master's real skill is adjudicating at speed. Everyone at the table can feel the difference between a ruling that arrives in two seconds and one that arrives after ninety seconds of page-turning — and the second one costs you the scene, not just the time.":
   "Настоящее умение мастера — решать быстро. Все за столом чувствуют разницу между решением, которое приходит через две секунды, и тем, которое приходит через девяносто секунд листания книги, — и второе стоит вам сцены, а не только времени.",
 "The fix is not a better index. It is <b>knowing the thing</b>: the fifteen conditions, the thirteen damage types, the ability and proficiency tables, challenge rating and the experience it is worth. The numbers you currently flip pages for.":
   "Лечится это не лучшим указателем. Лечится это <b>знанием</b>: пятнадцать состояний, тринадцать типов урона, таблицы характеристик и бонуса мастерства, показатель опасности и опыт, который он стоит. Те самые числа, ради которых вы сейчас листаете книгу.",
 "So this is a vocabulary course whose vocabulary happens to be a rules set. Same machine as every other FlashBoss pack — spaced repetition, a boss fight at the end of every cluster — pointed at the things you are expected to have in your head when someone asks whether they can shove the ogre off the bridge.":
   "Так что это курс лексики, чья лексика оказалась сводом правил. Та же машина, что и в любом другом наборе FlashBoss, — интервальное повторение, бой с боссом в конце каждого кластера, — наведённая на то, что вы должны держать в голове, когда кто-то спрашивает, можно ли столкнуть огра с моста.",

 # ---- the card ----
 "<h2>What a card holds</h2>": "<h2>Что стоит на карточке</h2>",
 "A real card from tier 1, quoted as it ships. The scene is the point: the rule arrives as something you could narrate, not as an index entry.":
   "Настоящая карточка с первой ступени, приведённая так, как она выходит. Сцена — это и есть суть: правило приходит как то, что можно рассказать, а не как статья в указателе.",
 ">the card<": ">карточка<",
 ">what each part is for<": ">зачем нужна каждая часть<",

 # the sample card, quoted from its own Russian twin in cluster1_10 rather than
 # translated here — scene, definition, rule line and notes, SRD page and all,
 # so the page shows what a Russian player really sees. The headword is left in
 # English ON PURPOSE: the Russian edition asks for the English term and offers
 # "Тусклый свет" only behind the on-card toggle. See the head comment.
 '<div class="hw">Dim Light</div>': '<div class="hw">Dim Light</div>',
 "“Past the torch's ring the corridor goes grey rather than black, and the ranger squints into it and is not sure what she saw.”":
   "«За кругом факела коридор становится серым, а не чёрным, и следопыт щурится туда, не понимая, что увидела.»",
 "Dusk and shadow: sight-based Perception suffers, and Darkvision sees the dark as this.":
   "Сумерки и тень: Восприятие через зрение страдает, а тёмное зрение так видит темноту.",
 "Shadow: creates a Lightly Obscured area": "Полутень: создаёт слабо заслонённую местность",
 "term | the border between bright and dark<br>usually the outer band of a light source · SRD p. 11":
   "термин | граница между светом и тьмой<br>обычно внешняя полоса источника света · SRD p. 11",

 # ---- what each part is for: whole <li> each, so no English article survives ----
 "<li><b>The term</b><span>What the table will actually say out loud. This is the answer you are drilled to produce.</span></li>":
   "<li><b>Термин</b><span>То, что за столом действительно произносят вслух. Это и есть ответ, на который вас натаскивают.</span></li>",
 "<li><b>The scene</b><span>That rule happening at a table. You remember a picture, and the picture carries the rule with it.</span></li>":
   "<li><b>Сцена</b><span>Это правило, как оно происходит за столом. Вы запоминаете картинку, а картинка несёт правило с собой.</span></li>",
 "<li><b>The definition</b><span>The meaning you are tested on — short enough to hold, complete enough to rule with.</span></li>":
   "<li><b>Определение</b><span>Значение, на котором вас проверяют, — достаточно короткое, чтобы удержать, и достаточно полное, чтобы по нему решать.</span></li>",
 "<li><b>The rule line</b><span>The rule as you would say it to a player, in one breath.</span></li>":
   "<li><b>Строка правила</b><span>Правило так, как вы сказали бы его игроку, на одном дыхании.</span></li>",
 "<li><b>The numbers</b><span>The category, the figures underneath, and the page of the reference document it comes from.</span></li>":
   "<li><b>Числа</b><span>Категория, цифры под ней и страница справочного документа, откуда правило взято.</span></li>",
 "A key turns that notes line into a map of all 24 card categories, and a second converts every distance and weight on the cards. Both ship inside the game, as do the English and German reference documents.":
   "Одна клавиша превращает эту строку заметок в карту всех 24 категорий карточек, другая пересчитывает каждое расстояние и вес на карточках. Обе есть внутри игры — как и английский и немецкий справочные документы.",

 # ---- the editions ----
 '<span class="tag">Languages</span>': '<span class="tag">Языки</span>',
 "<h2>Which edition you get</h2>": "<h2>Какое издание вам достанется</h2>",
 "This pack is more honest about its languages than most, because they are genuinely not all the same thing. Three kinds:":
   "Этот набор честнее многих в том, что говорит о своих языках, потому что они и правда не одно и то же. Три вида:",
 '<div class="h">German<span class="badge">Complete</span></div>':
   '<div class="h">Немецкий<span class="badge">Полное издание</span></div>',
 "<b>A full German edition.</b> Everything in German — headword, definition, rule line, scene and notes on all 1,205 cards, and all 62 reference lessons. It uses the established German rules vocabulary, <i>Rüstungsklasse</i>, <i>Trefferpunkte</i>, <i>Rettungswurf</i>, rather than invented calques, and it cites the German rules edition page by page, so a card sends you to the right page of the book you actually own.":
   "<b>Полное немецкое издание.</b> Всё по-немецки — заглавное слово, определение, строка правила, сцена и заметки на всех 1,205 карточках и все 62 справочных урока. Оно опирается на устоявшуюся немецкую терминологию правил, <i>Rüstungsklasse</i>, <i>Trefferpunkte</i>, <i>Rettungswurf</i>, а не на выдуманные кальки, и ссылается на немецкое издание правил постранично, так что карточка отправляет вас на нужную страницу той книги, которая у вас есть.",
 '<div class="h">Japanese · Simplified Chinese · Russian · Spanish<span class="badge">Play in yours, answer in English</span></div>':
   '<div class="h">Японский · Упрощённый китайский · Русский · Испанский<span class="badge">Игра на вашем языке, ответ по-английски</span></div>',
 "The question and the scene are in your language; the headword you answer with, and the word you hear, are <b>English</b>. A toggle on the card shows the translation whenever you want it, and the 62 reference lessons are written in your language too.":
   "Вопрос и сцена — на вашем языке; заглавное слово, которым вы отвечаете, и слово, которое вы слышите, — <b>английские</b>. Переключатель на карточке покажет перевод, когда он вам понадобится, и 62 справочных урока тоже написаны на вашем языке.",
 "<b>That is deliberate, not a shortcut.</b> You meet each rule in words you already think in, and you leave holding the term the table will actually use. It is the step you need before you sit down at an English-speaking game.":
   "<b>Так сделано нарочно, а не ради экономии.</b> С каждым правилом вы встречаетесь в словах, которыми и так думаете, а уходите, держа термин, которым за столом действительно пользуются. Это та ступень, которая нужна вам перед тем, как сесть за англоязычную игру.",
 '<div class="h">The all-in-your-language bonus<span class="badge">Beta</span></div>':
   '<div class="h">Бонус целиком на вашем языке<span class="badge">Бета</span></div>',
 "If you would rather have the whole card in Japanese, Simplified Chinese, Russian or Spanish, that edition is there as well. It comes with compromises, stated plainly: <b>the spoken word stays English</b>, there is no audio beyond it, and it carries <b>no revision drills</b>. A bonus, not a course in its own right — you already speak your own language.":
   "Если вам хочется, чтобы вся карточка была на японском, упрощённом китайском, русском или испанском, такое издание тоже есть. Оно идёт с компромиссами, и о них сказано прямо: <b>произносимое слово остаётся английским</b>, другого звука нет, и <b>упражнений на повторение</b> в нём нет. Это бонус, а не самостоятельный курс — своим языком вы и так владеете.",

 # ---- the tiers: whole <li> each ----
 ">The climb<": ">Подъём<",
 "<h2>Five tiers, each ending in something you can do</h2>":
   "<h2>Пять ступеней, и каждая кончается тем, что вы умеете</h2>",
 '<li><span class="w">Adjudicate a check</span><span class="d">The die, the DC, what the number is meant to mean, and the conditions that change it.</span></li>':
   '<li><span class="w">Разрешить проверку</span><span class="d">Кубик, Сл, что эта цифра должна значить, и состояния, которые её меняют.</span></li>',
 '<li><span class="w">Run a fight</span><span class="d">The turn, the actions in it, the damage types, and what a condition does to whoever is carrying it.</span></li>':
   '<li><span class="w">Провести бой</span><span class="d">Ход, действия в нём, типы урона и то, что состояние делает с тем, кто его носит.</span></li>',
 '<li><span class="w">Run a caster and read a stat block</span><span class="d">Slots, concentration, ranges — and a block of numbers you can look at and know what it will do.</span></li>':
   '<li><span class="w">Вести заклинателя и читать статблок</span><span class="d">Ячейки, концентрация, дистанции — и блок цифр, на который вы смотрите и знаете, что он сделает.</span></li>',
 '<li><span class="w">Know what the options bring</span><span class="d">The twelve classes, the nine species, and what the feats actually give a character.</span></li>':
   '<li><span class="w">Знать, что дают варианты</span><span class="d">Двенадцать классов, девять видов и то, что черты на самом деле дают персонажу.</span></li>',
 '<li><span class="w">Build encounters, hazards and treasure</span><span class="d">Challenge rating against experience, what a party survives, and what to hand out afterwards.</span></li>':
   '<li><span class="w">Строить столкновения, опасности и сокровища</span><span class="d">Показатель опасности против опыта, что отряд переживёт и что раздать после.</span></li>',
 "62 reference lessons, 82 pages, one waiting at the head of every cluster — in every language the pack ships.":
   "62 справочных урока, 82 страницы, по одному в начале каждого кластера — на каждом языке, на котором выходит набор.",

 # ---- the method: whole <dt>+<dd> each ----
 ">How it sticks<": ">Почему это остаётся<",
 "<h2>Flashcards as an integrated system</h2>": "<h2>Карточки как единая система</h2>",
 "<dt>Cards</dt><dd><b>1,205 cards in 62 themed clusters</b> across five tiers, every one carrying its term, its scene, its definition, its rule line and its numbers.</dd>":
   "<dt>Карточки</dt><dd><b>1,205 карточек в 62 тематических кластерах</b> на пяти ступенях, и каждая несёт свой термин, свою сцену, своё определение, свою строку правила и свои числа.</dd>",
 "<dt>Boss fights</dt><dd>Three kinds, not one: <b>name the creature, spell or term</b> from its definition; <b>give your ruling</b> on a scene; <b>read the number</b> off a table. No cluster is cleared until its definitions are mastered.</dd>":
   "<dt>Бои с боссами</dt><dd>Три вида, а не один: <b>назвать существо, заклинание или термин</b> по определению; <b>вынести решение</b> по сцене; <b>считать число</b> из таблицы. Кластер не пройден, пока его определения не освоены.</dd>",
 "<dt>Lessons</dt><dd><b>62 reference lessons, 82 pages</b> — one at the head of every cluster, in every language the pack ships.</dd>":
   "<dt>Уроки</dt><dd><b>62 справочных урока, 82 страницы</b> — по одному в начале каждого кластера, на каждом языке, на котором выходит набор.</dd>",
 "<dt>Fibonacci SRS</dt><dd>Rate each card 0–5. The better you know a rule, the longer before it comes back.</dd>":
   "<dt>SRS по Фибоначчи</dt><dd>Оценивайте каждую карточку от 0 до 5. Чем лучше вы знаете правило, тем дольше оно не вернётся.</dd>",
 '<dt>Audio</dt><dd>The Guide reads aloud in its own bundled voice. Samples are on the <a href="voices.html">voices page</a>.</dd>':
   '<dt>Звук</dt><dd>The Guide читает вслух собственным голосом из комплекта. Примеры — на <a href="voices.html">странице голосов</a>.</dd>',
 "<dt>The ruleset</dt><dd>The <b>2024 revision</b> as it now stands — the terms, the numbers and the procedures expected today. If your rules knowledge is a decade old, you relearn what changed by drilling what is, rather than reading a list of differences.</dd>":
   "<dt>Свод правил</dt><dd><b>Редакция 2024 года</b> в том виде, в каком она есть сейчас, — термины, числа и процедуры, которых ждут сегодня. Если вашему знанию правил десять лет, вы переучиваете изменившееся, тренируя то, что действует, а не читая список отличий.</dd>",

 # ---- the FAQ ----
 ">Questions<": ">Вопросы<",
 "<h2>Before you buy</h2>": "<h2>Перед покупкой</h2>",
 "<summary>Which edition of the rules is this?</summary>":
   "<summary>Какая это редакция правил?</summary>",
 "The <b>2024 revision</b>, built from the System Reference Document 5.2. Conditions, spells, species and stat blocks were revised between the 2014 rules and these, so if your table runs the older edition some of these cards will drill you on numbers you do not use. Check which one your table plays before you buy.":
   "<b>Редакция 2024 года</b>, собранная по System Reference Document 5.2. Состояния, заклинания, виды и статблоки между правилами 2014 года и нынешними переработали, так что если за вашим столом играют по старой редакции, часть этих карточек будет гонять вас по числам, которыми вы не пользуетесь. Перед покупкой проверьте, по какой редакции играет ваш стол.",
 "<summary>Do I need the base game?</summary>": "<summary>Нужна ли базовая игра?</summary>",
 'Yes. The Guide is DLC for FlashBoss, so you need the base game as well. On Windows 10 you also need <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a>, a free download from the Microsoft Store.':
   'Да. The Guide — это DLC для FlashBoss, так что базовая игра тоже нужна. На Windows 10 вам ещё понадобится <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a>, бесплатная загрузка из Microsoft Store.',
 "<summary>I am a player, not a game master. Is it for me?</summary>":
   "<summary>Я игрок, а не мастер. Это для меня?</summary>",
 "It is built for the person running the table, and that is where it pays most. A player who wants to stop asking what a condition does, or who is about to run their first game, gets the same cards — the tiers just matter less in that order.":
   "Он сделан для того, кто водит игру, и больше всего окупается именно там. Игрок, который хочет перестать спрашивать, что делает состояние, или который вот-вот проведёт свою первую игру, получает те же карточки — просто ступени в таком порядке значат меньше.",
 "<summary>Is my language a full edition or a mixed one?</summary>":
   "<summary>Мой язык — полное издание или смешанное?</summary>",
 'German is the full edition. <b>Japanese, Simplified Chinese, Russian and Spanish</b> play in your language and answer in English, with a toggle to the translation on the card and the lessons written in your language — and each also carries an all-in-your-language bonus edition in beta, with English audio and no drills. The <a href="#editions">languages section</a> above says exactly what each one gives you.':
   'Полное издание — немецкое. <b>Японский, упрощённый китайский, русский и испанский</b> играются на вашем языке, а отвечаете вы по-английски: на карточке есть переключатель на перевод, а уроки написаны на вашем языке — и у каждого есть ещё бонусное издание целиком на вашем языке, в бете, с английским звуком и без упражнений. <a href="#editions">Раздел о языках</a> выше говорит точно, что даёт каждое.',
 "<summary>Can I see the cards before I buy?</summary>":
   "<summary>Можно посмотреть карточки до покупки?</summary>",
 'The card lists and reference lessons for FlashBoss packs are on this site, free and printable, and there is a <a href="https://flashboss-demo.pages.dev/">playable boss fight</a> if you want to see the mechanic before anything else.':
   'Списки карточек и справочные уроки наборов FlashBoss есть на этом сайте, бесплатно и для печати, а ещё есть <a href="https://flashboss-demo.pages.dev/">играбельный бой с боссом</a>, если вы хотите сначала увидеть саму механику.',

 # ---- the close ----
 "<h2>Know it, don't look it up.</h2>": "<h2>Знать, а не искать.</h2>",
 "1,205 cards, 62 clusters, and a boss fight at every one of them.":
   "1,205 карточек, 62 кластера и бой с боссом у каждого из них.",
 "The Guide on Steam &rarr;": "The Guide в Steam &rarr;",

 # ---- the legal line: translated in full, all three prongs, nothing softened ----
 "5E compatible. Built from the System Reference Document 5.2. FlashBoss is not affiliated with, endorsed by, or sponsored by any rules publisher.":
   "Совместимо с 5E. Собрано по System Reference Document 5.2. FlashBoss не связан ни с одним издателем правил, не одобрен им и не спонсируется им.",
}

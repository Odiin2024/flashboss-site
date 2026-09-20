# Russian strings for in-development.html.
# This page lists what is NOT out yet, so the one rule above all others here is
# that it carries NO DATE of any kind — no month, no quarter, no year, no
# «скоро», no ETA. Where the English hedges without a date, the Russian hedges
# without a date. The only date on the page is the counting date in the closing
# note, and that is when the packs were counted, not when anything ships.
# Vocabulary is the settled Russian glossary plus the live Russian pages:
# «набор» for pack (never «пакет»), «кластер» (the glossary's word; the older
# pack pages still say «блок»), «уровни» for tiers (about.ru.html,
# french.ru.html: «на пяти уровнях»), «списки слов», «голоса», «материалы»,
# «главная». «В разработке» is what packs.ru.html already calls this page.
# Pack and product names stay Latin and undeclined — Swahili Pareto 1/2, Core,
# Pareto, The Guide Part II, Latin Core, Latin Pareto, Greek Roots, Castellano,
# Bahasa Indonesia. Bare language names take their Russian form, the way the
# live Russian pages already write суахили, латынь and Токи пона.
# Numbers are the English page's numbers; the build writes Russian thousands
# with no separator, so the values here keep the English comma and the build
# strips it. Nothing was recounted.
TITLE = "В разработке — FlashBoss"
DESCRIPTION = ("Что FlashBoss строит дальше: Swahili Pareto 1 и 2, русский, индонезийский, "
               "древнегреческий и новогреческий, The Guide Part II и две ветви латыни. "
               "Посчитано по самим наборам, без дат выхода.")

STRINGS = {
 # ---- nav / chrome ----
 ">packs<": ">наборы<",
 ">in development<": ">в разработке<",
 ">out now<": ">уже вышло<",
 ">english path<": ">английский путь<",
 ">voices<": ">голоса<",
 ">home<": ">главная<",
 ">resources<": ">материалы<",
 ">the english path<": ">английский путь<",

 # ---- hero: the h1 is keyed with its tag so the head comment is left alone ----
 ">Not out yet<": ">Ещё не вышло<",
 '<h1 class="reveal">In Development<': '<h1 class="reveal">В разработке<',
 "What is being built, and how far along it is. <b>Nothing on this page has a release date</b>, because none of it has one — a date goes up when a pack is ready, not before. Everything listed here exists as real cards today; the counts were taken from the packs themselves, not from a plan.":
   "Что строится сейчас и насколько далеко продвинулось. <b>Ни у чего на этой странице нет даты выхода</b>, потому что её ни у чего и нет — дата появляется, когда набор готов, и не раньше. Всё перечисленное здесь существует сегодня настоящими карточками; числа взяты из самих наборов, а не из плана.",

 # ---- the legend: whole line each, so the <b> keeps its Russian sentence ----
 "<b>Cards written</b> — the pack is authored and counted. What remains is checking, audio and a store page.":
   "<b>Карточки написаны</b> — набор создан и посчитан. Остаются проверка, озвучка и страница в магазине.",
 "<b>Planned</b> — decided and inventoried, not started. No cards exist yet.":
   "<b>Запланировано</b> — решено и расписано, но не начато. Карточек пока нет.",
 # the two state badges, after the legend lines above have already gone Russian
 ">Cards written<": ">Карточки написаны<",
 ">Planned<": ">Запланировано<",

 # ---- finishing a course already on sale ----
 "<h2>Finishing a course already on sale</h2>":
   "<h2>Завершение курса, который уже в продаже</h2>",
 "These continue packs you can buy today, and take the pack before them as read.":
   "Они продолжают наборы, которые можно купить уже сегодня, и считают предыдущий набор пройденным.",

 "1,000 words · 40 clusters · tiers 6–10":
   "1,000 слов · 40 кластеров · уровни 6–10",
 "The working vocabulary: money and the bank, the company and the contract, the ministry, elections, the court, the police, the press, the hospital. Continues <a href=\"swahili.html\">Swahili Core</a>, which is out now.":
   "Рабочая лексика: деньги и банк, фирма и договор, министерство, выборы, суд, полиция, пресса, больница. Продолжает <a href=\"swahili.html\">Swahili Core</a>, который уже вышел.",

 "1,000 words · 40 clusters · tiers 11–15":
   "1,000 слов · 40 кластеров · уровни 11–15",
 "The last thousand of the 3,000-word course, and where Swahili's derivation opens up — one root becoming six verbs through the passive, the stative, the reciprocal, the reflexive, the causative and the applicative.":
   "Последняя тысяча курса на 3,000 слов и то место, где раскрывается словообразование суахили — один корень становится шестью глаголами через пассив, статив, взаимную, возвратную, каузативную и аппликативную формы.",

 "925 cards · 50 clusters · three tiers · English and German":
   "925 карточек · 50 кластеров · три уровня · английский и немецкий",
 "The other half of a game master's memory. Where <a href=\"the-guide.html\">The Guide</a> holds the rules you adjudicate with, Part II holds what you populate a world with: the spell list, the creature roster and the treasure table. Requires The Guide.":
   "Вторая половина памяти мастера игры. Если <a href=\"the-guide.html\">The Guide</a> держит правила, по которым вы судите, то Part II держит то, чем вы населяете мир: список заклинаний, перечень существ и таблицу сокровищ. Требуется The Guide.",

 # ---- new languages: bare language names go Russian, Core/Pareto stay ----
 "<h2>New languages</h2>": "<h2>Новые языки</h2>",
 "Each is a full course in the usual shape — Core first, then Pareto 1, five tiers apiece.":
   "Каждый из них — полный курс привычной формы: сначала Core, потом Pareto 1, по пять уровней в каждом.",

 "Core and Pareto 1 · 1,000 words each · 40 clusters each":
   "Core и Pareto 1 · по 1,000 слов · по 40 кластеров",

 ">Russian<": ">Русский<",
 # the English paragraph opens with the native name as a flourish; on the
 # Russian page that would just repeat the item's own title, so it goes.
 "Русский. Two thousand words authored and counted.":
   "Две тысячи слов написаны и посчитаны.",

 ">Indonesian<": ">Индонезийский<",
 "Bahasa Indonesia — a language with no tenses, no genders and no plurals to memorise, and a word order you already have.":
   "Bahasa Indonesia — язык без времён, без родов и без форм множественного числа, которые надо заучивать, и с порядком слов, который у вас уже есть.",

 ">Modern Greek<": ">Новогреческий<",
 "Ελληνικά, the living language, with an alphabet ladder in the opening lessons. Not to be confused with Ancient Greek below, or with <a href=\"greek-roots.html\">Greek Roots</a>, which teaches the Greek already inside English.":
   "Ελληνικά, живой язык, с лестницей алфавита в первых уроках. Не путать с древнегреческим ниже и с <a href=\"greek-roots.html\">Greek Roots</a>, который учит тому греческому, что уже сидит внутри английского.",

 ">Ancient Greek<": ">Древнегреческий<",
 "A reading course, in the shape <a href=\"latin.html\">Latin</a> took: the sentences start built for the tier and end as the authors wrote them.":
   "Курс чтения, устроенный так же, как <a href=\"latin.html\">латынь</a>: предложения сначала собраны под уровень, а в конце идут такими, какими их написали авторы.",

 ">Polish and Portuguese<": ">Польский и португальский<",
 "Word lists locked · no cards authored yet":
   "Списки слов закреплены · карточки ещё не написаны",
 "The frequency backbones are chosen and fixed, which is the half of the work that decides what a course teaches. The cards themselves are not written.":
   "Частотная основа выбрана и закреплена, а это та половина работы, которая решает, чему учит курс. Сами карточки не написаны.",

 # ---- beyond the Latin trunk ----
 "<h2>Beyond the Latin trunk</h2>": "<h2>Дальше латинского ствола</h2>",
 "Latin Core and Latin Pareto are the whole 2,000-word reading course, grammar-complete at tier 10. There is deliberately no third staircase.":
   "Latin Core и Latin Pareto — это весь курс чтения на 2,000 слов, грамматически полный к уровню 10. Третьей лестницы намеренно нет.",

 ">Latin — the two branches<": ">Латынь — две ветви<",
 "Classical poetry · or ecclesiastical Latin": "Классическая поэзия · или церковная латынь",
 "Past 2,000 words Latin genuinely divides, and which thousand comes next depends on what you want to read: <b>classical poetry</b> — Vergil, Ovid, Catullus, Horace — or <b>ecclesiastical Latin</b>, the Vulgate, the hymns and the liturgy. Both are inventoried and reserved. Neither is built, and neither takes the other as a prerequisite.":
   "За 2,000 слов латынь действительно расходится, и какая тысяча будет следующей, зависит от того, что вы хотите читать: <b>классическая поэзия</b> — Вергилий, Овидий, Катулл, Гораций — или <b>церковная латынь</b>, Вульгата, гимны и литургия. Обе ветви расписаны и зарезервированы. Ни одна не построена, и ни одна не требует другой.",

 # ---- voices ----
 "<h2>Voices</h2>": "<h2>Голоса</h2>",
 ">Castellano — Spain, male<": ">Castellano — Испания, мужской<",
 "Replaces the included Latin American voice across every Spanish pack":
   "Заменяет прилагаемый латиноамериканский голос в каждом наборе испанского",
 "A voice pack rather than a course: it swaps the voice in cards, lessons and boss fights, and switches back whenever you like. Hear it against the voice it replaces on the <a href=\"voices.html\">voices page</a>.":
   "Голосовой набор, а не курс: он заменяет голос в карточках, уроках и боях с боссами и переключается обратно когда угодно. Послушайте его рядом с голосом, который он заменяет, на <a href=\"voices.html\">странице голосов</a>.",

 # ---- the closing note: the date here is the COUNTING date, not a release ----
 "Everything above was counted from the packs on <b>19 September 2026</b>. A pack leaves this page the day it goes on sale and appears on <a href=\"packs.html\">the pack list</a> instead — so if something has vanished from here, look for it there.":
   "Всё перечисленное выше посчитано по самим наборам <b>19 сентября 2026 года</b>. Набор покидает эту страницу в тот день, когда поступает в продажу, и появляется вместо неё в <a href=\"packs.html\">списке наборов</a> — так что если что-то отсюда пропало, ищите его там.",
 "And yes — the page that lists what's in development used to be, itself, in development.":
   "И да — страница, которая перечисляет то, что в разработке, сама когда-то была в разработке.",
}

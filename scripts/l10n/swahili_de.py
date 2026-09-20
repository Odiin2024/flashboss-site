# German strings for swahili.html.
# The store-facing sentences are LIFTED from the ratified German bundle copy
# (flashboss-admin/BUNDLE_COPY_SWAHILI_2026-09-08.md) wherever that sheet has
# them — the six-language list, "Vereinfachtem Chinesisch", the Stufen wording,
# "Bosskampf", "Text-to-Speech". The method and FAQ wording follows the German
# course pages that already exist (french.de.html, packs.de.html): "So bleibt es
# hängen", "Karteikarten als integriertes System", "Sprachausgabe", "Synthese,
# keine Aufnahme einer sprechenden Person", "Bevor du kaufst". The rest is mine.
#
# PAGE CANON, held here:
#   * every Swahili word, form and example SENTENCE is left byte-identical —
#     anaendesha, tulisafiri, walipanda, the three pack sentences, gari's card,
#     the ten noun-class names (m/wa, ji/ma, ku, pa …). Only the gloss after the
#     em dash becomes German, because the card carries a German gloss too.
#   * pack names stay English: Swahili Core, Swahili Pareto 1, Swahili Pareto 2,
#     Core, Pareto 1, Pareto 2. So does FlashBoss.
#   * grammar terms are the standard German ones: Nominalklasse, Kongruenz,
#     Tempus, Subjekt, Objekt, Kausativ, Präsens.
#   * the page's counts (1.000 / 40 / 20 / 14 / five Stufen) are the recount of
#     2026-09-19 and are reproduced exactly; the 2026-09-08 bundle sheet's
#     "49 Lektionen" predates it and does not win.
#   * banned and absent: hours, CEFR codes, prices, discounts, and a date for
#     anything already out.
TITLE = "Swahili — FlashBoss"
DESCRIPTION = ("FlashBoss Swahili: 1.000 Wörter in 40 Clustern und 20 Referenzlektionen, die "
               "Nominalklasse auf jedem Substantiv benannt, eine neuronale Kiswahili-Stimme und "
               "an jedem Tor ein Bosskampf. Übersetzungen und Lernhinweise in sechs Sprachen. "
               "Swahili Core jetzt auf Steam.")

STRINGS = {
 # ---- nav / chrome / footer ----
 ">packs<": ">Packs<",
 ">word list<": ">Wortliste<",
 ">lessons<": ">Lektionen<",
 ">voices<": ">Stimmen<",
 ">home<": ">Start<",

 # ---- hero ----
 "The newest course · <b>1,000 words out now</b>":
   "Der neueste Kurs · <b>1.000 Wörter jetzt erhältlich</b>",
 "The most regular language you will ever learn the hard way.":
   "Die regelmäßigste Sprache, die du je auf die harte Tour lernen wirst.",
 "Listen · read · repeat · rate · fight":
   "hören · lesen · wiederholen · bewerten · kämpfen",
 "Swahili does not conjugate so much as <b>assemble</b>. A verb is built from slots in a fixed order, and every noun belongs to a class that the rest of the sentence agrees with. Learn those two machines and the vocabulary stops being a list. <b>1,000 words, 40 clusters, 20 reference lessons</b> — with the class named on every noun.":
   "Swahili konjugiert nicht so sehr, als dass es <b>zusammensetzt</b>. Ein Verb wird aus Slots in fester Reihenfolge gebaut, und jedes Substantiv gehört zu einer Klasse, nach der sich der ganze übrige Satz richtet. Lerne diese beiden Maschinen, und der Wortschatz hört auf, eine Liste zu sein. <b>1.000 Wörter, 40 Cluster, 20 Referenzlektionen</b> — mit der Klasse auf jedem Substantiv.",

 # ---- the argument ----
 "Why Swahili is learnable": "Warum Swahili lernbar ist",
 "A language with no irregular verbs to speak of":
   "Eine Sprache praktisch ohne unregelmäßige Verben",
 "Swahili is the working language of East Africa — Tanzania, Kenya, Uganda, Rwanda, Burundi and the eastern Congo — and it is spoken by far more people who learned it than by people born to it. That has worn it smooth. Spelling is exactly as it sounds, stress is always the second-to-last syllable, and there is no tone and no grammatical gender.":
   "Swahili ist die Verkehrssprache Ostafrikas — Tansania, Kenia, Uganda, Ruanda, Burundi und der Osten des Kongo — und es sprechen weit mehr Menschen, die es gelernt haben, als Menschen, die damit aufgewachsen sind. Das hat es glattgeschliffen. Geschrieben wird genau so, wie es klingt, die Betonung liegt immer auf der vorletzten Silbe, und es gibt weder Töne noch ein grammatisches Geschlecht.",
 "What it has instead is <b>structure you can see</b>. The verb is a train of slots. The noun carries a class, and the class rides through the whole sentence. Neither is hidden, and neither has a list of exceptions waiting for you at intermediate level.":
   "Was es stattdessen hat, ist <b>sichtbare Struktur</b>. Das Verb ist ein Zug aus Slots. Das Substantiv trägt eine Klasse, und die Klasse fährt durch den ganzen Satz mit. Versteckt ist davon nichts, und auf der Mittelstufe wartet auf keines von beiden eine Liste von Ausnahmen.",
 "This course teaches ordinary Swahili — the language of the market, the school and the news. The frequency backbone it is built from was made for that, not for subtitles.":
   "Dieser Kurs lehrt gewöhnliches Swahili — die Sprache des Marktes, der Schule und der Nachrichten. Das Häufigkeitsgerüst, aus dem er gebaut ist, wurde dafür gemacht und nicht für Untertitel.",

 # ---- the verb train. The three Swahili sentences are quoted from the pack's
 #      own cards: they stay byte-identical, only the gloss becomes German. ----
 "The verb is an assembly": "Das Verb ist ein Bausatz",
 "Slots, in a fixed order": "Slots, in fester Reihenfolge",
 "Three sentences from the pack's own cards, taken apart. The order never changes: who, when, whom, what.":
   "Drei Sätze von den Karten des Pakets selbst, auseinandergenommen. Die Reihenfolge ändert sich nie: wer, wann, wen, was.",
 '<i class="ls"></i> who — the subject': '<i class="ls"></i> wer — das Subjekt',
 '<i class="lt"></i> when — the tense': '<i class="lt"></i> wann — das Tempus',
 '<i class="lo"></i> whom — the object': '<i class="lo"></i> wen — das Objekt',
 '<i class="lr"></i> what — the root': '<i class="lr"></i> was — die Wurzel',

 "Baba yangu <b>anaendesha</b> basi la shule kila asubuhi, na mama anaendesha gari. — My father drives the school bus every morning, and my mother drives the car.":
   "Baba yangu <b>anaendesha</b> basi la shule kila asubuhi, na mama anaendesha gari. — Mein Vater fährt jeden Morgen den Schulbus, und meine Mutter fährt das Auto.",
 '<span class="m s">a-<i>he / she</i></span>': '<span class="m s">a-<i>er / sie</i></span>',
 '<span class="m t">na-<i>present</i></span>': '<span class="m t">na-<i>Präsens</i></span>',
 '<span class="m r">endesha<i>drive, make go</i></span>':
   '<span class="m r">endesha<i>fahren, in Gang setzen</i></span>',
 "Three pieces, read left to right: <b>he · now · drives</b>. The root itself is built — <i>endesha</i> is the causative of <i>kwenda</i>, to go, so it means to make something go.":
   "Drei Teile, von links nach rechts gelesen: <b>er · jetzt · fährt</b>. Die Wurzel selbst ist zusammengesetzt — <i>endesha</i> ist das Kausativ von <i>kwenda</i>, gehen, und heißt damit: etwas gehen machen.",

 "<b>Tulisafiri</b> kwa treni kutoka jijini hadi kijijini kwetu wakati wa likizo. — We travelled by train from the city to our village during the holiday.":
   "<b>Tulisafiri</b> kwa treni kutoka jijini hadi kijijini kwetu wakati wa likizo. — In den Ferien sind wir mit dem Zug aus der Stadt in unser Dorf gefahren.",
 '<span class="m s">tu-<i>we</i></span>': '<span class="m s">tu-<i>wir</i></span>',
 '<span class="m t">li-<i>past</i></span>': '<span class="m t">li-<i>Vergangenheit</i></span>',
 '<span class="m r">safiri<i>travel</i></span>': '<span class="m r">safiri<i>reisen</i></span>',
 "Change one letter in the middle slot and you change the tense. <b>tuna</b>safiri is we are travelling; <b>tuta</b>safiri is we will travel. Nothing else in the word moves.":
   "Ändere einen Buchstaben im mittleren Slot, und das Tempus ändert sich. <b>tuna</b>safiri heißt wir reisen gerade, <b>tuta</b>safiri heißt wir werden reisen. Sonst bewegt sich nichts im Wort.",

 "Watu wengi <b>walipanda</b> basi hilo kubwa mapema asubuhi ya leo. — Many people boarded that big bus early this morning.":
   "Watu wengi <b>walipanda</b> basi hilo kubwa mapema asubuhi ya leo. — Viele Leute sind heute früh am Morgen in diesen großen Bus eingestiegen.",
 '<span class="m s">wa-<i>they, class m/wa</i></span>':
   '<span class="m s">wa-<i>sie, Klasse m/wa</i></span>',
 '<span class="m r">panda<i>climb, board, plant</i></span>':
   '<span class="m r">panda<i>steigen, einsteigen, pflanzen</i></span>',
 "The subject slot is not just a pronoun: it agrees with the <b>class</b> of the noun. <i>Watu</i> is class m/wa, so the verb starts wa-. That is the second machine.":
   "Der Subjektslot ist nicht bloß ein Pronomen: Er kongruiert mit der <b>Klasse</b> des Substantivs. <i>Watu</i> steht in der Klasse m/wa, also beginnt das Verb mit wa-. Das ist die zweite Maschine.",
 "The pack drills this directly. One of Swahili's three revision drills is the verb train, built slot by slot — you assemble the form rather than recall it whole.":
   "Das Paket übt genau das. Eine der drei Wiederholungsübungen von Swahili ist der Verbzug, Slot für Slot gebaut — du setzt die Form zusammen, statt sie als Ganzes abzurufen.",

 # ---- noun classes: whole cells, so no English label survives next to a
 #      class name. The class names themselves are Swahili and stay. ----
 "The engine": "Der Motor",
 "Every noun carries its class": "Jedes Substantiv trägt seine Klasse",
 "Swahili has no gender. It has classes — and the class of the noun decides the shape of its plural, its adjectives, its verb and its possessives. Get the class and the agreement comes free.":
   "Swahili hat kein Genus. Es hat Klassen — und die Klasse des Substantivs entscheidet über die Form seines Plurals, seiner Adjektive, seines Verbs und seiner Possessiva. Hast du die Klasse, bekommst du die Kongruenz umsonst dazu.",
 '<div class="k">m/wa</div><div class="v">people — <i>mtu / watu</i></div>':
   '<div class="k">m/wa</div><div class="v">Menschen — <i>mtu / watu</i></div>',
 '<div class="k">m/mi</div><div class="v">trees, living things, body parts</div>':
   '<div class="k">m/mi</div><div class="v">Bäume, Lebendiges, Körperteile</div>',
 '<div class="k">ji/ma</div><div class="v">large things, pairs, groups</div>':
   '<div class="k">ji/ma</div><div class="v">große Dinge, Paare, Gruppen</div>',
 '<div class="k">ki/vi</div><div class="v">objects, tools, languages</div>':
   '<div class="k">ki/vi</div><div class="v">Gegenstände, Werkzeuge, Sprachen</div>',
 '<div class="k">n/n</div><div class="v">loans, animals, many abstracts</div>':
   '<div class="k">n/n</div><div class="v">Lehnwörter, Tiere, viele Abstrakta</div>',
 '<div class="k">u/n</div><div class="v">abstract nouns, mass nouns</div>':
   '<div class="k">u/n</div><div class="v">Abstrakta, Stoffnamen</div>',
 '<div class="k">u/ma</div><div class="v">long thin things</div>':
   '<div class="k">u/ma</div><div class="v">lange dünne Dinge</div>',
 '<div class="k">u/u</div><div class="v">a smaller set, no plural shift</div>':
   '<div class="k">u/u</div><div class="v">eine kleinere Gruppe, kein Pluralwechsel</div>',
 '<div class="k">ku</div><div class="v">the infinitive used as a noun</div>':
   '<div class="k">ku</div><div class="v">der Infinitiv als Substantiv</div>',
 '<div class="k">pa</div><div class="v">place</div>':
   '<div class="k">pa</div><div class="v">Ort</div>',
 "Those are the ten classes this pack actually uses, taken from its cards rather than from a grammar. The class is printed on every single noun in the deck, where another course would leave you to infer it.":
   "Das sind die zehn Klassen, die dieses Paket wirklich benutzt, aus seinen Karten genommen und nicht aus einer Grammatik. Die Klasse steht auf jedem einzelnen Substantiv im Deck, wo ein anderer Kurs sie dich erraten ließe.",

 # ---- the card. gari and its Swahili example sentence stay. ----
 "What a card holds": "Was auf einer Karte steht",
 "A real one, from tier 2. The class sits beside the headword; the notes say the thing a dictionary would not.":
   "Eine echte, aus Stufe 2. Die Klasse steht neben dem Stichwort; die Notizen sagen das, was ein Wörterbuch nicht sagt.",
 '<div class="tr">a car, or any road vehicle</div>':
   '<div class="tr">ein Auto oder irgendein Straßenfahrzeug</div>',
 '<div class="exx">Our car has no fuel, so we have stopped near the bridge.</div>':
   '<div class="exx">Unser Auto hat kein Benzin, deshalb haben wir in der Nähe der Brücke angehalten.</div>',
 "The same card carries its translation, its example translation <b>and</b> its notes in German, Japanese, Russian, Simplified Chinese and Spanish as well as English — full coverage, every card, no gaps.":
   "Dieselbe Karte trägt ihre Übersetzung, die Übersetzung des Beispielsatzes <b>und</b> ihre Notizen auf Deutsch, Japanisch, Russisch, Vereinfachtem Chinesisch und Spanisch ebenso wie auf Englisch — vollständige Abdeckung, jede Karte, keine Lücke.",

 # ---- method: whole <dt>/<dd> pairs, so no English term is left stranded ----
 "How it sticks": "So bleibt es hängen",
 "Flashcards as an integrated system": "Karteikarten als integriertes System",
 "<dt>Cards</dt><dd><b>1,000 words across 40 clusters</b> and five tiers — greetings and family, the town, work and health, government, the news, and the small words that join sentences together. An example sentence on every card.</dd>":
   "<dt>Karten</dt><dd><b>1.000 Wörter über 40 Cluster</b> und fünf Stufen — Begrüßungen und Familie, die Stadt, Arbeit und Gesundheit, Behörden, die Nachrichten und die kleinen Wörter, die Sätze zusammenhalten. Auf jeder Karte ein Beispielsatz.</dd>",
 "<dt>Noun class</dt><dd>Named on <b>every noun</b>, on the card itself: <i>ji/ma</i>, <i>ki/vi</i>, <i>m/wa</i>. The engine the whole language runs on, never left implicit.</dd>":
   "<dt>Nominalklasse</dt><dd>Auf <b>jedem Substantiv</b> benannt, auf der Karte selbst: <i>ji/ma</i>, <i>ki/vi</i>, <i>m/wa</i>. Der Motor, mit dem die ganze Sprache läuft, nie stillschweigend vorausgesetzt.</dd>",
 "<dt>Your language</dt><dd>Translations and study notes in <b>English, German, Japanese, Russian, Simplified Chinese and Spanish</b> — full coverage on every card. Study Swahili through whichever you call home.</dd>":
   "<dt>Deine Sprache</dt><dd>Übersetzungen und Lernhinweise auf <b>Englisch, Deutsch, Japanisch, Russisch, Vereinfachtem Chinesisch und Spanisch</b> — vollständige Abdeckung auf jeder Karte. Lerne Swahili über die Sprache, die du deine nennst.</dd>",
 '<dt>Lessons</dt><dd><b>20 reference lessons</b> — the sound system, the noun-class families, the verb slot machine, the Swahili clock, and concord tier by tier. Readable in all six languages, and <a href="lessons.html?lang=Swahili">free to read here</a>.</dd>':
   '<dt>Lektionen</dt><dd><b>20 Referenzlektionen</b> — das Lautsystem, die Familien der Nominalklassen, das Slotwerk des Verbs, die Swahili-Uhr und die Kongruenz Stufe für Stufe. In allen sechs Sprachen lesbar und <a href="lessons.html?lang=Swahili">hier kostenlos zu lesen</a>.</dd>',
 "<dt>Drills</dt><dd>Three, shaped to Swahili rather than borrowed: the <b>verb train</b> built slot by slot, <b>plurals by noun class</b>, and <b>dictation</b>.</dd>":
   "<dt>Übungen</dt><dd>Drei, auf Swahili zugeschnitten statt anderswo geborgt: der <b>Verbzug</b>, Slot für Slot gebaut, <b>Plurale nach Nominalklasse</b> und <b>Diktat</b>.</dd>",
 "<dt>Audio</dt><dd>Text-to-speech on every word and every example sentence, in a neural standard Kiswahili voice. Synthesis, not a recording of a speaker.</dd>":
   "<dt>Sprachausgabe</dt><dd>Text-to-Speech auf jedem Wort und jedem Beispielsatz, in einer neuronalen Stimme für Standard-Kiswahili. Es ist Synthese, keine Aufnahme einer sprechenden Person.</dd>",
 "<dt>Fibonacci SRS</dt><dd>Rate each card 0–5. The better you know a word, the longer before it returns.</dd>":
   "<dt>Fibonacci-SRS</dt><dd>Bewerte jede Karte mit 0–5. Je besser du ein Wort kennst, desto länger dauert es, bis es wiederkommt.</dd>",
 "<dt>Boss fights</dt><dd>No cluster is cleared until its hardest words are answered. Beat it and its cards leave your daily deck for good.</dd>":
   "<dt>Bosskämpfe</dt><dd>Kein Cluster ist geschafft, bevor seine schwersten Wörter beantwortet sind. Besiege es, und seine Karten verlassen dein tägliches Deck für immer.</dd>",

 # ---- the three packs. Pack names stay English; no date on the unreleased two. ----
 "Three packs, three thousand words": "Drei Pakete, dreitausend Wörter",
 "Core is out. The two that follow are written and are not on sale yet; neither carries a date until it is.":
   "Core ist da. Die beiden folgenden sind geschrieben und noch nicht im Verkauf; keines trägt ein Datum, ehe es so weit ist.",
 '<div class="lvl">Tiers 1–5 · 1,000 words · 20 lessons</div>':
   '<div class="lvl">Stufen 1–5 · 1.000 Wörter · 20 Lektionen</div>',
 "<p>The foundation: greetings and the family through the town, work and health to government and the news.</p>":
   "<p>Das Fundament: von Begrüßungen und Familie über die Stadt, Arbeit und Gesundheit bis zu Behörden und Nachrichten.</p>",
 '<span class="here">On Steam</span>': '<span class="here">Auf Steam</span>',
 '<div class="lvl">Tiers 6–10 · 1,000 words · 14 lessons</div>':
   '<div class="lvl">Stufen 6–10 · 1.000 Wörter · 14 Lektionen</div>',
 "<p>The working vocabulary: money and the bank, the contract, the ministry, elections, the court, the press, the hospital.</p>":
   "<p>Der Arbeitswortschatz: Geld und Bank, der Vertrag, das Ministerium, Wahlen, das Gericht, die Presse, das Krankenhaus.</p>",
 '<span class="soon">Written, not yet out</span>':
   '<span class="soon">Geschrieben, noch nicht erschienen</span>',
 '<div class="lvl">Tiers 11–15 · 1,000 words · 14 lessons</div>':
   '<div class="lvl">Stufen 11–15 · 1.000 Wörter · 14 Lektionen</div>',
 "<p>Where derivation opens up — one root becomes six verbs — and the vocabulary follows it into public life and register.</p>":
   "<p>Wo die Ableitung sich öffnet — aus einer Wurzel werden sechs Verben — und der Wortschatz ihr ins öffentliche Leben und in die Stilebenen folgt.</p>",
 "Each pack is 1,000 words and five tiers, and each takes the one before it as read. The end of Pareto 1 is the hump: not finished, but the language has stopped being a wall.":
   "Jedes Paket umfasst 1.000 Wörter und fünf Stufen, und jedes setzt das vorige voraus. Am Ende von Pareto 1 ist der Berg geschafft: fertig bist du nicht, aber die Sprache ist keine Wand mehr.",

 # ---- FAQ ----
 "Questions": "Fragen",
 "Before you buy": "Bevor du kaufst",
 "<summary>Do I need the base game?</summary>": "<summary>Brauche ich das Grundspiel?</summary>",
 'Yes. Swahili Core is DLC for FlashBoss, so you need the base game as well. Everything else — the lessons, the audio, the drills, the boss fights — is inside the pack. On Windows 10 you also need <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a>, a free download from the Microsoft Store.':
   'Ja. Swahili Core ist ein DLC für FlashBoss, du brauchst also auch das Grundspiel. Alles andere — die Lektionen, die Sprachausgabe, die Übungen, die Bosskämpfe — steckt im Paket. Unter Windows 10 brauchst du außerdem <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a>, einen kostenlosen Download aus dem Microsoft Store.',
 "<summary>Can I study it in my own language?</summary>":
   "<summary>Kann ich in meiner eigenen Sprache lernen?</summary>",
 "Fully. Every card carries its translation, its example translation and its study notes in <b>German, Japanese, Russian, Simplified Chinese and Spanish</b> as well as English, with no gaps, and all 20 reference lessons carry the same six. The game's own interface speaks them too.":
   "Vollständig. Jede Karte trägt ihre Übersetzung, die Übersetzung des Beispielsatzes und ihre Lernhinweise auf <b>Deutsch, Japanisch, Russisch, Vereinfachtem Chinesisch und Spanisch</b> ebenso wie auf Englisch, ohne Lücke, und alle 20 Referenzlektionen tragen dieselben sechs. Die Oberfläche des Spiels spricht sie ebenfalls.",
 "<summary>Which Swahili is this?</summary>": "<summary>Welches Swahili ist das?</summary>",
 "Standard Kiswahili — the one taught in schools and used by the press across East Africa, based on the Zanzibar dialect. The voice is a neural standard Kiswahili voice.":
   "Standard-Kiswahili — das, was in den Schulen unterrichtet und von der Presse in ganz Ostafrika benutzt wird, auf der Grundlage des Sansibar-Dialekts. Die Stimme ist eine neuronale Stimme für Standard-Kiswahili.",
 "<summary>Can I see the words before I buy?</summary>":
   "<summary>Kann ich die Wörter vor dem Kauf sehen?</summary>",
 'All of them. The complete <a href="wordlists.html?lang=Swahili&amp;set=Core">word list</a> and all twenty <a href="lessons.html?lang=Swahili">reference lessons</a> are on this site — free, printable, no account. There is also a <a href="https://flashboss-demo.pages.dev/">playable boss fight</a>.':
   'Alle. Die komplette <a href="wordlists.html?lang=Swahili&amp;set=Core">Wortliste</a> und alle zwanzig <a href="lessons.html?lang=Swahili">Referenzlektionen</a> stehen auf dieser Seite — kostenlos, druckbar, ohne Konto. Es gibt außerdem einen <a href="https://flashboss-demo.pages.dev/">spielbaren Bosskampf</a>.',
 "<summary>Is there a British or American spelling layer?</summary>":
   "<summary>Gibt es eine britische oder amerikanische Schreibebene?</summary>",
 "That layer covers the English packs. Swahili's English is the translation side of the card, and the pack ships one edition of it.":
   "Diese Ebene gehört zu den englischen Paketen. Das Englisch von Swahili ist die Übersetzungsseite der Karte, und davon liefert das Paket eine einzige Fassung.",

 # ---- final ----
 "Start with <i>Habari?</i>": "Fang mit <i>Habari?</i> an",
 "Two machines and a thousand words. The rest of Swahili agrees with them.":
   "Zwei Maschinen und tausend Wörter. Der ganze Rest des Swahili richtet sich danach.",
 "Swahili Core on Steam &rarr;": "Swahili Core auf Steam &rarr;",
}

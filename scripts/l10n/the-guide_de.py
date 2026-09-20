# German strings for the-guide.html.
#
# Sources, in the order they win:
#   1. IP CARE, from the English page's own head comment. The trademarked game
#      name appears NOWHERE on this page and appears nowhere here either, in any
#      language or spelling. The licence framing is the store page's and must not
#      drift: "5E compatible" -> "5E-kompatibel", and "System Reference Document
#      5.2", "SRD" and "5E" stay in their English/technical form. The footer's
#      no-affiliation line is translated in full, all three prongs kept.
#   2. The ratified German bundle copy
#      (flashboss-admin/BUNDLE_COPY_THE_GUIDE_COMPLETE_2026-09-17.md) and the
#      trained German store page (store_page_descriptions/1143255_the_guide.json)
#      wherever either has the sentence: the "im Kopf haben" line, the five
#      what-a-card-is-for clauses, the full-German-edition paragraph, the mixed
#      edition, the bonus edition, the boss-fight kinds, the 2024 ruleset.
#   3. The shipped deck itself, knight/flashcard_sets/The_Guide/core, for rules
#      jargon a German table actually says: Zustand, Zauberplatz, Konzentration,
#      Herausforderungsgrad, Spezies, Talent, Zug, Schadensarten, Rettungswurf,
#      SG. The sample card (Dim Light, cluster1_10) is quoted from its OWN German
#      twin — TargetWord_de, Translation_de, ExampleSentence_de,
#      ExampleTranslation_de, Notes_de — so the page shows the card as the German
#      edition really ships it. ONE DEPARTURE from that twin: the citation stays
#      the English page's "SRD p. 11" as "SRD S. 12", because numbers on the page
#      are never changed. The German card itself cites S. 12, the German SRD's
#      own page; a later pass may prefer that, since the editions section says
#      German cites the German book page by page.
#
# Pack names stay English: The Guide. FlashBoss stays Latin. Numbers are the
# English page's, in German separators; nothing was recounted.
TITLE = "The Guide — FlashBoss"
DESCRIPTION = ("FlashBoss The Guide: die Regeln, die eine Spielleitung im Kopf haben muss, als "
               "Lernkarten. 1.205 Karten in 62 Clustern, 62 Referenzlektionen, ein Bosskampf an "
               "jedem Tor. Eine vollständige deutsche Ausgabe; Japanisch, Chinesisch, Russisch "
               "und Spanisch spielen in deiner Sprache und antworten auf Englisch. "
               "5E-kompatibel, nach dem System Reference Document 5.2 gebaut.")

STRINGS = {
 # ---- nav / chrome ----
 ">packs<": ">Packs<",
 ">card lists<": ">Kartenlisten<",
 ">lessons<": ">Lektionen<",
 ">voices<": ">Stimmen<",
 ">home<": ">Start<",

 # ---- hero ----
 "For the person running the table · <b>out now</b>":
   "Für die Person, die den Tisch leitet · <b>jetzt erhältlich</b>",
 "1,205 cards · 62 clusters": "1.205 Karten · 62 Cluster",
 "The rules a game master needs in their head — not on the page they are turning to.":
   "Die Regeln, die eine Spielleitung im Kopf haben muss — nicht auf der Seite, die sie gerade aufschlägt.",
 "Listen · read · repeat · rate · fight": "Hören · lesen · wiederholen · bewerten · kämpfen",
 # the five clauses are the ratified store line, word for word
 "Every card is one thing you should know cold rather than stop to look up: what a condition does, which die a check calls for, what a DC of 15 is meant to mean, what a stat block is telling you, what a party can actually do at level 5. <b>5E compatible, built from the System Reference Document 5.2.</b>":
   "Jede Karte ist genau eine Sache, die du auswendig wissen solltest, statt sie nachzuschlagen: was ein Zustand bewirkt, welchen Würfel eine Probe verlangt, was ein SG von 15 bedeuten soll, was ein Statblock dir sagt, was eine Gruppe auf Stufe 5 tatsächlich tun kann. <b>5E-kompatibel, nach dem System Reference Document 5.2 gebaut.</b>",
 ">what a card holds</a>": ">was auf einer Karte steht</a>",
 ">languages</a>": ">Sprachen</a>",

 # ---- the argument ----
 ">Why drill the rules at all<": ">Warum die Regeln überhaupt trainieren<",
 "<h2>Looking it up is the thing that breaks the table</h2>":
   "<h2>Nachschlagen ist das, was die Runde kaputtmacht</h2>",
 "A game master's real skill is adjudicating at speed. Everyone at the table can feel the difference between a ruling that arrives in two seconds and one that arrives after ninety seconds of page-turning — and the second one costs you the scene, not just the time.":
   "Das eigentliche Können einer Spielleitung ist, schnell zu entscheiden. Alle am Tisch spüren den Unterschied zwischen einem Urteil, das nach zwei Sekunden kommt, und einem, das nach neunzig Sekunden Blättern kommt — und das zweite kostet dich die Szene, nicht nur die Zeit.",
 "The fix is not a better index. It is <b>knowing the thing</b>: the fifteen conditions, the thirteen damage types, the ability and proficiency tables, challenge rating and the experience it is worth. The numbers you currently flip pages for.":
   "Die Lösung ist kein besseres Register. Sie heißt <b>es wissen</b>: die fünfzehn Zustände, die dreizehn Schadensarten, die Attributs- und Übungstabellen, Herausforderungsgrad und die EP, die er wert ist. Die Zahlen, für die du heute blätterst.",
 "So this is a vocabulary course whose vocabulary happens to be a rules set. Same machine as every other FlashBoss pack — spaced repetition, a boss fight at the end of every cluster — pointed at the things you are expected to have in your head when someone asks whether they can shove the ogre off the bridge.":
   "Das hier ist also ein Vokabelkurs, dessen Vokabular zufällig ein Regelwerk ist. Dieselbe Maschine wie in jedem anderen FlashBoss-Pack — verteilte Wiederholung, ein Bosskampf am Ende jedes Clusters — gerichtet auf die Dinge, die du im Kopf haben sollst, wenn jemand fragt, ob er den Oger von der Brücke schubsen kann.",

 # ---- the card ----
 "<h2>What a card holds</h2>": "<h2>Was auf einer Karte steht</h2>",
 "A real card from tier 1, quoted as it ships. The scene is the point: the rule arrives as something you could narrate, not as an index entry.":
   "Eine echte Karte aus Stufe 1, zitiert wie sie ausgeliefert wird. Die Szene ist der Kern: Die Regel kommt als etwas daher, das du erzählen könntest, nicht als Lexikon-Eintrag.",
 ">the card<": ">die Karte<",
 ">what each part is for<": ">wofür jeder Teil da ist<",

 # the sample card, quoted from its own German twin in cluster1_10 rather than
 # translated here — headword, scene, definition, rule line and notes, German
 # SRD page and all, so the page shows what a German player really sees
 '<div class="hw">Dim Light</div>': '<div class="hw">Dämmriges Licht</div>',
 "“Past the torch's ring the corridor goes grey rather than black, and the ranger squints into it and is not sure what she saw.”":
   "„Jenseits des Fackellichts wird der Gang grau statt schwarz; die Waldläuferin späht hinein und ist sich nicht sicher, was sie gesehen hat.“",
 "Dusk and shadow: sight-based Perception suffers, and Darkvision sees the dark as this.":
   "In Dämmerlicht leidet Wahrnehmung mit Sicht; Dunkelsicht sieht Dunkelheit wie dieses.",
 "Shadow: creates a Lightly Obscured area": "Schatten: leicht verschleierter Bereich",
 "term | the border between bright and dark<br>usually the outer band of a light source · SRD p. 11":
   "Begriff | Übergang zwischen hell und dunkel<br>äußerer Ring vieler Lichtquellen · SRD S. 12",

 # ---- what each part is for: whole <li> each, so no English article survives ----
 "<li><b>The term</b><span>What the table will actually say out loud. This is the answer you are drilled to produce.</span></li>":
   "<li><b>Der Begriff</b><span>Was am Tisch tatsächlich ausgesprochen wird. Das ist die Antwort, auf die du trainiert wirst.</span></li>",
 "<li><b>The scene</b><span>That rule happening at a table. You remember a picture, and the picture carries the rule with it.</span></li>":
   "<li><b>Die Szene</b><span>Diese Regel, wie sie am Tisch passiert. Du merkst dir ein Bild, und das Bild trägt die Regel mit sich.</span></li>",
 "<li><b>The definition</b><span>The meaning you are tested on — short enough to hold, complete enough to rule with.</span></li>":
   "<li><b>Die Definition</b><span>Die Bedeutung, auf die du geprüft wirst — kurz genug zum Behalten, vollständig genug zum Entscheiden.</span></li>",
 "<li><b>The rule line</b><span>The rule as you would say it to a player, in one breath.</span></li>":
   "<li><b>Die Regelzeile</b><span>Die Regel so, wie du sie einem Spieler sagen würdest, in einem Atemzug.</span></li>",
 "<li><b>The numbers</b><span>The category, the figures underneath, and the page of the reference document it comes from.</span></li>":
   "<li><b>Die Zahlen</b><span>Die Kategorie, die Werte darunter und die Seite des Referenzdokuments, aus der die Regel stammt.</span></li>",
 "A key turns that notes line into a map of all 24 card categories, and a second converts every distance and weight on the cards. Both ship inside the game, as do the English and German reference documents.":
   "Eine Taste verwandelt diese Notizzeile in eine Übersicht aller 24 Kartenkategorien, eine zweite rechnet jede Entfernungs- und Gewichtsangabe auf den Karten um. Beide liegen dem Spiel bei, ebenso die englischen und deutschen Referenzdokumente.",

 # ---- the editions ----
 '<span class="tag">Languages</span>': '<span class="tag">Sprachen</span>',
 "<h2>Which edition you get</h2>": "<h2>Welche Ausgabe du bekommst</h2>",
 "This pack is more honest about its languages than most, because they are genuinely not all the same thing. Three kinds:":
   "Dieses Pack ist bei seinen Sprachen ehrlicher als die meisten, weil sie wirklich nicht alle dasselbe sind. Drei Arten:",
 '<div class="h">German<span class="badge">Complete</span></div>':
   '<div class="h">Deutsch<span class="badge">Vollständig</span></div>',
 "<b>A full German edition.</b> Everything in German — headword, definition, rule line, scene and notes on all 1,205 cards, and all 62 reference lessons. It uses the established German rules vocabulary, <i>Rüstungsklasse</i>, <i>Trefferpunkte</i>, <i>Rettungswurf</i>, rather than invented calques, and it cites the German rules edition page by page, so a card sends you to the right page of the book you actually own.":
   "<b>Eine vollständige deutsche Ausgabe.</b> Alles auf Deutsch — Stichwort, Definition, Regelzeile, Szene und Anmerkungen auf allen 1.205 Karten sowie alle 62 Referenzlektionen. Sie verwendet den etablierten deutschen Regelwortschatz, <i>Rüstungsklasse</i>, <i>Trefferpunkte</i>, <i>Rettungswurf</i>, statt erfundener Lehnübersetzungen, und sie zitiert die deutsche Regelwerksausgabe seitenweise, sodass eine Karte dich auf die richtige Seite des Buches schickt, das du wirklich besitzt.",
 '<div class="h">Japanese · Simplified Chinese · Russian · Spanish<span class="badge">Play in yours, answer in English</span></div>':
   '<div class="h">Japanisch · Vereinfachtes Chinesisch · Russisch · Spanisch<span class="badge">Spielen in deiner Sprache, antworten auf Englisch</span></div>',
 "The question and the scene are in your language; the headword you answer with, and the word you hear, are <b>English</b>. A toggle on the card shows the translation whenever you want it, and the 62 reference lessons are written in your language too.":
   "Frage und Szene sind in deiner Sprache; das Stichwort, mit dem du antwortest, und das Wort, das du hörst, sind <b>Englisch</b>. Ein Umschalter auf der Karte zeigt dir die Übersetzung, wann immer du sie willst, und auch die 62 Referenzlektionen sind in deiner Sprache verfasst.",
 "<b>That is deliberate, not a shortcut.</b> You meet each rule in words you already think in, and you leave holding the term the table will actually use. It is the step you need before you sit down at an English-speaking game.":
   "<b>Das ist Absicht, keine Abkürzung.</b> Du triffst jede Regel in Worten, in denen du ohnehin denkst, und behältst am Ende den Begriff, den der Tisch tatsächlich benutzt. Das ist der Schritt, den du brauchst, bevor du an einem englischsprachigen Spiel Platz nimmst.",
 '<div class="h">The all-in-your-language bonus<span class="badge">Beta</span></div>':
   '<div class="h">Der Bonus komplett in deiner Sprache<span class="badge">Beta</span></div>',
 "If you would rather have the whole card in Japanese, Simplified Chinese, Russian or Spanish, that edition is there as well. It comes with compromises, stated plainly: <b>the spoken word stays English</b>, there is no audio beyond it, and it carries <b>no revision drills</b>. A bonus, not a course in its own right — you already speak your own language.":
   "Wenn du lieber die ganze Karte auf Japanisch, vereinfachtem Chinesisch, Russisch oder Spanisch hättest, gibt es diese Ausgabe auch. Sie bringt Kompromisse mit sich, klar gesagt: <b>das gesprochene Wort bleibt Englisch</b>, darüber hinaus gibt es keinen Ton, und sie trägt <b>keine Wiederholungsübungen</b>. Ein Bonus, kein eigenständiger Kurs — deine eigene Sprache sprichst du schon.",

 # ---- the tiers: whole <li> each ----
 ">The climb<": ">Der Aufstieg<",
 "<h2>Five tiers, each ending in something you can do</h2>":
   "<h2>Fünf Stufen, jede endet in etwas, das du kannst</h2>",
 '<li><span class="w">Adjudicate a check</span><span class="d">The die, the DC, what the number is meant to mean, and the conditions that change it.</span></li>':
   '<li><span class="w">Eine Probe bewerten</span><span class="d">Der Würfel, der SG, was die Zahl bedeuten soll, und die Zustände, die sie verändern.</span></li>',
 '<li><span class="w">Run a fight</span><span class="d">The turn, the actions in it, the damage types, and what a condition does to whoever is carrying it.</span></li>':
   '<li><span class="w">Einen Kampf leiten</span><span class="d">Der Zug, die Aktionen darin, die Schadensarten und was ein Zustand mit dem macht, der ihn trägt.</span></li>',
 '<li><span class="w">Run a caster and read a stat block</span><span class="d">Slots, concentration, ranges — and a block of numbers you can look at and know what it will do.</span></li>':
   '<li><span class="w">Einen Zauberwirker führen und einen Statblock lesen</span><span class="d">Zauberplätze, Konzentration, Reichweiten — und ein Block aus Zahlen, den du ansiehst und weißt, was er anrichten wird.</span></li>',
 '<li><span class="w">Know what the options bring</span><span class="d">The twelve classes, the nine species, and what the feats actually give a character.</span></li>':
   '<li><span class="w">Wissen, was die Optionen bringen</span><span class="d">Die zwölf Klassen, die neun Spezies und was die Talente einer Figur wirklich geben.</span></li>',
 '<li><span class="w">Build encounters, hazards and treasure</span><span class="d">Challenge rating against experience, what a party survives, and what to hand out afterwards.</span></li>':
   '<li><span class="w">Begegnungen, Gefahren und Schätze bauen</span><span class="d">Herausforderungsgrad gegen EP, was eine Gruppe übersteht, und was danach zu verteilen ist.</span></li>',
 "62 reference lessons, 82 pages, one waiting at the head of every cluster — in every language the pack ships.":
   "62 Referenzlektionen, 82 Seiten, je eine am Anfang jedes Clusters — in jeder Sprache, in der das Pack erscheint.",

 # ---- the method: whole <dt>+<dd> each ----
 ">How it sticks<": ">Warum es hängenbleibt<",
 "<h2>Flashcards as an integrated system</h2>": "<h2>Lernkarten als geschlossenes System</h2>",
 "<dt>Cards</dt><dd><b>1,205 cards in 62 themed clusters</b> across five tiers, every one carrying its term, its scene, its definition, its rule line and its numbers.</dd>":
   "<dt>Karten</dt><dd><b>1.205 Karten in 62 thematischen Clustern</b> über fünf Stufen, jede mit ihrem Begriff, ihrer Szene, ihrer Definition, ihrer Regelzeile und ihren Zahlen.</dd>",
 "<dt>Boss fights</dt><dd>Three kinds, not one: <b>name the creature, spell or term</b> from its definition; <b>give your ruling</b> on a scene; <b>read the number</b> off a table. No cluster is cleared until its definitions are mastered.</dd>":
   "<dt>Bosskämpfe</dt><dd>Drei Arten, nicht eine: <b>Kreatur, Zauber oder Begriff benennen</b> anhand ihrer Definition; <b>dein Urteil abgeben</b> zu einer Szene; <b>die Zahl ablesen</b> aus einer Tabelle. Kein Cluster gilt als gemeistert, bis seine Definitionen sitzen.</dd>",
 "<dt>Lessons</dt><dd><b>62 reference lessons, 82 pages</b> — one at the head of every cluster, in every language the pack ships.</dd>":
   "<dt>Lektionen</dt><dd><b>62 Referenzlektionen, 82 Seiten</b> — je eine am Anfang jedes Clusters, in jeder Sprache, in der das Pack erscheint.</dd>",
 "<dt>Fibonacci SRS</dt><dd>Rate each card 0–5. The better you know a rule, the longer before it comes back.</dd>":
   "<dt>Fibonacci-SRS</dt><dd>Bewerte jede Karte von 0–5. Je besser du eine Regel kennst, desto länger dauert es, bis sie wiederkommt.</dd>",
 '<dt>Audio</dt><dd>The Guide reads aloud in its own bundled voice. Samples are on the <a href="voices.html">voices page</a>.</dd>':
   '<dt>Audio</dt><dd>The Guide liest mit seiner eigenen mitgelieferten Stimme vor. Hörproben gibt es auf der <a href="voices.html">Stimmen-Seite</a>.</dd>',
 "<dt>The ruleset</dt><dd>The <b>2024 revision</b> as it now stands — the terms, the numbers and the procedures expected today. If your rules knowledge is a decade old, you relearn what changed by drilling what is, rather than reading a list of differences.</dd>":
   "<dt>Das Regelwerk</dt><dd>Die <b>Fassung von 2024</b>, genau so, wie sie jetzt steht — die Begriffe, die Zahlen und die Abläufe, die heute erwartet werden. Wenn dein Regelwissen ein Jahrzehnt alt ist, lernst du das Geänderte neu, indem du trainierst, was gilt, statt eine Liste der Unterschiede zu lesen.</dd>",

 # ---- the FAQ ----
 ">Questions<": ">Fragen<",
 "<h2>Before you buy</h2>": "<h2>Bevor du kaufst</h2>",
 "<summary>Which edition of the rules is this?</summary>":
   "<summary>Welche Regelausgabe ist das?</summary>",
 "The <b>2024 revision</b>, built from the System Reference Document 5.2. Conditions, spells, species and stat blocks were revised between the 2014 rules and these, so if your table runs the older edition some of these cards will drill you on numbers you do not use. Check which one your table plays before you buy.":
   "Die <b>Fassung von 2024</b>, nach dem System Reference Document 5.2 gebaut. Zustände, Zauber, Spezies und Statblöcke wurden zwischen den Regeln von 2014 und diesen überarbeitet; spielt dein Tisch also die ältere Ausgabe, trainieren dich manche dieser Karten auf Zahlen, die du nicht benutzt. Prüfe vor dem Kauf, welche dein Tisch spielt.",
 "<summary>Do I need the base game?</summary>": "<summary>Brauche ich das Grundspiel?</summary>",
 'Yes. The Guide is DLC for FlashBoss, so you need the base game as well. On Windows 10 you also need <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a>, a free download from the Microsoft Store.':
   'Ja. The Guide ist DLC für FlashBoss, du brauchst also auch das Grundspiel. Unter Windows 10 brauchst du außerdem <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a>, einen kostenlosen Download aus dem Microsoft Store.',
 "<summary>I am a player, not a game master. Is it for me?</summary>":
   "<summary>Ich bin Spieler, nicht Spielleitung. Ist das etwas für mich?</summary>",
 "It is built for the person running the table, and that is where it pays most. A player who wants to stop asking what a condition does, or who is about to run their first game, gets the same cards — the tiers just matter less in that order.":
   "Es ist für die Person gebaut, die den Tisch leitet, und dort zahlt es sich am meisten aus. Wer als Spieler aufhören will zu fragen, was ein Zustand bewirkt, oder wer bald seine erste Runde leitet, bekommt dieselben Karten — die Stufen zählen in dieser Reihenfolge nur weniger.",
 "<summary>Is my language a full edition or a mixed one?</summary>":
   "<summary>Ist meine Sprache eine vollständige oder eine gemischte Ausgabe?</summary>",
 'German is the full edition. <b>Japanese, Simplified Chinese, Russian and Spanish</b> play in your language and answer in English, with a toggle to the translation on the card and the lessons written in your language — and each also carries an all-in-your-language bonus edition in beta, with English audio and no drills. The <a href="#editions">languages section</a> above says exactly what each one gives you.':
   'Deutsch ist die vollständige Ausgabe. <b>Japanisch, vereinfachtes Chinesisch, Russisch und Spanisch</b> spielen in deiner Sprache und antworten auf Englisch, mit einem Umschalter zur Übersetzung auf der Karte und Lektionen in deiner Sprache — und jede trägt außerdem eine Bonusausgabe komplett in deiner Sprache als Beta, mit englischem Ton und ohne Übungen. Der <a href="#editions">Abschnitt über die Sprachen</a> weiter oben sagt genau, was dir jede einzelne gibt.',
 "<summary>Can I see the cards before I buy?</summary>":
   "<summary>Kann ich die Karten vor dem Kauf sehen?</summary>",
 'The card lists and reference lessons for FlashBoss packs are on this site, free and printable, and there is a <a href="https://flashboss-demo.pages.dev/">playable boss fight</a> if you want to see the mechanic before anything else.':
   'Die Kartenlisten und Referenzlektionen der FlashBoss-Packs stehen auf dieser Seite, kostenlos und druckbar, und es gibt einen <a href="https://flashboss-demo.pages.dev/">spielbaren Bosskampf</a>, falls du die Mechanik zuerst sehen willst.',

 # ---- the close ----
 "<h2>Know it, don't look it up.</h2>": "<h2>Wissen statt nachschlagen.</h2>",
 "1,205 cards, 62 clusters, and a boss fight at every one of them.":
   "1.205 Karten, 62 Cluster und an jedem davon ein Bosskampf.",
 "The Guide on Steam &rarr;": "The Guide auf Steam &rarr;",

 # ---- the legal line: translated in full, all three prongs, nothing softened ----
 "5E compatible. Built from the System Reference Document 5.2. FlashBoss is not affiliated with, endorsed by, or sponsored by any rules publisher.":
   "5E-kompatibel. Nach dem System Reference Document 5.2 gebaut. FlashBoss ist mit keinem Regelverlag verbunden, wird von keinem unterstützt und von keinem gesponsert.",
}

# The sample card cites SRD S. 12 where the English page cites SRD p. 11, and
# that is correct, not a slip. The German edition of The Guide ships a full
# German card — Notes_de on Dim Light in
# knight/flashcard_sets/The_Guide/core/tier_1/cluster1_10_vision_light_hiding
# reads "… äußerer Ring vieler Lichtquellen · SRD S. 12" — and this very page
# says the German edition "cites the German rules edition page by page, so a
# card sends you to the right page of the book you actually own". Showing p. 11
# to a German reader would contradict the product and the sentence above it.
# It was "corrected" to 11 once during this session and put back after checking
# the deck. NUMBERS_CHANGED tells verify.py this one is deliberate.
NUMBERS_CHANGED = {
    "11": "the English card cites the English SRD page; the German card cites S. 12",
    "12": "the German rules edition's page for Dim Light, from the shipped Notes_de",
}

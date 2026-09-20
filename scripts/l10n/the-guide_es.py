# Spanish (Latin America) strings for the-guide.html.
#
# Sources, in the order they win:
#   1. IP CARE, from the English page's own head comment. The trademarked game
#      name appears NOWHERE on this page and appears nowhere here either, in any
#      language or spelling. The licence framing is the store page's and must not
#      drift: "5E compatible" -> "Compatible con 5E", and "System Reference
#      Document 5.2", "SRD" and "5E" stay in their English/technical form. The
#      footer's no-affiliation line is translated in full, all three prongs kept
#      (not affiliated / not endorsed / not sponsored), nothing softened.
#   2. The ratified Spanish bundle copy
#      (flashboss-admin/BUNDLE_COPY_THE_GUIDE_COMPLETE_2026-09-17.md) wherever it
#      has the sentence: the "necesita en la cabeza" line, the five
#      what-a-card-is-for clauses word for word ("qué hace un estado, qué dado
#      pide una prueba, qué significa una CD 15, qué te está diciendo un bloque
#      de estadísticas"), "Compatible con 5E, basado en el System Reference
#      Document 5.2", "la revisión de 2024", "director de juego", "conmutador".
#   3. The shipped deck itself, knight/flashcard_sets/The_Guide/core, for rules
#      jargon a Spanish-speaking table actually says: estado, prueba, CD, bloque
#      de estadísticas, tirada de salvación, valor de desafío, tipos de daño,
#      especies, dotes, espacios de conjuro, Percepción, visión en la oscuridad.
#      The sample card (Dim Light, cluster1_10) is quoted from its OWN Spanish
#      twin — TargetWord_es, Translation_es, ExampleSentence_es,
#      ExampleTranslation_es, Notes_es — so the page shows the card as the
#      Spanish edition really ships it. ONE DEPARTURE from that twin: the
#      citation stays the English page's "SRD p. 11", because a page number on
#      this page is a fact and is never changed. The Spanish card itself cites
#      p. 12; a later pass may prefer that, but not this one.
#   4. The live Spanish pages for house vocabulary: "tarjetas" (glossary_es and
#      immersion.es.html; the ratified Guide sheet says "cartas" — see the note
#      below), "cluster/clusters", "boss fight/boss fights", "juego base",
#      "SRS de Fibonacci", "Escuchar · Leer · Repetir · Calificar · Luchar",
#      "paquetes", "lecciones", "voces", "inicio", « » for quoted speech.
#
# TARJETAS vs CARTAS — the one real departure from a ratified sheet. The Guide's
# own Spanish bundle copy says "cartas". glossary_es.txt (settled on the
# immersion page) says Cards -> Tarjetas, immersion.es.html uses "tarjetas" 28
# times, and every Roots/English page this one sits beside uses "tarjetas" too.
# The site term wins here so The Guide reads as part of the same catalogue; the
# store copy is untouched. Flagged for the owner.
#
# Pack names stay English: The Guide. FlashBoss stays Latin. Register is tú,
# Latin American vocabulary. Numbers are the English page's, in Spanish
# separators; nothing was recounted, and "SRD p. 11" is still page eleven.
TITLE = "The Guide — FlashBoss"
DESCRIPTION = ("FlashBoss The Guide: las reglas que un director de juego necesita en la cabeza, "
               "en tarjetas. 1.205 tarjetas en 62 clusters, 62 lecciones de referencia, un boss "
               "fight en cada puerta. Una edición completa en alemán; el japonés, el chino, el "
               "ruso y el español se juegan en tu idioma y responden en inglés. Compatible con "
               "5E, basado en el System Reference Document 5.2.")

STRINGS = {
 # ---- nav / chrome ----
 ">packs<": ">paquetes<",
 # the site says "vocabulario" for the word-list page, but this pack's lists are
 # rules cards, not vocabulary, so the English page's own distinction is kept
 ">card lists<": ">listas de tarjetas<",
 ">lessons<": ">lecciones<",
 ">voices<": ">voces<",
 ">home<": ">inicio<",

 # ---- hero ----
 "For the person running the table · <b>out now</b>":
   "Para quien dirige la mesa · <b>ya disponible</b>",
 "1,205 cards · 62 clusters": "1.205 tarjetas · 62 clusters",
 "The rules a game master needs in their head — not on the page they are turning to.":
   "Las reglas que un director de juego necesita en la cabeza — no en la página que está buscando.",
 # the site's own sig line, as the other Spanish pack pages render it
 "Listen · read · repeat · rate · fight": "Escuchar · Leer · Repetir · Calificar · Luchar",
 # the five clauses are the ratified store line, word for word
 "Every card is one thing you should know cold rather than stop to look up: what a condition does, which die a check calls for, what a DC of 15 is meant to mean, what a stat block is telling you, what a party can actually do at level 5. <b>5E compatible, built from the System Reference Document 5.2.</b>":
   "Cada tarjeta es una sola cosa que deberías saber de memoria en vez de detenerte a consultarla: qué hace un estado, qué dado pide una prueba, qué significa una CD 15, qué te está diciendo un bloque de estadísticas, qué puede hacer de verdad un grupo de nivel 5. <b>Compatible con 5E, basado en el System Reference Document 5.2.</b>",
 ">what a card holds</a>": ">qué lleva una tarjeta</a>",
 ">languages</a>": ">idiomas</a>",

 # ---- the argument ----
 ">Why drill the rules at all<": ">Por qué entrenar las reglas<",
 "<h2>Looking it up is the thing that breaks the table</h2>":
   "<h2>Consultarlo es lo que rompe la mesa</h2>",
 "A game master's real skill is adjudicating at speed. Everyone at the table can feel the difference between a ruling that arrives in two seconds and one that arrives after ninety seconds of page-turning — and the second one costs you the scene, not just the time.":
   "La verdadera habilidad de un director de juego es arbitrar rápido. Todos en la mesa notan la diferencia entre un fallo que llega en dos segundos y uno que llega tras noventa segundos de pasar páginas — y el segundo te cuesta la escena, no solo el tiempo.",
 "The fix is not a better index. It is <b>knowing the thing</b>: the fifteen conditions, the thirteen damage types, the ability and proficiency tables, challenge rating and the experience it is worth. The numbers you currently flip pages for.":
   "La solución no es un índice mejor. Es <b>saberlo</b>: los quince estados, los trece tipos de daño, las tablas de características y de competencia, el valor de desafío y la experiencia que vale. Los números por los que hoy pasas páginas.",
 "So this is a vocabulary course whose vocabulary happens to be a rules set. Same machine as every other FlashBoss pack — spaced repetition, a boss fight at the end of every cluster — pointed at the things you are expected to have in your head when someone asks whether they can shove the ogre off the bridge.":
   "Así que esto es un curso de vocabulario cuyo vocabulario resulta ser un reglamento. La misma máquina que cualquier otro paquete de FlashBoss — repetición espaciada, un boss fight al final de cada cluster — apuntada a las cosas que se espera que tengas en la cabeza cuando alguien pregunta si puede empujar al ogro fuera del puente.",

 # ---- the card ----
 "<h2>What a card holds</h2>": "<h2>Qué lleva una tarjeta</h2>",
 "A real card from tier 1, quoted as it ships. The scene is the point: the rule arrives as something you could narrate, not as an index entry.":
   "Una tarjeta real del nivel 1, citada tal como se publica. La escena es lo importante: la regla llega como algo que podrías narrar, no como una entrada de índice.",
 ">the card<": ">la tarjeta<",
 ">what each part is for<": ">para qué sirve cada parte<",

 # the sample card, quoted from its own Spanish twin in cluster1_10 rather than
 # translated here — headword, scene, definition, rule line and notes, so the
 # page shows what a Spanish player really sees. The citation is the ONLY thing
 # kept from the English page: SRD p. 11 is page eleven and stays page eleven.
 # Quotation marks are « », which is what the Spanish pages already use.
 '<div class="hw">Dim Light</div>': '<div class="hw">Luz tenue</div>',
 "“Past the torch's ring the corridor goes grey rather than black, and the ranger squints into it and is not sure what she saw.”":
   "«Pasado el anillo de la antorcha el pasillo se vuelve gris en vez de negro, y la exploradora entorna los ojos sin estar segura.»",
 "Dusk and shadow: sight-based Perception suffers, and Darkvision sees the dark as this.":
   "Ocaso y sombra: la Percepción por la vista sufre, y la visión en la oscuridad la ve así.",
 "Shadow: creates a Lightly Obscured area":
   "También llamada «sombras»: hace que la zona esté ligeramente oscura.",
 "term | the border between bright and dark<br>usually the outer band of a light source · SRD p. 11":
   "término | la frontera entre lo brillante y lo oscuro<br>el ocaso y la luna llena la dan · SRD p. 11",

 # ---- what each part is for: whole <li> each, so no English article survives ----
 "<li><b>The term</b><span>What the table will actually say out loud. This is the answer you are drilled to produce.</span></li>":
   "<li><b>El término</b><span>Lo que en la mesa se va a decir en voz alta. Esa es la respuesta que entrenas para dar.</span></li>",
 "<li><b>The scene</b><span>That rule happening at a table. You remember a picture, and the picture carries the rule with it.</span></li>":
   "<li><b>La escena</b><span>Esa regla ocurriendo en una mesa. Recuerdas una imagen, y la imagen se lleva la regla consigo.</span></li>",
 "<li><b>The definition</b><span>The meaning you are tested on — short enough to hold, complete enough to rule with.</span></li>":
   "<li><b>La definición</b><span>El significado sobre el que te examinan — corto para retenerlo, completo para arbitrar con él.</span></li>",
 "<li><b>The rule line</b><span>The rule as you would say it to a player, in one breath.</span></li>":
   "<li><b>La línea de regla</b><span>La regla tal como se la dirías a un jugador, de un tirón.</span></li>",
 "<li><b>The numbers</b><span>The category, the figures underneath, and the page of the reference document it comes from.</span></li>":
   "<li><b>Los números</b><span>La categoría, las cifras de abajo y la página del documento de referencia de la que viene.</span></li>",
 "A key turns that notes line into a map of all 24 card categories, and a second converts every distance and weight on the cards. Both ship inside the game, as do the English and German reference documents.":
   "Una tecla convierte esa línea de notas en un mapa de las 24 categorías de tarjeta, y una segunda convierte cada distancia y cada peso de las tarjetas. Las dos vienen dentro del juego, igual que los documentos de referencia en inglés y en alemán.",

 # ---- the editions ----
 '<span class="tag">Languages</span>': '<span class="tag">Idiomas</span>',
 "<h2>Which edition you get</h2>": "<h2>Qué edición te toca</h2>",
 "This pack is more honest about its languages than most, because they are genuinely not all the same thing. Three kinds:":
   "Este paquete es más honesto con sus idiomas que la mayoría, porque de verdad no todos son lo mismo. Tres clases:",
 '<div class="h">German<span class="badge">Complete</span></div>':
   '<div class="h">Alemán<span class="badge">Completa</span></div>',
 "<b>A full German edition.</b> Everything in German — headword, definition, rule line, scene and notes on all 1,205 cards, and all 62 reference lessons. It uses the established German rules vocabulary, <i>Rüstungsklasse</i>, <i>Trefferpunkte</i>, <i>Rettungswurf</i>, rather than invented calques, and it cites the German rules edition page by page, so a card sends you to the right page of the book you actually own.":
   "<b>Una edición completa en alemán.</b> Todo en alemán — palabra principal, definición, línea de regla, escena y notas en las 1.205 tarjetas, y las 62 lecciones de referencia. Usa el vocabulario de reglas alemán ya establecido, <i>Rüstungsklasse</i>, <i>Trefferpunkte</i>, <i>Rettungswurf</i>, en vez de calcos inventados, y cita la edición alemana de las reglas página por página, de modo que una tarjeta te manda a la página correcta del libro que de verdad tienes.",
 '<div class="h">Japanese · Simplified Chinese · Russian · Spanish<span class="badge">Play in yours, answer in English</span></div>':
   '<div class="h">Japonés · Chino simplificado · Ruso · Español<span class="badge">Juega en el tuyo, responde en inglés</span></div>',
 "The question and the scene are in your language; the headword you answer with, and the word you hear, are <b>English</b>. A toggle on the card shows the translation whenever you want it, and the 62 reference lessons are written in your language too.":
   "La pregunta y la escena están en tu idioma; la palabra principal con la que respondes, y la palabra que oyes, están en <b>inglés</b>. Un conmutador en la tarjeta muestra la traducción cuando la quieras, y las 62 lecciones de referencia también están escritas en tu idioma.",
 "<b>That is deliberate, not a shortcut.</b> You meet each rule in words you already think in, and you leave holding the term the table will actually use. It is the step you need before you sit down at an English-speaking game.":
   "<b>Eso es deliberado, no un atajo.</b> Te encuentras cada regla en palabras en las que ya piensas, y te vas con el término que la mesa va a usar de verdad. Es el paso que necesitas antes de sentarte a una partida en inglés.",
 '<div class="h">The all-in-your-language bonus<span class="badge">Beta</span></div>':
   '<div class="h">El extra todo en tu idioma<span class="badge">Beta</span></div>',
 "If you would rather have the whole card in Japanese, Simplified Chinese, Russian or Spanish, that edition is there as well. It comes with compromises, stated plainly: <b>the spoken word stays English</b>, there is no audio beyond it, and it carries <b>no revision drills</b>. A bonus, not a course in its own right — you already speak your own language.":
   "Si prefieres la tarjeta entera en japonés, chino simplificado, ruso o español, esa edición también está. Viene con concesiones, dichas sin rodeos: <b>la palabra hablada sigue siendo inglesa</b>, no hay más audio que ese, y <b>no lleva ejercicios de repaso</b>. Un extra, no un curso por sí solo — tu propio idioma ya lo hablas.",

 # ---- the tiers: whole <li> each ----
 ">The climb<": ">La subida<",
 "<h2>Five tiers, each ending in something you can do</h2>":
   "<h2>Cinco niveles, cada uno termina en algo que sabes hacer</h2>",
 '<li><span class="w">Adjudicate a check</span><span class="d">The die, the DC, what the number is meant to mean, and the conditions that change it.</span></li>':
   '<li><span class="w">Arbitrar una prueba</span><span class="d">El dado, la CD, qué significa el número, y los estados que lo cambian.</span></li>',
 '<li><span class="w">Run a fight</span><span class="d">The turn, the actions in it, the damage types, and what a condition does to whoever is carrying it.</span></li>':
   '<li><span class="w">Dirigir un combate</span><span class="d">El turno, las acciones que caben en él, los tipos de daño, y qué le hace un estado a quien lo lleva encima.</span></li>',
 '<li><span class="w">Run a caster and read a stat block</span><span class="d">Slots, concentration, ranges — and a block of numbers you can look at and know what it will do.</span></li>':
   '<li><span class="w">Llevar un lanzador de conjuros y leer un bloque de estadísticas</span><span class="d">Espacios de conjuro, concentración, alcances — y un bloque de números que miras y sabes qué va a hacer.</span></li>',
 '<li><span class="w">Know what the options bring</span><span class="d">The twelve classes, the nine species, and what the feats actually give a character.</span></li>':
   '<li><span class="w">Saber qué aportan las opciones</span><span class="d">Las doce clases, las nueve especies, y qué le dan realmente las dotes a un personaje.</span></li>',
 '<li><span class="w">Build encounters, hazards and treasure</span><span class="d">Challenge rating against experience, what a party survives, and what to hand out afterwards.</span></li>':
   '<li><span class="w">Construir encuentros, peligros y tesoro</span><span class="d">El valor de desafío frente a la experiencia, qué sobrevive un grupo, y qué repartir después.</span></li>',
 "62 reference lessons, 82 pages, one waiting at the head of every cluster — in every language the pack ships.":
   "62 lecciones de referencia, 82 páginas, una esperando al principio de cada cluster — en todos los idiomas en los que sale el paquete.",

 # ---- the method: whole <dt>+<dd> each ----
 ">How it sticks<": ">Por qué se queda<",
 "<h2>Flashcards as an integrated system</h2>": "<h2>Tarjetas como sistema integrado</h2>",
 "<dt>Cards</dt><dd><b>1,205 cards in 62 themed clusters</b> across five tiers, every one carrying its term, its scene, its definition, its rule line and its numbers.</dd>":
   "<dt>Tarjetas</dt><dd><b>1.205 tarjetas en 62 clusters temáticos</b> repartidas en cinco niveles, cada una con su término, su escena, su definición, su línea de regla y sus números.</dd>",
 "<dt>Boss fights</dt><dd>Three kinds, not one: <b>name the creature, spell or term</b> from its definition; <b>give your ruling</b> on a scene; <b>read the number</b> off a table. No cluster is cleared until its definitions are mastered.</dd>":
   "<dt>Boss fights</dt><dd>Tres clases, no una: <b>nombrar la criatura, el hechizo o el término</b> por su definición; <b>dar tu fallo</b> sobre una escena; <b>leer el número</b> en una tabla. Ningún cluster se supera hasta dominar sus definiciones.</dd>",
 "<dt>Lessons</dt><dd><b>62 reference lessons, 82 pages</b> — one at the head of every cluster, in every language the pack ships.</dd>":
   "<dt>Lecciones</dt><dd><b>62 lecciones de referencia, 82 páginas</b> — una al principio de cada cluster, en todos los idiomas en los que sale el paquete.</dd>",
 "<dt>Fibonacci SRS</dt><dd>Rate each card 0–5. The better you know a rule, the longer before it comes back.</dd>":
   "<dt>SRS de Fibonacci</dt><dd>Califica cada tarjeta de 0 a 5. Cuanto mejor conoces una regla, más tarda en volver.</dd>",
 '<dt>Audio</dt><dd>The Guide reads aloud in its own bundled voice. Samples are on the <a href="voices.html">voices page</a>.</dd>':
   '<dt>Audio</dt><dd>The Guide lee en voz alta con su propia voz incluida. Hay muestras en la <a href="voices.html">página de voces</a>.</dd>',
 "<dt>The ruleset</dt><dd>The <b>2024 revision</b> as it now stands — the terms, the numbers and the procedures expected today. If your rules knowledge is a decade old, you relearn what changed by drilling what is, rather than reading a list of differences.</dd>":
   "<dt>El reglamento</dt><dd>La <b>revisión de 2024</b> tal como está ahora — los términos, los números y los procedimientos que hoy se esperan. Si tu conocimiento de las reglas tiene ya una década, vuelves a aprender lo que cambió entrenando lo que rige, en vez de leer una lista de diferencias.</dd>",

 # ---- the FAQ ----
 ">Questions<": ">Preguntas<",
 "<h2>Before you buy</h2>": "<h2>Antes de comprar</h2>",
 "<summary>Which edition of the rules is this?</summary>":
   "<summary>¿De qué edición de las reglas se trata?</summary>",
 "The <b>2024 revision</b>, built from the System Reference Document 5.2. Conditions, spells, species and stat blocks were revised between the 2014 rules and these, so if your table runs the older edition some of these cards will drill you on numbers you do not use. Check which one your table plays before you buy.":
   "La <b>revisión de 2024</b>, basada en el System Reference Document 5.2. Los estados, los hechizos, las especies y los bloques de estadísticas se revisaron entre las reglas de 2014 y estas, así que si tu mesa juega la edición anterior algunas de estas tarjetas te entrenarán con números que no usas. Comprueba cuál juega tu mesa antes de comprar.",
 "<summary>Do I need the base game?</summary>": "<summary>¿Necesito el juego base?</summary>",
 'Yes. The Guide is DLC for FlashBoss, so you need the base game as well. On Windows 10 you also need <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a>, a free download from the Microsoft Store.':
   'Sí. The Guide es DLC de FlashBoss, así que también necesitas el juego base. En Windows 10 necesitas además <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a>, una descarga gratuita de la Microsoft Store.',
 "<summary>I am a player, not a game master. Is it for me?</summary>":
   "<summary>Soy jugador, no director de juego. ¿Es para mí?</summary>",
 "It is built for the person running the table, and that is where it pays most. A player who wants to stop asking what a condition does, or who is about to run their first game, gets the same cards — the tiers just matter less in that order.":
   "Está hecho para quien dirige la mesa, y ahí es donde más rinde. Un jugador que quiere dejar de preguntar qué hace un estado, o que está por dirigir su primera partida, recibe las mismas tarjetas — solo que en ese caso los niveles importan menos.",
 "<summary>Is my language a full edition or a mixed one?</summary>":
   "<summary>¿Mi idioma es una edición completa o una mixta?</summary>",
 'German is the full edition. <b>Japanese, Simplified Chinese, Russian and Spanish</b> play in your language and answer in English, with a toggle to the translation on the card and the lessons written in your language — and each also carries an all-in-your-language bonus edition in beta, with English audio and no drills. The <a href="#editions">languages section</a> above says exactly what each one gives you.':
   'El alemán es la edición completa. <b>El japonés, el chino simplificado, el ruso y el español</b> se juegan en tu idioma y responden en inglés, con un conmutador a la traducción en la tarjeta y las lecciones escritas en tu idioma — y cada uno lleva además una edición extra todo en tu idioma, en beta, con audio en inglés y sin ejercicios. La <a href="#editions">sección de idiomas</a> de arriba dice exactamente qué te da cada uno.',
 "<summary>Can I see the cards before I buy?</summary>":
   "<summary>¿Puedo ver las tarjetas antes de comprar?</summary>",
 'The card lists and reference lessons for FlashBoss packs are on this site, free and printable, and there is a <a href="https://flashboss-demo.pages.dev/">playable boss fight</a> if you want to see the mechanic before anything else.':
   'Las listas de tarjetas y las lecciones de referencia de los paquetes de FlashBoss están en este sitio, gratis y listas para imprimir, y hay un <a href="https://flashboss-demo.pages.dev/">boss fight jugable</a> si quieres ver la mecánica antes que nada.',

 # ---- the close ----
 "<h2>Know it, don't look it up.</h2>": "<h2>Sábelo, no lo consultes.</h2>",
 "1,205 cards, 62 clusters, and a boss fight at every one of them.":
   "1.205 tarjetas, 62 clusters y un boss fight en cada uno de ellos.",
 "The Guide on Steam &rarr;": "The Guide en Steam &rarr;",

 # ---- the legal line: translated in full, all three prongs, nothing softened ----
 "5E compatible. Built from the System Reference Document 5.2. FlashBoss is not affiliated with, endorsed by, or sponsored by any rules publisher.":
   "Compatible con 5E. Basado en el System Reference Document 5.2. FlashBoss no está afiliada a ninguna editorial de reglas, ninguna la respalda y ninguna la patrocina.",
}

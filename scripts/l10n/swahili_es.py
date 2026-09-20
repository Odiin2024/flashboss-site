# Spanish (Latin America) strings for swahili.html.
# The store-facing sentences follow the ratified Spanish bundle copy
# (flashboss-admin/BUNDLE_COPY_SWAHILI_2026-09-08.md) wherever that sheet has
# them — "suajili" for the language, "niveles 1–15" for the tiers, "oración de
# ejemplo", "notas de estudio", the six-language list ("alemán, japonés, ruso,
# chino simplificado y español"). The method and FAQ wording follows the Spanish
# course pages that already exist (french.es.html, greek-roots.es.html,
# english.es.html): "Cómo se fija", "Las tarjetas como sistema integrado",
# "SRS de Fibonacci", "Califica cada tarjeta de 0 a 5", "dejan tu mazo diario
# para siempre", "Es síntesis, no la grabación de una persona", "Preguntas",
# and the Windows Terminal answer. The rest is mine.
#
# Two terms follow the LIVE SITE and the immersion glossary rather than the
# Steam sheet, exactly as immersion_es.py already settled them: "cluster"
# (the sheet says "clúster") and "boss fight" (the sheet says "pelea contra un
# jefe"); home.es.html carries "boss fight" in its own <title>. "tarjetas" for
# cards follows the glossary and the newer Roots pages, not the older
# "cartas" of french.es.html.
#
# PAGE CANON, held here:
#   * every Swahili word, form and example SENTENCE is left byte-identical —
#     anaendesha, tulisafiri, walipanda, the three pack sentences, gari's card,
#     the ten noun-class names (m/wa, ji/ma, ku, pa …). Only the gloss after the
#     em dash becomes Spanish, because the card carries a Spanish gloss too.
#   * pack names stay English: Swahili Core, Swahili Pareto 1, Swahili Pareto 2,
#     Core, Pareto 1, Pareto 2. So does FlashBoss.
#   * grammar terms are the standard Spanish ones: clase nominal, concordancia,
#     tiempo, sujeto, objeto, causativo, presente.
#   * the page's counts (1.000 / 40 / 20 / 14 / cinco niveles) are the recount of
#     2026-09-19 and are reproduced exactly; the 2026-09-08 bundle sheet's
#     "49 lecciones" predates it and does not win.
#   * banned and absent: hours, CEFR codes, prices, discounts, and a date for
#     anything already out.
#
# Register: tú, Latin American vocabulary (auto, manejar, noticieros,
# computadora — the marker about.es.html already uses).
TITLE = "Suajili — FlashBoss"
DESCRIPTION = ("FlashBoss Suajili: 1.000 palabras en 40 clusters y 20 lecciones de referencia, la "
               "clase nominal nombrada en cada sustantivo, una voz neuronal de kiswahili y un boss "
               "fight en cada puerta. Traducciones y notas de estudio en seis idiomas. "
               "Swahili Core ya está en Steam.")

STRINGS = {
 # ---- nav / chrome / footer ----
 ">packs<": ">paquetes<",
 ">word list<": ">vocabulario<",
 ">lessons<": ">lecciones<",
 ">voices<": ">voces<",
 ">home<": ">inicio<",

 # ---- hero ----
 "The newest course · <b>1,000 words out now</b>":
   "El curso más nuevo · <b>1.000 palabras ya disponibles</b>",
 "The most regular language you will ever learn the hard way.":
   "La lengua más regular que vas a aprender por las malas.",
 # the sig line the other Spanish course pages already render
 "Listen · read · repeat · rate · fight":
   "Escuchar · Leer · Repetir · Calificar · Luchar",
 "Swahili does not conjugate so much as <b>assemble</b>. A verb is built from slots in a fixed order, and every noun belongs to a class that the rest of the sentence agrees with. Learn those two machines and the vocabulary stops being a list. <b>1,000 words, 40 clusters, 20 reference lessons</b> — with the class named on every noun.":
   "El suajili no conjuga tanto como <b>ensambla</b>. El verbo se arma con casillas en un orden fijo, y cada sustantivo pertenece a una clase con la que concuerda el resto de la oración. Aprende esas dos máquinas y el vocabulario deja de ser una lista. <b>1.000 palabras, 40 clusters, 20 lecciones de referencia</b> — con la clase nombrada en cada sustantivo.",

 # ---- the argument ----
 "Why Swahili is learnable": "Por qué el suajili se puede aprender",
 "A language with no irregular verbs to speak of":
   "Una lengua prácticamente sin verbos irregulares",
 "Swahili is the working language of East Africa — Tanzania, Kenya, Uganda, Rwanda, Burundi and the eastern Congo — and it is spoken by far more people who learned it than by people born to it. That has worn it smooth. Spelling is exactly as it sounds, stress is always the second-to-last syllable, and there is no tone and no grammatical gender.":
   "El suajili es la lengua de trabajo de África Oriental — Tanzania, Kenia, Uganda, Ruanda, Burundi y el este del Congo — y lo hablan muchas más personas que lo aprendieron que personas que nacieron con él. Eso lo fue puliendo. Se escribe exactamente como suena, el acento cae siempre en la penúltima sílaba, y no hay tonos ni género gramatical.",
 "What it has instead is <b>structure you can see</b>. The verb is a train of slots. The noun carries a class, and the class rides through the whole sentence. Neither is hidden, and neither has a list of exceptions waiting for you at intermediate level.":
   "Lo que tiene en cambio es <b>una estructura que se ve</b>. El verbo es un tren de casillas. El sustantivo lleva una clase, y esa clase viaja por toda la oración. Ninguna de las dos está escondida, y ninguna te guarda una lista de excepciones para el nivel intermedio.",
 "This course teaches ordinary Swahili — the language of the market, the school and the news. The frequency backbone it is built from was made for that, not for subtitles.":
   "Este curso enseña suajili corriente — la lengua del mercado, de la escuela y de los noticieros. La columna de frecuencia sobre la que está construido se hizo para eso, no para los subtítulos.",

 # ---- the verb train. The three Swahili sentences are quoted from the pack's
 #      own cards: they stay byte-identical, only the gloss becomes Spanish. ----
 "The verb is an assembly": "El verbo es un ensamblaje",
 "Slots, in a fixed order": "Casillas, en un orden fijo",
 "Three sentences from the pack's own cards, taken apart. The order never changes: who, when, whom, what.":
   "Tres oraciones de las propias tarjetas del paquete, desarmadas. El orden nunca cambia: quién, cuándo, a quién, qué.",
 '<i class="ls"></i> who — the subject': '<i class="ls"></i> quién — el sujeto',
 '<i class="lt"></i> when — the tense': '<i class="lt"></i> cuándo — el tiempo',
 # "a quién" would leave this legend cell starting with a bare "a", which the
 # stranded-article scan reads as an English article; "quién recibe" says the
 # same thing and starts on a word of its own.
 '<i class="lo"></i> whom — the object': '<i class="lo"></i> quién recibe — el objeto',
 '<i class="lr"></i> what — the root': '<i class="lr"></i> qué — la raíz',

 "Baba yangu <b>anaendesha</b> basi la shule kila asubuhi, na mama anaendesha gari. — My father drives the school bus every morning, and my mother drives the car.":
   "Baba yangu <b>anaendesha</b> basi la shule kila asubuhi, na mama anaendesha gari. — Mi papá maneja el autobús escolar cada mañana, y mi mamá maneja el auto.",
 '<span class="m s">a-<i>he / she</i></span>': '<span class="m s">a-<i>él / ella</i></span>',
 '<span class="m t">na-<i>present</i></span>': '<span class="m t">na-<i>presente</i></span>',
 '<span class="m r">endesha<i>drive, make go</i></span>':
   '<span class="m r">endesha<i>manejar, hacer andar</i></span>',
 "Three pieces, read left to right: <b>he · now · drives</b>. The root itself is built — <i>endesha</i> is the causative of <i>kwenda</i>, to go, so it means to make something go.":
   "Tres piezas, leídas de izquierda a derecha: <b>él · ahora · maneja</b>. La raíz misma está construida — <i>endesha</i> es el causativo de <i>kwenda</i>, ir, así que significa hacer que algo ande.",

 "<b>Tulisafiri</b> kwa treni kutoka jijini hadi kijijini kwetu wakati wa likizo. — We travelled by train from the city to our village during the holiday.":
   "<b>Tulisafiri</b> kwa treni kutoka jijini hadi kijijini kwetu wakati wa likizo. — Viajamos en tren de la ciudad a nuestro pueblo durante las vacaciones.",
 '<span class="m s">tu-<i>we</i></span>': '<span class="m s">tu-<i>nosotros</i></span>',
 '<span class="m t">li-<i>past</i></span>': '<span class="m t">li-<i>pasado</i></span>',
 '<span class="m r">safiri<i>travel</i></span>': '<span class="m r">safiri<i>viajar</i></span>',
 "Change one letter in the middle slot and you change the tense. <b>tuna</b>safiri is we are travelling; <b>tuta</b>safiri is we will travel. Nothing else in the word moves.":
   "Cambia una letra en la casilla del medio y cambias el tiempo. <b>tuna</b>safiri es estamos viajando; <b>tuta</b>safiri es viajaremos. Nada más se mueve dentro de la palabra.",

 "Watu wengi <b>walipanda</b> basi hilo kubwa mapema asubuhi ya leo. — Many people boarded that big bus early this morning.":
   "Watu wengi <b>walipanda</b> basi hilo kubwa mapema asubuhi ya leo. — Mucha gente se subió a ese autobús grande temprano esta mañana.",
 '<span class="m s">wa-<i>they, class m/wa</i></span>':
   '<span class="m s">wa-<i>ellos, clase m/wa</i></span>',
 '<span class="m r">panda<i>climb, board, plant</i></span>':
   '<span class="m r">panda<i>subir, abordar, sembrar</i></span>',
 "The subject slot is not just a pronoun: it agrees with the <b>class</b> of the noun. <i>Watu</i> is class m/wa, so the verb starts wa-. That is the second machine.":
   "La casilla del sujeto no es solo un pronombre: concuerda con la <b>clase</b> del sustantivo. <i>Watu</i> es de clase m/wa, así que el verbo empieza con wa-. Esa es la segunda máquina.",
 "The pack drills this directly. One of Swahili's three revision drills is the verb train, built slot by slot — you assemble the form rather than recall it whole.":
   "El paquete lo ejercita directamente. Uno de los tres ejercicios de repaso del suajili es el tren del verbo, construido casilla por casilla — armas la forma en vez de recordarla entera.",

 # ---- noun classes: whole cells, so no English label survives next to a
 #      class name. The class names themselves are Swahili and stay. ----
 "The engine": "El motor",
 "Every noun carries its class": "Cada sustantivo lleva su clase",
 "Swahili has no gender. It has classes — and the class of the noun decides the shape of its plural, its adjectives, its verb and its possessives. Get the class and the agreement comes free.":
   "El suajili no tiene género. Tiene clases — y la clase del sustantivo decide la forma de su plural, de sus adjetivos, de su verbo y de sus posesivos. Acierta la clase y la concordancia viene de regalo.",
 '<div class="k">m/wa</div><div class="v">people — <i>mtu / watu</i></div>':
   '<div class="k">m/wa</div><div class="v">personas — <i>mtu / watu</i></div>',
 '<div class="k">m/mi</div><div class="v">trees, living things, body parts</div>':
   '<div class="k">m/mi</div><div class="v">árboles, seres vivos, partes del cuerpo</div>',
 '<div class="k">ji/ma</div><div class="v">large things, pairs, groups</div>':
   '<div class="k">ji/ma</div><div class="v">cosas grandes, pares, grupos</div>',
 '<div class="k">ki/vi</div><div class="v">objects, tools, languages</div>':
   '<div class="k">ki/vi</div><div class="v">objetos, herramientas, idiomas</div>',
 '<div class="k">n/n</div><div class="v">loans, animals, many abstracts</div>':
   '<div class="k">n/n</div><div class="v">préstamos, animales, muchos abstractos</div>',
 '<div class="k">u/n</div><div class="v">abstract nouns, mass nouns</div>':
   '<div class="k">u/n</div><div class="v">sustantivos abstractos y de materia</div>',
 '<div class="k">u/ma</div><div class="v">long thin things</div>':
   '<div class="k">u/ma</div><div class="v">cosas largas y delgadas</div>',
 '<div class="k">u/u</div><div class="v">a smaller set, no plural shift</div>':
   '<div class="k">u/u</div><div class="v">un grupo más pequeño, sin cambio en el plural</div>',
 '<div class="k">ku</div><div class="v">the infinitive used as a noun</div>':
   '<div class="k">ku</div><div class="v">el infinitivo usado como sustantivo</div>',
 '<div class="k">pa</div><div class="v">place</div>':
   '<div class="k">pa</div><div class="v">lugar</div>',
 "Those are the ten classes this pack actually uses, taken from its cards rather than from a grammar. The class is printed on every single noun in the deck, where another course would leave you to infer it.":
   "Esas son las diez clases que este paquete usa de verdad, sacadas de sus tarjetas y no de una gramática. La clase está impresa en cada uno de los sustantivos del mazo, donde otro curso te dejaría deducirla.",

 # ---- the card. gari and its Swahili example sentence stay. ----
 "What a card holds": "Qué lleva una tarjeta",
 "A real one, from tier 2. The class sits beside the headword; the notes say the thing a dictionary would not.":
   "Una de verdad, del nivel 2. La clase va junto a la palabra principal; las notas dicen lo que un diccionario no diría.",
 '<div class="tr">a car, or any road vehicle</div>':
   '<div class="tr">un auto, o cualquier vehículo de carretera</div>',
 '<div class="exx">Our car has no fuel, so we have stopped near the bridge.</div>':
   '<div class="exx">Nuestro auto no tiene combustible, así que nos detuvimos cerca del puente.</div>',
 "The same card carries its translation, its example translation <b>and</b> its notes in German, Japanese, Russian, Simplified Chinese and Spanish as well as English — full coverage, every card, no gaps.":
   "La misma tarjeta lleva su traducción, la traducción de su oración de ejemplo <b>y</b> sus notas en alemán, japonés, ruso, chino simplificado y español además de inglés — cobertura completa, en cada tarjeta, sin huecos.",

 # ---- method: whole <dt>/<dd> pairs, so no English term is left stranded ----
 "How it sticks": "Cómo se fija",
 "Flashcards as an integrated system": "Las tarjetas como sistema integrado",
 "<dt>Cards</dt><dd><b>1,000 words across 40 clusters</b> and five tiers — greetings and family, the town, work and health, government, the news, and the small words that join sentences together. An example sentence on every card.</dd>":
   "<dt>Tarjetas</dt><dd><b>1.000 palabras en 40 clusters</b> y cinco niveles — saludos y familia, el pueblo, el trabajo y la salud, el gobierno, los noticieros, y las palabras pequeñas que unen las oraciones. Una oración de ejemplo en cada tarjeta.</dd>",
 "<dt>Noun class</dt><dd>Named on <b>every noun</b>, on the card itself: <i>ji/ma</i>, <i>ki/vi</i>, <i>m/wa</i>. The engine the whole language runs on, never left implicit.</dd>":
   "<dt>Clase nominal</dt><dd>Nombrada en <b>cada sustantivo</b>, en la tarjeta misma: <i>ji/ma</i>, <i>ki/vi</i>, <i>m/wa</i>. El motor con el que funciona toda la lengua, nunca dado por supuesto.</dd>",
 "<dt>Your language</dt><dd>Translations and study notes in <b>English, German, Japanese, Russian, Simplified Chinese and Spanish</b> — full coverage on every card. Study Swahili through whichever you call home.</dd>":
   "<dt>Tu idioma</dt><dd>Traducciones y notas de estudio en <b>inglés, alemán, japonés, ruso, chino simplificado y español</b> — cobertura completa en cada tarjeta. Estudia suajili desde el idioma que llames tuyo.</dd>",
 '<dt>Lessons</dt><dd><b>20 reference lessons</b> — the sound system, the noun-class families, the verb slot machine, the Swahili clock, and concord tier by tier. Readable in all six languages, and <a href="lessons.html?lang=Swahili">free to read here</a>.</dd>':
   '<dt>Lecciones</dt><dd><b>20 lecciones de referencia</b> — el sistema de sonidos, las familias de clases nominales, la máquina de casillas del verbo, el reloj suajili, y la concordancia nivel por nivel. Se pueden leer en los seis idiomas, y <a href="lessons.html?lang=Swahili">son gratis aquí</a>.</dd>',
 "<dt>Drills</dt><dd>Three, shaped to Swahili rather than borrowed: the <b>verb train</b> built slot by slot, <b>plurals by noun class</b>, and <b>dictation</b>.</dd>":
   "<dt>Ejercicios</dt><dd>Tres, hechos a la medida del suajili en vez de prestados: el <b>tren del verbo</b> construido casilla por casilla, los <b>plurales por clase nominal</b> y el <b>dictado</b>.</dd>",
 "<dt>Audio</dt><dd>Text-to-speech on every word and every example sentence, in a neural standard Kiswahili voice. Synthesis, not a recording of a speaker.</dd>":
   "<dt>Audio</dt><dd>Texto a voz en cada palabra y en cada oración de ejemplo, con una voz neuronal de kiswahili estándar. Es síntesis, no la grabación de una persona.</dd>",
 "<dt>Fibonacci SRS</dt><dd>Rate each card 0–5. The better you know a word, the longer before it returns.</dd>":
   "<dt>SRS de Fibonacci</dt><dd>Califica cada tarjeta de 0 a 5. Cuanto mejor conoces una palabra, más tarda en volver.</dd>",
 "<dt>Boss fights</dt><dd>No cluster is cleared until its hardest words are answered. Beat it and its cards leave your daily deck for good.</dd>":
   "<dt>Boss fights</dt><dd>Ningún cluster se supera hasta que sus palabras más difíciles quedan respondidas. Véncelo y sus tarjetas dejan tu mazo diario para siempre.</dd>",

 # ---- the three packs. Pack names stay English; no date on the unreleased two. ----
 "Three packs, three thousand words": "Tres paquetes, tres mil palabras",
 "Core is out. The two that follow are written and are not on sale yet; neither carries a date until it is.":
   "Core ya está. Los dos que siguen están escritos y todavía no están a la venta; ninguno lleva fecha hasta que lo esté.",
 '<div class="lvl">Tiers 1–5 · 1,000 words · 20 lessons</div>':
   '<div class="lvl">Niveles 1–5 · 1.000 palabras · 20 lecciones</div>',
 "<p>The foundation: greetings and the family through the town, work and health to government and the news.</p>":
   "<p>El cimiento: de los saludos y la familia al pueblo, el trabajo y la salud, hasta el gobierno y los noticieros.</p>",
 '<span class="here">On Steam</span>': '<span class="here">En Steam</span>',
 '<div class="lvl">Tiers 6–10 · 1,000 words · 14 lessons</div>':
   '<div class="lvl">Niveles 6–10 · 1.000 palabras · 14 lecciones</div>',
 "<p>The working vocabulary: money and the bank, the contract, the ministry, elections, the court, the press, the hospital.</p>":
   "<p>El vocabulario de trabajo: el dinero y el banco, el contrato, el ministerio, las elecciones, el tribunal, la prensa, el hospital.</p>",
 '<span class="soon">Written, not yet out</span>':
   '<span class="soon">Escrito, aún no disponible</span>',
 '<div class="lvl">Tiers 11–15 · 1,000 words · 14 lessons</div>':
   '<div class="lvl">Niveles 11–15 · 1.000 palabras · 14 lecciones</div>',
 "<p>Where derivation opens up — one root becomes six verbs — and the vocabulary follows it into public life and register.</p>":
   "<p>Donde la derivación se abre — una raíz se vuelve seis verbos — y el vocabulario la sigue hacia la vida pública y el registro.</p>",
 "Each pack is 1,000 words and five tiers, and each takes the one before it as read. The end of Pareto 1 is the hump: not finished, but the language has stopped being a wall.":
   "Cada paquete son 1.000 palabras y cinco niveles, y cada uno da por sabido el anterior. El final de Pareto 1 es la cima: no has terminado, pero la lengua ha dejado de ser un muro.",

 # ---- FAQ ----
 "Questions": "Preguntas",
 "Before you buy": "Antes de comprar",
 "<summary>Do I need the base game?</summary>": "<summary>¿Necesito el juego base?</summary>",
 'Yes. Swahili Core is DLC for FlashBoss, so you need the base game as well. Everything else — the lessons, the audio, the drills, the boss fights — is inside the pack. On Windows 10 you also need <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a>, a free download from the Microsoft Store.':
   'Sí. Swahili Core es un DLC de FlashBoss, así que también necesitas el juego base. Todo lo demás — las lecciones, el audio, los ejercicios, los boss fights — va dentro del paquete. En Windows 10 también necesitas <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a>: una descarga gratuita de la Microsoft Store.',
 "<summary>Can I study it in my own language?</summary>":
   "<summary>¿Puedo estudiarlo en mi propio idioma?</summary>",
 "Fully. Every card carries its translation, its example translation and its study notes in <b>German, Japanese, Russian, Simplified Chinese and Spanish</b> as well as English, with no gaps, and all 20 reference lessons carry the same six. The game's own interface speaks them too.":
   "Entero. Cada tarjeta lleva su traducción, la traducción de su oración de ejemplo y sus notas de estudio en <b>alemán, japonés, ruso, chino simplificado y español</b> además de inglés, sin huecos, y las 20 lecciones de referencia llevan esos mismos seis. La interfaz del juego también los habla.",
 "<summary>Which Swahili is this?</summary>": "<summary>¿Qué suajili es este?</summary>",
 "Standard Kiswahili — the one taught in schools and used by the press across East Africa, based on the Zanzibar dialect. The voice is a neural standard Kiswahili voice.":
   "Kiswahili estándar — el que se enseña en las escuelas y usa la prensa en toda África Oriental, basado en el dialecto de Zanzíbar. La voz es una voz neuronal de kiswahili estándar.",
 "<summary>Can I see the words before I buy?</summary>":
   "<summary>¿Puedo ver las palabras antes de comprar?</summary>",
 'All of them. The complete <a href="wordlists.html?lang=Swahili&amp;set=Core">word list</a> and all twenty <a href="lessons.html?lang=Swahili">reference lessons</a> are on this site — free, printable, no account. There is also a <a href="https://flashboss-demo.pages.dev/">playable boss fight</a>.':
   'Todas. El <a href="wordlists.html?lang=Swahili&amp;set=Core">vocabulario</a> completo y las veinte <a href="lessons.html?lang=Swahili">lecciones de referencia</a> están en este sitio — gratis, imprimibles, sin cuenta. También hay un <a href="https://flashboss-demo.pages.dev/">boss fight jugable</a>.',
 "<summary>Is there a British or American spelling layer?</summary>":
   "<summary>¿Hay una capa de ortografía británica o estadounidense?</summary>",
 "That layer covers the English packs. Swahili's English is the translation side of the card, and the pack ships one edition of it.":
   "Esa capa es de los paquetes de inglés. El inglés del suajili es el lado de traducción de la tarjeta, y el paquete trae una sola versión.",

 # ---- final ----
 "Start with <i>Habari?</i>": "Empieza con <i>Habari?</i>",
 "Two machines and a thousand words. The rest of Swahili agrees with them.":
   "Dos máquinas y mil palabras. Todo el resto del suajili concuerda con ellas.",
 "Swahili Core on Steam &rarr;": "Swahili Core en Steam &rarr;",
}

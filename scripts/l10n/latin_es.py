# Spanish (Latin America) strings for latin.html — the Latin LANGUAGE COURSE
# page (Latin Core + Latin Pareto), not the Latin Roots English pack.
#
# Canon sentences are LIFTED from the ratified sources wherever they have them:
# the Spanish half of the Latin bundle sheet
# (flashboss-admin/BUNDLE_COPY_LATIN_2026-09-08.md) gives the bundle name
# "FlashBoss Latín — El curso completo", "niveles 1–10" for the tiers, "oración
# de ejemplo", "tarjetas" and "notas de estudio"; french.es.html is the same
# page template already translated by the fleet, so its wording owns the shared
# furniture — "Escuchar · Leer · Repetir · Calificar · Luchar", the hero alt,
# "SRS de Fibonacci", "Graduación", "Tu idioma", "Preguntas", "Lo que la gente
# pregunta antes de comprar.", the Windows-Terminal answer and the demo answer.
# swahili.es.html (the sibling built in this same batch) gives "Cómo se fija",
# "Las tarjetas como sistema integrado" and "Niveles 1–5"; the live Spanish
# pages give "toca para girar" (33 hits) and "página de vocabulario" /
# "página de lecciones".
#
# THE CLUSTER NAMES ARE NOT MINE. Every one of the eighty comes from
# clusters_latin_es.txt — the strings the game itself ships for this locale.
# They drop the English "&" for "y", because that is how the game writes them.
#
# Pack names stay English: Latin Core, Latin Pareto, Core, Pareto. FlashBoss
# stays Latin script. "Latin Pareto" is the store name — never "Pareto 1".
# The Latin itself is never translated: the example sentences, the dictionary
# forms (virtūs, f., -is), the sigla (Caes. BG 5.44.5) and the epigraph stay
# byte-identical; only the gloss around them becomes Spanish.
# Numbers are the English page's own, in Spanish separators; the page was
# recounted from the packs on 2026-09-19 and beats the bundle sheet where they
# disagree — Core 26 reference lessons, Pareto 18, 44 in all.
# Terms: tier -> nivel (the ratified sheet's own word, and swahili.es.html's),
# cluster -> cluster, boss fight -> boss fight, card -> tarjeta, headword ->
# palabra principal, reference lesson -> lección de referencia, citation ->
# referencia, macron -> macrón. Register: tú, Latin American vocabulary.
TITLE = "Latín — FlashBoss"
DESCRIPTION = ("FlashBoss Latín: un curso de lectura de 2.000 palabras en diez niveles y ochenta "
               "clusters, con 44 lecciones de referencia, palabras principales con macrón y "
               "oraciones de ejemplo que terminan en César, Cicerón, Salustio, Nepote y Livio sin "
               "adaptar. Latin Core y Latin Pareto, ya en Steam.")

STRINGS = {
 # ---- nav / chrome ----
 ">home<": ">inicio<",
 ">packs<": ">paquetes<",
 ">resources<": ">recursos<",
 ">walkthrough (beta)<": ">guía completa (beta)<",
 '<span class="here">Latin</span>': '<span class="here">latín</span>',

 # ---- hero ----
 "FlashBoss — the moonlit school that fronts every FlashBoss course":
   "FlashBoss — la escuela a la luz de la luna que abre todos los cursos de FlashBoss",
 "Two packs · <b>2,000 words</b> · ten tiers · 44 lessons · out now on Steam":
   "Dos paquetes · <b>2.000 palabras</b> · diez niveles · 44 lecciones · ya en Steam",
 "Read real Latin. Not books about it.": "Lee latín de verdad. No libros sobre el latín.",
 "Listen · Read · Repeat · Rate · Fight": "Escuchar · Leer · Repetir · Calificar · Luchar",
 "Two thousand words, ten tiers, one skill. The sentences start built for you and end as <b>Caesar, Cicero, Sallust, Nepos and Livy actually wrote them</b> — nothing trimmed but length, nothing invented.":
   "Dos mil palabras, diez niveles, una sola destreza. Las oraciones empiezan construidas para ti y terminan tal como <b>las escribieron de verdad César, Cicerón, Salustio, Nepote y Livio</b> — no se recortó más que la extensión, no se inventó nada.",
 ">Word Lists<": ">Vocabulario<",
 ">Lessons<": ">Lecciones<",
 ">Try the demo<": ">Probar demo<",

 # ---- the argument: one skill, and the order that teaches it ----
 "Latin course design": "Cómo está hecho el curso de latín",
 "One skill: reading": "Una sola destreza: leer",
 "Legendō discitur — it is learned by reading.":
   "Legendō discitur — se aprende leyendo.",
 "Nothing here asks you to compose Latin of your own. The whole course is built so that you can look at a printed line and know what it says — and it gets you there by putting you in front of sentences from the very first tier, not by making you wait until the grammar is finished.":
   "Aquí nada te pide componer latín propio. Todo el curso está hecho para que puedas mirar una línea impresa y saber qué dice — y te lleva hasta ahí poniéndote oraciones delante desde el primer nivel, no haciéndote esperar a que la gramática esté completa.",
 "The order is the argument. Two thousand lemmas are laid down in ten tiers, each tier eight clusters of twenty-five cards, and the grammar arrives one lesson at a time at the exact card that first needs it. No example sentence ever uses grammar you have not been taught. By Tier 10 the ladder has nothing left to teach and you are reading Cicero unadapted — <b>17,007 words of Latin read in context</b> along the way.":
   "El orden es el argumento. Dos mil lemas quedan asentados en diez niveles, cada nivel con ocho clusters de veinticinco tarjetas, y la gramática llega de a una lección por vez, justo en la tarjeta que primero la necesita. Ninguna oración de ejemplo usa gramática que no te hayan enseñado. En el nivel 10 la escalera ya no tiene nada que enseñar y estás leyendo a Cicerón sin adaptar — <b>17.007 palabras de latín leídas en contexto</b> por el camino.",

 "Latin Core — tiers 1 to 5": "Latin Core — niveles 1 a 5",
 "Latin Pareto — tiers 6 to 10": "Latin Pareto — niveles 6 a 10",
 "The alphabet as Rome said it, the pointing words, the connectives, the prime movers, the first nouns of senate and sword.":
   "El alfabeto como lo decía Roma, las palabras que señalan, los enlaces, los motores primeros, los primeros sustantivos de senado y espada.",
 "The accusative, the present tense, the imperative. The daily round, the forum, the body, counting and worth.":
   "El acusativo, el presente, el imperativo. La ronda diaria, el foro, el cuerpo, la cuenta y el valor.",
 "Genitive and dative, the full plural, two more conjugations, the imperfect. The road, the household, the turning year.":
   "Genitivo y dativo, el plural completo, dos conjugaciones más, el imperfecto. El camino, la casa, el año que gira.",
 "The ablative, the third declension, prepositions and case — and the first real Caesar, lightly adapted.":
   "El ablativo, la tercera declinación, preposiciones y caso — y el primer César de verdad, ligeramente adaptado.",
 "The perfect and its family, principal parts, relative clauses. Caesar is now on 86 of the 200 cards, and unadapted on 26 of them.":
   "El perfecto y su familia, las partes principales, las oraciones de relativo. César está ya en 86 de las 200 tarjetas, y sin adaptar en 26 de ellas.",
 "Participles, all three of them, and the passive. Caesar continues, and Nepos comes into his own.":
   "Los participios, los tres, y la voz pasiva. César sigue, y Nepote pasa al primer plano.",
 "The ablative absolute, the passive complete, deponents. Cicero's letters open the informal register.":
   "El ablativo absoluto, la pasiva completa, los deponentes. Las cartas de Cicerón abren el registro informal.",
 "The infinitive family and reported speech. Sallust arrives; 192 of 200 cards are now unadapted.":
   "La familia del infinitivo y el estilo indirecto. Llega Salustio; 192 de 200 tarjetas ya están sin adaptar.",
 "The subjunctive, cum-clauses, purpose and result, indirect questions. Livy joins the roll.":
   "El subjuntivo, las oraciones con cum, las finales y las consecutivas, las interrogativas indirectas. Livio entra en la lista.",
 "Gerund and gerundive, and how to read a citation. Cicero's speeches and philosophy close the trunk.":
   "Gerundio y gerundivo, y cómo se lee una referencia. Los discursos y la filosofía de Cicerón cierran el tronco.",

 # ---- the sentence ladder: Latin stays Latin, the gloss becomes Spanish ----
 "Watch it grow up": "Mira cómo crece",
 "From made for you to written by Cicero": "De hecho para ti a escrito por Cicerón",
 "One card's example sentence from each of the ten tiers, in order. Nothing below is a paraphrase: from Tier 4 the citations are real, and the unmarked ones are the author's own words.":
   "La oración de ejemplo de una tarjeta de cada uno de los diez niveles, en orden. Nada de lo que sigue es una paráfrasis: desde el nivel 4 las referencias son reales, y las que no llevan marca son las palabras del propio autor.",
 "<span class=\"en\">As you see, Caesar is one of ours.</span>":
   "<span class=\"en\">Como ves, César es de los nuestros.</span>",
 "<span class=\"en\">While Caesar is in Gaul, the senate approves the law.</span>":
   "<span class=\"en\">Mientras César está en la Galia, el senado aprueba la ley.</span>",
 "<span class=\"en\">Our troops were already departing and abandoning the camp.</span>":
   "<span class=\"en\">Nuestras tropas ya se retiraban y abandonaban el campamento.</span>",
 "<span class=\"en\">The storms both kept our men in camp and held the enemy back from battle.</span>":
   "<span class=\"en\">Las tormentas retenían a los nuestros en el campamento y a la vez mantenían al enemigo lejos del combate.</span>",
 "<span class=\"en\">There he reached the furthest ridge and drew up his line in that place.</span>":
   "<span class=\"en\">Allí llegó a la cresta más lejana y formó su línea de batalla en ese mismo lugar.</span>",
 "<span class=\"en\">Not even Vorenus keeps himself behind the rampart then; fearing what everyone would think, he follows after.</span>":
   "<span class=\"en\">Ni siquiera Voreno se queda entonces detrás del terraplén; por miedo a lo que todos pensaran, sale tras él.</span>",
 "<span class=\"en\">All the ties of the closest friendship hold between him and me.</span>":
   "<span class=\"en\">Entre él y yo median todos los lazos de la amistad más estrecha.</span>",
 "<span class=\"en\">At home we have want, abroad debt, a bad case and a prospect much harsher still.</span>":
   "<span class=\"en\">En casa tenemos carencia, fuera deudas, una mala causa y un porvenir mucho más duro todavía.</span>",
 "<span class=\"en\">Seeing his forces routed and himself left with a few, mindful of his birth and former standing, Catiline charges into the thickest of the enemy and there, fighting, is run through.</span>":
   "<span class=\"en\">Al ver desbaratadas sus tropas y que él mismo quedaba con unos pocos, consciente de su linaje y de su antigua dignidad, Catilina carga contra lo más denso del enemigo y allí, peleando, cae atravesado.</span>",
 "<span class=\"en\">You see that man with the rather curly hair, the dark one, who watches us with a look that makes him seem very sharp to himself.</span>":
   "<span class=\"en\">Ven a ese de pelo algo rizado, el moreno, que nos observa con una cara que a sus propios ojos lo vuelve agudísimo.</span>",
 ">built for the tier<": ">construida para el nivel<",
 ">adapted from Caes. BG 4.34.4<": ">adaptada de Caes. BG 4.34.4<",

 # ---- whose Latin: the source arc ----
 "Whose Latin": "De quién es este latín",
 "The authors arrive in order": "Los autores llegan en orden",
 "Tiers 1 to 3 have no citations at all, and say so: those sentences are built to a grammar ceiling, because real Latin has no register that simple. Caesar enters at Tier 4 and the scaffolding is gone by Tier 8.":
   "Los niveles 1 a 3 no llevan ninguna referencia, y lo dicen: esas oraciones están construidas hasta un tope de gramática, porque el latín real no tiene un registro tan simple. César entra en el nivel 4, y para el nivel 8 el andamiaje ya no está.",
 ">Tiers 1–3<": ">Niveles 1–3<",
 "Sentences constructed to the tier's grammar — no author claimed, none implied":
   "Oraciones construidas según la gramática del nivel — no se atribuye ningún autor, ni se insinúa",
 ">0 of 600 cited<": ">0 de 600 con referencia<",
 "Caesar, <i>Gallic War</i> — mostly clause-trimmed for length":
   "César, <i>Guerra de las Galias</i> — casi siempre podado de alguna subordinada por extensión",
 ">62 cited · 13 unadapted<": ">62 con referencia · 13 sin adaptar<",
 "Caesar throughout, Nepos beginning": "César en todo el nivel, Nepote empezando",
 ">86 cited · 26 unadapted<": ">86 con referencia · 26 sin adaptar<",
 "Caesar and Nepos, <i>Lives</i>": "César y Nepote, <i>Vidas</i>",
 ">145 cited · 84 unadapted<": ">145 con referencia · 84 sin adaptar<",
 "Cicero's letters — <i>ad Atticum</i>, <i>ad Familiares</i> — beside Caesar and Nepos":
   "Las cartas de Cicerón — <i>ad Atticum</i>, <i>ad Familiares</i> — junto a César y Nepote",
 ">170 cited · 109 unadapted<": ">170 con referencia · 109 sin adaptar<",
 "Sallust joins; the adapting effectively stops":
   "Se suma Salustio; la adaptación prácticamente se detiene",
 ">196 cited · 192 unadapted<": ">196 con referencia · 192 sin adaptar<",
 "Livy Book 1 joins Sallust, Cicero and Caesar":
   "El libro 1 de Livio se suma a Salustio, Cicerón y César",
 ">197 cited · 195 unadapted<": ">197 con referencia · 195 sin adaptar<",
 "Cicero's speeches and philosophy — the hardest band the trunk reaches":
   "Los discursos y la filosofía de Cicerón — la franja más difícil a la que llega el tronco",
 ">196 cited · 194 unadapted<": ">196 con referencia · 194 sin adaptar<",
 "Across the two packs, <b>1,052 of the 2,000 example sentences carry a citation</b>, and 813 of those are the author's own unaltered words. Every citation on every card names its book, chapter and section, and Lesson 41 teaches you how to read one.":
   "En los dos paquetes, <b>1.052 de las 2.000 oraciones de ejemplo llevan una referencia</b>, y 813 de ellas son las palabras del autor sin alterar. Cada referencia de cada tarjeta nombra su libro, su capítulo y su sección, y la lección 41 te enseña a leerla.",

 # ---- the tier and cluster ledger; the eighty names are the game's own,
 #      straight from clusters_latin_es.txt, "y" where English writes "&" ----
 "The whole map": "El mapa completo",
 "Ten tiers, eighty clusters": "Diez niveles, ochenta clusters",
 "Every cluster is 25 cards and ends in a boss fight. Nothing is hidden — the full list is on the <a href=\"wordlists.html?lang=Latin&amp;set=Core\">word lists page</a>, free to read before you buy.":
   "Cada cluster son 25 tarjetas y termina en un boss fight. Nada está escondido — la lista completa está en la <a href=\"wordlists.html?lang=Latin&amp;set=Core\">página de vocabulario</a>, gratis para leer antes de comprar.",
 ">Tier 1<": ">Nivel 1<",
 ">Tier 2<": ">Nivel 2<",
 ">Tier 3<": ">Nivel 3<",
 ">Tier 4<": ">Nivel 4<",
 ">Tier 5<": ">Nivel 5<",
 ">Tier 6<": ">Nivel 6<",
 ">Tier 7<": ">Nivel 7<",
 ">Tier 8<": ">Nivel 8<",
 ">Tier 9<": ">Nivel 9<",
 ">Tier 10<": ">Nivel 10<",
 "The Pointing Words · The Joints · The Links · The Prime Movers · Senate &amp; Sword · Many &amp; Mighty · The Lay of Things · The Marshalling":
   "Las palabras que señalan · Las junturas · Los enlaces · Los motores primeros · Senado y espada · Muchos y poderosos · El estado de las cosas · El despliegue",
 "The Daily Round · Arms &amp; the Man · The Forum · Flesh &amp; Breath · Tally &amp; Measure · Worth &amp; Honor · Time &amp; Tide · The Rally":
   "La ronda diaria · Las armas y el hombre · El foro · Carne y aliento · Cuenta y medida · Valor y honor · Tiempo y marea · La reagrupación",
 "To &amp; Fro · The Long Road · Flesh &amp; Frame · The Fathers · House &amp; Hearth · Hopes &amp; Fears · The Turning Year · The Waystation":
   "De aquí para allá · El largo camino · Carne y armazón · Los padres · Casa y hogar · Esperanzas y miedos · El año que gira · La posta",
 "Moods &amp; Moments · The Turning Hand · The Living Frame · The Curia · By Land &amp; Sea · More &amp; Most · The Winter Camp · The Muster Roll":
   "Ánimos y momentos · La mano que gira · El cuerpo vivo · La curia · Por tierra y mar · Más y lo más · El campamento de invierno · El rol de leva",
 "What Was Done · The Perfect Stems · The Pitched Battle · The Work in Hand · Life &amp; Limb · Praise &amp; Blame · The Appointed Hour · The Full Account":
   "Lo que se hizo · Los temas de perfecto · La batalla campal · La obra en curso · Vida y miembro · Elogio y reproche · La hora señalada · La cuenta completa",
 "The Life of the Mind · Hours &amp; Days · A Soldier&#x27;s Life · The Full Tally · The Family Estate · The Mortal Frame · Treaties &amp; Powers · The Loose Ends":
   "La vida de la mente · Horas y días · Vida de soldado · El recuento total · La hacienda familiar · El cuerpo mortal · Tratados y potencias · Los cabos sueltos",
 "Comings &amp; Partings · The Ready Hand · The Head Count · Wounds &amp; Toil · Kin &amp; Neighbor · Rank &amp; Office · The Sea Road · The Middle Way":
   "Llegadas y despedidas · La mano presta · El recuento de cabezas · Heridas y fatigas · Parientes y vecinos · Rango y magistratura · El camino del mar · La vía media",
 "True &amp; False · The Bidding · Sound &amp; Sick · Weight &amp; Worth · The Present Hour · The Tide of Battle · The Household Store · The Last Ditch":
   "Verdadero y falso · El mandato · Sano y enfermo · Peso y valor · La hora presente · La marea de la batalla · El caudal de la casa · La última trinchera",
 "Hopes &amp; Vows · By the Numbers · Right &amp; Wrong · The Broken Line · Dust &amp; Ashes · The Sacred Rites · Fraud &amp; Force · What Remains":
   "Esperanzas y votos · Según los números · Lo justo y lo injusto · La línea quebrada · Polvo y ceniza · Los ritos sagrados · Fraude y fuerza · Lo que queda",
 "The Open Book · The Final Battle · Blood &amp; Bone · Honor &amp; Shame · Envoys &amp; Treaties · Hearth &amp; Heir · The Last Measure · The Closing Page":
   "El libro abierto · La batalla final · Sangre y hueso · Honor y vergüenza · Enviados y tratados · Hogar y heredero · La última medida · La página final",
 ">8 clusters · 200 cards<": ">8 clusters · 200 tarjetas<",
 "<span>Core: 5 tiers · 40 clusters · <b>1,000 cards</b></span><span>26 reference lessons</span><span>the reading foundation</span>":
   "<span>Core: 5 niveles · 40 clusters · <b>1.000 tarjetas</b></span><span>26 lecciones de referencia</span><span>la base para leer</span>",
 "<span>Pareto: 5 tiers · 40 clusters · <b>1,000 cards</b></span><span>18 reference lessons</span><span>the trunk complete</span>":
   "<span>Pareto: 5 niveles · 40 clusters · <b>1.000 tarjetas</b></span><span>18 lecciones de referencia</span><span>el tronco completo</span>",

 # ---- the card: the macron ----
 "Read it by sight": "Leerlo de un vistazo",
 "The macron is data, not decoration": "El macrón es información, no adorno",
 "Every headword is printed as a dictionary prints it — long vowels marked, gender and genitive stem for a noun, conjugation for a verb. 1,320 of the 2,000 headwords carry a macron. Tap a card to flip it.":
   "Cada palabra principal está impresa como la imprime un diccionario — vocales largas marcadas, género y tema de genitivo en el sustantivo, conjugación en el verbo. 1.320 de las 2.000 palabras principales llevan macrón. Toca una tarjeta para girarla.",
 # the genitive shorthand is the dictionary form; it stays exactly as printed
 ">f., -is<": ">f., -is<",
 '''courage, manliness; virtue — &ldquo;Roman courage is great.&rdquo;<span class="nb">noun | gen sg virtūtis — the stem is virtūt-
long ū: vir-tūs
From vir &lsquo;man&rsquo;: the quality of a man.</span>''':
   '''valor, hombría; virtud — &ldquo;El valor romano es grande.&rdquo;<span class="nb">sustantivo | gen. sg. virtūtis — el tema es virtūt-
ū larga: vir-tūs
De vir &lsquo;varón&rsquo;: la cualidad del varón.</span>''',
 '''make, do — &ldquo;We are doing the same thing.&rdquo;<span class="nb">verb | 1st pl facimus = &lsquo;we make, we do&rsquo;
long ō: fa-ci-ō; a and i stay short
idem = &lsquo;the same thing&rsquo; (object role)</span>''':
   '''hacer — &ldquo;Hacemos lo mismo.&rdquo;<span class="nb">verbo | 1.ª pl. facimus = &lsquo;hacemos&rsquo;
ō larga: fa-ci-ō; la a y la i quedan breves
idem = &lsquo;lo mismo&rsquo; (función de objeto)</span>''',
 '''evil, misfortune — &ldquo;The state sees the shared misfortune.&rdquo;<span class="nb">noun | acc sg malum = nom sg in form
no macron: ma-lum, both vowels short
mālum, with a long ā, is an apple.</span>''':
   '''mal, desgracia — &ldquo;La ciudad ve la desgracia común.&rdquo;<span class="nb">sustantivo | ac. sg. malum = nom. sg. por la forma
sin macrón: ma-lum, las dos vocales breves
mālum, con ā larga, es una manzana.</span>''',
 ">tap to flip<": ">toca para girar<",

 # ---- the two minimal pairs ----
 ">Tier 1 · Tier 3<": ">Nivel 1 · Nivel 3<",
 ">Tier 10 · Tier 4<": ">Nivel 10 · Nivel 4<",
 "<b>this one</b> against <b>here</b>. One letter apart in print, and the line over the vowel is the only thing that separates them.":
   "<b>este</b> frente a <b>aquí</b>. En letra impresa las separa un solo trazo, y esa raya sobre la vocal es lo único que las distingue.",
 "<b>bone</b> against <b>mouth</b>. Same three letters, same neuter third declension, six tiers apart — and the card that teaches the second one says so.":
   "<b>hueso</b> frente a <b>boca</b>. Las mismas tres letras, la misma tercera declinación neutra, seis niveles de distancia — y la tarjeta que enseña la segunda lo dice.",
 "The macrons stop at the headword. Example sentences are printed unmarked, the way every real Latin text you will ever open is printed — so what you practise reading is the thing itself, not a teaching aid. The card tells you the vowel length; the sentence makes you carry it.":
   "Los macrones se detienen en la palabra principal. Las oraciones de ejemplo van impresas sin marcas, igual que se imprime cualquier texto latino real que vayas a abrir — así lo que practicas leyendo es la cosa misma y no una ayuda didáctica. La tarjeta te dice la cantidad de la vocal; la oración te obliga a llevarla puesta.",

 # ---- reference lessons ----
 "Not just a word list": "Más que una lista de palabras",
 "Forty-four lessons, fired in sequence": "Cuarenta y cuatro lecciones, disparadas en secuencia",
 "A reference lesson unlocks at the exact card where you first need it, and stays available afterwards. Core's twenty-six and Pareto's eighteen are all free to read on the <a href=\"lessons.html?lang=Latin\">lessons page</a>.":
   "Una lección de referencia se desbloquea justo en la tarjeta donde la necesitas por primera vez, y después queda disponible. Las veintiséis de Core y las dieciocho de Pareto se pueden leer gratis en la <a href=\"lessons.html?lang=Latin\">página de lecciones</a>.",

 # whole <li> each, so no English article is stranded in front of a Spanish noun
 "<li><span class=\"no\">01</span>Welcome to Latin<span class=\"d\">The four letters an English reader gets wrong — c, g, v, qu — in the restored sounds, and what a macron is for.</span></li>":
   "<li><span class=\"no\">01</span>Bienvenida al latín<span class=\"d\">Las cuatro letras que un lector de inglés pronuncia mal — c, g, v, qu — en los sonidos restituidos, y para qué sirve un macrón.</span></li>",
 "<li><span class=\"no\">10</span>The accusative<span class=\"d\">The first case that changes what a sentence means, met on the card that first needs it.</span></li>":
   "<li><span class=\"no\">10</span>El acusativo<span class=\"d\">El primer caso que cambia lo que significa una oración, encontrado en la tarjeta que primero lo necesita.</span></li>",
 "<li><span class=\"no\">14</span>Genitive and dative<span class=\"d\">Of and to, and why the genitive singular is printed on every noun card.</span></li>":
   "<li><span class=\"no\">14</span>Genitivo y dativo<span class=\"d\">El «de» y el «a», y por qué el genitivo singular va impreso en cada tarjeta de sustantivo.</span></li>",
 "<li><span class=\"no\">18</span>The ablative<span class=\"d\">The case English has no name for, and the six jobs it does.</span></li>":
   "<li><span class=\"no\">18</span>El ablativo<span class=\"d\">El caso que el inglés no sabe nombrar, y los seis trabajos que hace.</span></li>",
 "<li><span class=\"no\">23</span>Principal parts<span class=\"d\">Why a Latin verb is quoted four ways, and how to get from any of them to the rest.</span></li>":
   "<li><span class=\"no\">23</span>Las partes principales<span class=\"d\">Por qué un verbo latino se enuncia de cuatro maneras, y cómo pasar desde cualquiera de ellas a las demás.</span></li>",
 "<li><span class=\"no\">30</span>The ablative absolute<span class=\"d\">The construction that makes Caesar readable at speed.</span></li>":
   "<li><span class=\"no\">30</span>El ablativo absoluto<span class=\"d\">La construcción que vuelve a César legible a velocidad.</span></li>",
 "<li><span class=\"no\">34</span>Reported speech<span class=\"d\">Accusative and infinitive: how a Roman writes &lsquo;he said that&hellip;&rsquo;.</span></li>":
   "<li><span class=\"no\">34</span>El estilo indirecto<span class=\"d\">Acusativo con infinitivo: cómo escribe un romano &lsquo;dijo que&hellip;&rsquo;.</span></li>",
 "<li><span class=\"no\">41</span>Reading the citation<span class=\"d\">What <i>Caes. BG 5.44.5</i> means, and how to go and find the rest of the page.</span></li>":
   "<li><span class=\"no\">41</span>Leer la referencia<span class=\"d\">Qué significa <i>Caes. BG 5.44.5</i>, y cómo ir a buscar el resto de la página.</span></li>",

 "Also inside: i acting as y, ch and ae/oe, the connectives, the prime movers, the present tense, the imperative, the sound system, the full plural, two more conjugations, the imperfect, the third declension, prepositions and case, the perfect and its family, relative clauses, connectives at speed, all three participles and their two jobs, the passive twice over, deponents, the infinitive family, the subjunctive mood, cum-clauses, purpose and result, indirect questions, the gerund, the gerundive — and a closing lesson on where to go next.":
   "También adentro: la i en función consonántica, ch y ae/oe, los enlaces, los motores primeros, el presente, el imperativo, el sistema de sonidos, el plural completo, dos conjugaciones más, el imperfecto, la tercera declinación, preposiciones y caso, el perfecto y su familia, las oraciones de relativo, los enlaces a velocidad, los tres participios y sus dos trabajos, la pasiva dos veces, los deponentes, la familia del infinitivo, el modo subjuntivo, las oraciones con cum, las finales y las consecutivas, las interrogativas indirectas, el gerundio, el gerundivo — y una lección de cierre sobre adónde ir después.",

 # ---- the two packs, and the fork past them ----
 "Two packs to literacy": "Dos paquetes hasta saber leer",
 "Latin is a trunk, not a staircase of three. Core and Pareto together are the whole 2,000-word reading course, grammar-complete at the end of it.":
   "El latín es un tronco, no una escalera de tres tramos. Core y Pareto juntos son el curso de lectura entero de 2.000 palabras, con la gramática terminada al final.",
 ">Tiers 1–5 · 1,000 words · 26 lessons<": ">Niveles 1–5 · 1.000 palabras · 26 lecciones<",
 "The reading foundation. Sentences built to the tier at first, real Caesar by the end. Requires the base game.":
   "La base para leer. Al principio oraciones construidas para el nivel, César de verdad al final. Requiere el juego base.",
 ">Tiers 6–10 · 1,000 words · 18 lessons<": ">Niveles 6–10 · 1.000 palabras · 18 lecciones<",
 "The second thousand, and the end of the scaffolding: Nepos, Cicero's letters, Sallust, Livy, Cicero's speeches. Requires Core.":
   "El segundo millar, y el final del andamiaje: Nepote, las cartas de Cicerón, Salustio, Livio, los discursos de Cicerón. Requiere Core.",
 ">On Steam<": ">En Steam<",

 "Then choose your third thousand": "Después elige tu tercer millar",
 "Basic literacy is the fork, not the finish. The trunk stops at 2,000 words on purpose: past that, Latin genuinely divides, and which 1,000 words come next depends on what you want to read. Neither branch is built yet.":
   "Saber leer lo básico es la bifurcación, no la meta. El tronco se detiene en 2.000 palabras a propósito: más allá, el latín se divide de verdad, y qué 1.000 palabras vienen después depende de lo que quieras leer. Ninguna de las dos ramas está construida todavía.",
 ">Classical Poetry<": ">Poesía clásica<",
 ">Vergil · Ovid · Catullus · Horace<": ">Virgilio · Ovidio · Catulo · Horacio<",
 "Verse word order, metre, and the vocabulary that only ever shows up in poets. The trunk's prose ladder is the prerequisite, not a substitute.":
   "El orden de palabras del verso, la métrica y el vocabulario que solo aparece en los poetas. La escalera de prosa del tronco es el requisito previo, no un sustituto.",
 ">planned · not yet built<": ">planeado · aún no construido<",
 ">Ecclesiastical Latin<": ">Latín eclesiástico<",
 ">the Vulgate · the hymns · the liturgy<": ">la Vulgata · los himnos · la liturgia<",
 "Church Latin is its own register — different syntax, different vocabulary, and its own pronunciation, which is why it is a branch and not a chapter of the trunk.":
   "El latín de la Iglesia es un registro propio — otra sintaxis, otro vocabulario y su propia pronunciación; por eso es una rama y no un capítulo del tronco.",
 "Both branches take Core and Pareto as their entry requirement. Neither has a date; both are inventoried and reserved rather than promised.":
   "Las dos ramas piden Core y Pareto como requisito de entrada. Ninguna tiene fecha; las dos están inventariadas y reservadas, no prometidas.",

 # ---- method ----
 "How it sticks": "Cómo se fija",
 "Flashcards as an integrated system": "Las tarjetas como sistema integrado",
 "<dt>Fibonacci SRS</dt>": "<dt>SRS de Fibonacci</dt>",
 "Rate each card 0–5. The better you know a word, the longer before it returns — spaced repetition on Fibonacci intervals.":
   "Califica cada tarjeta de 0 a 5. Cuanto mejor conoces una palabra, más tarda en volver — repetición espaciada en intervalos de Fibonacci.",
 # "boss fight" is the Spanish site's own term, so the heading stays as it is
 "<dt>Boss fights</dt>": "<dt>Boss fights</dt>",
 "Each of the 80 clusters is gated by a duel you can't win without confronting and overcoming your most difficult words.":
   "Cada uno de los 80 clusters está protegido por un duelo que no puedes ganar sin enfrentarte a tus palabras más difíciles y superarlas.",
 "<dt>Graduation</dt>": "<dt>Graduación</dt>",
 "Beat a cluster and its cards leave your daily deck for good. The deck gets smaller as you learn.":
   "Vence un cluster y sus tarjetas dejan tu mazo diario para siempre. El mazo se hace más pequeño a medida que aprendes.",
 "<dt>Audio</dt>": "<dt>Audio</dt>",
 "A Latin neural voice on every headword and every example sentence — <i>la_LA-flashboss_m</i>, fine-tuned for FlashBoss and released CC0, reading Classical (restored) pronunciation and honouring the macrons as real vowel length. It is synthesis, not a recording of a speaker.":
   "Una voz neuronal latina en cada palabra principal y en cada oración de ejemplo — <i>la_LA-flashboss_m</i>, ajustada para FlashBoss y publicada como CC0, que lee la pronunciación clásica (restituida) y respeta los macrones como cantidad vocálica real. Es voz sintetizada, no la grabación de una persona.",
 "<dt>Your language</dt>": "<dt>Tu idioma</dt>",
 "All 2,000 cards carry their translation, their example translation <i>and</i> their notes in <b>German, Spanish, Japanese, Russian and Simplified Chinese</b> as well as English — 30,000 fields, with no gaps. All 44 reference lessons carry the same five, and so does the game's interface. Latin is fully playable without a word of English.":
   "Las 2.000 tarjetas llevan su traducción, la traducción del ejemplo <i>y</i> sus notas en <b>alemán, español, japonés, ruso y chino simplificado</b> además de inglés — 30.000 campos, sin huecos. Las 44 lecciones de referencia llevan esos mismos cinco idiomas, y la interfaz del juego también. El latín se juega entero sin una palabra de inglés.",
 "<dt>Macrons</dt>": "<dt>Macrones</dt>",
 "Long vowels marked on 1,320 of the 2,000 headwords, left off the sentences — dictionary convention where it teaches, print convention where you read.":
   "Vocales largas marcadas en 1.320 de las 2.000 palabras principales y no en las oraciones — convención de diccionario donde enseña, convención de imprenta donde lees.",
 "<dt>Real sources</dt>": "<dt>Fuentes reales</dt>",
 "1,052 example sentences cite the book, chapter and section they came from; 813 are unaltered. Everything is drawn from public-domain editions.":
   "1.052 oraciones de ejemplo citan el libro, el capítulo y la sección de los que salieron; 813 están sin alterar. Todo sale de ediciones de dominio público.",
 "Forty-four reference lessons across the two packs fire at the point in the sequence where they unlock what you are about to read.":
   "Cuarenta y cuatro lecciones de referencia repartidas entre los dos paquetes aparecen en el punto de la secuencia donde desbloquean lo que estás a punto de leer.",

 # ---- FAQ ----
 ">Questions<": ">Preguntas<",
 "The things people ask before they buy.": "Lo que la gente pregunta antes de comprar.",

 ">Where do I buy it?<": ">¿Dónde lo compro?<",
 """Both packs are on Steam now: <a href="https://store.steampowered.com/app/5063240/?utm_source=website-latin-faq" target="_blank" rel="noopener">Latin Core</a> and <a href="https://store.steampowered.com/app/5063250/?utm_source=website-latin-faq" target="_blank" rel="noopener">Latin Pareto</a>. Both word lists and all forty-four lessons are readable here, free, if you want to judge the course before you buy either one.""":
   """Los dos paquetes ya están en Steam: <a href="https://store.steampowered.com/app/5063240/?utm_source=website-latin-faq" target="_blank" rel="noopener">Latin Core</a> y <a href="https://store.steampowered.com/app/5063250/?utm_source=website-latin-faq" target="_blank" rel="noopener">Latin Pareto</a>. Las dos listas de vocabulario y las cuarenta y cuatro lecciones se pueden leer aquí, gratis, si quieres juzgar el curso antes de comprar cualquiera de los dos.""",

 ">Which pronunciation is this?<": ">¿Qué pronunciación es esta?<",
 "Classical — the restored pronunciation of Caesar's Rome, in the lessons and in the voice alike: c and g always hard, v as English w, <i>Caesar</i> said as the German <i>Kaiser</i>. An ecclesiastical voice is planned separately, and Church Latin proper is a branch of its own rather than an option inside this course.":
   "La clásica — la pronunciación restituida de la Roma de César, tanto en las lecciones como en la voz: c y g siempre oclusivas, v como la w inglesa, <i>Caesar</i> dicho como el alemán <i>Kaiser</i>. Hay una voz eclesiástica planeada aparte, y el latín de la Iglesia propiamente dicho es una rama aparte, no una opción dentro de este curso.",

 ">Do I need anything else to play it?<": ">¿Necesito algo más para jugarlo?<",
 """Yes. Latin Core is a DLC for the FlashBoss base game, so you need the base game as well. Latin Pareto requires Core — the packs build on each other in order. Everything else — the lessons, the audio, the boss fights — is inside the pack. On Windows 10 you also need <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a> — a free, secure download from the Microsoft Store.""":
   """Sí. Latin Core es un DLC para el juego base de FlashBoss, así que también necesitas el juego base. Latin Pareto requiere Core — los paquetes se apoyan uno en otro, en orden. Todo lo demás — las lecciones, el audio, los boss fights — va dentro del paquete. En Windows 10 también necesitas <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a>: una descarga gratuita y segura de la Microsoft Store.""",

 ">Is the Latin real, or written for the course?<": ">¿El latín es real o está escrito para el curso?<",
 "Both, in a stated order. Tiers 1 to 3 are constructed to the grammar you have been taught — no real author writes at that ceiling, and the cards claim none. Caesar enters at Tier 4, lightly trimmed. From Tier 8 on, almost every sentence is an author's own unaltered words. Across the two packs 1,052 of 2,000 sentences carry a citation and 813 of those are unadapted.":
   "Las dos cosas, en un orden declarado. Los niveles 1 a 3 están construidos según la gramática que ya te enseñaron — ningún autor real escribe en ese tope, y las tarjetas no atribuyen ninguno. César entra en el nivel 4, apenas recortado. Del nivel 8 en adelante, casi cada oración son las palabras sin alterar de un autor. En los dos paquetes, 1.052 de 2.000 oraciones llevan referencia y 813 de ellas están sin adaptar.",

 ">Can I play it in my own language?<": ">¿Puedo jugarlo en mi propio idioma?<",
 "Fully. Every one of the 2,000 cards carries its translation, its example translation and its study notes in <b>German, Spanish, Japanese, Russian and Simplified Chinese</b> as well as English, with no gaps anywhere. All forty-four reference lessons carry the same five, and the game's own interface speaks all six.":
   "Entero. Cada una de las 2.000 tarjetas lleva su traducción, la traducción del ejemplo y sus notas de estudio en <b>alemán, español, japonés, ruso y chino simplificado</b> además de inglés, sin huecos en ninguna parte. Las cuarenta y cuatro lecciones de referencia llevan esos mismos cinco idiomas, y la interfaz del juego habla los seis.",

 ">What does the course get me to?<": ">¿Hasta dónde me lleva el curso?<",
 "Reading unadapted classical prose with a dictionary beside you. Two thousand of the highest-frequency lemmas, the whole grammar of the indicative and subjunctive, participles, the infinitive constructions, the gerund and gerundive — and 17,007 words of Latin read in context on the way there. Not speaking Latin, and not writing it: the course is honest that it teaches one skill.":
   "Hasta leer prosa clásica sin adaptar con un diccionario al lado. Dos mil de los lemas más frecuentes, toda la gramática del indicativo y del subjuntivo, los participios, las construcciones de infinitivo, el gerundio y el gerundivo — y 17.007 palabras de latín leídas en contexto por el camino. No hasta hablar latín, ni hasta escribirlo: el curso dice con honestidad que enseña una sola destreza.",

 ">Why is there no Pareto 2?<": ">¿Por qué no hay Pareto 2?<",
 "Because Latin forks instead. Core plus Pareto is a complete 2,000-word trunk, grammar-complete at Tier 10. The third thousand depends on where you are going — classical poetry or ecclesiastical Latin — so it is planned as two branches rather than one more staircase. Neither is built yet.":
   "Porque el latín se bifurca en vez de seguir. Core más Pareto son un tronco completo de 2.000 palabras, con la gramática terminada en el nivel 10. El tercer millar depende de adónde vayas — poesía clásica o latín eclesiástico — así que está planeado como dos ramas y no como otra escalera más. Ninguna está construida todavía.",

 ">Can I see the words before I buy?<": ">¿Puedo ver las palabras antes de comprar?<",
 """All of them. The complete word lists for Core and Pareto are on the <a href="wordlists.html?lang=Latin&amp;set=Core">word lists page</a>, and all forty-four reference lessons are on the <a href="lessons.html?lang=Latin">lessons page</a> — free, printable, no account.""":
   """Todas. Las listas completas de Core y Pareto están en la <a href="wordlists.html?lang=Latin&amp;set=Core">página de vocabulario</a>, y las cuarenta y cuatro lecciones de referencia están en la <a href="lessons.html?lang=Latin">página de lecciones</a> — gratis, imprimibles, sin cuenta.""",

 ">Is there a demo?<": ">¿Hay demo?<",
 """There's a playable boss fight in the browser, if you want to know what the fight feels like before you commit: <a href="https://flashboss-demo.pages.dev/">try the demo</a>.""":
   """Hay un boss fight jugable en el navegador, si quieres saber cómo se siente el combate antes de comprometerte: <a href="https://flashboss-demo.pages.dev/">probar demo</a>.""",

 # ---- closing call to action ----
 "Start with <i>Roma est.</i>": "Empieza con <i>Roma est.</i>",
 "Two words on the first card of the first cluster. Two thousand words later, Cicero.":
   "Dos palabras en la primera tarjeta del primer cluster. Dos mil palabras después, Cicerón.",
 "— both on Steam": "— los dos en Steam",
 """Or read the <a href="wordlists.html?lang=Latin&amp;set=Core">word list</a> and the <a href="lessons.html?lang=Latin">lessons</a> first — they're free, and they're the whole course.""":
   """O lee antes el <a href="wordlists.html?lang=Latin&amp;set=Core">vocabulario</a> y las <a href="lessons.html?lang=Latin">lecciones</a> — son gratis, y son el curso entero.""",
 # the bundle name is the ratified Spanish one from the Latin paste sheet
 """Everything here in one purchase: <a href="https://store.steampowered.com/bundle/87746/?utm_source=website-bundle" target="_blank" rel="noopener"><b>FlashBoss Latin — The Complete Course</b></a>. Already own part of it? Steam charges you only for the rest.""":
   """Todo esto en una sola compra: <a href="https://store.steampowered.com/bundle/87746/?utm_source=website-bundle" target="_blank" rel="noopener"><b>FlashBoss Latín — El curso completo</b></a>. ¿Ya tienes una parte? Steam solo te cobra lo que falta.""",

 # ---- footer epigraph: the Latin stands, the gloss and the cite become Spanish ----
 "<span class=\"tr\">Chance counts for much in everything, and most of all in warfare.</span>":
   "<span class=\"tr\">El azar puede mucho en todas las cosas, y sobre todo en la guerra.</span>",
 "Latin Core · Tier 4 · Caes. BG 6.30.2": "Latin Core · Nivel 4 · Caes. BG 6.30.2",
}

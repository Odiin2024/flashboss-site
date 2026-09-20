# Spanish (Latin America) strings for in-development.html.
# This page lists what is NOT out yet, so the rule above all others here is that
# it carries NO DATE of any kind — no month, no quarter, no year, no "pronto",
# no ETA. Where the English hedges without a date, the Spanish hedges without a
# date. The only date on the page is the counting date in the closing note, and
# that is when the packs were counted, not when anything ships.
# Vocabulary is read off the live Spanish pages: "paquetes" (packs.es.html),
# "en desarrollo" (what packs.es.html already calls this page in its lede),
# "ya disponible", "clusters", "tarjetas", "lecciones", "boss fights",
# "Listas de vocabulario" (wordlists.es.html's own <title>), "suajili" for the
# bare language name (swahili.html">suajili on the live pages), and the voices
# format "España · masculina" (voices.es.html writes "Alemania · masculina").
# TIERS ARE "etapas": that is what the live Spanish pages say and how
# packs.es.html writes this very construction ("las etapas 6–15"). It differs
# from immersion_es.py, which wrote "niveles" — flagged for the owner.
# Pack and product names stay English — Swahili Pareto 1/2, Core, Pareto,
# The Guide Part II, Latin Core, Latin Pareto, Greek Roots. Bare language names
# are Spanish, the way packs.es.html already writes francés and suajili.
# Numbers are the English page's numbers in Spanish separators; nothing recounted.
# Register: tú, Latin American vocabulary (reemplaza, no sustituye; allá, no allí).
TITLE = "En desarrollo — FlashBoss"
DESCRIPTION = ("Lo que FlashBoss está construyendo ahora: Swahili Pareto 1 y 2, ruso, indonesio, "
               "griego antiguo y moderno, The Guide Part II y las dos ramas del latín. "
               "Contado desde los paquetes, sin fechas de lanzamiento.")

STRINGS = {
 # ---- nav / chrome ----
 ">packs<": ">paquetes<",
 ">in development<": ">en desarrollo<",
 ">out now<": ">ya disponible<",
 ">english path<": ">camino del inglés<",
 ">voices<": ">voces<",
 ">home<": ">inicio<",
 ">resources<": ">recursos<",
 ">the english path<": ">el camino del inglés<",

 # ---- hero: the h1 is keyed with its tag so the head comment is left alone ----
 ">Not out yet<": ">Todavía no disponible<",
 '<h1 class="reveal">In Development<': '<h1 class="reveal">En desarrollo<',
 "What is being built, and how far along it is. <b>Nothing on this page has a release date</b>, because none of it has one — a date goes up when a pack is ready, not before. Everything listed here exists as real cards today; the counts were taken from the packs themselves, not from a plan.":
   "Lo que se está construyendo, y hasta dónde va. <b>Nada de esta página tiene fecha de lanzamiento</b>, porque nada la tiene — una fecha se publica cuando un paquete está listo, no antes. Todo lo que aparece aquí existe hoy como tarjetas reales; las cifras salieron de los paquetes mismos, no de un plan.",

 # ---- the legend: whole line each, so the <b> keeps its Spanish sentence ----
 "<b>Cards written</b> — the pack is authored and counted. What remains is checking, audio and a store page.":
   "<b>Tarjetas escritas</b> — el paquete está redactado y contado. Faltan la revisión, el audio y una página de tienda.",
 "<b>Planned</b> — decided and inventoried, not started. No cards exist yet.":
   "<b>Planeado</b> — decidido e inventariado, sin empezar. Todavía no existe ninguna tarjeta.",
 # the two state badges, after the legend lines above have already gone Spanish
 ">Cards written<": ">Tarjetas escritas<",
 ">Planned<": ">Planeado<",

 # ---- finishing a course already on sale ----
 "<h2>Finishing a course already on sale</h2>":
   "<h2>Terminar un curso que ya está a la venta</h2>",
 "These continue packs you can buy today, and take the pack before them as read.":
   "Estos continúan paquetes que ya puedes comprar hoy, y dan por hecho el paquete anterior.",

 "1,000 words · 40 clusters · tiers 6–10":
   "1.000 palabras · 40 clusters · etapas 6–10",
 "The working vocabulary: money and the bank, the company and the contract, the ministry, elections, the court, the police, the press, the hospital. Continues <a href=\"swahili.html\">Swahili Core</a>, which is out now.":
   "El vocabulario de trabajo: el dinero y el banco, la empresa y el contrato, el ministerio, las elecciones, el juzgado, la policía, la prensa, el hospital. Continúa <a href=\"swahili.html\">Swahili Core</a>, que ya está disponible.",

 "1,000 words · 40 clusters · tiers 11–15":
   "1.000 palabras · 40 clusters · etapas 11–15",
 "The last thousand of the 3,000-word course, and where Swahili's derivation opens up — one root becoming six verbs through the passive, the stative, the reciprocal, the reflexive, the causative and the applicative.":
   "El último millar del curso de 3.000 palabras, y el punto donde se abre la derivación del suajili — una raíz que se vuelve seis verbos por el pasivo, el estativo, el recíproco, el reflexivo, el causativo y el aplicativo.",

 "925 cards · 50 clusters · three tiers · English and German":
   "925 tarjetas · 50 clusters · tres etapas · inglés y alemán",
 "The other half of a game master's memory. Where <a href=\"the-guide.html\">The Guide</a> holds the rules you adjudicate with, Part II holds what you populate a world with: the spell list, the creature roster and the treasure table. Requires The Guide.":
   "La otra mitad de la memoria de un director de juego. Donde <a href=\"the-guide.html\">The Guide</a> guarda las reglas con las que arbitras, Part II guarda aquello con lo que pueblas un mundo: la lista de conjuros, el catálogo de criaturas y la tabla de tesoros. Requiere The Guide.",

 # ---- new languages: bare language names go Spanish, Core/Pareto stay ----
 "<h2>New languages</h2>": "<h2>Nuevos idiomas</h2>",
 "Each is a full course in the usual shape — Core first, then Pareto 1, five tiers apiece.":
   "Cada uno es un curso completo con la forma de siempre — primero Core, después Pareto 1, cinco etapas cada uno.",

 "Core and Pareto 1 · 1,000 words each · 40 clusters each":
   "Core y Pareto 1 · 1.000 palabras cada uno · 40 clusters cada uno",

 ">Russian<": ">Ruso<",
 "Русский. Two thousand words authored and counted.":
   "Русский. Dos mil palabras redactadas y contadas.",

 ">Indonesian<": ">Indonesio<",
 "Bahasa Indonesia — a language with no tenses, no genders and no plurals to memorise, and a word order you already have.":
   "Bahasa Indonesia — una lengua sin tiempos verbales, sin géneros y sin plurales que memorizar, y con un orden de palabras que ya tienes.",

 ">Modern Greek<": ">Griego moderno<",
 "Ελληνικά, the living language, with an alphabet ladder in the opening lessons. Not to be confused with Ancient Greek below, or with <a href=\"greek-roots.html\">Greek Roots</a>, which teaches the Greek already inside English.":
   "Ελληνικά, la lengua viva, con una escalera del alfabeto en las primeras lecciones. No lo confundas con el griego antiguo de más abajo, ni con <a href=\"greek-roots.html\">Greek Roots</a>, que enseña el griego que ya está dentro del inglés.",

 ">Ancient Greek<": ">Griego antiguo<",
 "A reading course, in the shape <a href=\"latin.html\">Latin</a> took: the sentences start built for the tier and end as the authors wrote them.":
   "Un curso de lectura, con la forma que tomó el <a href=\"latin.html\">latín</a>: las frases empiezan construidas para la etapa y terminan tal como las escribieron los autores.",

 ">Polish and Portuguese<": ">Polaco y portugués<",
 "Word lists locked · no cards authored yet":
   "Listas de vocabulario fijadas · todavía no hay tarjetas escritas",
 "The frequency backbones are chosen and fixed, which is the half of the work that decides what a course teaches. The cards themselves are not written.":
   "La columna vertebral de frecuencia ya está elegida y fijada en los dos casos, y en eso está la mitad del trabajo que decide qué enseña un curso. Las tarjetas mismas no están escritas.",

 # ---- beyond the Latin trunk ----
 "<h2>Beyond the Latin trunk</h2>": "<h2>Más allá del tronco del latín</h2>",
 "Latin Core and Latin Pareto are the whole 2,000-word reading course, grammar-complete at tier 10. There is deliberately no third staircase.":
   "Latin Core y Latin Pareto son el curso de lectura completo de 2.000 palabras, con la gramática cerrada en la etapa 10. No hay una tercera escalera, y es a propósito.",

 ">Latin — the two branches<": ">Latín — las dos ramas<",
 "Classical poetry · or ecclesiastical Latin": "Poesía clásica · o latín eclesiástico",
 "Past 2,000 words Latin genuinely divides, and which thousand comes next depends on what you want to read: <b>classical poetry</b> — Vergil, Ovid, Catullus, Horace — or <b>ecclesiastical Latin</b>, the Vulgate, the hymns and the liturgy. Both are inventoried and reserved. Neither is built, and neither takes the other as a prerequisite.":
   "Pasadas las 2.000 palabras el latín se divide de verdad, y qué millar viene después depende de lo que quieras leer: <b>poesía clásica</b> — Virgilio, Ovidio, Catulo, Horacio — o <b>latín eclesiástico</b>, la Vulgata, los himnos y la liturgia. Los dos están inventariados y reservados. Ninguno está construido, y ninguno exige al otro como requisito.",

 # ---- voices ----
 "<h2>Voices</h2>": "<h2>Voces</h2>",
 ">Castellano — Spain, male<": ">Castellano — España, masculina<",
 "Replaces the included Latin American voice across every Spanish pack":
   "Reemplaza la voz latinoamericana incluida en todos los paquetes de español",
 "A voice pack rather than a course: it swaps the voice in cards, lessons and boss fights, and switches back whenever you like. Hear it against the voice it replaces on the <a href=\"voices.html\">voices page</a>.":
   "Un paquete de voz, no un curso: cambia la voz en las tarjetas, las lecciones y los boss fights, y vuelves a la anterior cuando quieras. Escúchala frente a la voz que reemplaza en la <a href=\"voices.html\">página de voces</a>.",

 # ---- the closing note: the date here is the COUNTING date, not a release ----
 "Everything above was counted from the packs on <b>19 September 2026</b>. A pack leaves this page the day it goes on sale and appears on <a href=\"packs.html\">the pack list</a> instead — so if something has vanished from here, look for it there.":
   "Todo lo de arriba se contó desde los paquetes el <b>19 de septiembre de 2026</b>. Un paquete deja esta página el día que sale a la venta y pasa a <a href=\"packs.html\">la lista de paquetes</a> — así que si algo desapareció de aquí, búscalo allá.",
 "And yes — the page that lists what's in development used to be, itself, in development.":
   "Y sí — la página que lista lo que está en desarrollo estuvo, ella misma, en desarrollo.",
}

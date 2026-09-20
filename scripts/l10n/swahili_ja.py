# Japanese strings for swahili.html.
# The store-facing vocabulary is LIFTED from the ratified Japanese bundle copy
# (flashboss-admin/BUNDLE_COPY_SWAHILI_2026-09-08.md) wherever that sheet has
# it — スワヒリ語, ティア, クラスター, ボス戦, 間隔反復, 参照レッスン, 学習ノート,
# 簡体字中国語, and the six-language list. The method and FAQ wording follows the
# Japanese course pages that already exist (french.ja.html, english.ja.html,
# packs.ja.html): "なぜ定着するのか", "単語カードを、ひとつの仕組みに",
# "フィボナッチ間隔反復", "合成音声であり、話者の録音ではありません",
# "買う前に単語を見られますか？", "これはどのフランス語ですか?" → "これはどの
# スワヒリ語ですか？", and the whole shape of "はい。…はFlashBoss本体のDLCなので、
# 基本ゲームも必要です。… Windows 10では Windows Terminal も必要です".
# The hero signature line is the live ja pages' own string, verbatim:
# "聞く・読む・繰り返す・評価する・戦う". The rest is mine.
#
# PAGE CANON, held here:
#   * every Swahili word, form and example SENTENCE is left byte-identical —
#     anaendesha, tulisafiri, walipanda, the three quoted pack sentences, gari's
#     card, the ten noun-class names (m/wa, ji/ma, ku, pa …). Only the gloss
#     after the em dash becomes Japanese, because the card carries a Japanese
#     gloss too.
#   * pack names stay English: Swahili Core, Swahili Pareto 1, Swahili Pareto 2,
#     Core, Pareto 1, Pareto 2. So does FlashBoss.
#   * grammar terms are the standard Japanese ones: 名詞クラス, 一致, 時制, 主語,
#     目的語, 使役形, 現在.
#   * the page's counts (1,000 / 40 / 20 / 14 / five tiers) are the recount of
#     2026-09-19 and are reproduced exactly; the 2026-09-08 bundle sheet's
#     「49の参照レッスン」 predates it and does not win. ja keeps the English
#     page's comma, so 1,000 is written 1,000.
#   * banned and absent: hours, CEFR codes, prices, discounts, and a date for
#     anything already out.
#
# Register: です／ます, no keigo inflation, no exclamation marks. NO SPACES around
# Latin-script words inside a Japanese sentence — that is what the live ja pages
# do ("stubbornとobstinate"), and what the immersion page settled; french.ja.html
# spaces a few ("bonjour から"), and this file does not follow it.
# 基本ゲーム, not ベースゲーム, per the immersion page and every live ja page.
# An ASCII comma between example pairs becomes 、 (<i>ji/ma</i>、<i>ki/vi</i>).
#
# FLAGGED FOR THE OWNER: the language name. The ja site writes スワヒリ語
# everywhere (lessons.ja.html's LANG_JA map, wordlists.ja.html), so the prose and
# the <title> say スワヒリ語 where the German file simply kept "Swahili". The nav
# crumb and the <h1> still read "Swahili" — no key covers them, and the key set
# is fixed by swahili_de.py.
TITLE = "スワヒリ語 — FlashBoss"
DESCRIPTION = ("FlashBossのスワヒリ語：40クラスターの1,000語と20の参照レッスン、"
               "どの名詞にも名詞クラスを明記、標準スワヒリ語のニューラル音声、"
               "そしてどの関門にもボス戦。訳語と学習ノートは6言語。"
               "Swahili CoreはSteamで発売中。")

STRINGS = {
 # ---- nav / chrome / footer ----
 ">packs<": ">パック<",
 ">word list<": ">単語リスト<",
 ">lessons<": ">レッスン<",
 ">voices<": ">音声<",
 ">home<": ">ホーム<",

 # ---- hero ----
 "The newest course · <b>1,000 words out now</b>":
   "最新のコース · <b>1,000語、発売中</b>",
 "The most regular language you will ever learn the hard way.":
   "苦労して学ぶ言語のなかで、これがいちばん規則的です。",
 # the live ja pages' own signature line, verbatim
 "Listen · read · repeat · rate · fight":
   "聞く・読む・繰り返す・評価する・戦う",
 "Swahili does not conjugate so much as <b>assemble</b>. A verb is built from slots in a fixed order, and every noun belongs to a class that the rest of the sentence agrees with. Learn those two machines and the vocabulary stops being a list. <b>1,000 words, 40 clusters, 20 reference lessons</b> — with the class named on every noun.":
   "スワヒリ語は活用するというより<b>組み立てます</b>。動詞は決まった順番のスロットから組み立てられ、名詞はいずれかのクラスに属して、文の残りがそのクラスに一致します。この二つの仕組みを覚えれば、語彙は単なるリストではなくなります。<b>1,000語、40クラスター、20の参照レッスン</b> — クラスはどの名詞にも書かれています。",

 # ---- the argument ----
 "Why Swahili is learnable": "スワヒリ語が学べる理由",
 "A language with no irregular verbs to speak of":
   "不規則動詞がほとんどない言語",
 "Swahili is the working language of East Africa — Tanzania, Kenya, Uganda, Rwanda, Burundi and the eastern Congo — and it is spoken by far more people who learned it than by people born to it. That has worn it smooth. Spelling is exactly as it sounds, stress is always the second-to-last syllable, and there is no tone and no grammatical gender.":
   "スワヒリ語は東アフリカの共通語です — タンザニア、ケニア、ウガンダ、ルワンダ、ブルンジ、そしてコンゴ東部 — 生まれつき話す人より、学んで話す人のほうがはるかに多い言語です。そのぶん角が取れました。綴りは音のとおり、アクセントはつねに後ろから2番目の音節、声調も文法上の性もありません。",
 "What it has instead is <b>structure you can see</b>. The verb is a train of slots. The noun carries a class, and the class rides through the whole sentence. Neither is hidden, and neither has a list of exceptions waiting for you at intermediate level.":
   "かわりにあるのは<b>目に見える構造</b>です。動詞はスロットの連なった列車です。名詞はクラスを帯び、そのクラスが文の全体を走り抜けます。どちらも隠れていませんし、どちらにも中級で待ち構える例外の一覧はありません。",
 "This course teaches ordinary Swahili — the language of the market, the school and the news. The frequency backbone it is built from was made for that, not for subtitles.":
   "このコースが教えるのは、ふつうのスワヒリ語です — 市場と学校とニュースのことば。土台にした頻度データは、字幕のためではなく、そのために作られたものです。",

 # ---- the verb train. The three Swahili sentences are quoted from the pack's
 #      own cards: they stay byte-identical, only the gloss becomes Japanese. ----
 "The verb is an assembly": "動詞は組み立て品",
 "Slots, in a fixed order": "決まった順番のスロット",
 "Three sentences from the pack's own cards, taken apart. The order never changes: who, when, whom, what.":
   "パック自身のカードから取った3つの文を、分解しました。順番は決して変わりません：誰が、いつ、誰を、何を。",
 '<i class="ls"></i> who — the subject': '<i class="ls"></i> 誰が — 主語',
 '<i class="lt"></i> when — the tense': '<i class="lt"></i> いつ — 時制',
 '<i class="lo"></i> whom — the object': '<i class="lo"></i> 誰を — 目的語',
 '<i class="lr"></i> what — the root': '<i class="lr"></i> 何を — 語根',

 "Baba yangu <b>anaendesha</b> basi la shule kila asubuhi, na mama anaendesha gari. — My father drives the school bus every morning, and my mother drives the car.":
   "Baba yangu <b>anaendesha</b> basi la shule kila asubuhi, na mama anaendesha gari. — 父は毎朝スクールバスを運転し、母は車を運転します。",
 '<span class="m s">a-<i>he / she</i></span>': '<span class="m s">a-<i>彼 / 彼女</i></span>',
 '<span class="m t">na-<i>present</i></span>': '<span class="m t">na-<i>現在</i></span>',
 '<span class="m r">endesha<i>drive, make go</i></span>':
   '<span class="m r">endesha<i>運転する、行かせる</i></span>',
 "Three pieces, read left to right: <b>he · now · drives</b>. The root itself is built — <i>endesha</i> is the causative of <i>kwenda</i>, to go, so it means to make something go.":
   "3つの部品を、左から右へ読みます：<b>彼 · いま · 運転する</b>。語根そのものが組み立てです — <i>endesha</i>は<i>kwenda</i>（行く）の使役形なので、何かを行かせるという意味になります。",

 "<b>Tulisafiri</b> kwa treni kutoka jijini hadi kijijini kwetu wakati wa likizo. — We travelled by train from the city to our village during the holiday.":
   "<b>Tulisafiri</b> kwa treni kutoka jijini hadi kijijini kwetu wakati wa likizo. — 休みのあいだ、私たちは町から自分たちの村まで列車で旅をしました。",
 '<span class="m s">tu-<i>we</i></span>': '<span class="m s">tu-<i>私たち</i></span>',
 '<span class="m t">li-<i>past</i></span>': '<span class="m t">li-<i>過去</i></span>',
 '<span class="m r">safiri<i>travel</i></span>': '<span class="m r">safiri<i>旅をする</i></span>',
 "Change one letter in the middle slot and you change the tense. <b>tuna</b>safiri is we are travelling; <b>tuta</b>safiri is we will travel. Nothing else in the word moves.":
   "真ん中のスロットの文字を1つ変えれば、時制が変わります。<b>tuna</b>safiriは旅をしているところ、<b>tuta</b>safiriはこれから旅をする、です。語のほかの部分は何も動きません。",

 "Watu wengi <b>walipanda</b> basi hilo kubwa mapema asubuhi ya leo. — Many people boarded that big bus early this morning.":
   "Watu wengi <b>walipanda</b> basi hilo kubwa mapema asubuhi ya leo. — 今朝早く、大勢の人があの大きなバスに乗りました。",
 '<span class="m s">wa-<i>they, class m/wa</i></span>':
   '<span class="m s">wa-<i>彼ら、m/waクラス</i></span>',
 '<span class="m r">panda<i>climb, board, plant</i></span>':
   '<span class="m r">panda<i>登る、乗る、植える</i></span>',
 "The subject slot is not just a pronoun: it agrees with the <b>class</b> of the noun. <i>Watu</i> is class m/wa, so the verb starts wa-. That is the second machine.":
   "主語のスロットは、ただの代名詞ではありません：名詞の<b>クラス</b>に一致します。<i>Watu</i>はm/waクラスなので、動詞はwa-で始まります。これが二つめの仕組みです。",
 "The pack drills this directly. One of Swahili's three revision drills is the verb train, built slot by slot — you assemble the form rather than recall it whole.":
   "パックはこれをそのままドリルにしています。スワヒリ語の3つの復習ドリルのひとつが動詞の列車で、スロットを一つずつ組み立てていきます — 形をまるごと思い出すのではなく、組み立てるのです。",

 # ---- noun classes: whole cells, so no English label survives next to a
 #      class name. The class names themselves are Swahili and stay. ----
 "The engine": "エンジン",
 "Every noun carries its class": "どの名詞もクラスを帯びています",
 "Swahili has no gender. It has classes — and the class of the noun decides the shape of its plural, its adjectives, its verb and its possessives. Get the class and the agreement comes free.":
   "スワヒリ語に性はありません。あるのはクラスです — そして名詞のクラスが、複数形、形容詞、動詞、所有形のかたちを決めます。クラスさえつかめば、一致はおまけで付いてきます。",
 '<div class="k">m/wa</div><div class="v">people — <i>mtu / watu</i></div>':
   '<div class="k">m/wa</div><div class="v">人 — <i>mtu / watu</i></div>',
 '<div class="k">m/mi</div><div class="v">trees, living things, body parts</div>':
   '<div class="k">m/mi</div><div class="v">木、生きもの、体の部分</div>',
 '<div class="k">ji/ma</div><div class="v">large things, pairs, groups</div>':
   '<div class="k">ji/ma</div><div class="v">大きなもの、対になるもの、集まり</div>',
 '<div class="k">ki/vi</div><div class="v">objects, tools, languages</div>':
   '<div class="k">ki/vi</div><div class="v">物、道具、言語</div>',
 '<div class="k">n/n</div><div class="v">loans, animals, many abstracts</div>':
   '<div class="k">n/n</div><div class="v">借用語、動物、多くの抽象語</div>',
 '<div class="k">u/n</div><div class="v">abstract nouns, mass nouns</div>':
   '<div class="k">u/n</div><div class="v">抽象名詞、不可算名詞</div>',
 '<div class="k">u/ma</div><div class="v">long thin things</div>':
   '<div class="k">u/ma</div><div class="v">細長いもの</div>',
 '<div class="k">u/u</div><div class="v">a smaller set, no plural shift</div>':
   '<div class="k">u/u</div><div class="v">小さめの一群、複数形で形が変わりません</div>',
 '<div class="k">ku</div><div class="v">the infinitive used as a noun</div>':
   '<div class="k">ku</div><div class="v">名詞として使う不定詞</div>',
 '<div class="k">pa</div><div class="v">place</div>':
   '<div class="k">pa</div><div class="v">場所</div>',
 "Those are the ten classes this pack actually uses, taken from its cards rather than from a grammar. The class is printed on every single noun in the deck, where another course would leave you to infer it.":
   "これが、このパックで実際に使われている10のクラスです。文法書からではなく、パックのカードから取りました。クラスはデッキのすべての名詞に印字されています。ほかのコースなら、読み手に推測させるところです。",

 # ---- the card. gari and its Swahili example sentence stay. ----
 "What a card holds": "カードに載っているもの",
 "A real one, from tier 2. The class sits beside the headword; the notes say the thing a dictionary would not.":
   "ティア2の実物です。クラスは見出し語の隣に置かれ、ノートは辞書が言わないことを言います。",
 '<div class="tr">a car, or any road vehicle</div>':
   '<div class="tr">車、あるいは路上を走る乗り物全般</div>',
 '<div class="exx">Our car has no fuel, so we have stopped near the bridge.</div>':
   '<div class="exx">私たちの車は燃料が切れたので、橋の近くで止まっています。</div>',
 "The same card carries its translation, its example translation <b>and</b> its notes in German, Japanese, Russian, Simplified Chinese and Spanish as well as English — full coverage, every card, no gaps.":
   "同じカードが、訳語、例文の訳、<b>そして</b>ノートを、英語だけでなくドイツ語・日本語・ロシア語・簡体字中国語・スペイン語でも載せています — どのカードも全言語そろっていて、抜けはありません。",

 # ---- method: whole <dt>/<dd> pairs, so no English term is left stranded ----
 "How it sticks": "なぜ定着するのか",
 "Flashcards as an integrated system": "単語カードを、ひとつの仕組みに",
 "<dt>Cards</dt><dd><b>1,000 words across 40 clusters</b> and five tiers — greetings and family, the town, work and health, government, the news, and the small words that join sentences together. An example sentence on every card.</dd>":
   "<dt>カード</dt><dd><b>40クラスターにわたる1,000語</b>と5つのティア — あいさつと家族、町、仕事と健康、役所、ニュース、そして文と文をつなぐ小さな語。どのカードにも例文が付きます。</dd>",
 "<dt>Noun class</dt><dd>Named on <b>every noun</b>, on the card itself: <i>ji/ma</i>, <i>ki/vi</i>, <i>m/wa</i>. The engine the whole language runs on, never left implicit.</dd>":
   "<dt>名詞クラス</dt><dd><b>どの名詞にも</b>、カードそのものに書かれています：<i>ji/ma</i>、<i>ki/vi</i>、<i>m/wa</i>。言語全体を動かしているエンジンを、暗黙のままにはしません。</dd>",
 "<dt>Your language</dt><dd>Translations and study notes in <b>English, German, Japanese, Russian, Simplified Chinese and Spanish</b> — full coverage on every card. Study Swahili through whichever you call home.</dd>":
   "<dt>あなたの言語</dt><dd><b>英語・ドイツ語・日本語・ロシア語・簡体字中国語・スペイン語</b>の訳語と学習ノート — どのカードにも全言語そろっています。自分が母語と呼ぶ言語で、スワヒリ語を学べます。</dd>",
 '<dt>Lessons</dt><dd><b>20 reference lessons</b> — the sound system, the noun-class families, the verb slot machine, the Swahili clock, and concord tier by tier. Readable in all six languages, and <a href="lessons.html?lang=Swahili">free to read here</a>.</dd>':
   '<dt>レッスン</dt><dd><b>20の参照レッスン</b> — 音の体系、名詞クラスの一族、動詞のスロット装置、スワヒリの時刻、そしてティアごとの一致。6言語すべてで読めて、<a href="lessons.html?lang=Swahili">ここで無料で読めます</a>。</dd>',
 "<dt>Drills</dt><dd>Three, shaped to Swahili rather than borrowed: the <b>verb train</b> built slot by slot, <b>plurals by noun class</b>, and <b>dictation</b>.</dd>":
   "<dt>ドリル</dt><dd>3つ。よそから借りたものではなく、スワヒリ語に合わせて作りました：スロットを一つずつ組み立てる<b>動詞の列車</b>、<b>名詞クラス別の複数形</b>、そして<b>ディクテーション</b>。</dd>",
 "<dt>Audio</dt><dd>Text-to-speech on every word and every example sentence, in a neural standard Kiswahili voice. Synthesis, not a recording of a speaker.</dd>":
   "<dt>音声</dt><dd>すべての語とすべての例文に、標準スワヒリ語のニューラル音声によるテキスト読み上げ。合成音声であり、話者の録音ではありません。</dd>",
 "<dt>Fibonacci SRS</dt><dd>Rate each card 0–5. The better you know a word, the longer before it returns.</dd>":
   "<dt>フィボナッチ間隔反復</dt><dd>カードごとに0〜5で自己評価します。よく覚えている語ほど、次に出るまでの間隔が延びます。</dd>",
 "<dt>Boss fights</dt><dd>No cluster is cleared until its hardest words are answered. Beat it and its cards leave your daily deck for good.</dd>":
   "<dt>ボス戦</dt><dd>いちばん手強い語に答えないかぎり、クラスターは攻略できません。倒せば、そのカードは毎日のデッキから永久に外れます。</dd>",

 # ---- the three packs. Pack names stay English; no date on the unreleased two. ----
 "Three packs, three thousand words": "3つのパック、3,000語",
 "Core is out. The two that follow are written and are not on sale yet; neither carries a date until it is.":
   "Coreは発売中です。続く2つは書き上がっていますが、まだ販売していません。売り出すまでは、どちらにも日付を出しません。",
 '<div class="lvl">Tiers 1–5 · 1,000 words · 20 lessons</div>':
   '<div class="lvl">ティア1〜5 · 1,000語 · レッスン20本</div>',
 "<p>The foundation: greetings and the family through the town, work and health to government and the news.</p>":
   "<p>土台：あいさつと家族から、町、仕事と健康を経て、役所とニュースまで。</p>",
 '<span class="here">On Steam</span>': '<span class="here">Steamで発売中</span>',
 '<div class="lvl">Tiers 6–10 · 1,000 words · 14 lessons</div>':
   '<div class="lvl">ティア6〜10 · 1,000語 · レッスン14本</div>',
 "<p>The working vocabulary: money and the bank, the contract, the ministry, elections, the court, the press, the hospital.</p>":
   "<p>実務の語彙：お金と銀行、契約、省庁、選挙、裁判所、報道、病院。</p>",
 '<span class="soon">Written, not yet out</span>':
   '<span class="soon">執筆済み、未発売</span>',
 '<div class="lvl">Tiers 11–15 · 1,000 words · 14 lessons</div>':
   '<div class="lvl">ティア11〜15 · 1,000語 · レッスン14本</div>',
 "<p>Where derivation opens up — one root becomes six verbs — and the vocabulary follows it into public life and register.</p>":
   "<p>派生が開けるところ — ひとつの語根が6つの動詞になります — そして語彙はそれを追って、公共の場と文体の層へ入っていきます。</p>",
 "Each pack is 1,000 words and five tiers, and each takes the one before it as read. The end of Pareto 1 is the hump: not finished, but the language has stopped being a wall.":
   "どのパックも1,000語と5つのティアで、前のパックを済ませたものとして進みます。Pareto 1の終わりが峠です。まだ終わりではありませんが、そこでスワヒリ語は壁ではなくなります。",

 # ---- FAQ ----
 "Questions": "質問",
 "Before you buy": "買う前に",
 "<summary>Do I need the base game?</summary>": "<summary>基本ゲームは必要ですか？</summary>",
 'Yes. Swahili Core is DLC for FlashBoss, so you need the base game as well. Everything else — the lessons, the audio, the drills, the boss fights — is inside the pack. On Windows 10 you also need <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a>, a free download from the Microsoft Store.':
   'はい。Swahili CoreはFlashBossのDLCなので、基本ゲームも必要です。それ以外 — レッスン、音声、ドリル、ボス戦 — はすべてパックの中に入っています。Windows 10では<a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a>も必要です。Microsoft Storeから無料でダウンロードできます。',
 "<summary>Can I study it in my own language?</summary>":
   "<summary>自分の言語で学べますか？</summary>",
 "Fully. Every card carries its translation, its example translation and its study notes in <b>German, Japanese, Russian, Simplified Chinese and Spanish</b> as well as English, with no gaps, and all 20 reference lessons carry the same six. The game's own interface speaks them too.":
   "完全に学べます。どのカードも、訳語、例文の訳、学習ノートを、英語だけでなく<b>ドイツ語・日本語・ロシア語・簡体字中国語・スペイン語</b>で持っていて、抜けはありません。20の参照レッスンも同じ6言語です。ゲームのインターフェースもこの6言語を話します。",
 "<summary>Which Swahili is this?</summary>": "<summary>これはどのスワヒリ語ですか？</summary>",
 "Standard Kiswahili — the one taught in schools and used by the press across East Africa, based on the Zanzibar dialect. The voice is a neural standard Kiswahili voice.":
   "標準スワヒリ語です — 東アフリカ全域で学校が教え、報道が使うもので、ザンジバル方言がもとになっています。音声は標準スワヒリ語のニューラル音声です。",
 "<summary>Can I see the words before I buy?</summary>":
   "<summary>買う前に単語を見られますか？</summary>",
 'All of them. The complete <a href="wordlists.html?lang=Swahili&amp;set=Core">word list</a> and all twenty <a href="lessons.html?lang=Swahili">reference lessons</a> are on this site — free, printable, no account. There is also a <a href="https://flashboss-demo.pages.dev/">playable boss fight</a>.':
   'すべて見られます。完全な<a href="wordlists.html?lang=Swahili&amp;set=Core">単語リスト</a>と20本の<a href="lessons.html?lang=Swahili">参照レッスン</a>が、このサイトにあります — 無料、印刷可、アカウント不要。<a href="https://flashboss-demo.pages.dev/">遊べるボス戦</a>もあります。',
 "<summary>Is there a British or American spelling layer?</summary>":
   "<summary>英国綴りと米国綴りの切り替えはありますか？</summary>",
 "That layer covers the English packs. Swahili's English is the translation side of the card, and the pack ships one edition of it.":
   "その層は英語のパックのためのものです。スワヒリ語のパックでは、英語はカードの訳語の側にあり、パックが出すのはその1種類だけです。",

 # ---- final ----
 "Start with <i>Habari?</i>": "<i>Habari?</i>から始めましょう",
 "Two machines and a thousand words. The rest of Swahili agrees with them.":
   "二つの仕組みと1,000語。スワヒリ語の残りは、それに一致します。",
 "Swahili Core on Steam &rarr;": "Swahili CoreをSteamで &rarr;",
}

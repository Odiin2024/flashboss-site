# Japanese strings for the-guide.html.
#
# Same key set, same order, as scripts/l10n/the-guide_de.py.
#
# Sources, in the order they win:
#   1. IP CARE, from the English page's own head comment. The trademarked game
#      name appears NOWHERE on this page and appears nowhere here either, in any
#      language or spelling — not in kanji, not in katakana. The licence framing
#      is the store page's and must not drift: "5E" -> "5E対応", and "System
#      Reference Document 5.2", "SRD" and "5E" stay in their English/technical
#      form. "the 2024 revision" / "the 2014 rules" keep their figures exactly
#      and take only the surrounding word in Japanese, the way the ratified
#      Japanese store copy already writes them (2024年改訂版). The footer's
#      no-affiliation line is translated in full, all three prongs kept —
#      提携 / 承認 / 後援.
#   2. The ratified Japanese bundle copy
#      (flashboss-admin/BUNDLE_COPY_THE_GUIDE_COMPLETE_2026-09-17.md) wherever
#      it has the sentence: ゲームマスター, 卓上で起きている場面, the five
#      what-a-card-is-for clauses in the hero lede, 状態 / 判定 / DC /
#      ステータスブロック, リファレンスレッスン, クラスター, ボス戦, 宝物,
#      5E対応, 2024年改訂版, 簡体字中国語.
#   3. The shipped deck itself, knight/flashcard_sets/The_Guide/core, for rules
#      jargon a Japanese table actually says, read off the Japanese reference
#      lessons rather than invented: 状態, 判定, ダイス, 手番, アクション,
#      能力値, 習熟ボーナス, セーヴ, 精神集中, 呪文スロット, 射程, 脅威度,
#      経験点, 種族, 特技, クラス, ダメージ種別, 裁定, 遭遇, 罠, 卓.
#      The sample card (Dim Light, cluster1_10) is quoted from its OWN Japanese
#      twin — ExampleSentence_ja, Translation_ja, ExampleTranslation_ja,
#      Notes_ja — so the page shows the card as the Japanese edition really
#      ships it, 〈知覚〉, 暗視, 軽度の隠蔽 and all. Its citation is "SRD p. 11",
#      which is also the English page's figure, so nothing moved.
#   4. The live ja pages of this site for chrome and register:
#      聞く・読む・繰り返す・評価する・戦う (the sig line, on eleven pages),
#      定着のしくみ, 統合システムとしてのフラッシュカード, フィボナッチSRS,
#      質問, 発売中, ティア1 / 5つのティア, 基本ゲーム.
#
# THE HEADWORD STAYS ENGLISH — the one deliberate difference from the German
# file. German is the full edition, so its sample card shows a German headword.
# Japanese is the mixed edition: the editions section three screens below says
# in so many words that the headword you answer with is English. Printing
# 薄暗い光 in the .hw slot would contradict the page's own promise and would
# show the beta bonus edition instead of the one a Japanese buyer gets. The key
# is kept, mapped to itself, so the key set still matches the German file.
#
# Register: です／ます, no keigo inflation, no exclamation marks. NO SPACES
# around Latin-script words inside a Japanese sentence (The GuideはFlashBossの
# DLC…), which is what the live ja pages do and what the ratified Steam sheet
# does not; the site wins, so the lifted sentences are de-spaced. 、 rather than
# an ASCII comma between listed examples.
#
# Pack names stay English: The Guide. FlashBoss stays Latin. Numbers are the
# English page's; ja writes the same thousands comma the English page already
# writes, so nothing moves and nothing was recounted. Where English spells a
# number as a word (fifteen conditions, twelve classes, two seconds) the
# Japanese uses the ASCII digit, which is what both the live ja pages
# (6つのステップ) and the shipped ja lessons (12のクラス, 9の種族) do.
TITLE = "The Guide — FlashBoss"
DESCRIPTION = ("FlashBoss The Guide：ゲームマスターが頭に入れておくべき規則を、"
               "フラッシュカードで。62のクラスターに1,205枚、62本のリファレンスレッスン、"
               "どの関門にもボス戦。ドイツ語は完全版。日本語・簡体字中国語・ロシア語・"
               "スペイン語はあなたの言語で進み、答えは英語です。5E対応、"
               "System Reference Document 5.2に基づいています。")

STRINGS = {
 # ---- nav / chrome ----
 ">packs<": ">パック<",
 ">card lists<": ">カードリスト<",
 ">lessons<": ">レッスン<",
 ">voices<": ">音声<",
 ">home<": ">ホーム<",

 # ---- hero ----
 "For the person running the table · <b>out now</b>":
   "卓を回す人のために · <b>発売中</b>",
 "1,205 cards · 62 clusters": "カード1,205枚 · 62クラスター",
 "The rules a game master needs in their head — not on the page they are turning to.":
   "ゲームマスターが頭に入れておくべき規則 — いま開こうとしているページの上ではなく。",
 # the sig line as eleven live ja pages already write it, ・ and all
 "Listen · read · repeat · rate · fight": "聞く・読む・繰り返す・評価する・戦う",
 # the five clauses are the ratified store line, word for word, with the sixth
 # clause (level 5) the English page adds; 骰子 in the sheet is replaced by
 # ダイス, which is what the shipped ja lessons and a Japanese table say
 "Every card is one thing you should know cold rather than stop to look up: what a condition does, which die a check calls for, what a DC of 15 is meant to mean, what a stat block is telling you, what a party can actually do at level 5. <b>5E compatible, built from the System Reference Document 5.2.</b>":
   "どのカードも、その場で調べるのではなく覚えておくべきことをひとつだけ載せています：状態が何をするのか、判定はどのダイスを求めるのか、DC15とはどの程度なのか、ステータスブロックは何を語っているのか、レベル5のパーティは実際に何ができるのか。<b>5E対応、System Reference Document 5.2に基づいています。</b>",
 ">what a card holds</a>": ">カードに載っているもの</a>",
 ">languages</a>": ">言語</a>",

 # ---- the argument ----
 ">Why drill the rules at all<": ">そもそも、なぜ規則を反復するのか<",
 "<h2>Looking it up is the thing that breaks the table</h2>":
   "<h2>卓を壊すのは、調べることです</h2>",
 "A game master's real skill is adjudicating at speed. Everyone at the table can feel the difference between a ruling that arrives in two seconds and one that arrives after ninety seconds of page-turning — and the second one costs you the scene, not just the time.":
   "ゲームマスターの本当の腕は、素早く裁定することです。2秒で出る裁定と、90秒ページをめくったあとに出る裁定。その差は卓にいる全員が感じ取ります — そして後者が奪うのは、時間だけではなく、その場面そのものです。",
 "The fix is not a better index. It is <b>knowing the thing</b>: the fifteen conditions, the thirteen damage types, the ability and proficiency tables, challenge rating and the experience it is worth. The numbers you currently flip pages for.":
   "答えは、もっとよい索引ではありません。<b>それを知っていること</b>です：15の状態、13のダメージ種別、能力値と習熟の表、脅威度とそれが値する経験点。いまページをめくって探している、あの数字たちです。",
 "So this is a vocabulary course whose vocabulary happens to be a rules set. Same machine as every other FlashBoss pack — spaced repetition, a boss fight at the end of every cluster — pointed at the things you are expected to have in your head when someone asks whether they can shove the ogre off the bridge.":
   "つまりこれは語彙コースで、その語彙がたまたま規則集なのです。仕組みはほかのFlashBossパックと同じ — 間隔反復、どのクラスターの最後にもボス戦 — それを、オーガを橋から突き落とせるかと誰かに訊かれたときに頭に入っているべきものへ向けています。",

 # ---- the card ----
 "<h2>What a card holds</h2>": "<h2>カードに載っているもの</h2>",
 "A real card from tier 1, quoted as it ships. The scene is the point: the rule arrives as something you could narrate, not as an index entry.":
   "ティア1の実物のカードを、出荷されているそのまま引きました。要は場面です：規則は索引の項目としてではなく、語って聞かせられるものとして届きます。",
 ">the card<": ">カード<",
 ">what each part is for<": ">各部分の役割<",

 # the sample card, quoted from its own Japanese twin in cluster1_10 rather than
 # translated here — scene, definition, rule line and notes, so the page shows
 # what a Japanese player really sees. NO DEPARTURE: the ja card's own citation
 # is SRD p. 11, the same page the English page prints.
 # The headword stays English on purpose — see the head comment. Mapped to
 # itself so the key set still matches the German file; build.py skips it.
 '<div class="hw">Dim Light</div>': '<div class="hw">Dim Light</div>',
 "“Past the torch's ring the corridor goes grey rather than black, and the ranger squints into it and is not sure what she saw.”":
   "「松明の輪の先で廊下は黒ではなく灰色になり、レンジャーは目を細めますが、何を見たのか確信が持てません。」",
 "Dusk and shadow: sight-based Perception suffers, and Darkvision sees the dark as this.":
   "夕暮れと影です。視覚による〈知覚〉が損なわれ、暗視は暗闇をこれとして見ます。",
 "Shadow: creates a Lightly Obscured area": "影です。軽度の隠蔽の区域を作ります",
 "term | the border between bright and dark<br>usually the outer band of a light source · SRD p. 11":
   "用語 | 明るい光と暗闇の境目<br>ふつうは光源の外側の帯です · SRD p. 11",

 # ---- what each part is for: whole <li> each, so no English article survives ----
 "<li><b>The term</b><span>What the table will actually say out loud. This is the answer you are drilled to produce.</span></li>":
   "<li><b>用語</b><span>卓で実際に声に出して言われることば。反復して出せるようにする、その答えです。</span></li>",
 "<li><b>The scene</b><span>That rule happening at a table. You remember a picture, and the picture carries the rule with it.</span></li>":
   "<li><b>場面</b><span>その規則が卓で起きているところ。覚えるのは絵で、その絵が規則を一緒に運んできます。</span></li>",
 "<li><b>The definition</b><span>The meaning you are tested on — short enough to hold, complete enough to rule with.</span></li>":
   "<li><b>定義</b><span>出題される意味 — 覚えておける短さで、裁定に足りる過不足なさで。</span></li>",
 "<li><b>The rule line</b><span>The rule as you would say it to a player, in one breath.</span></li>":
   "<li><b>規則の一行</b><span>プレイヤーに言うときのままの規則を、ひと息で。</span></li>",
 "<li><b>The numbers</b><span>The category, the figures underneath, and the page of the reference document it comes from.</span></li>":
   "<li><b>数字</b><span>分類、その下の数値、そして出典となるリファレンス文書のページ。</span></li>",
 "A key turns that notes line into a map of all 24 card categories, and a second converts every distance and weight on the cards. Both ship inside the game, as do the English and German reference documents.":
   "キーをひとつ押せば、そのノート行が24あるカード分類すべての一覧に変わります。もうひとつのキーは、カード上の距離と重量をすべて換算します。どちらもゲームに同梱されていて、英語とドイツ語のリファレンス文書も同じく入っています。",

 # ---- the editions ----
 '<span class="tag">Languages</span>': '<span class="tag">言語</span>',
 "<h2>Which edition you get</h2>": "<h2>どの版が手に入るか</h2>",
 "This pack is more honest about its languages than most, because they are genuinely not all the same thing. Three kinds:":
   "このパックは、言語について多くのパックより正直です。本当に、どれも同じものではないからです。3種類あります：",
 '<div class="h">German<span class="badge">Complete</span></div>':
   '<div class="h">ドイツ語<span class="badge">完全版</span></div>',
 "<b>A full German edition.</b> Everything in German — headword, definition, rule line, scene and notes on all 1,205 cards, and all 62 reference lessons. It uses the established German rules vocabulary, <i>Rüstungsklasse</i>, <i>Trefferpunkte</i>, <i>Rettungswurf</i>, rather than invented calques, and it cites the German rules edition page by page, so a card sends you to the right page of the book you actually own.":
   "<b>完全なドイツ語版です。</b>すべてドイツ語 — 1,205枚すべてのカードの見出し語、定義、規則の一行、場面、ノート、そして62本のリファレンスレッスンすべて。<i>Rüstungsklasse</i>、<i>Trefferpunkte</i>、<i>Rettungswurf</i>という定着したドイツ語の規則用語を使い、造語の直訳は使いません。ドイツ語版の規則書をページ単位で引くので、カードは実際に手元にある本の正しいページへ送ってくれます。",
 '<div class="h">Japanese · Simplified Chinese · Russian · Spanish<span class="badge">Play in yours, answer in English</span></div>':
   '<div class="h">日本語 · 簡体字中国語 · ロシア語 · スペイン語<span class="badge">自分の言語で進み、英語で答える</span></div>',
 "The question and the scene are in your language; the headword you answer with, and the word you hear, are <b>English</b>. A toggle on the card shows the translation whenever you want it, and the 62 reference lessons are written in your language too.":
   "問いと場面はあなたの言語で。答えとなる見出し語と、耳で聞く語は<b>英語</b>です。カード上の切り替えでいつでも訳文を表示でき、62本のリファレンスレッスンもあなたの言語で書かれています。",
 "<b>That is deliberate, not a shortcut.</b> You meet each rule in words you already think in, and you leave holding the term the table will actually use. It is the step you need before you sit down at an English-speaking game.":
   "<b>これは手抜きではなく、意図したつくりです。</b>ひとつひとつの規則に、すでに自分が考えている言葉で出会い、卓で実際に使われる用語を手に持って出ていきます。英語で遊ぶ卓に着く前に、必要な一歩です。",
 '<div class="h">The all-in-your-language bonus<span class="badge">Beta</span></div>':
   '<div class="h">全文あなたの言語のボーナス版<span class="badge">ベータ</span></div>',
 "If you would rather have the whole card in Japanese, Simplified Chinese, Russian or Spanish, that edition is there as well. It comes with compromises, stated plainly: <b>the spoken word stays English</b>, there is no audio beyond it, and it carries <b>no revision drills</b>. A bonus, not a course in its own right — you already speak your own language.":
   "カード全体を日本語・簡体字中国語・ロシア語・スペイン語で読みたい方には、その版もあります。妥協点ははっきり書いておきます：<b>読み上げられる語は英語のまま</b>、それ以外の音声はなく、<b>復習ドリルもありません</b>。独立したコースではなくボーナスです — 自分の言語は、もう話せるのですから。",

 # ---- the tiers: whole <li> each ----
 ">The climb<": ">登り<",
 "<h2>Five tiers, each ending in something you can do</h2>":
   "<h2>5つのティア、それぞれ「できること」で終わります</h2>",
 '<li><span class="w">Adjudicate a check</span><span class="d">The die, the DC, what the number is meant to mean, and the conditions that change it.</span></li>':
   '<li><span class="w">判定を裁定する</span><span class="d">ダイス、DC、その数字が意味するところ、そしてそれを変える状態。</span></li>',
 '<li><span class="w">Run a fight</span><span class="d">The turn, the actions in it, the damage types, and what a condition does to whoever is carrying it.</span></li>':
   '<li><span class="w">戦闘を回す</span><span class="d">手番、その中のアクション、ダメージ種別、そして状態が、それを負った者に何をするか。</span></li>',
 '<li><span class="w">Run a caster and read a stat block</span><span class="d">Slots, concentration, ranges — and a block of numbers you can look at and know what it will do.</span></li>':
   '<li><span class="w">術者を回し、ステータスブロックを読む</span><span class="d">呪文スロット、精神集中、射程 — そして、ひと目で何が起きるか分かる数字のかたまり。</span></li>',
 '<li><span class="w">Know what the options bring</span><span class="d">The twelve classes, the nine species, and what the feats actually give a character.</span></li>':
   '<li><span class="w">選択肢が何をもたらすか知る</span><span class="d">12のクラス、9の種族、そして特技がキャラクターに実際に与えるもの。</span></li>',
 '<li><span class="w">Build encounters, hazards and treasure</span><span class="d">Challenge rating against experience, what a party survives, and what to hand out afterwards.</span></li>':
   '<li><span class="w">遭遇、危険、宝物を組み立てる</span><span class="d">脅威度と経験点の釣り合い、パーティが生き延びられる範囲、そして終わったあとに何を渡すか。</span></li>',
 "62 reference lessons, 82 pages, one waiting at the head of every cluster — in every language the pack ships.":
   "62本のリファレンスレッスン、82ページ。どのクラスターの冒頭にも1本ずつ待っています — このパックが出ているすべての言語で。",

 # ---- the method: whole <dt>+<dd> each ----
 ">How it sticks<": ">定着のしくみ<",
 "<h2>Flashcards as an integrated system</h2>": "<h2>統合システムとしてのフラッシュカード</h2>",
 "<dt>Cards</dt><dd><b>1,205 cards in 62 themed clusters</b> across five tiers, every one carrying its term, its scene, its definition, its rule line and its numbers.</dd>":
   "<dt>カード</dt><dd><b>62のテーマ別クラスターに1,205枚</b>、5つのティアにまたがります。どの1枚も、用語、場面、定義、規則の一行、数字を載せています。</dd>",
 "<dt>Boss fights</dt><dd>Three kinds, not one: <b>name the creature, spell or term</b> from its definition; <b>give your ruling</b> on a scene; <b>read the number</b> off a table. No cluster is cleared until its definitions are mastered.</dd>":
   "<dt>ボス戦</dt><dd>1種類ではなく3種類：定義から<b>怪物・呪文・用語を言い当てる</b>、場面に<b>裁定を下す</b>、表から<b>数字を読む</b>。定義をものにするまで、クラスターは攻略できません。</dd>",
 "<dt>Lessons</dt><dd><b>62 reference lessons, 82 pages</b> — one at the head of every cluster, in every language the pack ships.</dd>":
   "<dt>レッスン</dt><dd><b>62本のリファレンスレッスン、82ページ</b> — どのクラスターの冒頭にも1本ずつ、このパックが出ているすべての言語で。</dd>",
 "<dt>Fibonacci SRS</dt><dd>Rate each card 0–5. The better you know a rule, the longer before it comes back.</dd>":
   "<dt>フィボナッチSRS</dt><dd>各カードを0〜5で評価。よく知っている規則ほど、戻ってくるまでが長くなります。</dd>",
 '<dt>Audio</dt><dd>The Guide reads aloud in its own bundled voice. Samples are on the <a href="voices.html">voices page</a>.</dd>':
   '<dt>音声</dt><dd>The Guideは専用の同梱音声で読み上げます。サンプルは<a href="voices.html">音声ページ</a>にあります。</dd>',
 "<dt>The ruleset</dt><dd>The <b>2024 revision</b> as it now stands — the terms, the numbers and the procedures expected today. If your rules knowledge is a decade old, you relearn what changed by drilling what is, rather than reading a list of differences.</dd>":
   "<dt>規則の版</dt><dd>いま現在の<b>2024年改訂版</b> — 今日求められる用語、数字、手順です。規則の知識が10年前のものなら、差分の一覧を読むのではなく、いま通用するものを反復することで、変わった点を学び直せます。</dd>",

 # ---- the FAQ ----
 ">Questions<": ">質問<",
 "<h2>Before you buy</h2>": "<h2>購入の前に</h2>",
 "<summary>Which edition of the rules is this?</summary>":
   "<summary>これはどの版の規則ですか？</summary>",
 "The <b>2024 revision</b>, built from the System Reference Document 5.2. Conditions, spells, species and stat blocks were revised between the 2014 rules and these, so if your table runs the older edition some of these cards will drill you on numbers you do not use. Check which one your table plays before you buy.":
   "<b>2024年改訂版</b>で、System Reference Document 5.2に基づいています。状態、呪文、種族、ステータスブロックは、2014年の規則からこの版のあいだで改訂されました。卓が古い版で遊んでいるなら、使わない数字を反復させるカードも出てきます。購入の前に、卓がどちらで遊んでいるか確かめてください。",
 "<summary>Do I need the base game?</summary>": "<summary>基本ゲームは必要ですか？</summary>",
 'Yes. The Guide is DLC for FlashBoss, so you need the base game as well. On Windows 10 you also need <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a>, a free download from the Microsoft Store.':
   'はい。The GuideはFlashBossのDLCなので、基本ゲームも必要です。Windows 10では<a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a>も必要です。Microsoft Storeから無料で手に入ります。',
 "<summary>I am a player, not a game master. Is it for me?</summary>":
   "<summary>ゲームマスターではなくプレイヤーです。自分にも向いていますか？</summary>",
 "It is built for the person running the table, and that is where it pays most. A player who wants to stop asking what a condition does, or who is about to run their first game, gets the same cards — the tiers just matter less in that order.":
   "卓を回す人のために作られていて、いちばん効くのもそこです。状態が何をするのかを訊かずに済ませたいプレイヤーや、はじめて卓を回そうとしている人にも、同じカードが届きます — ただ、その場合はティアの順番の重みが下がるだけです。",
 "<summary>Is my language a full edition or a mixed one?</summary>":
   "<summary>自分の言語は完全版ですか、混成版ですか？</summary>",
 'German is the full edition. <b>Japanese, Simplified Chinese, Russian and Spanish</b> play in your language and answer in English, with a toggle to the translation on the card and the lessons written in your language — and each also carries an all-in-your-language bonus edition in beta, with English audio and no drills. The <a href="#editions">languages section</a> above says exactly what each one gives you.':
   'ドイツ語が完全版です。<b>日本語、簡体字中国語、ロシア語、スペイン語</b>はあなたの言語で進み、答えは英語です。カード上には訳文への切り替えがあり、レッスンもあなたの言語で書かれています — さらにそれぞれに、全文あなたの言語のボーナス版がベータとして付きます。こちらは音声が英語で、ドリルはありません。上の<a href="#editions">言語のセクション</a>に、どれが何をくれるか正確に書いてあります。',
 "<summary>Can I see the cards before I buy?</summary>":
   "<summary>購入の前にカードを見られますか？</summary>",
 'The card lists and reference lessons for FlashBoss packs are on this site, free and printable, and there is a <a href="https://flashboss-demo.pages.dev/">playable boss fight</a> if you want to see the mechanic before anything else.':
   'FlashBossパックのカードリストとリファレンスレッスンは、このサイトに無料で置いてあり、印刷もできます。先に仕組みを見たい方には、<a href="https://flashboss-demo.pages.dev/">遊べるボス戦</a>もあります。',

 # ---- the close ----
 "<h2>Know it, don't look it up.</h2>": "<h2>調べるのではなく、知っていること。</h2>",
 "1,205 cards, 62 clusters, and a boss fight at every one of them.":
   "カード1,205枚、62クラスター、そのすべてにボス戦。",
 "The Guide on Steam &rarr;": "SteamでThe Guideを手に入れる &rarr;",

 # ---- the legal line: translated in full, all three prongs, nothing softened ----
 "5E compatible. Built from the System Reference Document 5.2. FlashBoss is not affiliated with, endorsed by, or sponsored by any rules publisher.":
   "5E対応。System Reference Document 5.2に基づいています。FlashBossは、いかなる規則の出版元とも提携しておらず、その承認も後援も受けていません。",
}

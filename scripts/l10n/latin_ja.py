# Japanese strings for latin.html — the Latin LANGUAGE COURSE page
# (Latin Core + Latin Pareto), not the Latin Roots English pack.
#
# Key set and key order are latin_de.py's, the worked example for this page.
#
# Canon sentences are LIFTED wherever a ratified or already-published source
# has them: the Japanese Latin bundle sheet
# (flashboss-admin/BUNDLE_COPY_LATIN_2026-09-08.md) supplies the bundle name
# "FlashBoss ラテン語 — コンプリートコース"; french.ja.html is this same page
# template already translated by the fleet, so its wording owns the shared
# furniture — 聞く・読む・繰り返す・評価する・戦う, 全体図, 見ただけで分かる,
# タップでめくる, なぜ定着するのか, 単語カードを、ひとつの仕組みに,
# フィボナッチ間隔反復, 卒業, あなたの言語, よくある質問, the boss-fight,
# graduation, Windows-Terminal and demo answers, and the hero alt.
#
# CLUSTER NAMES ARE NOT MINE. Every one of the eighty comes from
# clusters_latin_ja.txt, i.e. from cluster_names_ja.json in the packs — the
# words the player actually sees in the game. None coined here.
#
# Pack names stay English: Latin Core, Latin Pareto, Core, Pareto. FlashBoss
# stays Latin script. "Latin Pareto" is the store name — never "Pareto 1".
# Latin itself is never translated: the example sentences, the dictionary
# forms, the sigla (Caes. BG 5.44.5) and the epigraph stand byte-identical.
# Numbers are the English page's own; ja writes the same comma, so nothing
# moves. The page was recounted on 2026-09-19 and beats the bundle sheet where
# they disagree — 26 Core lessons, 18 Pareto, 44 in all.
#
# Register: です／ます, no keigo inflation, no exclamation marks. Terms are the
# ones the live ja pages already use: ティア, クラスター, ボス戦, 参照レッスン,
# 見出し語, 基本ゲーム, 単語リスト, 攻略ガイド（β）. NO SPACES around
# Latin-script words inside a Japanese sentence, and 、 rather than an ASCII
# comma between example pairs — both are what the live ja pages do.
TITLE = "ラテン語 — FlashBoss"
DESCRIPTION = ("FlashBossのラテン語：10ティア・80クラスターで2,000語を読む読解コース。"
               "参照レッスン44本、マクロン付きの見出し語、そして最後は手を加えていない"
               "カエサル、キケロ、サッルスティウス、ネポス、リウィウスで終わる例文。"
               "Latin CoreとLatin Pareto、Steamで発売中。")

STRINGS = {
 # ---- nav / chrome ----
 ">home<": ">ホーム<",
 ">packs<": ">パック<",
 ">resources<": ">リソース<",
 ">walkthrough (beta)<": ">攻略ガイド（β）<",
 # the live ja language pages keep the English name here (French, German,
 # Italian); the page's own title is Japanese, so this follows the title.
 '<span class="here">Latin</span>': '<span class="here">ラテン語</span>',

 # ---- hero ----
 "FlashBoss — the moonlit school that fronts every FlashBoss course":
   "FlashBoss — すべてのコースの顔である月夜の学び舎",
 "Two packs · <b>2,000 words</b> · ten tiers · 44 lessons · out now on Steam":
   "2パック · <b>2,000語</b> · 10ティア · レッスン44本 · Steamで発売中",
 "Read real Latin. Not books about it.":
   "本物のラテン語を読む。ラテン語について書かれた本ではなく。",
 "Listen · Read · Repeat · Rate · Fight": "聞く・読む・繰り返す・評価する・戦う",
 "Two thousand words, ten tiers, one skill. The sentences start built for you and end as <b>Caesar, Cicero, Sallust, Nepos and Livy actually wrote them</b> — nothing trimmed but length, nothing invented.":
   "2,000語、10ティア、ひとつの技能。例文はあなたのために組まれた文から始まり、最後は<b>カエサル、キケロ、サッルスティウス、ネポス、リウィウスが実際に書いたとおりの文</b>になります — 削ったのは長さだけ、作り足したものはありません。",
 ">Word Lists<": ">単語リスト<",
 ">Lessons<": ">レッスン<",
 ">Try the demo<": ">デモを試す<",

 # ---- the argument: one skill, and the order that teaches it ----
 "Latin course design": "ラテン語コースの設計",
 "One skill: reading": "ひとつの技能：読むこと",
 "Legendō discitur — it is learned by reading.":
   "Legendō discitur — 読むことによって学ばれる。",
 "Nothing here asks you to compose Latin of your own. The whole course is built so that you can look at a printed line and know what it says — and it gets you there by putting you in front of sentences from the very first tier, not by making you wait until the grammar is finished.":
   "ここでは、自分でラテン語を作文することは求められません。このコースはすべて、印刷された一行を見て、それが何を言っているか分かるようになるために組まれています — しかもそこへは、文法が終わるまで待たせるのではなく、最初のティアから例文の前に立たせることで連れていきます。",
 "The order is the argument. Two thousand lemmas are laid down in ten tiers, each tier eight clusters of twenty-five cards, and the grammar arrives one lesson at a time at the exact card that first needs it. No example sentence ever uses grammar you have not been taught. By Tier 10 the ladder has nothing left to teach and you are reading Cicero unadapted — <b>17,007 words of Latin read in context</b> along the way.":
   "順序こそが論拠です。2,000の見出し語が10のティアに置かれ、どのティアも25枚ずつのクラスターが8つ。文法は、それを最初に必要とするカードのところへ、レッスン1本ずつ届きます。まだ習っていない文法を使う例文は、ひとつもありません。ティア10でははしごに教えることが残っておらず、あなたはキケロを原文のまま読んでいます — その道中で、<b>文脈の中の17,007語のラテン語</b>を読むことになります。",

 "Latin Core — tiers 1 to 5": "Latin Core — ティア1〜5",
 "Latin Pareto — tiers 6 to 10": "Latin Pareto — ティア6〜10",
 "The alphabet as Rome said it, the pointing words, the connectives, the prime movers, the first nouns of senate and sword.":
   "ローマが発音したとおりのアルファベット、指し示す語、つなぎの語、第一の動者、元老院と剣の最初の名詞。",
 "The accusative, the present tense, the imperative. The daily round, the forum, the body, counting and worth.":
   "対格、現在時制、命令法。日々の巡り、フォルム、体、数えることと値打ち。",
 "Genitive and dative, the full plural, two more conjugations, the imperfect. The road, the household, the turning year.":
   "属格と与格、複数形のすべて、さらに2つの活用、未完了過去。道、家、巡る年。",
 "The ablative, the third declension, prepositions and case — and the first real Caesar, lightly adapted.":
   "奪格、第三変化、前置詞と格 — そして最初の本物のカエサル、わずかに手を加えたもの。",
 "The perfect and its family, principal parts, relative clauses. Caesar is now on 86 of the 200 cards, and unadapted on 26 of them.":
   "完了とその一族、主要形、関係節。カエサルは200枚のうち86枚に載り、うち26枚は原文のままです。",
 "Participles, all three of them, and the passive. Caesar continues, and Nepos comes into his own.":
   "分詞、3つすべて、そして受動態。カエサルは続き、ネポスが本領を現します。",
 "The ablative absolute, the passive complete, deponents. Cicero's letters open the informal register.":
   "絶対奪格、受動態の完成、異態動詞。キケロの書簡が、くだけた語法の扉を開きます。",
 "The infinitive family and reported speech. Sallust arrives; 192 of 200 cards are now unadapted.":
   "不定法の一族と間接話法。サッルスティウスが加わり、200枚のうち192枚が原文のままになります。",
 "The subjunctive, cum-clauses, purpose and result, indirect questions. Livy joins the roll.":
   "接続法、cum節、目的と結果、間接疑問。リウィウスが名簿に加わります。",
 "Gerund and gerundive, and how to read a citation. Cicero's speeches and philosophy close the trunk.":
   "動名詞と動形容詞、そして出典の読み方。キケロの弁論と哲学が幹を締めくくります。",

 # ---- the sentence ladder: Latin stays Latin, the gloss becomes Japanese ----
 "Watch it grow up": "育っていく例文",
 "From made for you to written by Cicero": "「あなたのために作った文」から「キケロが書いた文」へ",
 "One card's example sentence from each of the ten tiers, in order. Nothing below is a paraphrase: from Tier 4 the citations are real, and the unmarked ones are the author's own words.":
   "10のティアそれぞれから、カード1枚分の例文を順に並べました。以下に言い換えはひとつもありません。ティア4からは出典が実在し、印のないものは著者自身のことばです。",
 '<span class="en">As you see, Caesar is one of ours.</span>':
   '<span class="en">ご覧のとおり、カエサルは我々の側の人です。</span>',
 '<span class="en">While Caesar is in Gaul, the senate approves the law.</span>':
   '<span class="en">カエサルがガリアにいるあいだに、元老院は法を承認します。</span>',
 '<span class="en">Our troops were already departing and abandoning the camp.</span>':
   '<span class="en">我らの軍はすでに出発し、陣営を後にしつつありました。</span>',
 '<span class="en">The storms both kept our men in camp and held the enemy back from battle.</span>':
   '<span class="en">嵐は我らの兵を陣中にとどめ、同時に敵を戦いから遠ざけていました。</span>',
 '<span class="en">There he reached the furthest ridge and drew up his line in that place.</span>':
   '<span class="en">そこで彼は最も奥の尾根に達し、その場所に戦列を敷きました。</span>',
 '<span class="en">Not even Vorenus keeps himself behind the rampart then; fearing what everyone would think, he follows after.</span>':
   '<span class="en">そのときウォレヌスでさえ、塁の内にとどまってはいません。皆がどう思うかを恐れて、あとに続きます。</span>',
 '<span class="en">All the ties of the closest friendship hold between him and me.</span>':
   '<span class="en">この上なく親しい間柄の絆が、すべて彼と私のあいだにあります。</span>',
 '<span class="en">At home we have want, abroad debt, a bad case and a prospect much harsher still.</span>':
   '<span class="en">内には欠乏、外には負債、事情は悪く、見通しはさらに厳しいものです。</span>',
 '<span class="en">Seeing his forces routed and himself left with a few, mindful of his birth and former standing, Catiline charges into the thickest of the enemy and there, fighting, is run through.</span>':
   '<span class="en">自軍が潰走し、自分がわずかな者と取り残されたのを見て、カティリナは家柄とかつての威信を思い、敵のもっとも密集したところへ突き入り、そこで戦いながら刺し貫かれます。</span>',
 '<span class="en">You see that man with the rather curly hair, the dark one, who watches us with a look that makes him seem very sharp to himself.</span>':
   '<span class="en">あの少し縮れ毛の、浅黒い男が見えるでしょう。自分をひどく切れ者だと思っているような顔つきで、こちらを見ている男です。</span>',
 ">built for the tier<": ">ティアのために作った文<",
 ">adapted from Caes. BG 4.34.4<": ">Caes. BG 4.34.4より改変<",

 # ---- whose Latin: the source arc ----
 "Whose Latin": "誰のラテン語か",
 "The authors arrive in order": "著者は順に登場します",
 "Tiers 1 to 3 have no citations at all, and say so: those sentences are built to a grammar ceiling, because real Latin has no register that simple. Caesar enters at Tier 4 and the scaffolding is gone by Tier 8.":
   "ティア1から3には出典がまったくなく、そのことを明記しています。これらの文は文法の上限に合わせて組まれたものです。本物のラテン語には、それほど単純な語法の層が存在しないからです。カエサルはティア4で登場し、ティア8までに足場は取り払われます。",
 ">Tiers 1–3<": ">ティア1〜3<",
 "Sentences constructed to the tier's grammar — no author claimed, none implied":
   "そのティアの文法に合わせて組んだ文 — 著者を名乗らず、におわせもしません",
 ">0 of 600 cited<": ">600枚中、出典0<",
 "Caesar, <i>Gallic War</i> — mostly clause-trimmed for length":
   "カエサル、<i>ガリア戦記</i> — 多くは長さのために節を刈り込んでいます",
 ">62 cited · 13 unadapted<": ">出典62 · 原文のまま13<",
 "Caesar throughout, Nepos beginning": "全体にカエサル、ネポスが始まります",
 ">86 cited · 26 unadapted<": ">出典86 · 原文のまま26<",
 "Caesar and Nepos, <i>Lives</i>": "カエサルとネポス、<i>英雄伝</i>",
 ">145 cited · 84 unadapted<": ">出典145 · 原文のまま84<",
 "Cicero's letters — <i>ad Atticum</i>, <i>ad Familiares</i> — beside Caesar and Nepos":
   "キケロの書簡 — <i>ad Atticum</i>、<i>ad Familiares</i> — がカエサルとネポスに並びます",
 ">170 cited · 109 unadapted<": ">出典170 · 原文のまま109<",
 "Sallust joins; the adapting effectively stops":
   "サッルスティウスが加わり、改変は事実上なくなります",
 ">196 cited · 192 unadapted<": ">出典196 · 原文のまま192<",
 "Livy Book 1 joins Sallust, Cicero and Caesar":
   "リウィウス第1巻が、サッルスティウス、キケロ、カエサルに加わります",
 ">197 cited · 195 unadapted<": ">出典197 · 原文のまま195<",
 "Cicero's speeches and philosophy — the hardest band the trunk reaches":
   "キケロの弁論と哲学 — 幹が届くうちで最も難しい帯域",
 ">196 cited · 194 unadapted<": ">出典196 · 原文のまま194<",
 "Across the two packs, <b>1,052 of the 2,000 example sentences carry a citation</b>, and 813 of those are the author's own unaltered words. Every citation on every card names its book, chapter and section, and Lesson 41 teaches you how to read one.":
   "2つのパック全体で、<b>2,000の例文のうち1,052に出典が付いています</b>。そのうち813は、著者自身の手を加えていないことばです。どのカードの出典も、巻・章・節を示します。その読み方はレッスン41が教えます。",

 # ---- the tier and cluster ledger ----
 # Every cluster name below comes from cluster_names_ja.json in the packs, not
 # from this translator's ear: the player sees these words in the game.
 "The whole map": "全体図",
 "Ten tiers, eighty clusters": "10ティア、80クラスター",
 "Every cluster is 25 cards and ends in a boss fight. Nothing is hidden — the full list is on the <a href=\"wordlists.html?lang=Latin&amp;set=Core\">word lists page</a>, free to read before you buy.":
   "どのクラスターも25枚、最後はボス戦です。隠しごとはありません — 全リストは<a href=\"wordlists.html?lang=Latin&amp;set=Core\">単語リストのページ</a>にあり、購入前に無料で読めます。",
 ">Tier 1<": ">ティア1<",
 ">Tier 2<": ">ティア2<",
 ">Tier 3<": ">ティア3<",
 ">Tier 4<": ">ティア4<",
 ">Tier 5<": ">ティア5<",
 ">Tier 6<": ">ティア6<",
 ">Tier 7<": ">ティア7<",
 ">Tier 8<": ">ティア8<",
 ">Tier 9<": ">ティア9<",
 ">Tier 10<": ">ティア10<",
 "The Pointing Words · The Joints · The Links · The Prime Movers · Senate &amp; Sword · Many &amp; Mighty · The Lay of Things · The Marshalling":
   "指し示す語 · 継ぎ目 · つなぎ · 第一の動者 · 元老院と剣 · 多くと強き · 物のありよう · 布陣",
 "The Daily Round · Arms &amp; the Man · The Forum · Flesh &amp; Breath · Tally &amp; Measure · Worth &amp; Honor · Time &amp; Tide · The Rally":
   "日々の巡り · 武器と人 · フォルム · 肉と息 · 数と量 · 値と誉れ · 時と潮 · 再集結",
 "To &amp; Fro · The Long Road · Flesh &amp; Frame · The Fathers · House &amp; Hearth · Hopes &amp; Fears · The Turning Year · The Waystation":
   "行きつ戻りつ · 長き道 · 肉と骨組み · 父祖 · 家と炉 · 望みと恐れ · 巡る年 · 宿駅",
 "Moods &amp; Moments · The Turning Hand · The Living Frame · The Curia · By Land &amp; Sea · More &amp; Most · The Winter Camp · The Muster Roll":
   "気分と瞬間 · 転じる手 · 生ける体 · クリア · 陸と海より · より多くと最も · 冬営 · 名簿",
 "What Was Done · The Perfect Stems · The Pitched Battle · The Work in Hand · Life &amp; Limb · Praise &amp; Blame · The Appointed Hour · The Full Account":
   "成されしこと · 完了の語幹 · 会戦 · 手中の業 · 命と体 · 誉と咎 · 定めの刻 · 全き記述",
 "The Life of the Mind · Hours &amp; Days · A Soldier&#x27;s Life · The Full Tally · The Family Estate · The Mortal Frame · Treaties &amp; Powers · The Loose Ends":
   "精神の営み · 時と日 · 兵士の暮らし · 全き数え · 家の財産 · 死すべき身 · 条約と権力 · ほつれた端",
 "Comings &amp; Partings · The Ready Hand · The Head Count · Wounds &amp; Toil · Kin &amp; Neighbor · Rank &amp; Office · The Sea Road · The Middle Way":
   "出会いと別れ · 疾き手 · 頭数 · 傷と労苦 · 親族と隣人 · 位と官職 · 海の道 · 中道",
 "True &amp; False · The Bidding · Sound &amp; Sick · Weight &amp; Worth · The Present Hour · The Tide of Battle · The Household Store · The Last Ditch":
   "真と偽 · 下す命 · 健と病 · 重さと価 · 今の刻 · 戦の潮目 · 家の蓄え · 最後の防塁",
 "Hopes &amp; Vows · By the Numbers · Right &amp; Wrong · The Broken Line · Dust &amp; Ashes · The Sacred Rites · Fraud &amp; Force · What Remains":
   "望みと誓い · 数に照らして · 是と非 · 崩れた陣列 · 塵と灰 · 聖なる祭儀 · 偽りと暴力 · 残りしもの",
 "The Open Book · The Final Battle · Blood &amp; Bone · Honor &amp; Shame · Envoys &amp; Treaties · Hearth &amp; Heir · The Last Measure · The Closing Page":
   "開かれた書 · 最後の戦い · 血と骨 · 誉れと恥 · 使節と条約 · 炉と世継ぎ · 最後の計り · 結びの頁",
 ">8 clusters · 200 cards<": ">8クラスター · 200枚<",
 "<span>Core: 5 tiers · 40 clusters · <b>1,000 cards</b></span><span>26 reference lessons</span><span>the reading foundation</span>":
   "<span>Core：5ティア · 40クラスター · <b>1,000枚</b></span><span>参照レッスン26本</span><span>読みの土台</span>",
 "<span>Pareto: 5 tiers · 40 clusters · <b>1,000 cards</b></span><span>18 reference lessons</span><span>the trunk complete</span>":
   "<span>Pareto：5ティア · 40クラスター · <b>1,000枚</b></span><span>参照レッスン18本</span><span>幹の完成</span>",

 # ---- the card: the macron ----
 "Read it by sight": "見ただけで分かる",
 "The macron is data, not decoration": "マクロンは飾りではなく、情報です",
 "Every headword is printed as a dictionary prints it — long vowels marked, gender and genitive stem for a noun, conjugation for a verb. 1,320 of the 2,000 headwords carry a macron. Tap a card to flip it.":
   "見出し語はすべて、辞書が印刷するとおりに出ます — 長母音には印、名詞には性と属格の語幹、動詞には活用。2,000の見出し語のうち1,320にマクロンが付きます。カードをタップするとめくれます。",
 # the Latin dictionary shorthand stands as it is printed, in every locale
 ">f., -is<": ">f., -is<",
 '''courage, manliness; virtue — &ldquo;Roman courage is great.&rdquo;<span class="nb">noun | gen sg virtūtis — the stem is virtūt-
long ū: vir-tūs
From vir &lsquo;man&rsquo;: the quality of a man.</span>''':
   '''勇気、雄々しさ、徳 — &ldquo;ローマの勇気は大きい。&rdquo;<span class="nb">名詞｜属格単数virtūtis — 語幹はvirtūt-
長いū：vir-tūs
vir&lsquo;男&rsquo;から。男に備わる性質のこと。</span>''',
 '''make, do — &ldquo;We are doing the same thing.&rdquo;<span class="nb">verb | 1st pl facimus = &lsquo;we make, we do&rsquo;
long ō: fa-ci-ō; a and i stay short
idem = &lsquo;the same thing&rsquo; (object role)</span>''':
   '''作る、行う — &ldquo;私たちは同じことをしています。&rdquo;<span class="nb">動詞｜1人称複数facimus = &lsquo;私たちは作る、行う&rsquo;
長いō：fa-ci-ō。aとiは短いまま
idem = &lsquo;同じもの&rsquo;（目的語の役割）</span>''',
 '''evil, misfortune — &ldquo;The state sees the shared misfortune.&rdquo;<span class="nb">noun | acc sg malum = nom sg in form
no macron: ma-lum, both vowels short
mālum, with a long ā, is an apple.</span>''':
   '''悪、災い — &ldquo;国家は共通の災いを見ています。&rdquo;<span class="nb">名詞｜対格単数malum = 形は主格単数と同じ
マクロンなし：ma-lum、母音はどちらも短い
mālumは長いāで、りんごのこと。</span>''',
 ">tap to flip<": ">タップでめくる<",

 # ---- the two minimal pairs ----
 ">Tier 1 · Tier 3<": ">ティア1 · ティア3<",
 ">Tier 10 · Tier 4<": ">ティア10 · ティア4<",
 "<b>this one</b> against <b>here</b>. One letter apart in print, and the line over the vowel is the only thing that separates them.":
   "<b>これ</b>と<b>ここ</b>。印刷では一文字の違いで、母音の上の線だけが二つを分けています。",
 "<b>bone</b> against <b>mouth</b>. Same three letters, same neuter third declension, six tiers apart — and the card that teaches the second one says so.":
   "<b>骨</b>と<b>口</b>。同じ三文字、同じ中性第三変化で、ティアは六つ離れています — そして二つめを教えるカードが、そのことを書いています。",
 "The macrons stop at the headword. Example sentences are printed unmarked, the way every real Latin text you will ever open is printed — so what you practise reading is the thing itself, not a teaching aid. The card tells you the vowel length; the sentence makes you carry it.":
   "マクロンは見出し語で止まります。例文は印を付けずに組まれています。これから開く本物のラテン語の本が、すべてそう印刷されているからです — だから読む練習の相手は、教材ではなく実物そのものです。母音の長さはカードが教え、それを担わせるのは文の役目です。",

 # ---- reference lessons ----
 "Not just a word list": "単語リストでは終わらない",
 "Forty-four lessons, fired in sequence": "44のレッスンが、順に発火する",
 "A reference lesson unlocks at the exact card where you first need it, and stays available afterwards. Core's twenty-six and Pareto's eighteen are all free to read on the <a href=\"lessons.html?lang=Latin\">lessons page</a>.":
   "参照レッスンは、それが必要になるちょうどそのカードで解錠され、以後はいつでも読み返せます。Coreの26本とParetoの18本は、すべて<a href=\"lessons.html?lang=Latin\">レッスンのページ</a>で無料で読めます。",

 # whole <li> each, so no English article is stranded in front of a Japanese noun
 '<li><span class="no">01</span>Welcome to Latin<span class="d">The four letters an English reader gets wrong — c, g, v, qu — in the restored sounds, and what a macron is for.</span></li>':
   '<li><span class="no">01</span>ラテン語へようこそ<span class="d">英語の読み手が読み違える四つの文字 — c、g、v、qu — を復元音で。そしてマクロンは何のためにあるのか。</span></li>',
 '<li><span class="no">10</span>The accusative<span class="d">The first case that changes what a sentence means, met on the card that first needs it.</span></li>':
   '<li><span class="no">10</span>対格<span class="d">文の意味を変える最初の格を、それを最初に必要とするカードの上で。</span></li>',
 '<li><span class="no">14</span>Genitive and dative<span class="d">Of and to, and why the genitive singular is printed on every noun card.</span></li>':
   '<li><span class="no">14</span>属格と与格<span class="d">「〜の」と「〜に」、そしてなぜ属格単数がすべての名詞カードに印刷されているのか。</span></li>',
 '<li><span class="no">18</span>The ablative<span class="d">The case English has no name for, and the six jobs it does.</span></li>':
   '<li><span class="no">18</span>奪格<span class="d">英語に名前のない格と、それが担う六つの仕事。</span></li>',
 '<li><span class="no">23</span>Principal parts<span class="d">Why a Latin verb is quoted four ways, and how to get from any of them to the rest.</span></li>':
   '<li><span class="no">23</span>主要形<span class="d">ラテン語の動詞がなぜ四つの形で示されるのか、そしてどの形からでも残りへ辿り着く方法。</span></li>',
 '<li><span class="no">30</span>The ablative absolute<span class="d">The construction that makes Caesar readable at speed.</span></li>':
   '<li><span class="no">30</span>絶対奪格<span class="d">カエサルを速さのまま読めるようにする構文。</span></li>',
 '<li><span class="no">34</span>Reported speech<span class="d">Accusative and infinitive: how a Roman writes &lsquo;he said that&hellip;&rsquo;.</span></li>':
   '<li><span class="no">34</span>間接話法<span class="d">対格と不定法：ローマ人は&lsquo;彼は〜と言った&hellip;&rsquo;をどう書くのか。</span></li>',
 '<li><span class="no">41</span>Reading the citation<span class="d">What <i>Caes. BG 5.44.5</i> means, and how to go and find the rest of the page.</span></li>':
   '<li><span class="no">41</span>出典の読み方<span class="d"><i>Caes. BG 5.44.5</i>が何を指すのか、そしてその頁の続きをどう探しに行くのか。</span></li>',

 "Also inside: i acting as y, ch and ae/oe, the connectives, the prime movers, the present tense, the imperative, the sound system, the full plural, two more conjugations, the imperfect, the third declension, prepositions and case, the perfect and its family, relative clauses, connectives at speed, all three participles and their two jobs, the passive twice over, deponents, the infinitive family, the subjunctive mood, cum-clauses, purpose and result, indirect questions, the gerund, the gerundive — and a closing lesson on where to go next.":
   "ほかに収録：yとして働くi、chとae/oe、つなぎの語、第一の動者、現在時制、命令法、音の体系、複数形のすべて、さらに2つの活用、未完了過去、第三変化、前置詞と格、完了とその一族、関係節、速さの中でのつなぎの語、3つの分詞すべてとその2つの働き、受動態を二度、異態動詞、不定法の一族、接続法、cum節、目的と結果、間接疑問、動名詞、動形容詞 — そして次に向かう先を示す最終レッスン。",

 # ---- the two packs, and the fork past them ----
 "Two packs to literacy": "読めるようになるまで、2パック",
 "Latin is a trunk, not a staircase of three. Core and Pareto together are the whole 2,000-word reading course, grammar-complete at the end of it.":
   "ラテン語は幹であって、3段の階段ではありません。CoreとParetoを合わせたものが2,000語の読解コースのすべてで、終わりまでに文法は完結します。",
 ">Tiers 1–5 · 1,000 words · 26 lessons<": ">ティア1〜5 · 1,000語 · レッスン26本<",
 "The reading foundation. Sentences built to the tier at first, real Caesar by the end. Requires the base game.":
   "読みの土台。はじめはティアに合わせて組んだ文、終わりには本物のカエサル。基本ゲームが必要です。",
 ">Tiers 6–10 · 1,000 words · 18 lessons<": ">ティア6〜10 · 1,000語 · レッスン18本<",
 "The second thousand, and the end of the scaffolding: Nepos, Cicero's letters, Sallust, Livy, Cicero's speeches. Requires Core.":
   "第二の1,000語、そして足場の終わり：ネポス、キケロの書簡、サッルスティウス、リウィウス、キケロの弁論。Coreが必要です。",
 ">On Steam<": ">Steamで発売中<",

 "Then choose your third thousand": "そのあと、第三の1,000語を選ぶ",
 "Basic literacy is the fork, not the finish. The trunk stops at 2,000 words on purpose: past that, Latin genuinely divides, and which 1,000 words come next depends on what you want to read. Neither branch is built yet.":
   "基本の読解力は分岐点であって、終点ではありません。幹が2,000語で止まるのは意図的です。その先でラテン語は本当に分かれ、次の1,000語が何になるかは、何を読みたいかで決まります。どちらの枝も、まだ作られていません。",
 ">Classical Poetry<": ">古典詩<",
 ">Vergil · Ovid · Catullus · Horace<": ">ウェルギリウス · オウィディウス · カトゥルス · ホラティウス<",
 "Verse word order, metre, and the vocabulary that only ever shows up in poets. The trunk's prose ladder is the prerequisite, not a substitute.":
   "韻文の語順、韻律、そして詩人のところにしか現れない語彙。幹の散文のはしごは前提であって、代わりにはなりません。",
 ">planned · not yet built<": ">計画中 · 未制作<",
 ">Ecclesiastical Latin<": ">教会ラテン語<",
 ">the Vulgate · the hymns · the liturgy<": ">ウルガータ · 賛歌 · 典礼<",
 "Church Latin is its own register — different syntax, different vocabulary, and its own pronunciation, which is why it is a branch and not a chapter of the trunk.":
   "教会ラテン語は、それ自体がひとつの語法の層です — 構文も語彙も異なり、発音も独自のもの。だからこれは幹の一章ではなく、一本の枝なのです。",
 "Both branches take Core and Pareto as their entry requirement. Neither has a date; both are inventoried and reserved rather than promised.":
   "どちらの枝も、CoreとParetoを入口の条件とします。日付はどちらにもありません。約束ではなく、棚に載せて確保してあるだけです。",

 # ---- method ----
 "How it sticks": "なぜ定着するのか",
 "Flashcards as an integrated system": "単語カードを、ひとつの仕組みに",
 "<dt>Fibonacci SRS</dt>": "<dt>フィボナッチ間隔反復</dt>",
 "Rate each card 0–5. The better you know a word, the longer before it returns — spaced repetition on Fibonacci intervals.":
   "カードごとに0〜5で自己評価。よく覚えているほど、次に出るまでの間隔が延びます — フィボナッチ数列にもとづく間隔反復です。",
 "<dt>Boss fights</dt>": "<dt>ボス戦</dt>",
 "Each of the 80 clusters is gated by a duel you can't win without confronting and overcoming your most difficult words.":
   "80クラスターそれぞれの関門は決闘。いちばん苦手な単語と向き合い、打ち倒さない限り勝てません。",
 "<dt>Graduation</dt>": "<dt>卒業</dt>",
 "Beat a cluster and its cards leave your daily deck for good. The deck gets smaller as you learn.":
   "クラスターを攻略すると、そのカードは日々の山から永久に抜けます。学ぶほど、山は小さくなります。",
 "<dt>Audio</dt>": "<dt>音声</dt>",
 "A Latin neural voice on every headword and every example sentence — <i>la_LA-flashboss_m</i>, fine-tuned for FlashBoss and released CC0, reading Classical (restored) pronunciation and honouring the macrons as real vowel length. It is synthesis, not a recording of a speaker.":
   "見出し語にも例文にも、ラテン語のニューラル音声 — <i>la_LA-flashboss_m</i>。FlashBoss向けに追加学習し、CC0で公開しています。古典式（復元）発音で読み、マクロンを実際の母音の長さとして扱います。合成音声であり、話者の録音ではありません。",
 "<dt>Your language</dt>": "<dt>あなたの言語</dt>",
 "All 2,000 cards carry their translation, their example translation <i>and</i> their notes in <b>German, Spanish, Japanese, Russian and Simplified Chinese</b> as well as English — 30,000 fields, with no gaps. All 44 reference lessons carry the same five, and so does the game's interface. Latin is fully playable without a word of English.":
   "2,000枚すべてが、訳・例文訳<i>と</i>解説を、英語に加えて<b>ドイツ語・スペイン語・日本語・ロシア語・簡体字中国語</b>で持っています — 30,000のフィールドに、欠けはひとつもありません。参照レッスン44本すべてが同じ5言語を備え、ゲームのインターフェースも同じです。ラテン語は英語を一語も使わずに遊べます。",
 "<dt>Macrons</dt>": "<dt>マクロン</dt>",
 "Long vowels marked on 1,320 of the 2,000 headwords, left off the sentences — dictionary convention where it teaches, print convention where you read.":
   "長母音の印は2,000の見出し語のうち1,320に付き、例文には付きません — 教えるところは辞書の流儀、読むところは印刷の流儀です。",
 "<dt>Real sources</dt>": "<dt>本物の出典</dt>",
 "1,052 example sentences cite the book, chapter and section they came from; 813 are unaltered. Everything is drawn from public-domain editions.":
   "1,052の例文が、出どころの巻・章・節を示します。うち813は手を加えていません。すべてパブリックドメインの版から採っています。",
 "Forty-four reference lessons across the two packs fire at the point in the sequence where they unlock what you are about to read.":
   "2つのパックを合わせた参照レッスン44本が、これから読むものを解錠する地点で発火します。",

 # ---- FAQ ----
 ">Questions<": ">よくある質問<",
 "The things people ask before they buy.": "買う前に、みなさんが尋ねること。",

 ">Where do I buy it?<": ">どこで買えますか?<",
 """Both packs are on Steam now: <a href="https://store.steampowered.com/app/5063240/?utm_source=website-latin-faq" target="_blank" rel="noopener">Latin Core</a> and <a href="https://store.steampowered.com/app/5063250/?utm_source=website-latin-faq" target="_blank" rel="noopener">Latin Pareto</a>. Both word lists and all forty-four lessons are readable here, free, if you want to judge the course before you buy either one.""":
   """2つのパックはどちらもSteamで発売中です：<a href="https://store.steampowered.com/app/5063240/?utm_source=website-latin-faq" target="_blank" rel="noopener">Latin Core</a>と<a href="https://store.steampowered.com/app/5063250/?utm_source=website-latin-faq" target="_blank" rel="noopener">Latin Pareto</a>。単語リストは両方とも、レッスンも44本すべて、このサイトで無料で読めます。どちらかを買う前にコースを見極めたい方は、どうぞ。""",

 ">Which pronunciation is this?<": ">これはどの発音ですか?<",
 "Classical — the restored pronunciation of Caesar's Rome, in the lessons and in the voice alike: c and g always hard, v as English w, <i>Caesar</i> said as the German <i>Kaiser</i>. An ecclesiastical voice is planned separately, and Church Latin proper is a branch of its own rather than an option inside this course.":
   "古典式 — カエサルのローマの復元発音です。レッスンでも音声でも同じで、cとgはつねに硬音、vは英語のwのように、<i>Caesar</i>はドイツ語の<i>Kaiser</i>のように読みます。教会式の音声は別に計画していますし、教会ラテン語そのものは、このコース内の選択肢ではなく独立した枝です。",

 ">Do I need anything else to play it?<": ">遊ぶのに他に必要なものはありますか?<",
 """Yes. Latin Core is a DLC for the FlashBoss base game, so you need the base game as well. Latin Pareto requires Core — the packs build on each other in order. Everything else — the lessons, the audio, the boss fights — is inside the pack. On Windows 10 you also need <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a> — a free, secure download from the Microsoft Store.""":
   """はい。Latin CoreはFlashBoss基本ゲームのDLCなので、基本ゲームも必要です。Latin ParetoはCoreを前提とします — パックは順に積み上がります。それ以外 — レッスン、音声、ボス戦 — はすべてパックの中に入っています。Windows 10では<a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a>も必要です — Microsoft Storeから無料・安全にダウンロードできます。""",

 ">Is the Latin real, or written for the course?<": ">ラテン語は本物ですか、それともコースのために書かれたものですか?<",
 "Both, in a stated order. Tiers 1 to 3 are constructed to the grammar you have been taught — no real author writes at that ceiling, and the cards claim none. Caesar enters at Tier 4, lightly trimmed. From Tier 8 on, almost every sentence is an author's own unaltered words. Across the two packs 1,052 of 2,000 sentences carry a citation and 813 of those are unadapted.":
   "両方です。しかも順序を明記しています。ティア1から3は、あなたが習った文法に合わせて組んだ文です — 本物の著者はその上限では書かないので、カードも著者を名乗りません。カエサルはティア4で登場し、わずかに刈り込んであります。ティア8からは、ほとんどの文が著者自身の、手を加えていないことばです。2つのパック全体で、2,000の文のうち1,052に出典が付き、そのうち813は原文のままです。",

 ">Can I play it in my own language?<": ">自分の言語で遊べますか?<",
 "Fully. Every one of the 2,000 cards carries its translation, its example translation and its study notes in <b>German, Spanish, Japanese, Russian and Simplified Chinese</b> as well as English, with no gaps anywhere. All forty-four reference lessons carry the same five, and the game's own interface speaks all six.":
   "完全に遊べます。2,000枚のカードはすべて、訳・例文訳・学習ノートを、英語に加えて<b>ドイツ語・スペイン語・日本語・ロシア語・簡体字中国語</b>で持っており、どこにも欠けはありません。参照レッスン44本すべてが同じ5言語を備え、ゲーム本体のインターフェースは6言語すべてに対応しています。",

 ">What does the course get me to?<": ">このコースでどこまで行けますか?<",
 "Reading unadapted classical prose with a dictionary beside you. Two thousand of the highest-frequency lemmas, the whole grammar of the indicative and subjunctive, participles, the infinitive constructions, the gerund and gerundive — and 17,007 words of Latin read in context on the way there. Not speaking Latin, and not writing it: the course is honest that it teaches one skill.":
   "辞書を傍らに置いて、手を加えていない古典散文を読めるところまでです。最頻出の見出し語2,000、直説法と接続法の文法のすべて、分詞、不定法の構文、動名詞と動形容詞 — そしてその道中で、文脈の中の17,007語のラテン語を読むことになります。ラテン語を話すところまでではなく、書くところまででもありません。このコースは、ひとつの技能を教えるのだと正直に言います。",

 ">Why is there no Pareto 2?<": ">Pareto 2はないのですか?<",
 "Because Latin forks instead. Core plus Pareto is a complete 2,000-word trunk, grammar-complete at Tier 10. The third thousand depends on where you are going — classical poetry or ecclesiastical Latin — so it is planned as two branches rather than one more staircase. Neither is built yet.":
   "ラテン語は、代わりに分岐するからです。CoreとParetoで2,000語の幹は完結し、ティア10で文法も完結します。第三の1,000語は、どこへ向かうかによって変わります — 古典詩か、教会ラテン語か — なので、もう一段の階段ではなく2本の枝として計画しています。どちらもまだ作られていません。",

 ">Can I see the words before I buy?<": ">買う前に単語を見られますか?<",
 """All of them. The complete word lists for Core and Pareto are on the <a href="wordlists.html?lang=Latin&amp;set=Core">word lists page</a>, and all forty-four reference lessons are on the <a href="lessons.html?lang=Latin">lessons page</a> — free, printable, no account.""":
   """全部見られます。CoreとParetoの完全な単語リストは<a href="wordlists.html?lang=Latin&amp;set=Core">単語リストのページ</a>に、参照レッスン44本は<a href="lessons.html?lang=Latin">レッスンのページ</a>にあります — 無料、印刷可、アカウント不要です。""",

 ">Is there a demo?<": ">デモはありますか?<",
 """There's a playable boss fight in the browser, if you want to know what the fight feels like before you commit: <a href="https://flashboss-demo.pages.dev/">try the demo</a>.""":
   """ブラウザで遊べるボス戦があります。決める前に戦いの手ざわりを知りたい方はこちらへ：<a href="https://flashboss-demo.pages.dev/">デモを試す</a>。""",

 # ---- closing call to action ----
 "Start with <i>Roma est.</i>": "<i>Roma est.</i>から始めよう。",
 "Two words on the first card of the first cluster. Two thousand words later, Cicero.":
   "最初のクラスターの最初のカードに、たった二語。2,000語の先に、キケロがいます。",
 "— both on Steam": "— どちらもSteamで発売中",
 """Or read the <a href="wordlists.html?lang=Latin&amp;set=Core">word list</a> and the <a href="lessons.html?lang=Latin">lessons</a> first — they're free, and they're the whole course.""":
   """あるいは、まず<a href="wordlists.html?lang=Latin&amp;set=Core">単語リスト</a>と<a href="lessons.html?lang=Latin">レッスン</a>を — どちらも無料で、そしてこれがコースのすべてです。""",
 # the bundle name is the ratified Japanese one from the Latin paste sheet
 """Everything here in one purchase: <a href="https://store.steampowered.com/bundle/87746/?utm_source=website-bundle" target="_blank" rel="noopener"><b>FlashBoss Latin — The Complete Course</b></a>. Already own part of it? Steam charges you only for the rest.""":
   """ここにあるすべてを、ひとつの購入で：<a href="https://store.steampowered.com/bundle/87746/?utm_source=website-bundle" target="_blank" rel="noopener"><b>FlashBoss ラテン語 — コンプリートコース</b></a>。一部をすでにお持ちですか？Steamは残りの分だけを請求します。""",

 # ---- footer epigraph: the Latin stands, the gloss and the cite become Japanese ----
 '<span class="tr">Chance counts for much in everything, and most of all in warfare.</span>':
   '<span class="tr">運はあらゆることにおいて大きな力を持ち、とりわけ戦においてそうです。</span>',
 "Latin Core · Tier 4 · Caes. BG 6.30.2": "Latin Core · ティア4 · Caes. BG 6.30.2",
}

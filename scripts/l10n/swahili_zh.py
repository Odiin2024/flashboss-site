# Simplified Chinese strings for swahili.html.
# The key set is swahili_de.py's, key for key and in the same order — that file
# is the worked example for this page and fixes which strings exist.
#
# Where the ratified Chinese bundle copy
# (flashboss-admin/BUNDLE_COPY_SWAHILI_2026-09-08.md) has a sentence, its
# wording is reused: 斯瓦希里语 for the language (also what lessons.zh.html,
# wordlists.zh.html and about.zh.html already write), 语音朗读 for the
# text-to-speech line, the six-language list in the sheet's own order
# (英语、德语、日语、俄语、简体中文和西班牙语), 卡包 for a pack and
# Complete-the-Set's "只收取……的费用" turn of phrase. The immersion page's
# glossary supplies the rest: 词族, Boss 战, 基础游戏, 卡片, 词目, 单词列表,
# 课程, 语音, 复习练习, 斐波那契间隔重复.
#
# TERMINOLOGY, and the owner should look at this once — the two sheets for this
# locale disagree and the newer one wins here:
#   cluster    = 词族    — the Roots sheet and the zh immersion page. THIS
#                          Swahili sheet (2026-09-08) says 集群, as does
#                          about.zh.html. The brief tells me to reuse the
#                          glossary, and a site that called the same thing two
#                          names on two pages of one locale would read as two
#                          products.
#   boss fight = Boss 战 — the Roots sheet and the zh immersion page. The
#                          Swahili sheet says 头目. Same reasoning.
# Everything else my own, in the plain register of the live zh pages.
#
# PAGE CANON, held here:
#   * every Swahili word, form and example SENTENCE is left byte-identical —
#     anaendesha, tulisafiri, walipanda, the three quoted pack sentences,
#     gari's card, the ten noun-class names (m/wa, ji/ma, ku, pa …). Only the
#     gloss after the dash becomes Chinese, because the card carries a Chinese
#     gloss too.
#   * pack names stay English and sit bare inside the Chinese sentence, with a
#     space on each side and no 《》 and no bracketed gloss: Swahili Core,
#     Swahili Pareto 1, Swahili Pareto 2, Core, Pareto 1, Pareto 2. So does
#     FlashBoss, and so do Steam, DLC, Windows Terminal, Microsoft Store.
#   * grammar terms are the ordinary Chinese ones: 名词类别 (noun class),
#     一致 / 一致关系 (agreement, concord), 时态, 主语, 宾语, 使役式, 现在时.
#     A verb slot is 槽位.
#   * the page's counts (1,000 / 40 / 20 / 14 / five 层级) are the recount of
#     2026-09-19 and are reproduced exactly; the 2026-09-08 bundle sheet's
#     "3000 词" and "全部 49 课" predate it and do not win.
#   * banned and absent: hours, CEFR codes, prices, discounts, and a date for
#     anything already out.
#
# Punctuation: full-width inside Chinese sentences, 、 between example pairs,
# and the em dash rendered —— in running prose, which is what the live zh pages
# do. The page's own " · " separators and its Swahili full stops are left alone.
TITLE = "斯瓦希里语 — FlashBoss"
DESCRIPTION = ("FlashBoss 斯瓦希里语：1,000 个单词，分布在 40 个词族与 20 节参考课中，"
               "每个名词都标出它的名词类别，配标准斯瓦希里语的神经网络语音，每一道关口都有"
               "一场 Boss 战。译文与学习注释提供六种语言。Swahili Core 已在 Steam 发售。")

STRINGS = {
 # ---- nav / chrome / footer ----
 ">packs<": ">卡包<",
 ">word list<": ">单词列表<",
 ">lessons<": ">课程<",
 ">voices<": ">语音<",
 ">home<": ">主页<",

 # ---- hero ----
 "The newest course · <b>1,000 words out now</b>":
   "最新的课程 · <b>1,000 个单词现已推出</b>",
 "The most regular language you will ever learn the hard way.":
   "你会靠硬功夫学下来的语言里，最规则的一门。",
 "Listen · read · repeat · rate · fight":
   "听 · 读 · 重复 · 评分 · 战斗",
 "Swahili does not conjugate so much as <b>assemble</b>. A verb is built from slots in a fixed order, and every noun belongs to a class that the rest of the sentence agrees with. Learn those two machines and the vocabulary stops being a list. <b>1,000 words, 40 clusters, 20 reference lessons</b> — with the class named on every noun.":
   "斯瓦希里语与其说是在变位，不如说是在<b>组装</b>。动词由固定顺序的槽位拼成，每个名词都属于某一类别，句子的其余部分都要与它保持一致。学会这两台机器，词汇就不再是一张清单。<b>1,000 个单词、40 个词族、20 节参考课</b>——每个名词都标出它的类别。",

 # ---- the argument ----
 "Why Swahili is learnable": "斯瓦希里语为什么学得会",
 "A language with no irregular verbs to speak of":
   "一门几乎没有不规则动词的语言",
 "Swahili is the working language of East Africa — Tanzania, Kenya, Uganda, Rwanda, Burundi and the eastern Congo — and it is spoken by far more people who learned it than by people born to it. That has worn it smooth. Spelling is exactly as it sounds, stress is always the second-to-last syllable, and there is no tone and no grammatical gender.":
   "斯瓦希里语是东非的通用语——坦桑尼亚、肯尼亚、乌干达、卢旺达、布隆迪，以及刚果东部——说它的人里，后天学会的远多于自幼说到大的。这一点把它磨平了。怎么读就怎么拼，重音永远落在倒数第二个音节，既没有声调，也没有语法上的性。",
 "What it has instead is <b>structure you can see</b>. The verb is a train of slots. The noun carries a class, and the class rides through the whole sentence. Neither is hidden, and neither has a list of exceptions waiting for you at intermediate level.":
   "它有的是<b>看得见的结构</b>。动词是一列由槽位连成的火车。名词带着类别，这个类别会一路贯穿整个句子。两者都不藏着，也都没有一张例外清单等在中级阶段。",
 "This course teaches ordinary Swahili — the language of the market, the school and the news. The frequency backbone it is built from was made for that, not for subtitles.":
   "这门课教的是寻常的斯瓦希里语——市场、学校与新闻里的语言。它所依据的词频骨架就是为此而做的，不是为字幕而做的。",

 # ---- the verb train. The three Swahili sentences are quoted from the pack's
 #      own cards: they stay byte-identical, only the gloss becomes Chinese. ----
 "The verb is an assembly": "动词是一套组装件",
 "Slots, in a fixed order": "槽位，顺序固定",
 "Three sentences from the pack's own cards, taken apart. The order never changes: who, when, whom, what.":
   "三个句子取自卡包自己的卡片，拆开来看。顺序从不改变：谁、何时、对谁、做什么。",
 '<i class="ls"></i> who — the subject': '<i class="ls"></i> 谁——主语',
 '<i class="lt"></i> when — the tense': '<i class="lt"></i> 何时——时态',
 '<i class="lo"></i> whom — the object': '<i class="lo"></i> 对谁——宾语',
 '<i class="lr"></i> what — the root': '<i class="lr"></i> 做什么——词根',

 "Baba yangu <b>anaendesha</b> basi la shule kila asubuhi, na mama anaendesha gari. — My father drives the school bus every morning, and my mother drives the car.":
   "Baba yangu <b>anaendesha</b> basi la shule kila asubuhi, na mama anaendesha gari. ——我父亲每天早上开校车，我母亲开小汽车。",
 '<span class="m s">a-<i>he / she</i></span>': '<span class="m s">a-<i>他 / 她</i></span>',
 '<span class="m t">na-<i>present</i></span>': '<span class="m t">na-<i>现在时</i></span>',
 '<span class="m r">endesha<i>drive, make go</i></span>':
   '<span class="m r">endesha<i>驾驶、使之行进</i></span>',
 "Three pieces, read left to right: <b>he · now · drives</b>. The root itself is built — <i>endesha</i> is the causative of <i>kwenda</i>, to go, so it means to make something go.":
   "三个部件，从左往右读：<b>他 · 现在 · 驾驶</b>。词根本身也是拼出来的——<i>endesha</i> 是 <i>kwenda</i>（走、去）的使役式，所以它的意思是让某样东西动起来。",

 "<b>Tulisafiri</b> kwa treni kutoka jijini hadi kijijini kwetu wakati wa likizo. — We travelled by train from the city to our village during the holiday.":
   "<b>Tulisafiri</b> kwa treni kutoka jijini hadi kijijini kwetu wakati wa likizo. ——假期里，我们坐火车从城里回到我们的村子。",
 '<span class="m s">tu-<i>we</i></span>': '<span class="m s">tu-<i>我们</i></span>',
 '<span class="m t">li-<i>past</i></span>': '<span class="m t">li-<i>过去时</i></span>',
 '<span class="m r">safiri<i>travel</i></span>': '<span class="m r">safiri<i>旅行</i></span>',
 "Change one letter in the middle slot and you change the tense. <b>tuna</b>safiri is we are travelling; <b>tuta</b>safiri is we will travel. Nothing else in the word moves.":
   "把中间那个槽位改掉一个字母，时态就变了。<b>tuna</b>safiri 是我们正在旅行，<b>tuta</b>safiri 是我们将要旅行。词里别的部分纹丝不动。",

 "Watu wengi <b>walipanda</b> basi hilo kubwa mapema asubuhi ya leo. — Many people boarded that big bus early this morning.":
   "Watu wengi <b>walipanda</b> basi hilo kubwa mapema asubuhi ya leo. ——今天一早，很多人上了那辆大巴士。",
 '<span class="m s">wa-<i>they, class m/wa</i></span>':
   '<span class="m s">wa-<i>他们，m/wa 类</i></span>',
 '<span class="m r">panda<i>climb, board, plant</i></span>':
   '<span class="m r">panda<i>攀登、上车、种植</i></span>',
 "The subject slot is not just a pronoun: it agrees with the <b>class</b> of the noun. <i>Watu</i> is class m/wa, so the verb starts wa-. That is the second machine.":
   "主语槽位不只是一个代词：它要与名词的<b>类别</b>保持一致。<i>Watu</i> 属于 m/wa 类，所以动词以 wa- 开头。这就是第二台机器。",
 "The pack drills this directly. One of Swahili's three revision drills is the verb train, built slot by slot — you assemble the form rather than recall it whole.":
   "卡包直接练这个。斯瓦希里语的三种复习练习之一就是动词火车，一个槽位一个槽位地搭起来——你是把词形组装出来，而不是整个回忆出来。",

 # ---- noun classes: whole cells, so no English label survives next to a
 #      class name. The class names themselves are Swahili and stay. ----
 "The engine": "引擎",
 "Every noun carries its class": "每个名词都带着它的类别",
 "Swahili has no gender. It has classes — and the class of the noun decides the shape of its plural, its adjectives, its verb and its possessives. Get the class and the agreement comes free.":
   "斯瓦希里语没有性。它有的是类别——名词的类别决定了它的复数、它的形容词、它的动词和它的所有格各是什么样子。抓住类别，一致关系就是白送的。",
 '<div class="k">m/wa</div><div class="v">people — <i>mtu / watu</i></div>':
   '<div class="k">m/wa</div><div class="v">人——<i>mtu / watu</i></div>',
 '<div class="k">m/mi</div><div class="v">trees, living things, body parts</div>':
   '<div class="k">m/mi</div><div class="v">树木、有生命之物、身体部位</div>',
 '<div class="k">ji/ma</div><div class="v">large things, pairs, groups</div>':
   '<div class="k">ji/ma</div><div class="v">大的东西、成对之物、群体</div>',
 '<div class="k">ki/vi</div><div class="v">objects, tools, languages</div>':
   '<div class="k">ki/vi</div><div class="v">物件、工具、语言</div>',
 '<div class="k">n/n</div><div class="v">loans, animals, many abstracts</div>':
   '<div class="k">n/n</div><div class="v">外来词、动物、许多抽象名词</div>',
 '<div class="k">u/n</div><div class="v">abstract nouns, mass nouns</div>':
   '<div class="k">u/n</div><div class="v">抽象名词、物质名词</div>',
 '<div class="k">u/ma</div><div class="v">long thin things</div>':
   '<div class="k">u/ma</div><div class="v">细长的东西</div>',
 '<div class="k">u/u</div><div class="v">a smaller set, no plural shift</div>':
   '<div class="k">u/u</div><div class="v">较小的一组，复数不换形</div>',
 '<div class="k">ku</div><div class="v">the infinitive used as a noun</div>':
   '<div class="k">ku</div><div class="v">用作名词的不定式</div>',
 '<div class="k">pa</div><div class="v">place</div>':
   '<div class="k">pa</div><div class="v">处所</div>',
 "Those are the ten classes this pack actually uses, taken from its cards rather than from a grammar. The class is printed on every single noun in the deck, where another course would leave you to infer it.":
   "这就是这个卡包真正用到的十个类别，取自它的卡片，而不是取自一本语法书。牌组里每一个名词都印着自己的类别，换成别的课程，只会留给你自己去推断。",

 # ---- the card. gari and its Swahili example sentence stay. ----
 "What a card holds": "一张卡片上有什么",
 "A real one, from tier 2. The class sits beside the headword; the notes say the thing a dictionary would not.":
   "这是一张真卡片，取自第 2 层级。类别就在词目旁边；注解讲的是词典不会讲的那些事。",
 '<div class="tr">a car, or any road vehicle</div>':
   '<div class="tr">汽车，或者任何一种道路车辆</div>',
 '<div class="exx">Our car has no fuel, so we have stopped near the bridge.</div>':
   '<div class="exx">我们的车没油了，所以我们在桥边停了下来。</div>',
 "The same card carries its translation, its example translation <b>and</b> its notes in German, Japanese, Russian, Simplified Chinese and Spanish as well as English — full coverage, every card, no gaps.":
   "同一张卡片的译文、例句译文<b>以及</b>注解，除英语外还提供德语、日语、俄语、简体中文和西班牙语——每张卡片都齐全，没有缺口。",

 # ---- method: whole <dt>/<dd> pairs, so no English term is left stranded ----
 "How it sticks": "怎样才记得住",
 "Flashcards as an integrated system": "卡片作为一套完整的系统",
 "<dt>Cards</dt><dd><b>1,000 words across 40 clusters</b> and five tiers — greetings and family, the town, work and health, government, the news, and the small words that join sentences together. An example sentence on every card.</dd>":
   "<dt>卡片</dt><dd><b>1,000 个单词，分布在 40 个词族</b>与五个层级中——问候与家人、城镇、工作与健康、政府、新闻，以及把句子接起来的那些小词。每张卡片都配一个例句。</dd>",
 "<dt>Noun class</dt><dd>Named on <b>every noun</b>, on the card itself: <i>ji/ma</i>, <i>ki/vi</i>, <i>m/wa</i>. The engine the whole language runs on, never left implicit.</dd>":
   "<dt>名词类别</dt><dd>在<b>每个名词</b>上标出，就写在卡片本身：<i>ji/ma</i>、<i>ki/vi</i>、<i>m/wa</i>。整门语言靠它运转的引擎，从不含糊带过。</dd>",
 "<dt>Your language</dt><dd>Translations and study notes in <b>English, German, Japanese, Russian, Simplified Chinese and Spanish</b> — full coverage on every card. Study Swahili through whichever you call home.</dd>":
   "<dt>你的语言</dt><dd>译文与学习注释提供<b>英语、德语、日语、俄语、简体中文和西班牙语</b>——每张卡片都齐全。用你称作母语的那一种来学斯瓦希里语。</dd>",
 '<dt>Lessons</dt><dd><b>20 reference lessons</b> — the sound system, the noun-class families, the verb slot machine, the Swahili clock, and concord tier by tier. Readable in all six languages, and <a href="lessons.html?lang=Swahili">free to read here</a>.</dd>':
   '<dt>课程</dt><dd><b>20 节参考课</b>——语音系统、名词类别的各个族群、动词的槽位机器、斯瓦希里语的钟点，以及逐个层级讲的一致关系。六种语言都能读，<a href="lessons.html?lang=Swahili">在这里免费阅读</a>。</dd>',
 "<dt>Drills</dt><dd>Three, shaped to Swahili rather than borrowed: the <b>verb train</b> built slot by slot, <b>plurals by noun class</b>, and <b>dictation</b>.</dd>":
   "<dt>练习</dt><dd>三种，按斯瓦希里语的样子做的，不是从别处借来的：一个槽位一个槽位搭起来的<b>动词火车</b>、<b>按名词类别变复数</b>，以及<b>听写</b>。</dd>",
 "<dt>Audio</dt><dd>Text-to-speech on every word and every example sentence, in a neural standard Kiswahili voice. Synthesis, not a recording of a speaker.</dd>":
   "<dt>语音</dt><dd>每个单词、每个例句都有语音朗读，用的是标准斯瓦希里语的神经网络语音。这是合成出来的，不是真人的录音。</dd>",
 "<dt>Fibonacci SRS</dt><dd>Rate each card 0–5. The better you know a word, the longer before it returns.</dd>":
   "<dt>斐波那契间隔重复</dt><dd>给每张卡片打 0–5 分。一个词你记得越牢，它再回来之前的间隔就越长。</dd>",
 "<dt>Boss fights</dt><dd>No cluster is cleared until its hardest words are answered. Beat it and its cards leave your daily deck for good.</dd>":
   "<dt>Boss 战</dt><dd>不答出一个词族里最难的那些词，这个词族就不算清掉。打赢它，它的卡片就永远离开你的每日卡组。</dd>",

 # ---- the three packs. Pack names stay English; no date on the unreleased two. ----
 "Three packs, three thousand words": "三个卡包，三千个单词",
 "Core is out. The two that follow are written and are not on sale yet; neither carries a date until it is.":
   "Core 已经发售。后面两个已经写好，但还没有上架；在上架之前，它们都不标日期。",
 '<div class="lvl">Tiers 1–5 · 1,000 words · 20 lessons</div>':
   '<div class="lvl">层级 1–5 · 1,000 个单词 · 20 节课</div>',
 "<p>The foundation: greetings and the family through the town, work and health to government and the news.</p>":
   "<p>地基：从问候与家人，经过城镇、工作与健康，一直到政府与新闻。</p>",
 '<span class="here">On Steam</span>': '<span class="here">在 Steam 发售</span>',
 '<div class="lvl">Tiers 6–10 · 1,000 words · 14 lessons</div>':
   '<div class="lvl">层级 6–10 · 1,000 个单词 · 14 节课</div>',
 "<p>The working vocabulary: money and the bank, the contract, the ministry, elections, the court, the press, the hospital.</p>":
   "<p>办事用的词汇：钱与银行、合同、部委、选举、法院、新闻界、医院。</p>",
 '<span class="soon">Written, not yet out</span>':
   '<span class="soon">已写好，尚未发售</span>',
 '<div class="lvl">Tiers 11–15 · 1,000 words · 14 lessons</div>':
   '<div class="lvl">层级 11–15 · 1,000 个单词 · 14 节课</div>',
 "<p>Where derivation opens up — one root becomes six verbs — and the vocabulary follows it into public life and register.</p>":
   "<p>派生在这里打开——一个词根长出六个动词——词汇也随之走进公共生活与语体层次。</p>",
 "Each pack is 1,000 words and five tiers, and each takes the one before it as read. The end of Pareto 1 is the hump: not finished, but the language has stopped being a wall.":
   "每个卡包都是 1,000 个单词、五个层级，而且都默认你已经学过前一个。Pareto 1 的终点是那道坎：还没有学完，但这门语言已经不再是一堵墙。",

 # ---- FAQ ----
 "Questions": "问题",
 "Before you buy": "在你购买之前",
 "<summary>Do I need the base game?</summary>": "<summary>我需要基础游戏吗？</summary>",
 'Yes. Swahili Core is DLC for FlashBoss, so you need the base game as well. Everything else — the lessons, the audio, the drills, the boss fights — is inside the pack. On Windows 10 you also need <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a>, a free download from the Microsoft Store.':
   '需要。Swahili Core 是 FlashBoss 的 DLC，所以你还需要基础游戏。其余的一切——课程、语音、练习、Boss 战——都在这个卡包里面。在 Windows 10 上，你还需要 <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a>，可以从 Microsoft Store 免费下载。',
 "<summary>Can I study it in my own language?</summary>":
   "<summary>我可以用自己的语言来学吗？</summary>",
 "Fully. Every card carries its translation, its example translation and its study notes in <b>German, Japanese, Russian, Simplified Chinese and Spanish</b> as well as English, with no gaps, and all 20 reference lessons carry the same six. The game's own interface speaks them too.":
   "完全可以。每张卡片的译文、例句译文和学习注释，除英语外还有<b>德语、日语、俄语、简体中文和西班牙语</b>，没有缺口；全部 20 节参考课也是这六种语言。游戏自己的界面同样说这几种语言。",
 "<summary>Which Swahili is this?</summary>": "<summary>这是哪一种斯瓦希里语？</summary>",
 "Standard Kiswahili — the one taught in schools and used by the press across East Africa, based on the Zanzibar dialect. The voice is a neural standard Kiswahili voice.":
   "标准斯瓦希里语——学校里教的、东非各地新闻界使用的那一种，以桑给巴尔方言为基础。语音是标准斯瓦希里语的神经网络语音。",
 "<summary>Can I see the words before I buy?</summary>":
   "<summary>买之前我能先看到这些单词吗？</summary>",
 'All of them. The complete <a href="wordlists.html?lang=Swahili&amp;set=Core">word list</a> and all twenty <a href="lessons.html?lang=Swahili">reference lessons</a> are on this site — free, printable, no account. There is also a <a href="https://flashboss-demo.pages.dev/">playable boss fight</a>.':
   '全都能看。完整的<a href="wordlists.html?lang=Swahili&amp;set=Core">单词列表</a>和全部二十节<a href="lessons.html?lang=Swahili">参考课</a>都在本站——免费、可打印、不用注册账号。还有一场<a href="https://flashboss-demo.pages.dev/">可以直接玩的 Boss 战</a>。',
 "<summary>Is there a British or American spelling layer?</summary>":
   "<summary>有英式或美式拼写的层吗？</summary>",
 "That layer covers the English packs. Swahili's English is the translation side of the card, and the pack ships one edition of it.":
   "那个层属于英语的几个卡包。斯瓦希里语这边的英语是卡片的译文一侧，这个卡包只发行一个版本。",

 # ---- final ----
 "Start with <i>Habari?</i>": "从 <i>Habari?</i> 开始",
 "Two machines and a thousand words. The rest of Swahili agrees with them.":
   "两台机器，一千个单词。斯瓦希里语余下的部分都与它们保持一致。",
 "Swahili Core on Steam &rarr;": "在 Steam 上查看 Swahili Core &rarr;",
}

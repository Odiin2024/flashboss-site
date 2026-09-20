# Simplified Chinese strings for the-guide.html.
#
# Sources, in the order they win:
#   1. IP CARE, from the English page's own head comment. The trademarked game
#      name appears NOWHERE on this page and appears nowhere here either, in any
#      language or spelling, Latin or Chinese. The licence framing is the store
#      page's and must not drift: "5E", "SRD" and "System Reference Document 5.2"
#      stay in their English/technical form, "5E compatible" is the ratified
#      sheet's 兼容 5E, "the 2024 revision" is 2024年修订版 and "the 2014 rules"
#      is 2014年规则. The footer's no-affiliation line is translated in full,
#      all three prongs kept: no affiliation, no endorsement, no sponsorship.
#   2. The ratified Chinese bundle copy
#      (flashboss-admin/BUNDLE_COPY_THE_GUIDE_COMPLETE_2026-09-17.md) wherever it
#      has the sentence: the five what-a-card-is-for clauses are its own line,
#      word for word — 某个状态有什么效果、某项检定要掷哪个骰、DC 15 究竟意味着
#      什么、一个属性块在告诉你什么 — and so are 游戏主持人, 桌边, 场景,
#      参考课程, 层级, 挑战等级, 宝物.
#   3. The shipped deck itself, knight/flashcard_sets/The_Guide/core, for rules
#      jargon a Chinese table actually says: 状态, 检定, 属性块, 法术位, 专注,
#      察觉, 黑暗视觉, 轻度遮蔽, 伤害类型, 职业, 专长, 回合, 动作. DC stays DC,
#      which is what a Chinese table says out loud. The sample card (Dim Light,
#      cluster1_10) is quoted from its OWN Chinese twin — Translation_zh,
#      ExampleSentence_zh, ExampleTranslation_zh, Notes_zh — so the page shows
#      the card as the Chinese edition really ships it. That is also why the
#      HEADWORD STAYS ENGLISH below: Chinese is the mixed edition, "play in
#      yours, answer in English", so a Chinese player really does see
#      "Dim Light" over a Chinese scene and a Chinese definition. Translating it
#      to 微光光照 (the deck's TargetWord_zh, which is the all-in-your-language
#      bonus edition) would contradict the editions section three screens down.
#      The card's Notes_zh cites SRD p. 11, the same page the English page cites.
#
# TERMINOLOGY, and the owner should look at this once:
#   cluster = 集群. glossary_zh.txt settled 词族 on the immersion page, but 词族
#   means "word family" — words sharing a root — and a cluster here is a themed
#   group of RULES (vision/light/hiding, the modifier table, the conditions),
#   which share no root. This product's own ratified Chinese Steam copy says
#   集群 four times, and the live zh site pages say 集群 too, so 集群 keeps the
#   page and the store listing it links to saying the same word. This is the one
#   deliberate departure from the glossary.
#   boss fight = Boss 战, kept from glossary_zh.txt. The Guide's ratified sheet
#   says 头目战; Boss 战 is correct either way and is the term the rest of this
#   locale uses for the game's core mechanic, so the brand term wins here.
#
# Pack names stay English: The Guide. FlashBoss stays Latin. Numbers are the
# English page's, and zh keeps the comma separator, so 1,205 is written 1,205;
# SRD p. 11 is page eleven and stays eleven. Nothing was recounted.
#
# Punctuation: full-width throughout, 、 between the example clauses, a literal
# —— where the English page has a prose em dash, no 《》 around Latin names and
# no bracketed gloss.
TITLE = "The Guide — FlashBoss"
DESCRIPTION = ("FlashBoss The Guide：游戏主持人必须记在脑子里的规则，做成卡片。1,205 张卡片，"
               "分在 62 个集群里，62 节参考课程，每道关口都有一场 Boss 战。德语是完整版；"
               "日语、简体中文、俄语和西班牙语用你的语言游玩，用英语作答。"
               "兼容 5E，依据 System Reference Document 5.2 构建。")

STRINGS = {
 # ---- nav / chrome ----
 ">packs<": ">卡包<",
 ">card lists<": ">卡片列表<",
 ">lessons<": ">课程<",
 ">voices<": ">语音<",
 ">home<": ">主页<",

 # ---- hero ----
 "For the person running the table · <b>out now</b>":
   "写给带团的人 · <b>现已推出</b>",
 "1,205 cards · 62 clusters": "1,205 张卡片 · 62 个集群",
 "The rules a game master needs in their head — not on the page they are turning to.":
   "游戏主持人必须记在脑子里的规则——而不是正翻开的那一页上的规则。",
 "Listen · read · repeat · rate · fight": "听 · 读 · 重复 · 评分 · 战斗",
 # the five clauses are the ratified store line, word for word
 "Every card is one thing you should know cold rather than stop to look up: what a condition does, which die a check calls for, what a DC of 15 is meant to mean, what a stat block is telling you, what a party can actually do at level 5. <b>5E compatible, built from the System Reference Document 5.2.</b>":
   "每张卡片都是一件你应当脱口而出、而非临时翻查的事：某个状态有什么效果、某项检定要掷哪个骰、DC 15 究竟意味着什么、一个属性块在告诉你什么、一支队伍在 5 级时究竟做得到什么。<b>兼容 5E，依据 System Reference Document 5.2 构建。</b>",
 ">what a card holds</a>": ">卡片上有什么</a>",
 ">languages</a>": ">语言</a>",

 # ---- the argument ----
 ">Why drill the rules at all<": ">为什么要练熟规则<",
 "<h2>Looking it up is the thing that breaks the table</h2>":
   "<h2>临时翻书，正是毁掉一场团的那件事</h2>",
 "A game master's real skill is adjudicating at speed. Everyone at the table can feel the difference between a ruling that arrives in two seconds and one that arrives after ninety seconds of page-turning — and the second one costs you the scene, not just the time.":
   "游戏主持人真正的本事是快速裁定。两秒钟就给出的裁定，和翻了九十秒书才给出的裁定，桌边每个人都感觉得到差别——后者让你付出的是这场戏，而不只是时间。",
 "The fix is not a better index. It is <b>knowing the thing</b>: the fifteen conditions, the thirteen damage types, the ability and proficiency tables, challenge rating and the experience it is worth. The numbers you currently flip pages for.":
   "办法不是更好的索引。办法是<b>真的知道</b>：十五种状态、十三种伤害类型、属性表与熟练加值表、挑战等级，以及它值多少经验值。那些你现在要翻页才查得到的数字。",
 "So this is a vocabulary course whose vocabulary happens to be a rules set. Same machine as every other FlashBoss pack — spaced repetition, a boss fight at the end of every cluster — pointed at the things you are expected to have in your head when someone asks whether they can shove the ogre off the bridge.":
   "所以这是一门词汇课程，只不过它的词汇恰好是一套规则。和其他每个 FlashBoss 卡包是同一台机器——间隔重复，每个集群的结尾都有一场 Boss 战——只是对准了那些你被指望已经记在脑子里的东西：比如有人问，能不能把食人魔从桥上推下去。",

 # ---- the card ----
 "<h2>What a card holds</h2>": "<h2>卡片上有什么</h2>",
 "A real card from tier 1, quoted as it ships. The scene is the point: the rule arrives as something you could narrate, not as an index entry.":
   "第 1 层级里的一张真实卡片，按发行时的样子引用。场景才是关键：规则以你能讲出来的样子到来，而不是一条索引词条。",
 ">the card<": ">卡片<",
 ">what each part is for<": ">每一部分是做什么的<",

 # the sample card, quoted from its own Chinese twin in cluster1_10 rather than
 # translated here — scene, definition, rule line and notes, SRD page and all.
 # THE HEADWORD STAYS ENGLISH ON PURPOSE. Chinese is the mixed edition: the
 # headword you answer with is English, and this is the card a Chinese player
 # actually sees. The value is the key unchanged so the key set still matches.
 '<div class="hw">Dim Light</div>': '<div class="hw">Dim Light</div>',
 "“Past the torch's ring the corridor goes grey rather than black, and the ranger squints into it and is not sure what she saw.”":
   "“火把光圈之外，走廊转为灰而不是黑，巡林客眯着眼望进去，不确定自己看见了什么。”",
 "Dusk and shadow: sight-based Perception suffers, and Darkvision sees the dark as this.":
   "黄昏与阴影：靠视觉的察觉会吃亏，而黑暗视觉把黑暗看成这个样子。",
 "Shadow: creates a Lightly Obscured area": "阴影：会造成轻度遮蔽的区域",
 "term | the border between bright and dark<br>usually the outer band of a light source · SRD p. 11":
   "术语 | 明亮与黑暗之间的地带<br>通常是光源的外圈 · SRD p. 11",

 # ---- what each part is for: whole <li> each, so no English article survives ----
 "<li><b>The term</b><span>What the table will actually say out loud. This is the answer you are drilled to produce.</span></li>":
   "<li><b>术语</b><span>桌边真正会说出口的那个词。这就是你被练到要给出的答案。</span></li>",
 "<li><b>The scene</b><span>That rule happening at a table. You remember a picture, and the picture carries the rule with it.</span></li>":
   "<li><b>场景</b><span>那条规则在桌边发生的样子。你记住的是一幅画面，而画面把规则一起带着。</span></li>",
 "<li><b>The definition</b><span>The meaning you are tested on — short enough to hold, complete enough to rule with.</span></li>":
   "<li><b>释义</b><span>你被考的那个意思——短到记得住，全到能据此裁定。</span></li>",
 "<li><b>The rule line</b><span>The rule as you would say it to a player, in one breath.</span></li>":
   "<li><b>规则行</b><span>你会怎样对玩家说这条规则，一口气说完。</span></li>",
 "<li><b>The numbers</b><span>The category, the figures underneath, and the page of the reference document it comes from.</span></li>":
   "<li><b>数字</b><span>类别、底下的数值，以及它出自参考文档的哪一页。</span></li>",
 "A key turns that notes line into a map of all 24 card categories, and a second converts every distance and weight on the cards. Both ship inside the game, as do the English and German reference documents.":
   "一个按键把那行注解变成全部 24 个卡片类别的对照表，另一个按键换算卡片上的每一个距离与重量。两者都随游戏附带，英语和德语的参考文档也一样。",

 # ---- the editions ----
 '<span class="tag">Languages</span>': '<span class="tag">语言</span>',
 "<h2>Which edition you get</h2>": "<h2>你拿到的是哪个版本</h2>",
 "This pack is more honest about its languages than most, because they are genuinely not all the same thing. Three kinds:":
   "这个卡包在语言这件事上比大多数更直说，因为它们确实不是同一回事。共三种：",
 '<div class="h">German<span class="badge">Complete</span></div>':
   '<div class="h">德语<span class="badge">完整版</span></div>',
 "<b>A full German edition.</b> Everything in German — headword, definition, rule line, scene and notes on all 1,205 cards, and all 62 reference lessons. It uses the established German rules vocabulary, <i>Rüstungsklasse</i>, <i>Trefferpunkte</i>, <i>Rettungswurf</i>, rather than invented calques, and it cites the German rules edition page by page, so a card sends you to the right page of the book you actually own.":
   "<b>一个完整的德语版本。</b>全都是德语——全部 1,205 张卡片的词目、释义、规则行、场景与注解，以及全部 62 节参考课程。它用的是德语圈既有的规则词汇，<i>Rüstungsklasse</i>、<i>Trefferpunkte</i>、<i>Rettungswurf</i>，而不是生造的直译，并且逐页引用德语规则书，所以一张卡片会把你指向你手上那本书的正确页码。",
 '<div class="h">Japanese · Simplified Chinese · Russian · Spanish<span class="badge">Play in yours, answer in English</span></div>':
   '<div class="h">日语 · 简体中文 · 俄语 · 西班牙语<span class="badge">用你的语言游玩，用英语作答</span></div>',
 "The question and the scene are in your language; the headword you answer with, and the word you hear, are <b>English</b>. A toggle on the card shows the translation whenever you want it, and the 62 reference lessons are written in your language too.":
   "问题和场景用你的语言；你用来作答的词目，以及你听到的那个词，是<b>英语</b>。卡片上有一个开关，随时可以显示译文，62 节参考课程也用你的语言写成。",
 "<b>That is deliberate, not a shortcut.</b> You meet each rule in words you already think in, and you leave holding the term the table will actually use. It is the step you need before you sit down at an English-speaking game.":
   "<b>这是刻意的安排，不是省事。</b>你用自己本来就在用来思考的语言认识每一条规则，走的时候手里拿着桌边真正会用的那个术语。在你坐进一场英语的游戏之前，这一步是必需的。",
 '<div class="h">The all-in-your-language bonus<span class="badge">Beta</span></div>':
   '<div class="h">全用你的语言的附赠版本<span class="badge">测试版</span></div>',
 "If you would rather have the whole card in Japanese, Simplified Chinese, Russian or Spanish, that edition is there as well. It comes with compromises, stated plainly: <b>the spoken word stays English</b>, there is no audio beyond it, and it carries <b>no revision drills</b>. A bonus, not a course in its own right — you already speak your own language.":
   "如果你更想要整张卡片都是日语、简体中文、俄语或西班牙语，这个版本也有。它带着一些取舍，这里直说：<b>朗读的词仍然是英语</b>，除此之外没有音频，而且它<b>没有复习练习</b>。它是附赠，不是一门独立的课程——你自己的语言你已经会说了。",

 # ---- the tiers: whole <li> each ----
 ">The climb<": ">攀登<",
 "<h2>Five tiers, each ending in something you can do</h2>":
   "<h2>五个层级，每一级都以一件你做得到的事收尾</h2>",
 '<li><span class="w">Adjudicate a check</span><span class="d">The die, the DC, what the number is meant to mean, and the conditions that change it.</span></li>':
   '<li><span class="w">裁定一次检定</span><span class="d">骰子、DC、那个数字应当意味着什么，以及会改变它的各种状态。</span></li>',
 '<li><span class="w">Run a fight</span><span class="d">The turn, the actions in it, the damage types, and what a condition does to whoever is carrying it.</span></li>':
   '<li><span class="w">主持一场战斗</span><span class="d">回合、回合里的各种动作、伤害类型，以及一个状态会对带着它的人做什么。</span></li>',
 '<li><span class="w">Run a caster and read a stat block</span><span class="d">Slots, concentration, ranges — and a block of numbers you can look at and know what it will do.</span></li>':
   '<li><span class="w">操作施法者，读懂属性块</span><span class="d">法术位、专注、射程——以及一块你看一眼就知道它会干什么的数字。</span></li>',
 '<li><span class="w">Know what the options bring</span><span class="d">The twelve classes, the nine species, and what the feats actually give a character.</span></li>':
   '<li><span class="w">知道各种选项带来什么</span><span class="d">十二个职业、九个物种，以及专长究竟给一个角色什么。</span></li>',
 '<li><span class="w">Build encounters, hazards and treasure</span><span class="d">Challenge rating against experience, what a party survives, and what to hand out afterwards.</span></li>':
   '<li><span class="w">设计遭遇、危害与宝物</span><span class="d">挑战等级对上经验值、一支队伍扛得住什么，以及事后该发什么。</span></li>',
 "62 reference lessons, 82 pages, one waiting at the head of every cluster — in every language the pack ships.":
   "62 节参考课程，82 页，每个集群的开头都等着一节——卡包发行的每种语言都有。",

 # ---- the method: whole <dt>+<dd> each ----
 ">How it sticks<": ">为什么记得住<",
 "<h2>Flashcards as an integrated system</h2>": "<h2>把卡片做成一个完整的系统</h2>",
 "<dt>Cards</dt><dd><b>1,205 cards in 62 themed clusters</b> across five tiers, every one carrying its term, its scene, its definition, its rule line and its numbers.</dd>":
   "<dt>卡片</dt><dd><b>1,205 张卡片，分在 62 个主题集群里</b>，横跨五个层级，每一张都带着它的术语、场景、释义、规则行和数字。</dd>",
 "<dt>Boss fights</dt><dd>Three kinds, not one: <b>name the creature, spell or term</b> from its definition; <b>give your ruling</b> on a scene; <b>read the number</b> off a table. No cluster is cleared until its definitions are mastered.</dd>":
   "<dt>Boss 战</dt><dd>有三种，而不是一种：从释义<b>说出生物、法术或术语</b>；对一个场景<b>给出你的裁定</b>；从一张表里<b>读出那个数字</b>。一个集群里的释义没有掌握，这个集群就不算过关。</dd>",
 "<dt>Lessons</dt><dd><b>62 reference lessons, 82 pages</b> — one at the head of every cluster, in every language the pack ships.</dd>":
   "<dt>课程</dt><dd><b>62 节参考课程，82 页</b>——每个集群的开头一节，卡包发行的每种语言都有。</dd>",
 "<dt>Fibonacci SRS</dt><dd>Rate each card 0–5. The better you know a rule, the longer before it comes back.</dd>":
   "<dt>斐波那契 SRS</dt><dd>给每张卡片打 0–5 分。一条规则你记得越牢，它再回来的间隔就越长。</dd>",
 '<dt>Audio</dt><dd>The Guide reads aloud in its own bundled voice. Samples are on the <a href="voices.html">voices page</a>.</dd>':
   '<dt>音频</dt><dd>The Guide 用自带的语音朗读。试听在<a href="voices.html">语音页面</a>。</dd>',
 "<dt>The ruleset</dt><dd>The <b>2024 revision</b> as it now stands — the terms, the numbers and the procedures expected today. If your rules knowledge is a decade old, you relearn what changed by drilling what is, rather than reading a list of differences.</dd>":
   "<dt>规则版本</dt><dd><b>2024年修订版</b>，就是它现在的样子——今天所期待的术语、数字与流程。如果你的规则知识是十年前的，你靠练现行的内容来重新学会改动之处，而不是读一张差异清单。</dd>",

 # ---- the FAQ ----
 ">Questions<": ">问题<",
 "<h2>Before you buy</h2>": "<h2>购买之前</h2>",
 "<summary>Which edition of the rules is this?</summary>":
   "<summary>这是哪一版规则？</summary>",
 "The <b>2024 revision</b>, built from the System Reference Document 5.2. Conditions, spells, species and stat blocks were revised between the 2014 rules and these, so if your table runs the older edition some of these cards will drill you on numbers you do not use. Check which one your table plays before you buy.":
   "<b>2024年修订版</b>，依据 System Reference Document 5.2 构建。状态、法术、物种与属性块在 2014年规则和这一版之间经过修订，所以如果你那桌跑的是旧版，其中一些卡片会让你去练你用不到的数字。买之前先确认你那桌玩的是哪一版。",
 "<summary>Do I need the base game?</summary>": "<summary>我需要基础游戏吗？</summary>",
 'Yes. The Guide is DLC for FlashBoss, so you need the base game as well. On Windows 10 you also need <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a>, a free download from the Microsoft Store.':
   '需要。The Guide 是 FlashBoss 的 DLC，所以你还需要基础游戏。在 Windows 10 上你还需要 <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a>，可以从 Microsoft Store 免费下载。',
 "<summary>I am a player, not a game master. Is it for me?</summary>":
   "<summary>我是玩家，不是游戏主持人。这适合我吗？</summary>",
 "It is built for the person running the table, and that is where it pays most. A player who wants to stop asking what a condition does, or who is about to run their first game, gets the same cards — the tiers just matter less in that order.":
   "它是为带团的人做的，用在那里回报最大。如果你是玩家，想不再开口问某个状态有什么效果，或者快要带自己的第一场团，你拿到的是同样的卡片——只是层级的顺序对你没那么要紧。",
 "<summary>Is my language a full edition or a mixed one?</summary>":
   "<summary>我的语言是完整版还是混合版？</summary>",
 'German is the full edition. <b>Japanese, Simplified Chinese, Russian and Spanish</b> play in your language and answer in English, with a toggle to the translation on the card and the lessons written in your language — and each also carries an all-in-your-language bonus edition in beta, with English audio and no drills. The <a href="#editions">languages section</a> above says exactly what each one gives you.':
   '德语是完整版。<b>日语、简体中文、俄语和西班牙语</b>用你的语言游玩，用英语作答，卡片上有切换到译文的开关，课程也用你的语言写成——每一种还另外带一个全用你的语言的附赠版本，处于测试阶段，音频是英语，也没有练习。上面的<a href="#editions">语言一节</a>把每一种到底给你什么说得很清楚。',
 "<summary>Can I see the cards before I buy?</summary>":
   "<summary>买之前能先看看卡片吗？</summary>",
 'The card lists and reference lessons for FlashBoss packs are on this site, free and printable, and there is a <a href="https://flashboss-demo.pages.dev/">playable boss fight</a> if you want to see the mechanic before anything else.':
   'FlashBoss 各卡包的卡片列表与参考课程都在本站，免费，可打印；如果你想先看看这个机制，还有一场<a href="https://flashboss-demo.pages.dev/">可以直接玩的 Boss 战</a>。',

 # ---- the close ----
 "<h2>Know it, don't look it up.</h2>": "<h2>记住它，别去查它。</h2>",
 "1,205 cards, 62 clusters, and a boss fight at every one of them.":
   "1,205 张卡片，62 个集群，每一个集群都有一场 Boss 战。",
 "The Guide on Steam &rarr;": "在 Steam 上查看 The Guide &rarr;",

 # ---- the legal line: translated in full, all three prongs, nothing softened ----
 "5E compatible. Built from the System Reference Document 5.2. FlashBoss is not affiliated with, endorsed by, or sponsored by any rules publisher.":
   "兼容 5E。依据 System Reference Document 5.2 构建。FlashBoss 与任何规则出版商均无隶属关系，未获其认可，也未受其赞助。",
}

# Simplified Chinese strings for immersion.html.
# Canon sentences are LIFTED VERBATIM from the ratified Chinese bundle copy
# (flashboss-admin/BUNDLE_COPY_ROOTS_SERIES_2026-09-19.md) wherever that sheet
# has them — the ladder heading, the two start sentences, the immersion law,
# the floor/ceiling phrasing and the four pack one-liners. The rest is mine.
# Pack names stay English and sit bare inside the Chinese sentence: no 《》, no
# gloss, a single space on each side, which is what the live zh pages already do
# ("在 Steam 发售", "用 FlashBoss 学习").
# Numbers are the English page's, and zh keeps the comma separator, so 1,000
# is written 1,000 here exactly as on the English page.
#
# TERMINOLOGY, and the owner should look at this once:
#   cluster    = 词族      (ratified sheet)   — the live zh pages say 集群
#   boss fight = Boss 战   (ratified sheet)   — the live zh pages say 头目战
#   base game  = 基础游戏  (ratified sheet)   — the live zh pages say 基础版
# The sheet wins here because the brief ranks it above invention and it is what
# the Steam store shows for this exact product today, and because a page that
# quoted the sheet in half its sentences and the site in the other half would
# name the same thing twice. If the site is harmonised the other way, these
# three words are the whole diff.
#
# Punctuation: full-width inside Chinese sentences; &mdash; is kept as the
# entity where it separates two short labels (the band rows, the facts lines),
# and rendered as —— inside running prose, which is what the live zh pages do.
TITLE = "英语沉浸系统 — FlashBoss"
DESCRIPTION = ("一条路，六个步骤：English Advance、German Roots、Norman Roots、English Adept、"
               "Latin Roots、Greek Roots。用英语教英语，每个词族的结尾都有一场 Boss 战。")

STRINGS = {
 # ---- nav / chrome ----
 # NOTE: this key hits twice — the nav's own-page label AND <em>immersion</em>
 # in the immersion law, which one global replace cannot tell apart. So the value
 # has to work in both: 沉浸 is the nav label and is also the word the law
 # sentence goes on to name ("这正是 沉浸 这个词在这里所做的事"). The ratified
 # sheet localises the concept the same way ("沉浸正在于此"), and de does it too
 # (<em>Immersion</em>), so this is not one of the English words rule 5 protects.
 ">immersion<": ">沉浸<",
 ">packs<": ">卡包<",
 ">word lists<": ">单词列表<",
 ">lessons<": ">课程<",
 ">home<": ">主页<",
 ">voices<": ">语音<",
 ">resources<": ">资源<",
 ">how it works<": ">运作原理<",

 # ---- hero ----
 "English &middot;": "英语 &middot;",
 "six steps": "六个步骤",
 "&middot; one path": "&middot; 一条路",
 "The English immersion system": "英语沉浸系统",
 "one path, six steps": "一条路，六个步骤",
 "Whether English is your first language or your second:":
   "无论英语是你的母语还是第二语言：",
 "a six-step path through survival and out the other side of mastery.":
   "一条六步的路，从生存起步，穿过精通，再从另一头走出来。",
 "Two steps ship free with the game. Four are the Roots packs. Every card is English, taught in English.":
   "其中两步随游戏免费附带。四步是 Roots 扩展包。每张卡片都是英语，用英语来教。",
 "the packs": "全部卡包",

 # ---- the ladder ----
 "The ladder": "阶梯",
 "One path, six steps": "一条路，六个步骤",
 "The base game holds the floor and the ceiling of a normal immersion course. Two Roots packs sit inside it, two sit beyond it. Read the ladder top to bottom.":
   "基础游戏撑起一门正常沉浸课程的地板与天花板。两个 Roots 扩展包在课程之内，另外两个在课程之外。阶梯请从上往下读。",
 "Floor &mdash; base game": "地板 &mdash; 基础游戏",
 "Inside the course &mdash; DLC": "课程之内 &mdash; DLC",
 "Ceiling &mdash; base game": "天花板 &mdash; 基础游戏",
 "Beyond the course &mdash; DLC, elective": "课程之外 &mdash; DLC，选修",
 "Optional": "可选",
 "Inside": "课程之内",
 "Ceiling": "天花板",
 "Beyond": "课程之外",

 "500 cards &middot; 500 words &middot; 25 clusters &middot; 15 lessons &middot; ships with the game":
   "500 张卡片 &middot; 500 个单词 &middot; 25 个词族 &middot; 15 节课 &middot; 随游戏附带",
 "The English of everyday tasks &mdash; forms, notices, instructions, offices. Read a form and fill it, follow written directions, hold the words that officialdom uses about you. The one optional door on the path.":
   "日常事务的英语——表格、告示、说明、机关窗口。读懂一张表格并把它填好，照着书面指示走，掌握官方用在你身上的那些词。这条路上唯一一道可选的门。",
 "1,000 cards &middot; 47 clusters &middot; 48 lessons":
   "1,000 张卡片 &middot; 47 个词族 &middot; 48 节课",
 "The Germanic half of English: the plain words, the compounds whose seam has gone invisible, and the native prefixes &mdash;":
   "英语中日耳曼语的那一半：朴素的词、接缝已看不出的复合词，以及本族前缀——",
 "1,000 cards &middot; 48 clusters &middot; 49 lessons":
   "1,000 张卡片 &middot; 48 个词族 &middot; 49 节课",
 "The Old French layer that settled on top of the Germanic one. Every card names the twins:":
   "覆盖在日耳曼语层之上的古法语层。每张卡片都点出孪生词：",
 ", and the pack teaches the typical French spellings you learn to spot.":
   "，这个扩展包还教那些你会学着一眼认出的典型法语拼写。",
 "1,000 cards &middot; 56 clusters &middot; 12 lessons &middot; synonyms on all 1,000 cards &middot; ships with the game":
   "1,000 张卡片 &middot; 56 个词族 &middot; 12 节课 &middot; 1,000 张卡片全部配同义词 &middot; 随游戏附带",
 "The articulate vocabulary of an adult reader, grouped by what it does. Read adult prose without stalling; have the word you actually meant, not the nearest one. Just to the end of Adept is a valuable resource for a high-schooler.":
   "成年读者谈吐自如的词汇，按各自的用处分组。读成人文章不再卡壳；用得出你真正想用的那个词，而不是最接近的那个。只走到 Adept 的终点，对一名中学生也已经是一份有价值的资源。",
 "500 cards = 1,000 words (a paired cousin on every card) &middot; 30 clusters &middot; 31 lessons":
   "500 张卡片 = 1,000 个单词（每张卡片配一个同源的亲属词） &middot; 30 个词族 &middot; 31 节课",
 "Famous Latin, everyday Latin, the prefixes, the great root families &mdash;":
   "著名的拉丁语、日常的拉丁语、前缀、几大词根家族——",
 "&mdash; and the suffixes.": "——以及后缀。",
 "teaches": "教出",
 "in the same breath.": "是同一口气的事。",
 "1,000 cards &middot; 56 clusters &middot; 62 lessons &middot; the Greek script on all 1,000":
   "1,000 张卡片 &middot; 56 个词族 &middot; 62 节课 &middot; 1,000 张卡片全部呈现希腊字母",
 "suffixes, hybrids flagged as hybrids. An unfamiliar technical word stops being unfamiliar.":
   "词尾，混合词会被标注为混合词。一个陌生的专业词不再陌生。",

 # ---- S4, verbatim from the ratified Chinese bundle copy ----
 # The sheet's start sentence is language-neutral in zh — unlike the German and
 # Spanish sheets, it does not point the reader at their own family's pack. The
 # companion sentence is left as the sheet writes it, a conditional on a Romance
 # mother tongue: Chinese is neither Germanic nor Romance, so the condition
 # simply does not fire and nothing contradicts "从 German Roots 起步".
 "Start at Advance if school let you down or English is new to you. Otherwise start at German Roots.":
   "如果学校的英语没能帮到你，或者你刚接触英语，就从 Advance 开始。否则请从 German Roots 起步。",
 "If your first language is a Romance one, take Norman Roots before German Roots.":
   "若你的母语属于罗曼语族，先学 Norman Roots，再学 German Roots。",
 "The base game has the floor and the ceiling. German Roots and Norman Roots sit inside the course. Latin Roots and Greek Roots sit beyond it. English Advance is elective if you had a standard education. Latin Roots and Greek Roots are elective in full. There is no requirement to take the packs in order; the ladder is the recommendation.":
   "基础游戏撑起地板与天花板。German Roots 和 Norman Roots 位于课程之内。Latin Roots 和 Greek Roots 则在课程之外。如果你受过常规教育，English Advance 是选修。Latin Roots 和 Greek Roots 完全是选修。扩展包不要求按顺序学；阶梯只是建议。",

 # ---- the two pairs ----
 "Inside the course": "课程之内",
 "The two layers English is made of": "构成英语的两层",
 "German Roots and Norman Roots are the pair inside the course.":
   "German Roots 和 Norman Roots 是课程之内的一对。",
 "They are the two layers English is stitched from &mdash; the one it kept from before 1066, and the one that landed with the Conquest &mdash; and they sit between":
   "它们是英语缝合而成的两层——一层是英语从 1066 年之前留下来的，一层随征服一同登陆——它们位于",
 "</b> and <b>English Adept</b>.": "</b> 与 <b>English Adept</b> 之间。",
 "They are the reason English has": "也正因如此，英语才会同时有",
 ". At the end of German Roots you see the seam in a compound word and read the meaning off it. At the end of Norman Roots you read the second layer of English as a layer, not as a list of hard words.":
   "。学完 German Roots，你能看见复合词里的接缝，并据此读出词义。学完 Norman Roots，你把英语的第二层当作一层来读，而不是当作一串难词。",
 "Step 2 &middot; 1,000 cards &middot; 47 clusters &middot; 48 lessons":
   "第 2 步 &middot; 1,000 张卡片 &middot; 47 个词族 &middot; 48 节课",
 "The Germanic backbone of everyday English &mdash; the words you already half-know. Where a Germanic speaker begins, and the default for everyone else.":
   "日常英语的日耳曼语骨架——那些你已经半懂的词。说日耳曼语的人从这里开始，其他人则以此为默认起点。",
 "Learn more &rarr;": "了解更多 &rarr;",
 "Step 3 &middot; 1,000 cards &middot; 48 clusters &middot; 49 lessons":
   "第 3 步 &middot; 1,000 张卡片 &middot; 48 个词族 &middot; 49 节课",
 "The second English &mdash; 1066 and the French that came with it. Where a Romance speaker begins.":
   "第二种英语——1066 年，以及随之而来的法语。说罗曼语的人从这里开始。",

 "Beyond the course": "课程之外",
 "Past the ceiling, for the curious": "越过天花板，留给好奇的人",
 "Latin Roots and Greek Roots are the pair beyond the course.":
   "Latin Roots 和 Greek Roots 是课程之外的一对。",
 "They come after": "它们排在",
 ", for readers who want the scholarly layer and the vocabulary of the sciences. A hobby for the linguistically curious, and none the worse for it.":
   " 之后，面向想要学术层与科学词汇的读者。这是语言好奇者的一项爱好，并不因此逊色。",
 "Part of the course, and past the point where anyone needs them. At the end of the pair an unfamiliar technical or literary word is not unfamiliar: you take it apart on sight, and the boundaries between European languages have started to look like dialect boundaries.":
   "既是课程的一部分，也已越过任何人所需的边界。学完这一对，陌生的专业词或文学词不再陌生：你一眼就能把它拆开，而欧洲各语言之间的界线，开始看起来像方言的界线。",
 "Step 5 &middot; 500 cards = 1,000 words &middot; 30 clusters &middot; 31 lessons":
   "第 5 步 &middot; 500 张卡片 = 1,000 个单词 &middot; 30 个词族 &middot; 31 节课",
 "English built from its parts &mdash; the classical and scientific layer, assembled. Every card teaches a paired cousin word beside the headword.":
   "用部件组装起来的英语——古典与科学的那一层，拼装完成。每张卡片都在词目旁边教一个同源的亲属词。",
 "Step 6 &middot; 1,000 cards &middot; 56 clusters &middot; 62 lessons":
   "第 6 步 &middot; 1,000 张卡片 &middot; 56 个词族 &middot; 62 节课",
 "The vocabulary of science, medicine, and abstraction &mdash; the layer above Latin, with the Greek script on the card.":
   "科学、医学与抽象的词汇——拉丁语之上的那一层，卡片上直接呈现希腊字母。",
 "Latin Roots and Greek Roots come after Adept, in whichever order you like.":
   "Latin Roots 和 Greek Roots 排在 Adept 之后，先学哪个由你决定。",

 # ---- the table ----
 "Step by step": "一步一步",
 "What you get": "你会得到什么",
 "Counted from the pack trees, not from copy. Five tiers in every pack. A boss fight at the end of every cluster.":
   "数字是从卡包本身数出来的，不是从文案里抄的。每个扩展包五个层级。每个词族结尾都有一场 Boss 战。",
 ">Step<": ">步骤<",
 ">Cards<": ">卡片<",
 ">Words<": ">单词<",
 ">Clusters<": ">词族<",
 ">Lessons<": ">课程<",
 ">Ships as<": ">发行方式<",
 ">base game<": ">基础游戏<",
 "Latin Roots is 500 cards because every one of the 500 teaches a paired cousin word beside the headword: 1,000 words. Where a step shows fewer lessons than clusters (Advance, Adept), its lessons are chapter openings rather than a door on every cluster; the four Roots packs have a lesson at every cluster door, and lessons there are mandatory.":
   "Latin Roots 是 500 张卡片，因为这 500 张每一张都在词目旁边教一个同源的亲属词：共 1,000 个单词。凡是课程数少于词族数的步骤（Advance、Adept），它的课程是章节的开场，而不是每个词族都有一道门；四个 Roots 扩展包在每个词族的门口都有一节课，那里的课程是必修。",

 # ---- the card / the play ----
 "On every card, in every step": "每一步的每一张卡片上",
 "The same card anatomy from the floor to the last Greek root.":
   "从地板到最后一个希腊语词根，卡片的构造始终一样。",
 "The card": "卡片",
 "The play": "玩法",
 "boss fight": "Boss 战",
 "at the end of every cluster &mdash; eight headwords on the grid, answered on the numberpad":
   "位于每个词族的结尾——网格上八个词目，用小键盘作答",
 "Fibonacci spaced repetition": "斐波那契间隔重复",
 "between the fights": "穿插在两场战斗之间",
 "lesson at every cluster door": "每个词族的门口都有一节课",
 "in all four Roots packs": "四个 Roots 扩展包都是如此",
 "<li>three <b>": "<li>每个扩展包三种 <b>",
 "revision drills": "复习练习",
 "per pack: the roots rack, antonyms and cloze in German, Latin and Greek Roots; dictation in place of the rack for Norman Roots (its cards are single Old French words, not sums) and for Adept":
   "分别是：词根架、反义词与填空，见于 German、Latin 和 Greek Roots；Norman Roots 与 Adept 用听写代替词根架（它们的卡片是单个古法语词，而不是部件之和）",

 # ---- the fight ----
 "The gate": "关口",
 "Every cluster ends in a fight": "每个词族都以一场 Boss 战收尾",
 "Eight headwords on the grid, answered on the numberpad. A right answer moves you one step along the track.":
   "网格上八个词目，用小键盘作答。答对一题，在赛道上前进一步。",
 "A wrong one puts you": "答错一题，会把你",
 "two steps back": "推后两步",
 ", and the cards you are worst at are the ones waiting at positions three and four — so a cluster cannot be beaten until its hardest words are.":
   "，而你最不熟的那些卡片，正等在第三、第四位——所以不拿下一个词族里最难的词，就拿不下这个词族。",
 "Beat it and those cards leave your daily deck for good.":
   "打赢它，这些卡片就永远离开你的每日卡组。",
 "Fight one yourself &rarr;": "亲自打一场 &rarr;",
 "try the demo": "试玩演示",

 # ---- the law: S3 and S6 verbatim from the ratified Chinese bundle copy ----
 "The immersion law": "沉浸法则",
 "English, whatever the menus say": "无论菜单说什么，卡片都是英语",
 "Card text is English whatever the interface language.":
   "无论界面语言是什么，卡面文字都是英语。",
 "The interface, the cluster names and the Advance lessons are translated into German, Spanish, Japanese, Russian and Chinese. The cards never are &mdash; not one card in any of the six packs carries a foreign-language field. That is what the word":
   "界面、词族名称和 Advance 的课程有德语、西班牙语、日语、俄语和简体中文版本。卡片则从不翻译——六个扩展包里没有任何一张卡片带有外语字段。这正是",
 "is doing here.": "这个词在这里所做的事。",
 "Every pack carries the British/American spelling split as a layer: a British twin of the headword, both example sentences, the definition and the notes, wherever the British text differs from the American, chosen by your spelling preference or your English voice.":
   "每个扩展包都把英式与美式拼写的分野做成一个层：凡是英式文本与美式不同之处，词目、两个例句、释义与注解都另有一个英式的孪生版本，由你的拼写偏好或英语语音设定决定。",

 # ---- the series ----
 "The full immersion series": "完整沉浸系列",
 "Six steps, one series": "六个步骤，一个系列",
 "The six steps are one series: the four Roots DLCs &mdash; German and Norman inside the course, Latin and Greek beyond it &mdash; together with the base game that carries English Advance and English Adept. Taken as the series, the floor, the two layers of English, the ceiling and the two Roots past it arrive as a single course rather than six separate packs. Available on Steam.":
   "这六个步骤是一个系列：四个 Roots DLC——German 与 Norman 在课程之内，Latin 与 Greek 在课程之外——加上带着 English Advance 和 English Adept 的基础游戏。作为一个系列来看，地板、英语的两层、天花板，以及越过天花板的那两个 Roots，会作为一门完整课程到来，而不是六个各自独立的卡包。已在 Steam 发售。",
 # The store listing's own localised name, from the ratified sheet — this is the
 # zh title of the bundle on Steam, not one of the six pack names, so it is the
 # one place "Roots" appears in Chinese.
 "FlashBoss Roots — The Complete Series": "FlashBoss 词根 — 完整系列",
 "is the five items in one: the base game, which\n      carries English Advance and English Adept inside it free, and the four Roots packs. Already own part of\n      it? Steam charges you only for the rest.":
   "把五件商品合为一件：基础游戏（它免费带着 English Advance 和 English Adept），以及四个 Roots 扩展包。已经拥有其中一部分？Steam 只收取其余部分的费用。",
 "The Complete Series &rarr;": "完整系列 &rarr;",
 "FlashBoss &middot; base game": "FlashBoss &middot; 基础游戏",
 "Start where the ladder says.": "从阶梯指给你的地方开始。",
 "The floor and the ceiling ship free with the game. The four Roots packs are on Steam, together or one at a time.":
   "地板与天花板随游戏免费附带。四个 Roots 扩展包在 Steam 上发售，可以一起买，也可以一个一个买。",
 "Knowledge is power": "知识就是力量",

 # ---- the card list: whole <li> each, so no English article survives ----
 "<li>the <b>headword</b>, in English</li>": "<li><b>词目</b>，英语</li>",
 "<li>a <b>definition</b>, in English &mdash; never a translation</li>":
   "<li><b>释义</b>，英语——从不使用翻译</li>",
 "<li>an <b>example sentence</b></li>": "<li><b>例句</b></li>",
 "<li>a <b>second example</b> &mdash; the same word again, or a related word, the cousin or twin that the notes go on to explain</li>":
   "<li><b>第二个例句</b>——同一个词再出现一次，或者一个相关的词，也就是注解接下来要讲的亲属词或孪生词</li>",
 "<li>a <b>Notes</b> line: part of speech, the parts the word is built from, the etymon</li>":
   "<li>一行 <b>Notes</b>：词性、这个词由哪些部件构成，以及词源</li>",
 "<li><b>synonyms</b> on every card of Adept, German Roots, Norman Roots and Greek Roots; antonyms where a true one exists</li>":
   "<li>Adept、German Roots、Norman Roots 和 Greek Roots 的每张卡片都有<b>同义词</b>；确有真正反义词的，也给出反义词</li>",
 "<li>the <b>British/American spelling split</b>, as a layer &mdash; see below</li>":
   "<li><b>英式与美式拼写的分野</b>，作为一个层——见下文</li>",

 # ---- fragments that sit between <em> pairs ----
 "</em> and <em>": "</em> 和 <em>",
 "</em> / Germanic <em>": "</em> / 日耳曼语 <em>",
 "</em> / Latin <em>": "</em> / 拉丁语 <em>",
 " &mdash; the roots, the number and size prefixes, the ":
   "——词根、表示数目与大小的前缀，以及 ",
 # ---- the fight GIF's alt: the zh capture, so it says what is on screen.
 #      bossfight-immersion.zh.gif is a Latin Roots fight with a Chinese
 #      interface and English card text — the immersion law made visible, so the
 #      alt says both halves out loud. ----
 "A Latin Roots boss fight in the real game: the boss asks which word means a glass tank for fish, the answer aquarium lands, and the cluster is conquered — its eight words leaving rotation.":
   "真实游戏中的一场 Latin Roots Boss 战：界面是简体中文，卡面文字是英语。头目问哪个词指养鱼的玻璃缸，答案 aquarium 落位，这个词族被攻克——它的八个词离开轮转。",

 # the two <li>s whose leading article no key covered: dropping it matches the
 # other bullets, which carry no article in any locale.
 "<li>a <b>": "<li><b>",

 # CJK punctuation between the example pairs: the English page separates them
 # with an ASCII comma, which reads as a gap in Chinese.
 "</em>, <em>": "</em>、<em>",
 # Same class of fix: the German Roots gist ends its Chinese sentence on an
 # ASCII full stop, because the stop sits outside every prose key
 # (…&mdash; <em>be-, fore-, …, up-</em>.). The only other "</em>." on the page
 # is <em>demand</em>., and the long S-sentence that starts ". At the end of
 # German Roots" has already consumed it by the time this short key runs.
 "</em>.": "</em>。",
}

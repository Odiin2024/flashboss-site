# Simplified Chinese strings for latin.html — the Latin LANGUAGE COURSE page
# (Latin Core + Latin Pareto), not the Latin Roots English pack.
#
# The key set is latin_de.py's, key for key and in the same order: that file is
# the worked example for this page and fixes which strings exist.
#
# WHERE THE WORDS COME FROM, in order of authority:
#   * the cluster names are the GAME's own Chinese names, lifted byte for byte
#     from the shipped list (scratchpad clusters_latin_zh.txt). Not one is mine.
#     The same names are reused in the tier blurbs where the English blurb names
#     a cluster in lower case — 指代词, 连接词, 核心动词, 元老院与利剑,
#     日常诸务, 公共广场, 漫漫长路, 流转之年 — so the page and the game agree.
#   * the bundle name is the ratified Chinese one from the Latin paste sheet
#     (flashboss-admin/BUNDLE_COPY_LATIN_2026-09-08.md): FlashBoss 拉丁语 — 完整课程,
#     em dash U+2014, both halves localised. The Steam URLs and app IDs are
#     untouched.
#   * the immersion page's zh glossary owns the recurring terms: 词族, Boss 战,
#     基础游戏, 卡片, 词目, 单词列表, 课程, 语音, 斐波那契间隔重复, 试玩演示.
#   * french.zh.html is this same page template already translated by the
#     fleet, so its wording owns the shared furniture: 听 · 读 · 重复 · 评分 ·
#     战斗, 全景地图, 看例句成长, 一眼认出, 点击翻面, 不只是一份单词列表,
#     为何记得住, 闪卡组成的完整系统, 层级 N, 常见问题, the SRS and graduation
#     lines, 游玩还需要别的什么吗, 买之前能看到单词吗, 有试玩吗.
#   * the hero alt is the string the other Chinese pages already carry.
#
# TERMINOLOGY, and the owner should look at this once — two ratified sheets for
# this locale disagree and the glossary wins here, as it did on the Swahili page:
#   cluster    = 词族    — the Roots sheet, immersion.zh.html, swahili.zh.html
#                          and in-development.zh.html. THIS Latin sheet
#                          (2026-09-08) says 集群, and so does french.zh.html.
#   boss fight = Boss 战 — same split: the Latin sheet says 头目, french.zh.html
#                          says 头目战.
# The brief tells me to reuse the glossary, and a locale that called one thing
# two names on two pages would read as two products. If the site is harmonised
# the other way, these two words are the whole diff.
#
# PAGE CANON, held here:
#   * Latin is never translated. Every Latin example sentence, every dictionary
#     form (virtūs, f., -is — the genitive shorthand stays exactly as written),
#     every siglum and citation (Caes. BG 5.44.5, Cic. Verr. 2.2.108,
#     Sall. Cat. 60.7, Caes. BG 6.30.2) and the ten ladder lines are
#     byte-identical. Only the explanation and the gloss around them is Chinese.
#   * pack names stay English and sit bare inside the Chinese sentence, one
#     space each side, no 《》 and no bracketed gloss: Latin Core, Latin Pareto,
#     Core, Pareto. So do FlashBoss, Steam, DLC, Windows Terminal, Microsoft
#     Store and the voice id la_LA-flashboss_m. "Latin Pareto" is the store
#     name — never "Pareto 1".
#   * the counts are the page's own recount of 2026-09-19 and are reproduced
#     exactly: Latin Core 26 参考课程, Latin Pareto 18, 44 in total, 80 词族,
#     2,000 cards, 17,007 words read in context, 1,052 cited, 813 unaltered,
#     1,320 macronned. zh keeps the comma separator, so every figure is written
#     as the English page writes it.
#   * grammar terms are the ordinary Chinese ones: 宾格, 属格, 与格, 夺格,
#     第三变格法, 变位, 未完成时, 完成时, 关系从句, 分词, 被动式, 独立夺格,
#     异态动词, 不定式, 间接引语, 虚拟式, 动名词, 动形词. A macron is 长音符,
#     a lemma 词条, a headword 词目, a citation 出处.
#   * banned and absent: hours, CEFR codes, prices, dates.
#
# Punctuation: full-width inside Chinese sentences, 、 between example pairs,
# and the em dash rendered —— in running prose, which is what the live zh pages
# do. The page's own " · " separators are left alone.
TITLE = "拉丁语 — FlashBoss"
DESCRIPTION = ("FlashBoss 拉丁语：一门 2,000 词的阅读课程，分十个层级、八十个词族，"
               "配 44 节参考课程、标注长音符的词目，以及最终走向未经改编的凯撒、西塞罗、"
               "萨卢斯特、奈波斯与李维的例句。Latin Core 与 Latin Pareto 已在 Steam 发售。")

STRINGS = {
 # ---- nav / chrome ----
 ">home<": ">主页<",
 ">packs<": ">卡包<",
 ">resources<": ">资源<",
 ">walkthrough (beta)<": ">攻略手册（beta）<",
 '<span class="here">Latin</span>': '<span class="here">拉丁语</span>',

 # ---- hero ----
 "FlashBoss — the moonlit school that fronts every FlashBoss course":
   "FlashBoss——月光下的学舍，每一门课程的门面",
 "Two packs · <b>2,000 words</b> · ten tiers · 44 lessons · out now on Steam":
   "两个卡包 · <b>2,000 个单词</b> · 十个层级 · 44 节课程 · 已在 Steam 发售",
 "Read real Latin. Not books about it.": "读真正的拉丁语，不是关于拉丁语的书。",
 "Listen · Read · Repeat · Rate · Fight": "听 · 读 · 重复 · 评分 · 战斗",
 "Two thousand words, ten tiers, one skill. The sentences start built for you and end as <b>Caesar, Cicero, Sallust, Nepos and Livy actually wrote them</b> — nothing trimmed but length, nothing invented.":
   "两千个单词，十个层级，一项技能。例句起初是为你而造的，到最后则是<b>凯撒、西塞罗、萨卢斯特、奈波斯与李维真正写下的样子</b>——删去的只有长度，没有一处是编出来的。",
 ">Word Lists<": ">单词列表<",
 ">Lessons<": ">课程<",
 ">Try the demo<": ">试玩演示<",

 # ---- the argument: one skill, and the order that teaches it ----
 "Latin course design": "拉丁语课程的设计",
 "One skill: reading": "一项技能：阅读",
 "Legendō discitur — it is learned by reading.":
   "Legendō discitur——它是靠阅读学会的。",
 "Nothing here asks you to compose Latin of your own. The whole course is built so that you can look at a printed line and know what it says — and it gets you there by putting you in front of sentences from the very first tier, not by making you wait until the grammar is finished.":
   "这里没有一处要求你自己写拉丁语。整门课程的搭建，只为让你看着印出来的一行字就知道它在说什么——而它带你到那里的办法，是从第一个层级起就把句子摆在你面前，而不是让你等到语法讲完。",
 "The order is the argument. Two thousand lemmas are laid down in ten tiers, each tier eight clusters of twenty-five cards, and the grammar arrives one lesson at a time at the exact card that first needs it. No example sentence ever uses grammar you have not been taught. By Tier 10 the ladder has nothing left to teach and you are reading Cicero unadapted — <b>17,007 words of Latin read in context</b> along the way.":
   "顺序本身就是论证。两千个词条铺成十个层级，每个层级八个词族，每个词族二十五张卡片，语法则一次一节课，恰好落在第一次需要它的那张卡片上。任何例句都不会用到你还没学过的语法。到了层级 10，阶梯已经没有东西可教，你读的是未经改编的西塞罗——一路上<b>在上下文中读过 17,007 个拉丁语词</b>。",

 "Latin Core — tiers 1 to 5": "Latin Core——层级 1 至 5",
 "Latin Pareto — tiers 6 to 10": "Latin Pareto——层级 6 至 10",
 "The alphabet as Rome said it, the pointing words, the connectives, the prime movers, the first nouns of senate and sword.":
   "罗马人读出来的字母表、指代词、连接词、核心动词，以及元老院与利剑的头一批名词。",
 "The accusative, the present tense, the imperative. The daily round, the forum, the body, counting and worth.":
   "宾格、现在时、命令式。日常诸务、公共广场、身体、计数与价值。",
 "Genitive and dative, the full plural, two more conjugations, the imperfect. The road, the household, the turning year.":
   "属格与与格、完整的复数、另外两种变位、未完成时。漫漫长路、家宅、流转之年。",
 "The ablative, the third declension, prepositions and case — and the first real Caesar, lightly adapted.":
   "夺格、第三变格法、介词与格——以及第一段真正的凯撒，略作改编。",
 "The perfect and its family, principal parts, relative clauses. Caesar is now on 86 of the 200 cards, and unadapted on 26 of them.":
   "完成时及其家族、动词的基本形式、关系从句。凯撒此时占了 200 张卡片中的 86 张，其中 26 张未经改编。",
 "Participles, all three of them, and the passive. Caesar continues, and Nepos comes into his own.":
   "分词，三种全在，以及被动式。凯撒继续，奈波斯开始站到台前。",
 "The ablative absolute, the passive complete, deponents. Cicero's letters open the informal register.":
   "独立夺格、被动式讲完、异态动词。西塞罗的书信打开了非正式的语域。",
 "The infinitive family and reported speech. Sallust arrives; 192 of 200 cards are now unadapted.":
   "不定式家族与间接引语。萨卢斯特到场；200 张卡片中已有 192 张未经改编。",
 "The subjunctive, cum-clauses, purpose and result, indirect questions. Livy joins the roll.":
   "虚拟式、cum 从句、目的与结果、间接疑问句。李维加入名册。",
 "Gerund and gerundive, and how to read a citation. Cicero's speeches and philosophy close the trunk.":
   "动名词与动形词，以及怎样读一条出处。西塞罗的演说与哲学为主干收尾。",

 # ---- the sentence ladder: Latin stays Latin, the gloss becomes Chinese ----
 "Watch it grow up": "看例句成长",
 "From made for you to written by Cicero": "从「为你而造」到「西塞罗所写」",
 "One card's example sentence from each of the ten tiers, in order. Nothing below is a paraphrase: from Tier 4 the citations are real, and the unmarked ones are the author's own words.":
   "十个层级各取一张卡片的例句，按顺序排列。下面没有一句是转述：从层级 4 起，出处都是真的，未加标注的就是作者本人的原话。",
 "<span class=\"en\">As you see, Caesar is one of ours.</span>":
   "<span class=\"en\">如你所见，凯撒是我们这边的人。</span>",
 "<span class=\"en\">While Caesar is in Gaul, the senate approves the law.</span>":
   "<span class=\"en\">凯撒在高卢期间，元老院通过了这条法律。</span>",
 "<span class=\"en\">Our troops were already departing and abandoning the camp.</span>":
   "<span class=\"en\">我们的部队已经在撤离，正放弃营地。</span>",
 "<span class=\"en\">The storms both kept our men in camp and held the enemy back from battle.</span>":
   "<span class=\"en\">风暴既把我们的人困在营中，也让敌人无法出战。</span>",
 "<span class=\"en\">There he reached the furthest ridge and drew up his line in that place.</span>":
   "<span class=\"en\">他在那里抵达最远的山脊，并就地摆开战线。</span>",
 "<span class=\"en\">Not even Vorenus keeps himself behind the rampart then; fearing what everyone would think, he follows after.</span>":
   "<span class=\"en\">那一刻连沃雷努斯也没有待在壁垒后面；他顾忌众人的看法，便跟了上去。</span>",
 "<span class=\"en\">All the ties of the closest friendship hold between him and me.</span>":
   "<span class=\"en\">最亲密交谊的一切纽带，都维系在他与我之间。</span>",
 "<span class=\"en\">At home we have want, abroad debt, a bad case and a prospect much harsher still.</span>":
   "<span class=\"en\">在家是匮乏，在外是负债，处境不佳，前景更为严酷。</span>",
 "<span class=\"en\">Seeing his forces routed and himself left with a few, mindful of his birth and former standing, Catiline charges into the thickest of the enemy and there, fighting, is run through.</span>":
   "<span class=\"en\">喀提林见自己的军队溃散、身边只剩下少数人，便念及出身与昔日的地位，冲进敌阵最密处，在那里边战边被刺穿。</span>",
 "<span class=\"en\">You see that man with the rather curly hair, the dark one, who watches us with a look that makes him seem very sharp to himself.</span>":
   "<span class=\"en\">你们看那个头发略带鬈曲、肤色黝黑的人，他望着我们的那副神情，仿佛自以为十分精明。</span>",
 ">built for the tier<": ">为该层级而造<",
 ">adapted from Caes. BG 4.34.4<": ">改编自 Caes. BG 4.34.4<",

 # ---- whose Latin: the source arc ----
 "Whose Latin": "谁的拉丁语",
 "The authors arrive in order": "作者依序登场",
 "Tiers 1 to 3 have no citations at all, and say so: those sentences are built to a grammar ceiling, because real Latin has no register that simple. Caesar enters at Tier 4 and the scaffolding is gone by Tier 8.":
   "层级 1 至 3 完全没有出处，而且明说了：那些句子是按语法上限造出来的，因为真正的拉丁语没有那么简单的语域。凯撒在层级 4 登场，到层级 8 脚手架已经撤光。",
 ">Tiers 1–3<": ">层级 1–3<",
 "Sentences constructed to the tier's grammar — no author claimed, none implied":
   "按该层级语法造出的句子——不声称有作者，也不暗示有",
 ">0 of 600 cited<": ">600 张中 0 张有出处<",
 "Caesar, <i>Gallic War</i> — mostly clause-trimmed for length":
   "凯撒，<i>高卢战记</i>——多数为控制长度删去了从句",
 ">62 cited · 13 unadapted<": ">62 张有出处 · 13 张未经改编<",
 "Caesar throughout, Nepos beginning": "通篇是凯撒，奈波斯开始出现",
 ">86 cited · 26 unadapted<": ">86 张有出处 · 26 张未经改编<",
 "Caesar and Nepos, <i>Lives</i>": "凯撒与奈波斯，<i>名人传</i>",
 ">145 cited · 84 unadapted<": ">145 张有出处 · 84 张未经改编<",
 "Cicero's letters — <i>ad Atticum</i>, <i>ad Familiares</i> — beside Caesar and Nepos":
   "西塞罗的书信——<i>ad Atticum</i>、<i>ad Familiares</i>——与凯撒、奈波斯并列",
 ">170 cited · 109 unadapted<": ">170 张有出处 · 109 张未经改编<",
 "Sallust joins; the adapting effectively stops":
   "萨卢斯特加入；改编实际上到此为止",
 ">196 cited · 192 unadapted<": ">196 张有出处 · 192 张未经改编<",
 "Livy Book 1 joins Sallust, Cicero and Caesar":
   "李维第 1 卷加入萨卢斯特、西塞罗与凯撒",
 ">197 cited · 195 unadapted<": ">197 张有出处 · 195 张未经改编<",
 "Cicero's speeches and philosophy — the hardest band the trunk reaches":
   "西塞罗的演说与哲学——主干所能达到的最难一档",
 ">196 cited · 194 unadapted<": ">196 张有出处 · 194 张未经改编<",
 "Across the two packs, <b>1,052 of the 2,000 example sentences carry a citation</b>, and 813 of those are the author's own unaltered words. Every citation on every card names its book, chapter and section, and Lesson 41 teaches you how to read one.":
   "两个卡包合起来，<b>2,000 个例句中有 1,052 个带着出处</b>，其中 813 个是作者本人未经改动的原话。每张卡片上的每一条出处都写明卷、章、节，第 41 课教你怎么读它。",

 # ---- the tier and cluster ledger; the cluster names are the game's own ----
 "The whole map": "全景地图",
 "Ten tiers, eighty clusters": "十个层级，八十个词族",
 "Every cluster is 25 cards and ends in a boss fight. Nothing is hidden — the full list is on the <a href=\"wordlists.html?lang=Latin&amp;set=Core\">word lists page</a>, free to read before you buy.":
   "每个词族 25 张卡片，以一场 Boss 战收尾。没有任何隐藏——完整列表就在<a href=\"wordlists.html?lang=Latin&amp;set=Core\">单词列表页面</a>，购买前即可免费阅读。",
 ">Tier 1<": ">层级 1<",
 ">Tier 2<": ">层级 2<",
 ">Tier 3<": ">层级 3<",
 ">Tier 4<": ">层级 4<",
 ">Tier 5<": ">层级 5<",
 ">Tier 6<": ">层级 6<",
 ">Tier 7<": ">层级 7<",
 ">Tier 8<": ">层级 8<",
 ">Tier 9<": ">层级 9<",
 ">Tier 10<": ">层级 10<",
 "The Pointing Words · The Joints · The Links · The Prime Movers · Senate &amp; Sword · Many &amp; Mighty · The Lay of Things · The Marshalling":
   "指代词 · 连词 · 连接词 · 核心动词 · 元老院与利剑 · 众多与强大 · 万物之布局 · 统御之术",
 "The Daily Round · Arms &amp; the Man · The Forum · Flesh &amp; Breath · Tally &amp; Measure · Worth &amp; Honor · Time &amp; Tide · The Rally":
   "日常诸务 · 武器与战士 · 公共广场 · 血肉与生命 · 计数与衡量 · 价值与荣耀 · 时间与潮流 · 集结",
 "To &amp; Fro · The Long Road · Flesh &amp; Frame · The Fathers · House &amp; Hearth · Hopes &amp; Fears · The Turning Year · The Waystation":
   "往来 · 漫漫长路 · 血肉与躯干 · 父辈们 · 家宅与炉灶 · 希望与恐惧 · 流转之年 · 驿站",
 "Moods &amp; Moments · The Turning Hand · The Living Frame · The Curia · By Land &amp; Sea · More &amp; Most · The Winter Camp · The Muster Roll":
   "情绪与瞬间 · 翻转之手 · 生命之躯 · 库里亚 · 陆与海 · 更多与最多 · 冬营 · 兵员册",
 "What Was Done · The Perfect Stems · The Pitched Battle · The Work in Hand · Life &amp; Limb · Praise &amp; Blame · The Appointed Hour · The Full Account":
   "已成之事 · 完成时词干 · 会战 · 手头之务 · 性命与肢体 · 赞扬与责备 · 约定之时 · 详账",
 "The Life of the Mind · Hours &amp; Days · A Soldier&#x27;s Life · The Full Tally · The Family Estate · The Mortal Frame · Treaties &amp; Powers · The Loose Ends":
   "心灵生活 · 时辰与日子 · 军旅生涯 · 全部计数 · 家族庄园 · 凡胎肉身 · 条约与权势 · 未尽事宜",
 "Comings &amp; Partings · The Ready Hand · The Head Count · Wounds &amp; Toil · Kin &amp; Neighbor · Rank &amp; Office · The Sea Road · The Middle Way":
   "聚散离合 · 得力助手 · 人数清点 · 伤痛与辛劳 · 亲族与邻里 · 爵位与官职 · 海路 · 中道",
 "True &amp; False · The Bidding · Sound &amp; Sick · Weight &amp; Worth · The Present Hour · The Tide of Battle · The Household Store · The Last Ditch":
   "真与假 · 竞逐 · 健与病 · 重量与价值 · 此刻 · 战势 · 家庭储备 · 绝境",
 "Hopes &amp; Vows · By the Numbers · Right &amp; Wrong · The Broken Line · Dust &amp; Ashes · The Sacred Rites · Fraud &amp; Force · What Remains":
   "愿与誓 · 计数 · 是与非 · 断线 · 尘与烬 · 神圣仪式 · 欺诈与武力 · 余下之物",
 "The Open Book · The Final Battle · Blood &amp; Bone · Honor &amp; Shame · Envoys &amp; Treaties · Hearth &amp; Heir · The Last Measure · The Closing Page":
   "开卷之书 · 最终之战 · 血与骨 · 荣辱 · 使节与盟约 · 炉灶与继承人 · 最终手段 · 终章",
 ">8 clusters · 200 cards<": ">8 个词族 · 200 张卡片<",
 "<span>Core: 5 tiers · 40 clusters · <b>1,000 cards</b></span><span>26 reference lessons</span><span>the reading foundation</span>":
   "<span>Core：5 个层级 · 40 个词族 · <b>1,000 张卡片</b></span><span>26 节参考课程</span><span>阅读的地基</span>",
 "<span>Pareto: 5 tiers · 40 clusters · <b>1,000 cards</b></span><span>18 reference lessons</span><span>the trunk complete</span>":
   "<span>Pareto：5 个层级 · 40 个词族 · <b>1,000 张卡片</b></span><span>18 节参考课程</span><span>主干至此完成</span>",

 # ---- the card: the macron ----
 "Read it by sight": "一眼认出",
 "The macron is data, not decoration": "长音符是信息，不是装饰",
 "Every headword is printed as a dictionary prints it — long vowels marked, gender and genitive stem for a noun, conjugation for a verb. 1,320 of the 2,000 headwords carry a macron. Tap a card to flip it.":
   "每个词目都按词典的印法印出——长元音标出来，名词给出性与属格词干，动词给出变位。2,000 个词目中有 1,320 个带着长音符。点击卡片即可翻面。",
 # the dictionary shorthand is the same in any language and stays as written
 ">f., -is<": ">f., -is<",
 '''courage, manliness; virtue — &ldquo;Roman courage is great.&rdquo;<span class="nb">noun | gen sg virtūtis — the stem is virtūt-
long ū: vir-tūs
From vir &lsquo;man&rsquo;: the quality of a man.</span>''':
   '''勇气、男子气概；德性——&ldquo;罗马人的勇气是伟大的。&rdquo;<span class="nb">名词 | 属格单数 virtūtis——词干是 virtūt-
长音 ū：vir-tūs
源自 vir&lsquo;男人&rsquo;：属于男人的那种品质。</span>''',
 '''make, do — &ldquo;We are doing the same thing.&rdquo;<span class="nb">verb | 1st pl facimus = &lsquo;we make, we do&rsquo;
long ō: fa-ci-ō; a and i stay short
idem = &lsquo;the same thing&rsquo; (object role)</span>''':
   '''做、干——&ldquo;我们在做同一件事。&rdquo;<span class="nb">动词 | 第 1 人称复数 facimus =&lsquo;我们做、我们干&rsquo;
长音 ō：fa-ci-ō；a 与 i 仍是短音
idem =&lsquo;同一件事&rsquo;（充当宾语）</span>''',
 '''evil, misfortune — &ldquo;The state sees the shared misfortune.&rdquo;<span class="nb">noun | acc sg malum = nom sg in form
no macron: ma-lum, both vowels short
mālum, with a long ā, is an apple.</span>''':
   '''恶、不幸——&ldquo;城邦看见了共同的不幸。&rdquo;<span class="nb">名词 | 宾格单数 malum = 形式上等同主格单数
没有长音符：ma-lum，两个元音都是短音
mālum 的 ā 是长音，指的是苹果。</span>''',
 ">tap to flip<": ">点击翻面<",

 # ---- the two minimal pairs ----
 ">Tier 1 · Tier 3<": ">层级 1 · 层级 3<",
 ">Tier 10 · Tier 4<": ">层级 10 · 层级 4<",
 "<b>this one</b> against <b>here</b>. One letter apart in print, and the line over the vowel is the only thing that separates them.":
   "<b>这一个</b>对上<b>在这里</b>。印出来只差一道笔画，元音上的那一横是把两者分开的唯一东西。",
 "<b>bone</b> against <b>mouth</b>. Same three letters, same neuter third declension, six tiers apart — and the card that teaches the second one says so.":
   "<b>骨头</b>对上<b>嘴</b>。同样的三个字母，同样是中性第三变格法，相隔六个层级——而教第二个词的那张卡片会把这一点说出来。",
 "The macrons stop at the headword. Example sentences are printed unmarked, the way every real Latin text you will ever open is printed — so what you practise reading is the thing itself, not a teaching aid. The card tells you the vowel length; the sentence makes you carry it.":
   "长音符只标到词目为止。例句一律不标，正如你今后翻开的每一部真实拉丁语文本那样——所以你练的是这门语言本身，而不是一件教学辅具。卡片告诉你元音的长短；句子让你自己把它带着走。",

 # ---- reference lessons ----
 "Not just a word list": "不只是一份单词列表",
 "Forty-four lessons, fired in sequence": "四十四节课程，依序触发",
 "A reference lesson unlocks at the exact card where you first need it, and stays available afterwards. Core's twenty-six and Pareto's eighteen are all free to read on the <a href=\"lessons.html?lang=Latin\">lessons page</a>.":
   "参考课程恰在你第一次需要它的那张卡片处解锁，此后随时可以回看。Core 的二十六节与 Pareto 的十八节，都可在<a href=\"lessons.html?lang=Latin\">课程页面</a>免费阅读。",

 # whole <li> each, so no English article is stranded in front of a Chinese noun
 "<li><span class=\"no\">01</span>Welcome to Latin<span class=\"d\">The four letters an English reader gets wrong — c, g, v, qu — in the restored sounds, and what a macron is for.</span></li>":
   "<li><span class=\"no\">01</span>拉丁语入门<span class=\"d\">英语读者最容易读错的四个字母——c、g、v、qu——在复原读音里的读法，以及长音符是做什么用的。</span></li>",
 "<li><span class=\"no\">10</span>The accusative<span class=\"d\">The first case that changes what a sentence means, met on the card that first needs it.</span></li>":
   "<li><span class=\"no\">10</span>宾格<span class=\"d\">第一个会改变句子意思的格，在第一次需要它的那张卡片上与你相遇。</span></li>",
 "<li><span class=\"no\">14</span>Genitive and dative<span class=\"d\">Of and to, and why the genitive singular is printed on every noun card.</span></li>":
   "<li><span class=\"no\">14</span>属格与与格<span class=\"d\">「的」与「给」，以及为什么每张名词卡片上都印着属格单数。</span></li>",
 "<li><span class=\"no\">18</span>The ablative<span class=\"d\">The case English has no name for, and the six jobs it does.</span></li>":
   "<li><span class=\"no\">18</span>夺格<span class=\"d\">英语没有名字可叫的那个格，以及它担着的六项职能。</span></li>",
 "<li><span class=\"no\">23</span>Principal parts<span class=\"d\">Why a Latin verb is quoted four ways, and how to get from any of them to the rest.</span></li>":
   "<li><span class=\"no\">23</span>动词的基本形式<span class=\"d\">拉丁语动词为什么要列出四种形式，以及怎样从其中任意一种推出其余几种。</span></li>",
 "<li><span class=\"no\">30</span>The ablative absolute<span class=\"d\">The construction that makes Caesar readable at speed.</span></li>":
   "<li><span class=\"no\">30</span>独立夺格<span class=\"d\">让凯撒能被快速读下来的那个结构。</span></li>",
 "<li><span class=\"no\">34</span>Reported speech<span class=\"d\">Accusative and infinitive: how a Roman writes &lsquo;he said that&hellip;&rsquo;.</span></li>":
   "<li><span class=\"no\">34</span>间接引语<span class=\"d\">宾格加不定式：罗马人怎样写&lsquo;他说……&rsquo;。</span></li>",
 "<li><span class=\"no\">41</span>Reading the citation<span class=\"d\">What <i>Caes. BG 5.44.5</i> means, and how to go and find the rest of the page.</span></li>":
   "<li><span class=\"no\">41</span>读懂出处<span class=\"d\"><i>Caes. BG 5.44.5</i> 是什么意思，以及怎样去把那一页的其余部分找出来。</span></li>",

 "Also inside: i acting as y, ch and ae/oe, the connectives, the prime movers, the present tense, the imperative, the sound system, the full plural, two more conjugations, the imperfect, the third declension, prepositions and case, the perfect and its family, relative clauses, connectives at speed, all three participles and their two jobs, the passive twice over, deponents, the infinitive family, the subjunctive mood, cum-clauses, purpose and result, indirect questions, the gerund, the gerundive — and a closing lesson on where to go next.":
   "另外还有：i 当作 y 来读、ch 与 ae/oe、连接词、核心动词、现在时、命令式、语音系统、完整的复数、另外两种变位、未完成时、第三变格法、介词与格、完成时及其家族、关系从句、快速读连接词、三种分词及其两项用途、被动式讲两遍、异态动词、不定式家族、虚拟语气、cum 从句、目的与结果、间接疑问句、动名词、动形词——以及一节讲下一步往哪里走的收尾课程。",

 # ---- the two packs, and the fork past them ----
 "Two packs to literacy": "两个卡包，通向阅读能力",
 "Latin is a trunk, not a staircase of three. Core and Pareto together are the whole 2,000-word reading course, grammar-complete at the end of it.":
   "拉丁语是一根主干，不是三级台阶。Core 与 Pareto 合起来就是完整的 2,000 词阅读课程，走到终点时语法也讲完了。",
 ">Tiers 1–5 · 1,000 words · 26 lessons<": ">层级 1–5 · 1,000 个单词 · 26 节课程<",
 "The reading foundation. Sentences built to the tier at first, real Caesar by the end. Requires the base game.":
   "阅读的地基。起初是为该层级而造的句子，到末尾是真正的凯撒。需要基础游戏。",
 ">Tiers 6–10 · 1,000 words · 18 lessons<": ">层级 6–10 · 1,000 个单词 · 18 节课程<",
 "The second thousand, and the end of the scaffolding: Nepos, Cicero's letters, Sallust, Livy, Cicero's speeches. Requires Core.":
   "第二个一千词，也是脚手架的终点：奈波斯、西塞罗的书信、萨卢斯特、李维、西塞罗的演说。需要 Core。",
 ">On Steam<": ">在 Steam 发售<",

 "Then choose your third thousand": "然后选定你的第三个一千词",
 "Basic literacy is the fork, not the finish. The trunk stops at 2,000 words on purpose: past that, Latin genuinely divides, and which 1,000 words come next depends on what you want to read. Neither branch is built yet.":
   "基本的阅读能力是分岔口，不是终点。主干特意停在 2,000 词：再往前，拉丁语是真的分开了，接下来该学哪 1,000 个词，取决于你想读什么。两条分支都还没有做出来。",
 ">Classical Poetry<": ">古典诗歌<",
 ">Vergil · Ovid · Catullus · Horace<": ">维吉尔 · 奥维德 · 卡图卢斯 · 贺拉斯<",
 "Verse word order, metre, and the vocabulary that only ever shows up in poets. The trunk's prose ladder is the prerequisite, not a substitute.":
   "诗的语序、格律，以及只在诗人笔下出现的词汇。主干的散文阶梯是前提，不是替代。",
 ">planned · not yet built<": ">已列入计划 · 尚未做出<",
 ">Ecclesiastical Latin<": ">教会拉丁语<",
 ">the Vulgate · the hymns · the liturgy<": ">武加大译本 · 圣歌 · 礼仪<",
 "Church Latin is its own register — different syntax, different vocabulary, and its own pronunciation, which is why it is a branch and not a chapter of the trunk.":
   "教会拉丁语自成一种语域——句法不同、词汇不同，读音也是自己的一套，所以它是一条分支，而不是主干里的一章。",
 "Both branches take Core and Pareto as their entry requirement. Neither has a date; both are inventoried and reserved rather than promised.":
   "两条分支都以 Core 与 Pareto 为入门条件。两者都没有日期；它们是被登记并预留下来的，不是被承诺的。",

 # ---- method ----
 "How it sticks": "为何记得住",
 "Flashcards as an integrated system": "闪卡组成的完整系统",
 "<dt>Fibonacci SRS</dt>": "<dt>斐波那契间隔重复</dt>",
 "Rate each card 0–5. The better you know a word, the longer before it returns — spaced repetition on Fibonacci intervals.":
   "每张卡片按 0–5 评分。一个单词记得越牢，它再次出现的间隔就越长——基于斐波那契数列的间隔重复。",
 "<dt>Boss fights</dt>": "<dt>Boss 战</dt>",
 "Each of the 80 clusters is gated by a duel you can't win without confronting and overcoming your most difficult words.":
   "80 个词族，每一个都由一场决斗把守。不直面并战胜你最棘手的单词，就无法取胜。",
 "<dt>Graduation</dt>": "<dt>毕业</dt>",
 "Beat a cluster and its cards leave your daily deck for good. The deck gets smaller as you learn.":
   "击败一个词族，它的卡片就永远退出你的每日卡组。学得越多，卡组就越小。",
 "<dt>Audio</dt>": "<dt>语音</dt>",
 "A Latin neural voice on every headword and every example sentence — <i>la_LA-flashboss_m</i>, fine-tuned for FlashBoss and released CC0, reading Classical (restored) pronunciation and honouring the macrons as real vowel length. It is synthesis, not a recording of a speaker.":
   "每个词目、每个例句都配有拉丁语的神经网络语音——<i>la_LA-flashboss_m</i>，为 FlashBoss 微调并以 CC0 发布，读的是古典（复原）读音，并把长音符当作真实的元音长度来处理。它是合成语音，不是真人录音。",
 "<dt>Your language</dt>": "<dt>你的语言</dt>",
 "All 2,000 cards carry their translation, their example translation <i>and</i> their notes in <b>German, Spanish, Japanese, Russian and Simplified Chinese</b> as well as English — 30,000 fields, with no gaps. All 44 reference lessons carry the same five, and so does the game's interface. Latin is fully playable without a word of English.":
   "2,000 张卡片全部带有译文、例句译文<i>与</i>注释，除英语外还有<b>德语、西班牙语、日语、俄语和简体中文</b>——共 30,000 个字段，没有缺口。全部 44 节参考课程同样有这五种语言，游戏界面也是如此。拉丁语课程不需要一个英语单词也能游玩。",
 "<dt>Macrons</dt>": "<dt>长音符</dt>",
 "Long vowels marked on 1,320 of the 2,000 headwords, left off the sentences — dictionary convention where it teaches, print convention where you read.":
   "2,000 个词目中有 1,320 个标出了长元音，句子里则不标——在教的地方用词典的惯例，在读的地方用印刷的惯例。",
 "<dt>Real sources</dt>": "<dt>真实出处</dt>",
 "1,052 example sentences cite the book, chapter and section they came from; 813 are unaltered. Everything is drawn from public-domain editions.":
   "1,052 个例句标明了自己出自哪一卷、哪一章、哪一节；其中 813 个未经改动。全部取自公有领域的版本。",
 "Forty-four reference lessons across the two packs fire at the point in the sequence where they unlock what you are about to read.":
   "两个卡包合计四十四节参考课程，在序列中的恰当节点触发——恰好为你即将读到的内容解锁铺垫。",

 # ---- FAQ ----
 ">Questions<": ">常见问题<",
 "The things people ask before they buy.": "人们在购买之前会问的那些问题。",

 ">Where do I buy it?<": ">在哪里购买？<",
 """Both packs are on Steam now: <a href="https://store.steampowered.com/app/5063240/?utm_source=website-latin-faq" target="_blank" rel="noopener">Latin Core</a> and <a href="https://store.steampowered.com/app/5063250/?utm_source=website-latin-faq" target="_blank" rel="noopener">Latin Pareto</a>. Both word lists and all forty-four lessons are readable here, free, if you want to judge the course before you buy either one.""":
   """两个卡包现已在 Steam 发售：<a href="https://store.steampowered.com/app/5063240/?utm_source=website-latin-faq" target="_blank" rel="noopener">Latin Core</a> 与 <a href="https://store.steampowered.com/app/5063250/?utm_source=website-latin-faq" target="_blank" rel="noopener">Latin Pareto</a>。如果你想在掏钱之前先判断这门课程，两份单词列表和全部四十四节课程都可以在本站免费阅读。""",

 ">Which pronunciation is this?<": ">这是哪一种读音？<",
 "Classical — the restored pronunciation of Caesar's Rome, in the lessons and in the voice alike: c and g always hard, v as English w, <i>Caesar</i> said as the German <i>Kaiser</i>. An ecclesiastical voice is planned separately, and Church Latin proper is a branch of its own rather than an option inside this course.":
   "古典读音——凯撒时代罗马的复原读音，课程与语音都是如此：c 与 g 始终读硬音，v 读作英语的 w，<i>Caesar</i> 读得像德语的 <i>Kaiser</i>。教会读音的语音另有计划，而真正的教会拉丁语自成一条分支，不是这门课程里的一个选项。",

 ">Do I need anything else to play it?<": ">游玩还需要别的什么吗？<",
 """Yes. Latin Core is a DLC for the FlashBoss base game, so you need the base game as well. Latin Pareto requires Core — the packs build on each other in order. Everything else — the lessons, the audio, the boss fights — is inside the pack. On Windows 10 you also need <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a> — a free, secure download from the Microsoft Store.""":
   """需要。Latin Core 是 FlashBoss 基础游戏的 DLC，所以你还需要基础游戏。Latin Pareto 需要 Core——这些卡包按顺序层层相叠。其余的一切——课程、语音、Boss 战——都在卡包里面。在 Windows 10 上，你还需要 <a href="https://apps.microsoft.com/detail/9n0dx20hk701" target="_blank" rel="noopener">Windows Terminal</a>——可以从 Microsoft Store 免费、安全地下载。""",

 ">Is the Latin real, or written for the course?<": ">这些拉丁语是真的，还是为课程写的？<",
 "Both, in a stated order. Tiers 1 to 3 are constructed to the grammar you have been taught — no real author writes at that ceiling, and the cards claim none. Caesar enters at Tier 4, lightly trimmed. From Tier 8 on, almost every sentence is an author's own unaltered words. Across the two packs 1,052 of 2,000 sentences carry a citation and 813 of those are unadapted.":
   "两者都有，而且顺序是写明的。层级 1 至 3 是按你已经学过的语法造出来的——没有哪个真实作者会写在那个上限上，卡片也不声称有作者。凯撒在层级 4 登场，略作删减。从层级 8 起，几乎每个句子都是作者本人未经改动的原话。两个卡包合起来，2,000 个句子中有 1,052 个带着出处，其中 813 个未经改编。",

 ">Can I play it in my own language?<": ">可以用我自己的语言游玩吗？<",
 "Fully. Every one of the 2,000 cards carries its translation, its example translation and its study notes in <b>German, Spanish, Japanese, Russian and Simplified Chinese</b> as well as English, with no gaps anywhere. All forty-four reference lessons carry the same five, and the game's own interface speaks all six.":
   "完全可以。2,000 张卡片中的每一张，除英语外都带有<b>德语、西班牙语、日语、俄语和简体中文</b>的译文、例句译文与学习注释，任何地方都没有缺口。全部四十四节参考课程同样有这五种语言，游戏自己的界面则说全部六种。",

 ">What does the course get me to?<": ">这门课程能把我带到什么程度？<",
 "Reading unadapted classical prose with a dictionary beside you. Two thousand of the highest-frequency lemmas, the whole grammar of the indicative and subjunctive, participles, the infinitive constructions, the gerund and gerundive — and 17,007 words of Latin read in context on the way there. Not speaking Latin, and not writing it: the course is honest that it teaches one skill.":
   "带到手边放一本词典就能读未经改编的古典散文。两千个最高频的词条、陈述式与虚拟式的全部语法、分词、不定式结构、动名词与动形词——一路上还在上下文中读过 17,007 个拉丁语词。不是说拉丁语，也不是写拉丁语：这门课程坦白地说，它只教一项技能。",

 ">Why is there no Pareto 2?<": ">为什么没有 Pareto 2？<",
 "Because Latin forks instead. Core plus Pareto is a complete 2,000-word trunk, grammar-complete at Tier 10. The third thousand depends on where you are going — classical poetry or ecclesiastical Latin — so it is planned as two branches rather than one more staircase. Neither is built yet.":
   "因为拉丁语在这里分岔了。Core 加 Pareto 就是一根完整的 2,000 词主干，到层级 10 语法已经讲完。第三个一千词取决于你要去哪里——古典诗歌，还是教会拉丁语——所以它被规划成两条分支，而不是再加一级台阶。两者都还没有做出来。",

 ">Can I see the words before I buy?<": ">买之前能看到单词吗？<",
 """All of them. The complete word lists for Core and Pareto are on the <a href="wordlists.html?lang=Latin&amp;set=Core">word lists page</a>, and all forty-four reference lessons are on the <a href="lessons.html?lang=Latin">lessons page</a> — free, printable, no account.""":
   """全都能看。Core 与 Pareto 的完整单词列表就在<a href="wordlists.html?lang=Latin&amp;set=Core">单词列表页面</a>，全部四十四节参考课程就在<a href="lessons.html?lang=Latin">课程页面</a>——免费、可打印、不用注册账号。""",

 ">Is there a demo?<": ">有试玩吗？<",
 """There's a playable boss fight in the browser, if you want to know what the fight feels like before you commit: <a href="https://flashboss-demo.pages.dev/">try the demo</a>.""":
   """浏览器里有一场可以直接玩的 Boss 战，如果你想在决定之前先知道战斗是什么感觉：<a href="https://flashboss-demo.pages.dev/">试玩演示</a>。""",

 # ---- closing call to action ----
 "Start with <i>Roma est.</i>": "从 <i>Roma est.</i> 开始",
 "Two words on the first card of the first cluster. Two thousand words later, Cicero.":
   "第一个词族第一张卡片上的两个词。两千个单词之后，是西塞罗。",
 "— both on Steam": "——两者都已在 Steam 发售",
 """Or read the <a href="wordlists.html?lang=Latin&amp;set=Core">word list</a> and the <a href="lessons.html?lang=Latin">lessons</a> first — they're free, and they're the whole course.""":
   """也可以先读<a href="wordlists.html?lang=Latin&amp;set=Core">单词列表</a>和<a href="lessons.html?lang=Latin">课程</a>——它们是免费的，而且它们就是整门课程。""",
 # the bundle name is the ratified Chinese one from the Latin paste sheet
 """Everything here in one purchase: <a href="https://store.steampowered.com/bundle/87746/?utm_source=website-bundle" target="_blank" rel="noopener"><b>FlashBoss Latin — The Complete Course</b></a>. Already own part of it? Steam charges you only for the rest.""":
   """这里的一切，一次购买：<a href="https://store.steampowered.com/bundle/87746/?utm_source=website-bundle" target="_blank" rel="noopener"><b>FlashBoss 拉丁语 — 完整课程</b></a>。已经拥有其中一部分？Steam 只收取其余部分的费用。""",

 # ---- footer epigraph: the Latin stands, the gloss and the cite become Chinese ----
 "<span class=\"tr\">Chance counts for much in everything, and most of all in warfare.</span>":
   "<span class=\"tr\">机运在万事之中都举足轻重，在战事之中尤其如此。</span>",
 "Latin Core · Tier 4 · Caes. BG 6.30.2": "Latin Core · 层级 4 · Caes. BG 6.30.2",
}

# Simplified Chinese strings for in-development.html.
# This page lists what is NOT out yet, so the rule above all others here is that
# it carries NO DATE of any kind — no month, no quarter, no year, no 即将推出,
# no ETA. Where the English hedges without a date, the Chinese hedges without a
# date. The only date on the page is the counting date in the closing note, and
# that is when the packs were counted, not when anything ships. The old
# placeholder zh page said 即将上线™; nothing of it is reused.
# Vocabulary is read off the live Chinese pages: 卡包 (packs.zh.html),
# 单词列表, 课程, 语音, 资源, 主页 (the glossary settled on immersion.zh),
# 现已推出 / 现已发售 and 尚未发售 (packs.zh.html, voices.zh.html), 词族 for
# cluster and Boss 战 for boss fight (the ratified Steam copy — see the note
# below), 层级 for tier (immersion.zh). 开发中 is what packs.zh.html already
# calls this page: 正在制作、即将上线的内容，请见 <a>开发中</a> 页面.
# Pack and product names stay English and sit bare in the Chinese sentence, one
# space each side, no 《》 and no gloss — Swahili Pareto 1/2, Swahili Core,
# Core, Pareto, The Guide, The Guide Part II, Latin Core, Latin Pareto,
# Greek Roots, Castellano. Bare language names take their Chinese form the way
# the live zh pages write 俄语, 希腊语, 拉丁语, 斯瓦希里语.
# Numbers are the English page's numbers; zh keeps the comma separator, so
# 1,000 is written 1,000 here exactly as on the English page. Nothing recounted.
#
# THREE THINGS THE OWNER SHOULD LOOK AT ONCE:
#   * cluster = 词族 and boss fight = Boss 战 come from the ratified Chinese
#     bundle copy, which is what immersion.zh already uses. The live zh pages
#     say 集群 and 头目战 (voices.zh.html line 284). The new pages are
#     self-consistent; if the site is harmonised the other way these two words
#     are the whole diff, on this page as on immersion.
#   * english path = 英语之路 in the nav and the footer. The immersion page
#     itself is titled 英语沉浸系统 and labels itself 沉浸 in its own nav, so
#     this is a link label, not a second name for the page.
#   * the four poets are given in their standard Chinese forms (维吉尔、奥维德、
#     卡图卢斯、贺拉斯) and the Vulgate as 武加大译本, the way italian.zh.html
#     already writes 但丁《天堂篇》 — minus the 《》, which the brief bans here.
#
# Punctuation: full-width inside Chinese sentences, 、 between example pairs.
# The literal em dash is rendered —— in running prose, which is what the live
# zh pages do; the · in the facts lines is the English page's own character and
# is left alone.
TITLE = "开发中 — FlashBoss"
DESCRIPTION = ("FlashBoss 接下来在做的东西：Swahili Pareto 1 与 2、俄语、印尼语、"
               "古希腊语与现代希腊语、The Guide Part II，以及拉丁语的两个分支。"
               "数字从卡包本身数出，没有发售日期。")

STRINGS = {
 # ---- nav / chrome ----
 ">packs<": ">卡包<",
 ">in development<": ">开发中<",
 ">out now<": ">现已推出<",
 ">english path<": ">英语之路<",
 ">voices<": ">语音<",
 ">home<": ">主页<",
 ">resources<": ">资源<",
 ">the english path<": ">英语之路<",

 # ---- hero: the h1 is keyed with its tag so the head comment is left alone ----
 # 尚未发售 is what voices.zh.html already puts on a thing that has no date.
 ">Not out yet<": ">尚未发售<",
 '<h1 class="reveal">In Development<': '<h1 class="reveal">开发中<',
 "What is being built, and how far along it is. <b>Nothing on this page has a release date</b>, because none of it has one — a date goes up when a pack is ready, not before. Everything listed here exists as real cards today; the counts were taken from the packs themselves, not from a plan.":
   "正在做的东西，以及各自到了哪一步。<b>本页上的一切都没有发售日期</b>，因为它们本来就没有——日期要等一个卡包做好了才挂出来，不会提前。这里列出的每一样今天都已经是真实的卡片；数字是从卡包本身数出来的，不是从计划里来的。",

 # ---- the legend: whole line each, so the <b> keeps its Chinese sentence ----
 "<b>Cards written</b> — the pack is authored and counted. What remains is checking, audio and a store page.":
   "<b>卡片已写成</b>——这个卡包已经写完并清点过。剩下的是校对、音频和一个商店页面。",
 "<b>Planned</b> — decided and inventoried, not started. No cards exist yet.":
   "<b>已规划</b>——已经定下来并列入清单，但还没有动工。目前一张卡片也没有。",
 # the two state badges, after the legend lines above have already gone Chinese
 ">Cards written<": ">卡片已写成<",
 ">Planned<": ">已规划<",

 # ---- finishing a course already on sale ----
 "<h2>Finishing a course already on sale</h2>":
   "<h2>把已经在售的课程补完</h2>",
 "These continue packs you can buy today, and take the pack before them as read.":
   "它们续接你今天就能买到的卡包，并默认前一个卡包你已经学过。",

 "1,000 words · 40 clusters · tiers 6–10":
   "1,000 个单词 · 40 个词族 · 第 6–10 层级",
 "The working vocabulary: money and the bank, the company and the contract, the ministry, elections, the court, the police, the press, the hospital. Continues <a href=\"swahili.html\">Swahili Core</a>, which is out now.":
   "办事用的词汇：钱与银行、公司与合同、部委、选举、法院、警察、新闻界、医院。它续接 <a href=\"swahili.html\">Swahili Core</a>，后者现已发售。",

 "1,000 words · 40 clusters · tiers 11–15":
   "1,000 个单词 · 40 个词族 · 第 11–15 层级",
 "The last thousand of the 3,000-word course, and where Swahili's derivation opens up — one root becoming six verbs through the passive, the stative, the reciprocal, the reflexive, the causative and the applicative.":
   "这门 3,000 词课程的最后一千词，也是斯瓦希里语的派生开始展开的地方——一个词根经由被动、状态、相互、反身、使役与施用，变成六个动词。",

 "925 cards · 50 clusters · three tiers · English and German":
   "925 张卡片 · 50 个词族 · 三个层级 · 英语与德语",
 "The other half of a game master's memory. Where <a href=\"the-guide.html\">The Guide</a> holds the rules you adjudicate with, Part II holds what you populate a world with: the spell list, the creature roster and the treasure table. Requires The Guide.":
   "游戏主持人记忆的另一半。<a href=\"the-guide.html\">The Guide</a> 装的是你用来裁定的规则，Part II 装的则是你用来填满一个世界的东西：法术表、怪物名录与宝物表。需要 The Guide。",

 # ---- new languages: bare language names go Chinese, Core/Pareto stay ----
 "<h2>New languages</h2>": "<h2>新语言</h2>",
 "Each is a full course in the usual shape — Core first, then Pareto 1, five tiers apiece.":
   "每一门都是通常形态的完整课程——先 Core，再 Pareto 1，各五个层级。",

 "Core and Pareto 1 · 1,000 words each · 40 clusters each":
   "Core 与 Pareto 1 · 各 1,000 个单词 · 各 40 个词族",

 ">Russian<": ">俄语<",
 "Русский. Two thousand words authored and counted.":
   "Русский。两千个单词已经写成并清点。",

 ">Indonesian<": ">印尼语<",
 "Bahasa Indonesia — a language with no tenses, no genders and no plurals to memorise, and a word order you already have.":
   "Bahasa Indonesia——一门没有时态、没有性、也没有复数形式要背的语言，语序则是你早就有的那种。",

 ">Modern Greek<": ">现代希腊语<",
 "Ελληνικά, the living language, with an alphabet ladder in the opening lessons. Not to be confused with Ancient Greek below, or with <a href=\"greek-roots.html\">Greek Roots</a>, which teaches the Greek already inside English.":
   "Ελληνικά，活着的那一门，开头几节课里有一道字母阶梯。不要和下面的古希腊语混淆，也不要和 <a href=\"greek-roots.html\">Greek Roots</a> 混淆，后者教的是已经在英语里面的希腊语。",

 ">Ancient Greek<": ">古希腊语<",
 "A reading course, in the shape <a href=\"latin.html\">Latin</a> took: the sentences start built for the tier and end as the authors wrote them.":
   "一门阅读课程，形态和 <a href=\"latin.html\">拉丁语</a> 那门一样：句子起初是为所在层级搭起来的，到最后就是作者原样写下的句子。",

 ">Polish and Portuguese<": ">波兰语与葡萄牙语<",
 "Word lists locked · no cards authored yet":
   "单词列表已定 · 尚未撰写卡片",
 "The frequency backbones are chosen and fixed, which is the half of the work that decides what a course teaches. The cards themselves are not written.":
   "两门语言的词频主干都已选定并固定下来，而这正是决定一门课程教什么的那一半工作。卡片本身还没有写。",

 # ---- beyond the Latin trunk ----
 "<h2>Beyond the Latin trunk</h2>": "<h2>拉丁语主干之外</h2>",
 "Latin Core and Latin Pareto are the whole 2,000-word reading course, grammar-complete at tier 10. There is deliberately no third staircase.":
   "Latin Core 与 Latin Pareto 合起来就是整门 2,000 词的阅读课程，到第 10 层级语法已经完整。这里有意不设第三段楼梯。",

 ">Latin — the two branches<": ">拉丁语——两个分支<",
 "Classical poetry · or ecclesiastical Latin": "古典诗歌 · 或教会拉丁语",
 "Past 2,000 words Latin genuinely divides, and which thousand comes next depends on what you want to read: <b>classical poetry</b> — Vergil, Ovid, Catullus, Horace — or <b>ecclesiastical Latin</b>, the Vulgate, the hymns and the liturgy. Both are inventoried and reserved. Neither is built, and neither takes the other as a prerequisite.":
   "过了 2,000 词，拉丁语是真的会分岔，下一个一千词是哪一千，取决于你想读什么：<b>古典诗歌</b>——维吉尔、奥维德、卡图卢斯、贺拉斯——或者<b>教会拉丁语</b>，武加大译本、圣歌与礼仪。两边都已列入清单并预留下来。两边都还没有做，也都不以另一边为前提。",

 # ---- voices ----
 "<h2>Voices</h2>": "<h2>语音</h2>",
 ">Castellano — Spain, male<": ">Castellano——西班牙，男声<",
 "Replaces the included Latin American voice across every Spanish pack":
   "在所有西班牙语卡包中替换随附的拉美语音",
 "A voice pack rather than a course: it swaps the voice in cards, lessons and boss fights, and switches back whenever you like. Hear it against the voice it replaces on the <a href=\"voices.html\">voices page</a>.":
   "这是语音包，不是课程：它会替换卡片、课程和 Boss 战里的语音，你随时可以切回去。在<a href=\"voices.html\">语音页面</a>，可以把它和被它替换掉的那把声音对比着听。",

 # ---- the closing note: the date here is the COUNTING date, not a release ----
 "Everything above was counted from the packs on <b>19 September 2026</b>. A pack leaves this page the day it goes on sale and appears on <a href=\"packs.html\">the pack list</a> instead — so if something has vanished from here, look for it there.":
   "以上内容都是 <b>2026 年 9 月 19 日</b> 从卡包中数出来的。一个卡包在开售当天就会离开本页，转而出现在<a href=\"packs.html\">卡包列表</a>上——所以如果这里少了什么，就去那边找。",
 "And yes — the page that lists what's in development used to be, itself, in development.":
   "是的——这个列出开发中内容的页面，自己也曾经在开发中。",
}

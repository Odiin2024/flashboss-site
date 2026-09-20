# Japanese strings for in-development.html.
# This page lists what is NOT out yet, so the rule above all others here is that
# it carries NO DATE of any kind — no month, no quarter, no year, no 近日公開,
# no ETA. Where the English hedges without a date, the Japanese hedges without a
# date. The one date on the page is the counting date in the closing note, and
# that is when the packs were counted, not when anything ships. packs.ja.html
# writes "開発中・近日登場" in its own lede; 近日 is not repeated here.
#
# Register: です／ます, no keigo inflation, no exclamation marks, and NO SPACES
# around Latin-script words inside a Japanese sentence — the house style settled
# on immersion.ja.html and already live on packs.ja.html ("stubbornとobstinate").
# Terms are the ones the live ja pages use: パック, クラスター, ティア,
# レッスン, カード, ボス戦, 単語リスト, 音声, ストアページ, はしご, 発売中.
# 開発中 is what packs.ja.html already calls this page; 未発売 is what
# voices.ja.html already puts on a thing that has not shipped, so the kicker
# uses it rather than inventing a phrase.
#
# Pack and product names stay English — Swahili Pareto 1/2, Core, Pareto,
# The Guide Part II, Latin Core, Latin Pareto, Greek Roots, Castellano. Bare
# language names take their Japanese form, the way packs.ja.html already writes
# スワヒリ語 and ロシア語. Русский and Ελληνικά stay in their own scripts, as in
# the English.
# Numbers are the English page's numbers; ja writes the same comma the English
# already writes, so nothing moves and nothing is recounted.
TITLE = "開発中 — FlashBoss"
DESCRIPTION = ("FlashBossが次に作っているもの：Swahili Pareto 1と2、ロシア語、"
               "インドネシア語、古代ギリシャ語と現代ギリシャ語、The Guide Part II、"
               "そしてラテン語の二つの枝。パックから数えた数字で、発売日はありません。")

STRINGS = {
 # ---- nav / chrome ----
 ">packs<": ">パック<",
 ">in development<": ">開発中<",
 ">out now<": ">発売中<",
 ">english path<": ">英語の道<",
 ">voices<": ">音声<",
 ">home<": ">ホーム<",
 ">resources<": ">リソース<",
 ">the english path<": ">英語の道<",

 # ---- hero: the h1 is keyed with its tag so the head comment is left alone ----
 ">Not out yet<": ">未発売<",
 '<h1 class="reveal">In Development<': '<h1 class="reveal">開発中<',
 "What is being built, and how far along it is. <b>Nothing on this page has a release date</b>, because none of it has one — a date goes up when a pack is ready, not before. Everything listed here exists as real cards today; the counts were taken from the packs themselves, not from a plan.":
   "いま何が作られていて、どこまで進んでいるか。<b>このページのどれにも発売日はありません</b>。どれもまだ日付を持っていないからです — 日付が出るのはパックが仕上がったときで、それより前ではありません。ここに載っているものはすべて、今日すでに本物のカードとして存在します。数字は計画からではなく、パックそのものから取りました。",

 # ---- the legend: whole line each, so the <b> keeps its Japanese sentence ----
 "<b>Cards written</b> — the pack is authored and counted. What remains is checking, audio and a store page.":
   "<b>カード執筆済み</b> — パックは書き上がり、数え終えています。残っているのは点検と音声、そしてストアページです。",
 "<b>Planned</b> — decided and inventoried, not started. No cards exist yet.":
   "<b>計画中</b> — 決定して棚卸しも済み、着手はまだです。カードはまだありません。",
 # the two state badges, after the legend lines above have already gone Japanese
 ">Cards written<": ">カード執筆済み<",
 ">Planned<": ">計画中<",

 # ---- finishing a course already on sale ----
 "<h2>Finishing a course already on sale</h2>": "<h2>発売中のコースを仕上げる</h2>",
 "These continue packs you can buy today, and take the pack before them as read.":
   "いずれも、今日買えるパックの続きです。ひとつ前のパックを済ませてあることを前提にしています。",

 "1,000 words · 40 clusters · tiers 6–10": "1,000語 · 40クラスター · ティア6〜10",
 'The working vocabulary: money and the bank, the company and the contract, the ministry, elections, the court, the police, the press, the hospital. Continues <a href="swahili.html">Swahili Core</a>, which is out now.':
   '仕事で使う語彙：お金と銀行、会社と契約、省庁、選挙、裁判所、警察、報道、病院。発売中の<a href="swahili.html">Swahili Core</a>に続くパックです。',

 "1,000 words · 40 clusters · tiers 11–15": "1,000語 · 40クラスター · ティア11〜15",
 "The last thousand of the 3,000-word course, and where Swahili's derivation opens up — one root becoming six verbs through the passive, the stative, the reciprocal, the reflexive, the causative and the applicative.":
   "3,000語コースの最後の1,000語。そして、スワヒリ語の派生が開けるところです — ひとつの語根が、受動・状態・相互・再帰・使役・適用の派生を通して6つの動詞になります。",

 "925 cards · 50 clusters · three tiers · English and German":
   "カード925枚 · 50クラスター · ティア3つ · 英語とドイツ語",
 "The other half of a game master's memory. Where <a href=\"the-guide.html\">The Guide</a> holds the rules you adjudicate with, Part II holds what you populate a world with: the spell list, the creature roster and the treasure table. Requires The Guide.":
   'ゲームマスターの記憶の、もう半分。<a href="the-guide.html">The Guide</a>が裁定に使う規則を収めているのに対し、Part IIが収めるのは、世界に住人と中身を与えるもの — 呪文のリスト、クリーチャーの一覧、宝物表です。The Guideが必要です。',

 # ---- new languages: bare language names go Japanese, Core/Pareto stay ----
 "<h2>New languages</h2>": "<h2>新しい言語</h2>",
 "Each is a full course in the usual shape — Core first, then Pareto 1, five tiers apiece.":
   "どれも、いつもどおりの形をした完全なコースです — まずCore、そしてPareto 1、それぞれティアが5つ。",

 "Core and Pareto 1 · 1,000 words each · 40 clusters each":
   "CoreとPareto 1 · それぞれ1,000語 · それぞれ40クラスター",

 ">Russian<": ">ロシア語<",
 "Русский. Two thousand words authored and counted.": "Русский。2,000語を書き上げ、数え終えています。",

 ">Indonesian<": ">インドネシア語<",
 "Bahasa Indonesia — a language with no tenses, no genders and no plurals to memorise, and a word order you already have.":
   "Bahasa Indonesia — 時制がなく、性がなく、覚えるべき複数形もない言語。語順は英語と同じものです。",

 ">Modern Greek<": ">現代ギリシャ語<",
 'Ελληνικά, the living language, with an alphabet ladder in the opening lessons. Not to be confused with Ancient Greek below, or with <a href="greek-roots.html">Greek Roots</a>, which teaches the Greek already inside English.':
   'Ελληνικά、生きているほうのギリシャ語です。最初のレッスンにアルファベットのはしごが置いてあります。下にある古代ギリシャ語とも、英語の中にすでにあるギリシャ語を教える<a href="greek-roots.html">Greek Roots</a>とも別のものです。',

 ">Ancient Greek<": ">古代ギリシャ語<",
 'A reading course, in the shape <a href="latin.html">Latin</a> took: the sentences start built for the tier and end as the authors wrote them.':
   '読むためのコースで、<a href="latin.html">ラテン語</a>が取ったのと同じ形をしています：文はそのティアに合わせて組まれたものから始まり、最後は著者が書いたそのままの文になります。',

 ">Polish and Portuguese<": ">ポーランド語とポルトガル語<",
 "Word lists locked · no cards authored yet": "単語リスト確定 · カードはまだ未執筆",
 "The frequency backbones are chosen and fixed, which is the half of the work that decides what a course teaches. The cards themselves are not written.":
   "頻度順の背骨はどちらも選び終え、確定しています。コースが何を教えるかを決めるのは、この半分の作業です。カードそのものは、まだ書かれていません。",

 # ---- beyond the Latin trunk ----
 "<h2>Beyond the Latin trunk</h2>": "<h2>ラテン語の幹の先へ</h2>",
 "Latin Core and Latin Pareto are the whole 2,000-word reading course, grammar-complete at tier 10. There is deliberately no third staircase.":
   "Latin CoreとLatin Paretoで、2,000語の読解コースはまるごと完結し、ティア10で文法が出そろいます。3つめの階段は、意図して用意していません。",

 ">Latin — the two branches<": ">ラテン語 — 二つの枝<",
 "Classical poetry · or ecclesiastical Latin": "古典詩 · または教会ラテン語",
 "Past 2,000 words Latin genuinely divides, and which thousand comes next depends on what you want to read: <b>classical poetry</b> — Vergil, Ovid, Catullus, Horace — or <b>ecclesiastical Latin</b>, the Vulgate, the hymns and the liturgy. Both are inventoried and reserved. Neither is built, and neither takes the other as a prerequisite.":
   "2,000語を越えるとラテン語は本当に二手に分かれ、次の1,000語がどちらになるかは、何を読みたいかで決まります：<b>古典詩</b> — ウェルギリウス、オウィディウス、カトゥルス、ホラティウス — か、<b>教会ラテン語</b>、つまりウルガータ訳、賛歌、典礼のことばか。どちらも棚卸しを済ませ、枠を取ってあります。どちらもまだ作られておらず、どちらも他方を前提としません。",

 # ---- voices ----
 "<h2>Voices</h2>": "<h2>音声</h2>",
 ">Castellano — Spain, male<": ">Castellano — スペイン、男性<",
 "Replaces the included Latin American voice across every Spanish pack":
   "すべてのスペイン語パックで、同梱のラテンアメリカ音声を置き換えます",
 'A voice pack rather than a course: it swaps the voice in cards, lessons and boss fights, and switches back whenever you like. Hear it against the voice it replaces on the <a href="voices.html">voices page</a>.':
   'コースではなく音声パックです：カード、レッスン、ボス戦の声を差し替え、いつでも元に戻せます。置き換えられる側の音声との聴き比べは<a href="voices.html">音声のページ</a>で。',

 # ---- the closing note: the date here is the COUNTING date, not a release ----
 'Everything above was counted from the packs on <b>19 September 2026</b>. A pack leaves this page the day it goes on sale and appears on <a href="packs.html">the pack list</a> instead — so if something has vanished from here, look for it there.':
   '以上はすべて、<b>2026年9月19日</b>にパックから数えたものです。パックは発売された日にこのページを離れ、代わりに<a href="packs.html">パック一覧</a>に載ります — ここから消えたものがあれば、そちらを探してください。',
 "And yes — the page that lists what's in development used to be, itself, in development.":
   "そして、そのとおり — 開発中のものを並べるこのページ自体が、かつては開発中でした。",
}

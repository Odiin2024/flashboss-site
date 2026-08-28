/* ============================================================
   FlashBoss — client-side language matching (GitHub Pages).

   GitHub Pages is static: it can't read Accept-Language or do a
   server 302. So the English (canonical) pages carry this script
   SYNCHRONOUSLY in <head> — it runs before the body paints, so a
   matched visitor never sees a flash of English. Point the Steam
   "Website" field / ad links at the English URL and everyone lands
   in their own language when a translation exists.

   Behaviour:
     • Only the English pages include this file. A fresh visit whose
       browser prefers de/es/ja is sent to that variant (when it
       exists). If English is the top preference, or no translation
       exists, the visitor stays on English (graceful fallback).
     • One redirect per tab session (sessionStorage guard) — after
       that, the on-page EN▾ switcher lets anyone read English with
       no bounce-back. A new visit re-matches.

   MAINTENANCE: AVAIL maps each page's base name -> the locales that
   have a translated file. When a localized page ships (or a locale
   is dropped), update the one line here. Keep it in sync with the
   hreflang blocks. Locale codes: de, es, ja, zh, ru.
   ============================================================ */
(function () {
  var AVAIL = {
    'home':           ['de', 'es', 'ja', 'zh', 'ru'],
    'packs':          ['de', 'es', 'ja', 'zh', 'ru'],
    'voices':         ['de', 'es', 'ja', 'zh', 'ru'],
    'about':          ['de', 'es', 'ja', 'zh', 'ru'],
    'resources':      ['de', 'es', 'ja', 'zh', 'ru'],
    'wordlists':      ['de', 'es', 'ja', 'zh', 'ru'],
    'lessons':        ['de', 'es', 'ja', 'zh', 'ru'],
    'latin-roots':    ['de', 'es', 'ja', 'zh', 'ru'],
    'french':         ['de', 'es', 'ja', 'zh', 'ru'],
    'toki-pona':      ['de', 'es', 'ja', 'zh', 'ru'],
    'german-roots':   ['de', 'es', 'ja', 'zh', 'ru'],
    'norman-roots':   ['de', 'es', 'ja', 'zh', 'ru'],
    'german':         ['de', 'es', 'ja', 'zh', 'ru'],
    'spanish':        ['de', 'es', 'ja', 'zh', 'ru'],
    'italian':        ['de', 'es', 'ja', 'zh', 'ru'],
    'esperanto':      ['de', 'es', 'ja', 'zh', 'ru'],
    'index':          ['de', 'es', 'ja', 'zh', 'ru'],
    'greek-roots':    ['de', 'es', 'ja', 'zh', 'ru'],
    'english':        ['de', 'es', 'ja', 'zh', 'ru'],
    'affiliate':      ['de', 'es', 'ja', 'zh', 'ru'],
    'in-development':  ['de', 'es', 'ja', 'zh', 'ru']
  };
  try {
    var file = location.pathname.split('/').pop();
    if (!file) file = 'index.html';                        // directory URL -> the index document
    if (file.slice(-5) !== '.html') return;                // non-html asset
    var base = file.slice(0, -5);
    var locales = AVAIL[base];
    if (!locales) return;                                  // not a localized page
    if (sessionStorage.getItem('fbLang') === '1') return;  // already matched this session

    var prefs = navigator.languages || [navigator.language || 'en'];
    var pick = null;
    for (var i = 0; i < prefs.length; i++) {
      var two = String(prefs[i] || '').slice(0, 2).toLowerCase();
      if (two === 'en') break;                             // English preferred -> stay
      if (locales.indexOf(two) !== -1) { pick = two; break; }
    }
    if (!pick) return;

    sessionStorage.setItem('fbLang', '1');
    location.replace(base + '.' + pick + '.html' + location.search + location.hash);
  } catch (e) { /* storage blocked / unsupported — fail open to English */ }
})();

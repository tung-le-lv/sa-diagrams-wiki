# -*- coding: utf-8 -*-
"""Assembles the site. Run: python build.py

One page per category and per level, plus a learning-path page and an overview:

    index.html                overview, level cards, question table, category index
    learning-path.html        the three levels, sequenced
    level-<slug>.html         every entry at one level           (3)
    <category-slug>.html      every entry in one category       (15)
"""
from entries import *

import os, re, json

ROOT = os.path.dirname(os.path.abspath(__file__))

LEVELS   = {1:("Foundation","level-foundation","t1"),
            2:("Core practice","level-core-practice","t2"),
            3:("Specialist","level-specialist","t3")}
CATNAME  = {i:n for i,n,_,_ in CATS}
CATSLUG  = {i:s for i,_,s,_ in CATS}
STAGE    = {l:(n,out,body) for l,n,out,body in STAGES}
PATH_BY_NAME = {name:(lvl,step) for lvl,step,label,name in PATH}
PATH_ORDER   = {name:i+1 for i,(lvl,step,label,name)
                in enumerate(sorted(PATH,key=lambda r:(r[0],r[1])))}
BY_NAME  = {en["name"]: en for en in E}

def slug(s):
    return re.sub(r"-+","-",re.sub(r"[^a-z0-9]+","-",s.lower())).strip("-")

def anchor(name):
    return "d-"+slug(name)

def url(en):
    """An entry's canonical home is its category page."""
    return "%s.html#%s" % (CATSLUG[en["cat"]], anchor(en["name"]))

# ------------------------------------------------------------------ validation
PAINT_OK = re.compile(r'^(#[0-9A-Fa-f]{3,8}|none|url\(#\w+\)|currentColor)$')

def check_plates():
    """A colour argument passed by mistake into a positional slot renders as an invalid
    paint value, which browsers drop silently — the shape just disappears. Catch it here."""
    bad=[]
    for en in E:
        for attr,val in re.findall(r'\b(fill|stroke)="([^"]*)"', en["svg"]):
            if not PAINT_OK.match(val):
                bad.append("%s: %s=%r" % (en["name"], attr, val))
    if bad:
        raise SystemExit("Invalid SVG paint values:\n  " + "\n  ".join(sorted(set(bad))))

def check_text_fit():
    """Rough fit check for icon boxes: left-aligned text can run past the box edge, and SVG
    will happily draw it there. The condensed face averages ~0.5em per character."""
    import svg_kit
    warn=[]
    for tx, by, right, h, text, fs in svg_kit._boxes:
        over = (tx + len(text)*fs*0.50) - (right-6)
        if over > 0: warn.append("%6.0fpx over  %r" % (over, text))
    return sorted(set(warn), reverse=True)

# ------------------------------------------------------------------------ CSS
CSS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Sans+Condensed:wght@600;700&display=swap">
<style>
:root{
  --paper:#EDEFF1; --surface:#F9FAFB; --ink:#14181B; --ink2:#3D464E; --muted:#66707A;
  --line:#D4D9DE; --hair:#E4E8EB; --accent:#1F5F8B;
  --accent-ink:#134568; --accent-soft:#E1EBF3; --flag:#9C4034; --flag-soft:#F4E7E4;
  --amb:#7A5C1F; --amb-soft:#F4EEDF; --grn:#33604A; --grn-soft:#E4EEE8;
  --plate:#FFFFFF; --plate-line:#DEE3E7; --shadow:0 1px 2px rgba(20,30,40,.06),0 8px 24px -14px rgba(20,30,40,.28);
  --disp:'IBM Plex Sans Condensed',system-ui,-apple-system,'Segoe UI',sans-serif;
  --sans:'IBM Plex Sans',system-ui,-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
  --mono:'IBM Plex Mono',ui-monospace,SFMono-Regular,Menlo,monospace;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --paper:#111417; --surface:#191D21; --ink:#E8EBED; --ink2:#BAC3CA; --muted:#8A949D;
  --line:#292F35; --hair:#20262A; --accent:#79B7DF; --accent-ink:#A3CDEA; --accent-soft:#16242E;
  --flag:#D28D80; --flag-soft:#2A1D1A; --amb:#D0B475; --amb-soft:#25211A; --grn:#8CBFA3; --grn-soft:#182420;
  --shadow:0 1px 2px rgba(0,0,0,.5),0 10px 28px -14px rgba(0,0,0,.8);
}}
:root[data-theme="dark"]{
  --paper:#111417; --surface:#191D21; --ink:#E8EBED; --ink2:#BAC3CA; --muted:#8A949D;
  --line:#292F35; --hair:#20262A; --accent:#79B7DF; --accent-ink:#A3CDEA; --accent-soft:#16242E;
  --flag:#D28D80; --flag-soft:#2A1D1A; --amb:#D0B475; --amb-soft:#25211A; --grn:#8CBFA3; --grn-soft:#182420;
  --shadow:0 1px 2px rgba(0,0,0,.5),0 10px 28px -14px rgba(0,0,0,.8);
}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);
  font-size:14.5px;line-height:1.6;-webkit-font-smoothing:antialiased}
a{color:var(--accent-ink)}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:2px}

header.top{position:sticky;top:0;z-index:20;background:var(--surface);
  border-bottom:1px solid var(--line);padding:14px 26px}
.topin{max-width:1180px;margin:0 auto;display:flex;align-items:baseline;gap:20px;flex-wrap:wrap}
.brand{font-family:var(--disp);font-weight:700;font-size:19px;letter-spacing:.005em;margin:0}
.brand a{text-decoration:none;color:var(--ink)}
.brand em{font-style:normal;color:var(--accent-ink)}
.tagline{font-family:var(--mono);font-size:11px;color:var(--muted);letter-spacing:.02em;margin:0}
.search{margin-left:auto;display:flex;align-items:center;gap:9px}
.search input{font-family:var(--mono);font-size:12.5px;color:var(--ink);background:var(--paper);
  border:1px solid var(--line);border-radius:3px;padding:7px 11px;width:236px}
.search input::placeholder{color:var(--muted)}
#count{font-family:var(--mono);font-size:11px;color:var(--muted);white-space:nowrap}

.shell{max-width:1180px;margin:0 auto;padding:0 26px 80px;display:grid;
  grid-template-columns:224px minmax(0,1fr);gap:44px;align-items:start}

nav.cats{position:sticky;top:78px;max-height:calc(100vh - 96px);overflow-y:auto;
  padding:30px 0 20px;display:flex;flex-direction:column;gap:2px;scrollbar-width:thin}
.navlabel{font-family:var(--mono);font-size:10px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--muted);margin:0 0 10px 8px}
.navlabel.second{margin-top:20px;padding-top:16px;border-top:1px solid var(--hair)}
.cat{display:flex;gap:9px;align-items:baseline;font-family:var(--disp);font-size:13.5px;
  font-weight:600;color:var(--ink2);text-decoration:none;border-left:2px solid transparent;
  padding:5px 8px;line-height:1.3;border-radius:0 3px 3px 0}
.cat:hover{color:var(--ink);background:var(--hair)}
.cat[aria-current="page"]{color:var(--accent-ink);border-left-color:var(--accent);
  background:var(--accent-soft);font-weight:700}
.cat .n{font-family:var(--mono);font-size:10px;color:var(--muted);min-width:15px}
.cat .k{font-family:var(--mono);font-size:10px;color:var(--muted);margin-left:auto}
.cat.star .n{color:var(--flag)}

main{padding-top:30px;min-width:0}
#pagebody{display:flex;flex-direction:column;gap:14px}

.phead{margin:0 0 6px}
.crumb{font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;
  color:var(--muted);margin:0 0 7px}
.crumb a{color:var(--muted);text-decoration:none}
.crumb a:hover{color:var(--accent-ink)}
h1.ptitle{font-family:var(--disp);font-weight:700;font-size:29px;letter-spacing:.004em;
  margin:0 0 9px;line-height:1.12;text-wrap:balance}
.pblurb{margin:0;max-width:72ch;color:var(--ink2);font-size:15px}
.pblurb b{color:var(--ink);font-weight:600}
.pmeta{font-family:var(--mono);font-size:11px;color:var(--muted);margin:11px 0 0}

.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(252px,1fr));gap:12px;margin:0}
a.card{display:block;text-decoration:none;background:var(--surface);border:1px solid var(--line);
  border-radius:4px;padding:15px 16px 16px;box-shadow:var(--shadow)}
a.card:hover{border-color:var(--accent)}
a.card .cn{font-family:var(--mono);font-size:10px;color:var(--muted);letter-spacing:.08em}
a.card h3{font-family:var(--disp);font-weight:700;font-size:16.5px;margin:3px 0 5px;
  color:var(--ink);line-height:1.2}
a.card:hover h3{color:var(--accent-ink)}
a.card p{margin:0;font-size:12.8px;color:var(--muted);line-height:1.5}
a.card .k{font-family:var(--mono);font-size:10px;color:var(--accent-ink);margin-top:9px;display:block}
a.lcard{border-left:3px solid var(--line)}
a.lcard.l1{border-left-color:var(--flag)} a.lcard.l2{border-left-color:var(--amb)}
a.lcard.l3{border-left-color:var(--grn)}
a.lcard.l1 h3{color:var(--flag)} a.lcard.l2 h3{color:var(--amb)} a.lcard.l3 h3{color:var(--grn)}
.sect{font-family:var(--mono);font-size:10px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--muted);margin:20px 0 2px}

ol.path{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:1px;
  background:var(--hair);border:1px solid var(--hair);border-radius:4px;overflow:hidden}
li.stage{background:var(--surface);display:grid;grid-template-columns:250px minmax(0,1fr);
  gap:26px;padding:20px 20px 21px;position:relative}
li.stage::before{content:"";position:absolute;left:0;top:0;bottom:0;width:3px}
li.stage.s1::before{background:var(--flag)}
li.stage.s2::before{background:var(--amb)}
li.stage.s3::before{background:var(--grn)}
.stage-head .sn{font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;
  color:var(--muted);display:block;margin-bottom:4px}
.stage-head h2{font-family:var(--disp);font-weight:700;font-size:19px;margin:0 0 3px;line-height:1.2}
.stage.s1 .stage-head h2{color:var(--flag)}
.stage.s2 .stage-head h2{color:var(--amb)}
.stage.s3 .stage-head h2{color:var(--grn)}
.stage-head .outcome{margin:0 0 7px;font-size:13.4px;font-weight:600;color:var(--ink)}
.stage-head p{margin:0 0 11px;font-size:12.4px;color:var(--muted);line-height:1.5}
.stage-head .more{font-family:var(--mono);font-size:10.5px;text-decoration:none}
ol.steps{margin:0;padding:0;list-style:none;display:flex;flex-wrap:wrap;gap:6px;
  align-content:flex-start;counter-reset:st}
ol.steps li{counter-increment:st}
ol.steps a{display:inline-flex;gap:7px;align-items:baseline;text-decoration:none;color:var(--ink2);
  font-size:13px;border:1px solid var(--line);background:var(--paper);border-radius:3px;
  padding:4px 10px;line-height:1.35}
ol.steps a::before{content:counter(st);font-family:var(--mono);font-size:9.5px;color:var(--muted)}
ol.steps a:hover{border-color:var(--accent);background:var(--accent-soft);color:var(--accent-ink)}
ol.steps a:hover::before{color:var(--accent-ink)}

.qwrap{background:var(--surface);border:1px solid var(--line);border-radius:4px;
  padding:18px 20px 16px;box-shadow:var(--shadow)}
.qwrap>p{font-family:var(--mono);font-size:9.5px;letter-spacing:.11em;text-transform:uppercase;
  color:var(--muted);margin:0 0 11px}
.qgrid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1px 26px;margin:0}
.qgrid a{display:flex;gap:10px;align-items:baseline;justify-content:space-between;
  text-decoration:none;padding:5px 6px;border-radius:3px;border-bottom:1px solid var(--hair)}
.qgrid a:hover{background:var(--accent-soft)}
.qgrid .q{color:var(--ink2);font-size:13.2px}
.qgrid .d{font-family:var(--disp);font-weight:600;font-size:12.5px;color:var(--accent-ink);
  white-space:nowrap}

article.entry{background:var(--surface);border:1px solid var(--line);border-radius:4px;
  padding:24px 26px 26px;box-shadow:var(--shadow);scroll-margin-top:88px}
article.entry.flash{border-color:var(--accent);box-shadow:0 0 0 2px var(--accent-soft),var(--shadow)}
.ehead{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;margin-bottom:3px}
.plateno{font-family:var(--mono);font-size:11px;color:var(--accent-ink);letter-spacing:.06em;
  background:var(--accent-soft);padding:2px 7px;border-radius:2px}
h2.name{font-family:var(--disp);font-weight:700;font-size:23px;letter-spacing:.004em;margin:0;
  text-wrap:balance;line-height:1.15}
.badges{margin-left:auto;display:flex;gap:7px;align-items:baseline;flex-wrap:wrap}
.tier{font-family:var(--mono);font-size:10px;letter-spacing:.08em;text-transform:uppercase;
  padding:2px 7px;border-radius:2px;border:1px solid var(--line);color:var(--muted);text-decoration:none}
.tier.t1{color:var(--flag);border-color:var(--flag);background:var(--flag-soft)}
.onpath{font-family:var(--mono);font-size:10px;letter-spacing:.06em;padding:2px 7px;
  border-radius:2px;border:1px solid var(--accent);color:var(--accent-ink);
  background:var(--accent-soft);text-decoration:none}
.catline{font-family:var(--mono);font-size:10.5px;letter-spacing:.09em;text-transform:uppercase;
  color:var(--muted);margin:0 0 12px}
.catline a{color:var(--muted);text-decoration:none}
.catline a:hover{color:var(--accent-ink)}
p.defn{margin:0 0 18px;max-width:70ch;font-size:15px;color:var(--ink2)}
ul.alias{list-style:none;display:flex;flex-wrap:wrap;gap:6px;margin:0 0 20px;padding:0}
ul.alias li{font-family:var(--mono);font-size:10px;color:var(--muted);border:1px solid var(--hair);
  background:var(--paper);border-radius:2px;padding:2px 7px}
ul.alias li.lab{border-color:transparent;background:none;letter-spacing:.08em;text-transform:uppercase}

figure.fig{margin:0 0 20px}
.sheet{background:var(--plate);border:1px solid var(--plate-line);border-radius:3px;
  box-shadow:0 1px 3px rgba(20,30,40,.07);padding:16px 18px;overflow-x:auto}
svg.plate{display:block;width:100%;height:auto;min-width:560px;font-family:var(--disp)}
figcaption{font-family:var(--mono);font-size:11px;color:var(--muted);margin-top:9px;line-height:1.5}
figcaption::before{content:"Fig. ";color:var(--accent-ink)}

dl.facts{margin:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));
  gap:1px;background:var(--hair);border:1px solid var(--hair);border-radius:3px;overflow:hidden}
dl.facts>div{background:var(--surface);padding:13px 15px}
dl.facts>div.fail{background:var(--flag-soft)}
dt{font-family:var(--mono);font-size:9.5px;letter-spacing:.11em;text-transform:uppercase;
  color:var(--muted);margin:0 0 4px}
div.fail dt{color:var(--flag)}
dd{margin:0;font-size:13.8px;line-height:1.55;color:var(--ink2)}

ol.listing{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:1px;
  background:var(--hair);border:1px solid var(--hair);border-radius:4px;overflow:hidden}
ol.listing a{background:var(--surface);display:grid;
  grid-template-columns:32px minmax(0,1fr) minmax(0,1.35fr);gap:14px;align-items:baseline;
  padding:11px 15px;text-decoration:none}
ol.listing a:hover{background:var(--accent-soft)}
ol.listing .st{font-family:var(--mono);font-size:10px;color:var(--muted)}
ol.listing .nm{font-family:var(--disp);font-weight:600;font-size:14px;color:var(--ink)}
ol.listing a:hover .nm{color:var(--accent-ink)}
ol.listing .an{font-size:12.8px;color:var(--muted);line-height:1.45}

.pager{display:flex;gap:12px;justify-content:space-between;margin-top:6px}
.pager a,.pager span.sp{flex:1 1 0;min-width:0}
.pager a{background:var(--surface);border:1px solid var(--line);border-radius:4px;
  padding:12px 15px;text-decoration:none;box-shadow:var(--shadow)}
.pager a:hover{border-color:var(--accent)}
.pager a span{display:block;font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--muted);margin-bottom:3px}
.pager b{font-family:var(--disp);font-size:14.5px;font-weight:700;color:var(--ink)}
.pager a:hover b{color:var(--accent-ink)}
.pager .nx{text-align:right}

#results{display:none;flex-direction:column;gap:1px;background:var(--hair);
  border:1px solid var(--hair);border-radius:4px;overflow:hidden}
#results a{background:var(--surface);display:block;padding:13px 16px;text-decoration:none}
#results a:hover{background:var(--accent-soft)}
#results .rn{font-family:var(--disp);font-weight:700;font-size:15.5px;color:var(--ink)}
#results a:hover .rn{color:var(--accent-ink)}
#results .rm{font-family:var(--mono);font-size:10px;letter-spacing:.07em;text-transform:uppercase;
  color:var(--muted);margin-left:9px;white-space:nowrap}
#results .ra{display:block;margin-top:3px;font-size:13px;color:var(--ink2)}
#results p.none{background:var(--surface);font-family:var(--mono);font-size:13px;
  color:var(--muted);padding:26px 16px;margin:0}
footer{max-width:1180px;margin:0 auto;padding:0 26px 60px;font-family:var(--mono);
  font-size:11px;color:var(--muted);line-height:1.7}
footer a{color:var(--muted)}

@media (max-width:900px){
  .shell{grid-template-columns:1fr;gap:0;padding:0 18px 60px}
  nav.cats{position:static;max-height:none;flex-direction:row;overflow-x:auto;padding:18px 0 4px;
    gap:6px;border-bottom:1px solid var(--line);align-items:center}
  .navlabel{display:none}
  .cat{white-space:nowrap;border-left:0;border-bottom:2px solid transparent;border-radius:3px;padding:6px 10px}
  .cat[aria-current="page"]{border-left:0;border-bottom-color:var(--accent)}
  .cat .k{display:none}
  article.entry{padding:20px 18px}
  dl.facts{grid-template-columns:1fr}
  li.stage{grid-template-columns:1fr;gap:12px}
  .qgrid{grid-template-columns:1fr}
  ol.listing a{grid-template-columns:26px 1fr;gap:6px 10px}
  ol.listing .an{grid-column:2}
  .pager{flex-direction:column}
  .pager .nx{text-align:left}
  h1.ptitle{font-size:24px}
  .search{margin-left:0;width:100%}
  .search input{flex:1;width:auto}
  h2.name{font-size:20px}
  .badges{margin-left:0;width:100%}
}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
</style>
"""

# ------------------------------------------------------------------ fragments
def render_entry(en, idx):
    lname, lslug, lcls = LEVELS[en["tier"]]
    step = PATH_BY_NAME.get(en["name"])
    badge = ('<a class="onpath" href="learning-path.html">learning path · step %d</a>' % step[1]) if step else ""
    alias = ""
    if en["alias"]:
        alias = ('<ul class="alias"><li class="lab">also called</li>'
                 + "".join('<li>%s</li>' % e(a) for a in en["alias"]) + '</ul>')
    return (
    '<article class="entry" id="%s">'
    '<div class="ehead"><span class="plateno">%02d.%d</span><h2 class="name">%s</h2>'
    '<span class="badges">%s<a class="tier %s" href="%s.html">%s</a></span></div>'
    '<p class="catline"><a href="%s.html">%s</a></p>'
    '<p class="defn">%s</p>%s'
    '<figure class="fig"><div class="sheet">%s</div><figcaption>%s</figcaption></figure>'
    '<dl class="facts">'
    '<div><dt>Answers</dt><dd>%s</dd></div>'
    '<div><dt>Reach for it when</dt><dd>%s</dd></div>'
    '<div><dt>It must show</dt><dd>%s</dd></div>'
    '<div class="fail"><dt>Common failure</dt><dd>%s</dd></div>'
    '</dl></article>'
    % (anchor(en["name"]), en["cat"], idx, e(en["name"]), badge, lcls, lslug, e(lname),
       CATSLUG[en["cat"]], e(CATNAME[en["cat"]]), e(en["defn"]), alias,
       en["svg"], e(en["cap"]), e(en["answers"]), e(en["when"]), e(en["must"]), e(en["fail"])))

# Plate number NN.n — position within the entry's own category, in declaration order.
CAT_INDEX, _seen = {}, {}
for _en in E:
    _seen[_en["cat"]] = _seen.get(_en["cat"], 0) + 1
    CAT_INDEX[_en["name"]] = _seen[_en["cat"]]

def nav(active):
    n = ('<a class="cat" href="index.html"%s><span class="n">⌂</span><span>Overview</span></a>'
         % (' aria-current="page"' if active == "index" else ""))
    n += '<p class="navlabel second">By level</p>'
    n += ('<a class="cat star" href="learning-path.html"%s><span class="n">★</span>'
          '<span>Learning path</span><span class="k">%d</span></a>'
          % (' aria-current="page"' if active == "learning-path" else "", len(PATH)))
    for l in (1, 2, 3):
        name, lslug, _ = LEVELS[l]
        cnt = sum(1 for x in E if x["tier"] == l)
        n += ('<a class="cat" href="%s.html"%s><span class="n">L%d</span>'
              '<span>%s</span><span class="k">%d</span></a>'
              % (lslug, ' aria-current="page"' if active == lslug else "", l, e(name), cnt))
    n += '<p class="navlabel second">Categories</p>'
    for i, name, cslug, _ in CATS:
        cnt = sum(1 for x in E if x["cat"] == i)
        n += ('<a class="cat" href="%s.html"%s><span class="n">%02d</span>'
              '<span>%s</span><span class="k">%d</span></a>'
              % (cslug, ' aria-current="page"' if active == cslug else "", i, e(name), cnt))
    return n

def pager(prev, nxt):
    if not prev and not nxt: return ""
    out = '<div class="pager">'
    out += (('<a href="%s.html"><span>Previous</span><b>%s</b></a>' % (prev[0], e(prev[1])))
            if prev else '<span class="sp"></span>')
    out += (('<a class="nx" href="%s.html"><span>Next</span><b>%s</b></a>' % (nxt[0], e(nxt[1])))
            if nxt else '<span class="sp"></span>')
    return out + '</div>'

SEARCH_INDEX = json.dumps(
    [[en["name"], url(en), CATNAME[en["cat"]], LEVELS[en["tier"]][0], en["answers"],
      " ".join([en["name"], CATNAME[en["cat"]], en["answers"], en["when"]] + en["alias"]).lower()]
     for en in E], ensure_ascii=False, separators=(",", ":"))

JS = """
<script>window.IDX=%s;</script>
<script>
(function(){
  var box=document.getElementById('q'), count=document.getElementById('count'),
      res=document.getElementById('results'), body=document.getElementById('pagebody');
  function esc(s){return s.replace(/[&<>"]/g,function(c){
    return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
  function run(){
    var t=(box.value||'').trim().toLowerCase();
    if(!t){ res.style.display='none'; body.style.display=''; count.textContent=''; return; }
    var hits=window.IDX.filter(function(r){return r[5].indexOf(t)>-1;});
    res.innerHTML = hits.length
      ? hits.map(function(r){
          return '<a href="'+r[1]+'"><span class="rn">'+esc(r[0])+'</span>'
               + '<span class="rm">'+esc(r[2])+' \\u00b7 '+esc(r[3])+'</span>'
               + '<span class="ra">'+esc(r[4])+'</span></a>';}).join('')
      : '<p class="none">No diagram type matches that. Try \\u201cevent\\u201d, '
        + '\\u201cfailover\\u201d or \\u201clineage\\u201d.</p>';
    res.style.display='flex'; body.style.display='none';
    count.textContent = hits.length + (hits.length===1?' match':' matches');
  }
  box.addEventListener('input', run);
  if(box.value) run();
  var t;
  function flash(){
    if(location.hash.length<2) return;
    var el=document.getElementById(location.hash.slice(1));
    if(!el || el.className.indexOf('entry')<0) return;
    clearTimeout(t); el.classList.add('flash');
    t=setTimeout(function(){el.classList.remove('flash');},1600);
  }
  window.addEventListener('hashchange', flash); flash();
})();
</script>
""" % SEARCH_INDEX

def page(fname, title, desc, active, body):
    html = ('<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
            '<meta name="description" content="%s">\n'
            '<title>%s</title>\n' % (e(desc), e(title))
        + CSS
        + ('<header class="top"><div class="topin">'
           '<h1 class="brand"><a href="index.html">Architecture <em>Diagram Dictionary</em></a></h1>'
           '<p class="tagline">%d types · %d categories · 3 levels</p>'
           '<div class="search"><input id="q" type="search" placeholder="Search all %d types…" '
           'aria-label="Search diagram types" autocomplete="off"><span id="count"></span></div>'
           '</div></header>' % (len(E), len(CATS), len(E)))
        + DEFS
        + '<div class="shell"><nav class="cats" aria-label="Sections">' + nav(active) + '</nav>'
          '<main><div id="results"></div><div id="pagebody">' + body + '</div></main></div>'
        + ('<footer>Levels &nbsp;—&nbsp; L1 foundation: describe any system. L2 core practice: '
           'design and operate a distributed one. L3 specialist: depth where the domain requires it. '
           '<a href="learning-path.html">The learning path</a> sequences %d of the %d types across '
           'those levels. Sample plates are drawn to one house style; they show the notation, not a '
           'real system.</footer>' % (len(PATH), len(E)))
        + JS)
    with open(os.path.join(ROOT, fname), "w", encoding="utf-8") as f:
        f.write(html)
    return len(html)

# ---------------------------------------------------------------------- pages
def build():
    written = []

    # overview -------------------------------------------------------------
    lcards = ""
    for l in (1, 2, 3):
        name, lslug, _ = LEVELS[l]
        _, outcome, _blurb = STAGE[l]
        cnt = sum(1 for x in E if x["tier"] == l)
        lcards += ('<a class="card lcard l%d" href="%s.html"><span class="cn">Level %d</span>'
                   '<h3>%s</h3><p>%s</p><span class="k">%d diagram types →</span></a>'
                   % (l, lslug, l, e(name), e(outcome), cnt))
    ccards = ""
    for i, name, cslug, blurb in CATS:
        cnt = sum(1 for x in E if x["cat"] == i)
        ccards += ('<a class="card" href="%s.html"><span class="cn">%02d</span><h3>%s</h3>'
                   '<p>%s</p><span class="k">%d types →</span></a>'
                   % (cslug, i, e(name), e(blurb), cnt))
    qrows = "".join('<a href="%s"><span class="q">%s</span><span class="d">%s</span></a>'
                    % (url(BY_NAME[n]), e(q), e(n)) for q, n in QUESTIONS)
    body = ('<div class="phead"><h1 class="ptitle">An architecture diagram dictionary</h1>'
            '<p class="pblurb">%d diagram types across %d categories — each with a sample plate, the '
            'question it answers, when to reach for it, what it must show, and the mistake that shows '
            'up in review. <b>Choose the diagram by the question you are trying to settle</b>, then '
            'draw only what that question needs.</p></div>'
            '<p class="sect">Start here · by level</p><div class="grid">%s</div>'
            '<p class="sect">Or start from the question you need to settle</p>'
            '<div class="qwrap"><p>Question → diagram</p><div class="qgrid">%s</div></div>'
            '<p class="sect">Browse by category</p><div class="grid">%s</div>'
            % (len(E), len(CATS), lcards, qrows, ccards))
    written.append(("index.html", page(
        "index.html", "Architecture Diagram Dictionary",
        "%d software architecture diagram types across %d categories — each with a sample plate, "
        "the question it answers, and the mistake that shows up in review." % (len(E), len(CATS)),
        "index", body)))

    # learning path --------------------------------------------------------
    stages = ""
    for l, name, outcome, blurb in STAGES:
        _, lslug, _ = LEVELS[l]
        chips = "".join('<li><a href="%s">%s</a></li>' % (url(BY_NAME[n]), e(label))
                        for lv, st, label, n in sorted(PATH, key=lambda r: (r[0], r[1])) if lv == l)
        stages += ('<li class="stage s%d"><div class="stage-head">'
                   '<span class="sn">Level %d · %d diagrams</span><h2>%s</h2>'
                   '<p class="outcome">%s</p><p>%s</p>'
                   '<a class="more" href="%s.html">All %d at this level →</a></div>'
                   '<ol class="steps">%s</ol></li>'
                   % (l, l, sum(1 for lv, _, _, _ in PATH if lv == l), e(name), e(outcome), e(blurb),
                      lslug, sum(1 for x in E if x["tier"] == l), chips))
    listing = "".join(
        '<li><a href="%s"><span class="st">%d</span><span class="nm">%s</span>'
        '<span class="an">%s</span></a></li>'
        % (url(BY_NAME[n]), PATH_ORDER[n], e(BY_NAME[n]["name"]), e(BY_NAME[n]["answers"]))
        for lv, st, label, n in sorted(PATH, key=lambda r: (r[0], r[1])))
    body = ('<div class="phead"><p class="crumb"><a href="index.html">Overview</a> · Learning path</p>'
            '<h1 class="ptitle">Learning path</h1>'
            '<p class="pblurb">%d types is a reference, not a syllabus. These %d carry most of the '
            'work, arranged in three levels that build on one another — each assumes the one above '
            'it. Everything else in the dictionary is here for the day a problem calls for it.</p>'
            '</div><ol class="path">%s</ol>'
            '<p class="sect">The path in order</p><ol class="listing">%s</ol>'
            % (len(E), len(PATH), stages, listing))
    written.append(("learning-path.html", page(
        "learning-path.html", "Learning path · Architecture Diagram Dictionary",
        "A three-level learning path through software architecture diagrams, from foundation to "
        "specialist.", "learning-path", body)))

    # one page per level ---------------------------------------------------
    for l in (1, 2, 3):
        name, lslug, _ = LEVELS[l]
        _, outcome, blurb = STAGE[l]
        ents = [x for x in E if x["tier"] == l]
        onpath = sum(1 for x in ents if x["name"] in PATH_BY_NAME)
        prev = ((LEVELS[l-1][1], "Level %d · %s" % (l-1, LEVELS[l-1][0])) if l > 1
                else ("learning-path", "Learning path"))
        nxt = (LEVELS[l+1][1], "Level %d · %s" % (l+1, LEVELS[l+1][0])) if l < 3 else None
        body = ('<div class="phead"><p class="crumb"><a href="index.html">Overview</a> · '
                '<a href="learning-path.html">Learning path</a> · Level %d</p>'
                '<h1 class="ptitle">%s</h1><p class="pblurb"><b>%s.</b> %s</p>'
                '<p class="pmeta">%d types at this level · %d of them on the learning path</p></div>'
                % (l, e(name), e(outcome), e(blurb), len(ents), onpath))
        body += "".join(render_entry(en, CAT_INDEX[en["name"]]) for en in ents)
        body += pager(prev, nxt)
        written.append((lslug + ".html", page(
            lslug + ".html", "%s · Architecture Diagram Dictionary" % name,
            "Level %d of the learning path — %s. %d diagram types."
            % (l, outcome[0].lower() + outcome[1:], len(ents)), lslug, body)))

    # one page per category ------------------------------------------------
    for pos, (i, name, cslug, blurb) in enumerate(CATS):
        ents = [x for x in E if x["cat"] == i]
        prev = ((CATS[pos-1][2], "%02d · %s" % (CATS[pos-1][0], CATS[pos-1][1])) if pos > 0
                else ("index", "Overview"))
        nxt = ((CATS[pos+1][2], "%02d · %s" % (CATS[pos+1][0], CATS[pos+1][1]))
               if pos < len(CATS) - 1 else None)
        lv = {}
        for x in ents: lv[x["tier"]] = lv.get(x["tier"], 0) + 1
        mix = " · ".join("%d %s" % (lv[k], LEVELS[k][0].lower()) for k in sorted(lv))
        body = ('<div class="phead"><p class="crumb"><a href="index.html">Overview</a> · '
                'Category %02d</p><h1 class="ptitle">%s</h1><p class="pblurb">%s</p>'
                '<p class="pmeta">%d types · %s</p></div>'
                % (i, e(name), e(blurb), len(ents), e(mix)))
        body += "".join(render_entry(en, n + 1) for n, en in enumerate(ents))
        body += pager(prev, nxt)
        written.append((cslug + ".html", page(
            cslug + ".html", "%s · Architecture Diagram Dictionary" % name,
            "%s %d diagram types." % (blurb, len(ents)), cslug, body)))
    return written


check_plates()
_fit = check_text_fit()
if _fit:
    print("text may overflow its box in %d place(s):" % len(_fit))
    for w in _fit: print("   " + w)

pages = build()
print("wrote %d pages, %.0f KB total, %d entries"
      % (len(pages), sum(n for _, n in pages) / 1024.0, len(E)))
for fname, n in pages:
    print("   %-32s %6.0f KB" % (fname, n / 1024.0))

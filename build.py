# -*- coding: utf-8 -*-
"""Assembles index.html. Run: python build.py"""
from entries import *

import os, re
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")

TIERS={1:("Must know","t1"),2:("Very important","t2"),3:("Know when to use","t3")}
CATNAME={i:n for i,n in CATS}
PRIO_BY_NAME={name:(tier,rank,label) for tier,rank,label,name in PRIORITY}
# Order used by the shortlist view: tier first, then the rank given in the notes.
PRIO_ORDER={name:i+1 for i,(tier,rank,label,name) in enumerate(sorted(PRIORITY,key=lambda r:(r[0],r[1])))}

def slug(s):
    return "d-"+re.sub(r"-+","-",re.sub(r"[^a-z0-9]+","-",s.lower())).strip("-")

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
.brand em{font-style:normal;color:var(--accent-ink)}
.tagline{font-family:var(--mono);font-size:11px;color:var(--muted);letter-spacing:.02em;margin:0}
.search{margin-left:auto;display:flex;align-items:center;gap:9px}
.search input{font-family:var(--mono);font-size:12.5px;color:var(--ink);background:var(--paper);
  border:1px solid var(--line);border-radius:3px;padding:7px 11px;width:232px}
.search input::placeholder{color:var(--muted)}
#count{font-family:var(--mono);font-size:11px;color:var(--muted);white-space:nowrap}

.shell{max-width:1180px;margin:0 auto;padding:0 26px 80px;display:grid;
  grid-template-columns:224px minmax(0,1fr);gap:44px;align-items:start}

nav.cats{position:sticky;top:78px;max-height:calc(100vh - 96px);overflow-y:auto;
  padding:30px 0 20px;display:flex;flex-direction:column;gap:2px;scrollbar-width:thin}
.navlabel{font-family:var(--mono);font-size:10px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--muted);margin:0 0 10px 8px}
.navlabel.second{margin-top:20px;padding-top:16px;border-top:1px solid var(--hair)}
.cat{display:flex;gap:9px;align-items:baseline;font-family:var(--disp);font-size:13.5px;font-weight:600;
  color:var(--ink2);background:none;border:0;border-left:2px solid transparent;
  padding:5px 8px;text-align:left;cursor:pointer;line-height:1.3;border-radius:0 3px 3px 0}
.cat:hover{color:var(--ink);background:var(--hair)}
.cat[aria-pressed="true"]{color:var(--accent-ink);border-left-color:var(--accent);
  background:var(--accent-soft);font-weight:700}
.cat .n{font-family:var(--mono);font-size:10px;color:var(--muted);min-width:15px}
.cat .k{font-family:var(--mono);font-size:10px;color:var(--muted);margin-left:auto}
.cat.star .n{color:var(--flag)}

main{padding-top:30px;display:flex;flex-direction:column;gap:14px}
.intro{order:-3;border-left:2px solid var(--accent);padding:2px 0 2px 16px;margin:0 0 6px;
  max-width:66ch;color:var(--ink2);font-size:14.5px}
.intro b{color:var(--ink);font-weight:600}
main.prio-view article.entry{order:var(--po,999)}
.empty{order:9999}

/* ---- the shortlist panel ---- */
section.priority{order:-2;background:var(--surface);border:1px solid var(--line);
  border-radius:4px;padding:24px 26px 22px;box-shadow:var(--shadow);margin-bottom:6px}
.priority>h2{font-family:var(--disp);font-weight:700;font-size:22px;margin:0 0 4px;
  letter-spacing:.004em;line-height:1.2;text-wrap:balance}
.priority>p.plede{margin:0 0 20px;color:var(--ink2);max-width:70ch;font-size:14px}
.ptiers{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1px;
  background:var(--hair);border:1px solid var(--hair);border-radius:3px;overflow:hidden}
.ptier{background:var(--surface);padding:14px 16px 16px}
.pt-h{font-family:var(--mono);font-size:9.5px;letter-spacing:.11em;text-transform:uppercase;
  color:var(--muted);margin:0 0 9px;display:flex;gap:7px;align-items:baseline}
.pt-h b{font-weight:600}
.ptier.a .pt-h b{color:var(--flag)}
.ptier.b .pt-h b{color:var(--amb)}
.ptier.c .pt-h b{color:var(--grn)}
.ptier ol{margin:0;padding:0;list-style:none;counter-reset:p}
.ptier li{counter-increment:p;margin:0 0 1px}
.ptier a{display:flex;gap:8px;align-items:baseline;text-decoration:none;color:var(--ink2);
  font-size:13.2px;padding:3px 5px;border-radius:3px;line-height:1.35}
.ptier a::before{content:counter(p);font-family:var(--mono);font-size:9.5px;color:var(--muted);
  min-width:12px;text-align:right}
.ptier a:hover{background:var(--accent-soft);color:var(--accent-ink)}
.qwrap{margin-top:22px;padding-top:18px;border-top:1px solid var(--hair)}
.qwrap>p{font-family:var(--mono);font-size:9.5px;letter-spacing:.11em;text-transform:uppercase;
  color:var(--muted);margin:0 0 11px}
.qgrid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1px 26px;margin:0}
.qgrid a{display:flex;gap:10px;align-items:baseline;justify-content:space-between;
  text-decoration:none;padding:5px 6px;border-radius:3px;border-bottom:1px solid var(--hair)}
.qgrid a:hover{background:var(--accent-soft)}
.qgrid .q{color:var(--ink2);font-size:13.2px}
.qgrid .d{font-family:var(--disp);font-weight:600;font-size:12.5px;color:var(--accent-ink);
  white-space:nowrap}

/* ---- entries ---- */
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
  padding:2px 7px;border-radius:2px;border:1px solid var(--line);color:var(--muted)}
.tier.t1{color:var(--flag);border-color:var(--flag);background:var(--flag-soft)}
.shortlist{font-family:var(--mono);font-size:10px;letter-spacing:.06em;padding:2px 7px;
  border-radius:2px;border:1px solid var(--accent);color:var(--accent-ink);background:var(--accent-soft)}
.catline{font-family:var(--mono);font-size:10.5px;letter-spacing:.09em;text-transform:uppercase;
  color:var(--muted);margin:0 0 12px}
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

.empty{font-family:var(--mono);font-size:13px;color:var(--muted);padding:40px 0}
footer{max-width:1180px;margin:0 auto;padding:0 26px 60px;font-family:var(--mono);
  font-size:11px;color:var(--muted);line-height:1.7}

@media (max-width:900px){
  .shell{grid-template-columns:1fr;gap:0;padding:0 18px 60px}
  nav.cats{position:static;max-height:none;flex-direction:row;overflow-x:auto;padding:18px 0 4px;
    gap:6px;border-bottom:1px solid var(--line);align-items:center}
  .navlabel{display:none}
  .navlabel.second{display:none}
  .cat{white-space:nowrap;border-left:0;border-bottom:2px solid transparent;border-radius:3px;padding:6px 10px}
  .cat[aria-pressed="true"]{border-left:0;border-bottom-color:var(--accent)}
  .cat .k{display:none}
  article.entry{padding:20px 18px}
  dl.facts{grid-template-columns:1fr}
  .ptiers{grid-template-columns:1fr}
  .qgrid{grid-template-columns:1fr}
  section.priority{padding:20px 18px}
  .search{margin-left:0;width:100%}
  .search input{flex:1;width:auto}
  h2.name{font-size:20px}
  .badges{margin-left:0;width:100%}
}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
</style>
"""

def build():
    ids={en["name"]:slug(en["name"]) for en in E}
    per={}; rows=[]
    for en in E:
        per[en["cat"]]=per.get(en["cat"],0)+1
        idx=per[en["cat"]]
        tname,tcls=TIERS[en["tier"]]
        prio=PRIO_BY_NAME.get(en["name"])
        q=" ".join([en["name"],CATNAME[en["cat"]],en["defn"],en["answers"],en["when"]]+en["alias"]).lower()
        badge=('<span class="shortlist">shortlist · tier %d #%d</span>'%(prio[0],prio[1])) if prio else ""
        alias=""
        if en["alias"]:
            alias='<ul class="alias"><li class="lab">also called</li>'+"".join(
                '<li>%s</li>'%e(a) for a in en["alias"])+'</ul>'
        rows.append(
        '<article class="entry" id="%s" data-cat="%d" data-tier="%d" data-prio="%d"%s data-q="%s">'
        '<div class="ehead"><span class="plateno">%02d.%d</span><h2 class="name">%s</h2>'
        '<span class="badges">%s<span class="tier %s">%s</span></span></div>'
        '<p class="catline">%s</p>'
        '<p class="defn">%s</p>%s'
        '<figure class="fig"><div class="sheet">%s</div><figcaption>%s</figcaption></figure>'
        '<dl class="facts">'
        '<div><dt>Answers</dt><dd>%s</dd></div>'
        '<div><dt>Reach for it when</dt><dd>%s</dd></div>'
        '<div><dt>It must show</dt><dd>%s</dd></div>'
        '<div class="fail"><dt>Common failure</dt><dd>%s</dd></div>'
        '</dl></article>'
        %(ids[en["name"]],en["cat"],en["tier"],1 if prio else 0,
          (' style="--po:%d"'%PRIO_ORDER[en["name"]]) if prio else "",
          e(q),en["cat"],idx,e(en["name"]),badge,tcls,e(tname),e(CATNAME[en["cat"]]),
          e(en["defn"]),alias,en["svg"],e(en["cap"]),e(en["answers"]),e(en["when"]),
          e(en["must"]),e(en["fail"])))

    counts={}; tcounts={}
    for en in E:
        counts[en["cat"]]=counts.get(en["cat"],0)+1
        tcounts[en["tier"]]=tcounts.get(en["tier"],0)+1

    nav='<p class="navlabel">Architect’s priority</p>'
    nav+=('<button class="cat star" data-f="prio" aria-pressed="false"><span class="n">★</span>'
          '<span>The shortlist</span><span class="k">%d</span></button>'%len(PRIORITY))
    for t in (1,2,3):
        nav+=('<button class="cat" data-f="t%d" aria-pressed="false"><span class="n">T%d</span>'
              '<span>%s</span><span class="k">%d</span></button>'%(t,t,e(TIERS[t][0]),tcounts.get(t,0)))
    nav+='<p class="navlabel second">Categories</p>'
    nav+=('<button class="cat" data-f="all" aria-pressed="true"><span class="n">··</span>'
          '<span>All types</span><span class="k">%d</span></button>'%len(E))
    for i,n in CATS:
        nav+=('<button class="cat" data-f="%d" aria-pressed="false"><span class="n">%02d</span>'
              '<span>%s</span><span class="k">%d</span></button>'%(i,i,e(n),counts.get(i,0)))

    tierblocks=""
    for t,cls,head in ((1,"a","Must know"),(2,"b","Very important"),(3,"c","Know when to use")):
        items="".join(
            '<li><a href="#%s" data-go>%s</a></li>'%(ids[name],e(label))
            for tt,rank,label,name in sorted(PRIORITY,key=lambda r:(r[0],r[1])) if tt==t)
        tierblocks+=('<div class="ptier %s"><p class="pt-h"><b>Tier %d</b> %s</p><ol>%s</ol></div>'
                     %(cls,t,e(head),items))

    qrows="".join('<a href="#%s" data-go><span class="q">%s</span><span class="d">%s</span></a>'
                  %(ids[name],e(q),e(name)) for q,name in QUESTIONS)

    panel=('<section class="priority" id="priority">'
      '<h2>The diagrams I’d prioritize for a Software Architect</h2>'
      '<p class="plede">You don’t need to memorise every notation, and you should not try to master fifty '
      'diagrams equally. These %d are the ones worth being fluent in, ranked. Everything else in this '
      'dictionary is there for the day you need it.</p>'
      '<div class="ptiers">%s</div>'
      '<div class="qwrap"><p>Or pick by the question you are trying to settle</p>'
      '<div class="qgrid">%s</div></div></section>')%(len(PRIORITY),tierblocks,qrows)

    js = """
<script>
(function(){
  var entries=[].slice.call(document.querySelectorAll('article.entry'));
  var buttons=[].slice.call(document.querySelectorAll('.cat'));
  var box=document.getElementById('q');
  var count=document.getElementById('count');
  var empty=document.getElementById('empty');
  var panel=document.getElementById('priority');
  var main=document.querySelector('main');
  var filter='all';
  function match(el){
    if(filter==='all') return true;
    if(filter==='prio') return el.dataset.prio==='1';
    if(filter.charAt(0)==='t') return el.dataset.tier===filter.charAt(1);
    return el.dataset.cat===filter;
  }
  function apply(){
    var term=(box.value||'').trim().toLowerCase();
    var shown=0;
    entries.forEach(function(el){
      var vis = match(el) && (!term || el.dataset.q.indexOf(term)>-1);
      el.hidden = !vis;
      if(vis) shown++;
    });
    count.textContent = shown + (shown===1?' type':' types');
    empty.hidden = shown>0;
    panel.hidden = !!term || !(filter==='all'||filter==='prio'||filter.charAt(0)==='t');
    main.classList.toggle('prio-view', filter==='prio');
  }
  function setFilter(f){
    filter=f;
    buttons.forEach(function(o){o.setAttribute('aria-pressed', String(o.dataset.f===f));});
    apply();
  }
  buttons.forEach(function(b){
    b.addEventListener('click',function(){
      setFilter(b.dataset.f);
      window.scrollTo({top:0,behavior:'smooth'});
    });
  });
  var timer;
  function reveal(id){
    var t=document.getElementById(id);
    if(!t) return;
    if(t.hidden){ box.value=''; setFilter('all'); }
    t.scrollIntoView({behavior:'smooth',block:'start'});
    clearTimeout(timer);
    entries.forEach(function(el){el.classList.remove('flash');});
    t.classList.add('flash');
    timer=setTimeout(function(){t.classList.remove('flash');},1600);
  }
  [].slice.call(document.querySelectorAll('[data-go]')).forEach(function(a){
    a.addEventListener('click',function(ev){
      ev.preventDefault();
      var id=a.getAttribute('href').slice(1);
      history.replaceState(null,'','#'+id);
      reveal(id);
    });
  });
  box.addEventListener('input',apply);
  apply();
  if(location.hash.length>1) reveal(location.hash.slice(1));
})();
</script>
"""

    html_out = (
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
    '<title>Architecture Diagram Dictionary</title>\n' + CSS +
    '<header class="top"><div class="topin">'
    '<h1 class="brand">Architecture <em>Diagram Dictionary</em></h1>'
    '<p class="tagline">%d types · 15 categories · pick by the question you need answered</p>'
    '<div class="search"><input id="q" type="search" placeholder="Search %d types…" '
    'aria-label="Search diagram types" autocomplete="off"><span id="count"></span></div>'
    '</div></header>'
    % (len(E), len(E))
    + DEFS +
    '<div class="shell"><nav class="cats" aria-label="Diagram categories">' + nav + '</nav>'
    '<main>'
    '<p class="intro">A working reference, not a taxonomy. Every entry answers one question — '
    '<b>choose the diagram by the question you are trying to settle</b>, then draw only what that '
    'question needs. Names vary between organisations, so each entry lists the aliases it also '
    'travels under.</p>'
    + panel
    + "".join(rows) +
    '<p class="empty" id="empty" hidden>No diagram type matches that. Try “event”, “failover”, '
    '“lineage”, or clear the search.</p>'
    '</main></div>'
    '<footer>Tier 1 · must know &nbsp;—&nbsp; Tier 2 · very important &nbsp;—&nbsp; '
    'Tier 3 · know when to use. The shortlist marks the %d types worth being fluent in first. '
    'Sample plates are drawn to one house style; they show the notation, not a real system.</footer>'
    % len(PRIORITY)
    + js)
    return html_out

check_plates()
with open(OUT,"w",encoding="utf-8") as f:
    f.write(build())
print("wrote %s (%d bytes, %d entries, %d shortlisted)"
      % (OUT, os.path.getsize(OUT), len(E), len(PRIORITY)))

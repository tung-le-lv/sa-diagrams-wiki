# -*- coding: utf-8 -*-
"""Assembles the site. Run: python build.py

One page per category and per audience, plus an overview:

    index.html                 overview: frequency panel, question table, category index
    questions.html             question -> diagram, and every type by what it answers
    pages/audience-<key>.html  every entry drawn for one audience   (7)
    pages/<category-slug>.html every entry in one category         (18)
"""
from entries import *

import os, re, json, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
SUB  = "pages"          # every page except index.html lives here
AST  = "assets"         # shared CSS and JS, written once and cached across pages


def site_url():
    """Absolute base URL, needed for canonical links, Open Graph and the sitemap.
    Derived from the git remote so it stays right after a fork; override with SITE_URL."""
    env = os.environ.get("SITE_URL")
    if env:
        return env.rstrip("/")
    try:
        r = subprocess.check_output(["git", "-C", ROOT, "remote", "get-url", "origin"],
                                    stderr=subprocess.DEVNULL).decode().strip()
        m = re.search(r"[:/]([^/:]+)/([^/]+?)(?:\.git)?$", r)
        if m:
            return "https://%s.github.io/%s" % (m.group(1), m.group(2))
    except Exception:
        pass
    return ""

SITE = site_url()

CATNAME  = {i:n for i,n,_,_ in CATS}
CATSLUG  = {i:s for i,_,s,_ in CATS}
BY_NAME  = {en["name"]: en for en in E}
# The two categories that carry a canonical-set panel. Looked up by slug so inserting a
# category ahead of them does not silently point the panel at the wrong page.
CAT_C4   = next(i for i, _n, s, _b in CATS if s == "c4-model")
CAT_UML  = next(i for i, _n, s, _b in CATS if s == "uml")

def cat_listing(i):
    """Entries shown on category i: the ones filed there, plus any that also belong,
    inserted at the position their ALSO_IN entry asks for."""
    out = [x for x in E if x["cat"] == i]
    borrowed = sorted(((pos, BY_NAME[n]) for n, lst in ALSO_IN.items()
                       for c, pos in lst if c == i), key=lambda t: t[0])
    for pos, en in borrowed:
        out.insert(min(max(pos - 1, 0), len(out)), en)
    return out
AUDNAME  = {k:l for k,l,_,_,_ in AUDIENCES}
AUDPLUR  = {k:pl for k,_,pl,_,_ in AUDIENCES}
AUDSLUG  = {k:"audience-"+k for k,_,_,_,_ in AUDIENCES}
AUDKEYS  = [k for k,_,_,_,_ in AUDIENCES]
# extra words people actually type when they mean an audience
AUDSYN   = {"architect":"architect solution architect design review",
            "developer":"developer engineer engineering dev implementation",
            "operations":"operations ops sre platform on-call oncall devops runbook",
            "security":"security appsec threat audit compliance ciso",
            "data":"data analytics analyst data engineer steward bi",
            "business":"business ba business analyst product domain expert stakeholder",
            "management":"management executive exec leadership portfolio budget cto sponsor"}

def slug(s):
    return re.sub(r"-+","-",re.sub(r"[^a-z0-9]+","-",s.lower())).strip("-")

def anchor(name):
    return "d-"+slug(name)

def P(target, root):
    """Link to a logical page from index.html (root=True) or from inside SUB."""
    if target == "index":
        return "index.html" if root else "../index.html"
    return ("%s/%s.html" % (SUB, target)) if root else ("%s.html" % target)

def A(fname, root):
    """Link to a shared asset from index.html (root=True) or from inside SUB."""
    return ("%s/%s" % (AST, fname)) if root else ("../%s/%s" % (AST, fname))

def abs_url(fname, root):
    """Absolute URL of a built page, for canonical / og:url / the sitemap."""
    if not SITE:
        return ""
    return "%s/%s" % (SITE, fname if root else "%s/%s" % (SUB, fname))

def url(en, root=False):
    """An entry's canonical home is its category page."""
    return P(CATSLUG[en["cat"]], root) + "#" + anchor(en["name"])

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

def check_related():
    """A see-also pointing at a name that no longer exists is a dead link on 30 pages."""
    names = {en["name"] for en in E}
    bad = ["RELATED key is not an entry: " + k for k in RELATED if k not in names]
    bad += ["%s -> %s does not exist" % (k, n)
            for k, v in RELATED.items() for n in v if n not in names]
    bad += ["%s links to itself" % k for k, v in RELATED.items() if k in v]
    if bad:
        raise SystemExit("See-also links:\n  " + "\n  ".join(sorted(bad)))

def check_frequency():
    """The overview panel names diagrams in prose; a rename must not leave it lying."""
    names = {en["name"] for en in E}
    slugs = {s for _i, _n, s, _b in CATS}
    bad = []
    for _grp, _sub, items in FREQUENCY:
        for label, target, _gloss in items:
            for t in (target if isinstance(target, list) else [target]):
                if not t:
                    continue
                if t.startswith("cat:"):
                    if t[4:] not in slugs: bad.append("FREQUENCY: no category %r" % t[4:])
                elif t not in names:
                    bad.append("FREQUENCY: no entry %r" % t)
    if bad:
        raise SystemExit("Overview frequency panel:\n  " + "\n  ".join(sorted(set(bad))))

def audience_entries(k):
    """Entries drawn primarily for audience k, in rank order where one is declared.
    sorted() is stable, so anything unranked keeps declaration order at the end."""
    ents = [x for x in E if AUDIENCE[x["name"]][0] == k]
    rank = {n: i for i, n in enumerate(AUDIENCE_ORDER.get(k, []))}
    return sorted(ents, key=lambda x: rank.get(x["name"], len(rank)))

def check_audience_order():
    """A rank naming an entry that is not primary for that audience silently does
    nothing, which is the worst kind of wrong. Unranked entries are only a warning."""
    bad, warn = [], []
    for k, names in AUDIENCE_ORDER.items():
        if k not in {a for a, _, _, _, _ in AUDIENCES}:
            bad.append("AUDIENCE_ORDER: no audience %r" % k); continue
        primary = {x["name"] for x in E if AUDIENCE[x["name"]][0] == k}
        bad += ["AUDIENCE_ORDER[%r]: %r is not primary for it" % (k, n)
                for n in names if n not in primary]
        bad += ["AUDIENCE_ORDER[%r]: %r listed twice" % (k, n)
                for n in sorted(set(names)) if names.count(n) > 1]
        warn += ["%s: %s is unranked, so it lands at the end" % (k, n)
                 for n in sorted(primary - set(names))]
    if bad:
        raise SystemExit("Audience rank order:\n  " + "\n  ".join(sorted(bad)))
    return warn

def check_audiences():
    """Every entry must declare an audience, and only ones that exist."""
    valid = {k for k, _, _, _, _ in AUDIENCES}
    names = {en["name"] for en in E}
    missing = sorted(names - set(AUDIENCE))
    unknown = sorted(set(AUDIENCE) - names)
    badkey = sorted(k for k, v in AUDIENCE.items()
                    if v[0] not in valid or any(x not in valid for x in v[1]))
    problems = ([("untagged entry: " + m) for m in missing]
                + [("AUDIENCE key matches no entry: " + u) for u in unknown]
                + [("unknown audience on: " + b) for b in badkey])
    if problems:
        raise SystemExit("Audience tagging:\n  " + "\n  ".join(problems))

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
# The font links stay in the head of every page; the stylesheet itself is written
# once to assets/site.css so the browser downloads and caches it a single time.
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700'
         '&family=IBM+Plex+Sans+Condensed:wght@600;700&display=swap">\n')

CSS = """
:root{
  --paper:#EDEFF1; --surface:#F9FAFB; --ink:#14181B; --ink2:#3D464E; --muted:#66707A;
  --line:#D4D9DE; --hair:#E4E8EB; --accent:#1F5F8B;
  --accent-ink:#134568; --accent-soft:#E1EBF3; --flag:#9C4034; --flag-soft:#F4E7E4;
  --amb:#7A5C1F; --amb-soft:#F4EEDF; --grn:#33604A; --grn-soft:#E4EEE8;
  --plate:#FFFFFF; --plate-line:#DEE3E7; --shadow:0 1px 2px rgba(20,30,40,.06),0 8px 24px -14px rgba(20,30,40,.28);
  --hdr:61px;   /* height of the sticky header; site.js measures the real one */
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
/* the shell widens on pages that carry a TOC, so the header has to widen with it or
   the brand stops lining up with the nav underneath it */
body.wide .topin{max-width:1400px}
@media (max-width:1300px){body.wide .topin{max-width:1180px}}
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
/* pages that list entries get a third column: what is on this page, and where you are
   in it. The shell widens rather than squeezing the plates, which have a min-width. */
.shell.has-toc{max-width:1400px;grid-template-columns:224px minmax(0,1fr) 208px;gap:40px}

/* Pinned directly under the header and exactly one viewport tall, so it never moves
   while the main column scrolls. `height` rather than `max-height`: a max-height only
   engages once the content is long enough, which is what makes a sticky column drift. */
aside.toc{position:sticky;top:var(--hdr);align-self:start;height:calc(100vh - var(--hdr));
  overflow-y:auto;overscroll-behavior:contain;padding:26px 0 24px;scrollbar-width:thin}
.toclabel{font-family:var(--mono);font-size:10px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--muted);margin:0 0 10px 10px}
aside.toc ol{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:1px}
aside.toc a{display:block;text-decoration:none;color:var(--ink2);
  font-size:12.4px;line-height:1.35;padding:4px 10px;border-left:2px solid transparent;
  border-radius:0 3px 3px 0}
aside.toc a:hover{color:var(--ink);background:var(--hair)}
aside.toc a.on{color:var(--accent-ink);border-left-color:var(--accent);
  background:var(--accent-soft);font-weight:600}
aside.toc a.sec{font-family:var(--disp);font-weight:600;margin-top:9px;padding-top:10px;
  border-top:1px solid var(--hair)}
@media (max-width:1300px){
  .shell.has-toc{max-width:1180px;grid-template-columns:224px minmax(0,1fr);gap:44px}
  aside.toc{display:none}
}

nav.cats{position:sticky;top:var(--hdr);align-self:start;height:calc(100vh - var(--hdr));
  overflow-y:auto;overscroll-behavior:contain;
  padding:26px 0 24px;display:flex;flex-direction:column;gap:2px;scrollbar-width:thin}
.navlabel{font-family:var(--mono);font-size:10px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--muted);margin:0 0 10px 8px}
.navlabel.second{margin-top:20px;padding-top:16px;border-top:1px solid var(--hair)}
.cat{display:flex;gap:9px;align-items:baseline;font-family:var(--disp);font-size:13.5px;
  font-weight:600;color:var(--ink2);text-decoration:none;border-left:2px solid transparent;
  padding:5px 8px;line-height:1.3;border-radius:0 3px 3px 0}
.cat:hover{color:var(--ink);background:var(--hair)}
.cat[aria-current="page"]{color:var(--accent-ink);border-left-color:var(--accent);
  background:var(--accent-soft);font-weight:700}
.cat .k{font-family:var(--mono);font-size:10px;color:var(--muted);margin-left:auto}

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
.sect{font-family:var(--mono);font-size:10px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--muted);margin:20px 0 2px}


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

.freq{background:var(--surface);border:1px solid var(--line);border-radius:4px;
  box-shadow:var(--shadow);overflow:hidden}
.freq p.flead{margin:0;padding:14px 20px;font-size:13.4px;color:var(--ink2);line-height:1.55;
  border-bottom:1px solid var(--line);background:var(--paper)}
.freq section{padding:15px 20px 17px;border-top:1px solid var(--hair)}
.freq section:first-of-type{border-top:0}
.freq h3{font-family:var(--disp);font-weight:700;font-size:15px;margin:0;color:var(--ink);
  line-height:1.25}
.freq .gsub{margin:2px 0 11px;font-size:12.6px;color:var(--muted);max-width:80ch;line-height:1.5}
.freq ul{list-style:none;margin:0;padding:0;display:grid;
  grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:0 24px}
.freq li{padding:6px 0;border-top:1px solid var(--hair);font-size:13px;line-height:1.5;
  color:var(--ink2)}
.freq li a{font-family:var(--disp);font-weight:600;font-size:13.4px;text-decoration:none;
  color:var(--accent-ink)}
.freq li a:hover{text-decoration:underline}
.freq li b.off{font-family:var(--disp);font-weight:600;font-size:13.4px;color:var(--ink2)}
.freq li .d{color:var(--muted);font-size:12.5px}
.freq p.bar{margin:0;padding:14px 20px;background:var(--accent-soft);
  border-top:1px solid var(--line);font-size:13.4px;color:var(--ink2);line-height:1.55}
.freq p.bar b{color:var(--accent-ink);font-weight:700}

article.entry{background:var(--surface);border:1px solid var(--line);border-radius:4px;
  padding:24px 26px 26px;box-shadow:var(--shadow);scroll-margin-top:calc(var(--hdr) + 16px)}
article.entry.flash{border-color:var(--accent);box-shadow:0 0 0 2px var(--accent-soft),var(--shadow)}
.ehead{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;margin-bottom:3px}
h2.name{font-family:var(--disp);font-weight:700;font-size:23px;letter-spacing:.004em;margin:0;
  text-wrap:balance;line-height:1.15}
.catline{font-family:var(--mono);font-size:10.5px;letter-spacing:.09em;text-transform:uppercase;
  color:var(--muted);margin:0 0 12px}
.catline a{color:var(--muted);text-decoration:none}
.catline a:hover{color:var(--accent-ink)}
.catline .shown{margin-left:8px;padding:1px 6px;border:1px solid var(--line);border-radius:2px;
  color:var(--muted);letter-spacing:.06em}
p.defn{margin:0 0 18px;max-width:70ch;font-size:15px;color:var(--ink2)}
ul.alias{list-style:none;display:flex;flex-wrap:wrap;gap:6px;margin:0 0 20px;padding:0}
ul.alias li{font-family:var(--mono);font-size:10px;color:var(--muted);border:1px solid var(--hair);
  background:var(--paper);border-radius:2px;padding:2px 7px}
ul.alias li.lab{border-color:transparent;background:none;letter-spacing:.08em;text-transform:uppercase}
ul.alias.aud{margin-bottom:10px}
ul.alias.aud li{border-color:var(--line);padding:0}
ul.alias.aud li.lab{border-color:transparent;padding:2px 7px}
ul.alias.aud a{display:block;padding:2px 8px;text-decoration:none;color:var(--ink2);
  font-family:var(--sans);font-size:11px;font-weight:500}
ul.alias.aud a:hover{color:var(--accent-ink);background:var(--accent-soft)}
ul.alias.aud li.pri{border-color:var(--accent);background:var(--accent-soft)}
ul.alias.aud li.pri a{color:var(--accent-ink);font-weight:700}
a.card.acard{border-left:3px solid var(--accent)}
.canon{background:var(--surface);border:1px solid var(--line);border-radius:4px;
  padding:18px 20px 16px;box-shadow:var(--shadow)}
.canon>h2{font-family:var(--disp);font-weight:700;font-size:17px;margin:0 0 4px}
.canon>p{margin:0 0 14px;font-size:13.2px;color:var(--muted);max-width:74ch}
.canoncols{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px}
.canoncols h3{font-family:var(--mono);font-size:9.5px;letter-spacing:.11em;text-transform:uppercase;
  color:var(--muted);margin:0 0 8px;font-weight:600}
.canoncols ol{margin:0;padding:0;list-style:none;counter-reset:u}
.canoncols li{counter-increment:u;margin-bottom:1px}
.canoncols a{display:flex;gap:8px;align-items:baseline;text-decoration:none;color:var(--ink2);
  font-size:13.2px;padding:3px 6px;border-radius:3px}
.canoncols a::before{content:counter(u);font-family:var(--mono);font-size:9.5px;
  color:var(--muted);min-width:12px;text-align:right}
.canoncols a:hover{background:var(--accent-soft);color:var(--accent-ink)}
.canoncols .away{font-family:var(--mono);font-size:9.5px;color:var(--muted);margin-left:auto;
  white-space:nowrap}
a.card.acard .who{display:block;font-size:11.5px;color:var(--ink2);margin-top:5px}

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
ol.listing a.two{grid-template-columns:minmax(0,1fr) minmax(0,1.35fr)}
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
  .shell,.shell.has-toc{grid-template-columns:1fr;gap:0;padding:0 18px 60px}
  nav.cats{position:static;height:auto;max-height:none;overscroll-behavior:auto;
    flex-direction:row;overflow-x:auto;padding:18px 0 4px;
    gap:6px;border-bottom:1px solid var(--line);align-items:center}
  .navlabel{display:none}
  .cat{white-space:nowrap;border-left:0;border-bottom:2px solid transparent;border-radius:3px;padding:6px 10px}
  .cat[aria-current="page"]{border-left:0;border-bottom-color:var(--accent)}
  .cat .k{display:none}
  article.entry{padding:20px 18px}
  dl.facts{grid-template-columns:1fr}
  .qgrid{grid-template-columns:1fr}
  ol.listing a{grid-template-columns:26px 1fr;gap:6px 10px}
  ol.listing a.two{grid-template-columns:1fr}
  ol.listing .an{grid-column:2}
  ol.listing a.two .an{grid-column:1}
  .pager{flex-direction:column}
  .pager .nx{text-align:left}
  h1.ptitle{font-size:24px}
  .search{margin-left:0;width:100%}
  .search input{flex:1;width:auto}
  h2.name{font-size:20px}
}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}

ul.rel{list-style:none;display:flex;flex-wrap:wrap;gap:6px;margin:14px 0 0;padding:0;
  align-items:baseline}
ul.rel li.lab{font-family:var(--mono);font-size:10px;letter-spacing:.08em;text-transform:uppercase;
  color:var(--muted)}
ul.rel a{font-family:var(--disp);font-size:11.5px;font-weight:600;text-decoration:none;
  color:var(--ink2);border:1px solid var(--line);border-radius:2px;padding:2px 8px;display:block}
ul.rel a:hover{color:var(--accent-ink);border-color:var(--accent);background:var(--accent-soft)}

/* This is a reference. People print it and save it as PDF, so make that page work. */
@media print{
  :root{--paper:#fff;--surface:#fff;--ink:#000;--ink2:#222;--muted:#555;--line:#bbb;--hair:#ddd;
        --accent-soft:#fff;--shadow:none}
  header.top,nav.cats,aside.toc,.search,#results,.pager,footer{display:none!important}
  .shell{display:block;max-width:none;padding:0}
  main{padding:0}
  article.entry{break-inside:avoid;page-break-inside:avoid;border:1px solid #bbb;
    box-shadow:none;margin-bottom:14px}
  .freq section,.freq p.bar{break-inside:avoid;page-break-inside:avoid}
  figure.fig,.sheet{break-inside:avoid;page-break-inside:avoid;overflow:visible}
  svg.plate{min-width:0}
  dl.facts{break-inside:avoid;page-break-inside:avoid}
  a{color:#000;text-decoration:none}
  h1.ptitle{font-size:22px}
  @page{margin:14mm}
}
"""

# ------------------------------------------------------------------ fragments
def render_entry(en, root=False, home=None):
    ap, asec = AUDIENCE[en["name"]]
    aud = ('<ul class="alias aud"><li class="lab">audience</li>'
           + '<li class="pri"><a href="%s">%s</a></li>' % (P(AUDSLUG[ap], root), e(AUDNAME[ap]))
           + "".join('<li><a href="%s">%s</a></li>' % (P(AUDSLUG[k], root), e(AUDNAME[k]))
                     for k in asec)
           + '</ul>')
    alias = ""
    if en["alias"]:
        alias = ('<ul class="alias"><li class="lab">also called</li>'
                 + "".join('<li>%s</li>' % e(a) for a in en["alias"]) + '</ul>')
    # See also — the relationship between two entries is the thing a dictionary
    # cannot express with aliases alone, and it is how people actually navigate.
    rel = ""
    kin = [n for n in RELATED.get(en["name"], []) if n in BY_NAME]
    if kin:
        rel = ('<ul class="rel"><li class="lab">see also</li>'
               + "".join('<li><a href="%s">%s</a></li>' % (url(BY_NAME[n], root), e(n))
                         for n in kin) + '</ul>')
    # give every plate an accessible name by pointing it at its own caption
    capid = "cap-" + anchor(en["name"])
    plate = en["svg"].replace('<svg class="plate"',
                              '<svg class="plate" aria-labelledby="%s"' % capid, 1)
    return (
    '<article class="entry" id="%s">'
    '<div class="ehead"><h2 class="name">%s</h2></div>'
    '<p class="catline"><a href="%s">%s</a>%s</p>'
    '<p class="defn">%s</p>%s%s'
    '<figure class="fig"><div class="sheet">%s</div><figcaption id="%s">%s</figcaption></figure>'
    '<dl class="facts">'
    '<div><dt>Answers</dt><dd>%s</dd></div>'
    '<div><dt>Reach for it when</dt><dd>%s</dd></div>'
    '<div><dt>It must show</dt><dd>%s</dd></div>'
    '<div class="fail"><dt>Common failure</dt><dd>%s</dd></div>'
    '</dl>%s</article>'
    % (anchor(en["name"]), e(en["name"]),
       P(CATSLUG[en["cat"]], root), e(CATNAME[en["cat"]]),
       ("" if home is None or home == en["cat"] else ' <span class="shown">also shown here</span>'),
       e(en["defn"]), aud, alias,
       plate, capid, e(en["cap"]), e(en["answers"]), e(en["when"]), e(en["must"]), e(en["fail"]), rel))

def nav(active, root):
    n = ('<a class="cat" href="%s"%s><span>Overview</span></a>'
         % (P("index", root), ' aria-current="page"' if active == "index" else ""))
    n += ('<a class="cat" href="%s"%s>'
          '<span>Question → diagram</span><span class="k">%d</span></a>'
          % (P("questions", root),
             ' aria-current="page"' if active == "questions" else "", len(QUESTIONS)))
    n += '<p class="navlabel second">By audience</p>'
    for k, label, _pl, _who, _want in AUDIENCES:
        cnt = sum(1 for x in E if AUDIENCE[x["name"]][0] == k)
        n += ('<a class="cat" href="%s"%s>'
              '<span>%s</span><span class="k">%d</span></a>'
              % (P(AUDSLUG[k], root),
                 ' aria-current="page"' if active == AUDSLUG[k] else "", e(label), cnt))
    n += '<p class="navlabel second">Categories</p>'
    for i, name, cslug, _ in CATS:
        cnt = len(cat_listing(i))
        n += ('<a class="cat" href="%s"%s>'
              '<span>%s</span><span class="k">%d</span></a>'
              % (P(cslug, root), ' aria-current="page"' if active == cslug else "", e(name), cnt))
    return n

def frequency_panel(root=True):
    """The overview's fourth axis: not what a diagram is or who it is for, but how often
    you will actually reach for it. Every name is a link, so it doubles as a shortlist."""
    def href(target, label):
        if target.startswith("cat:"):
            return P(target[4:], root)
        return url(BY_NAME[target], root)
    out = ""
    for grp, sub, items in FREQUENCY:
        rows = ""
        for label, target, gloss in items:
            if isinstance(target, list):
                head = " · ".join('<a href="%s">%s</a>' % (href(t, t), e(t)) for t in target)
            elif target:
                head = '<a href="%s">%s</a>' % (href(target, label), e(label or target))
            else:
                head = '<b class="off">%s</b>' % e(label)
            rows += '<li>%s <span class="d">— %s</span></li>' % (head, e(gloss))
        out += ('<section><h3>%s</h3><p class="gsub">%s</p><ul>%s</ul></section>'
                % (e(grp), e(sub), rows))
    return ('<div class="freq"><p class="flead">%s</p>%s'
            '<p class="bar"><b>A practical bar.</b> %s</p></div>'
            % (e(FREQUENCY_LEAD), out, e(FREQUENCY_BAR)))

def toc(ents, extra=None):
    """What is on this page, in page order — the right-hand column. `extra` is for the
    sections that are not entries (the UML canon panel, the audience 'also read' list)."""
    if not ents and not extra:
        return ""
    rows = "".join(
        '<li><a href="#%s">%s</a></li>'
        % (anchor(en["name"]), e(en["name"])) for en in ents)
    rows += "".join('<li><a class="sec" href="#%s">%s</a></li>' % (i, e(t))
                    for i, t in (extra or []))
    return ('<aside class="toc" aria-label="On this page"><p class="toclabel">On this page</p>'
            '<ol>%s</ol></aside>' % rows)

def pager(prev, nxt, root=False):
    if not prev and not nxt: return ""
    out = '<div class="pager">'
    out += (('<a href="%s"><span>Previous</span><b>%s</b></a>' % (P(prev[0], root), e(prev[1])))
            if prev else '<span class="sp"></span>')
    out += (('<a class="nx" href="%s"><span>Next</span><b>%s</b></a>' % (P(nxt[0], root), e(nxt[1])))
            if nxt else '<span class="sp"></span>')
    return out + '</div>'

def search_index():
  """One index for the whole site, written once to assets/. URLs are stored in their
  root-relative form and prefixed at runtime with window.BASE, so the same file serves
  index.html and everything under pages/.

  The searchable blob carries the prose too — `defn`, `must` and `fail` are where the
  words people actually type live (“idempotency”, “grain”, “compensating action”)."""
  return json.dumps(
    [[en["name"], url(en, True), CATNAME[en["cat"]], en["answers"],
      AUDNAME[AUDIENCE[en["name"]][0]],
      " ".join([en["name"], CATNAME[en["cat"]], en["answers"], en["when"],
                en["defn"], en["must"], en["fail"], en["cap"]] + en["alias"]
               + [AUDSYN[a] for a in [AUDIENCE[en["name"]][0]] + AUDIENCE[en["name"]][1]]).lower()]
     for en in E], ensure_ascii=False, separators=(",", ":"))

SITE_JS = """
/* --- pin the sidebars under the header, whatever height it renders at ---- */
(function(){
  var h=document.querySelector('header.top');
  if(!h) return;
  function set(){
    document.documentElement.style.setProperty('--hdr', h.offsetHeight+'px');
  }
  set();
  /* the header wraps on narrow widths and reflows once the webfont lands */
  window.addEventListener('resize', set, {passive:true});
  if(document.fonts && document.fonts.ready) document.fonts.ready.then(set);
})();

/* --- table of contents: highlight where you are on the page ------------- */
(function(){
  var toc=document.querySelector('aside.toc');
  if(!toc) return;
  var arts=[].slice.call(document.querySelectorAll('article.entry'));
  if(!arts.length) return;
  var links={};
  [].forEach.call(toc.querySelectorAll('a[href^="#"]'),function(a){
    links[decodeURIComponent(a.getAttribute('href').slice(1))]=a;
  });
  var cur=null;
  function mark(id){
    if(id===cur) return;
    if(cur&&links[cur]) links[cur].classList.remove('on');
    cur=id;
    var a=links[id];
    if(!a) return;
    a.classList.add('on');
    /* keep the active row visible inside the TOC's own scroll box */
    var t=toc.getBoundingClientRect(), r=a.getBoundingClientRect();
    if(r.top<t.top||r.bottom>t.bottom) a.scrollIntoView({block:'nearest'});
  }
  /* the last entry whose top has passed under the sticky header wins */
  function pick(){
    var hdr=(document.querySelector('header.top')||{offsetHeight:61}).offsetHeight+18;
    var best=arts[0].id, y=-1e9;
    for(var i=0;i<arts.length;i++){
      var t=arts[i].getBoundingClientRect().top-hdr;
      if(t<=0 && t>y){ y=t; best=arts[i].id; }
    }
    mark(best);
  }
  var queued=false;
  window.addEventListener('scroll',function(){
    if(queued) return;
    queued=true;
    requestAnimationFrame(function(){ queued=false; pick(); });
  },{passive:true});
  window.addEventListener('resize',pick,{passive:true});
  pick();
})();

/* --- search ------------------------------------------------------------- */
(function(){
  var box=document.getElementById('q'), count=document.getElementById('count'),
      res=document.getElementById('results'), body=document.getElementById('pagebody'),
      toc=document.querySelector('aside.toc'), base=window.BASE||'';
  function esc(s){return s.replace(/[&<>"]/g,function(c){
    return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
  function run(){
    var t=(box.value||'').trim().toLowerCase();
    if(!t){ res.style.display='none'; body.style.display=''; count.textContent='';
            if(toc) toc.style.display=''; return; }
    /* results replace the page, so the page's contents list would be lying */
    if(toc) toc.style.display='none';
    /* every word must match, so "kafka ordering" narrows instead of finding nothing */
    var terms=t.split(/\\s+/).filter(Boolean);
    var hits=window.IDX.filter(function(r){
      return terms.every(function(w){return r[5].indexOf(w)>-1;});
    });
    res.innerHTML = hits.length
      ? hits.map(function(r){
          return '<a href="'+base+r[1]+'"><span class="rn">'+esc(r[0])+'</span>'
               + '<span class="rm">'+esc(r[2])+' \\u00b7 for '+esc(r[4])+'</span>'
               + '<span class="ra">'+esc(r[3])+'</span></a>';}).join('')
      : '<p class="none">No diagram type matches every word of that. Try \\u201cevent\\u201d, '
        + '\\u201cfailover\\u201d, \\u201ctenancy\\u201d or \\u201clineage\\u201d.</p>';
    res.style.display='flex'; body.style.display='none';
    count.textContent = hits.length + (hits.length===1?' match':' matches');
  }
  if(box){ box.addEventListener('input', run); if(box.value) run(); }
  var t;
  function flash(){
    if(location.hash.length<2) return;
    var el=document.getElementById(decodeURIComponent(location.hash.slice(1)));
    if(!el || el.className.indexOf('entry')<0) return;
    clearTimeout(t); el.classList.add('flash');
    t=setTimeout(function(){el.classList.remove('flash');},1600);
  }
  window.addEventListener('hashchange', flash); flash();
})();
"""

def write_assets():
    """CSS, the search index and the search script, written once instead of inlined
    into all 30 pages. Roughly halves the built site and lets the browser cache them."""
    d = os.path.join(ROOT, AST)
    os.makedirs(d, exist_ok=True)
    out = {}
    for fname, text in (("site.css", CSS),
                        ("search-index.js", "window.IDX=%s;\n" % search_index()),
                        ("site.js", SITE_JS)):
        with open(os.path.join(d, fname), "w", encoding="utf-8") as f:
            f.write(text)
        out[fname] = len(text.encode("utf-8"))
    return out

BUILT = []      # (fname, root) of every page written, for the sitemap

def page(fname, title, desc, active, body, root=False, aside=""):
    canon = abs_url(fname, root)
    social = ('<meta property="og:type" content="website">\n'
              '<meta property="og:site_name" content="Software Architect Diagram Dictionary">\n'
              '<meta property="og:title" content="%s">\n'
              '<meta property="og:description" content="%s">\n'
              '<meta name="twitter:card" content="summary">\n' % (e(title), e(desc)))
    if canon:
        social += ('<link rel="canonical" href="%s">\n'
                   '<meta property="og:url" content="%s">\n' % (e(canon), e(canon)))
    html = ('<!doctype html>\n<html lang="en">\n<head>\n'
            '<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
            '<meta name="description" content="%s">\n'
            '<title>%s</title>\n' % (e(desc), e(title))
        + social
        + FONTS
        + '<link rel="stylesheet" href="%s">\n' % A("site.css", root)
        + ('</head>\n<body%s>\n' % (' class="wide"' if aside else ""))
        + ('<header class="top"><div class="topin">'
           '<h1 class="brand"><a href="%s">Software Architect <em>Diagram Dictionary</em></a></h1>'
           '<p class="tagline">%d types · %d categories</p>'
           '<div class="search"><input id="q" type="search" placeholder="Search all %d types…" '
           'aria-label="Search diagram types" autocomplete="off"><span id="count"></span></div>'
           '</div></header>' % (P("index", root), len(E), len(CATS), len(E)))
        + DEFS
        + ('<div class="shell%s"><nav class="cats" aria-label="Sections">' % (" has-toc" if aside else ""))
        + nav(active, root) + '</nav>'
          '<main><div id="results"></div><div id="pagebody">' + body + '</div></main>'
        + aside + '</div>'
        + ('<footer>%d diagram types across %d categories. The <a href="%s">overview</a> groups '
           'them by how often you will actually draw one; the <a href="%s">question page</a> '
           'starts from what you are trying to settle. Sample plates are drawn to one house '
           'style; they show the notation, not a real system.</footer>'
           % (len(E), len(CATS), P("index", root), P("questions", root)))
        + '<script>window.BASE=%s;</script>\n' % json.dumps("" if root else "../")
        + '<script src="%s" defer></script>\n' % A("search-index.js", root)
        + '<script src="%s" defer></script>\n' % A("site.js", root)
        + '</body>\n</html>\n')
    path = os.path.join(ROOT, fname) if root else os.path.join(ROOT, SUB, fname)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    BUILT.append((fname, root))
    return len(html)


def write_sitemap():
    """Search engines need absolute URLs, so this only makes sense once SITE is known."""
    if not SITE:
        return None
    urls = "".join("  <url><loc>%s</loc></url>\n" % e(abs_url(f, r)) for f, r in BUILT)
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % urls)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % SITE)
    return len(BUILT)

# ---------------------------------------------------------------------- pages
def build():
    written = []

    # overview -------------------------------------------------------------
    ccards = ""
    for i, name, cslug, blurb in CATS:
        cnt = len(cat_listing(i))
        ccards += ('<a class="card" href="%s"><span class="cn">%02d</span><h3>%s</h3>'
                   '<p>%s</p><span class="k">%d types →</span></a>'
                   % (P(cslug, True), i, e(name), e(blurb), cnt))
    acards = ""
    for k, label, plural, who, want in AUDIENCES:
        cnt = sum(1 for x in E if AUDIENCE[x["name"]][0] == k)
        acards += ('<a class="card acard" href="%s"><span class="cn">Audience</span><h3>%s</h3>'
                   '<span class="who">%s</span><span class="k">%d types →</span></a>'
                   % (P(AUDSLUG[k], True), e(label), e(who), cnt))
    qrows = "".join('<a href="%s"><span class="q">%s</span><span class="d">%s</span></a>'
                    % (url(BY_NAME[n], True), e(q), e(n)) for q, n in QUESTIONS)
    body = ('<div class="phead"><h1 class="ptitle">A software architect’s diagram dictionary</h1>'
            '<p class="pblurb">%d diagram types across %d categories — each with a sample plate, the '
            'question it answers, when to reach for it, what it must show, and the mistake that shows '
            'up in review. <b>Choose the diagram by the question you are trying to settle</b>, then '
            'draw only what that question needs.</p></div>'
            '<p class="sect">Start here · how often a software architect actually draws each one</p>%s'
            '<p class="sect">Or start from the question you need to settle</p>'
            '<div class="qwrap"><p>Question → diagram</p><div class="qgrid">%s</div></div>'
            '<p class="sect">Or by who you are drawing it for</p><div class="grid">%s</div>'
            '<p class="sect">Browse by category</p><div class="grid">%s</div>'
            % (len(E), len(CATS), frequency_panel(True), qrows, acards, ccards))
    written.append(("index.html", page(
        "index.html", "Software Architect Diagram Dictionary",
        "%d software architecture diagram types across %d categories — each with a sample plate, "
        "the question it answers, and the mistake that shows up in review." % (len(E), len(CATS)),
        "index", body, root=True)))

    # question -> diagram, as its own page ---------------------------------
    # It is the best entry point in the whole site and it used to exist only
    # halfway down index.html.
    qrows2 = "".join('<a href="%s"><span class="q">%s</span><span class="d">%s</span></a>'
                     % (url(BY_NAME[n]), e(q), e(n)) for q, n in QUESTIONS)
    byq = {}
    for en in E:
        byq.setdefault(CATNAME[en["cat"]], []).append(en)
    alist = "".join(
        '<li><a class="two" href="%s"><span class="nm">%s</span>'
        '<span class="an">%s</span></a></li>'
        % (url(en), e(en["name"]), e(en["answers"]))
        for en in sorted(E, key=lambda x: x["answers"].lower()))
    body = ('<div class="phead"><p class="crumb"><a href="../index.html">Overview</a> · '
            'Question → diagram</p><h1 class="ptitle">Start from the question</h1>'
            '<p class="pblurb">Choosing by the name of a diagram is how you end up drawing the '
            'wrong one. <b>Choose by the question you are trying to settle</b>, then draw only '
            'what that question needs — and stop.</p></div>'
            '<div class="qwrap"><p>The %d questions that come up most</p>'
            '<div class="qgrid">%s</div></div>'
            '<p class="sect">Every type, by the question it answers</p>'
            '<ol class="listing">%s</ol>' % (len(QUESTIONS), qrows2, alist))
    written.append(("questions.html", page(
        "questions.html", "Question → diagram · Software Architect Diagram Dictionary",
        "Pick a software architecture diagram by the question you need to settle, not by its "
        "name. %d types, each with the question it answers." % len(E),
        "questions", body)))

    # one page per audience ------------------------------------------------
    for pos, (k, label, plural, who, want) in enumerate(AUDIENCES):
        ents = audience_entries(k)
        also = [x for x in E if k in AUDIENCE[x["name"]][1]]
        ranked = k in AUDIENCE_ORDER
        prev = ((AUDSLUG[AUDIENCES[pos-1][0]], "For %s" % AUDIENCES[pos-1][1].lower())
                if pos > 0 else ("index", "Overview"))
        nxt = ((AUDSLUG[AUDIENCES[pos+1][0]], "For %s" % AUDIENCES[pos+1][1].lower())
               if pos < len(AUDIENCES)-1 else None)
        secondary = ""
        if also:
            secondary = ('<p class="sect" id="also">Also useful to %s</p><ol class="listing">%s</ol>'
                         % (e(plural), "".join(
                '<li><a href="%s"><span class="st">%s</span><span class="nm">%s</span>'
                '<span class="an">%s</span></a></li>'
                % (url(x), AUDNAME[AUDIENCE[x["name"]][0]][:3].upper(), e(x["name"]), e(x["answers"]))
                for x in also)))
        body = ('<div class="phead"><p class="crumb"><a href="../index.html">Overview</a> · '
                'Audience</p><h1 class="ptitle">Drawn for %s</h1>'
                '<p class="pblurb"><b>%s.</b> %s</p>'
                '<p class="pmeta">%d types drawn primarily for this audience%s · %d more they also '
                'read</p></div>' % (e(plural), e(who), e(want), len(ents),
                                    ", ranked by how often you will reach for one" if ranked else "",
                                    len(also)))
        body += "".join(render_entry(en, root=False) for en in ents)
        body += secondary
        body += pager(prev, nxt, root=False)
        written.append((AUDSLUG[k] + ".html", page(
            AUDSLUG[k] + ".html", "For %s · Software Architect Diagram Dictionary" % plural,
            "Architecture diagram types drawn primarily for %s. %s" % (plural, who),
            AUDSLUG[k], body,
            aside=toc(ents, [("also", "Also useful to %s" % plural)] if also else None))))

    # one page per category ------------------------------------------------
    for pos, (i, name, cslug, blurb) in enumerate(CATS):
        ents = cat_listing(i)
        prev = ((CATS[pos-1][2], "%02d · %s" % (CATS[pos-1][0], CATS[pos-1][1])) if pos > 0
                else ("index", "Overview"))
        nxt = ((CATS[pos+1][2], "%02d · %s" % (CATS[pos+1][0], CATS[pos+1][1]))
               if pos < len(CATS) - 1 else None)
        nborrow = sum(1 for x in ents if x["cat"] != i)
        bits = []
        if nborrow: bits.append("%d filed here, %d also shown" % (len(ents) - nborrow, nborrow))
        bits.append("ordered by how often it earns its place")
        mix = " · ".join(bits)
        body = ('<div class="phead"><p class="crumb"><a href="../index.html">Overview</a> · '
                'Category %02d</p><h1 class="ptitle">%s</h1><p class="pblurb">%s</p>'
                '<p class="pmeta">%d types · %s</p></div>'
                % (i, e(name), e(blurb), len(ents), e(mix)))
        def canon_cols(groups, home):
            out = ""
            for group, members in groups:
                items = ""
                for n in members:
                    en = BY_NAME[n]
                    away = ("" if en["cat"] == home
                            else '<span class="away">filed in %s</span>' % e(CATNAME[en["cat"]]))
                    items += '<li><a href="%s">%s%s</a></li>' % (url(en), e(n), away)
                out += '<div><h3>%s · %d</h3><ol>%s</ol></div>' % (e(group), len(members), items)
            return out

        if i == CAT_C4:
            body += ('<div class="canon" id="c4set"><h2>The C4 model</h2>'
                     '<p>Four levels of zoom over one system, plus a supplementary set. All seven '
                     'are on this page. Three are <em>filed</em> elsewhere — you reach for a '
                     'sequence or deployment diagram by the job it does rather than because C4 '
                     'names it — so their entries live in those categories and are shown here too. '
                     'C4 is a notation, not a methodology: use the levels you need and stop, which '
                     'for most systems is the first two.</p>'
                     '<div class="canoncols">%s</div></div>' % canon_cols(C4_SET, CAT_C4))
        if i == CAT_UML:
            body += ('<div class="canon" id="uml14"><h2>The 14 UML diagram types</h2>'
                     '<p>UML 2.5 defines fourteen, in two groups of seven, and all fourteen are '
                     'on this page. Two of them are <em>filed</em> elsewhere — an architect reaches '
                     'for a sequence or deployment diagram by the job it does rather than by its '
                     'notation — so their entries live in those categories and are shown here too.'
                     '</p><div class="canoncols">%s</div></div>' % canon_cols(UML_14, CAT_UML))
        body += "".join(render_entry(en, root=False, home=i) for en in ents)
        body += pager(prev, nxt)
        written.append((cslug + ".html", page(
            cslug + ".html", "%s · Software Architect Diagram Dictionary" % name,
            "%s %d diagram types." % (blurb, len(ents)), cslug, body,
            aside=toc(ents, ([("c4set", "The C4 model")] if i == CAT_C4 else
                             [("uml14", "The 14 UML types")] if i == CAT_UML else None)))))
    return written


check_plates()
check_audiences()
check_related()
check_frequency()
_rankwarn = check_audience_order()
if _rankwarn:
    print("unranked on an audience page (%d):" % len(_rankwarn))
    for w in _rankwarn: print("   " + w)
_fit = check_text_fit()
if _fit:
    print("text may overflow its box in %d place(s):" % len(_fit))
    for w in _fit: print("   " + w)

def order_report():
    """Entries appear in declaration order, which is meant to run most-used first.
    Print what each category holds, marking the entries it only borrows, so one filed in
    the wrong place is easy to spot."""
    rows=[]
    for i, name, _slug, _b in CATS:
        ents=cat_listing(i)
        seq="".join("." if x["cat"]==i else "+" for x in ents)
        rows.append("   %02d %-30s %-14s %2d types" % (i, name, seq, len(ents)))
    return rows

_assets = write_assets()
pages = build()
_n = write_sitemap()

html_kb = sum(n for _, n in pages) / 1024.0
ast_kb  = sum(_assets.values()) / 1024.0
print("wrote %d pages (%.0f KB) + %d shared assets (%.0f KB), %d entries"
      % (len(pages), html_kb, len(_assets), ast_kb, len(E)))
for fname, n in pages:
    print("   %-32s %6.0f KB" % (fname, n / 1024.0))
print("   %-32s %6s" % ("assets/", ""))
for fname, n in sorted(_assets.items()):
    print("     %-30s %6.0f KB   (once, not %dx)" % (fname, n / 1024.0, len(pages)))
if _n:
    print("   %-32s %6d urls   %s" % ("sitemap.xml + robots.txt", _n, SITE))
else:
    print("   sitemap.xml skipped — set SITE_URL or add a git remote to generate it")
print("\ncategory contents  ·  . filed here, + also shown  ·  most-used first:")
for r in order_report(): print(r)

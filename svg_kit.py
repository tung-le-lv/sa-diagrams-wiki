# -*- coding: utf-8 -*-
import html

PAPER="#FFFFFF"; INK="#191D21"; MUTED="#6E7883"; LINE="#C6CCD2"
ACC="#1F5F8B"; ACC_S="#E2ECF4"
FLAG="#A8443A"; FLAG_S="#F7E9E5"
GRN="#3F6F51"; GRN_S="#E5EFE8"
AMB="#8A6A2B"; AMB_S="#F5EEDF"
VIO="#5B4B8A"; VIO_S="#EBE7F4"

def e(s): return html.escape(str(s), quote=True)

STYLES = {
 "plain": ("#FFFFFF", LINE, INK),
 "acc":   (ACC_S, ACC, "#123F5C"),
 "flag":  (FLAG_S, FLAG, "#7A2E27"),
 "grn":   (GRN_S, GRN, "#2A4C37"),
 "amb":   (AMB_S, AMB, "#5E4718"),
 "vio":   (VIO_S, VIO, "#3E3363"),
 "soft":  ("#F0F2F4", LINE, MUTED),
}
MARK = {MUTED:"mkm", ACC:"mka", FLAG:"mkf", GRN:"mkg", AMB:"mkb", VIO:"mkv"}

def node(x,y,w,h,title,sub=None,style="plain",rx=3,fs=12.5):
    fill,stroke,tc = STYLES[style]
    s='<rect x="%g" y="%g" width="%g" height="%g" rx="%g" fill="%s" stroke="%s" stroke-width="1.4"/>'%(x,y,w,h,rx,fill,stroke)
    cx=x+w/2.0
    if sub:
        s+='<text x="%g" y="%g" text-anchor="middle" font-size="%g" font-weight="600" fill="%s">%s</text>'%(cx,y+h/2.0-2,fs,tc,e(title))
        s+='<text x="%g" y="%g" text-anchor="middle" font-size="9.5" fill="%s">%s</text>'%(cx,y+h/2.0+11,MUTED,e(sub))
    else:
        s+='<text x="%g" y="%g" text-anchor="middle" font-size="%g" font-weight="600" fill="%s">%s</text>'%(cx,y+h/2.0+4.4,fs,tc,e(title))
    return s

def pill(x,y,w,h,title,style="plain",fs=11.5):
    return node(x,y,w,h,title,None,style,rx=h/2.0,fs=fs)

def cyl(x,y,w,h,title,sub=None,style="plain"):
    fill,stroke,tc = STYLES[style]
    ry=7.0
    s='<path d="M %g %g v %g a %g %g 0 0 0 %g 0 v %g z" fill="%s" stroke="%s" stroke-width="1.4"/>'%(x,y+ry,h-2*ry,w/2.0,ry,w,-(h-2*ry),fill,stroke)
    s+='<ellipse cx="%g" cy="%g" rx="%g" ry="%g" fill="%s" stroke="%s" stroke-width="1.4"/>'%(x+w/2.0,y+ry,w/2.0,ry,"#FFFFFF" if style=="plain" else fill,stroke)
    if sub:
        s+='<text x="%g" y="%g" text-anchor="middle" font-size="11.5" font-weight="600" fill="%s">%s</text>'%(x+w/2.0,y+h/2.0+1,tc,e(title))
        s+='<text x="%g" y="%g" text-anchor="middle" font-size="9.5" fill="%s">%s</text>'%(x+w/2.0,y+h/2.0+13,MUTED,e(sub))
    else:
        s+='<text x="%g" y="%g" text-anchor="middle" font-size="11.5" font-weight="600" fill="%s">%s</text>'%(x+w/2.0,y+h/2.0+7,tc,e(title))
    return s

# Zone wash — a grouping frame is a tinted region, not just an outline, so nesting and
# ownership read at a glance. Light enough that white boxes still sit clearly on top.
TINT = {ACC:"#EFF5FA", FLAG:"#FBF3F1", GRN:"#EFF6F2", AMB:"#FAF6EC", VIO:"#F4F2F9",
        MUTED:"#F5F7F8", LINE:"#F7F8F9", INK:"#F5F6F7"}

def frame(x,y,w,h,label,color=MUTED,dash=True,fill=None):
    d=' stroke-dasharray="6 5"' if dash else ''
    if fill is None: fill = TINT.get(color,"none")
    s='<rect x="%g" y="%g" width="%g" height="%g" rx="5" fill="%s" stroke="%s" stroke-width="1.2"%s/>'%(x,y,w,h,fill,color,d)
    s+='<text x="%g" y="%g" font-size="9.5" font-weight="600" letter-spacing="0.06em" fill="%s" paint-order="stroke" stroke="%s" stroke-width="4">%s</text>'%(x+11,y+0.5,color,fill if fill!="none" else PAPER,e(label.upper()))
    return s

def band(x,y,w,h,title,color=ACC,fs=10.5,rx=4.0):
    """A layered-architecture band: solid title bar over a tinted body."""
    hh=23.0
    s='<rect x="%g" y="%g" width="%g" height="%g" rx="%g" fill="%s" stroke="%s" stroke-width="1.2"/>'%(
        x,y,w,h,rx,TINT[color],color)
    s+='<rect x="%g" y="%g" width="%g" height="%g" rx="%g" fill="%s"/>'%(x,y,w,hh,rx,color)
    s+='<rect x="%g" y="%g" width="%g" height="%g" fill="%s"/>'%(x,y+hh-rx,w,rx,color)
    s+='<text x="%g" y="%g" text-anchor="middle" font-size="%g" font-weight="600" letter-spacing="0.04em" fill="#FFFFFF">%s</text>'%(
        x+w/2.0,y+15.5,fs,e(title))
    return s

def col(x,y,w,h,title,color=ACC,fs=10):
    """A labelled column — the same idea as band(), sized for vertical stacks."""
    return band(x,y,w,h,title,color,fs)

def arr(x1,y1,x2,y2,label=None,color=MUTED,dash=False,lp=0.5,dy=-6,fs=9.5,head=True):
    d=' stroke-dasharray="5 4"' if dash else ''
    m=' marker-end="url(#%s)"'%MARK[color] if head else ''
    s='<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="1.4"%s%s/>'%(x1,y1,x2,y2,color,d,m)
    if label:
        mx=x1+(x2-x1)*lp; my=y1+(y2-y1)*lp+dy
        s+=lbl(mx,my,label,fs)
    return s

def poly(pts,label=None,color=MUTED,dash=False,lx=None,ly=None,fs=9.5,head=True):
    d=' stroke-dasharray="5 4"' if dash else ''
    m=' marker-end="url(#%s)"'%MARK[color] if head else ''
    p=" ".join("%g,%g"%(a,b) for a,b in pts)
    s='<polyline points="%s" fill="none" stroke="%s" stroke-width="1.4"%s%s/>'%(p,color,d,m)
    if label: s+=lbl(lx,ly,label,fs)
    return s

def lbl(x,y,t,fs=9.5,color=None,weight="400",anchor="middle"):
    return '<text x="%g" y="%g" text-anchor="%s" font-size="%g" font-weight="%s" fill="%s" paint-order="stroke" stroke="%s" stroke-width="3.5">%s</text>'%(x,y,anchor,fs,weight,color or MUTED,PAPER,e(t))

def txt(x,y,t,fs=10.5,color=None,weight="400",anchor="start",style=""):
    return '<text x="%g" y="%g" text-anchor="%s" font-size="%g" font-weight="%s" fill="%s"%s>%s</text>'%(x,y,anchor,fs,weight,color or INK,(' font-style="italic"' if style=="i" else ''),e(t))

def svg(h, body, w=640):
    return '<svg class="plate" viewBox="0 0 %g %g" role="img" preserveAspectRatio="xMidYMid meet">%s</svg>'%(w,h,body)

def classbox(x,y,w,rows,title,style="plain"):
    hh=26.0; rh=15.0; h=hh+rh*len(rows)+8
    fill,stroke,tc=STYLES[style]
    s='<rect x="%g" y="%g" width="%g" height="%g" rx="3" fill="#FFFFFF" stroke="%s" stroke-width="1.4"/>'%(x,y,w,h,stroke)
    s+='<path d="M %g %g h %g v %g h %g z" fill="%s" stroke="%s" stroke-width="1.4"/>'%(x,y+hh,w,-hh+3,-w,fill,stroke)
    s+='<text x="%g" y="%g" text-anchor="middle" font-size="12" font-weight="600" fill="%s">%s</text>'%(x+w/2.0,y+17.5,tc,e(title))
    for i,r in enumerate(rows):
        s+='<text x="%g" y="%g" font-size="9.8" fill="%s">%s</text>'%(x+10,y+hh+13+i*rh,MUTED,e(r))
    return s

def lifelines(items, top=16, bottom=270, style=None):
    s=""; xs=[]
    for i,(x,w,name) in enumerate(items):
        st = (style[i] if style else "plain")
        s+=node(x,top,w,32,name,None,st,fs=11)
        cx=x+w/2.0; xs.append(cx)
        s+='<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="1.1" stroke-dasharray="4 4"/>'%(cx,top+32,cx,bottom,LINE)
    return s, xs

def msg(x1,x2,y,label,color=MUTED,dash=False,fs=9.5):
    s=arr(x1,y,x2,y,None,color,dash)
    mx=(x1+x2)/2.0
    return s+lbl(mx,y-6,label,fs)

def selfmsg(x,y,label,color=MUTED):
    s=poly([(x,y),(x+26,y),(x+26,y+16),(x+2,y+16)],color=color)
    return s+txt(x+32,y+12,label,9.5,MUTED)

DEFS = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>'
 + "".join('<marker id="%s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="%s"/></marker>'%(m,c) for c,m in MARK.items())
 + '</defs></svg>')


# ---------- additional primitives ----------
def dia(cx,cy,w,h,label=None,style="acc",fs=10,sub=None):
    """Diamond — decision / gateway."""
    fill,stroke,tc=STYLES[style]
    s='<path d="M %g %g L %g %g L %g %g L %g %g z" fill="%s" stroke="%s" stroke-width="1.4"/>'%(
        cx-w/2.0,cy,cx,cy-h/2.0,cx+w/2.0,cy,cx,cy+h/2.0,fill,stroke)
    if label:
        s+='<text x="%g" y="%g" text-anchor="middle" font-size="%g" font-weight="600" fill="%s">%s</text>'%(cx,cy+fs*0.36,fs,tc,e(label))
    if sub:
        s+=lbl(cx,cy+h/2.0+13,sub,9)
    return s

def stick(cx,y,label,color=INK,sub=None):
    """UML actor. Occupies y .. y+62 including the caption."""
    s='<circle cx="%g" cy="%g" r="7" fill="#FFFFFF" stroke="%s" stroke-width="1.4"/>'%(cx,y+7,color)
    s+=('<path d="M %g %g v 15 M %g %g h 22 M %g %g l -9 13 M %g %g l 9 13" '
        'stroke="%s" stroke-width="1.4" fill="none" stroke-linecap="round"/>')%(
        cx,y+14,cx-11,y+21,cx,y+29,cx,y+29,color)
    s+='<text x="%g" y="%g" text-anchor="middle" font-size="10" font-weight="600" fill="%s">%s</text>'%(cx,y+57,color,e(label))
    if sub: s+='<text x="%g" y="%g" text-anchor="middle" font-size="9" fill="%s">%s</text>'%(cx,y+69,MUTED,e(sub))
    return s

def oval(cx,cy,w,h,label,style="plain",fs=10.5,sub=None):
    """UML use case / rounded state."""
    fill,stroke,tc=STYLES[style]
    s='<ellipse cx="%g" cy="%g" rx="%g" ry="%g" fill="%s" stroke="%s" stroke-width="1.4"/>'%(cx,cy,w/2.0,h/2.0,fill,stroke)
    if sub:
        s+='<text x="%g" y="%g" text-anchor="middle" font-size="%g" font-weight="600" fill="%s">%s</text>'%(cx,cy-1,fs,tc,e(label))
        s+='<text x="%g" y="%g" text-anchor="middle" font-size="9" fill="%s">%s</text>'%(cx,cy+11,MUTED,e(sub))
    else:
        s+='<text x="%g" y="%g" text-anchor="middle" font-size="%g" font-weight="600" fill="%s">%s</text>'%(cx,cy+fs*0.36,fs,tc,e(label))
    return s

def note(x,y,w,lines,color=AMB,fs=9.5):
    """Folded-corner annotation. Height follows the line count."""
    h=14+len(lines)*13
    s='<path d="M %g %g h %g l %g %g v %g h %g z" fill="#FFFCF3" stroke="%s" stroke-width="1.2"/>'%(x,y,w-11,11,11,h-11,-w,color)
    s+='<path d="M %g %g v 11 h 11" fill="none" stroke="%s" stroke-width="1.2"/>'%(x+w-11,y,color)
    for i,t in enumerate(lines):
        s+='<text x="%g" y="%g" font-size="%g" fill="%s">%s</text>'%(x+9,y+16+i*13,fs,MUTED,e(t))
    return s

def grid(x,y,w,cols,rows,offsets,rh=27,hh=28,accent=ACC, cellcolor=None, rowicons=None):
    """Header row + data rows. `offsets` give each column's left edge as a fraction of w.
    `rowicons` is one (glyph, colour) per row, drawn at the head of the first column."""
    xs=[x+w*f for f in offsets]
    ind=24 if rowicons else 0
    s='<rect x="%g" y="%g" width="%g" height="%g" fill="%s" stroke="%s" stroke-width="1.2"/>'%(x,y,w,hh,ACC_S,accent)
    for i,c in enumerate(cols):
        s+=txt(xs[i]+8+(ind if i==0 else 0),y+hh*0.62,c,9.4,"#123F5C","600")
    for r,row in enumerate(rows):
        yy=y+hh+r*rh
        s+='<rect x="%g" y="%g" width="%g" height="%g" fill="%s" stroke="%s" stroke-width="1.1"/>'%(x,yy,w,rh,"#FFFFFF" if r%2 else "#F7F8F9",LINE)
        if rowicons:
            g,gc=rowicons[r]
            s+=icon(g,xs[0]+15,yy+rh/2.0,15,gc,1.4)
        for i,v in enumerate(row):
            col = cellcolor(r,i,v) if cellcolor else (INK if i==0 else MUTED)
            s+=txt(xs[i]+8+(ind if i==0 else 0),yy+rh*0.65,v,9.8,col,"600" if i==0 else "500")
    return s


# Boxes recorded for the build-time text-fit check: (text_x, box_y, box_right, h, text, fs)
_boxes = []

# ---------- icons ----------
# Each glyph is a list of path "d" strings on a 24x24 grid. Stroked, never filled, so the
# weight stays even at any size and the glyph inherits the box's accent colour.
ICONS = {
 "server":   ["M3 4h18v6H3z","M3 14h18v6H3z","M6.5 7h.01","M6.5 17h.01","M10 7h5","M10 17h5"],
 "db":       ["M4 6.5c0-1.9 3.6-3.5 8-3.5s8 1.6 8 3.5v11c0 1.9-3.6 3.5-8 3.5s-8-1.6-8-3.5z",
              "M4 6.5c0 1.9 3.6 3.5 8 3.5s8-1.6 8-3.5","M20 12c0 1.9-3.6 3.5-8 3.5S4 13.9 4 12"],
 "cloud":    ["M7 18.5h10.5a4 4 0 0 0 .4-8 6.2 6.2 0 0 0-11.8-1.3A3.6 3.6 0 0 0 7 18.5z"],
 "globe":    ["M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18z","M3.4 9.5h17.2","M3.4 14.5h17.2",
              "M12 3c-2.6 2.4-4 5.6-4 9s1.4 6.6 4 9","M12 3c2.6 2.4 4 5.6 4 9s-1.4 6.6-4 9"],
 "network":  ["M12 3.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5z","M5 15.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5z",
              "M19 15.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5z","M12 8.5v4","M12 12.5L6.5 15.5","M12 12.5l5.5 3"],
 "balancer": ["M12 3.5v7.5","M4.5 11h15","M6.5 11v7","M12 11v7","M17.5 11v7"],
 "firewall": ["M3 5h18v14H3z","M3 9.7h18","M3 14.3h18","M9 5v4.7","M15 5v4.7",
              "M6 9.7v4.6","M12 9.7v4.6","M18 9.7v4.6","M9 14.3V19","M15 14.3V19"],
 "shield":   ["M12 3l7.5 3v5.4c0 4.9-3 8.4-7.5 9.9-4.5-1.5-7.5-5-7.5-9.9V6z"],
 "lock":     ["M5 10.5h14v10H5z","M8.2 10.5V7.6a3.8 3.8 0 0 1 7.6 0v2.9","M12 14.5v2.5"],
 "key":      ["M8 3.5a4.5 4.5 0 1 0 0 9 4.5 4.5 0 0 0 0-9z","M11.2 11.2L20 20",
              "M17 17l-2 2","M14.5 14.5l-2 2","M8 8h.01"],
 "user":     ["M12 4a4 4 0 1 0 0 8 4 4 0 0 0 0-8z","M4.5 20.5c0-4.1 3.4-6.5 7.5-6.5s7.5 2.4 7.5 6.5"],
 "id":       ["M3.5 5h17v14h-17z","M9 10.2a2.2 2.2 0 1 0 0 4.4 2.2 2.2 0 0 0 0-4.4z",
              "M6 17.5c.6-1.6 1.7-2.4 3-2.4s2.4.8 3 2.4","M14.5 10.5h4","M14.5 14h4"],
 "token":    ["M3 9h18v2.2a1.8 1.8 0 0 0 0 3.6V17H3v-2.2a1.8 1.8 0 0 0 0-3.6z",
              "M9 9v1.8","M9 12.2v1.6","M9 15.2V17"],
 "warn":     ["M12 3.8L21.2 20H2.8z","M12 10v4.6","M12 17.3h.01"],
 "check":    ["M4 12.8l5.2 5.2L20 6.5"],
 "cert":     ["M4 3.5h9l3 3v10H4z","M13 3.5v3h3","M6.5 9h6","M6.5 12h4",
              "M17 12.5a3.5 3.5 0 1 0 0 7 3.5 3.5 0 0 0 0-7z","M15 19v3.5l2-1.2 2 1.2V19"],
 "branch":   ["M7 3.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5z","M7 15.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5z",
              "M17 3.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5z","M7 8.5v7","M17 8.5c0 4.5-4.5 3.5-7 6.5"],
 "rocket":   ["M12 2.5c3.2 2.7 4.8 6.3 4.8 10L12 17l-4.8-4.5c0-3.7 1.6-7.3 4.8-10z",
              "M12 8a1.7 1.7 0 1 0 0 3.4A1.7 1.7 0 0 0 12 8z","M8.6 15L6 21l4.2-1.9","M15.4 15l2.6 6-4.2-1.9"],
 "gear":     ["M12 8.8a3.2 3.2 0 1 0 0 6.4 3.2 3.2 0 0 0 0-6.4z",
              "M12 5.4a6.6 6.6 0 1 0 0 13.2 6.6 6.6 0 0 0 0-13.2z",
              "M18 12h2.8","M16.24 7.76l1.98-1.98","M12 6V3.2","M7.76 7.76L5.78 5.78",
              "M6 12H3.2","M7.76 16.24L5.78 18.22","M12 18v2.8","M16.24 16.24l1.98 1.98"],
 "sync":     ["M20 12a8 8 0 0 1-13.7 5.6","M4 12a8 8 0 0 1 13.7-5.6",
              "M17.7 3v3.4h-3.4","M6.3 21v-3.4h3.4"],
 "clock":    ["M12 3.2a8.8 8.8 0 1 0 0 17.6 8.8 8.8 0 0 0 0-17.6z","M12 7v5.4l3.6 2.1"],
 "bell":     ["M6.5 16.5V10.5a5.5 5.5 0 0 1 11 0v6l1.8 2.5H4.7z","M9.8 19a2.2 2.2 0 0 0 4.4 0","M12 5V3"],
 "chart":    ["M3.5 20.5h17","M7 20.5v-6.5","M12 20.5v-11","M17 20.5v-4"],
 "pulse":    ["M2.5 13h4l2.6-7.5L12.7 19l2.8-6 1.9 2h4.1"],
 "log":      ["M6 3h9l4 4v14H6z","M15 3v4h4","M9 12h7","M9 15.5h7","M9 19h4"],
 "search":   ["M10.8 3.5a7.3 7.3 0 1 0 0 14.6 7.3 7.3 0 0 0 0-14.6z","M16.2 16.2l4.6 4.6"],
 "eye":      ["M2.5 12S6.2 6 12 6s9.5 6 9.5 6-3.7 6-9.5 6-9.5-6-9.5-6z","M12 9a3 3 0 1 0 0 6 3 3 0 0 0 0-6z"],
 "funnel":   ["M3.5 4.5h17l-6.8 8v8l-3.4-2v-6z"],
 "archive":  ["M3 4.5h18v4.5H3z","M5 9v11h14V9","M9.8 13h4.4"],
 "bolt":     ["M13.5 2.5L5 14h6l-2 7.5L18 10h-6.5z"],
 "container":["M12 2.8l8.5 4.6v9.2L12 21.2l-8.5-4.6V7.4z","M3.5 7.4l8.5 4.6 8.5-4.6","M12 12v9.2"],
 "k8s":      ["M12 2.8L19.19 6.26L20.97 14.05L15.99 20.29L8.01 20.29L3.03 14.05L4.81 6.26z",
              "M12 12V8","M12 12l3.8 2.8","M12 12l-3.8 2.8"],
 "terminal": ["M3 4.5h18v15H3z","M6.5 9.5l3 2.5-3 2.5","M12.5 15h5"],
 "queue":    ["M3 8h13v8H3z","M3 11.5h13","M18 12h3","M18.7 9.7L21 12l-2.3 2.3"],
}

# Icons take the box's own accent so a drawing gains colour without gaining noise.
ICON_COLOR = {"plain":ACC,"acc":ACC,"flag":FLAG,"grn":GRN,"amb":AMB,"vio":VIO,"soft":MUTED}

def icon(name,cx,cy,size=17,color=None,w=1.5):
    """Glyph `name` centred on (cx,cy). Stroke width is pre-divided by the scale so the
    rendered weight is `w` whatever the size."""
    d=ICONS[name]; s=size/24.0
    return ('<g transform="translate(%g %g) scale(%g)" fill="none" stroke="%s" stroke-width="%g" '
            'stroke-linecap="round" stroke-linejoin="round">%s</g>'
            %(cx-size/2.0,cy-size/2.0,s,color or ACC,w/s,"".join('<path d="%s"/>'%p for p in d)))

def inode(x,y,w,h,title,sub=None,style="plain",ic=None,fs=11,rx=3,isize=17,pad=11):
    """Box with a glyph on the left and left-aligned text — the infrastructure idiom.
    Falls back to a centred plain node when `ic` is None."""
    if ic is None: return node(x,y,w,h,title,sub,style,rx,fs)
    fill,stroke,tc = STYLES[style]
    s='<rect x="%g" y="%g" width="%g" height="%g" rx="%g" fill="%s" stroke="%s" stroke-width="1.4"/>'%(
        x,y,w,h,rx,fill,stroke)
    s+=icon(ic,x+pad+isize/2.0,y+h/2.0,isize,ICON_COLOR[style])
    tx=x+pad+isize+9
    _boxes.append((tx,y,x+w,h,title,fs))
    if sub:
        s+='<text x="%g" y="%g" font-size="%g" font-weight="600" fill="%s">%s</text>'%(tx,y+h/2.0-2,fs,tc,e(title))
        s+='<text x="%g" y="%g" font-size="9.5" fill="%s">%s</text>'%(tx,y+h/2.0+11,MUTED,e(sub))
        _boxes.append((tx,y,x+w,h,sub,9.5))
    else:
        s+='<text x="%g" y="%g" font-size="%g" font-weight="600" fill="%s">%s</text>'%(tx,y+h/2.0+4.2,fs,tc,e(title))
    return s

def ihead(x,y,w,h,title,ic,style="plain",fs=11):
    """Lifeline / column header: glyph above a centred caption."""
    fill,stroke,tc = STYLES[style]
    s='<rect x="%g" y="%g" width="%g" height="%g" rx="3" fill="%s" stroke="%s" stroke-width="1.4"/>'%(
        x,y,w,h,fill,stroke)
    s+=icon(ic,x+w/2.0,y+15,16,ICON_COLOR[style])
    s+='<text x="%g" y="%g" text-anchor="middle" font-size="%g" font-weight="600" fill="%s">%s</text>'%(
        x+w/2.0,y+h-8,fs,tc,e(title))
    return s

def ilifelines(items, top=16, bottom=270, hh=46):
    """lifelines() with an icon in each header. items: (x, w, name, icon, style)."""
    s=""; xs=[]
    for x,w,name,ic,st in items:
        s+=ihead(x,top,w,hh,name,ic,st,fs=10.5)
        cx=x+w/2.0; xs.append(cx)
        s+='<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="1.1" stroke-dasharray="4 4"/>'%(
            cx,top+hh,cx,bottom,LINE)
    return s, xs

def lolli(x,y,label=None,color=ACC,side="left",length=24,fs=9.2):
    """UML provided interface — the ball on a stick."""
    d = -1 if side=="left" else 1
    s='<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="1.4"/>'%(x,y,x+d*length,y,color)
    s+='<circle cx="%g" cy="%g" r="5.5" fill="#FFFFFF" stroke="%s" stroke-width="1.4"/>'%(x+d*(length+6),y,color)
    if label: s+=lbl(x+d*(length+6),y-16,label,fs,color,"600")
    return s

def socket(x,y,label=None,color=ACC,side="right",length=24,fs=9.2):
    """UML required interface — the socket that a provided ball sits in."""
    d = 1 if side=="right" else -1
    cx = x+d*length          # where the provided ball sits, in the mouth of the cup
    # the stem stops at the back of the cup, or the arc reads as part of the line
    s='<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="1.4"/>'%(x,y,cx-d*12,y,color)
    s+='<path d="M %g %g A 12 12 0 0 %d %g %g" fill="none" stroke="%s" stroke-width="1.6"/>'%(
        cx,y-12,(0 if d>0 else 1),cx,y+12,color)
    if label: s+=lbl(cx,y+25,label,fs,color,"600")
    return s

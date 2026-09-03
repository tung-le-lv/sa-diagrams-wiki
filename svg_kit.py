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

def frame(x,y,w,h,label,color=MUTED,dash=True,fill="none"):
    d=' stroke-dasharray="6 5"' if dash else ''
    s='<rect x="%g" y="%g" width="%g" height="%g" rx="5" fill="%s" stroke="%s" stroke-width="1.2"%s/>'%(x,y,w,h,fill,color,d)
    s+='<text x="%g" y="%g" font-size="9.5" font-weight="600" letter-spacing="0.06em" fill="%s" paint-order="stroke" stroke="%s" stroke-width="4">%s</text>'%(x+11,y+0.5,color,PAPER,e(label.upper()))
    return s

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

def grid(x,y,w,cols,rows,offsets,rh=27,hh=28,accent=ACC, cellcolor=None):
    """Header row + data rows. `offsets` give each column's left edge as a fraction of w."""
    xs=[x+w*f for f in offsets]
    s='<rect x="%g" y="%g" width="%g" height="%g" fill="%s" stroke="%s" stroke-width="1.2"/>'%(x,y,w,hh,ACC_S,accent)
    for i,c in enumerate(cols):
        s+=txt(xs[i]+8,y+hh*0.62,c,9.4,"#123F5C","600")
    for r,row in enumerate(rows):
        yy=y+hh+r*rh
        s+='<rect x="%g" y="%g" width="%g" height="%g" fill="%s" stroke="%s" stroke-width="1.1"/>'%(x,yy,w,rh,"#FFFFFF" if r%2 else "#F7F8F9",LINE)
        for i,v in enumerate(row):
            col = cellcolor(r,i,v) if cellcolor else (INK if i==0 else MUTED)
            s+=txt(xs[i]+8,yy+rh*0.65,v,9.8,col,"600" if i==0 else "500")
    return s

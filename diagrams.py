# -*- coding: utf-8 -*-
"""One drawing function per diagram type. Each returns a complete <svg> string."""
from svg_kit import *

# ---------- diagrams ----------
def d_context():
    b=""
    b+=frame(232,86,186,92,"in scope",ACC,dash=False)
    b+=inode(248,106,154,54,"Order Platform","the system in scope","acc","container",fs=12.5)
    b+=inode(24,26,166,46,"Customer","person","soft","user",fs=11)
    b+=inode(24,192,166,46,"Support agent","person","soft","user",fs=11)
    b+=inode(452,20,164,46,"Payment provider","external","vio","lock",fs=11)
    b+=inode(452,108,164,46,"Email / SMS","external","vio","bell",fs=11)
    b+=inode(452,196,164,46,"Carrier API","external","vio","globe",fs=11)
    b+=arr(190,58,244,120,"places orders",lp=0.28,dy=-6)
    b+=arr(190,210,246,152,"handles returns",lp=0.55,dy=12)
    b+=arr(404,120,450,50,"authorises",lp=0.55,dy=-5)
    b+=arr(404,132,450,132,"notifies",dy=-6)
    b+=arr(404,144,450,212,"books shipment",lp=0.55,dy=12)
    b+=txt(24,272,"One box for the system, everyone and everything around it, and a verb on every arrow.",10,MUTED)
    b+=txt(24,287,"The moment a second box of yours appears, this has become a container diagram.",10,MUTED)
    return svg(298,b)

def d_container():
    b=""
    b+=frame(24,20,592,58,"clients",MUTED)
    b+=inode(40,34,168,34,"Web SPA","React","soft","globe",fs=10.5,isize=14,pad=8)
    b+=inode(224,34,168,34,"Mobile app","iOS / Android","soft","container",fs=10.5,isize=14,pad=8)
    b+=inode(408,34,192,34,"Partner system","server-to-server","soft","network",fs=10.5,isize=14,pad=8)
    b+=inode(150,96,240,44,"API Gateway",".NET 8 · authn, rate limit","acc","shield",fs=11.5)
    b+=inode(424,96,192,44,"Identity provider","OIDC","vio","key",fs=10.5)
    b+=arr(124,68,214,94); b+=arr(308,68,286,94)
    b+=arr(504,68,504,94)
    b+=arr(422,118,392,118,"validates",dy=-5,fs=9,color=VIO,dash=True)
    b+=frame(24,158,382,142,"our services",ACC,dash=False)
    b+=inode(40,182,170,42,"Order Service",".NET 8","acc","server",fs=10.5)
    b+=inode(222,182,170,42,"Payment Service",".NET 8","acc","server",fs=10.5)
    b+=cyl(40,240,170,48,"Orders DB","PostgreSQL","grn")
    b+=cyl(222,240,170,48,"Payments DB","PostgreSQL","grn")
    b+=arr(125,224,125,238); b+=arr(307,224,307,238)
    b+=arr(210,203,220,203)
    b+=arr(230,140,200,180,"HTTPS / JSON",lp=0.5,dy=-4,fs=9)
    b+=inode(424,182,192,42,"Kafka","event bus · 3 brokers","amb","queue",fs=10.5)
    b+=inode(424,240,192,42,"Notification Svc",".NET 8","acc","bell",fs=10.5)
    b+=inode(424,296,192,40,"Stripe","external system","soft","lock",fs=10.5)
    b+=arr(392,196,422,196,"events",dy=-5,fs=9,color=AMB,dash=True)
    b+=arr(520,224,520,238,None,AMB,dash=True)
    # Payment Service — not its database — is what calls the provider
    b+=poly([(392,214),(410,214),(410,316),(422,316)],color=MUTED)
    b+=lbl(352,312,"HTTPS  ·  sync, 3 s timeout",9)
    b+=txt(24,362,"Technology in brackets on every box, protocol on every arrow, solid for synchronous calls and",10,MUTED)
    b+=txt(24,377,"dashed for events. Boxes with no technology on them are a picture of nouns, not an architecture.",10,MUTED)
    return svg(388,b)

def d_component():
    b=frame(24,20,592,240,"Order Service  ·  one container",ACC,dash=False)
    b+=band(44,44,168,66,"API layer",ACC)
    b+=inode(52,74,152,28,"OrdersController",None,"plain","network",fs=9.5,isize=12,pad=5)
    b+=band(236,44,168,66,"Application",ACC)
    b+=inode(244,74,152,28,"PlaceOrderHandler",None,"plain","gear",fs=9.5,isize=12,pad=5)
    b+=band(428,44,168,66,"Infrastructure",ACC)
    b+=inode(436,74,152,28,"SqlOrderRepository",None,"soft","db",fs=9.5,isize=12,pad=5)
    b+=frame(44,130,552,112,"domain  ·  depends on nothing outside itself",GRN,dash=False)
    b+=inode(62,156,182,44,"Order","aggregate root","grn","container",fs=11)
    b+=inode(262,156,164,44,"OrderValidator","policy","grn","check",fs=10.5)
    b+=inode(444,156,134,44,"OrderPlaced","domain event","grn","bolt",fs=10.5)
    b+=txt(62,222,"No EF Core, no HTTP, no Kafka in here — which is what lets the arrows above point inward.",9.5,MUTED)
    b+=arr(212,84,234,84)
    # the adapter depends on the port, never the reverse — so this arrow points back at
    # Application, matching the rule the package diagram states
    b+=arr(426,84,406,84,None,ACC)
    b+=lbl(416,74,"port",8.4,ACC,"600")
    b+=arr(320,110,320,154,"mutates",lp=0.5,dy=-4,fs=9)
    b+=arr(244,178,258,178); b+=arr(426,178,442,178)
    b+=txt(24,290,"Worth drawing only for a service whose internals are genuinely non-obvious. Draw the container",10,MUTED)
    b+=txt(24,305,"boundary explicitly, or the level of zoom is ambiguous and the diagram starts an argument.",10,MUTED)
    b+=txt(24,320,"Both outer bands point at Application: the adapter depends on the port, not the other way round.",10,MUTED)
    return svg(332,b)

def d_class():
    b=""
    b+=classbox(36,44,164,["+ id : CustomerId","+ email : Email"],"Customer")
    b+=classbox(240,44,176,["+ id : OrderId","+ status : OrderStatus","+ total() : Money","+ place() / cancel()"],"Order","acc")
    b+=classbox(456,44,152,["+ productId","+ quantity : int","+ unitPrice : Money"],"OrderLine")
    b+=arr(200,80,238,80,None)
    b+=lbl(219,72,"places"); b+=lbl(206,94,"1",9.5); b+=lbl(232,94,"0..*",9.5)
    b+='<path d="M 424 80 l 10 -7 l 10 7 l -10 7 z" fill="%s" stroke="%s" stroke-width="1.3"/>'%(ACC,ACC)
    b+=arr(444,80,454,80,None,head=False)
    b+=lbl(438,66,"contains"); b+=lbl(420,98,"1",9.5); b+=lbl(452,98,"1..*",9.5)
    b+=txt(36,190,"The diamond is solid, and that is the content: composition — order lines cannot exist",10,MUTED)
    b+=txt(36,205,"without the order, which is what makes Order the aggregate root. A hollow diamond would",10,MUTED)
    b+=txt(36,220,"be aggregation, where the part outlives the whole. One fill decides which you meant.",10,MUTED)
    return svg(236,b)

def d_state():
    b=""
    b+='<circle cx="34" cy="126" r="6.5" fill="%s"/>'%INK
    b+=pill(56,108,96,36,"Draft","soft",fs=12)
    b+=pill(180,108,104,36,"Pending","acc",fs=12)
    b+=pill(312,108,96,36,"Paid","acc",fs=12)
    b+=pill(436,108,104,36,"Shipped","acc",fs=12)
    b+=pill(180,200,104,34,"Cancelled","soft",fs=11.5)
    b+=pill(312,32,96,34,"Failed","flag",fs=11.5)
    b+=pill(436,200,104,34,"Delivered","grn",fs=11.5)
    b+=arr(40,126,54,126)
    b+=arr(152,126,178,126,"place()",dy=-5)
    b+=arr(284,126,310,126,"authorised",dy=-5,fs=9,color=GRN)
    b+=arr(408,126,434,126,"dispatch()",dy=-5,fs=9)
    b+=poly([(232,144),(232,198)],color=MUTED,label="cancel()",lx=232,ly=176,fs=9)
    # a payment is declined out of Pending — an order that reached Paid never can be
    b+=poly([(266,108),(266,42),(310,42)],color=FLAG,label="declined",lx=288,ly=36,fs=9)
    b+=poly([(312,58),(244,58),(244,106)],color=MUTED,label="retry",lx=278,ly=52,fs=9)
    b+=poly([(488,144),(488,198)],color=GRN,label="delivered",lx=488,ly=176,fs=9)
    b+='<circle cx="568" cy="217" r="8" fill="none" stroke="%s" stroke-width="1.5"/><circle cx="568" cy="217" r="4.5" fill="%s"/>'%(INK,INK)
    b+=arr(540,217,558,217)
    # Cancelled is an ending, so it is drawn as one
    b+='<circle cx="140" cy="217" r="8" fill="none" stroke="%s" stroke-width="1.5"/><circle cx="140" cy="217" r="4.5" fill="%s"/>'%(INK,INK)
    b+=arr(178,217,156,217)
    b+=note(24,268,592,["Can a shipped order be cancelled? The diagram forces the question, and the answer is a business","rule someone has to own. Every state here either has an exit or is drawn as a final state — one","with neither is an entity stuck forever and a support ticket nobody can close."],AMB)
    return svg(340,b)

def d_sequence():
    items=[(24,108,"Client","globe","soft"),(150,108,"Gateway","shield","acc"),
           (272,116,"Order Svc","server","acc"),(410,116,"Payment","lock","vio"),
           (550,66,"Kafka","queue","amb")]
    s,x=ilifelines(items,16,372,hh=46)
    b=s
    b+=msg(x[0],x[1],92,"POST /orders")
    b+=msg(x[1],x[2],118,"CreateOrder + idempotency-key")
    b+=selfmsg(x[2],132,"persist, status = Pending")
    b+=msg(x[2],x[3],178,"Authorise  (3 s timeout)",VIO)
    # a real alt: three operands, each with its guard, divided by dashed separators.
    # One undivided box with three messages in it says nothing about which is which.
    b+='<rect x="236" y="194" width="368" height="150" rx="4" fill="%s" stroke="%s" stroke-width="1.1" stroke-dasharray="5 4"/>'%(TINT[MUTED],LINE)
    b+='<rect x="236" y="194" width="42" height="15" rx="3" fill="%s"/>'%MUTED
    b+=txt(257,205,"alt",9,"#FFFFFF","600","middle")
    b+=txt(288,206,"[approved]",8.8,MUTED,"600")
    b+=msg(x[3],x[2],226,"Approved",GRN,dash=True)
    b+=msg(x[2],x[4],250,"OrderConfirmed",AMB)
    b+='<line x1="236" y1="262" x2="604" y2="262" stroke="%s" stroke-width="1" stroke-dasharray="5 4"/>'%LINE
    b+=txt(244,276,"[declined]",8.8,MUTED,"600")
    b+=msg(x[3],x[2],292,"Declined  ·  order stays Pending",FLAG,dash=True)
    b+='<line x1="236" y1="304" x2="604" y2="304" stroke="%s" stroke-width="1" stroke-dasharray="5 4"/>'%LINE
    b+=txt(244,318,"[no response within 3 s]",8.8,MUTED,"600")
    b+=selfmsg(x[2],322,"timer fires — outcome unknown",FLAG)
    b+=msg(x[2],x[0],364,"201 Created  ·  402 declined  ·  202 Accepted if unknown",MUTED,dash=True)
    b+=txt(24,398,"Timeouts and retries on every network hop, an idempotency key, and every branch drawn as its own",10,MUTED)
    b+=txt(24,413,"operand with a guard. A timeout is not a decline — on a timeout you do not know whether it happened,",10,MUTED)
    b+=txt(24,428,"which is why the third branch returns 202 and not 402.",10,MUTED)
    return svg(440,b)

def d_dfd():
    b=""
    b+=frame(200,22,416,208,"trust boundary  ·  our infrastructure",FLAG)
    b+=inode(24,104,152,52,"Customer","external entity","soft","user",fs=10.5)
    b+=inode(222,54,168,52,"Validate order","process 1.0","acc","check",fs=10.5)
    b+=inode(222,152,168,52,"Charge payment","process 2.0","acc","lock",fs=10.5)
    b+=band(422,50,176,60,"D1  Orders store",GRN,fs=9.8)
    b+=txt(510,96,"PII · encrypted at rest",8.8,MUTED,anchor="middle")
    b+=band(422,148,176,60,"D2  Payment tokens",GRN,fs=9.8)
    b+=txt(510,194,"tokenised · PCI scope",8.8,MUTED,anchor="middle")
    b+=arr(176,124,220,86,"order data",lp=0.5,dy=-6,fs=9,color=FLAG)
    b+=arr(390,80,420,80,"write",dy=-5,fs=9)
    b+=arr(306,106,306,150,"valid",lp=0.5,dy=-3,fs=9)
    b+=arr(390,178,420,178,"token",dy=-5,fs=9)
    b+=note(24,248,592,["Every arrow crossing the dashed line is one round of threat-model questions: can it be spoofed,","tampered with, replayed, or read by someone who should not see it?"],FLAG)
    b+=txt(24,330,"A DFD shows data movement, not the order steps execute in. Mixing control flow into it turns it",10,MUTED)
    b+=txt(24,345,"into a flowchart and it stops being usable for either privacy review or STRIDE.",10,MUTED)
    return svg(356,b)

def d_erd():
    b=""
    b+=classbox(24,44,164,["id  PK","email  UK","created_at"],"CUSTOMER","grn")
    b+=classbox(236,44,168,["id  PK","customer_id  FK","status","total_amount"],"ORDER","acc")
    b+=classbox(452,44,164,["id  PK","order_id  FK","quantity","unit_price"],"ORDER_ITEM","grn")
    b+=classbox(236,176,168,["id  PK","amount","status"],"PAYMENT","vio")
    b+=arr(188,78,234,78,None,head=False)
    b+=lbl(211,72,"places"); b+=lbl(194,92,"1",9.5); b+=lbl(228,92,"0..N",9.5)
    b+=arr(404,78,450,78,None,head=False)
    b+=lbl(427,72,"contains"); b+=lbl(410,92,"1",9.5); b+=lbl(444,92,"1..N",9.5)
    b+=arr(320,148,320,174,None,head=False)
    b+=lbl(352,164,"settled by"); b+=lbl(308,156,"1",9.5); b+=lbl(308,172,"0..1",9.5)
    b+=note(24,248,592,["unit_price is stored on the line, not read from the product — a price change must not rewrite","history. Snapshot or reference is the decision an ERD forces you to make, quietly, once."])
    b+=txt(24,330,"Keys, cardinality on both ends, and — in a service estate — which service owns each entity. One",10,MUTED)
    b+=txt(24,345,"diagram of eighty tables helps nobody: split by bounded context and link at the boundaries.",10,MUTED)
    return svg(356,b)

def d_lineage():
    b=""
    xs=[(20,"Orders DB","PostgreSQL","plain"),(140,"CDC","Debezium","plain"),(258,"Kafka","orders.cdc","amb"),(376,"dbt","transforms","plain"),(494,"Warehouse","gold marts","acc")]
    for i,(x,t,s2,st) in enumerate(xs):
        b+=node(x,64,104,48,t,s2,st)
        if i<len(xs)-1: b+=arr(x+104,88,x+118,88)
    b+=node(494,148,104,40,"BI dashboard",None,"plain",fs=10.5)
    b+=node(360,148,104,40,"Finance export",None,"plain",fs=10.5)
    b+=arr(546,112,546,146)
    b+=poly([(520,112),(520,130),(412,130),(412,146)],color=MUTED)
    b+=txt(20,32,"“Revenue looks wrong.” This is how you answer in five minutes.",10.5,MUTED,style="i")
    return svg(206,b)

def d_deploy():
    b=""
    b+=inode(225,14,190,38,"Route 53","health-checked","plain","globe",fs=11)
    b+=inode(225,62,190,38,"CloudFront + WAF",None,"plain","shield",fs=11)
    b+=inode(225,110,190,38,"Load balancer",None,"acc","balancer",fs=11)
    b+=frame(24,166,282,124,"availability zone A")
    b+=frame(334,166,282,124,"availability zone B")
    b+=inode(42,190,140,44,"EKS nodes","2–10 pods","plain","container",fs=10.5)
    b+=inode(352,190,140,44,"EKS nodes","2–10 pods","plain","container",fs=10.5)
    b+=cyl(198,186,90,52,"RDS primary",None,"acc")
    b+=cyl(508,186,90,52,"RDS standby",None,"soft")
    b+=arr(320,52,320,60)
    b+=arr(320,100,320,108)
    b+=poly([(290,148),(150,148),(150,188)],color=MUTED)
    b+=poly([(350,148),(460,148),(460,188)],color=MUTED)
    b+=arr(182,208,196,208)
    b+=poly([(352,224),(320,224),(320,212),(290,212)],color=MUTED)
    b+=arr(288,264,506,264,"synchronous replication",color=MUTED,dash=True,dy=-5,fs=9)
    return svg(302,b)

def d_vpc():
    b=frame(24,44,592,238,"VPC  ·  10.0.0.0/16",ACC)
    b+=frame(44,70,552,66,"public subnet  ·  10.0.0.0/20")
    b+=inode(60,86,168,36,"NAT gateway",None,"plain","network",fs=10.5)
    b+=inode(240,86,168,36,"Application LB",None,"acc","balancer",fs=10.5)
    b+=inode(420,86,160,36,"Bastion / SSM",None,"soft","terminal",fs=10.5)
    b+=frame(44,150,552,60,"private app subnet  ·  10.0.16.0/20")
    b+=inode(60,164,258,36,"Order Service  :8080",None,"plain","server",fs=10.5)
    b+=inode(330,164,250,36,"Payment Service  :8080",None,"plain","server",fs=10.5)
    b+=frame(44,224,552,48,"private data subnet  ·  10.0.32.0/20")
    b+=inode(60,234,168,30,"RDS  :5432",None,"plain","db",fs=10,isize=14,pad=8)
    b+=inode(240,234,168,30,"Redis  :6379",None,"plain","bolt",fs=10,isize=14,pad=8)
    b+=inode(420,234,160,30,"S3 endpoint",None,"soft","archive",fs=10,isize=14,pad=8)
    b+=arr(305,122,305,162,"443",lp=0.5,dy=-2,fs=9)
    b+=arr(190,200,190,232,"5432",lp=0.5,dy=-2,fs=9)
    b+=inode(250,10,142,24,"Internet gateway",None,"soft","globe",fs=9.5,isize=13,pad=6)
    b+=arr(321,34,321,84,None)
    # the egress path, which is the half of a VPC diagram people leave out
    b+=poly([(100,164),(100,124)],color=AMB,label="0.0.0.0/0",lx=100,ly=144,fs=8.6)
    b+=poly([(144,86),(144,58),(280,58),(280,36)],color=AMB,label="egress via NAT",lx=212,ly=54,fs=8.6)
    b+=txt(24,300,"CIDR on every subnet, ports on every arrow, and the egress path drawn — a private subnet with",10,MUTED)
    b+=txt(24,315,"no NAT route is a service that cannot reach an OS mirror, and you find out at build time.",10,MUTED)
    b+=txt(24,330,"Draw actual reachability, not intended: generate it from your IaC wherever you can.",10,MUTED)
    return svg(342,b)

def d_oauth():
    items=[(24,116,"Browser / SPA","globe","plain"),(180,116,"Auth server","key","acc"),
           (346,116,"API gateway","shield","plain"),(500,116,"Order Svc","server","plain")]
    s,x=ilifelines(items,16,344,hh=48)
    b=s
    b+=selfmsg(x[0],90,"generate code_verifier, challenge, state")
    b+=msg(x[0],x[1],132,"/authorize  (code_challenge, state, scope)")
    b+=msg(x[1],x[0],154,"redirect  (authorization_code, state)",MUTED,dash=True)
    b+=selfmsg(x[0],168,"state matches? — CSRF check")
    b+=msg(x[0],x[1],206,"/token  (code, code_verifier)",ACC)
    b+=msg(x[1],x[0],228,"access 15 min + refresh 8 h + id_token",ACC,dash=True)
    b+=msg(x[0],x[2],256,"GET /orders   Bearer …")
    b+=selfmsg(x[2],270,"verify sig, iss, aud, exp, scope")
    b+=msg(x[2],x[3],308,"forward + propagated identity")
    b+=msg(x[0],x[1],336,"/token  (grant_type=refresh_token)  at 15 min",AMB)
    b+=txt(24,374,"PKCE because the SPA is a public client and cannot keep a secret; state because the redirect",10,MUTED)
    b+=txt(24,389,"is attacker-reachable; short access tokens with a longer refresh because revocation has to mean",10,MUTED)
    b+=txt(24,404,"something. The gateway authenticates — the service still authorises, or one compromised edge",10,MUTED)
    b+=txt(24,419,"rule becomes a cross-tenant read.",10,MUTED)
    return svg(431,b)

def d_trust():
    b=frame(24,20,592,214,"untrusted  ·  internet",FLAG)
    b+=inode(44,58,132,44,"User","browser","soft","user",fs=10.5)
    b+=inode(44,140,132,44,"Attacker",None,"flag","warn",fs=10.5)
    b+=frame(200,44,410,172,"boundary 1  ·  edge",AMB)
    b+=inode(220,72,150,42,"WAF + CDN",None,"amb","firewall",fs=10.5)
    b+=inode(220,146,150,42,"API gateway","TLS 1.3","amb","shield",fs=10.5)
    b+=frame(392,64,200,138,"boundary 2  ·  private",ACC)
    b+=inode(410,90,166,40,"Order Service","mTLS only","acc","server",fs=10.5)
    b+=cyl(410,144,166,46,"Orders DB","AES-256, KMS","acc")
    b+=arr(176,82,218,88)
    b+=arr(176,158,218,164,None,FLAG,dash=True)
    b+=arr(295,114,295,144)
    b+=arr(370,164,406,124,"JWT, 15 min",lp=0.5,dy=-4,fs=9)
    b+=arr(493,130,493,142)
    return svg(246,b)

def d_context_map():
    b=""
    b+=frame(24,40,180,84,"sales context",ACC,dash=False)
    b+=node(44,60,140,44,"Order","aggregate root","acc",fs=11)
    b+=frame(240,40,180,84,"billing context",MUTED,dash=False)
    b+=node(260,60,140,44,"Invoice","bill-to party",fs=11)
    b+=frame(240,164,180,84,"fulfilment context",MUTED,dash=False)
    b+=node(260,184,140,44,"Shipment","delivery address",fs=11)
    b+=frame(456,40,160,84,"CRM  ·  vendor",MUTED)
    b+=node(472,60,128,44,"Account","legacy model","soft",fs=11)
    b+=arr(204,72,238,72,"published events",lp=0.5,dy=-5,fs=9)
    b+=poly([(114,124),(114,206),(258,206)],label="customer / supplier",lx=176,ly=200,fs=9)
    b+=arr(454,90,422,90,"anti-corruption layer",lp=0.5,dy=-5,fs=9)
    b+=txt(24,278,"“Customer” is not one thing: a buyer with a credit limit here, a bill-to party there,",10,MUTED)
    b+=txt(24,292,"a delivery address over there. Forcing one shared model builds a distributed monolith.",10,MUTED)
    return svg(302,b)

def d_storming():
    b=""
    # one colour per sticky type and no two the same — the colour vocabulary IS the notation,
    # so an actor that looks like an event defeats the whole exercise
    cols=[("Actor","soft",24),("Command","acc",128),("Aggregate","plain",232),
          ("Event","amb",336),("Policy","vio",440),("Read model","grn",544)]
    names=["Customer","Place order","Order","OrderPlaced","When placed,\nreserve stock","Order summary"]
    for i,(cap,st,x) in enumerate(cols):
        b+=node(x,74,92,64,names[i].split("\n")[0],(names[i].split("\n")[1] if "\n" in names[i] else None),st,fs=10.5)
        b+=txt(x+46,64,cap.upper(),8.6,MUTED,"600","middle")
        if i<len(cols)-1: b+=arr(x+92,106,x+102,106)
    # the hot spot — the sticky that records that the room could not agree
    b+=node(336,20,196,30,"Does stock reserve before payment?",None,"flag",fs=8.6)
    b+=txt(300,38,"HOT SPOT",8.6,FLAG,"600","end")
    b+=poly([(392,50),(392,72)],color=FLAG,dash=True)
    # the timeline the wall is built along
    b+='<line x1="24" y1="162" x2="612" y2="162" stroke="%s" stroke-width="1.4" marker-end="url(#mkm)"/>'%MUTED
    b+=txt(24,178,"time — events in the past tense, left to right, before anyone is allowed to discuss a solution",9,MUTED)
    b+=txt(24,208,"Seven colours and they are the whole notation: grey actor, blue command, white aggregate, orange",10,MUTED)
    b+=txt(24,223,"event, purple policy, green read model, red hot spot. No two the same, or the wall stops meaning",10,MUTED)
    b+=txt(24,238,"anything. Run it with the business in the room — the output isn’t the wall, it’s the contexts you",10,MUTED)
    b+=txt(24,253,"spot where the language changes.",10,MUTED)
    return svg(265,b)

def d_topology():
    b=""
    b+=band(24,20,180,236,"publishers",ACC,fs=10)
    pubs=[("Order Service","OrderPlaced v3",56),("Payment Service","PaymentAuthorised v2",120),
          ("Inventory","StockReserved v1",184)]
    for n,ev,y in pubs:
        b+=inode(36,y,156,52,n,ev,"acc","server",fs=10)
    b+=inode(238,110,164,58,"Kafka","3 brokers + registry","amb","queue",fs=11.5)
    b+=band(436,20,180,236,"consumers",GRN,fs=10)
    cons=[("Shipping Service","OrderPlaced v3",56),("Notification Service","OrderPlaced v3",120),
          ("Analytics sink","all events",184)]
    for n,ev,y in cons:
        b+=inode(448,y,156,52,n,ev,"grn","server",fs=10)
    for y in (82,146,210): b+=arr(204,y,236,y-(y-139)*0.35,None,AMB)
    for y in (82,146,210): b+=arr(404,139+(y-139)*0.35,434,y,None,AMB)
    b+=txt(320,186,"key = orderId",9,MUTED,anchor="middle")
    b+=txt(320,198,"one publish → three consumers",9,MUTED,anchor="middle")
    b+=note(24,272,592,["The question it answers: if I change this event’s schema, who breaks? The fan-out on the right","is the blast radius, and the registry is what stops a breaking change reaching it."])
    b+=txt(24,354,"Name events as facts, in the past tense. OrderPlaced is a fact; ShipOrder is an instruction to one",10,MUTED)
    b+=txt(24,369,"handler, and the moment you name it that way you have built a queue with extra steps.",10,MUTED)
    return svg(380,b)

def d_saga():
    b=""
    b+=band(24,20,592,110,"forward path  ·  choreographed: each step reacts to the last event",GRN,fs=10)
    steps=[("Order","placed",40,"grn","check"),("Payment","authorised",188,"grn","check"),
           ("Inventory","rejected",336,"flag","warn"),("Shipping","never reached",484,"soft","clock")]
    for n,s2,x,st,ic in steps:
        b+=inode(x,58,116,48,n,s2,st,ic,fs=10.5,isize=14,pad=7)
    for x in (156,304,452): b+=arr(x,82,x+30,82)
    b+=band(24,150,444,110,"compensation  ·  runs in reverse",FLAG,fs=10)
    b+=inode(40,188,168,48,"Cancel order","OrderCancelled","flag","sync",fs=10.5)
    b+=inode(240,188,206,48,"Refund payment","PaymentRefunded","flag","sync",fs=10.5)
    b+=arr(238,212,212,212,None,FLAG)
    b+=poly([(394,106),(394,132),(343,132),(343,186)],color=FLAG,label="StockRejected",lx=430,ly=128,fs=9)
    # the branch for a step that simply never answers — not the same as one that fails
    b+=poly([(246,106),(246,126),(120,126),(120,186)],color=AMB,label="no answer in 30 s",lx=180,ly=120,fs=8.8)
    b+=note(486,150,130,["There is no","rollback across","services — only a","second business","transaction that","undoes the first."],FLAG)
    b+=txt(24,296,"A compensation for every forward step, and a timeout branch for any step that may never answer —",10,MUTED)
    b+=txt(24,311,"silence is not failure, and a saga that waits forever for one is an order stuck in limbo. A saga",10,MUTED)
    b+=txt(24,326,"diagram with no compensation arrows is not a saga, it is a wish.",10,MUTED)
    return svg(338,b)

def d_cqrs():
    b=""
    b+=frame(24,44,286,196,"write side  ·  one model, strict invariants",ACC,dash=False)
    b+=inode(40,72,254,40,"Command API","POST /orders","acc","network",fs=10.5)
    b+=inode(40,124,254,44,"Order aggregate","validates every invariant","acc","container",fs=10.5)
    b+=cyl(40,182,254,48,"Write store","normalised","acc")
    b+=arr(167,112,167,122); b+=arr(167,168,167,180)
    b+=frame(330,44,286,196,"read side  ·  one model per query shape",GRN,dash=False)
    # events feed the projector, the projector writes the store, the API reads it.
    # Stacked bottom-up so the chain reads in the direction the data actually flows.
    b+=inode(346,72,254,40,"Query API","GET /orders?…","grn","search",fs=10.5)
    b+=cyl(346,128,254,48,"Read store","query-shaped","grn")
    b+=inode(346,190,254,44,"Projector","denormalises on event","grn","sync",fs=10.5)
    b+=arr(473,188,473,178,None,GRN)
    b+=arr(473,126,473,114,None,GRN)
    b+=inode(226,258,188,40,"Kafka  ·  domain events",None,"amb","queue",fs=10.5)
    b+=poly([(167,230),(167,278),(224,278)],color=AMB)
    b+=poly([(416,278),(473,278),(473,238)],color=AMB)
    b+=lbl(545,268,"p99 lag 1.4 s",9,AMB,"600")
    b+=note(24,314,592,["The read model is eventually consistent. Put a number on it — “under 2 s at p99” — or the","product team will assume zero and design a UI that lies to the customer."],FLAG)
    b+=txt(24,396,"Sold as a scaling pattern; bought as a consistency problem. Adopt it per context, never estate-wide.",10,MUTED)
    return svg(408,b)

def d_bff():
    b=""
    b+=node(24,24,124,40,"Mobile app",None,fs=11)
    b+=node(24,84,124,40,"Web SPA",None,fs=11)
    b+=node(24,144,124,40,"Partner system",None,"soft",fs=11)
    b+=node(190,74,130,60,"API gateway","authn · rate limit","acc",fs=11.5)
    b+=node(360,18,132,44,"Mobile BFF","chatty → coarse",fs=11)
    b+=node(360,82,132,44,"Web BFF",None,fs=11)
    b+=node(360,146,132,44,"Partner API","versioned","soft",fs=11)
    b+=node(526,50,90,44,"Order Svc",None,fs=10.5)
    b+=node(526,114,90,44,"User Svc",None,fs=10.5)
    b+=arr(148,44,188,90); b+=arr(148,104,188,104); b+=arr(148,164,188,120)
    b+=arr(320,90,358,44); b+=arr(320,104,358,104); b+=arr(320,118,358,164)
    b+=arr(492,44,524,66); b+=arr(492,104,524,90); b+=arr(492,110,524,130); b+=arr(492,164,524,142)
    b+=txt(24,214,"One mobile screen needing seven fields from three services makes one call, not seven.",10,MUTED)
    return svg(228,b)

def d_mesh():
    b=""
    b+=node(230,20,180,42,"Control plane","Istio / Linkerd","acc",fs=11.5)
    for i,(x,n) in enumerate([(30,"Order Service"),(240,"Payment Service"),(450,"Inventory")]):
        b+=frame(x,104,160,86,"pod")
        b+=node(x+14,120,132,32,n,None,"plain",fs=10.5)
        b+=node(x+14,160,132,24,"sidecar proxy",None,"soft",fs=9.5)
        b+=arr(x+80,62,x+80,102,None,ACC,dash=True)
    b+=lbl(320,84,"policy + certs pushed — never on the request path",8.6,ACC,"600")
    b+=arr(190,172,238,172,"mTLS",dy=-5,fs=9)
    b+=arr(400,172,448,172,"mTLS",dy=-5,fs=9)
    # which policies are enforced where — the stated must-show, and the thing that
    # decides whether a control-plane outage takes traffic down with it
    b+=node(24,212,286,44,"Enforced in the sidecar","mTLS, retries, timeouts, outlier ejection","grn",fs=10)
    b+=node(330,212,286,44,"Decided in the control plane","who may call whom, cert issue and rotation","acc",fs=10)
    b+=txt(30,290,"The mesh gives you mTLS, retries, timeouts and traces without touching application code — at",10,MUTED)
    b+=txt(30,305,"the price of a second control plane to operate and debug. Say which policies live where: the",10,MUTED)
    b+=txt(30,320,"decision is central, the enforcement is in every sidecar, and nothing sits on the request path",10,MUTED)
    b+=txt(30,335,"that a control-plane outage can break. Adopting this for three services is all cost, no benefit.",10,MUTED)
    return svg(347,b)

def d_swimlane():
    b=""
    lanes=[("Customer",26,ACC),("Order system",96,ACC),("Support agent",180,AMB),("Warehouse",256,GRN)]
    for n,y,c in lanes:
        b+='<rect x="112" y="%g" width="504" height="%g" rx="3" fill="%s" stroke="%s" stroke-width="1"/>'%(
            y-14,64 if n!="Order system" else 72,TINT[c],LINE)
        b+='<rect x="24" y="%g" width="82" height="%g" rx="3" fill="%s"/>'%(y-14,64 if n!="Order system" else 72,c)
        b+=txt(65,y+22,n,10,"#FFFFFF","600","middle")
    b+=inode(128,24,150,36,"Submit return",None,"plain","log",fs=10,isize=13,pad=6)
    b+=dia(360,112,132,44,"within 30 days?","acc",fs=9.5)
    b+=inode(128,186,150,36,"Manual review",None,"amb","user",fs=10,isize=13,pad=6)
    b+=inode(310,256,150,36,"Inspect item",None,"grn","search",fs=10,isize=13,pad=6)
    b+=inode(478,88,132,30,"Issue label",None,"plain","cert",fs=9.6,isize=12,pad=5)
    b+=inode(478,122,132,30,"Trigger refund",None,"grn","check",fs=9.6,isize=12,pad=5)
    b+=arr(203,60,340,104)
    b+=poly([(360,134),(360,168),(203,168),(203,184)],color=MUTED,label="no",lx=280,ly=163,fs=9)
    b+=arr(426,112,476,103,"yes",dy=-5,fs=9)
    b+=poly([(278,204),(544,204),(544,154)],color=AMB,label="approved",lx=420,ly=199,fs=9)
    # Issue label → Inspect item, routed round the outside of both boxes rather than
    # straight through them
    b+=poly([(478,103),(430,103),(430,238),(385,238),(385,252)],color=MUTED,
            label="item comes back",lx=430,ly=250,fs=8.8)
    b+=poly([(460,274),(566,274),(566,154)],color=GRN,label="item OK",lx=512,ly=269,fs=9)
    b+=txt(24,330,"Every lane crossing is a handoff — a queue, a delay, a place work gets lost. Count them, then",10,MUTED)
    b+=txt(24,345,"label the diagram as-is or to-be, or everyone will read your to-be as a description of today.",10,MUTED)
    return svg(356,b)

def d_bpmn():
    b=""
    b+='<circle cx="44" cy="86" r="15" fill="#FFFFFF" stroke="%s" stroke-width="1.5"/>'%MUTED
    b+=txt(44,118,"start",9,MUTED,anchor="middle")
    b+=node(94,64,124,44,"Receive claim",None,"plain",fs=11)
    b+='<path d="M 250 86 l 30 -30 l 30 30 l -30 30 z" fill="%s" stroke="%s" stroke-width="1.4"/>'%(ACC_S,ACC)
    b+=txt(280,91,"×",16,ACC,"600",anchor="middle")
    b+=txt(280,134,"exclusive gateway",9,MUTED,anchor="middle")
    b+=node(346,16,130,36,"Auto-assess",None,"plain",fs=10.5)
    b+=node(346,96,130,44,"Manual review",None,"amb",fs=11)
    # interrupting timer boundary event — a double circle sitting on the task border,
    # and it has to lead somewhere or it is decoration
    b+='<circle cx="366" cy="140" r="9.5" fill="#FFFFFF" stroke="%s" stroke-width="1.3"/>'%AMB
    b+='<circle cx="366" cy="140" r="6.5" fill="none" stroke="%s" stroke-width="1"/>'%AMB
    b+='<path d="M 366 136 v 4.5 l 3 2" stroke="%s" stroke-width="1.1" fill="none"/>'%AMB
    b+=txt(382,158,"timer · escalate after 3 days",8.8,AMB,"600")
    b+=node(250,194,150,36,"Escalate to senior",None,"plain",fs=10.5)
    b+='<circle cx="452" cy="212" r="15" fill="#FFFFFF" stroke="%s" stroke-width="3"/>'%INK
    b+=txt(452,244,"end · escalated",9,MUTED,anchor="middle")
    b+='<circle cx="576" cy="70" r="15" fill="#FFFFFF" stroke="%s" stroke-width="3"/>'%INK
    b+=txt(576,102,"end · settled",9,MUTED,anchor="middle")
    b+=arr(59,86,92,86)
    b+=arr(218,86,248,86)
    b+=poly([(280,56),(280,34),(344,34)],color=MUTED,label="simple",lx=306,ly=28,fs=9)
    b+=poly([(310,86),(324,86),(324,118),(344,118)],color=MUTED,label="complex",lx=322,ly=106,fs=9)
    b+=poly([(476,34),(576,34),(576,53)],color=MUTED)
    b+=poly([(476,118),(540,118),(540,70),(559,70)],color=MUTED)
    b+=poly([(366,149),(366,192)],color=AMB)
    b+=arr(400,212,435,212)
    b+=txt(24,290,"BPMN earns its formality only when the model is executable — handed to Camunda or Temporal,",10,MUTED)
    b+=txt(24,305,"not printed. Six symbols carry most real models: start, task, exclusive gateway, boundary timer",10,MUTED)
    b+=txt(24,320,"and an end event per distinct outcome — and every path has to reach one of them.",10,MUTED)
    return svg(332,b)

def d_pipeline():
    b=""
    b+=band(24,20,592,92,"build once  ·  one immutable artefact",ACC,fs=10)
    st=[("Commit","git push",36,"branch"),("Build + unit","artefact",150,"gear"),
        ("SAST / SCA","blocking",264,"shield"),("Contract","consumer-led",378,"check"),
        ("Sign + SBOM","provenance",492,"cert")]
    for i,(n,s2,x,ic) in enumerate(st):
        b+=inode(x,56,108,44,n,s2,"plain",ic,fs=9.6,isize=13,pad=6)
        if i<len(st)-1: b+=arr(x+108,78,st[i+1][2]-2,78)
    b+=poly([(546,112),(546,136),(367,136)],color=MUTED)
    b+=dia(322,136,90,36,"approve","acc",fs=9.5)
    b+=poly([(277,136),(94,136),(94,166)],color=MUTED)
    b+=band(24,166,592,96,"promote the same artefact  ·  never rebuild",GRN,fs=10)
    dp=[("Deploy dev","automatic",40,"rocket","plain"),("Deploy staging","+ smoke tests",180,"rocket","plain"),
        ("Canary  5 %","watch the SLO",324,"pulse","amb"),("Promote 100 %",None,464,"check","grn")]
    for i,(n,s2,x,ic,stl) in enumerate(dp):
        b+=inode(x,202,132,44,n,s2,stl,ic,fs=10,isize=13,pad=6)
        if i<3: b+=arr(x+132,224,dp[i+1][2]-2,224)
    b+=poly([(390,246),(390,278),(106,278),(106,248)],color=FLAG,label="SLO breach → automatic rollback",lx=248,ly=292,fs=9)
    b+=txt(24,326,"One immutable artefact promoted across environments — never rebuilt per environment, or what",10,MUTED)
    b+=txt(24,341,"you tested is not what you shipped. Roll back on a signal, not on somebody noticing.",10,MUTED)
    return svg(352,b)

def d_release():
    b=""
    b+=txt(24,26,"CANARY",9.5,ACC,"600")
    b+=inode(24,38,140,46,"Load balancer",None,"acc","balancer",fs=10.5)
    b+=inode(190,32,140,30,"v1  ·  95 %",None,"grn","container",fs=10,isize=13,pad=6)
    b+=inode(190,72,140,30,"v2  ·  5 %",None,"amb","container",fs=10,isize=13,pad=6)
    b+=arr(164,54,188,46); b+=arr(164,68,188,86)
    b+=inode(350,42,136,40,"SLO check",None,"plain","chart",fs=10.5)
    b+=arr(330,87,348,70)
    b+=inode(512,32,104,30,"Promote",None,"grn","check",fs=10,isize=13,pad=6)
    b+=inode(512,72,104,30,"Roll back",None,"flag","warn",fs=10,isize=13,pad=6)
    b+=arr(486,56,510,48,"pass",lp=0.5,dy=-5,fs=9)
    b+=arr(486,70,510,86,"fail",lp=0.5,dy=11,fs=9)
    b+='<line x1="24" y1="126" x2="616" y2="126" stroke="%s" stroke-width="1"/>'%LINE
    b+=txt(24,152,"BLUE / GREEN",9.5,ACC,"600")
    b+=inode(24,164,140,46,"Router",None,"acc","network",fs=10.5)
    b+=inode(190,158,180,30,"Blue  ·  live",None,"grn","container",fs=10,isize=13,pad=6)
    b+=inode(190,198,180,30,"Green  ·  idle, warmed",None,"soft","container",fs=10,isize=13,pad=6)
    b+=arr(164,180,188,172)
    b+=arr(164,194,188,212,None,MUTED,dash=True)
    # cut over moves traffic TO green, so the arrowhead belongs on green
    b+=poly([(372,173),(450,173),(450,213),(370,213)],color=ACC,label="cut over — one router change",lx=430,ly=248,fs=9)
    b+=txt(24,272,"Both strategies run two app versions against one schema — so migrations must expand,",10,MUTED)
    b+=txt(24,287,"backfill, then contract in a later release. That is the step teams forget, and it is the one",10,MUTED)
    b+=txt(24,302,"that makes the rollback in either strategy actually work.",10,MUTED)
    return svg(314,b)

def d_observability():
    b=""
    b+=inode(24,86,140,52,"Services","OTel SDK","acc","server",fs=11)
    b+=inode(180,86,140,52,"Collector","agent + gateway","plain","funnel",fs=11)
    b+=inode(356,20,150,40,"Loki","30 d · 1 TB/day cap","plain","log",fs=10.5)
    b+=inode(356,92,150,40,"Prometheus","15 s · 13 mo · 50 k","plain","chart",fs=10.5)
    b+=inode(356,164,150,40,"Tempo","10 % tail sample","plain","search",fs=10.5)
    b+=inode(536,52,80,40,"Grafana",None,"plain","eye",fs=10,isize=12,pad=5)
    b+=inode(536,132,80,40,"PagerDuty",None,"flag","bell",fs=10,isize=12,pad=5)
    b+=arr(164,112,178,112)
    b+=arr(320,105,354,42,"logs",lp=0.55,dy=-4,fs=9)
    b+=arr(320,112,354,112,"metrics",lp=0.5,dy=-5,fs=9)
    b+=arr(320,119,354,184,"traces",lp=0.55,dy=10,fs=9)
    b+='<line x1="514" y1="40" x2="514" y2="184" stroke="%s" stroke-width="1.2"/>'%LINE
    for yy in (40,112,184): b+=arr(506,yy,513,yy,None,MUTED,head=False)
    b+=arr(514,72,534,72); b+=arr(514,152,534,152)
    b+=txt(24,240,"One trace_id, set at the edge and propagated through every hop including the broker — it is the",10,MUTED)
    b+=txt(24,255,"only thing that joins the three signals into one investigation. Metrics alert you → traces localise",10,MUTED)
    b+=txt(24,270,"it → logs explain it. Retention and the cardinality cap are on the boxes because they are what",10,MUTED)
    b+=txt(24,285,"this costs; the collector is the architectural decision, because it lets you change the rest.",10,MUTED)
    return svg(297,b)

def d_breaker():
    b=""
    b+=pill(60,40,120,42,"Closed","grn",fs=12.5)
    b+=pill(400,40,120,42,"Open","flag",fs=12.5)
    b+=pill(230,150,120,42,"Half-open","amb",fs=12.5)
    b+=arr(182,54,398,54,"failure rate > 50 % over 20 calls",dy=-8,fs=9.5,color=FLAG)
    b+=poly([(452,82),(452,171),(354,171)],color=MUTED,label="after 30 s cooldown",lx=452,ly=126,fs=9.5)
    b+=poly([(228,171),(120,171),(120,84)],color=GRN,label="3 successes",lx=160,ly=182,fs=9.5)
    b+=poly([(290,148),(290,110),(438,110),(438,84)],color=FLAG,label="any failure",lx=364,ly=104,fs=9.5)
    b+=txt(24,232,"What makes this architectural, not a library detail: what you serve while it is open.",10,MUTED)
    b+=txt(24,247,"Cached price? Queue for later? Reject with a clear message? That is a product decision.",10,MUTED)
    return svg(258,b)

def d_failover():
    b=""
    b+=node(250,18,140,40,"Route 53","health checks","acc",fs=11)
    b+=frame(24,84,282,150,"primary  ·  eu-west-1  active",GRN,dash=False)
    b+=frame(334,84,282,150,"secondary  ·  warm standby",MUTED)
    b+=node(48,110,150,42,"App tier  ·  100 %",None,"grn",fs=10.5)
    b+=node(358,110,150,42,"App tier  ·  20 %",None,"soft",fs=10.5)
    b+=cyl(48,168,150,50,"Aurora writer",None,"grn")
    b+=cyl(358,168,150,50,"Aurora replica",None,"soft")
    b+=poly([(280,58),(123,58),(123,108)],color=GRN,label="100 %",lx=200,ly=52,fs=9)
    b+=poly([(360,58),(433,58),(433,108)],color=MUTED,dash=True,label="on failure",lx=420,ly=52,fs=9)
    b+=arr(123,152,123,166); b+=arr(433,152,433,166)
    b+=arr(198,193,356,193,"async replication  ·  lag ≈ 1 s",color=MUTED,dash=True,dy=-6,fs=9)
    b+=txt(24,262,"RPO = the replication lag, about a second. RTO = detection + DNS TTL + promotion + scale-up,",10,MUTED)
    b+=txt(24,277,"realistically 5–15 minutes — not the “instant” everyone assumes.",10,MUTED)
    return svg(288,b)

def d_tree():
    b=""
    b+=node(210,20,220,44,"Caller needs the result now?",None,"acc",fs=11.5)
    b+=node(40,110,190,44,"Callee always available?",None,"plain",fs=11)
    b+=node(400,110,190,44,"Consumers need ordering?",None,"plain",fs=11)
    b+=node(24,204,140,40,"Sync REST / gRPC",None,"grn",fs=10.5)
    b+=node(186,204,150,40,"Sync + circuit breaker",None,"amb",fs=10.5)
    b+=node(352,204,120,40,"Kafka, keyed",None,"grn",fs=10.5)
    b+=node(492,204,124,40,"SQS / Service Bus",None,"grn",fs=10.5)
    b+=poly([(280,64),(280,88),(135,88),(135,108)],color=MUTED,label="yes",lx=200,ly=82,fs=9)
    b+=poly([(360,64),(360,88),(495,88),(495,108)],color=MUTED,label="no",lx=440,ly=82,fs=9)
    b+=poly([(90,154),(90,182),(94,182),(94,202)],color=MUTED,label="yes",lx=74,ly=176,fs=9)
    b+=poly([(180,154),(180,182),(261,182),(261,202)],color=MUTED,label="no",lx=222,ly=176,fs=9)
    b+=poly([(450,154),(450,182),(412,182),(412,202)],color=MUTED,label="yes",lx=418,ly=176,fs=9)
    b+=poly([(540,154),(540,182),(554,182),(554,202)],color=MUTED,label="no",lx=572,ly=176,fs=9)
    b+=txt(24,272,"Published once, a decision tree is applied consistently by people who weren’t in the room —",10,MUTED)
    b+=txt(24,287,"and you stop answering the same question in every design review.",10,MUTED)
    return svg(298,b)

def d_matrix():
    b=""
    # weights above the columns, scores inside, total on the right — a comparison table
    # with neither weights nor scores is not a decision matrix
    cols=[("Option",None),("Delivery speed","weight 3"),("Op cost","weight 2"),("Team fit","weight 3"),
          ("Scale ceiling","weight 1"),("Reversibility","weight 3"),("Total","/ 60")]
    xs=[24,150,252,332,414,498,570]
    b+=txt(24,22,"WEIGHTS AGREED BEFORE ANY OPTION WAS SCORED",9,ACC,"600")
    b+='<rect x="24" y="30" width="592" height="42" fill="%s" stroke="%s" stroke-width="1.2"/>'%(ACC_S,ACC)
    for i,(c,w) in enumerate(cols):
        b+=txt(xs[i]+8,48,c,9.4,"#123F5C","600")
        if w: b+=txt(xs[i]+8,63,w,8.6,ACC,"500")
    rows=[["Monolith","5","5","5","2","4","54"],
          ["Modular monolith","4","5","5","4","5","56"],
          ["Microservices","2","2","2","5","1","24"]]
    for r,row in enumerate(rows):
        y=72+r*32; win=(r==1)
        b+='<rect x="24" y="%g" width="592" height="32" fill="%s" stroke="%s" stroke-width="1.1"/>'%(
            y,(GRN_S if win else ("#FFFFFF" if r%2 else "#F7F8F9")),(GRN if win else LINE))
        for i,v in enumerate(row):
            if i==0:   colr,wt=INK,("700" if win else "600")
            elif i==6: colr,wt=(GRN if win else MUTED),"700"
            else:      colr,wt={"5":GRN,"4":GRN,"3":MUTED,"2":AMB,"1":FLAG}.get(v,MUTED),"600"
            b+=txt(xs[i]+8,y+20,v,10,colr,wt)
    b+=txt(24,192,"Scores are 1–5, multiplied by the weight above each column. The weights were fixed first, which",10,MUTED)
    b+=txt(24,207,"is the only rule that keeps this honest — weight after scoring and the matrix documents a decision",10,MUTED)
    b+=txt(24,222,"you had already made. Reversibility is carried as a criterion and weighted as heavily as delivery",10,MUTED)
    b+=txt(24,237,"speed: a cheap-to-reverse choice should be made fast, alone, and revisited rather than debated.",10,MUTED)
    return svg(249,b)

def d_rag():
    b=""
    b+=txt(24,26,"INGESTION",9.5,ACC,"600")
    b+=node(24,38,110,42,"Source docs",None,"plain",fs=10.5)
    b+=node(158,38,110,42,"Chunk + metadata","+ ACL per chunk","plain",fs=10)
    b+=node(292,38,110,42,"Embed",None,"plain",fs=10.5)
    b+=cyl(426,32,140,52,"Vector store","chunks + ACL","acc")
    b+=arr(134,59,156,59); b+=arr(268,59,290,59); b+=arr(402,59,424,59)
    b+=txt(24,100,"refresh: nightly full, 5-minute delta on change",9,MUTED,style="i")
    b+='<line x1="24" y1="112" x2="616" y2="112" stroke="%s" stroke-width="1"/>'%LINE
    b+=txt(24,152,"QUERY",9.5,ACC,"600")
    b+=node(24,164,104,42,"Question",None,"plain",fs=10.5)
    b+=node(152,164,104,42,"Embed query",None,"plain",fs=10.5)
    b+=node(280,164,96,42,"Re-rank",None,"plain",fs=10.5)
    b+=node(400,164,110,42,"Prompt + cites",None,"plain",fs=10.5)
    b+=node(534,164,82,42,"LLM",None,"vio",fs=11)
    b+=arr(128,185,150,185); b+=arr(256,185,278,185); b+=arr(376,185,398,185); b+=arr(510,185,532,185)
    # the round trip that makes it retrieval-augmented: the query has to reach the store,
    # and the permission filter is applied there — not in the prompt
    b+=poly([(204,164),(204,128),(470,128),(470,88)],color=ACC,
            label="k-NN search, filtered by this user’s ACL",lx=330,ly=124,fs=9)
    b+=poly([(524,88),(524,150),(328,150),(328,162)],color=ACC,label="top-k chunks",lx=390,ly=146,fs=9)
    b+=node(24,240,246,38,"No relevant hit → say so","never let the model fill the gap","flag",fs=10)
    b+=node(290,240,326,38,"Guardrails + grounding check","every claim traceable to a cited chunk","amb",fs=10)
    b+=poly([(328,206),(328,222),(147,222),(147,238)],color=FLAG)
    b+=poly([(575,206),(575,222),(453,222),(453,238)],color=AMB)
    b+=txt(24,306,"Two paths, one store. Apply access control at retrieval, per user, against the chunk’s own",10,MUTED)
    b+=txt(24,321,"ACL — never in the prompt, where the model will happily quote a document the asker cannot",10,MUTED)
    b+=txt(24,336,"open. And decide up front what happens when nothing relevant comes back.",10,MUTED)
    return svg(348,b)

def d_serverless():
    b=""
    b+=node(24,60,110,44,"API Gateway",None,"acc",fs=10.5)
    b+=node(160,60,120,44,"createOrder","λ · 512 MB · max 50",fs=10.5)
    b+=cyl(306,54,124,52,"DynamoDB","orders")
    b+=node(456,20,160,40,"projectReadModel","λ · stream · max 2",fs=10.5)
    b+=node(456,86,160,40,"EventBridge",None,"amb",fs=10.5)
    b+=node(306,152,124,40,"SQS",None,"amb",fs=10.5)
    b+=node(160,152,120,40,"fulfil","λ · batch 10 · max 5",fs=10.5)
    b+=node(24,152,110,40,"DLQ","alarmed","flag",fs=10.5)
    b+=arr(134,82,158,82,"HTTP",dy=-5,fs=9)
    b+=arr(280,82,304,82)
    b+=poly([(430,68),(444,68),(444,44),(454,44)],color=MUTED,label="streams",lx=452,ly=64,fs=9)
    b+=poly([(430,94),(454,94)],color=MUTED)
    b+=poly([(536,126),(536,172),(432,172)],color=AMB,label="events",lx=520,ly=166,fs=9)
    b+=arr(304,172,282,172)
    b+=arr(158,172,136,172,"after 3 retries",lp=0.5,dy=-5,fs=9,color=FLAG)
    b+=txt(24,226,"Label the trigger on every arrow — HTTP, stream, schedule, event — plus the reserved",10,MUTED)
    b+=txt(24,241,"concurrency cap and the dead-letter queue. Those are the parts a serverless diagram exists to",10,MUTED)
    b+=txt(24,256,"show: without the cap, one traffic spike opens 3 000 connections to a database sized for 200.",10,MUTED)
    return svg(268,b)


# ==================================================================
# Additions — the remaining named types from the source notes.
# ==================================================================

# ---------- 1. Architecture & system-level ----------
def d_c4_code():
    b=frame(24,20,592,196,"PlaceOrderHandler  ·  component")
    b+=classbox(46,50,156,["+ Handle(cmd) : Result"],"PlaceOrderHandler","acc")
    b+=classbox(248,50,160,["- lines : List<Line>","+ Place() / Cancel()","+ Total() : Money"],"Order")
    b+=classbox(452,50,146,["+ Add(o) : Task","+ Save() : Task"],"IOrderRepository")
    b+=classbox(452,144,146,["EF Core"],"SqlOrderRepository","soft")
    b+=arr(202,72,246,72,"creates",dy=-5,fs=9)
    b+=arr(408,72,450,72,"persists",dy=-5,fs=9)
    b+='<path d="M 525 142 v -20" stroke="%s" stroke-width="1.3" stroke-dasharray="5 4" fill="none"/>'%MUTED
    b+='<path d="M 517 124 l 8 -9 l 8 9 z" fill="#FFFFFF" stroke="%s" stroke-width="1.3"/>'%MUTED
    b+=txt(46,178,"Hollow triangle on a dashed line = realises the interface. The handler depends on",10,MUTED)
    b+=txt(46,193,"the abstraction; only the composition root knows EF Core exists.",10,MUTED)
    b+=txt(24,242,"C4 level 4. Generate it from code on demand, for one component, then throw it away — a",10,MUTED)
    b+=txt(24,257,"checked-in code diagram is stale before the sprint ends. Most components never need one.",10,MUTED)
    return svg(268,b)

def d_solution():
    b=""
    b+=txt(24,22,"BUSINESS",9,MUTED,"600")
    b+=node(24,30,180,38,"Order-to-cash",None,"acc",fs=11)
    b+=node(216,30,180,38,"Returns",None,"acc",fs=11)
    b+=node(408,30,208,38,"Customer service",None,"acc",fs=11)
    b+=txt(24,100,"APPLICATIONS",9,MUTED,"600")
    b+=node(24,108,140,44,"Storefront","own · React",fs=10.5)
    b+=node(176,108,140,44,"Order platform","own · in scope","acc",fs=10.5)
    b+=node(328,108,140,44,"ERP","buy · SAP","soft",fs=10.5)
    b+=node(480,108,136,44,"CRM","buy · Dynamics","soft",fs=10.5)
    b+=txt(24,180,"INTEGRATION",9,MUTED,"600")
    b+=node(24,188,284,36,"Event backbone  ·  Kafka",None,"amb",fs=10.5)
    b+=node(320,188,296,36,"Sync APIs  ·  REST via gateway",None,"plain",fs=10.5)
    b+=txt(24,252,"DATA",9,MUTED,"600")
    b+=cyl(24,256,180,46,"Operational","one store per service")
    b+=cyl(216,256,180,46,"Analytical","Snowflake")
    b+=node(408,260,208,40,"Master data","customer golden record","soft",fs=10.5)
    b+=arr(94,68,94,106); b+=arr(246,68,246,106); b+=arr(512,68,512,106)
    b+=arr(246,152,246,186); b+=arr(468,152,468,186)
    b+=arr(114,224,114,254); b+=arr(306,224,306,254)
    b+=txt(24,332,"Four bands on one page: what the business does, what runs it, how the pieces join, where data sits.",10,MUTED)
    b+=txt(24,347,"Mark every application build / buy / reuse — that is the decision this diagram exists to carry.",10,MUTED)
    return svg(358,b)

def d_logical():
    b=""
    bands=[("Channels",26,["Web","Mobile","Partner API","Contact centre"],"soft"),
           ("Experience",92,["Session & personalisation","Content assembly"],"plain"),
           ("Business services",158,["Ordering","Pricing","Fulfilment","Billing"],"acc"),
           ("Integration",224,["Routing","Transformation","Event distribution"],"plain"),
           ("Data",290,["Operational","Analytical","Reference / master"],"plain")]
    for name,y,items,st in bands:
        b+=txt(24,y+26,name,10.5,INK,"600")
        n=len(items); x0=150; w=(466-(n-1)*10)/float(n)
        for i,it in enumerate(items):
            b+=node(x0+i*(w+10),y,w,42,it,None,st,fs=10)
        if y<290: b+=arr(383,y+42,383,y+64)
    b+=txt(24,372,"Deliberately technology-free — not one vendor, product or hostname on it. That is the point: the",10,MUTED)
    b+=txt(24,387,"logical view survives the re-platforming that renames every box in the physical view.",10,MUTED)
    return svg(398,b)

def d_physical():
    b=frame(24,22,592,208,"eu-west-1  ·  production",ACC)
    b+=node(44,48,168,44,"Edge","CloudFront","soft",fs=10.5)
    b+=node(228,48,180,44,"NLB","2 Gbps sustained","acc",fs=10.5)
    b+=node(424,48,172,44,"Redis","cache.r6g.large × 3",fs=10.5)
    b+=frame(44,108,264,106,"cluster  ·  6 × m6i.2xlarge")
    b+=node(62,132,110,34,"node-1","8 vCPU / 32 GB","plain",fs=9.5)
    b+=node(182,132,110,34,"node-2","8 vCPU / 32 GB","plain",fs=9.5)
    b+=node(62,174,110,32,"node-3",None,"plain",fs=9.5)
    b+=node(182,174,110,32,"node-4 … 6",None,"plain",fs=9.5)
    b+=frame(332,108,264,106,"data  ·  db.r6g.4xlarge")
    b+=cyl(350,126,110,50,"primary","16 vCPU","acc")
    b+=cyl(474,126,104,50,"replica","read-only","soft")
    b+=node(350,186,228,22,"gp3  ·  4 TB  ·  12 000 IOPS",None,"plain",fs=9.5)
    b+=arr(212,70,226,70); b+=arr(408,70,422,70)
    b+=arr(318,92,240,106); b+=arr(464,92,464,106)
    b+=txt(24,258,"Instance types, core counts, IOPS, link speeds. The logical diagram says what the parts are;",10,MUTED)
    b+=txt(24,273,"this one is where capacity, headroom and the monthly bill actually get decided.",10,MUTED)
    return svg(284,b)

def d_cloud():
    b=""
    b+=node(24,24,104,34,"Users",None,"soft",fs=10.5)
    b+=node(150,24,116,34,"Route 53",None,"plain",fs=10.5)
    b+=node(288,24,140,34,"CloudFront + WAF",None,"plain",fs=10.5)
    b+=node(450,24,166,34,"Cognito  ·  OIDC",None,"plain",fs=10.5)
    b+=frame(24,76,592,192,"VPC  ·  10.0.0.0/16  ·  3 AZs",ACC)
    b+=node(44,104,150,42,"ALB","public subnets","acc",fs=10.5)
    b+=node(214,104,180,42,"ECS Fargate","order-svc · 4–20 tasks",fs=10.5)
    b+=node(414,104,182,42,"ECS Fargate","payment-svc · 2–8 tasks",fs=10.5)
    b+=cyl(44,166,150,52,"Aurora","Multi-AZ writer","acc")
    b+=node(214,168,180,44,"ElastiCache","Redis · 3 nodes",fs=10.5)
    b+=node(414,168,182,44,"SQS + EventBridge","async fan-out","amb",fs=10.5)
    b+=node(44,230,270,26,"S3  ·  versioned, SSE-KMS",None,"plain",fs=9.5)
    b+=node(330,230,266,26,"Secrets Manager  ·  30 d rotation",None,"plain",fs=9.5)
    b+=arr(128,41,148,41); b+=arr(266,41,286,41)
    b+=poly([(358,58),(358,74),(119,74),(119,102)],color=MUTED)
    b+=arr(194,125,212,125); b+=arr(394,125,412,125)
    b+=arr(119,146,119,164); b+=arr(304,146,304,166); b+=arr(505,146,505,166)
    b+=poly([(533,58),(533,68),(304,68),(304,102)],color=MUTED,dash=True,label="JWT",lx=424,ly=64,fs=9)
    b+=txt(24,296,"Use the provider’s own service names — “Aurora Multi-AZ”, not “database”. The named service is the",10,MUTED)
    b+=txt(24,311,"contract: it fixes failover behaviour, quotas and price. A generic box hides all three.",10,MUTED)
    return svg(322,b)

def d_reference():
    b=frame(24,20,592,180,"reference architecture  ·  standard web service",ACC,dash=False)
    b+=node(46,54,116,40,"Ingress","gateway + WAF","acc",fs=10.5)
    b+=node(178,54,116,40,"Service","container, 12-factor","acc",fs=10.5)
    b+=node(310,54,116,40,"State","managed store","acc",fs=10.5)
    b+=node(442,54,150,40,"Platform","logs, metrics, traces","acc",fs=10.5)
    b+=arr(162,74,176,74); b+=arr(294,74,308,74); b+=arr(426,74,440,74)
    b+=node(46,116,168,66,"Team A  ·  conforms","adopts as-is","grn",fs=10.5)
    b+=node(230,116,168,66,"Team B  ·  extends","adds a read replica","amb",fs=10.5)
    b+=node(414,116,178,66,"Team C  ·  deviates","gRPC ingress — ADR-042","flag",fs=10.5)
    b+=arr(130,94,130,114,None,GRN); b+=arr(314,94,314,114,None,AMB); b+=arr(503,94,503,114,None,FLAG)
    b+=txt(24,228,"A reference architecture is a default, not a law. The third box is what makes it work: deviation is",10,MUTED)
    b+=txt(24,243,"allowed and costs one written ADR. Without that escape hatch, teams stop telling you they left.",10,MUTED)
    return svg(254,b)

def d_landscape():
    b=""
    for n,x,c in [("Commerce",24,ACC),("Finance",236,MUTED),("Logistics",448,MUTED)]:
        b+=frame(x,28,168,196,n,c,dash=False)
    b+=node(40,54,136,40,"Storefront","own · React",fs=10)
    b+=node(40,104,136,40,"Order platform","own · .NET","acc",fs=10)
    b+=node(40,154,136,40,"Pricing","own · .NET",fs=10)
    b+=node(252,54,136,40,"ERP","buy · SAP","soft",fs=10)
    b+=node(252,104,136,40,"Billing","own · .NET",fs=10)
    b+=node(252,154,136,40,"Tax engine","buy · Avalara","soft",fs=10)
    b+=node(464,54,136,40,"WMS","buy · Manhattan","soft",fs=10)
    b+=node(464,104,136,40,"Carrier hub","own · Go",fs=10)
    b+=node(464,154,136,40,"Track & trace","retire 2027","flag",fs=10)
    b+=arr(176,124,250,124,"events",dy=-5,fs=9,color=AMB)
    b+=arr(388,124,462,124,"events",dy=-5,fs=9,color=AMB)
    b+=poly([(108,194),(108,212),(532,212),(532,194)],color=MUTED,dash=True,label="nightly batch — the integration nobody owns",lx=320,ly=228,fs=9)
    b+=txt(24,266,"One row per domain, one box per system, and a lifecycle mark on each: invest, tolerate, retire.",10,MUTED)
    b+=txt(24,281,"Executives read this diagram to fund things. Keep it to one page or it stops being read.",10,MUTED)
    return svg(292,b)

# ---------- 2. UML ----------
def d_usecase():
    b=frame(184,20,336,206,"Order platform",MUTED,dash=False)
    b+=stick(76,40,"Customer")
    b+=stick(76,140,"Support agent")
    b+=stick(576,40,"Payment provider",sub="«system»")
    b+=oval(274,58,160,40,"Place order","acc",fs=10.5)
    b+=oval(274,120,160,40,"Cancel order",fs=10.5)
    b+=oval(274,182,160,40,"Track order",fs=10.5)
    b+=oval(452,58,116,34,"Take payment","soft",fs=9.8)
    b+=oval(452,182,116,34,"Send SMS update","soft",fs=9.8)
    b+=arr(108,58,192,58,None,head=False)
    b+=arr(108,68,192,114,None,head=False)
    b+=arr(108,152,192,126,None,head=False)
    b+=arr(108,162,192,178,None,head=False)
    b+=arr(560,58,512,58,None,head=False)
    # «include»: base → included.  «extend»: extension → base.  Directions matter.
    b+='<path d="M 356 58 h 30" stroke="%s" stroke-width="1.3" stroke-dasharray="4 4" fill="none" marker-end="url(#mkm)"/>'%MUTED
    b+=lbl(374,50,"«include»",8.8)
    b+='<path d="M 392 182 h -30" stroke="%s" stroke-width="1.3" stroke-dasharray="4 4" fill="none" marker-end="url(#mkm)"/>'%MUTED
    b+=lbl(374,174,"«extend»",8.8)
    b+=txt(24,258,"Scope, not design: the boundary says what is in the release, and every actor outside it is someone",10,MUTED)
    b+=txt(24,273,"whose needs you owe. Ovals are goals — “place order”, never “click submit button”. Include points",10,MUTED)
    b+=txt(24,288,"from the base to the step it always performs; extend points from the optional behaviour back to it.",10,MUTED)
    return svg(300,b)

def d_activity():
    b=""
    b+='<circle cx="46" cy="118" r="8" fill="%s"/>'%INK
    b+=node(80,98,116,40,"Receive order",None,"plain",fs=10.5)
    b+=dia(250,118,74,52,"valid?","acc",fs=10)
    b+='<rect x="316" y="42" width="7" height="152" fill="%s"/>'%INK
    b+=txt(320,32,"fork",9,MUTED,anchor="middle")
    b+=node(348,52,132,38,"Reserve stock",None,"plain",fs=10.5)
    b+=node(348,146,132,38,"Authorise payment",None,"plain",fs=10.5)
    b+='<rect x="508" y="42" width="7" height="152" fill="%s"/>'%INK
    b+=txt(512,32,"join",9,MUTED,anchor="middle")
    b+=node(348,222,132,38,"Reject order",None,"flag",fs=10.5)
    b+='<circle cx="576" cy="118" r="11" fill="none" stroke="%s" stroke-width="1.5"/><circle cx="576" cy="118" r="6" fill="%s"/>'%(INK,INK)
    b+=arr(54,118,78,118); b+=arr(196,118,212,118)
    b+=arr(287,118,314,118,"yes",dy=-5,fs=9)
    b+=poly([(250,144),(250,241),(346,241)],color=FLAG,label="no",lx=268,ly=190,fs=9)
    b+=poly([(323,71),(346,71)],color=MUTED); b+=poly([(323,165),(346,165)],color=MUTED)
    b+=poly([(480,71),(506,71)],color=MUTED); b+=poly([(480,165),(506,165)],color=MUTED)
    b+=arr(515,118,564,118)
    b+=poly([(480,241),(576,241),(576,131)],color=FLAG)
    b+=txt(24,290,"The bar is the whole reason to reach for an activity diagram instead of a flowchart: it states that",10,MUTED)
    b+=txt(24,305,"stock and payment run concurrently and that both must finish before the order proceeds.",10,MUTED)
    return svg(316,b)

def d_package():
    b=""
    def pkg(x,y,w,h,name,style="plain",sub=None):
        fill,stroke,tc=STYLES[style]
        s='<path d="M %g %g h 62 v 14 h %g v %g h %g z" fill="%s" stroke="%s" stroke-width="1.4"/>'%(x,y,w-62,h-14,-w,fill,stroke)
        s+=txt(x+w/2.0,y+(h+14)/2.0+2,name,11.5,tc,"600","middle")
        if sub: s+=txt(x+w/2.0,y+(h+14)/2.0+16,sub,9,MUTED,"400","middle")
        return s
    b+=pkg(228,24,180,62,"Api","acc","controllers, DTOs")
    b+=pkg(228,124,180,62,"Application",sub="handlers, ports")
    b+=pkg(228,224,180,62,"Domain","grn","entities, no deps")
    b+=pkg(452,124,164,62,"Infrastructure",sub="EF Core, HTTP")
    b+=pkg(24,124,164,62,"Contracts","soft","published events")
    b+='<path d="M 318 86 v 34" stroke="%s" stroke-width="1.3" stroke-dasharray="5 4" fill="none" marker-end="url(#mkm)"/>'%MUTED
    b+='<path d="M 318 186 v 34" stroke="%s" stroke-width="1.3" stroke-dasharray="5 4" fill="none" marker-end="url(#mkm)"/>'%MUTED
    b+='<path d="M 452 160 h -40" stroke="%s" stroke-width="1.3" stroke-dasharray="5 4" fill="none" marker-end="url(#mkm)"/>'%MUTED
    b+='<path d="M 188 152 h 36" stroke="%s" stroke-width="1.3" stroke-dasharray="5 4" fill="none" marker-end="url(#mkm)"/>'%MUTED
    # green, because it is a legal edge — red here would say the opposite of the label
    b+=poly([(534,186),(534,256),(412,256)],color=GRN,dash=True,label="allowed — it points inward",lx=500,ly=272,fs=9)
    b+=txt(24,306,"Dependencies point inward and Domain depends on nothing. Green is a legal edge; one arrow the",10,MUTED)
    b+=txt(24,321,"other way — Domain reaching out to Infrastructure — is an architecture violation you can see",10,MUTED)
    b+=txt(24,336,"from across the room, and can assert in a build test so it never lands twice.",10,MUTED)
    return svg(348,b)

def d_object():
    b=""
    def obj(x,y,w,rows,title,style="plain"):
        hh=26.0; rh=15.0; h=hh+rh*len(rows)+8
        fill,stroke,tc=STYLES[style]
        s='<rect x="%g" y="%g" width="%g" height="%g" rx="3" fill="#FFFFFF" stroke="%s" stroke-width="1.4"/>'%(x,y,w,h,stroke)
        s+='<path d="M %g %g h %g v %g h %g z" fill="%s" stroke="%s" stroke-width="1.4"/>'%(x,y+hh,w,-hh+3,-w,fill,stroke)
        s+='<text x="%g" y="%g" text-anchor="middle" font-size="11.5" font-weight="600" fill="%s" text-decoration="underline">%s</text>'%(x+w/2.0,y+17.5,tc,e(title))
        for i,r in enumerate(rows):
            s+='<text x="%g" y="%g" font-size="9.8" fill="%s">%s</text>'%(x+10,y+hh+13+i*rh,MUTED,e(r))
        return s
    b+=obj(30,44,168,["email = “ana@x.io”","tier = Gold"],"ana : Customer")
    b+=obj(242,44,172,["status = Pending","total = 148.00 EUR"],"o-8871 : Order","acc")
    b+=obj(452,26,164,["qty = 2","unitPrice = 39.00"],"l-1 : OrderLine")
    b+=obj(452,116,164,["qty = 1","unitPrice = 70.00"],"l-2 : OrderLine")
    b+=arr(198,72,240,72,None,head=False); b+=lbl(219,66,"places")
    b+=arr(414,72,450,56,None,head=False)
    b+=arr(414,80,450,142,None,head=False)
    b+=txt(30,214,"A class diagram says “an order has one or more lines”. This says: on 14 March, order o-8871 had",10,MUTED)
    b+=txt(30,229,"exactly these two. Reach for it to pin down one confusing case, not to document the model.",10,MUTED)
    return svg(240,b)

def d_composite():
    b=frame(56,24,528,182,"« component »  Order Service",ACC,dash=False)
    b+=node(86,64,140,50,"orders : Handler","part",fs=10.5)
    b+=node(250,64,140,50,"pricing : Engine","part","acc",fs=10.5)
    b+=node(250,140,140,46,"cache : Redis","part","soft",fs=10.5)
    b+=node(414,64,140,50,"repo : Store","part",fs=10.5)
    # ports are the squares on the boundary; the ball/socket on each says which way
    # the contract points, so provided and required are not the same drawing
    for y,lab in [(84,"IOrders"),(160,"IEvents")]:
        b+='<rect x="48" y="%g" width="16" height="16" fill="#FFFFFF" stroke="%s" stroke-width="1.4"/>'%(y-8,ACC)
        b+=lolli(48,y,lab,ACC,"left",14)
    b+='<rect x="576" y="80" width="16" height="16" fill="#FFFFFF" stroke="%s" stroke-width="1.4"/>'%MUTED
    b+=socket(592,88,"IPayments",MUTED,"right",22)
    b+=arr(64,84,84,84); b+=arr(226,89,248,89); b+=arr(390,89,412,89)
    b+=poly([(320,114),(320,138)],color=MUTED)
    b+=poly([(64,160),(156,160),(156,116)],color=MUTED)
    b+=arr(554,89,574,89)
    b+=txt(24,240,"Ports are the squares on the boundary, parts are the instances inside, connectors are the wiring",10,MUTED)
    b+=txt(24,255,"between them. A ball is an interface this component provides; a socket is one it requires — so",10,MUTED)
    b+=txt(24,270,"the whole contract is readable from outside, which is the only reason to draw this instead of a",10,MUTED)
    b+=txt(24,285,"component diagram.",10,MUTED)
    return svg(298,b)

def d_communication():
    b=""
    b+=node(38,110,116,44,":Client",None,"plain",fs=11)
    b+=node(240,40,140,44,":OrderService",None,"acc",fs=11)
    b+=node(240,180,140,44,":PaymentService",None,"plain",fs=11)
    b+=node(462,110,140,44,":OrderRepo",None,"plain",fs=11)
    b+='<line x1="154" y1="126" x2="240" y2="72" stroke="%s" stroke-width="1.4"/>'%LINE
    b+='<line x1="310" y1="84" x2="310" y2="178" stroke="%s" stroke-width="1.4"/>'%LINE
    b+='<line x1="380" y1="72" x2="462" y2="126" stroke="%s" stroke-width="1.4"/>'%LINE
    # Each message runs alongside its own link, in the direction it travels, and the
    # numbering nests: 1.1 happens inside 1, which is what carries the call depth.
    msgs=[(176,106, 22,-14,"1 : place(cmd)",      206, 78,False),
          (322,100,  0, 30,"1.1 : authorise()",   382,120,False),
          (298,160,  0,-30,"1.1 : ⟵ approved",    232,148,True),
          (398, 92, 26, 18,"1.2 : save(order)",   442, 86,False)]
    for x,y,dx,dy2,t,lx,ly,dash in msgs:
        b+=('<path d="M %g %g l %g %g" stroke="%s" stroke-width="1.6" fill="none"%s '
            'marker-end="url(#mka)"/>')%(x,y,dx,dy2,ACC,' stroke-dasharray="5 4"' if dash else '')
        b+=lbl(lx,ly,t,9.2,ACC)
    b+=txt(24,262,"Same information as a sequence diagram, arranged by topology rather than by time. Nesting in the",10,MUTED)
    b+=txt(24,277,"numbers is what carries the order: 1.1 and 1.2 both happen inside 1, and the dashed arrow is a",10,MUTED)
    b+=txt(24,292,"reply, not a new call. Better than a sequence when the shape of the call graph is the point;",10,MUTED)
    b+=txt(24,307,"worse whenever timing, timeouts or alt branches matter, which is most of the time.",10,MUTED)
    return svg(318,b)

def d_timing():
    b=""
    # A timing diagram whose axis is not linear is just an awkward state machine, so the
    # axis is computed: 150 px = t0-10 s, 608 px = t0+70 s, and every event is placed by X().
    T0=150.0; PPS=458.0/80.0
    def X(t): return T0+(t+10)*PPS
    lanes=[("Circuit breaker",["Closed","Open","Half-open"],48),
           ("Downstream API",["Healthy","Failing"],176)]
    for name,states,y0 in lanes:
        b+=txt(24,y0+18,name,10.5,INK,"600")
        for i,s in enumerate(states):
            yy=y0+i*30
            b+=txt(140,yy+16,s,9.2,MUTED,anchor="end")
            b+='<line x1="%g" y1="%g" x2="608" y2="%g" stroke="%s" stroke-width="1" stroke-dasharray="3 4"/>'%(T0,yy+12,yy+12,LINE)
    def seg(y,ta,tb,color=ACC):
        return '<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="2.6"/>'%(X(ta),y,X(tb),y,color)
    def step(t,ya,yb,color=ACC):
        return '<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="2.6"/>'%(X(t),ya,X(t),yb,color)
    CL,OP,HO = 60,90,120
    HE,FA    = 188,218
    b+=seg(CL,-10,20)+step(20,CL,OP)+seg(OP,20,50)+step(50,OP,HO)
    b+=seg(HO,50,56)+step(56,HO,CL)+seg(CL,56,70)
    b+=seg(HE,-10,0,FLAG)+step(0,HE,FA,FLAG)+seg(FA,0,52,FLAG)
    b+=step(52,FA,HE,FLAG)+seg(HE,52,70,FLAG)
    for t,lab,ty in [(0,"errors start",30),(20,"trip",30),(50,"probe",18),
                     (52,"dependency recovers",30),(56,"close",18)]:
        b+='<line x1="%g" y1="36" x2="%g" y2="240" stroke="%s" stroke-width="1" stroke-dasharray="2 4"/>'%(X(t),X(t),LINE)
        b+=txt(X(t),ty,lab,8.4,MUTED,anchor="middle")
    b+='<line x1="%g" y1="240" x2="608" y2="240" stroke="%s" stroke-width="1.2"/>'%(T0,LINE)
    for k in range(-10,71,10):
        b+='<line x1="%g" y1="240" x2="%g" y2="246" stroke="%s" stroke-width="1"/>'%(X(k),X(k),LINE)
        b+=txt(X(k),260,("t0" if k==0 else "%+d s"%k),8.4,MUTED,anchor="middle")
    b+=txt(24,260,"seconds",9,ACC,"600")
    b+=txt(24,294,"The only UML diagram with a real time axis — and the axis has to be linear, or the drawing lies:",10,MUTED)
    b+=txt(24,309,"20 seconds must occupy twice the width of 10. Note the breaker closes only after the dependency",10,MUTED)
    b+=txt(24,324,"recovers; a probe that fails in half-open sends it straight back to open.",10,MUTED)
    return svg(336,b)

def d_interaction_overview():
    b=""
    # branches placed either side of the decision so nothing overlaps the diamond
    b+='<circle cx="46" cy="70" r="8" fill="%s"/>'%INK
    for x,y,w,h,t,st in [(84,44,146,52,"ref  Authenticate","plain"),(276,44,150,52,"ref  Place order","acc"),
                         (100,196,150,52,"ref  Compensate","flag"),(452,196,150,52,"ref  Confirm & notify","plain")]:
        b+=node(x,y,w,h,t,None,st,fs=11)
        b+='<path d="M %g %g h 34 v 14" fill="none" stroke="%s" stroke-width="1.2"/>'%(x,y+14,STYLES[st][1])
    b+=dia(351,140,76,48,"ok?","acc",fs=10)
    b+=arr(54,70,82,70); b+=arr(230,70,274,70)
    b+=arr(351,96,351,114)
    b+=poly([(313,140),(175,140),(175,194)],color=FLAG,label="no",lx=240,ly=134,fs=9)
    b+=poly([(389,140),(527,140),(527,194)],color=GRN,label="yes",lx=462,ly=134,fs=9)
    for cx in (175,527):
        b+=arr(cx,248,cx,266)
        b+='<circle cx="%g" cy="280" r="11" fill="none" stroke="%s" stroke-width="1.5"/>'%(cx,INK)
        b+='<circle cx="%g" cy="280" r="6" fill="%s"/>'%(cx,INK)
    b+=txt(24,320,"An activity diagram whose nodes are whole sequence diagrams. Worth drawing exactly once per",10,MUTED)
    b+=txt(24,335,"large flow — as the index page that says which of your twelve sequence diagrams to open, and",10,MUTED)
    b+=txt(24,350,"in what order. The moment a message appears on it you have drawn a bad sequence diagram.",10,MUTED)
    return svg(362,b)

def d_profile():
    b=""
    b+=classbox(60,44,150,["(UML metaclass)"],"Component","soft")
    b+=classbox(300,44,164,["+ sla : Duration","+ tier : {1,2,3}","+ owner : Team"],"«stereotype»  Service","acc")
    b+='<path d="M 300 76 h -76" stroke="%s" stroke-width="1.3" fill="none"/>'%ACC
    b+='<path d="M 210 76 l 14 -8 v 16 z" fill="%s" stroke="%s" stroke-width="1.3"/>'%(ACC,ACC)
    b+=lbl(268,66,"«extension»",9,ACC)
    b+=node(300,168,164,54,"«Service»  Order Svc","sla = 300 ms · tier = 1","acc",fs=11)
    b+='<path d="M 382 148 v -12" stroke="%s" stroke-width="1.3" stroke-dasharray="5 4" fill="none" marker-end="url(#mka)"/>'%ACC
    b+=note(478,150,138,["Every service box now","carries its SLA and tier","because the profile says","it must."])
    b+=txt(24,264,"The one UML diagram about UML itself: it defines the stereotypes your other diagrams may use.",10,MUTED)
    b+=txt(24,279,"Rarely drawn — but if your organisation mandates a modelling standard in a tool, this is where",10,MUTED)
    b+=txt(24,294,"that standard is written down.",10,MUTED)
    return svg(304,b)

# ---------- 3. Interaction & runtime ----------
def d_requestflow():
    b=""
    hops=[("Browser",None,24,"soft"),("CDN","cache miss",126,"plain"),("Gateway","authn",232,"plain"),
          ("Order API","handler",338,"acc"),("Cache","hit 82 %",444,"plain"),("DB","read",550,"plain")]
    for i,(n,s2,x,st) in enumerate(hops):
        w=90 if i<5 else 66
        b+=node(x,58,w,46,n,s2,st,fs=10.5)
        if i<len(hops)-1: b+=arr(x+w,81,hops[i+1][2]-2,81)
    budget=[("2 ms",120),("14 ms",226),("6 ms",332),("1 ms",438),("22 ms",544)]
    b+=txt(24,132,"LATENCY BUDGET  ·  p99 target 300 ms",9,ACC,"600")
    for t,x in budget:
        b+=txt(x,152,t,9.5,MUTED,"600","middle")
    b+='<line x1="24" y1="162" x2="616" y2="162" stroke="%s" stroke-width="1"/>'%LINE
    b+=node(24,180,180,44,"Total server time  ·  45 ms",None,"grn",fs=10.5)
    b+=node(220,180,190,44,"Network + TLS  ·  90 ms",None,"amb",fs=10.5)
    b+=node(426,180,190,44,"Render + assets  ·  120 ms",None,"amb",fs=10.5)
    b+=txt(24,258,"One request, every hop, and a number on each. Drawn this way the argument stops being “the API",10,MUTED)
    b+=txt(24,273,"feels slow” and becomes “85 % of the budget is spent before our code runs”.",10,MUTED)
    return svg(284,b)

def d_messageflow():
    b=""
    b+=node(24,40,140,52,"Order platform","publisher","acc",fs=11)
    b+=node(24,146,140,52,"Partner WMS","external","soft",fs=11)
    b+=node(250,93,140,52,"Message broker","topic per contract","amb",fs=11)
    b+=node(476,40,140,52,"Billing","filter: type = Order*",fs=11)
    b+=node(476,146,140,52,"Analytics","all events",fs=11)
    b+=arr(164,72,246,106,"OrderPlaced v3",lp=0.52,dy=-7,fs=9)
    b+=arr(164,166,246,132,"ShipmentDispatched",lp=0.52,dy=13,fs=9)
    b+=arr(390,106,472,72,None)
    b+=arr(390,132,472,166,None)
    b+=note(24,212,420,["Every arrow carries four things: message name and version, payload","format, delivery guarantee, and ordering scope. Leave any of the four","off and the diagram cannot be implemented without a meeting."])
    b+=txt(24,302,"Not a sequence diagram: there is no time axis and no request. It is the wiring list for who sends",10,MUTED)
    b+=txt(24,317,"what to whom, which is the thing that has to be agreed before either side writes code.",10,MUTED)
    return svg(328,b)

# ---------- 4. Data architecture ----------
def d_datamodels():
    b=""
    b+=frame(24,22,186,214,"conceptual  ·  business",MUTED)
    b+=node(48,54,138,40,"Customer",None,"acc",fs=11)
    b+=node(48,124,138,40,"Order",None,"acc",fs=11)
    b+=node(48,186,138,40,"Product",None,"acc",fs=11)
    b+=arr(117,94,117,122,"places",lp=0.5,dy=-3,fs=8.8)
    b+=arr(117,164,117,184,None)
    b+=frame(228,22,186,214,"logical  ·  normalised",MUTED)
    b+=classbox(248,52,146,["customer_id","email","tier"],"Customer")
    b+=classbox(248,140,146,["order_id","customer_id","placed_at"],"Order","acc")
    b+=arr(321,131,321,138,None,head=False); b+=lbl(348,132,"1 : N",8.8)
    b+=frame(432,22,184,214,"physical  ·  PostgreSQL",ACC)
    b+=classbox(452,52,146,["id  bigint PK","email  citext UK","tier  smallint"],"customer")
    b+=classbox(452,140,146,["id  bigint PK","customer_id  FK idx","placed_at  timestamptz"],"orders","acc")
    b+=arr(525,131,525,138,None,head=False)
    b+=txt(432,232,"partitioned monthly",8.8,MUTED)
    b+=txt(24,268,"Same domain, three audiences. Conceptual is for the business and fits on a napkin; logical is",10,MUTED)
    b+=txt(24,283,"vendor-neutral and is where normalisation arguments happen; physical carries types, indexes and",10,MUTED)
    b+=txt(24,298,"partitioning. Showing a physical model to stakeholders is the usual mistake.",10,MUTED)
    return svg(310,b)

def d_datapipeline():
    b=""
    b+=txt(24,24,"BATCH  ·  ELT, nightly",9,ACC,"600")
    st=[("Sources","CRM, ERP, files",24),("Ingest","Fivetran",158),("Raw","object storage",292),
        ("Transform","dbt models",426),("Serve","marts + BI",560)]
    for i,(n,s2,x) in enumerate(st):
        w=118 if i<4 else 56
        if i==2: b+=cyl(x,32,w,50,n,s2)
        else: b+=node(x,34,w,46,n,s2,"acc" if i==3 else "plain",fs=10.5)
        if i<len(st)-1: b+=arr(x+w,57,st[i+1][2]-2,57)
    b+='<line x1="24" y1="106" x2="616" y2="106" stroke="%s" stroke-width="1"/>'%LINE
    b+=txt(24,130,"STREAM  ·  CDC, seconds",9,AMB,"600")
    st2=[("Source DB","Postgres",24),("CDC","Debezium",158),("Kafka","topic per table",292),
         ("Stream job","Flink",426),("Serve",None,560)]
    for i,(n,s2,x) in enumerate(st2):
        w=118 if i<4 else 56
        if i==0: b+=cyl(x,138,w,50,n,s2)
        else: b+=node(x,140,w,46,n,s2,"amb" if i==2 else "plain",fs=10.5)
        if i<len(st2)-1: b+=arr(x+w,163,st2[i+1][2]-2,163)
    b+=node(24,216,286,40,"Contract test on ingest","schema + volume + freshness","grn",fs=10.5)
    b+=node(330,216,286,40,"Backfill path","replay from raw, idempotent","grn",fs=10.5)
    b+=poly([(146,80),(146,214)],color=GRN,dash=True)
    b+=poly([(414,80),(414,214)],color=GRN,dash=True)
    b+=txt(24,290,"Two questions decide the shape: how fresh must it be, and what happens on reprocessing? Land raw",10,MUTED)
    b+=txt(24,305,"data immutably first — every transform you regret is then a re-run rather than a lost dataset.",10,MUTED)
    return svg(316,b)

def d_warehouse():
    b=""
    cols=[("Sources",24,110,MUTED),("Staging",148,104,MUTED),("Core  ·  dimensional",276,214,ACC),
          ("Marts",504,112,GRN)]
    for t,x,w,c in cols: b+=band(x,24,w,196,t,c)
    b+=inode(34,60,90,32,"OLTP",None,"soft","db",fs=9.5,isize=12,pad=5)
    b+=inode(34,100,90,32,"SaaS",None,"soft","cloud",fs=9.5,isize=12,pad=5)
    b+=inode(34,140,90,32,"Files",None,"soft","log",fs=9.5,isize=12,pad=5)
    b+=inode(158,90,84,42,"1:1","no logic","plain","archive",fs=9.5,isize=12,pad=5)
    b+=inode(322,58,122,36,"DimProduct","SCD type 2","plain","container",fs=9.5,isize=12,pad=5)
    b+=inode(322,104,122,44,"FactOrders","grain: 1 line","acc","chart",fs=10)
    b+=inode(288,160,94,32,"DimCustomer",None,"plain","user",fs=9,isize=11,pad=4)
    b+=inode(392,160,94,32,"DimDate",None,"plain","clock",fs=9,isize=11,pad=4)
    b+=inode(514,60,92,34,"Finance",None,"grn","chart",fs=9.5,isize=12,pad=5)
    b+=inode(514,104,92,34,"Ops",None,"grn","chart",fs=9.5,isize=12,pad=5)
    b+=inode(514,148,92,34,"Product",None,"grn","chart",fs=9.5,isize=12,pad=5)
    b+=arr(124,116,156,112); b+=arr(242,111,286,116)
    b+=arr(383,94,383,102,None,head=False)
    b+=arr(335,160,360,148,None,head=False); b+=arr(439,160,414,148,None,head=False)
    b+=arr(444,122,512,110)
    b+=note(24,236,592,["State the grain of the fact table in words, on the diagram — “one row per order line per day”.","Nearly every warehouse dispute is two people assuming different grains, and both being right.","Mark how each dimension handles change too: type 1 overwrites, type 2 keeps a row per version."])
    b+=txt(24,318,"Staging holds the data exactly as it arrived. Business logic starts in core, never before it.",10,MUTED)
    return svg(330,b)

def d_lakehouse():
    b=""
    tiers=[("Bronze","raw, append-only, as-landed",34,"soft"),("Silver","cleaned, conformed, typed",118,"plain"),("Gold","business-ready aggregates",202,"acc")]
    for n,s2,y,st in tiers:
        b+=node(24,y,300,58,n,s2,st,fs=12)
        if y<202: b+=arr(174,y+58,174,y+80)
    b+=frame(356,24,260,236,"one storage layer  ·  open table format",ACC,dash=False)
    b+=node(376,58,220,40,"Parquet + Delta / Iceberg","ACID, time travel","acc",fs=10.5)
    b+=node(376,112,220,36,"Catalogue","schema + lineage + ACL",fs=10.5)
    b+=node(376,164,104,34,"SQL engine",None,fs=9.8)
    b+=node(492,164,104,34,"Spark",None,fs=9.8)
    b+=node(376,212,104,34,"BI",None,fs=9.8)
    b+=node(492,212,104,34,"ML training",None,fs=9.8)
    b+=arr(486,98,486,110); b+=arr(428,148,428,162); b+=arr(544,148,544,162)
    b+=arr(428,198,428,210); b+=arr(544,198,544,210)
    b+=arr(324,140,354,140,"one copy",dy=-5,fs=9)
    b+=txt(24,290,"The lakehouse claim is that the warehouse and the lake stop being two copies of the truth: one",10,MUTED)
    b+=txt(24,305,"set of files, transactional, queried by SQL and by ML. The tier names carry the promise about",10,MUTED)
    b+=txt(24,320,"quality — a Gold table that is sometimes wrong destroys the whole convention.",10,MUTED)
    return svg(332,b)

def d_datamesh():
    b=""
    for i,(n,x) in enumerate([("Orders domain",24),("Payments domain",236),("Logistics domain",448)]):
        b+=frame(x,60,168,132,n,ACC if i==0 else MUTED,dash=False)
        b+=node(x+16,88,136,40,"Data product","versioned, SLO’d","acc" if i==0 else "plain",fs=10)
        b+=node(x+16,140,136,36,"Owned by that team",None,"soft",fs=9.5)
    b+=node(24,16,592,30,"Federated governance  ·  global rules: identity, PII, interop",None,"amb",fs=10.5)
    b+=node(24,210,592,40,"Self-serve data platform  ·  storage, pipelines, catalogue, access, observability",None,"grn",fs=10.5)
    for x in (108,320,532):
        b+=arr(x,46,x,86,None,AMB,dash=True)
        b+=arr(x,208,x,178,None,GRN,dash=True)
    b+=arr(194,108,234,108,None); b+=arr(406,108,446,108,None)
    b+=txt(24,282,"Four ideas, and the diagram fails if any is missing: domain ownership, data as a product with an",10,MUTED)
    b+=txt(24,297,"SLO, a self-serve platform, and federated governance. Without the bottom two bands this is just",10,MUTED)
    b+=txt(24,312,"a data warehouse nobody is responsible for.",10,MUTED)
    return svg(324,b)

def d_streaming():
    b=""
    b+=node(24,60,110,46,"Producers","apps, CDC, IoT","soft",fs=10.5)
    b+=node(154,60,132,46,"Kafka","key = deviceId · 12 parts","amb",fs=11)
    b+=frame(306,26,310,150,"stream processing  ·  Flink",ACC,dash=False)
    b+=node(324,54,124,38,"Filter / map","stateless",fs=10)
    b+=node(468,54,132,38,"Window","5 min tumbling + grace","acc",fs=10)
    b+=node(324,110,124,38,"Join","stream ⋈ table",fs=10)
    b+=node(468,110,132,38,"State store","RocksDB + ckpt",fs=10)
    b+=arr(448,73,466,73); b+=arr(386,92,386,108); b+=arr(448,129,466,129)
    b+=arr(134,83,152,83); b+=arr(286,83,304,83)
    b+=node(24,200,180,40,"Serving store","low-latency reads",fs=10.5)
    b+=node(228,200,180,40,"Warehouse","same events, batch",fs=10.5)
    b+=node(432,200,184,40,"Alerts / actions","sub-second","grn",fs=10.5)
    b+=poly([(386,176),(386,190),(114,190),(114,198)],color=MUTED)
    b+=poly([(386,190),(318,190),(318,198)],color=MUTED)
    b+=poly([(386,190),(524,190),(524,198)],color=MUTED)
    b+=note(24,116,262,["late arrivals: 2 min grace, then routed","to a side output and reconciled in the","batch path — never silently dropped"],AMB)
    b+=txt(24,272,"Three things make it a design rather than a picture, and all three are on the plate: the partition",10,MUTED)
    b+=txt(24,287,"key (which fixes what is ordered and what parallelises), the window definition, and what happens",10,MUTED)
    b+=txt(24,302,"to an event that arrives late. A box labelled “Kafka” states none of them.",10,MUTED)
    return svg(314,b)

# ---------- 5. Deployment & infrastructure ----------
def d_k8s():
    b=frame(24,20,592,246,"cluster",ACC)
    b+=frame(44,48,232,206,"control plane  ·  3 nodes",ACC,dash=False)
    b+=inode(60,74,200,40,"kube-apiserver","the only writer","acc","gear",fs=10)
    b+=inode(60,122,200,40,"etcd","quorum of 3","plain","db",fs=10)
    b+=inode(60,170,200,34,"scheduler",None,"plain","clock",fs=10)
    b+=inode(60,212,200,34,"controller-manager",None,"plain","sync",fs=10)
    b+=frame(296,48,320,206,"worker nodes")
    b+=inode(312,72,140,28,"kubelet",None,"soft","server",fs=9.5,isize=13,pad=6)
    b+=inode(462,72,140,28,"kubelet",None,"soft","server",fs=9.5,isize=13,pad=6)
    b+=frame(312,110,140,88,"node-1")
    b+=inode(322,128,120,26,"order-svc",None,"plain","container",fs=9,isize=12,pad=5)
    b+=inode(322,160,120,26,"order-svc",None,"plain","container",fs=9,isize=12,pad=5)
    b+=frame(462,110,140,88,"node-2")
    b+=inode(472,128,120,26,"payment",None,"plain","container",fs=9,isize=12,pad=5)
    b+=inode(472,160,120,26,"order-svc",None,"plain","container",fs=9,isize=12,pad=5)
    b+=inode(312,210,290,38,"Service  ·  stable VIP","selector app=order-svc","grn","balancer",fs=9.8)
    # the kubelet watches the API server, not the other way round — and reports back.
    # Those two arrows are the reconciliation loop.
    b+=arr(310,86,278,86,"watches",dy=-6,fs=8.4)
    b+=arr(278,104,310,104,"status",dy=11,fs=8.4)
    b+=arr(382,198,382,208,None,GRN); b+=arr(532,198,532,208,None,GRN)
    b+=inode(180,0,142,22,"Ingress",None,"soft","globe",fs=9.5,isize=12,pad=5)
    b+=poly([(251,22),(251,36),(457,36),(457,206)],color=MUTED,dash=True)
    b+=txt(24,296,"The mental model worth carrying is a loop, and both of its arrows are drawn: you write desired",10,MUTED)
    b+=txt(24,311,"state to the API server, the kubelet watches for what it has been assigned and reports back what",10,MUTED)
    b+=txt(24,326,"is really running. Nothing is “deployed” — it is declared, and the gap is closed continuously.",10,MUTED)
    return svg(338,b)

def d_multiregion():
    b=""
    b+=inode(225,16,190,40,"Global routing","latency or geo based","acc","globe",fs=11)
    b+=frame(24,80,250,160,"eu-west-1  ·  active",GRN,dash=False)
    b+=frame(366,80,250,160,"us-east-1  ·  active",GRN,dash=False)
    b+=inode(44,106,210,38,"App  ·  60 % traffic",None,"grn","server",fs=10.5)
    b+=inode(386,106,210,38,"App  ·  40 % traffic",None,"grn","server",fs=10.5)
    b+=cyl(44,160,210,54,"Writer","EU customers only","acc")
    b+=cyl(386,160,210,54,"Writer","US customers only","acc")
    b+=poly([(280,56),(149,56),(149,104)],color=GRN,label="eu users",lx=196,ly=50,fs=9)
    b+=poly([(360,56),(491,56),(491,104)],color=GRN,label="us users",lx=444,ly=50,fs=9)
    b+=arr(149,144,149,158); b+=arr(491,144,491,158)
    b+=arr(254,187,384,187,None,AMB,dash=True)
    b+=lbl(319,180,"replication",9,AMB); b+=lbl(319,204,"lag ≈ 300 ms",9,AMB)
    b+=txt(24,268,"Nothing crosses the gap on the request path — only replication does. Multi-region forces one",10,MUTED)
    b+=txt(24,283,"decision before any diagram is useful: is data partitioned by region (each row has one home, no",10,MUTED)
    b+=txt(24,298,"conflicts) or replicated everywhere (fast reads, and a conflict-resolution rule you must write",10,MUTED)
    b+=txt(24,313,"down)? Everything else follows from that answer.",10,MUTED)
    return svg(325,b)

def d_ha():
    b=""
    b+=inode(225,16,190,40,"Load balancer","health checks, 5 s","acc","balancer",fs=11)
    b+=frame(24,80,190,124,"AZ a",MUTED)
    b+=frame(226,80,190,124,"AZ b",MUTED)
    b+=frame(428,80,188,124,"AZ c",MUTED)
    # the utilisation number is the whole argument, so it goes on the plate
    for x,st,cap,ic in [(44,"grn","45 % utilised","server"),(246,"grn","45 % utilised","server"),
                        (448,"grn","45 % utilised","server")]:
        b+=inode(x,106,150,40,"App × 2",None,st,ic,fs=10.5)
        b+=node(x,158,150,32,cap,None,"soft",fs=9.2)
    b+=poly([(280,56),(119,56),(119,104)],color=MUTED)
    b+=arr(320,56,320,104)
    b+=poly([(360,56),(521,56),(521,104)],color=MUTED)
    b+=inode(24,226,286,44,"Lose one AZ → 68 %","3 × 45 % over 2 AZs — still serving","grn","check",fs=10.5)
    b+=inode(330,226,286,44,"Quorum data  ·  3 nodes","survives one loss, still writable","grn","db",fs=10.5)
    b+=note(24,286,592,["Redraw this at 70 % per AZ and the identical topology fails: losing one leaves the two","survivors needing 105 %. Same boxes, same arrows, different outcome — which is exactly why","the utilisation number belongs on the diagram and not in the paragraph underneath it."],FLAG)
    b+=txt(24,366,"High availability is arithmetic, not a topology. Put the number on the plate and the sizing",10,MUTED)
    b+=txt(24,381,"argument settles itself before anyone opens a spreadsheet.",10,MUTED)
    return svg(393,b)

def d_containerarch():
    b=""
    b+=inode(24,50,140,44,"Dockerfile","pinned base","plain","log",fs=10.5)
    b+=inode(180,50,140,44,"Build","no secrets","plain","gear",fs=10.5)
    b+=inode(336,50,140,44,"Registry","by digest","acc","archive",fs=10.5)
    b+=inode(492,50,124,44,"Runtime","non-root","grn","container",fs=10.5)
    b+=arr(164,72,178,72); b+=arr(320,72,334,72); b+=arr(476,72,490,72)
    b+=frame(24,124,290,124,"image layers  ·  cached top-down",MUTED)
    b+=inode(40,150,258,26,"distroless base","patched weekly","soft","shield",fs=9,isize=12,pad=5)
    b+=inode(40,182,258,26,"runtime deps","changes rarely","soft","archive",fs=9,isize=12,pad=5)
    b+=inode(40,214,258,26,"application","every build","acc","container",fs=9,isize=12,pad=5)
    b+=note(340,130,276,["Tag with the digest, not “latest”.","A tag can be moved; a digest cannot,","so only a digest answers “what is","actually running in production?”"])
    b+=txt(24,282,"The architectural content is the base image policy: who owns it, how often it is patched, and how a",10,MUTED)
    b+=txt(24,297,"CVE fix reaches every service without forty teams each rebuilding by hand.",10,MUTED)
    return svg(308,b)

# ---------- 6. Security ----------
def d_threat():
    b=""
    b+=inode(24,44,124,44,"Browser",None,"soft","globe",fs=10.5)
    b+=inode(196,44,140,44,"API gateway",None,"acc","shield",fs=10.5)
    b+=inode(376,44,132,44,"Order Svc",None,"acc","server",fs=10.5)
    b+=cyl(540,38,76,54,"DB",None,"acc")
    b+='<line x1="172" y1="20" x2="172" y2="112" stroke="%s" stroke-width="1.3" stroke-dasharray="6 5"/>'%FLAG
    b+=txt(172,14,"trust boundary",9,FLAG,"600","middle")
    b+='<line x1="356" y1="20" x2="356" y2="112" stroke="%s" stroke-width="1.3" stroke-dasharray="6 5"/>'%FLAG
    b+=txt(356,14,"trust boundary",9,FLAG,"600","middle")
    b+=arr(148,66,194,66,"1",dy=-5,fs=9,color=FLAG)
    b+=arr(336,66,374,66,"2",dy=-5,fs=9,color=FLAG)
    b+=arr(508,66,538,66,"3",dy=-5,fs=9,color=FLAG)
    # all six letters — a STRIDE table missing one is a STRIDE table that skipped a question
    rows=[["1","Spoofing","Forged JWT","Verify sig + iss + aud"],
          ["2","Tampering","Header injection","Strip and re-issue identity"],
          ["2","Repudiation","No audit of who acted","Signed audit log"],
          ["3","Info disclosure","Cross-tenant read","Tenant filter in the query"],
          ["1","Denial of service","Unbounded page size","Cap + rate limit per key"],
          ["3","Elevation of privilege","Service account is db_owner","Per-service role, least privilege"]]
    ico=[("id",FLAG),("warn",FLAG),("log",FLAG),("eye",FLAG),("bolt",FLAG),("key",FLAG)]
    b+=grid(24,130,592,["Flow","STRIDE category","Threat","Mitigation — and where it lives"],rows,
            [0,0.13,0.35,0.60],rh=26,hh=27,rowicons=ico)
    b+=txt(24,336,"The diagram is only the canvas. The work is walking each numbered flow through all six STRIDE",10,MUTED)
    b+=txt(24,351,"categories and writing a mitigation with an owner. An unmitigated row is an accepted risk —",10,MUTED)
    b+=txt(24,366,"which is fine, as long as somebody senior has actually accepted it in writing.",10,MUTED)
    return svg(378,b)

def d_zerotrust():
    b=""
    b+=txt(24,16,"SIGNALS  ·  evaluated per request, not per session",9,ACC,"600")
    sig=[("Identity",24,140,"id"),("Device posture",178,140,"lock"),
         ("Data sensitivity",332,140,"archive"),("Behaviour risk",486,130,"pulse")]
    for n,x,w,ic in sig:
        b+=inode(x,24,w,32,n,None,"plain",ic,fs=10,isize=14,pad=8)
        b+=arr(x+w/2.0,56,x+w/2.0,70,None,MUTED,dash=True,head=False)
    b+='<line x1="94" y1="70" x2="551" y2="70" stroke="%s" stroke-width="1.2" stroke-dasharray="5 4"/>'%MUTED
    b+=poly([(178,70),(178,220),(192,220)],color=MUTED,dash=True)
    b+=inode(24,110,140,52,"User / workload","no implicit trust","soft","user",fs=10.5)
    b+=inode(196,104,150,60,"Policy enforcement","PEP — inline","acc","shield",fs=10.5)
    b+=inode(196,196,150,48,"Policy decision","PDP — OPA / Cedar","acc","gear",fs=10.5)
    b+=inode(388,110,228,48,"Resource","authenticated and authorised","grn","lock",fs=10.5)
    b+=arr(164,136,194,134)
    b+=arr(240,164,240,194,"ask",lp=0.5,dy=-3,fs=9)
    b+=poly([(302,194),(302,166)],color=ACC,dash=True)
    b+=txt(312,184,"allow / deny  +  TTL",8.8,ACC,"600")
    b+=arr(346,134,386,134,"forwarded",lp=0.5,dy=-5,fs=8.6)
    b+=txt(24,282,"Zero trust is one sentence: never trust the network, always verify, per request. What makes it real",10,MUTED)
    b+=txt(24,297,"on a diagram is the decision point being consulted on every call — not a VPN at the edge and free",10,MUTED)
    b+=txt(24,312,"movement behind it. Show the signals, and show the TTL on the cached answer.",10,MUTED)
    return svg(324,b)

def d_identity():
    b=""
    b+=inode(24,60,140,50,"Workforce","Entra ID","soft","user",fs=10.5)
    b+=inode(24,132,140,50,"Customers","CIAM tenant","soft","user",fs=10.5)
    b+=inode(196,88,150,66,"Identity provider","OIDC + SAML · MFA","acc","key",fs=11)
    b+=inode(394,26,110,38,"Directory",None,"plain","db",fs=10,isize=14,pad=7)
    b+=inode(516,26,100,38,"SCIM",None,"plain","sync",fs=10,isize=14,pad=7)
    b+=inode(394,84,222,40,"Token service","15 min · aud per API","acc","token",fs=10.5)
    b+=inode(394,142,110,38,"Sessions",None,"plain","clock",fs=10,isize=14,pad=7)
    b+=inode(516,142,100,38,"Break-glass",None,"plain","warn",fs=10,isize=14,pad=7)
    b+=inode(196,196,420,40,"Joiner / mover / leaver — deprovisioning is the tested control",None,"amb","check",fs=10.5)
    b+=arr(164,85,194,105); b+=arr(164,157,194,140)
    b+=arr(346,104,392,50); b+=arr(346,110,392,104); b+=arr(346,132,392,158)
    b+=arr(504,45,514,45)
    b+=arr(266,154,266,194,None,AMB)
    b+=txt(24,270,"Authentication is the easy half. The parts that fail audits are on the bottom row: what happens the",10,MUTED)
    b+=txt(24,285,"hour someone leaves, and who can use the emergency account without anyone noticing.",10,MUTED)
    return svg(296,b)

def d_authz():
    b=""
    b+=inode(24,54,124,46,"Caller","token + claims","soft","user",fs=10.5)
    b+=inode(178,54,132,46,"PEP","in the service","acc","shield",fs=10.5)
    b+=inode(178,140,132,46,"PDP","policy engine","acc","gear",fs=10.5)
    b+=inode(350,24,266,28,"RBAC   role → permission",None,"plain","id",fs=9.5,isize=13,pad=7)
    b+=inode(350,60,266,28,"ABAC   tenant, region, amount",None,"plain","funnel",fs=9.5,isize=13,pad=7)
    b+=inode(350,96,266,28,"ReBAC   “is manager of”",None,"plain","network",fs=9.5,isize=13,pad=7)
    b+=inode(350,144,266,38,"Allow, with obligations","log it, mask fields, expire in 60 s","grn","check",fs=10)
    b+=arr(148,77,176,77); b+=arr(244,100,244,138,"ask",lp=0.5,dy=-2,fs=9)
    b+=arr(310,158,348,158,None,GRN)
    b+=poly([(310,150),(330,150),(330,38),(348,38)],color=MUTED,dash=True)
    b+=poly([(330,74),(348,74)],color=MUTED,dash=True)
    b+=poly([(330,110),(348,110)],color=MUTED,dash=True)
    b+=note(24,140,132,["Authentication ≠","authorisation. The","gateway proves who;","the service decides","what."],FLAG)
    b+=txt(24,268,"Draw the row your codebase actually implements. Most estates start RBAC, grow one ABAC rule",10,MUTED)
    b+=txt(24,283,"per quarter as if-statements scattered across services, and discover too late that no one can",10,MUTED)
    b+=txt(24,298,"answer “who can see this record?”. Centralise the decision; keep enforcement local.",10,MUTED)
    return svg(310,b)

def d_classification():
    b=""
    rows=[["Public","Marketing pages","None required","Any region","Indefinite"],
          ["Internal","Runbooks, dashboards","SSO","Any region","3 years"],
          ["Confidential","Customer PII","SSO + MFA, field encryption","EU only","7 y, then purge"],
          ["Restricted","Card data, health","Tokenised, break-glass access","EU, PCI scope","As law requires"]]
    def cc(r,i,v):
        if i==0: return [MUTED,INK,ACC,FLAG][r]
        return MUTED
    ico=[("globe",MUTED),("id",INK),("lock",ACC),("shield",FLAG)]
    b+=grid(24,28,592,["Class","Example","Access control","Residency","Retention"],rows,
            [0,0.22,0.40,0.68,0.86],rh=32,hh=30,cellcolor=cc,rowicons=ico)
    b+=inode(24,196,286,44,"Tag at creation","the only moment the author knows","grn","check",fs=10.5)
    b+=inode(330,196,286,44,"Propagate through pipelines","class travels with the column","grn","sync",fs=10.5)
    b+=arr(310,218,328,218,None,GRN)
    b+=txt(24,276,"Four classes is about the limit people will actually apply; seven becomes “internal” for everything.",10,MUTED)
    b+=txt(24,291,"The diagram earns its place when each row names a concrete control, so an engineer can read off",10,MUTED)
    b+=txt(24,306,"what to build rather than asking legal what “confidential” implies this week.",10,MUTED)
    return svg(318,b)

def d_keymgmt():
    b=""
    b+=inode(24,44,150,52,"KMS / HSM","root key never leaves","acc","lock",fs=11)
    b+=inode(212,44,150,52,"Key-encrypting key","per tenant, yearly","acc","key",fs=10.5)
    b+=inode(400,44,216,52,"Data-encrypting key","per object, rotated per write","plain","key",fs=10.5)
    b+=arr(174,70,210,70,"wraps",dy=-5,fs=9)
    b+=arr(362,70,398,70,"wraps",dy=-5,fs=9)
    b+=cyl(400,130,216,52,"Ciphertext + wrapped DEK","stored together")
    b+=arr(508,96,508,128)
    b+=inode(24,130,150,52,"Application","never sees the KEK","soft","server",fs=10.5)
    b+=poly([(99,96),(99,128)],color=MUTED)
    b+=arr(174,156,398,156,"decrypt(wrapped DEK) → plaintext DEK, in memory only",lp=0.5,dy=-6,fs=8.8,color=ACC)
    b+=inode(24,212,286,44,"Rotation = re-wrap the DEKs","no bulk re-encryption of data","grn","sync",fs=10.5)
    b+=inode(330,212,286,44,"Deletion = destroy the KEK","crypto-shredding, provable","grn","check",fs=10.5)
    b+=txt(24,292,"Envelope encryption is worth drawing because it makes two operations cheap that are otherwise",10,MUTED)
    b+=txt(24,307,"ruinous: rotating a key without rewriting a petabyte, and proving a tenant’s data is unrecoverable",10,MUTED)
    b+=txt(24,322,"after they leave. Both are contractual commitments someone has probably already signed.",10,MUTED)
    return svg(334,b)

# ---------- 7. Business & domain ----------
def d_domainmodel():
    b=frame(24,22,364,242,"Order  ·  aggregate",ACC,dash=False)
    b+=classbox(48,54,180,["+ id : OrderId","+ status : OrderStatus","+ place() / cancel()","— invariant: ≥ 1 line","— invariant: total ≤ limit"],"Order  «root»","acc")
    b+=classbox(252,54,120,["+ productId","+ qty : int"],"OrderLine")
    b+=classbox(252,164,120,["+ amount","+ currency"],"Money  «VO»","soft")
    b+=classbox(48,196,180,["+ street / city / post"],"Address  «VO»","soft")
    b+=arr(228,86,250,86,None,head=False); b+=lbl(239,80,"1..*",8.8)
    b+=poly([(138,196),(138,165)],color=MUTED,head=False)
    b+=poly([(312,118),(312,162)],color=MUTED,head=False)
    b+=node(430,54,186,50,"Customer  «root»","different aggregate",fs=10.5)
    b+=node(430,124,186,50,"Product  «root»","different aggregate",fs=10.5)
    b+=arr(388,79,428,79,"by id only",lp=0.5,dy=-5,fs=8.8)
    b+=arr(388,140,428,145,"by id only",lp=0.5,dy=12,fs=8.8)
    b+=note(430,196,186,["One transaction","= one aggregate.","Across aggregates:","events, eventually."])
    b+=txt(24,296,"The two decisions this diagram exists to record: where the consistency boundary is drawn, and",10,MUTED)
    b+=txt(24,311,"which invariants the root enforces. Entities have identity and a lifecycle; value objects are",10,MUTED)
    b+=txt(24,326,"compared by value and replaced wholesale. An anaemic box of getters is not a domain model.",10,MUTED)
    return svg(338,b)

def d_capability():
    b=""
    b+=txt(24,22,"LEVEL 1",9,MUTED,"600")
    for n,x,w in [("Market & sell",24,190),("Fulfil",228,190),("Serve & retain",432,184)]:
        b+=node(x,30,w,38,n,None,"acc",fs=11.5)
    b+=txt(24,92,"LEVEL 2  ·  shaded by maturity, not by team",9,MUTED,"600")
    l2=[("Campaigns",24,"grn"),("Pricing",118,"flag"),("Catalogue",212,"grn"),("Order capture",306,"amb"),
        ("Warehouse",400,"grn"),("Delivery",494,"amb"),("Returns",24,"flag"),("Support",118,"amb"),
        ("Loyalty",212,"soft"),("Billing",306,"grn"),("Disputes",400,"flag"),("Insight",494,"soft")]
    for i,(n,x,st) in enumerate(l2):
        y=100 if i<6 else 146
        b+=node(x,y,92,38,n,None,st,fs=9.6)
    b+=txt(24,212,"weak — invest",9,FLAG,"600")
    b+=txt(150,212,"adequate",9,AMB,"600")
    b+=txt(260,212,"strong",9,GRN,"600")
    b+=txt(360,212,"not needed",9,MUTED,"600")
    b+=txt(24,248,"Capabilities are what the business does, and they barely change; systems and org charts churn",10,MUTED)
    b+=txt(24,263,"constantly. Colour by how well each is served today and the investment conversation writes",10,MUTED)
    b+=txt(24,278,"itself — three red boxes are three funded programmes, and everything else can wait.",10,MUTED)
    return svg(290,b)

def d_valuestream():
    b=""
    st=[("Submit","customer",24),("Triage","support",148),("Approve","manager",272),("Ship label","system",396),("Refund","finance",520)]
    for i,(n,who,x) in enumerate(st):
        b+=node(x,54,96,46,n,who,"acc" if i in (1,4) else "plain",fs=10.5)
        if i<len(st)-1:
            b+='<path d="M %g 77 h 28" stroke="%s" stroke-width="1.4" marker-end="url(#mkm)"/>'%(x+96,MUTED)
    b+=txt(24,128,"PROCESS TIME  ·  work actually happening",9,GRN,"600")
    for t,x in [("4 min",72),("6 min",196),("2 min",320),("instant",444),("3 min",568)]:
        b+=txt(x,148,t,9.5,GRN,"600","middle")
    b+=txt(24,176,"WAIT TIME  ·  queue before the step",9,FLAG,"600")
    for t,x in [("—",72),("9 h",196),("2 d",320),("—",444),("4 d",568)]:
        b+=txt(x,196,t,9.5,FLAG,"600","middle")
    b+='<line x1="24" y1="212" x2="616" y2="212" stroke="%s" stroke-width="1"/>'%LINE
    b+=node(24,228,286,46,"Lead time  ·  6.4 days",None,"flag",fs=11.5)
    b+=node(330,228,286,46,"Process time  ·  15 minutes",None,"grn",fs=11.5)
    b+=txt(24,306,"Efficiency here is 0.2 %. That is normal, and it is the whole point: optimising the fifteen minutes",10,MUTED)
    b+=txt(24,321,"of work is worthless while six days are spent in queues. Automating approval beats making",10,MUTED)
    b+=txt(24,336,"approval faster — which is an architecture decision hiding inside a process map.",10,MUTED)
    return svg(348,b)

# ---------- 8. Event-driven ----------
def d_eventsourcing():
    b=""
    b+=node(24,50,116,44,"Command","PlaceOrder","acc",fs=10.5)
    b+=node(158,50,120,44,"Aggregate","rehydrated",fs=10.5)
    b+=arr(140,72,156,72)
    b+=frame(300,20,316,124,"event store  ·  append-only",ACC,dash=False)
    ev=[("1  OrderPlaced",46),("2  ItemAdded",76),("3  PaymentTaken",106)]
    for t,y in ev:
        b+=node(316,y,284,24,t,None,"amb",fs=9.5)
    b+=arr(278,72,298,72,"append",dy=-5,fs=9,color=AMB)
    b+=poly([(458,144),(458,164),(218,164),(218,96)],color=MUTED,dash=True,label="replay to rebuild state",lx=340,ly=178,fs=9)
    b+=node(24,196,178,44,"Snapshot at n = 200","an optimisation, not truth","soft",fs=10)
    b+=node(220,196,186,44,"Projection  ·  read model","rebuildable from zero","grn",fs=10)
    b+=node(424,196,192,44,"Audit / time travel","state as at any instant","grn",fs=10)
    b+=arr(202,218,218,218,None); b+=arr(406,218,422,218,None)
    b+=txt(24,278,"The log is the system of record; current state is a fold over it. That buys perfect audit and the",10,MUTED)
    b+=txt(24,293,"ability to build a read model you had not thought of yet. It costs you schema evolution forever:",10,MUTED)
    b+=txt(24,308,"you can never delete an old event shape, and “fix the data” means writing a correcting event.",10,MUTED)
    return svg(320,b)

def d_kafka():
    b=""
    b+=inode(24,48,120,44,"Producer","key = orderId","acc","server",fs=10.5)
    # six partitions claimed, six partitions drawn — the count is the whole argument
    b+=band(166,20,450,186,"topic  orders.v1  ·  6 partitions  ·  RF 3",AMB,fs=10)
    for j in range(6):
        y=46+j*24
        b+=node(180,y,44,20,"P%d"%j,None,"amb",fs=8.6)
        b+='<rect x="232" y="%g" width="372" height="20" rx="3" fill="#FFFFFF" stroke="%s" stroke-width="1.2"/>'%(y,LINE)
        for i in range(8):
            b+='<rect x="%g" y="%g" width="38" height="12" rx="2" fill="%s" stroke="%s" stroke-width="1"/>'%(
                238+i*45, y+4, AMB_S, AMB)
            b+=txt(257+i*45, y+13, str(i), 7.6, AMB, "600", "middle")
    b+=txt(420,200,"offsets — ordered within a partition, never across them",8.6,MUTED,anchor="middle")
    b+=arr(144,70,164,64,"hash(key)",lp=0.5,dy=-7,fs=8.4)
    b+=band(24,234,286,96,"consumer group  billing",GRN,fs=10)
    b+=inode(36,266,124,30,"instance 1","P0, P1, P2","grn","server",fs=9.2,isize=12,pad=5)
    b+=inode(172,266,126,30,"instance 2","P3, P4, P5","grn","server",fs=9.2,isize=12,pad=5)
    b+=txt(167,316,"own offset per partition · scales to 6 instances",8.8,MUTED,anchor="middle")
    b+=band(330,234,286,96,"consumer group  analytics",VIO,fs=10)
    b+=inode(342,266,262,30,"instance 1","all 6 partitions, own offsets","vio","server",fs=9.2,isize=12,pad=5)
    b+=txt(473,316,"reads the same events, independently",8.8,MUTED,anchor="middle")
    b+=poly([(300,206),(300,222),(167,222),(167,232)],color=AMB)
    b+=poly([(300,222),(473,222),(473,232)],color=AMB)
    b+=txt(24,356,"Three facts do all the work: ordering is per partition, the key chooses the partition, and one",10,MUTED)
    b+=txt(24,371,"partition goes to one consumer per group. Partition count is therefore your maximum parallelism —",10,MUTED)
    b+=txt(24,386,"six here, so a seventh billing instance would sit idle. Any two events that must stay in order",10,MUTED)
    b+=txt(24,401,"have to share a key. Choose the key deliberately; it is the hardest thing here to change later.",10,MUTED)
    return svg(413,b)

def d_outbox():
    b=frame(24,24,318,148,"one local transaction",ACC,dash=False)
    b+=node(46,54,128,44,"Handler","business logic","acc",fs=10.5)
    b+=cyl(46,116,128,46,"orders","row written")
    b+=cyl(200,116,124,46,"outbox","event row","amb")
    b+=arr(110,98,110,114); b+=poly([(174,76),(262,76),(262,114)],color=MUTED)
    b+=node(382,54,110,44,"Relay","poll or CDC",fs=10.5)
    b+=node(516,54,100,44,"Broker",None,"amb",fs=10.5)
    b+=arr(324,139,380,90,"reads unsent",lp=0.62,dy=-6,fs=8.8)
    b+=arr(492,76,514,76,"publish",dy=-9,fs=9,color=AMB)
    b+=poly([(566,98),(566,150),(324,150)],color=AMB,dash=True,label="mark sent",lx=452,ly=144,fs=9)
    b+=node(24,182,592,42,"At-least-once delivery  ·  consumers must be idempotent",None,"grn",fs=10.5)
    b+=txt(24,256,"Solves exactly one problem, and it is a common one: you cannot atomically write to your database",10,MUTED)
    b+=txt(24,271,"and publish to a broker. Without the outbox, a crash between the two leaves either an order",10,MUTED)
    b+=txt(24,286,"nobody hears about or an event for an order that does not exist. Both are worse than a duplicate.",10,MUTED)
    return svg(298,b)

def d_pubsub():
    b=""
    # the subscription sits BETWEEN topic and consumer — it is the thing that owns the
    # filter, the delivery guarantee and the dead-letter destination
    b+=node(24,84,130,48,"Publisher","knows no subscribers","acc",fs=10.5)
    b+=node(178,84,116,48,"Topic","orders.events","amb",fs=11)
    b+=arr(154,108,176,108)
    subs=[("billing-sub","filter: type = Placed",20,"Billing"),
          ("search-sub","no filter",92,"Search index"),
          ("fraud-sub","filter: amount > 1k",164,"Fraud")]
    for sname,f,y,cons in subs:
        b+=node(330,y,150,44,sname,f,"soft",fs=9.6)
        b+=node(506,y+2,110,40,cons,None,"plain",fs=10)
        b+=arr(294,108,328,y+22,None,AMB)
        b+=arr(480,y+22,504,y+22)
    b+=node(178,176,116,44,"DLQ","after 5 attempts","flag",fs=10)
    b+=poly([(330,196),(296,198)],color=FLAG,dash=True,label="poison",lx=320,ly=218,fs=8.8)
    b+=txt(330,236,"each subscription: its own filter, guarantee and DLQ",9,MUTED)
    b+=txt(24,266,"The difference from a queue is the fan-out: a queue delivers each message to one consumer, a",10,MUTED)
    b+=txt(24,281,"topic delivers to every subscription. Drawing the subscription as its own box is what makes the",10,MUTED)
    b+=txt(24,296,"filter and the dead-letter route visible. Adding a fourth must cost the publisher nothing — the",10,MUTED)
    b+=txt(24,311,"moment the publisher needs changing, you have point-to-point integration wearing a topic.",10,MUTED)
    return svg(323,b)

# ---------- 9. Integration & API ----------
def d_integration():
    b=""
    b+=txt(24,22,"POINT TO POINT  ·  n systems, up to n(n−1)/2 links",9,FLAG,"600")
    pts=[(70,58),(190,44),(300,74),(150,110),(266,120)]
    for i,(x,y) in enumerate(pts):
        for j,(x2,y2) in enumerate(pts):
            if j>i: b+='<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="1"/>'%(x+30,y+13,x2+30,y2+13,FLAG)
    for i,(x,y) in enumerate(pts):
        b+=node(x,y,60,26,chr(65+i),None,"soft",fs=10)
    b+='<line x1="352" y1="20" x2="352" y2="186" stroke="%s" stroke-width="1"/>'%LINE
    b+=txt(384,22,"MEDIATED  ·  one contract each",9,GRN,"600")
    b+=node(460,74,120,40,"Integration hub","canonical events","grn",fs=10)
    # five spokes, not four — the comparison is only an argument if both sides
    # are the same estate
    hub=[(390,34,425,62,492,72),(560,34,595,62,548,72),
         (390,128,425,128,492,116),(560,128,595,128,548,116),
         (485,150,520,148,520,116)]
    for i,(x,y,sx,sy,tx,ty) in enumerate(hub):
        b+=node(x,y,70,28,chr(65+i),None,"soft",fs=10)
        b+=arr(sx,sy,tx,ty,None,GRN)
    b+=txt(24,196,"the same 5 systems — 10 links, 10 formats, 10 owners",9,MUTED)
    b+=txt(384,196,"5 contracts, one format, one owner",9,MUTED)
    b+=node(24,212,286,44,"Buy vs build vs point-to-point","the actual decision on this page","acc",fs=10.5)
    b+=node(330,212,286,44,"Sync or async per link","and the retry story for each","acc",fs=10.5)
    b+=txt(24,292,"The hub is not automatically right — it centralises change, so it becomes a queue of other teams’",10,MUTED)
    b+=txt(24,307,"work. Below roughly six systems, point-to-point with good contracts wins. Above it, the count of",10,MUTED)
    b+=txt(24,322,"pairwise links is what kills you, and that is the number to put on the diagram.",10,MUTED)
    return svg(334,b)

def d_esb():
    b=""
    b+=node(24,44,116,44,"SAP","IDoc","soft",fs=10.5)
    b+=node(24,112,116,44,"Mainframe","fixed-width","soft",fs=10.5)
    b+=node(24,180,116,44,"SaaS CRM","REST","soft",fs=10.5)
    b+=frame(180,24,268,220,"enterprise service bus",ACC,dash=False)
    b+=node(196,52,236,32,"Adapters  ·  protocol in / out",None,"plain",fs=10)
    b+=node(196,94,236,32,"Transform  ·  to canonical model",None,"acc",fs=10)
    b+=node(196,136,236,32,"Route  ·  content-based",None,"plain",fs=10)
    b+=node(196,178,236,32,"Orchestrate  ·  multi-step, stateful",None,"plain",fs=10)
    b+=node(196,214,236,22,"Audit + replay",None,"soft",fs=9.2)
    b+=arr(140,66,194,66); b+=arr(140,134,194,110); b+=arr(140,202,194,190)
    b+=node(488,60,128,44,"Order platform",None,fs=10.5)
    b+=node(488,128,128,44,"Warehouse",None,fs=10.5)
    b+=node(488,196,128,44,"Partner EDI",None,"soft",fs=10.5)
    b+=arr(448,82,486,82); b+=arr(448,150,486,150); b+=arr(448,210,486,218)
    b+=txt(24,282,"The classic enterprise pattern, and the classic enterprise failure: put business logic in the bus and",10,MUTED)
    b+=txt(24,297,"you get a single deployable that every team must queue to change. Modern estates keep the",10,MUTED)
    b+=txt(24,312,"adapters and the canonical model and push routing to a broker — smart endpoints, dumb pipes.",10,MUTED)
    return svg(324,b)

def d_webhook():
    items=[(24,120,"Partner"),(190,130,"Our platform"),(376,120,"Signer"),(520,96,"Retry queue")]
    s,x=lifelines(items,16,288,["soft","acc","plain","amb"])
    b=s
    b+=msg(x[0],x[1],76,"POST /webhooks  {url, events}")
    b+=msg(x[1],x[0],98,"201  + shared secret (shown once)",MUTED,dash=True)
    b+=msg(x[1],x[2],130,"sign(body, secret, timestamp)")
    b+=msg(x[1],x[0],158,"POST url  ·  X-Signature, X-Event-Id",ACC)
    b+=msg(x[0],x[1],182,"2xx within 5 s → done",GRN,dash=True)
    b+=msg(x[0],x[1],206,"5xx / timeout",FLAG,dash=True)
    b+=msg(x[1],x[3],230,"retry 1m, 5m, 30m, 2h, 12h",AMB)
    # the replay path — the fourth property, and the one that is always missing
    b+=msg(x[0],x[1],262,"GET /events?since=…   ·  replay what was missed",ACC)
    b+=msg(x[1],x[0],284,"same events, same ids — dedupe by id",MUTED,dash=True)
    b+=txt(24,318,"Four things separate a webhook that works from one that pages you, and all four are drawn here:",10,MUTED)
    b+=txt(24,333,"a signature with a timestamp (so replays are rejected), a stable event id (so the receiver can",10,MUTED)
    b+=txt(24,348,"dedupe), bounded retries with backoff, and a pull endpoint so a partner who was down for a day",10,MUTED)
    b+=txt(24,363,"can catch up without you rerunning anything. Fire-and-forget is not a delivery guarantee.",10,MUTED)
    return svg(375,b)

# ---------- 10. Process & workflow ----------
def d_flowchart():
    b=""
    b+=oval(76,44,104,34,"Start","soft",fs=10.5)
    b+=node(24,90,104,38,"Read request",None,"plain",fs=10.5)
    b+=dia(76,168,120,54,"in cache?","acc",fs=10)
    b+=node(200,148,124,40,"Return cached",None,"grn",fs=10.5)
    b+=node(200,222,124,40,"Query source",None,"plain",fs=10.5)
    b+=dia(430,168,124,54,"found?","acc",fs=10)
    b+=node(388,242,124,38,"Write cache",None,"plain",fs=10.5)
    b+=node(368,44,124,38,"Return 404",None,"flag",fs=10.5)
    b+=oval(576,110,80,34,"End","soft",fs=10.5)
    b+=arr(76,61,76,88)
    b+=arr(76,128,76,140)
    b+=arr(136,168,198,168,"yes",dy=-5,fs=9)
    b+=poly([(76,195),(76,242),(198,242)],color=MUTED,label="no",lx=100,ly=236,fs=9)
    b+=poly([(324,242),(346,242),(346,168),(366,168)],color=MUTED)
    b+=poly([(430,141),(430,86)],color=FLAG,label="no",lx=446,ly=116,fs=9)
    b+=poly([(430,195),(430,240)],color=MUTED,label="yes",lx=448,ly=222,fs=9)
    b+=poly([(492,63),(576,63),(576,91)],color=MUTED)
    b+=poly([(512,261),(576,261),(576,129)],color=MUTED)
    b+=poly([(262,148),(262,127),(574,127)],color=GRN)
    b+=txt(24,300,"The oldest notation on this list and still the right one for a single actor doing sequential work with",10,MUTED)
    b+=txt(24,315,"branches. The moment there are two actors it should be a swimlane; the moment two things happen",10,MUTED)
    b+=txt(24,330,"at once it should be an activity diagram.",10,MUTED)
    return svg(342,b)

# ---------- 11. DevOps & CI/CD ----------
def d_gitops():
    b=""
    b+=inode(24,52,130,44,"Developer",None,"soft","user",fs=10.5)
    b+=inode(170,52,140,44,"App repo","code + tests","plain","branch",fs=10.5)
    b+=inode(170,132,140,44,"Config repo","desired state","acc","branch",fs=10.5)
    b+=inode(340,52,140,44,"CI","builds image","plain","gear",fs=10.5)
    b+=inode(340,132,140,44,"Reconciler","Argo CD / Flux","acc","sync",fs=10.5)
    b+=arr(154,74,168,74); b+=arr(310,74,338,74)
    b+=poly([(362,96),(362,114),(240,114),(240,130)],color=MUTED,dash=True,label="PR: bump image tag",lx=300,ly=108,fs=9)
    b+=arr(310,154,338,154,"pulls",dy=-5,fs=9)
    b+=frame(506,110,110,112,"cluster")
    b+=inode(518,138,88,30,"running",None,"grn","check",fs=9.5,isize=12,pad=5)
    b+=inode(518,182,88,30,"drifted",None,"flag","warn",fs=9.5,isize=12,pad=5)
    b+=arr(480,154,504,154,"applies",dy=-5,fs=9)
    b+=poly([(562,222),(562,246),(410,246),(410,178)],color=FLAG,dash=True,label="drift detected → reverted",lx=470,ly=260,fs=9)
    b+=txt(24,300,"Two properties are worth the change of habit: the cluster pulls rather than CI pushing, so no",10,MUTED)
    b+=txt(24,315,"pipeline needs production credentials; and git is the desired state, so rollback is git revert and",10,MUTED)
    b+=txt(24,330,"manual kubectl changes are silently undone. The audit trail comes free.",10,MUTED)
    return svg(342,b)

def d_devsecops():
    b=""
    b+=txt(24,32,"SHIFT LEFT  ·  each gate fails the build, not a report nobody opens",9,ACC,"600")
    st=[("Pre-commit","secret scan",24,"key"),("Build","SCA · SBOM",124,"gear"),
        ("Test","SAST",224,"search"),("Package","sign · attest",324,"cert"),
        ("Deploy","IaC scan",424,"rocket"),("Run","DAST · runtime",524,"eye")]
    for i,(n,s2,x,ic) in enumerate(st):
        b+=ihead(x,44,92,52,n,ic,"acc",fs=9.8)
        b+=txt(x+46,112,s2,8.6,MUTED,"500","middle")
        if i<len(st)-1: b+=arr(x+92,70,st[i+1][2]-2,70)
    b+=inode(24,136,286,42,"Blocking","criticals, secrets, unsigned images","flag","warn",fs=10.5)
    b+=inode(330,136,286,42,"Advisory","everything else, with an expiry date","amb","clock",fs=10.5)
    b+=poly([(167,120),(167,134)],color=FLAG); b+=poly([(473,120),(473,134)],color=AMB)
    b+=inode(24,200,592,42,"Admission control","the cluster refuses unsigned or unscanned images — the gate you cannot skip","grn","shield",fs=10.5)
    b+=arr(320,178,320,198,None,GRN)
    b+=txt(24,282,"Every gate needs an owner, a threshold and an exception path with a deadline. Gates that cannot",10,MUTED)
    b+=txt(24,297,"be bypassed get bypassed anyway — by teams routing around the pipeline entirely — unless there",10,MUTED)
    b+=txt(24,312,"is an honest way to ship with a known, time-boxed finding.",10,MUTED)
    return svg(324,b)

# ---------- 12. Observability ----------
def d_logging():
    b=""
    b+=inode(24,60,140,48,"Services","structured JSON","acc","server",fs=10.5)
    b+=inode(180,60,140,48,"Agent","tail + enrich","plain","funnel",fs=10.5)
    b+=inode(336,60,140,48,"Pipeline","redact, sample","flag","shield",fs=10.5)
    b+=inode(492,60,124,48,"Index","hot 7 d","plain","search",fs=10.5)
    b+=arr(164,84,178,84); b+=arr(320,84,334,84); b+=arr(476,84,490,84)
    b+=cyl(492,140,124,48,"Archive","1 y, object store","soft")
    b+=arr(554,108,554,138)
    b+=note(24,132,440,["Every line carries: timestamp, level, service, trace_id, tenant.","Without trace_id the log is unjoinable to the trace that found it.","Without tenant you cannot answer “was this customer affected?”."])
    b+=txt(24,238,"Logs are the most expensive telemetry per answer and the easiest to over-collect. The two levers",10,MUTED)
    b+=txt(24,253,"that matter are on this diagram: drop or sample at the pipeline before you pay to index, and tier",10,MUTED)
    b+=txt(24,268,"retention so the 1 % anyone actually greps stays fast.",10,MUTED)
    return svg(280,b)

def d_metrics():
    b=""
    b+=inode(24,58,140,46,"Service","/metrics","acc","server",fs=10.5)
    b+=inode(180,58,150,46,"Prometheus","scrape 15 s","plain","chart",fs=10.5)
    b+=inode(346,58,140,46,"Recording rules","pre-aggregated","plain","gear",fs=10.5)
    b+=inode(502,58,114,46,"Long-term","13 months","plain","archive",fs=10.5)
    b+=arr(164,81,178,81,"pull",dy=-5,fs=9); b+=arr(330,81,344,81); b+=arr(486,81,500,81)
    b+=inode(24,134,286,44,"RED for services","rate · errors · duration","grn","pulse",fs=10.5)
    b+=inode(330,134,286,44,"USE for resources","utilisation · saturation · errors","grn","chart",fs=10.5)
    b+=note(24,200,592,["Cardinality is the cost function: a metric labelled with user_id or URL path is not a metric,","it is a log with a billing surprise attached. Labels must be bounded and low-arity —","service, endpoint template, status class, region. Nothing that grows with your customers."],FLAG)
    b+=txt(24,290,"Metrics answer “is it broken and how badly”, cheaply and forever. They cannot answer “why”,",10,MUTED)
    b+=txt(24,305,"which is what the trace and the log are for. Size the dashboard for the first question only.",10,MUTED)
    return svg(316,b)

def d_tracing():
    b=""
    # bars are drawn at 1 px = 1 ms, so the root span's width IS the stated total
    b+=txt(24,24,"ONE REQUEST  ·  trace 9f2c…  ·  total 592 ms  ·  1 px = 1 ms",9.5,ACC,"600")
    spans=[("gateway",24,0,592,GRN),("  order-svc  handler",44,30,500,ACC),
           ("    auth check",64,42,55,MUTED),("    db  SELECT order",84,105,80,MUTED),
           ("    payment-svc  POST /auth",104,195,300,FLAG),("      db  SELECT card",124,210,40,MUTED),
           ("      external gateway",144,260,220,FLAG),("  kafka publish",164,505,87,AMB)]
    y0=44
    for name,dy,x0,w,c in spans:
        y=y0+dy
        b+='<rect x="%g" y="%g" width="%g" height="13" rx="2" fill="%s" opacity="0.22"/>'%(24+x0,y,max(w,6),c)
        b+='<rect x="%g" y="%g" width="%g" height="13" rx="2" fill="none" stroke="%s" stroke-width="1.1"/>'%(24+x0,y,max(w,6),c)
        b+=txt(28+x0,y+10,name,8.8,INK if c!=MUTED else MUTED,"600")
    b+='<line x1="284" y1="40" x2="284" y2="232" stroke="%s" stroke-width="1" stroke-dasharray="3 4"/>'%FLAG
    b+='<line x1="504" y1="40" x2="504" y2="232" stroke="%s" stroke-width="1" stroke-dasharray="3 4"/>'%FLAG
    b+='<line x1="24" y1="236" x2="616" y2="236" stroke="%s" stroke-width="1"/>'%LINE
    for k in range(0,6):
        xx=24+k*100
        b+='<line x1="%g" y1="236" x2="%g" y2="242" stroke="%s" stroke-width="1"/>'%(xx,xx,LINE)
        b+=txt(xx,256,"%d ms"%(k*100),8.4,MUTED,anchor="middle")
    b+=txt(394,278,"220 ms — 37 % of the request — in one third-party call",9.5,FLAG,"600","middle")
    b+=txt(24,308,"A trace is a tree of spans joined by one id propagated across every hop, including through the",10,MUTED)
    b+=txt(24,323,"broker. Head sampling is cheap and loses the rare slow request; tail sampling keeps the",10,MUTED)
    b+=txt(24,338,"interesting ones and costs more. Decide which, and write it on the diagram.",10,MUTED)
    return svg(350,b)

def d_alerting():
    b=""
    b+=inode(24,54,150,48,"SLO  ·  99.9 %","budget 43 min/mo","acc","chart",fs=10.5)
    b+=inode(190,54,150,48,"Burn rate","14.4× over 1 h","flag","warn",fs=10.5)
    b+=inode(356,54,140,48,"Alert manager","group · dedupe","plain","funnel",fs=10.5)
    b+=inode(512,54,104,48,"On call","one human","grn","user",fs=10.5)
    b+=arr(174,78,188,78); b+=arr(340,78,354,78); b+=arr(496,78,510,78)
    b+=inode(356,132,140,40,"Ticket queue","slow burn, 6 h","soft","clock",fs=10)
    b+=poly([(264,102),(264,152),(354,152)],color=MUTED,label="2× over 6 h",lx=298,ly=168,fs=9)
    b+=inode(512,132,104,40,"Escalate","15 min","amb","bell",fs=10)
    b+=arr(564,102,564,130,None,AMB)
    b+=inode(24,196,592,42,"Every page must be actionable, novel and urgent","otherwise it is a dashboard, and it is training people to ignore you","flag","bell",fs=10.5)
    b+=txt(24,272,"Alert on symptoms the user feels, at a burn rate tied to the budget you agreed. A fast burn wakes",10,MUTED)
    b+=txt(24,287,"someone; a slow burn opens a ticket. CPU is not a symptom — nobody has ever filed a complaint",10,MUTED)
    b+=txt(24,302,"about CPU. And route by service ownership, or the page reaches whoever is loudest, not nearest.",10,MUTED)
    return svg(314,b)

# ---------- 13. Reliability & resilience ----------
def d_faulttree():
    b=""
    b+=node(196,24,248,42,"TOP EVENT  ·  checkout unavailable",None,"flag",fs=11)
    b+=dia(320,96,84,44,"OR","flag",fs=11)
    b+=arr(320,66,320,74)
    b+=node(44,148,168,40,"Order service down",None,"plain",fs=10.5)
    b+=node(236,148,168,40,"Payment path down",None,"plain",fs=10.5)
    b+=node(428,148,188,40,"Database unreachable",None,"plain",fs=10.5)
    b+=poly([(320,118),(320,132),(128,132),(128,146)],color=FLAG)
    b+=poly([(320,132),(320,146)],color=FLAG)
    b+=poly([(320,132),(522,132),(522,146)],color=FLAG)
    b+=dia(320,222,84,44,"AND","grn",fs=11)
    b+=arr(320,188,320,200)
    b+=node(196,286,110,36,"Provider A out",None,"soft",fs=10)
    b+=node(330,286,110,36,"Provider B out",None,"soft",fs=10)
    b+=poly([(320,244),(320,268),(251,268),(251,284)],color=GRN)
    b+=poly([(320,268),(385,268),(385,284)],color=GRN)
    b+=txt(24,346,"Read it downward: an OR gate is a single point of failure, an AND gate is redundancy that works.",10,MUTED)
    b+=txt(24,361,"Every OR near the top is a design question — can this be made an AND? With rough probabilities on",10,MUTED)
    b+=txt(24,376,"the leaves the tree also tells you which branch is worth spending money on first.",10,MUTED)
    return svg(388,b)

def d_rbd():
    b=""
    b+=txt(24,24,"SERIES  ·  every block must work  —  availability multiplies",9,FLAG,"600")
    ser=[("DNS","99.99 %",24),("CDN","99.95 %",158),("App","99.9 %",292),("DB","99.95 %",426)]
    for i,(n,a,x) in enumerate(ser):
        b+=node(x,38,110,44,n,a,"plain",fs=10.5)
        if i<len(ser)-1: b+=arr(x+110,60,ser[i+1][2]-2,60)
    b+=arr(536,60,552,60,None,head=False)
    b+=node(552,38,64,44,"99.79 %",None,"flag",fs=10.5)
    b+='<line x1="24" y1="106" x2="616" y2="106" stroke="%s" stroke-width="1"/>'%LINE
    b+=txt(24,132,"PARALLEL  ·  one is enough  —  unavailability multiplies",9,GRN,"600")
    b+=node(24,168,96,44,"App","99.9 %","plain",fs=10.5)
    b+=node(200,144,150,36,"Instance A  99.9 %",None,"plain",fs=10)
    b+=node(200,192,150,36,"Instance B  99.9 %",None,"plain",fs=10)
    b+=poly([(120,190),(160,190),(160,162),(198,162)],color=GRN)
    b+=poly([(160,190),(160,210),(198,210)],color=GRN)
    b+=poly([(350,162),(392,162),(392,190),(414,190)],color=GRN)
    b+=poly([(350,210),(392,210)],color=GRN)
    b+=node(416,168,200,44,"99.9999 %  ·  if truly independent",None,"grn",fs=10.5)
    b+=note(24,238,592,["“If truly independent” is where these numbers usually die: two instances sharing one","availability zone, one deploy pipeline, one config store or one expiring certificate are","one block, not two. The maths rewards redundancy; the outage report rewards independence."],FLAG)
    b+=txt(24,340,"Useful precisely because it is arithmetic: it shows that a four-nines target cannot be met by a chain",10,MUTED)
    b+=txt(24,355,"of four three-nines dependencies, however much anyone wants it to.",10,MUTED)
    return svg(366,b)

def d_fmea():
    b=""
    rows=[["Broker unavailable","Orders stop publishing","Outbox fills, disk full","Alert on outbox depth","High"],
          ["Payment timeout","Unknown charge state","Double charge on retry","Idempotency key","High"],
          ["Cache stampede","Origin overload","Cascading 5xx","Request coalescing","Medium"],
          ["Bad deploy","Wrong config live","Silent data corruption","Canary + schema check","High"],
          ["Cert expiry","All mTLS fails","Total outage","Auto-renew + 30 d alert","Low"]]
    def cc(r,i,v):
        if i==4: return {"High":FLAG,"Medium":AMB,"Low":GRN}.get(v,MUTED)
        if i==0: return INK
        if i==2: return FLAG
        if i==3: return GRN
        return MUTED
    b+=grid(24,26,592,["Failure mode","Immediate effect","What it becomes","Detection / mitigation","Risk"],rows,
            [0,0.22,0.42,0.62,0.885],rh=30,hh=29,cellcolor=cc)
    b+=txt(24,240,"The third column is the one worth the meeting. Teams are good at listing failures and naming their",10,MUTED)
    b+=txt(24,255,"immediate effect; incidents are made by the second-order consequence nobody traced — the",10,MUTED)
    b+=txt(24,270,"retry that becomes a double charge, the queue that becomes a full disk. Detection before",10,MUTED)
    b+=txt(24,285,"mitigation: an unmitigated failure you can see beats a mitigated one you cannot.",10,MUTED)
    return svg(298,b)

def d_bulkhead():
    b=""
    b+=txt(24,24,"SHARED POOL  ·  one slow dependency takes everything",9,FLAG,"600")
    b+=node(24,36,120,52,"200 threads",None,"flag",fs=11)
    b+=node(196,32,140,26,"Search  ·  fast",None,"soft",fs=9.5)
    b+=node(196,64,140,26,"Reports  ·  slow, 30 s",None,"flag",fs=9.5)
    b+=arr(144,50,194,45); b+=arr(144,74,194,77)
    b+=txt(356,58,"reports hold 200 threads → search returns 503",9.5,FLAG,"600")
    b+='<line x1="24" y1="110" x2="616" y2="110" stroke="%s" stroke-width="1"/>'%LINE
    b+=txt(24,136,"BULKHEADS  ·  isolated pools, bounded blast radius",9,GRN,"600")
    b+=node(24,148,120,40,"Search  ·  120",None,"grn",fs=10.5)
    b+=node(24,196,120,40,"Reports  ·  40",None,"amb",fs=10.5)
    b+=node(24,244,120,40,"Admin  ·  20",None,"grn",fs=10.5)
    b+=node(196,148,140,40,"Search backend",None,"plain",fs=10)
    b+=node(196,196,140,40,"Report engine","degraded","flag",fs=10)
    b+=node(196,244,140,40,"Admin API",None,"plain",fs=10)
    b+=arr(144,168,194,168,None,GRN); b+=arr(144,216,194,216,None,FLAG); b+=arr(144,264,194,264,None,GRN)
    b+=node(376,148,240,40,"Still serving","the 120 are untouched","grn",fs=10.5)
    b+=node(376,196,240,40,"Fails fast","queue full → 429 immediately","amb",fs=10.5)
    b+=node(376,244,240,40,"Still serving",None,"grn",fs=10.5)
    b+=arr(336,168,374,168,None,GRN); b+=arr(336,216,374,216,None,AMB); b+=arr(336,264,374,264,None,GRN)
    b+=txt(24,324,"Named after ship compartments, and the metaphor is exact: the point is not to prevent the leak,",10,MUTED)
    b+=txt(24,339,"it is to stop the leak sinking the ship. Partition by dependency, by tenant, or by criticality —",10,MUTED)
    b+=txt(24,354,"and size each pool so the sum still fits, or you have simply renamed the shared pool.",10,MUTED)
    return svg(366,b)

def d_retry():
    b=""
    b+=node(24,52,116,48,"Caller","idempotency-key","acc",fs=10.5)
    b+=node(180,52,124,48,"Attempt 1","fails · 500",fs=10.5)
    b+=node(344,52,124,48,"Attempt 2","+ 1 s ± jitter",fs=10.5)
    b+=node(500,52,116,48,"Attempt 3","+ 2 s ± jitter",fs=10.5)
    b+=arr(140,76,178,76); b+=arr(304,76,342,76); b+=arr(468,76,498,76)
    b+=node(344,132,272,40,"Give up  ·  DLQ or 503 to the caller",None,"flag",fs=10.5)
    b+=poly([(558,100),(558,130)],color=FLAG)
    b+=note(24,124,296,["Retry only what is safe and transient:","timeouts, 429, 503, connection resets.","Never a 400, never a 409 — those will","fail identically forever."],FLAG)
    b+=node(24,228,286,44,"Jitter","without it, every client retries in step","grn",fs=10.5)
    b+=node(330,228,286,44,"Retry budget","cap at ~10 % of traffic, cluster-wide","grn",fs=10.5)
    b+=txt(24,304,"Retries are how a small failure becomes an outage: the dependency wobbles, every caller triples",10,MUTED)
    b+=txt(24,319,"its load, and the wobble becomes a collapse. Backoff, jitter, a cap, and a budget — and behind",10,MUTED)
    b+=txt(24,334,"them an idempotency key, or attempt 2 charges the customer a second time.",10,MUTED)
    return svg(346,b)

def d_activeactive():
    b=""
    b+=node(230,18,180,38,"Anycast / GeoDNS","both regions healthy","acc",fs=11)
    b+=frame(24,80,282,150,"region A  ·  serving",GRN,dash=False)
    b+=frame(334,80,282,150,"region B  ·  serving",GRN,dash=False)
    b+=node(46,106,150,38,"App  ·  live",None,"grn",fs=10.5)
    b+=node(356,106,150,38,"App  ·  live",None,"grn",fs=10.5)
    b+=cyl(46,158,150,52,"Store A","writes for EU rows","acc")
    b+=cyl(356,158,150,52,"Store B","writes for US rows","acc")
    b+=poly([(280,56),(121,56),(121,104)],color=GRN)
    b+=poly([(360,56),(431,56),(431,104)],color=GRN)
    b+=arr(121,144,121,156); b+=arr(431,144,431,156)
    b+=arr(196,192,354,192,None,AMB,dash=True)
    b+=arr(354,200,196,200,None,AMB,dash=True)
    b+=lbl(275,186,"bidirectional replication",9,AMB)
    b+=node(24,254,286,44,"Conflicts are guaranteed","last-write-wins loses data silently","flag",fs=10.5)
    b+=node(330,254,286,44,"So partition ownership","each row has exactly one home region","grn",fs=10.5)
    b+=txt(24,330,"Active/active doubles your capacity and removes the failover step — and buys you the hardest",10,MUTED)
    b+=txt(24,345,"problem in distributed data. Either shard so no row is written in two places, or choose a merge",10,MUTED)
    b+=txt(24,360,"rule (CRDT, vector clocks, business rule) and put it on the diagram. Silence here means data loss.",10,MUTED)
    return svg(372,b)

# ---------- 14. Decision ----------
def d_adr():
    b=""
    # Superseded and Deprecated are two different endings off Accepted, not a queue
    b+=pill(24,38,116,32,"Proposed","soft")
    b+=pill(180,38,116,32,"Accepted","grn")
    b+=pill(392,10,124,30,"Superseded","amb")
    b+=pill(392,74,124,30,"Deprecated","flag")
    b+=arr(140,54,178,54,"review",dy=-5,fs=9)
    b+=poly([(296,54),(344,54),(344,25),(390,25)],color=MUTED)
    b+=poly([(344,54),(344,89),(390,89)],color=MUTED)
    b+=lbl(348,18,"ADR-051 replaces it",8.8)
    b+=lbl(348,104,"nothing replaces it",8.8)
    b+=txt(24,132,"Two endings, not a queue: an ADR is superseded when a later one replaces it, deprecated when the "
                  "thing it decided is simply gone.",9.5,MUTED,style="i")
    b+=frame(24,148,592,166,"ADR-042  ·  Use Kafka for order events",ACC,dash=False)
    secs=[("Context","Three services need order state; nightly batch is too slow.",178),
          ("Decision","Publish domain events to Kafka, keyed by orderId.",216),
          ("Alternatives","Shared database (rejected: coupling). REST fan-out (rejected: n² links).",254),
          ("Consequences","+ decoupled  + replayable   − ops burden  − eventual consistency in the UI",292)]
    for h,t,y in secs:
        b+=txt(44,y,h.upper(),8.8,ACC,"600")
        b+=txt(150,y,t,10,INK if h=="Decision" else MUTED)
    b+='<line x1="140" y1="162" x2="140" y2="304" stroke="%s" stroke-width="1"/>'%LINE
    b+=txt(24,350,"Never edited, only superseded — the record of a decision you later reversed is more valuable than",10,MUTED)
    b+=txt(24,365,"the reversal. Keep them in the repo beside the code, numbered, one page each. If the consequences",10,MUTED)
    b+=txt(24,380,"section lists no downside, no trade-off was made and the ADR is marketing.",10,MUTED)
    return svg(392,b)

# ---------- 15. Specialised ----------
def d_servicedep():
    b=""
    b+=node(268,24,120,38,"Gateway",None,"soft",fs=10.5)
    b+=node(120,96,124,42,"Order","tier 1","acc",fs=10.5)
    b+=node(396,96,124,42,"Catalogue","tier 2",fs=10.5)
    b+=node(24,180,124,42,"Payment","tier 1","acc",fs=10.5)
    b+=node(180,180,124,42,"Inventory","tier 1","acc",fs=10.5)
    b+=node(396,180,124,42,"Reviews","tier 3",fs=10.5)
    b+=node(180,262,340,42,"Identity  ·  tier 0  ·  every service depends on it","single point of failure — 6 inbound","flag",fs=10.5)
    b+=arr(308,62,200,94); b+=arr(348,62,440,94)
    b+=arr(150,138,110,178); b+=arr(190,138,230,178)
    b+=arr(458,138,458,178)
    # finding 1 — the cycle, which needs both edges drawn to be a cycle at all
    b+=arr(246,108,394,108,None,FLAG)
    b+=arr(394,128,246,128,None,FLAG)
    b+=lbl(320,122,"cycle — each calls the other",8.8,FLAG,"600")
    # finding 2 — six inbound edges on one node, collected onto a rail so they can be counted
    b+=poly([(388,43),(578,43),(578,246)],color=FLAG,dash=True,head=False)
    b+=poly([(164,138),(164,246)],color=FLAG,dash=True,head=False)
    b+=poly([(520,110),(548,110),(548,246)],color=FLAG,dash=True,head=False)
    for x in (86,242,458):
        b+=poly([(x,222),(x,246)],color=FLAG,dash=True,head=False)
    b+='<line x1="86" y1="246" x2="578" y2="246" stroke="%s" stroke-width="1.2" stroke-dasharray="5 4"/>'%FLAG
    b+=arr(350,246,350,258,None,FLAG,dash=True)
    b+=lbl(350,240,"6 inbound",8.8,FLAG,"600")
    b+=txt(24,340,"Two things to look for and nothing else. Cycles — Order calls Catalogue and Catalogue calls back —",10,MUTED)
    b+=txt(24,355,"which make deployment order undefined and failures circular. And the node with the most inbound",10,MUTED)
    b+=txt(24,370,"edges, your real availability ceiling. Generate it from traces; the hand-drawn version flatters you.",10,MUTED)
    return svg(382,b)

def d_mlops():
    b=""
    b+=txt(24,24,"TRAINING",9,ACC,"600")
    tr=[("Raw data","versioned",24),("Features","feature store",146),("Train","experiment log",268),
        ("Evaluate","vs baseline",390),("Registry","staged model",506)]
    for i,(n,s2,x) in enumerate(tr):
        w=110 if i<4 else 110
        b+=node(x,34,w,46,n,s2,"acc" if i==4 else "plain",fs=10.5)
        if i<len(tr)-1: b+=arr(x+w,57,tr[i+1][2]-2,57)
    b+='<line x1="24" y1="104" x2="616" y2="104" stroke="%s" stroke-width="1"/>'%LINE
    b+=txt(24,128,"SERVING",9,GRN,"600")
    b+=node(24,138,110,46,"Request",None,"soft",fs=10.5)
    b+=node(146,138,124,46,"Feature lookup","same store","grn",fs=10.5)
    b+=node(282,138,124,46,"Model","shadow + canary","grn",fs=10.5)
    b+=node(418,138,198,46,"Prediction + explanation",None,"grn",fs=10.5)
    b+=arr(134,161,144,161); b+=arr(270,161,280,161); b+=arr(406,161,416,161)
    b+=poly([(561,80),(561,110),(344,110),(344,136)],color=ACC,dash=True,label="promote",lx=460,ly=104,fs=9)
    b+=node(24,208,592,44,"Monitor  ·  input drift · prediction drift · label lag · fairness — the trigger to retrain","and the reason the loop is a loop, not a pipeline","amb",fs=10.5)
    b+=poly([(344,184),(344,206)],color=AMB)
    b+=txt(24,286,"The trap is the two feature paths: if training reads a warehouse table and serving computes the",10,MUTED)
    b+=txt(24,301,"same feature in application code, they will diverge, and the model will quietly get worse. One",10,MUTED)
    b+=txt(24,316,"feature store, used by both, is the architectural decision on this page.",10,MUTED)
    return svg(328,b)

def d_llmapp():
    b=""
    b+=node(24,20,286,40,"Guardrails on both sides","injection + PII in  ·  policy + PII out","flag",fs=10)
    b+=node(330,20,286,40,"Evals + traces","every turn logged, replayable, costed","grn",fs=10)
    b+=node(24,92,96,44,"User",None,"soft",fs=10.5)
    b+=node(142,92,142,44,"Orchestrator","plan · act · observe","acc",fs=10.5)
    b+=node(342,92,124,44,"Model","tool-calling","vio",fs=10.5)
    b+=node(508,92,108,44,"Response","cited, checked","grn",fs=10.5)
    b+=arr(167,60,167,90,None,FLAG,dash=True)
    b+=arr(473,60,473,90,None,GRN,dash=True)
    b+=arr(120,114,140,114)
    b+=arr(466,108,506,108,"loop exits",lp=0.5,dy=-6,fs=8.4,color=GRN)
    # the loop is drawn, because the loop is the thing that breaks — and it is bounded,
    # because an unbounded one does not fail loudly
    b+=arr(284,104,340,104,"prompt + tool results",lp=0.5,dy=-16,fs=8.4,color=ACC)
    b+=arr(340,126,284,126,"next tool call",lp=0.5,dy=13,fs=8.4,color=VIO)
    b+=poly([(213,136),(213,166),(404,166),(404,138)],color=AMB,dash=True,head=False)
    b+=lbl(308,182,"bounded — 6 turns max  ·  60 s  ·  $0.05  ·  then stop and say why",9,AMB,"600")
    b+='<line x1="117" y1="204" x2="522" y2="204" stroke="%s" stroke-width="1.1" stroke-dasharray="5 4"/>'%MUTED
    b+=poly([(213,166),(213,204)],color=MUTED,dash=True,head=False)
    b+=node(24,216,186,38,"Tools","typed, allow-listed","plain",fs=9.6)
    b+=node(226,216,186,38,"Retrieval","the RAG plate","plain",fs=9.6)
    b+=node(428,216,188,38,"Memory","short-term + long-term","plain",fs=9.6)
    for x in (117,319,522):
        b+=arr(x,204,x,214,None,MUTED,dash=True)
    b+=txt(24,290,"Draw the loop, and put numbers on it. An agent with no turn cap, no wall-clock cap and no cost",10,MUTED)
    b+=txt(24,305,"ceiling does not fail loudly — it fails at 3 a.m. with a five-figure bill and no answer. And treat",10,MUTED)
    b+=txt(24,320,"model output as untrusted input to everything downstream, because that is exactly what it is.",10,MUTED)
    return svg(332,b)

def d_iot():
    b=""
    b+=frame(24,26,168,148,"field",MUTED)
    b+=node(40,52,136,34,"Sensors × 40 k",None,"soft",fs=10)
    b+=node(40,96,136,34,"Actuators",None,"soft",fs=10)
    b+=node(40,136,136,30,"MQTT, 3G, flaky",None,"plain",fs=9.2)
    b+=frame(216,26,180,148,"edge gateway",ACC,dash=False)
    b+=node(232,52,148,34,"Buffer + store-forward",None,"acc",fs=9.8)
    b+=node(232,96,148,34,"Local rules","act without cloud",fs=9.8)
    b+=node(232,136,148,30,"OTA update agent",None,"plain",fs=9.2)
    b+=frame(420,26,196,148,"cloud",MUTED)
    b+=node(436,52,164,34,"Ingest  ·  IoT hub",None,"plain",fs=9.8)
    b+=node(436,96,164,34,"Device twin","desired vs reported","acc",fs=9.8)
    b+=node(436,136,164,30,"Time series + analytics",None,"plain",fs=9.2)
    b+=arr(192,66,214,66); b+=arr(396,66,418,66)
    b+=poly([(490,130),(490,190),(306,190),(306,168)],color=MUTED,dash=True,label="desired state down",lx=400,ly=204,fs=9)
    b+=txt(24,240,"The three constraints that make IoT its own shape: the link is intermittent, so the edge must keep",10,MUTED)
    b+=txt(24,255,"working and buffer; the fleet is enormous, so per-device identity and rotation must be automatic;",10,MUTED)
    b+=txt(24,270,"and firmware update is a first-class path, because a device you cannot patch is a device you own",10,MUTED)
    b+=txt(24,285,"for ten years. Twins exist so the cloud can hold intent for a thing that is currently offline.",10,MUTED)
    return svg(298,b)

def d_edge():
    b=""
    tiers=[("Device","0 ms","on the thing itself",24,"soft"),("Edge / PoP","2–10 ms","cache, auth, filter",172,"acc"),
           ("Regional","20–40 ms","stateful services",320,"plain"),("Core cloud","80–150 ms","training, warehouse",468,"plain")]
    for n,lat,role,x,st in tiers:
        b+=node(x,50,128,60,n,role,st,fs=11)
        b+=txt(x+64,132,lat,10,ACC,"600","middle")
        if x<468: b+=arr(x+128,80,x+146,80)
    b+='<line x1="24" y1="146" x2="616" y2="146" stroke="%s" stroke-width="1"/>'%LINE
    b+=node(24,166,286,44,"Push outward","latency, bandwidth cost, data residency","grn",fs=10.5)
    b+=node(330,166,286,44,"Keep inward","consistency, expensive compute, state","acc",fs=10.5)
    b+=arr(196,224,196,236,None,GRN); b+=arr(444,236,444,224,None,ACC)
    b+=node(24,240,592,40,"The dividing line is the design: what can be decided with local knowledge, and what cannot",None,"amb",fs=10.5)
    b+=txt(24,314,"Every millisecond of the round trip is on this diagram, which is what makes it useful — a video",10,MUTED)
    b+=txt(24,329,"analytics rule at 100 ms is a different product from one at 5 ms. Push the decision to the tier",10,MUTED)
    b+=txt(24,344,"that has enough information to make it, and no further.",10,MUTED)
    return svg(356,b)
def d_uml_component():
    b=""
    def comp(x,y,w,h,name,style="acc"):
        fill,stroke,tc = STYLES[style]
        s='<rect x="%g" y="%g" width="%g" height="%g" rx="3" fill="%s" stroke="%s" stroke-width="1.4"/>'%(
            x,y,w,h,fill,stroke)
        s+=txt(x+w/2.0,y+21,"«component»",9,MUTED,anchor="middle")
        s+=txt(x+w/2.0,y+40,name,12,tc,"600","middle")
        s+=icon("container",x+w-17,y+16,13,stroke)
        return s
    b+=comp(24,140,132,72,"Web UI","soft")
    b+=comp(230,100,170,140,"Order Service")
    b+=comp(500,90,116,72,"Payment Svc")
    b+=comp(500,182,116,72,"Notification")
    # provided (ball) meets required (socket): the assembly connector
    b+=socket(156,176,None,MUTED,"right",44)
    b+=lolli(230,176,"IOrders",ACC,"left",24)
    b+=socket(400,126,None,ACC,"right",70)
    b+=lolli(500,126,"IPayments",ACC,"left",24)
    b+=socket(400,218,None,ACC,"right",70)
    b+=lolli(500,218,"INotify",ACC,"left",24)
    b+=txt(214,268,"assembly connector  ·  a required interface sitting on the provided one",9,MUTED,anchor="middle")
    b+=poly([(200,182),(200,258),(214,258)],color=MUTED,head=False)
    b+=txt(24,300,"Not the C4 component diagram. This is UML structural notation: the ball is an interface a",10,MUTED)
    b+=txt(24,315,"component provides, the socket one it requires, and the two together are a contract you can",10,MUTED)
    b+=txt(24,330,"swap either side of. C4 borrowed the word and means something else by it — what is inside",10,MUTED)
    b+=txt(24,345,"one container — so say which you mean before anyone starts drawing.",10,MUTED)
    return svg(358,b)

# ==================================================================
# Additions — the gaps a working architect hits that the first pass missed.
# ==================================================================

# ---------- 1. Architecture & system-level ----------
def d_hexagonal():
    b=""
    b+=txt(24,24,"DRIVING  ·  adapters that call us",9,ACC,"600")
    b+=txt(466,24,"DRIVEN  ·  adapters we call",9,ACC,"600")
    b+='<path d="M 200 148 L 262 58 L 378 58 L 440 148 L 378 238 L 262 238 Z" fill="%s" stroke="%s" stroke-width="1.8"/>'%(TINT[ACC],ACC)
    b+=txt(320,110,"Domain",13,"#123F5C","700","middle")
    b+=txt(320,127,"entities, value objects, invariants",8.6,MUTED,anchor="middle")
    b+=txt(320,164,"Application",11.5,"#123F5C","600","middle")
    b+=txt(320,181,"use cases, orchestration only",8.6,MUTED,anchor="middle")
    for n,t,y in [("REST controller","HTTP",100),("Scheduled job","cron",148),("Test harness","in-memory",196)]:
        b+=node(24,y-19,150,38,n,t,"soft",fs=10)
    for n,t,y in [("Postgres adapter","SQL",100),("Kafka adapter","producer",148),("Stripe adapter","HTTP",196)]:
        b+=node(466,y-19,150,38,n,t,"soft",fs=10)
    # the port is a square ON the boundary — an interface the hexagon itself owns
    for y in (100,148,196):
        ex=200+(abs(148-y)/90.0)*62
        b+='<rect x="%g" y="%g" width="13" height="13" fill="#FFFFFF" stroke="%s" stroke-width="1.4"/>'%(ex-6.5,y-6.5,ACC)
        b+=arr(176,y,ex-9,y)
        ex2=440-(abs(148-y)/90.0)*62
        b+='<rect x="%g" y="%g" width="13" height="13" fill="#FFFFFF" stroke="%s" stroke-width="1.4"/>'%(ex2-6.5,y-6.5,ACC)
        b+=arr(ex2+9,y,464,y)
    b+=lbl(320,254,"the port is the square on the edge — an interface the hexagon owns",8.6,ACC,"600")
    b+=note(24,272,286,["Driving adapters call in; the hexagon","calls driven adapters out. Either way","the adapter depends on the port — so","the dependency always points inward."],ACC)
    b+=node(330,272,286,44,"Swap an adapter, keep the core","Postgres → DynamoDB touches exactly one box","grn",fs=9.6)
    b+=txt(24,368,"The hexagon is a rule with a shape: nothing inside it may import a framework, a driver or an",10,MUTED)
    b+=txt(24,383,"HTTP type. That is what makes the core testable without infrastructure and survivable across a",10,MUTED)
    b+=txt(24,398,"re-platforming — and it holds only because it is checkable in a build test.",10,MUTED)
    return svg(410,b)

# ---------- 3. Interaction & runtime ----------
def d_processview():
    b=""
    b+=frame(24,36,286,182,"process  ·  api-server  ×4 replicas",ACC,dash=False)
    b+=inode(42,64,250,32,"Accept loop","1 thread, epoll","acc","sync",fs=9.8)
    b+=inode(42,106,250,38,"Request pool","32 threads · bounded queue 100","acc","server",fs=9.8)
    b+=inode(42,154,250,46,"Connection pool","10 to Postgres","amb","db",fs=9.8)
    b+=frame(330,36,286,182,"process  ·  worker  ×2 replicas",MUTED,dash=False)
    b+=inode(348,64,250,32,"Consumer","4 threads, prefetch 10","plain","queue",fs=9.8)
    b+=inode(348,106,250,38,"Job pool","8 threads · CPU bound","plain","gear",fs=9.8)
    b+=inode(348,154,250,46,"Connection pool","5 to Postgres","amb","db",fs=9.8)
    b+=cyl(216,266,208,52,"Postgres","max_connections = 100","grn")
    b+=poly([(167,200),(167,244),(260,244),(260,264)],color=AMB)
    b+=poly([(473,200),(473,244),(380,244),(380,264)],color=AMB)
    b+=lbl(320,240,"4 × 10  +  2 × 5  =  50 of 100 — the ceiling nobody sized",8.8,AMB,"600")
    b+=node(24,336,286,44,"Threads are not the constraint","32 × 4 = 128 in flight, and that is fine","amb",fs=9.6)
    b+=node(330,336,286,44,"The pool is","double the replicas and Postgres runs out, not CPU","flag",fs=9.6)
    b+=txt(24,410,"The forgotten view of the 4+1 set, and the one that explains outages a structure diagram",10,MUTED)
    b+=txt(24,425,"cannot: what runs as a process, what runs as a thread, what is shared between them, and which",10,MUTED)
    b+=txt(24,440,"bound is reached first. Autoscaling multiplies every number on this page — including the ones",10,MUTED)
    b+=txt(24,455,"that belong to something you do not own.",10,MUTED)
    return svg(467,b)

# ---------- 4. Data architecture ----------
def d_sharding():
    b=""
    specs=[("Hash","hash(tenantId) % 8",
            ["+ even spread by design","− no range scans","− adding a shard","   rehashes everything"],24,ACC),
           ("Range","month(created_at)",
            ["+ range scans stay cheap","+ old shards go cold","− this month is always","   the hot shard"],216,AMB),
           ("Directory","tenant → shard map",
            ["+ move one tenant at a time","+ residency per tenant","− the lookup becomes","   a tier-0 dependency"],408,GRN)]
    for name,key,lines,x,c in specs:
        b+=band(x,20,184,172,name,c,fs=10)
        b+=node(x+12,50,160,30,key,None,"plain",fs=9.2)
        for i,t in enumerate(lines):
            b+=txt(x+12,102+i*16,t,8.8,GRN if t.startswith("+") else (FLAG if t.startswith("−") else MUTED))
    b+=txt(24,216,"AND THE PART THAT ACTUALLY DECIDES IT  ·  what happens when you outgrow N",9,ACC,"600")
    for i in range(4):
        b+=inode(24+i*152,230,140,38,"shard %d"%i,"~2 TB","plain","db",fs=9.6,isize=13,pad=6)
    b+=node(24,288,286,46,"Re-sharding live is a quarter","not a sprint, and not a maintenance window","flag",fs=9.6)
    b+=node(330,288,286,46,"So write the rebalance plan down","split · backfill · dual-read · cut over · drop","grn",fs=9.6)
    b+=txt(24,364,"The shard key is the hardest decision here to reverse and the one most often made by whoever",10,MUTED)
    b+=txt(24,379,"wrote the first migration. Choose it for the query you run most, not the write you make most —",10,MUTED)
    b+=txt(24,394,"and state what happens at the shard count you will actually reach, not the one you start with.",10,MUTED)
    return svg(406,b)

# ---------- 7. Business & domain ----------
def d_teamtopo():
    b=""
    b+=txt(24,22,"FOUR TEAM TYPES, THREE INTERACTION MODES  ·  and nothing else",9,ACC,"600")
    b+=node(24,34,276,54,"Stream-aligned  ·  Orders","owns Order Service end to end","acc",fs=11)
    b+=node(340,34,276,54,"Stream-aligned  ·  Payments","owns Payment Service end to end","acc",fs=11)
    b+=arr(300,54,338,54,None,ACC); b+=arr(338,70,300,70,None,ACC)
    b+=lbl(319,46,"collaboration",8.4,ACC,"600")
    b+=lbl(319,86,"time-boxed, then split",8.2,MUTED)
    b+=node(24,126,240,50,"Enabling  ·  SRE guild","coaches a team, then leaves","amb",fs=10.5)
    b+=node(376,126,240,50,"Complicated subsystem","pricing engine — specialists","vio",fs=10.5)
    b+=poly([(144,126),(144,108),(162,108),(162,90)],color=AMB,dash=True,label="facilitating",lx=104,ly=112,fs=8.6)
    b+=poly([(496,126),(496,108),(478,108),(478,90)],color=VIO,label="X-as-a-service",lx=556,ly=112,fs=8.6)
    b+=node(24,214,592,50,"Platform  ·  the golden path as a product",
            "paved road, self-serve, opt-in — measured by adoption, not by tickets closed","grn",fs=11)
    b+=arr(162,212,162,180,None,GRN); b+=arr(478,212,478,180,None,GRN)
    b+=lbl(320,204,"X-as-a-service to everyone above",8.6,GRN,"600")
    b+=note(24,282,592,["This is a design, not a description. Team boundaries and service boundaries are the same",
                        "boundaries — so if this does not match the bounded context map, one of the two is wrong,",
                        "and it is almost always cheaper to move the team than to move the code."],ACC)
    b+=txt(24,384,"Inverse Conway: choose the architecture you want, then shape the teams to match, because the",10,MUTED)
    b+=txt(24,399,"system ends up looking like the org chart whether anyone planned it or not. Cognitive load is",10,MUTED)
    b+=txt(24,414,"the sizing rule — a stream-aligned team that owns nine services owns none of them well.",10,MUTED)
    return svg(426,b)

def d_wardley():
    b=""
    X0,X1,Y0,Y1=96,608,38,232
    b+='<rect x="%g" y="%g" width="%g" height="%g" rx="3" fill="#FCFCFD" stroke="%s" stroke-width="1.2"/>'%(
        X0,Y0,X1-X0,Y1-Y0,LINE)
    for i,s in enumerate(["Genesis","Custom-built","Product / rental","Commodity"]):
        xx=X0+(X1-X0)*i/4.0
        if i: b+='<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="1" stroke-dasharray="3 4"/>'%(xx,Y0,xx,Y1,LINE)
        b+=txt(xx+(X1-X0)/8.0,Y1+16,s,8.8,MUTED,anchor="middle")
    b+=txt(24,Y0+12,"visible to",9,MUTED); b+=txt(24,Y0+25,"the user",9,MUTED)
    b+=txt(24,Y1-8,"invisible",9,MUTED)
    b+=txt(352,Y1+38,"evolution  →  everything drifts right, and you cannot stop it",9,ACC,"600",anchor="middle")
    pts={"Customer":(150,62),"Checkout":(214,98),"Fraud score":(198,150),
         "Payment API":(392,124),"Identity":(486,170),"Compute":(566,208)}
    for a,c in [("Customer","Checkout"),("Checkout","Fraud score"),("Checkout","Payment API"),
                ("Payment API","Identity"),("Fraud score","Compute"),("Identity","Compute")]:
        ax,ay=pts[a]; bx,by=pts[c]
        b+='<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="1.2"/>'%(ax,ay,bx,by,LINE)
    style={"Customer":ACC,"Checkout":ACC,"Fraud score":FLAG,"Payment API":VIO,"Identity":VIO,"Compute":GRN}
    for n,(px,py) in pts.items():
        b+='<circle cx="%g" cy="%g" r="6" fill="#FFFFFF" stroke="%s" stroke-width="1.8"/>'%(px,py,style[n])
        b+=lbl(px,py-13,n,9,style[n],"600")
    b+=node(24,286,286,46,"Build only what is left of the line","genesis and custom — that is the differentiator","flag",fs=9.6)
    b+=node(330,286,286,46,"Rent everything right of it","paying staff to run a commodity is paying to lose","grn",fs=9.6)
    b+=txt(24,362,"Two axes and that is the entire notation: a value chain running down from a user need, and",10,MUTED)
    b+=txt(24,377,"evolution running left to right. What makes it a map rather than a diagram is that the pieces",10,MUTED)
    b+=txt(24,392,"move — so it tells you where to invest now, and what to stop building before the market",10,MUTED)
    b+=txt(24,407,"commoditises it underneath you.",10,MUTED)
    return svg(419,b)

# ---------- 9. Integration & API ----------
def d_ratelimit():
    b=""
    b+=inode(24,44,116,44,"Client","API key","soft","user",fs=10)
    b+=inode(162,44,150,44,"Edge / CDN","coarse, per IP","plain","globe",fs=10)
    b+=inode(334,44,150,44,"Gateway","per key, token bucket","acc","shield",fs=10)
    b+=inode(506,44,110,44,"Service","per tenant","acc","server",fs=10)
    b+=arr(140,66,160,66); b+=arr(312,66,332,66); b+=arr(484,66,504,66)
    b+=cyl(334,116,150,46,"Redis","shared counters","amb")
    b+=arr(409,88,409,114,"INCR + TTL",lp=0.5,dy=-2,fs=8.4)
    b+=inode(24,116,286,46,"429 + Retry-After + RateLimit-*","a limit they cannot see is one they cannot respect","flag","warn",fs=9.4,isize=14,pad=8)
    rows=[["Free","100 / min","20","reject"],
          ["Pro","5 000 / min","500","reject"],
          ["Partner","50 000 / min","5 000","shed to queue"],
          ["Internal","no quota","—","alert only"]]
    b+=grid(24,182,592,["Tier","Sustained","Burst","Over the limit"],rows,[0,0.26,0.52,0.72],rh=26,hh=28)
    b+=note(24,308,592,["Limit per key, not per IP: one partner behind one NAT is a single caller, and ten thousand",
                        "mobile clients on one carrier are not. And count in a shared store — a per-instance limiter",
                        "running on eight instances is an eight-times-larger limit than the one in your contract."],AMB)
    b+=txt(24,410,"A rate limit is a product decision written as infrastructure: it decides which customers are",10,MUTED)
    b+=txt(24,425,"able to hurt each other, and it is the cheapest protection you will ever deploy. Publish the",10,MUTED)
    b+=txt(24,440,"numbers, return them in headers on every response, and make the tier a field on the account.",10,MUTED)
    return svg(452,b)

# ---------- 13. Reliability & resilience ----------
def d_backup():
    b=""
    b+=cyl(24,52,150,56,"Primary","Postgres","acc")
    b+=inode(206,50,166,42,"Base backup","nightly full","plain","archive",fs=10)
    b+=inode(206,102,166,42,"WAL shipping","every 60 s","plain","sync",fs=10)
    b+=inode(404,50,212,42,"Object store","versioned · object lock","grn","lock",fs=10)
    b+=inode(404,102,212,42,"Separate region + account","ransomware blast radius","grn","shield",fs=9.4)
    b+=arr(174,71,204,71); b+=arr(174,89,204,123)
    b+=arr(372,71,402,71); b+=arr(372,123,402,123)
    b+=node(24,168,286,46,"RPO = 60 s","the shipping interval — not the nightly backup","amb",fs=9.6)
    b+=node(330,168,286,46,"RTO = 40 min","restore 2 TB, replay WAL, repoint the app","amb",fs=9.6)
    b+=inode(24,232,592,46,"Restored monthly into a scratch account, and timed",
             "an untested backup is a filesystem you are paying to keep","grn","check",fs=10.5)
    b+=note(24,296,592,["Backup is not DR and DR is not backup. Failover moves you onto a replica of the same data, so",
                        "it carries the corruption and the DELETE across with it. Point-in-time restore is the only",
                        "thing that answers “someone dropped the table at 14:05” — and nobody rehearses it."],FLAG)
    b+=txt(24,398,"Three numbers make this real and all three are on the plate: how much data you lose, how long",10,MUTED)
    b+=txt(24,413,"you are down, and when the restore was last actually executed. The third is the one auditors",10,MUTED)
    b+=txt(24,428,"ask for, and the one teams cannot answer.",10,MUTED)
    return svg(440,b)

# ---------- 16. Quality & cross-cutting ----------
def d_qascenario():
    b=""
    b+=node(24,116,108,44,"Utility",None,"acc",fs=12)
    for n,pri,y,c in [("Performance","(H, H)",24,ACC),("Availability","(H, M)",76,GRN),
                      ("Security","(H, H)",128,FLAG),("Modifiability","(M, M)",180,VIO)]:
        b+=node(168,y,150,40,n,pri,"plain",fs=10.5)
        b+=poly([(132,138),(150,138),(150,y+20),(166,y+20)],color=MUTED)
    b+=txt(168,244,"( how much the business cares , how likely we are to miss it )",8.4,MUTED)
    b+=frame(346,20,270,220,"one scenario, all six parts",ACC,dash=False)
    for k,v,y in [("Source","a signed-in customer",54),("Stimulus","submits checkout",82),
                  ("Artefact","the order API",110),("Environment","peak Black Friday load",138),
                  ("Response","order accepted, 201",166),("Measure","p99 < 400 ms, 99.95 % of the hour",194)]:
        b+=txt(360,y,k.upper(),8.2,ACC,"600")
        b+=txt(438,y,v,9,MUTED)
    b+=node(24,270,592,46,"A quality attribute with no measure is a wish",
            "“fast”, “secure” and “scalable” cannot be tested, budgeted, or traded against anything","flag",fs=10.5)
    b+=txt(24,346,"The one artefact here about requirements rather than structure — and the one most often",10,MUTED)
    b+=txt(24,361,"missing, which is why so many reviews argue about boxes instead. Rank every leaf twice, and",10,MUTED)
    b+=txt(24,376,"let only the (H, H) leaves shape the architecture: those are the ones that cost real money to",10,MUTED)
    b+=txt(24,391,"satisfy and real credibility to miss.",10,MUTED)
    return svg(403,b)

def d_tenancy():
    b=""
    specs=[("Silo","stack per tenant",24,"grn",2,2),
           ("Bridge","shared app, DB per tenant",216,"amb",1,2),
           ("Pool","shared everything",408,"flag",1,1)]
    for name,sub,x,st,na,nd in specs:
        c={"grn":GRN,"amb":AMB,"flag":FLAG}[st]
        b+=band(x,20,184,172,name,c,fs=10)
        b+=txt(x+92,60,sub,8.6,MUTED,anchor="middle")
        w=(160-8*(na-1))/float(na)
        for i in range(na):
            b+=node(x+12+i*(w+8),70,w,28,("App %s"%chr(65+i)) if na>1 else "App",None,st,fs=9.2)
        w=(160-8*(nd-1))/float(nd)
        for i in range(nd):
            b+=cyl(x+12+i*(w+8),110,w,46,("DB %s"%chr(65+i)) if nd>1 else "One DB",
                   None if nd>1 else "tenant_id column",st)
    rows=[["Silo","Physical — a bug hits one","Highest","Impossible","Regulated, enterprise"],
          ["Bridge","Data is separated","Medium","Compute only","Mid-market"],
          ["Pool","As good as the WHERE clause","Lowest","All tenants at once","Self-serve, volume"]]
    b+=grid(24,214,592,["Model","Blast radius of a bug","Cost / tenant","Noisy neighbour","Fits"],rows,
            [0,0.14,0.46,0.62,0.81],rh=28,hh=28)
    b+=note(24,338,592,["Most estates end up running all three at once, and that is fine so long as it was chosen: pool",
                        "the free tier, bridge the mid-market, silo the two customers whose contract demands it. What",
                        "is not fine is discovering which model you have by reading a WHERE clause."],AMB)
    b+=txt(24,440,"The decision that shapes everything downstream — schema, backup, migration, incident blast",10,MUTED)
    b+=txt(24,455,"radius and the price list. Decide it once, record it here, and make the tenant boundary a thing",10,MUTED)
    b+=txt(24,470,"the code cannot forget: one filter, in one place, enforced by a test and never by discipline.",10,MUTED)
    return svg(482,b)

def d_caching():
    b=""
    b+=txt(24,24,"LAYERS  ·  each one a separate invalidation problem",9,ACC,"600")
    for n,s2,x,st,ic in [("Browser","Cache-Control 60 s",24,"soft","globe"),
                         ("CDN","stale-while-reval.",166,"plain","cloud"),
                         ("Redis","cache-aside, 5 min",308,"acc","bolt"),
                         ("Database","source of truth",450,"grn","db")]:
        b+=inode(x,38,126,48,n,s2,st,ic,fs=10,isize=13,pad=6)
        if x<450: b+=arr(x+126,62,x+140,62)
    b+=node(24,104,286,44,"Invalidation is the hard half","a TTL is a guess; an event-driven purge is a design","amb",fs=9.4)
    b+=node(330,104,286,44,"Stampede protection","single-flight lock + jittered TTL","flag",fs=9.4)
    b+=txt(24,182,"THE READ PATH  ·  and what a miss actually costs",9,ACC,"600")
    b+=node(24,196,104,38,"Read key",None,"plain",fs=10)
    b+=dia(212,215,116,44,"in cache?","acc",fs=9.5)
    b+=node(318,192,138,34,"Serve  ·  1 ms",None,"grn",fs=9.8)
    b+=node(318,238,138,34,"Load  ·  40 ms",None,"amb",fs=9.8)
    b+=node(478,238,138,34,"Store + jitter",None,"plain",fs=9.8)
    b+=arr(128,215,152,215)
    b+=arr(270,213,316,209,"hit 94 %",lp=0.5,dy=-6,fs=8.6)
    b+=poly([(212,237),(212,255),(316,255)],color=AMB,label="miss 6 %",lx=252,ly=250,fs=8.6)
    b+=arr(456,255,476,255)
    b+=poly([(547,238),(547,215),(462,215)],color=MUTED,dash=True,label="then serve",lx=506,ly=210,fs=8.6)
    b+=note(24,290,592,["94 % is not the number that matters. Six per cent of steady traffic reaching a database sized",
                        "for six per cent is fine; the same six per cent arriving in one second when the cache",
                        "restarts is an outage. Size the origin for the miss storm, not for the average."],FLAG)
    b+=txt(24,392,"The cheapest performance win available, and the most reliable source of “it works on my",10,MUTED)
    b+=txt(24,407,"machine, stale in production”. Three answers are the whole architecture: what the TTL is, who",10,MUTED)
    b+=txt(24,422,"invalidates, and what a cold cache does to the tier behind it.",10,MUTED)
    return svg(434,b)

def d_finops():
    b=""
    b+=txt(24,22,"TAGGING  ·  applied by the platform, never by hand — untagged spend is unattributable spend",9,ACC,"600")
    for n,v,x,w in [("service","order-api",24,142),("team","payments",176,132),
                    ("env","prod",318,104),("cost-centre","CC-4471",432,184)]:
        b+=node(x,32,w,38,n,v,"acc",fs=9.6)
    rows=[["Compute  ·  ECS + Lambda","£18 400","direct","£0.0021 / order"],
          ["Managed data  ·  Aurora","£9 200","direct","£0.0011 / order"],
          ["Egress  ·  NAT + CDN","£6 900","direct","£0.0008 / order"],
          ["Observability  ·  logs","£4 800","shared, by log volume","£0.0006 / order"],
          ["Platform  ·  cluster, mesh","£5 700","shared, by CPU-hour","£0.0007 / order"]]
    b+=grid(24,92,592,["Line","Monthly","Attribution","Unit cost"],rows,[0,0.42,0.58,0.82],rh=26,hh=28)
    b+=node(24,266,286,46,"£45 000 a month","across 8.7 m orders","acc",fs=10.5)
    b+=node(330,266,286,46,"£0.0053 per order","the number to track per release","grn",fs=10.5)
    b+=note(24,330,592,["Shared cost has to be allocated by something, and whatever you pick becomes an incentive:",
                        "charge the cluster by CPU-hour and teams right-size their requests; split it evenly and",
                        "nobody ever does. Unallocated shared cost is the line that quietly grows."],AMB)
    b+=txt(24,432,"The only plate here with money on it, and it belongs here because cost is a quality attribute",10,MUTED)
    b+=txt(24,447,"like latency: settled by the same design choices, and the one the business will actually ask",10,MUTED)
    b+=txt(24,462,"you about. Track cost per unit of work, not total spend — total going up while cost per order",10,MUTED)
    b+=txt(24,477,"goes down is a company that is growing.",10,MUTED)
    return svg(489,b)

# ---------- 17. Evolution & migration ----------
def d_migration():
    b=""
    for t,x,c in [("AS-IS  ·  today",24,MUTED),("TRANSITION  ·  6–18 months",216,AMB),
                  ("TO-BE  ·  target",408,GRN)]:
        b+=band(x,20,184,192,t,c,fs=9.6)
    b+=node(36,56,160,44,"Monolith","everything","soft",fs=10.5)
    b+=cyl(36,112,160,50,"One database",None,"soft")
    b+=arr(116,100,116,110)
    b+=node(228,56,160,32,"Routing facade","by URL prefix","acc",fs=9.4)
    b+=node(228,98,76,34,"Monolith",None,"soft",fs=9)
    b+=node(312,98,76,34,"Orders",None,"grn",fs=9)
    b+=cyl(228,144,160,46,"One database","still shared — split it last","amb")
    b+=arr(266,88,266,96); b+=arr(350,88,350,96)
    b+=node(420,56,160,32,"API gateway",None,"acc",fs=9.4)
    b+=node(420,98,76,34,"Orders",None,"grn",fs=9)
    b+=node(504,98,76,34,"Billing",None,"grn",fs=9)
    b+=cyl(420,144,76,46,"DB",None,"grn"); b+=cyl(504,144,76,46,"DB",None,"grn")
    b+=arr(458,88,458,96); b+=arr(542,88,542,96)
    b+=arr(458,132,458,142); b+=arr(542,132,542,142)
    b+=arr(204,116,214,116); b+=arr(396,116,406,116)
    b+=node(24,232,286,46,"The transition state is an architecture","it runs in production for a year — design it, don’t tolerate it","flag",fs=9.4)
    b+=node(330,232,286,46,"Every step reversible on its own","route back at the facade, in one config change","grn",fs=9.4)
    b+=inode(24,294,592,46,"Strangler fig: the facade is what makes it incremental",
             "new capability in front of the old, old capability retired behind it, caller unaware","acc","branch",fs=10.5)
    b+=txt(24,370,"Almost every real architecture job is a migration, and almost no dictionary has a diagram for",10,MUTED)
    b+=txt(24,385,"one. Draw three states, not two: the middle column is where you will actually live, it is the",10,MUTED)
    b+=txt(24,400,"one nobody designs, and it is the one on call at 3 a.m. Put a date on when it ends, or it",10,MUTED)
    b+=txt(24,415,"quietly becomes the target state.",10,MUTED)
    return svg(427,b)

def d_apiversion():
    b=""
    for n,s2,x,w,stl in [("Preview","no SLA",24,126,"soft"),("Current","supported",166,126,"grn"),
                         ("Deprecated","announced, still works",308,150,"amb"),("Sunset","410 Gone",474,142,"flag")]:
        b+=node(x,44,w,46,n,s2,stl,fs=10.5)
    b+=arr(150,67,164,67); b+=arr(292,67,306,67); b+=arr(458,67,472,67)
    b+=lbl(157,34,"GA",8.4); b+=lbl(299,34,"12 months notice",8.4); b+=lbl(465,34,"window closes",8.4)
    b+=txt(24,122,"TWO VERSIONS IN FLIGHT  ·  and how a caller finds out",9,ACC,"600")
    b+=inode(24,138,140,44,"Client A","pinned to v1","soft","user",fs=9.6)
    b+=inode(24,194,140,44,"Client B","on v2","soft","user",fs=9.6)
    b+=inode(200,138,180,44,"/v1/orders","Deprecation + Sunset hdrs","amb","network",fs=9.6)
    b+=inode(200,194,180,44,"/v2/orders","current","grn","network",fs=9.6)
    b+=inode(416,166,200,44,"Order Service","one codebase, two shapes","acc","server",fs=9.6)
    b+=arr(164,160,198,160); b+=arr(164,216,198,216)
    b+=arr(380,160,414,178); b+=arr(380,216,414,198)
    b+=note(24,256,592,["Three headers turn a deprecation into a contract instead of an email: Deprecation: true,",
                        "Sunset: <http-date>, and a Link header pointing at the migration guide. The caller can then",
                        "alert on their own clock rather than finding out the morning you switch it off."],AMB)
    b+=node(24,358,286,46,"Version the contract, not the code","one codebase serving two shapes beats two deployments","flag",fs=9.4)
    b+=node(330,358,286,46,"Count who is still on v1","you cannot sunset what you cannot measure","grn",fs=9.4)
    b+=txt(24,434,"A version you cannot retire is one you will support forever, so the retirement path is the part",10,MUTED)
    b+=txt(24,449,"of the design that matters. Publish the window when you publish the version, and instrument",10,MUTED)
    b+=txt(24,464,"per-caller usage from day one — the sunset conversation is entirely about that number.",10,MUTED)
    return svg(476,b)

def d_schemaevo():
    b=""
    b+=txt(24,22,"COMPATIBILITY MODE  ·  the registry setting decides who you may upgrade first",9,ACC,"600")
    rows=[["Backward","new code reads old data","add optional, remove a field","consumers first"],
          ["Forward","old code reads new data","add a field, remove optional","producers first"],
          ["Full","both directions hold","add optional, with a default","either, any order"],
          ["None","nothing is checked","anything at all","a coordinated outage"]]
    def cc(r,i,v):
        if r==3: return FLAG
        return INK if i==0 else MUTED
    b+=grid(24,34,592,["Mode","What still reads","The change it allows","Upgrade order"],rows,
            [0,0.15,0.40,0.72],rh=27,hh=28,cellcolor=cc)
    b+=txt(24,196,"SAFE",9,GRN,"600")
    b+=classbox(24,208,258,["orderId  : string","total    : int","currency : string = “GBP”"],"OrderPlaced v4","grn")
    b+=txt(24,304,"a new field with a default — old consumers ignore it",8.8,GRN)
    b+=txt(334,196,"NOT SAFE",9,FLAG,"600")
    b+=classbox(334,208,258,["orderId  : string","total    : decimal","currency : string"],"OrderPlaced v4","flag")
    b+=txt(334,304,"int → decimal is a different type, not a wider one",8.8,FLAG)
    b+=note(24,322,592,["Old events live forever. Anything published today has to stay readable by code written five",
                        "years from now, which is why the only reliably safe change is adding an optional field with",
                        "a default — and why renaming one is a new event type, never an edit."],AMB)
    b+=txt(24,424,"Every event-driven estate reaches this question, usually on the day a consumer breaks in",10,MUTED)
    b+=txt(24,439,"production. Set the mode in the registry before the first event is published, and make the",10,MUTED)
    b+=txt(24,454,"build fail on an incompatible change rather than the consumer fail at 2 a.m.",10,MUTED)
    return svg(466,b)

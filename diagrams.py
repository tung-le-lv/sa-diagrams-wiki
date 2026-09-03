# -*- coding: utf-8 -*-
"""One drawing function per diagram type. Each returns a complete <svg> string."""
from svg_kit import *

# ---------- diagrams ----------
def d_context():
    b=""
    b+=node(240,100,170,58,"Order Platform","the system in scope","acc",fs=13)
    b+=node(40,26,150,46,"Customer","person")
    b+=node(40,182,150,46,"Support agent","person")
    b+=node(460,26,150,46,"Payment provider","external","soft")
    b+=node(460,106,150,46,"Email / SMS","external","soft")
    b+=node(460,186,150,46,"Carrier API","external","soft")
    b+=arr(190,52,238,112,"places orders",lp=0.55,dy=-5)
    b+=arr(190,208,238,148,"handles returns",lp=0.55,dy=12)
    b+=arr(412,116,458,58,"authorises",lp=0.5,dy=-5)
    b+=arr(412,129,458,129,"notifies",dy=-6)
    b+=arr(412,142,458,200,"books shipment",lp=0.5,dy=12)
    return svg(250,b)

def d_container():
    b=""
    b+=node(40,20,140,42,"Web SPA","React")
    b+=node(200,20,140,42,"Mobile app","iOS / Android")
    b+=node(120,92,200,46,"API Gateway",".NET 8","acc")
    b+=node(30,170,150,48,"Order Service",".NET")
    b+=node(200,170,150,48,"Payment Service",".NET")
    b+=node(420,170,180,48,"Stripe","external system","soft")
    b+=cyl(30,250,150,46,"Orders DB","PostgreSQL")
    b+=node(200,252,150,44,"Kafka","event bus","amb")
    b+=node(420,252,180,44,"Notification Service",".NET")
    b+=arr(110,62,180,90)
    b+=arr(270,62,240,90)
    b+=arr(180,138,110,168,"HTTPS / JSON",lp=0.5,dy=-4,fs=9)
    b+=arr(260,138,272,168)
    b+=arr(105,218,105,248)
    b+=arr(275,218,275,250)
    b+=arr(350,194,418,194,"sync, 3s timeout",fs=9)
    b+=arr(180,200,200,200)
    b+=arr(350,274,418,274,"OrderConfirmed",color=AMB,fs=9,dash=True)
    return svg(310,b)

def d_component():
    b=frame(24,22,592,206,"Order Service  ·  container")
    b+=node(52,54,152,46,"OrdersController","REST endpoint")
    b+=node(244,54,168,46,"PlaceOrderHandler","application layer")
    b+=node(452,54,140,46,"OrderRepository","EF Core")
    b+=node(244,140,168,46,"Order","aggregate root","acc")
    b+=node(452,140,140,46,"OutboxPublisher","infrastructure")
    b+=node(52,140,152,46,"OrderValidator","policy")
    b+=arr(204,77,242,77)
    b+=arr(412,77,450,77)
    b+=arr(328,100,328,138,"mutates",lp=0.5,dy=-4,fs=9)
    b+=arr(412,163,450,163)
    b+=arr(204,163,242,163,"rules",dy=-5,fs=9)
    return svg(240,b)

def d_class():
    b=""
    b+=classbox(36,44,164,["+ id : CustomerId","+ email : Email"],"Customer")
    b+=classbox(240,44,176,["+ id : OrderId","+ status : OrderStatus","+ total() : Money","+ place() / cancel()"],"Order","acc")
    b+=classbox(456,44,152,["+ productId","+ quantity : int","+ unitPrice : Money"],"OrderLine")
    b+=arr(200,80,238,80,None)
    b+=lbl(219,72,"places"); b+=lbl(206,94,"1",9.5); b+=lbl(232,94,"0..*",9.5)
    b+='<path d="M 424 80 l 10 -7 l 10 7 l -10 7 z" fill="%s" stroke="%s" stroke-width="1.3"/>'%(ACC_S,ACC)
    b+=arr(444,80,454,80,None,head=False)
    b+=lbl(438,66,"contains"); b+=lbl(420,98,"1",9.5); b+=lbl(452,98,"1..*",9.5)
    b+=txt(36,190,"Filled diamond = composition: order lines cannot exist without the order,",10,MUTED)
    b+=txt(36,205,"which is what makes Order the aggregate root.",10,MUTED)
    return svg(222,b)

def d_state():
    b=""
    b+=pill(30,104,88,34,"Draft")
    b+=pill(146,104,96,34,"Pending","acc")
    b+=pill(270,104,88,34,"Paid")
    b+=pill(386,104,96,34,"Shipped")
    b+=pill(510,104,102,34,"Delivered","grn")
    b+=pill(146,190,96,32,"Cancelled","soft")
    b+=pill(270,26,88,32,"Failed","flag")
    b+=arr(118,121,144,121,"place()",dy=-5)
    b+=arr(242,121,268,121,"authorised",dy=-5,fs=9)
    b+=arr(358,121,384,121,"dispatch()",dy=-5,fs=9)
    b+=arr(482,121,508,121,"delivered",dy=-5,fs=9)
    b+=poly([(200,138),(200,188)],label="cancel()",lx=200,ly=168,color=MUTED)
    b+=poly([(300,104),(300,60)],label="declined",lx=300,ly=88,color=FLAG)
    b+=poly([(270,42),(214,42),(214,102)],color=MUTED,label="retry",lx=238,ly=36)
    b+='<circle cx="20" cy="121" r="5.5" fill="%s"/>'%INK
    b+=arr(26,121,28,121,head=False)
    b+='<circle cx="622" cy="121" r="7" fill="none" stroke="%s" stroke-width="1.4"/><circle cx="622" cy="121" r="4" fill="%s"/>'%(INK,INK)
    b+=arr(612,121,614,121,head=False)
    return svg(238,b)

def d_sequence():
    items=[(24,104,"Client"),(150,104,"Gateway"),(276,116,"Order Svc"),(414,116,"Payment"),(552,76,"Kafka")]
    s,x=lifelines(items,16,276,["plain","plain","acc","plain","amb"])
    b=s
    b+=msg(x[0],x[1],76,"POST /orders")
    b+=msg(x[1],x[2],100,"CreateOrder + idempotency-key")
    b+=selfmsg(x[2],114,"persist, status = Pending")
    b+=msg(x[2],x[3],158,"Authorise  (3s timeout)")
    b+='<rect x="240" y="172" width="330" height="66" rx="3" fill="none" stroke="%s" stroke-width="1.1" stroke-dasharray="5 4"/>'%LINE
    b+=txt(248,185,"alt",9.5,MUTED,"600")
    b+=msg(x[3],x[2],200,"Approved",GRN,dash=True)
    b+=msg(x[2],x[4],200,"OrderConfirmed",AMB)
    b+=msg(x[3],x[2],228,"Declined / no response",FLAG,dash=True)
    b+=msg(x[2],x[0],266,"201 Created  ·  or 202 if uncertain",MUTED,dash=True)
    return svg(288,b)

def d_dfd():
    b=frame(196,20,436,196,"trust boundary")
    b+=node(24,96,150,50,"Customer","external entity","soft")
    b+=node(220,54,150,50,"Validate order","process 1.0","acc")
    b+=node(220,152,150,50,"Charge payment","process 2.0","acc")
    b+='<path d="M 430 60 h 176 M 430 100 h 176" stroke="%s" stroke-width="1.4"/>'%LINE
    b+='<rect x="430" y="60" width="176" height="40" fill="#FFFFFF" opacity="0"/>'
    b+=txt(518,84,"D1  Orders store",11,INK,"600","middle")
    b+='<path d="M 430 158 h 176 M 430 198 h 176" stroke="%s" stroke-width="1.4"/>'%LINE
    b+=txt(518,182,"D2  Payment tokens",11,INK,"600","middle")
    b+=arr(174,116,218,84,"order data",lp=0.5,dy=-6,fs=9)
    b+=arr(370,79,428,79,"write",dy=-5,fs=9)
    b+=arr(295,104,295,150,"valid",lp=0.5,dy=-3,fs=9)
    b+=arr(370,177,428,177,"token",dy=-5,fs=9)
    return svg(228,b)

def d_erd():
    b=""
    b+=classbox(30,40,160,["id  PK","email  UK","created_at"],"CUSTOMER")
    b+=classbox(240,40,164,["id  PK","customer_id  FK","status","total_amount"],"ORDER","acc")
    b+=classbox(452,40,158,["id  PK","order_id  FK","quantity","unit_price"],"ORDER_ITEM")
    b+=classbox(240,168,164,["id  PK","amount","status"],"PAYMENT")
    b+=arr(190,74,238,74,None,head=False)
    b+=lbl(214,68,"places"); b+=lbl(196,88,"1",9.5); b+=lbl(232,88,"0..N",9.5)
    b+=arr(404,74,450,74,None,head=False)
    b+=lbl(427,68,"contains"); b+=lbl(410,88,"1",9.5); b+=lbl(444,88,"1..N",9.5)
    b+=arr(322,140,322,166,None,head=False)
    b+=lbl(352,156,"settled by"); b+=lbl(312,152,"0..1",9.5)
    b+=txt(30,232,"unit_price is stored on the line, not read from the product — price changes",10,MUTED)
    b+=txt(30,247,"must not rewrite history. Snapshot vs reference is the call an ERD forces.",10,MUTED)
    return svg(262,b)

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
    b=frame(24,26,592,238,"VPC  ·  10.0.0.0/16",ACC)
    b+=frame(44,52,552,66,"public subnet")
    b+=inode(60,68,168,36,"NAT gateway",None,"plain","network",fs=10.5)
    b+=inode(240,68,168,36,"Application LB",None,"acc","balancer",fs=10.5)
    b+=inode(420,68,160,36,"Bastion / SSM",None,"soft","terminal",fs=10.5)
    b+=frame(44,132,552,60,"private app subnet")
    b+=inode(60,146,258,36,"Order Service  :8080",None,"plain","server",fs=10.5)
    b+=inode(330,146,250,36,"Payment Service  :8080",None,"plain","server",fs=10.5)
    b+=frame(44,206,552,48,"private data subnet")
    b+=inode(60,216,168,30,"RDS  :5432",None,"plain","db",fs=10,isize=14,pad=8)
    b+=inode(240,216,168,30,"Redis  :6379",None,"plain","bolt",fs=10,isize=14,pad=8)
    b+=inode(420,216,160,30,"S3 endpoint",None,"soft","archive",fs=10,isize=14,pad=8)
    b+=arr(305,104,305,144,"443",lp=0.5,dy=-2,fs=9)
    b+=arr(190,182,190,214,"5432",lp=0.5,dy=-2,fs=9)
    b+=inode(250,0,142,24,"Internet gateway",None,"soft","globe",fs=9.5,isize=13,pad=6)
    b+=arr(321,24,321,66,None)
    return svg(276,b)

def d_oauth():
    items=[(24,116,"Browser / SPA","globe","plain"),(180,116,"Auth server","key","acc"),
           (346,116,"API gateway","shield","plain"),(500,116,"Order Svc","server","plain")]
    s,x=ilifelines(items,16,286,hh=48)
    b=s
    b+=selfmsg(x[0],90,"generate code_verifier + challenge")
    b+=msg(x[0],x[1],132,"/authorize  (code_challenge, scope)")
    b+=msg(x[1],x[0],154,"redirect with authorization_code",MUTED,dash=True)
    b+=msg(x[0],x[1],180,"/token  (code, code_verifier)",ACC)
    b+=msg(x[1],x[0],202,"id_token + access_token",ACC,dash=True)
    b+=msg(x[0],x[2],230,"GET /orders   Bearer …")
    b+=selfmsg(x[2],244,"verify sig, iss, aud, exp, scope")
    b+=msg(x[2],x[3],282,"forward + propagated identity")
    b+=txt(24,312,"The gateway authenticates. The service still authorises — trusting the edge alone is how tenant-isolation bugs happen.",10,MUTED)
    return svg(324,b)

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
    cols=[("Actor","amb",24),("Command","acc",128),("Aggregate","soft",232),("Event","amb",336),("Policy","vio",440),("Read model",  "grn",544)]
    names=["Customer","Place order","Order","OrderPlaced","When placed,\nreserve stock","Order summary"]
    for i,(cap,st,x) in enumerate(cols):
        b+=node(x,60,92,64,names[i].split("\n")[0],(names[i].split("\n")[1] if "\n" in names[i] else None),st,fs=10.5)
        b+=txt(x+46,50,cap.upper(),8.6,MUTED,"600","middle")
        if i<len(cols)-1: b+=arr(x+92,92,x+102,92)
    b+=txt(24,158,"Orange = domain event (past tense). Blue = command. Purple = policy (“whenever X, then Y”).",10,MUTED)
    b+=txt(24,173,"Run it on a wall with the business present. The output isn’t the wall — it’s the contexts you spot",10,MUTED)
    b+=txt(24,188,"where the language changes.",10,MUTED)
    return svg(200,b)

def d_topology():
    b=""
    b+=node(250,110,140,54,"Kafka","3 brokers","amb",fs=13)
    left=[("Order Service","OrderPlaced",24),("Payment Service","PaymentAuthorised",92),("Inventory","StockReserved",160)]
    for i,(n,ev,y) in enumerate(left):
        b+=node(24,y,150,44,n,ev,"plain",fs=10.5)
        b+=arr(174,y+22,248,132,None,AMB)
    right=[("Shipping Service",24),("Notification Service",92),("Analytics sink",160)]
    for n,y in right:
        b+=node(466,y,150,44,n,None,"plain",fs=10.5)
        b+=arr(392,132,464,y+22,None,AMB)
    b+=txt(24,242,"The question it answers: if I change this event’s schema, who breaks?",10.5,MUTED,style="i")
    return svg(256,b)

def d_saga():
    b=""
    steps=[("Order","placed",24),("Payment","authorised",180),("Inventory","rejected",336),("Shipping","not reached",492)]
    sts=["acc","grn","flag","soft"]
    for i,(n,s2,x) in enumerate(steps):
        b+=node(x,46,124,50,n,s2,sts[i],fs=11.5)
        if i<3: b+=arr(x+124,71,x+178,71)
    b+=txt(24,32,"FORWARD PATH",9,MUTED,"600")
    b+=txt(24,140,"COMPENSATION",9,FLAG,"600")
    b+=node(180,154,124,44,"Refund payment",None,"flag",fs=10.5)
    b+=node(24,154,124,44,"Cancel order",None,"flag",fs=10.5)
    b+=poly([(398,96),(398,124),(242,124),(242,152)],color=FLAG,label="StockRejected",lx=320,ly=118,fs=9)
    b+=arr(178,176,150,176,"PaymentRefunded",FLAG,lp=0.5,dy=-6,fs=9)
    b+=txt(24,228,"There is no rollback across services — only a second business transaction that undoes the first.",10,MUTED)
    b+=txt(24,243,"A saga diagram with no compensation arrows is not a saga.",10,MUTED)
    return svg(256,b)

def d_cqrs():
    b=""
    b+=node(24,40,132,46,"Command API","write side","acc",fs=11)
    b+=node(24,110,132,46,"Query API","read side","grn",fs=11)
    b+=node(190,40,140,46,"Order aggregate","validates invariants",fs=11)
    b+=cyl(364,34,132,52,"Write store","normalised")
    b+=node(190,110,140,46,"Projector","denormalises",fs=11)
    b+=cyl(364,104,132,52,"Read store","query-shaped","grn")
    b+=node(530,34,86,52,"Kafka",None,"amb",fs=11)
    b+=arr(156,63,188,63)
    b+=arr(330,60,362,60)
    b+=arr(496,60,528,60,"events",lp=0.5,dy=-5,fs=9)
    b+=poly([(573,86),(573,132),(498,132)],color=AMB)
    b+=arr(330,130,362,130,None,GRN)
    b+=arr(188,133,158,133,None,GRN)
    b+=txt(24,192,"The read model is eventually consistent. Say by how much — “under 2 s at p99” — or the",10,MUTED)
    b+=txt(24,207,"product team will assume zero and design a UI that lies.",10,MUTED)
    return svg(220,b)

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
    b+=arr(190,172,238,172,"mTLS",dy=-5,fs=9)
    b+=arr(400,172,448,172,"mTLS",dy=-5,fs=9)
    b+=txt(30,222,"The mesh gives you mTLS, retries, timeouts and traces without touching application code —",10,MUTED)
    b+=txt(30,237,"at the price of a second control plane to operate and debug.",10,MUTED)
    return svg(250,b)

def d_swimlane():
    b=""
    lanes=[("Customer",30),("Order system",96),("Support agent",184),("Warehouse",250)]
    for n,y in lanes:
        b+='<line x1="120" y1="%g" x2="616" y2="%g" stroke="%s" stroke-width="1"/>'%(y-12,y-12,LINE)
        b+=txt(24,y+12,n,10.5,INK,"600")
    b+='<line x1="120" y1="18" x2="120" y2="304" stroke="%s" stroke-width="1.2"/>'%LINE
    b+='<line x1="120" y1="304" x2="616" y2="304" stroke="%s" stroke-width="1"/>'%LINE
    b+=node(140,26,140,36,"Submit return",None,"plain",fs=10.5)
    b+=node(320,92,132,36,"Within 30 days?",None,"acc",fs=10.5)
    b+=node(140,180,140,36,"Manual review",None,"amb",fs=10.5)
    b+=node(320,246,140,36,"Inspect item",None,"plain",fs=10.5)
    b+=node(486,92,124,36,"Issue label",None,"plain",fs=10.5)
    b+=node(486,158,124,36,"Trigger refund",None,"grn",fs=10.5)
    b+=arr(210,62,340,90)
    b+=poly([(340,128),(340,156),(210,156),(210,178)],color=MUTED,label="no",lx=280,ly=150,fs=9)
    b+=poly([(452,110),(484,110)],color=MUTED,label="yes",lx=468,ly=104,fs=9)
    b+=poly([(280,198),(548,198),(548,130)],color=MUTED,label="approved",lx=430,ly=192,fs=9)
    b+=poly([(548,128),(548,92),(390,92),(390,244)],color=MUTED)
    b+=poly([(460,264),(548,264),(548,196)],color=MUTED,label="item OK",lx=506,ly=258,fs=9)
    b+=txt(24,326,"Every lane crossing is a handoff — a queue, a delay, a place work gets lost. Count them.",10,MUTED)
    return svg(338,b)

def d_bpmn():
    b=""
    b+='<circle cx="44" cy="86" r="15" fill="#FFFFFF" stroke="%s" stroke-width="1.5"/>'%MUTED
    b+=txt(44,120,"start",9,MUTED,anchor="middle")
    b+=node(94,64,124,44,"Receive claim",None,"plain",fs=11)
    b+='<path d="M 296 86 l 30 -30 l 30 30 l -30 30 z" fill="%s" stroke="%s" stroke-width="1.4"/>'%(ACC_S,ACC)
    b+=txt(326,91,"×",16,ACC,"600",anchor="middle")
    b+=txt(326,138,"exclusive gateway",9,MUTED,anchor="middle")
    b+=node(238,20,116,32,"Auto-assess",None,"plain",fs=10.5)
    b+=node(392,64,124,44,"Manual review",None,"amb",fs=11)
    b+='<circle cx="404" cy="108" r="9" fill="#FFFFFF" stroke="%s" stroke-width="1.3"/>'%AMB
    b+='<path d="M 404 103 v 5 l 3 3" stroke="%s" stroke-width="1.2" fill="none"/>'%AMB
    b+=txt(404,132,"timer: escalate after 3 days",9,AMB,anchor="middle")
    b+='<circle cx="576" cy="86" r="15" fill="#FFFFFF" stroke="%s" stroke-width="3"/>'%INK
    b+=txt(576,120,"end",9,MUTED,anchor="middle")
    b+=arr(59,86,92,86)
    b+=arr(218,86,294,86)
    b+=poly([(326,56),(326,36),(360,36)],color=MUTED,label="simple",lx=340,ly=30,fs=9)
    b+=arr(356,86,390,86,"complex",dy=-5,fs=9)
    b+=poly([(354,36),(546,36),(546,80)],color=MUTED)
    b+=arr(516,86,559,86)
    b+=txt(24,182,"BPMN earns its cost when the diagram is executable — handed to Camunda or Temporal,",10,MUTED)
    b+=txt(24,197,"not printed.",10,MUTED)
    return svg(210,b)

def d_pipeline():
    b=""
    st=[("Commit","git push",24,"branch"),("Build + unit","one artefact",144,"gear"),
        ("SAST / SCA","blocking",264,"shield"),("Contract tests","consumer-led",384,"check"),
        ("Sign + SBOM","provenance",504,"cert")]
    for i,(n,s2,x,ic) in enumerate(st):
        b+=inode(x,50,110,46,n,s2,"plain",ic,fs=9.8,isize=13,pad=6)
        if i<len(st)-1: b+=arr(x+110,73,st[i+1][2]-2,73)
    b+=poly([(559,96),(559,128),(367,128)],color=MUTED)
    b+=dia(320,128,90,36,"approve","acc",fs=9.5)
    b+=poly([(275,128),(94,128),(94,154)],color=MUTED)
    b+=inode(24,156,140,44,"Deploy dev","automatic","plain","rocket",fs=10.5)
    b+=inode(180,156,150,44,"Deploy staging","+ smoke tests","plain","rocket",fs=10.5)
    b+=inode(346,156,130,44,"Canary  5 %",None,"acc","pulse",fs=10.5)
    b+=inode(492,156,124,44,"Promote 100 %",None,"grn","check",fs=10.5)
    b+=arr(164,178,178,178); b+=arr(330,178,344,178); b+=arr(476,178,490,178)
    b+=poly([(411,200),(411,226),(94,226),(94,202)],color=FLAG,label="SLO breach → auto rollback",lx=262,ly=240,fs=9)
    b+=txt(24,274,"One immutable artefact promoted across environments — never rebuilt per environment.",10,MUTED)
    return svg(286,b)

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
    b+=poly([(370,213),(450,213),(450,173),(372,173)],color=ACC,label="cut over",lx=488,ly=196,fs=9)
    b+=txt(24,268,"Both strategies run two app versions against one schema — so migrations must expand,",10,MUTED)
    b+=txt(24,283,"backfill, then contract in a later release. That is the step teams forget.",10,MUTED)
    return svg(294,b)

def d_observability():
    b=""
    b+=inode(24,86,140,52,"Services","OTel SDK","acc","server",fs=11)
    b+=inode(180,86,140,52,"Collector","agent + gateway","plain","funnel",fs=11)
    b+=inode(356,20,150,40,"Loki","30 d hot","plain","log",fs=10.5)
    b+=inode(356,92,150,40,"Prometheus","15 s, 13 mo","plain","chart",fs=10.5)
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
    b+=txt(24,240,"Metrics alert you → traces localise it → logs explain it. A pipeline that doesn’t connect all",10,MUTED)
    b+=txt(24,255,"three leaves a gap someone falls into mid-incident. Propagate one trace_id everywhere.",10,MUTED)
    return svg(266,b)

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
    cols=["Option","Delivery speed","Op cost","Team fit","Scale ceiling","Reversibility"]
    xs=[24,164,286,378,470,566]
    b+='<rect x="24" y="30" width="592" height="30" fill="%s" stroke="%s" stroke-width="1.2"/>'%(ACC_S,ACC)
    for i,c in enumerate(cols):
        b+=txt(xs[i]+8,50,c,9.6,"#123F5C","600")
    rows=[["Monolith","Fast","Low","High","Medium","High"],
          ["Modular monolith","Fast","Low","High","High","High"],
          ["Microservices","Slow at first","High","Needs platform","Very high","Low"]]
    fills={"High":GRN,"Fast":GRN,"Very high":GRN,"Low":FLAG,"Slow at first":FLAG,"Needs platform":AMB,"Medium":AMB}
    for r,row in enumerate(rows):
        y=60+r*34
        b+='<rect x="24" y="%g" width="592" height="34" fill="%s" stroke="%s" stroke-width="1.1"/>'%(y,"#FFFFFF" if r%2 else "#F7F8F9",LINE)
        for i,v in enumerate(row):
            col=INK if i==0 else fills.get(v,MUTED)
            w="600" if i==0 else "500"
            if i>0 and (i==2 or i==5):
                col = {"Low":(GRN if i==2 else FLAG),"High":(FLAG if i==2 else GRN)}.get(v,col)
            b+=txt(xs[i]+8,y+21,v,10,col,w)
    b+=txt(24,190,"Two rules keep it honest: weight the criteria before scoring the options, and include",10,MUTED)
    b+=txt(24,205,"reversibility — cheap-to-reverse decisions should be made fast and alone.",10,MUTED)
    return svg(216,b)

def d_rag():
    b=""
    b+=txt(24,26,"INGESTION",9.5,ACC,"600")
    b+=node(24,38,110,42,"Source docs",None,"plain",fs=10.5)
    b+=node(158,38,110,42,"Chunk + metadata",None,"plain",fs=10.5)
    b+=node(292,38,110,42,"Embed",None,"plain",fs=10.5)
    b+=cyl(426,32,140,52,"Vector store","+ ACL filters","acc")
    b+=arr(134,59,156,59); b+=arr(268,59,290,59); b+=arr(402,59,424,59)
    b+='<line x1="24" y1="106" x2="616" y2="106" stroke="%s" stroke-width="1"/>'%LINE
    b+=txt(24,132,"QUERY",9.5,ACC,"600")
    b+=node(24,144,104,42,"Question",None,"plain",fs=10.5)
    b+=node(152,144,104,42,"Embed query",None,"plain",fs=10.5)
    b+=node(280,144,96,42,"Re-rank",None,"plain",fs=10.5)
    b+=node(400,144,110,42,"Prompt + cites",None,"plain",fs=10.5)
    b+=node(534,144,82,42,"LLM",None,"vio",fs=11)
    b+=arr(128,165,150,165); b+=arr(256,165,278,165); b+=arr(376,165,398,165); b+=arr(510,165,532,165)
    b+=poly([(496,84),(496,116),(328,116),(328,142)],color=ACC,label="top-k, filtered by user",lx=412,ly=110,fs=9)
    b+=node(400,214,216,36,"Guardrails + grounding check",None,"amb",fs=10.5)
    b+=poly([(575,186),(575,212)],color=MUTED)
    b+=txt(24,240,"Apply access control at retrieval,",10,MUTED)
    b+=txt(24,255,"never in the prompt.",10,MUTED)
    return svg(268,b)

def d_serverless():
    b=""
    b+=node(24,60,110,44,"API Gateway",None,"acc",fs=10.5)
    b+=node(160,60,120,44,"createOrder","λ · 512 MB",fs=10.5)
    b+=cyl(306,54,124,52,"DynamoDB","orders")
    b+=node(456,20,160,40,"projectReadModel","λ · stream trigger",fs=10.5)
    b+=node(456,86,160,40,"EventBridge",None,"amb",fs=10.5)
    b+=node(306,152,124,40,"SQS",None,"amb",fs=10.5)
    b+=node(160,152,120,40,"fulfil","λ · batch 10",fs=10.5)
    b+=node(24,152,110,40,"DLQ","alarmed","flag",fs=10.5)
    b+=arr(134,82,158,82,"HTTP",dy=-5,fs=9)
    b+=arr(280,82,304,82)
    b+=poly([(430,68),(444,68),(444,44),(454,44)],color=MUTED,label="streams",lx=452,ly=64,fs=9)
    b+=poly([(430,94),(454,94)],color=MUTED)
    b+=poly([(536,126),(536,172),(432,172)],color=AMB,label="events",lx=520,ly=166,fs=9)
    b+=arr(304,172,282,172)
    b+=arr(158,172,136,172,"after 3 retries",lp=0.5,dy=-5,fs=9,color=FLAG)
    b+=txt(24,226,"Label the trigger on every arrow — HTTP, stream, schedule, event — plus concurrency limits",10,MUTED)
    b+=txt(24,241,"and the dead-letter queue. Those are the parts a serverless diagram exists to show.",10,MUTED)
    return svg(252,b)


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
    b+=poly([(534,186),(534,256),(412,256)],color=FLAG,dash=True,label="reads Domain directly — allowed",lx=470,ly=272,fs=9)
    b+=txt(24,306,"Dependencies point inward and Domain depends on nothing. One arrow the other way is an",10,MUTED)
    b+=txt(24,321,"architecture violation you can see from across the room — and can assert in a build test.",10,MUTED)
    return svg(332,b)

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
    b=frame(24,24,592,182,"« component »  Order Service",ACC,dash=False)
    b+=node(72,64,150,50,"orders : Handler","part",fs=10.5)
    b+=node(262,64,150,50,"pricing : Engine","part","acc",fs=10.5)
    b+=node(262,140,150,46,"cache : Redis","part","soft",fs=10.5)
    b+=node(452,64,140,50,"repo : Store","part",fs=10.5)
    for x,y,lab in [(24,84,"IOrders"),(24,160,"IEvents")]:
        b+='<rect x="%g" y="%g" width="16" height="16" fill="#FFFFFF" stroke="%s" stroke-width="1.4"/>'%(x-8,y-8,ACC)
        b+=txt(x-6,y+26,lab,9.5,ACC,"600")
    b+='<rect x="608" y="81" width="16" height="16" fill="#FFFFFF" stroke="%s" stroke-width="1.4"/>'%MUTED
    b+=txt(604,130,"IPayments",9.5,MUTED,"600","end")
    b+=arr(32,84,70,84); b+=arr(222,89,260,89); b+=arr(412,89,450,89)
    b+=poly([(337,114),(337,138)],color=MUTED)
    b+=poly([(32,160),(147,160),(147,116)],color=MUTED)
    b+=arr(592,89,606,89)
    b+=txt(24,240,"Ports are the small squares on the boundary; parts are the instances inside; connectors are the",10,MUTED)
    b+=txt(24,255,"wiring between them. It answers “what does this component require in order to run?”.",10,MUTED)
    return svg(266,b)

def d_communication():
    b=""
    b+=node(38,110,116,44,":Client",None,"plain",fs=11)
    b+=node(240,40,140,44,":OrderService",None,"acc",fs=11)
    b+=node(240,180,140,44,":PaymentService",None,"plain",fs=11)
    b+=node(462,110,140,44,":OrderRepo",None,"plain",fs=11)
    b+='<line x1="154" y1="126" x2="240" y2="72" stroke="%s" stroke-width="1.4"/>'%LINE
    b+='<line x1="310" y1="84" x2="310" y2="178" stroke="%s" stroke-width="1.4"/>'%LINE
    b+='<line x1="380" y1="72" x2="462" y2="126" stroke="%s" stroke-width="1.4"/>'%LINE
    for x,y,dx,dy2,t in [(178,108,20,-4,"1 : place(cmd)"),(320,110,26,0,"2 : authorise()"),
                         (320,150,26,0,"3 : approved"),(410,104,22,-4,"4 : save(order)")]:
        b+='<path d="M %g %g l %g %g" stroke="%s" stroke-width="1.6" marker-end="url(#mka)"/>'%(x,y,dx,dy2,ACC)
        b+=lbl(x+dx/2.0,y+dy2-9,t,9.2,ACC)
    b+=txt(24,262,"Same information as a sequence diagram, arranged by topology rather than by time — the numbers",10,MUTED)
    b+=txt(24,277,"carry the order. Better than a sequence when the shape of the call graph is the point; worse",10,MUTED)
    b+=txt(24,292,"whenever timing, timeouts or alt branches matter, which is most of the time.",10,MUTED)
    return svg(302,b)

def d_timing():
    b=""
    lanes=[("Circuit breaker",["Closed","Open","Half-open"],40),("Downstream API",["Healthy","Failing"],168)]
    x0=150; x1=608
    for name,states,y0 in lanes:
        b+=txt(24,y0+18,name,10.5,INK,"600")
        for i,s in enumerate(states):
            yy=y0+i*30
            b+=txt(140,yy+16,s,9.2,MUTED,anchor="end")
            b+='<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="1" stroke-dasharray="3 4"/>'%(x0,yy+12,x1,yy+12,LINE)
    def seg(y,xa,xb,color=ACC):
        return '<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="2.6"/>'%(xa,y,xb,y,color)
    def step(x,ya,yb,color=ACC):
        return '<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="2.6"/>'%(x,ya,x,yb,color)
    b+=seg(52,150,272); b+=step(272,52,82); b+=seg(82,272,430); b+=step(430,82,112)
    b+=seg(112,430,500); b+=step(500,112,52); b+=seg(52,500,608)
    b+=seg(180,150,240,FLAG); b+=step(240,180,210,FLAG); b+=seg(210,240,470,FLAG)
    b+=step(470,210,180,FLAG); b+=seg(180,470,608,FLAG)
    for x,t in [(240,"t0  errors start"),(272,"t0+20s  trip"),(430,"t0+50s  probe"),(500,"t0+56s  close")]:
        b+='<line x1="%g" y1="34" x2="%g" y2="240" stroke="%s" stroke-width="1" stroke-dasharray="2 4"/>'%(x,x,LINE)
        b+=txt(x,256,t,8.8,MUTED,anchor="middle")
    b+='<line x1="150" y1="240" x2="608" y2="240" stroke="%s" stroke-width="1.2"/>'%LINE
    b+=txt(24,288,"The only UML diagram with a real time axis. Use it when the question is how long something sits in",10,MUTED)
    b+=txt(24,303,"a state — a 30-second cooldown, a 3-second timeout, an SLA measured in milliseconds.",10,MUTED)
    return svg(314,b)

def d_interaction_overview():
    b=""
    b+='<circle cx="46" cy="70" r="8" fill="%s"/>'%INK
    for x,y,w,h,t,st in [(84,44,146,52,"ref  Authenticate","plain"),(276,44,150,52,"ref  Place order","acc"),
                         (276,158,150,52,"ref  Compensate","flag"),(470,44,146,52,"ref  Confirm & notify","plain")]:
        b+=node(x,y,w,h,t,None,st,fs=11)
        b+='<path d="M %g %g h 34 v 14" fill="none" stroke="%s" stroke-width="1.2"/>'%(x,y+14,STYLES[st][1])
    b+=dia(250,180,66,48,"ok?","acc",fs=10)
    b+=arr(54,70,82,70); b+=arr(230,70,274,70)
    b+=poly([(351,96),(351,132),(250,132),(250,156)],color=MUTED)
    b+=arr(283,180,274,180,None,head=False)
    b+=poly([(283,180),(400,180)],color=FLAG,label="no",lx=340,ly=174,fs=9)
    b+=poly([(250,204),(250,238),(543,238),(543,98)],color=MUTED,label="yes",lx=300,ly=232,fs=9)
    b+=txt(24,286,"An activity diagram whose nodes are whole sequence diagrams. Worth drawing exactly once per",10,MUTED)
    b+=txt(24,301,"large flow — as the index page that says which of your twelve sequence diagrams to open.",10,MUTED)
    return svg(312,b)

def d_profile():
    b=""
    b+=classbox(60,44,150,["(UML metaclass)"],"Component","soft")
    b+=classbox(300,44,164,["+ sla : Duration","+ tier : {1,2,3}","+ owner : Team"],"«stereotype»  Service","acc")
    b+='<path d="M 300 76 h -66" stroke="%s" stroke-width="1.3" fill="none"/>'%ACC
    b+='<path d="M 234 76 l 14 -8 v 16 z" fill="%s" stroke="%s" stroke-width="1.3"/>'%(ACC_S,ACC)
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
    b+=arr(321,120,321,138,None,head=False); b+=lbl(348,132,"1 : N",8.8)
    b+=frame(432,22,184,214,"physical  ·  PostgreSQL",ACC)
    b+=classbox(452,52,146,["id  bigint PK","email  citext UK","tier  smallint"],"customer")
    b+=classbox(452,140,146,["id  bigint PK","customer_id  FK idx","placed_at  timestamptz"],"orders","acc")
    b+=arr(525,120,525,138,None,head=False)
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
    b+=node(24,50,116,44,"Sources","OLTP, SaaS","soft",fs=10.5)
    b+=node(160,50,116,44,"Staging","1:1, no logic",fs=10.5)
    b+=frame(296,24,320,166,"core  ·  dimensional model",ACC,dash=False)
    b+=node(400,52,120,44,"FactOrders","grain: 1 line","acc",fs=10.5)
    b+=node(312,118,110,36,"DimCustomer","SCD 2",fs=9.8)
    b+=node(436,118,110,36,"DimDate",None,fs=9.8)
    b+=node(312,52,76,28,"DimProduct",None,fs=9)
    b+=arr(388,66,398,68,None,head=False)
    b+=arr(367,118,420,98,None,head=False)
    b+=arr(470,118,470,98,None,head=False)
    b+=arr(140,72,158,72); b+=arr(276,72,294,72)
    b+=node(24,142,246,44,"Marts  ·  finance, ops, product","one per consumer","grn",fs=10.5)
    b+=poly([(456,190),(456,210),(147,210),(147,188)],color=GRN)
    b+=txt(24,244,"State the grain of the fact table in words on the diagram — “one row per order line per day”.",10,MUTED)
    b+=txt(24,259,"Nearly every warehouse dispute is two people assuming different grains and both being right.",10,MUTED)
    return svg(270,b)

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
    b+=node(154,60,132,46,"Kafka","partitioned log","amb",fs=11)
    b+=frame(306,26,310,150,"stream processing  ·  Flink",ACC,dash=False)
    b+=node(324,54,124,38,"Filter / map","stateless",fs=10)
    b+=node(468,54,132,38,"Window","5 min tumbling","acc",fs=10)
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
    b+=txt(24,272,"Three things make it a design rather than a picture: the partition key (which fixes what is ordered",10,MUTED)
    b+=txt(24,287,"and what parallelises), the window definition, and how late-arriving events are handled. “Kafka”",10,MUTED)
    b+=txt(24,302,"on a box says none of them.",10,MUTED)
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
    b+=arr(276,86,310,86,"watch",dy=-5,fs=8.8)
    b+=arr(382,198,382,208,None,GRN); b+=arr(532,198,532,208,None,GRN)
    b+=inode(180,0,142,22,"Ingress",None,"soft","globe",fs=9.5,isize=12,pad=5)
    b+=poly([(251,22),(251,36),(457,36),(457,206)],color=MUTED,dash=True)
    b+=txt(24,296,"The mental model worth carrying: you write desired state to the API server, controllers reconcile",10,MUTED)
    b+=txt(24,311,"reality toward it, forever. Nothing is “deployed” — it is declared, and drift is corrected.",10,MUTED)
    return svg(322,b)

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
    for x,st,cap,ic in [(44,"grn","2 of 3 needed","server"),(246,"grn","2 of 3 needed","server"),
                        (448,"amb","spare capacity","server")]:
        b+=inode(x,106,150,40,"App × 2",None,st,ic,fs=10.5)
        b+=node(x,158,150,32,cap,None,"soft",fs=9.2)
    b+=poly([(280,56),(119,56),(119,104)],color=MUTED)
    b+=arr(320,56,320,104)
    b+=poly([(360,56),(521,56),(521,104)],color=MUTED)
    b+=inode(24,226,286,44,"N + 1 sizing","each AZ can absorb one AZ failing","grn","check",fs=10.5)
    b+=inode(330,226,286,44,"Quorum data  ·  3 nodes","survives one loss, still writable","grn","db",fs=10.5)
    b+=txt(24,304,"High availability is arithmetic, not a topology: if three AZs each run at 70 % you cannot lose one.",10,MUTED)
    b+=txt(24,319,"Put the utilisation number on the diagram and the sizing argument settles itself.",10,MUTED)
    return svg(330,b)

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
    rows=[["1","Spoofing","Forged JWT","Verify sig + iss + aud"],
          ["2","Tampering","Header injection","Strip and re-issue identity"],
          ["3","Info disclosure","Cross-tenant read","Tenant filter in the query"],
          ["2","Repudiation","No audit of who acted","Signed audit log"],
          ["1","DoS","Unbounded page size","Cap + rate limit per key"]]
    ico=[("id",FLAG),("warn",FLAG),("eye",FLAG),("log",FLAG),("bolt",FLAG)]
    b+=grid(24,130,592,["Flow","STRIDE category","Threat","Mitigation — and where it lives"],rows,
            [0,0.13,0.33,0.60],rh=26,hh=27,rowicons=ico)
    b+=txt(24,308,"The diagram is only the canvas. The work is walking each numbered flow through the six STRIDE",10,MUTED)
    b+=txt(24,323,"categories and writing a mitigation with an owner. An unmitigated row is an accepted risk —",10,MUTED)
    b+=txt(24,338,"which is fine, as long as somebody senior has actually accepted it in writing.",10,MUTED)
    return svg(350,b)

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
    b+=poly([(312,140),(312,162)],color=MUTED,head=False)
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
    b+=node(24,44,124,44,"Producer","key = orderId","acc",fs=10.5)
    b+=frame(180,20,436,140,"topic  orders.v1  ·  6 partitions  ·  RF 3",AMB,dash=False)
    for i,(p,y) in enumerate([("P0",44),("P1",80),("P2",116)]):
        b+=node(196,y,52,26,p,None,"amb",fs=9.5)
        b+=node(256,y,344,26,"offsets ── 0 1 2 3 4 5 6 7 → ordered within the partition only",None,"soft",fs=8.8)
    b+=arr(148,66,194,58,"hash(key)",lp=0.5,dy=-7,fs=8.4)
    b+=frame(24,188,286,96,"consumer group  billing",GRN,dash=False)
    b+=node(40,212,120,32,"instance 1","P0, P1","grn",fs=9.5)
    b+=node(170,212,124,32,"instance 2","P2","grn",fs=9.5)
    b+=node(40,252,254,24,"own offset per partition  ·  scales to 6",None,"soft",fs=8.8)
    b+=frame(330,188,286,96,"consumer group  analytics",MUTED,dash=False)
    b+=node(346,212,254,32,"instance 1","all partitions, own offsets",fs=9.5)
    b+=node(346,252,254,24,"reads the same events, independently",None,"soft",fs=8.8)
    b+=poly([(300,160),(300,176),(167,176),(167,210)],color=AMB)
    b+=poly([(300,176),(473,176),(473,210)],color=AMB)
    b+=txt(24,314,"Three facts do all the work: ordering is per partition, the key chooses the partition, and one",10,MUTED)
    b+=txt(24,329,"partition goes to one consumer per group. So partition count is your maximum parallelism, and",10,MUTED)
    b+=txt(24,344,"any two events that must stay in order have to share a key. Pick the key deliberately.",10,MUTED)
    return svg(356,b)

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
    b+=node(24,84,130,48,"Publisher","knows no subscribers","acc",fs=10.5)
    b+=node(196,84,124,48,"Topic","orders.events","amb",fs=11)
    b+=arr(154,108,194,108)
    subs=[("Billing","filter: type = Placed",20),("Search index","all events",92),("Fraud","filter: amount > 1k",164)]
    for n,f,y in subs:
        b+=node(378,y,150,44,n,f,"plain",fs=10)
        b+=arr(320,108,376,y+22,None,AMB)
        b+=node(548,y+6,68,32,"sub",None,"soft",fs=9)
        b+=arr(528,y+22,546,y+22,None)
    b+=node(196,168,124,44,"DLQ","after 5 attempts","flag",fs=10)
    b+=poly([(378,186),(322,190)],color=FLAG,dash=True,label="poison",lx=350,ly=210,fs=8.8)
    b+=txt(24,254,"The difference from a queue is the fan-out: a queue delivers each message to one consumer, a",10,MUTED)
    b+=txt(24,269,"topic delivers to every subscription. Adding a fourth subscriber must cost the publisher nothing —",10,MUTED)
    b+=txt(24,284,"the moment the publisher needs changing, you have point-to-point integration wearing a topic.",10,MUTED)
    return svg(296,b)

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
    b+=txt(24,164,"10 bespoke integrations, 10 formats, 10 owners",9,MUTED)
    b+='<line x1="352" y1="20" x2="352" y2="178" stroke="%s" stroke-width="1"/>'%LINE
    b+=txt(384,22,"MEDIATED  ·  one contract each",9,GRN,"600")
    b+=node(460,74,120,40,"Integration hub","canonical events","grn",fs=10)
    hub=[(390,34,425,62,492,72),(560,34,595,62,548,72),
         (390,128,425,128,492,116),(560,128,595,128,548,116)]
    for i,(x,y,sx,sy,tx,ty) in enumerate(hub):
        b+=node(x,y,70,28,chr(65+i),None,"soft",fs=10)
        b+=arr(sx,sy,tx,ty,None,GRN)
    b+=txt(384,164,"5 contracts, one format, one team owning the middle",9,MUTED)
    b+=node(24,196,286,44,"Buy vs build vs point-to-point","the actual decision on this page","acc",fs=10.5)
    b+=node(330,196,286,44,"Sync or async per link","and the retry story for each","acc",fs=10.5)
    b+=txt(24,276,"The hub is not automatically right — it centralises change, so it becomes a queue of other teams’",10,MUTED)
    b+=txt(24,291,"work. Below roughly six systems, point-to-point with good contracts wins. Above it, the count of",10,MUTED)
    b+=txt(24,306,"pairwise links is what kills you, and that is the number to put on the diagram.",10,MUTED)
    return svg(318,b)

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
    s,x=lifelines(items,16,240,["soft","acc","plain","amb"])
    b=s
    b+=msg(x[0],x[1],76,"POST /webhooks  {url, events}")
    b+=msg(x[1],x[0],98,"201  + shared secret (shown once)",MUTED,dash=True)
    b+=msg(x[1],x[2],130,"sign(body, secret, timestamp)")
    b+=msg(x[1],x[0],158,"POST url  ·  X-Signature, X-Event-Id",ACC)
    b+=msg(x[0],x[1],182,"2xx within 5 s → done",GRN,dash=True)
    b+=msg(x[0],x[1],206,"5xx / timeout",FLAG,dash=True)
    b+=msg(x[1],x[3],230,"retry 1m, 5m, 30m, 2h, 12h",AMB)
    b+=txt(24,268,"Four things separate a webhook that works from one that pages you: a signature with a timestamp",10,MUTED)
    b+=txt(24,283,"(so replays are rejected), a stable event id (so the receiver can dedupe), bounded retries with",10,MUTED)
    b+=txt(24,298,"backoff, and a way for the partner to re-request what they missed. Fire-and-forget is not delivery.",10,MUTED)
    return svg(310,b)

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
    b+=txt(24,24,"ONE REQUEST  ·  trace 9f2c…  ·  total 412 ms",9.5,ACC,"600")
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
    b+='<line x1="284" y1="40" x2="284" y2="230" stroke="%s" stroke-width="1" stroke-dasharray="3 4"/>'%FLAG
    b+='<line x1="504" y1="40" x2="504" y2="230" stroke="%s" stroke-width="1" stroke-dasharray="3 4"/>'%FLAG
    b+=txt(394,244,"220 ms — 53 % of the request — in one third-party call",9.5,FLAG,"600","middle")
    b+=txt(24,278,"A trace is a tree of spans joined by one id propagated across every hop, including through the",10,MUTED)
    b+=txt(24,293,"broker. Head sampling is cheap and loses the rare slow request; tail sampling keeps the",10,MUTED)
    b+=txt(24,308,"interesting ones and costs more. Decide which, and write it on the diagram.",10,MUTED)
    return svg(320,b)

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
    b+=arr(196,196,354,196,"bidirectional replication",color=AMB,dash=True,dy=-6,fs=9)
    b+=node(24,254,286,44,"Conflicts are guaranteed","last-write-wins loses data silently","flag",fs=10.5)
    b+=node(330,254,286,44,"So partition ownership","each row has exactly one home region","grn",fs=10.5)
    b+=txt(24,330,"Active/active doubles your capacity and removes the failover step — and buys you the hardest",10,MUTED)
    b+=txt(24,345,"problem in distributed data. Either shard so no row is written in two places, or choose a merge",10,MUTED)
    b+=txt(24,360,"rule (CRDT, vector clocks, business rule) and put it on the diagram. Silence here means data loss.",10,MUTED)
    return svg(372,b)

# ---------- 14. Decision ----------
def d_adr():
    b=""
    b+=pill(24,30,116,32,"Proposed","soft")
    b+=pill(180,30,116,32,"Accepted","grn")
    b+=pill(336,30,116,32,"Superseded","amb")
    b+=pill(492,30,124,32,"Deprecated","flag")
    b+=arr(140,46,178,46,"review",dy=-5,fs=9)
    b+=arr(296,46,334,46,"ADR-051",dy=-5,fs=9)
    b+=arr(452,46,490,46)
    b+=frame(24,88,592,166,"ADR-042  ·  Use Kafka for order events",ACC,dash=False)
    secs=[("Context","Three services need order state; nightly batch is too slow.",118),
          ("Decision","Publish domain events to Kafka, keyed by orderId.",156),
          ("Alternatives","Shared database (rejected: coupling). REST fan-out (rejected: n² links).",194),
          ("Consequences","+ decoupled  + replayable   − ops burden  − eventual consistency in the UI",232)]
    for h,t,y in secs:
        b+=txt(44,y,h.upper(),8.8,ACC,"600")
        b+=txt(150,y,t,10,INK if h=="Decision" else MUTED)
    b+='<line x1="140" y1="102" x2="140" y2="244" stroke="%s" stroke-width="1"/>'%LINE
    b+=txt(24,290,"Never edited, only superseded — the record of a decision you later reversed is more valuable than",10,MUTED)
    b+=txt(24,305,"the reversal. Keep them in the repo beside the code, numbered, one page each. If the consequences",10,MUTED)
    b+=txt(24,320,"section lists no downside, no trade-off was made and the ADR is marketing.",10,MUTED)
    return svg(332,b)

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
    for x in (86,242,458):
        b+=poly([(x,222),(x,242),(350,242),(350,260)],color=FLAG,dash=True)
    b+=arr(396,117,246,117,"sync call — a cycle",lp=0.5,dy=-6,fs=8.8,color=FLAG)
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
    b+=node(24,70,110,46,"User",None,"soft",fs=10.5)
    b+=node(150,70,132,46,"Orchestrator","plan · act · observe","acc",fs=10.5)
    b+=node(316,20,132,40,"Model","tool-calling","vio",fs=10.5)
    b+=node(316,76,132,34,"Tools","typed, allow-listed",fs=10)
    b+=node(316,122,132,34,"Retrieval","the RAG plate",fs=10)
    b+=node(316,168,132,34,"Memory","short + long term",fs=10)
    b+=node(490,70,126,46,"Response","cited, checked","grn",fs=10.5)
    b+=arr(134,93,148,93); b+=arr(448,93,488,93)
    b+=arr(282,86,314,42); b+=arr(282,93,314,93); b+=arr(282,100,314,136); b+=arr(282,107,314,182)
    b+=node(24,224,286,44,"Guardrails  ·  in and out","injection, PII, policy, cost cap","flag",fs=10.5)
    b+=node(330,224,286,44,"Evals + traces","every step logged and replayable","grn",fs=10.5)
    b+=poly([(216,116),(216,222)],color=FLAG,dash=True)
    b+=poly([(473,116),(473,222)],color=GRN,dash=True)
    b+=txt(24,300,"Draw the loop, because the loop is what breaks: how many times may it call a tool, what is the",10,MUTED)
    b+=txt(24,315,"token and money ceiling per request, and what happens when the model asks for a tool it should",10,MUTED)
    b+=txt(24,330,"not have? Treat model output as untrusted input to everything downstream — it is.",10,MUTED)
    return svg(342,b)

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
        b+=node(x,50,148,60,n,role,st,fs=11)
        b+=txt(x+74,132,lat,10,ACC,"600","middle")
        if x<468: b+=arr(x+148,80,x+170,80)
    b+='<line x1="24" y1="146" x2="616" y2="146" stroke="%s" stroke-width="1"/>'%LINE
    b+=node(24,166,286,44,"Push outward","latency, bandwidth cost, data residency","grn",fs=10.5)
    b+=node(330,166,286,44,"Keep inward","consistency, expensive compute, state","acc",fs=10.5)
    b+=arr(196,224,196,236,None,GRN); b+=arr(444,236,444,224,None,ACC)
    b+=node(24,240,592,40,"The dividing line is the design: what can be decided with local knowledge, and what cannot",None,"amb",fs=10.5)
    b+=txt(24,314,"Every millisecond of the round trip is on this diagram, which is what makes it useful — a video",10,MUTED)
    b+=txt(24,329,"analytics rule at 100 ms is a different product from one at 5 ms. Push the decision to the tier",10,MUTED)
    b+=txt(24,344,"that has enough information to make it, and no further.",10,MUTED)
    return svg(356,b)

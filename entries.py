# -*- coding: utf-8 -*-
"""Categories, the learning path, and the dictionary entries.

All prose lives here. `alias` carries the other names each type travels under,
so the alternative vocabulary in the source notes stays searchable.
"""
from diagrams import *

# (number, name, slug, what the category is for)
CATS = [
 (1,"Architecture & system-level","architecture-system-level",
    "The whole-system views: what the system is, what it is made of, and how the pieces fit together. "
    "Keep these current — they are the diagrams people actually read."),
 (2,"C4 model","c4-model",
    "Four levels of zoom over one system — context, containers, components, code — "
    "plus the supplementary views the model defines. The most widely understood way to "
    "explain an architecture to someone who was not in the room."),
 (3,"UML","uml",
    "The standard notations. A handful earn their keep in architecture work; the rest are worth "
    "recognising, so you know what you are looking at when someone hands you one."),
 (4,"Interaction & runtime","interaction-runtime",
    "What happens at runtime rather than what exists: the order of messages, the path of a single "
    "request, and where the time actually goes."),
 (5,"Data architecture","data-architecture",
    "How data is structured, where it lives, how it moves between systems, and how you prove where "
    "a number on a report came from."),
 (6,"Deployment & infrastructure","deployment-infrastructure",
    "Where the software actually runs. These settle availability, capacity and cost arguments, "
    "because they are the diagrams that carry numbers."),
 (7,"Security","security",
    "Who can do what, how they prove who they are, and what protects data as it crosses each "
    "boundary between zones of different trust."),
 (8,"Business & domain","business-domain",
    "The views that decide service boundaries before any technology is chosen. A wrong boundary "
    "costs more than any technology choice, and no amount of engineering recovers it."),
 (9,"Event-driven","event-driven",
    "Asynchronous communication: what is published, who consumes it, what is ordered relative to "
    "what, and how a transaction spanning several services unwinds when a step fails."),
 (10,"Integration & API","integration-api",
    "How systems reach each other across team and company boundaries, and who owns each contract."),
 (11,"Process & workflow","process-workflow",
    "Business processes as they are actually executed, in notations that business stakeholders "
    "will read and correct."),
 (12,"DevOps & CI/CD","devops-cicd",
    "How a change reaches production, and how it comes back out. Architecture that cannot be "
    "deployed safely is not finished architecture."),
 (13,"Observability","observability",
    "How you find out something broke, and then why. Design these before go-live, not after the "
    "first incident."),
 (14,"Reliability & resilience","reliability-resilience",
    "How the system behaves when part of it fails, and whether the availability you promised is "
    "arithmetically possible in the first place."),
 (15,"Decision","decision",
    "Not diagrams of systems but of choices: what was decided, what was rejected, and what the "
    "decision now costs you."),
 (16,"Specialised","specialised",
    "Domain-specific architectures. Recognise them all so you know what exists and what it is "
    "called; reach for one when the problem is genuinely that shape."),
 (17,"Quality & cross-cutting","quality-cross-cutting",
    "The concerns that belong to no single service and are therefore owned by nobody until an "
    "architect draws them: what “good” means expressed as numbers, and the decisions — tenancy, "
    "caching, cost — that cut across every box on every other page."),
 (18,"Evolution & migration","evolution-migration",
    "Architecture as a verb. Almost nothing is built from nothing; the real work is moving a "
    "running system, and keeping its contracts honest while you do it."),
]

# The three levels of the learning path. Each builds on the one before it.
# (level, name, what it enables, why it comes at this point)
STAGES = [
 (1,"Foundation","Describe any system, to any audience",
    "The questions asked in every architecture review: what the system is, what it is made of, how a "
    "request moves through it, where it runs, and how its data is shaped."),
 (2,"Core practice","Design and operate a distributed system",
    "What a service estate demands beyond description: where boundaries fall, how services "
    "communicate without coupling, how a change reaches production, and how the system behaves "
    "when part of it fails."),
 (3,"Specialist","Go deep where the domain requires it",
    "Depth for one technology or problem shape. Recognise all of them; reach for one when the "
    "problem is genuinely that shape, and not before."),
]

# The learning path: (level, step, label, entry name). Order is the order to learn them in.
PATH = [
 (1, 1,"System context diagram","System context diagram (C4 level 1)"),
 (1, 2,"C4 container diagram","Container diagram (C4 level 2)"),
 (1, 3,"C4 component diagram","Component diagram (C4 level 3)"),
 (1, 4,"Sequence diagram","Sequence diagram"),
 (1, 5,"Deployment diagram","Deployment diagram"),
 (1, 6,"Cloud architecture diagram","Cloud architecture diagram"),
 (1, 7,"Data flow diagram","Data flow diagram"),
 (1, 8,"ERD","Entity relationship diagram"),
 (1, 9,"Domain model","Domain model"),
 (1,10,"State machine diagram","State machine diagram"),
 (1,11,"Security / auth flow","OAuth 2.0 / OIDC flow"),
 (1,12,"Network diagram","Network / VPC diagram"),
 (2, 1,"Bounded context map","Bounded context map"),
 (2, 2,"Event-driven architecture","Event topology diagram"),
 (2, 3,"CQRS diagram","CQRS diagram"),
 (2, 4,"Saga diagram","Saga diagram"),
 (2, 5,"Integration / API diagram","Integration architecture diagram"),
 (2, 6,"CI/CD diagram","CI/CD pipeline diagram"),
 (2, 7,"DR / failover diagram","Failover / DR diagram"),
 (2, 8,"Observability architecture","Observability architecture"),
 (2, 9,"BPMN / swimlane","Swimlane diagram"),
 (2,10,"Data pipeline / data lineage","Data lineage diagram"),
 (3, 1,"Event storming","Event storming board"),
 (3, 2,"Event sourcing","Event sourcing diagram"),
 (3, 3,"Kafka topology","Kafka topic architecture"),
 (3, 4,"Service mesh","Service mesh diagram"),
 (3, 5,"Kubernetes architecture","Kubernetes architecture diagram"),
 (3, 6,"Zero trust","Zero trust architecture"),
 (3, 7,"Threat model","Threat model (STRIDE)"),
 (3, 8,"Fault tree","Fault tree analysis"),
 (3, 9,"Reliability block diagram","Reliability block diagram"),
 (3,10,"Serverless architecture","Serverless architecture"),
 (3,11,"AI / LLM architecture","LLM application & agent architecture"),
 (3,12,"IoT architecture","IoT architecture"),
 (2,11,"Quality attribute scenarios","Quality attribute scenario model"),
 (2,12,"Caching architecture","Caching architecture"),
 (2,13,"Migration / transition state","Migration & transition-state architecture"),
 (3,13,"Multi-tenancy isolation","Multi-tenancy isolation model"),
]

# Choose by the question you are trying to settle, not by the diagram's name.
QUESTIONS = [
 ("What is our system?","System context diagram (C4 level 1)"),
 ("What are its major pieces?","Container diagram (C4 level 2)"),
 ("What’s inside a service?","Component diagram (C4 level 3)"),
 ("How do requests flow?","Sequence diagram"),
 ("How does data move?","Data flow diagram"),
 ("How is data structured?","Entity relationship diagram"),
 ("How is the domain structured?","Domain model"),
 ("How do services communicate?","Event topology diagram"),
 ("Where does it run?","Deployment diagram"),
 ("How is the network structured?","Network / VPC diagram"),
 ("How does authentication work?","OAuth 2.0 / OIDC flow"),
 ("What happens when something fails?","Failover / DR diagram"),
 ("How is it deployed?","CI/CD pipeline diagram"),
 ("How do we monitor it?","Observability architecture"),
 ("How are business processes executed?","Swimlane diagram"),
 ("Why did we choose this architecture?","Architecture decision record"),
 ("What does “fast enough” actually mean?","Quality attribute scenario model"),
 ("How do we get from here to there?","Migration & transition-state architecture"),
 ("How isolated is one customer from another?","Multi-tenancy isolation model"),
 ("What does all of this cost?","Cost & FinOps attribution view"),
]

# ---------------------------------------------------------------------------
# Primary audience — who the diagram is drawn FOR. It is often the question that
# decides which of two similar diagrams to reach for: a context diagram and a
# container diagram show the same system, but one is for a steering committee and
# the other for the engineers building it.
# (key, label, plural, who that means, what they want from a diagram)
AUDIENCES = [
 ("architect","Architect","architects","Architecture peers, design review, other teams",
   "Wants the boundaries, the trade-off and the consequence. An architect reads every diagram "
   "here; these are the ones drawn primarily for a fellow architect rather than for a specific "
   "delivery need."),
 ("developer","Developer","developers","Engineers building and changing the code",
   "Wants enough precision to implement from: technologies, protocols, contracts, failure "
   "branches. A diagram that omits the timeout is one they cannot code against."),
 ("operations","Operations","operations","SRE, platform engineering and whoever is on call",
   "Wants to know what runs where, what fails, what it looks like when it fails, and what to do "
   "about it at three in the morning. Numbers matter more than shapes."),
 ("security","Security","security","Security review, threat modelling, audit and compliance",
   "Wants boundaries, data classification, and the control on every crossing. Reads a diagram "
   "looking for what is missing rather than for what is there."),
 ("data","Data","data teams","Data engineers, analysts and data stewards",
   "Wants grain, lineage, freshness and ownership — where a number came from, and whether it can "
   "be trusted."),
 ("business","Business","business stakeholders","Business analysts, product and domain experts",
   "Wants the process and the language of the domain, with no technology in the way. If they "
   "cannot correct it out loud, the diagram has failed."),
 ("management","Management","management","Executives, portfolio owners and whoever signs the budget",
   "Wants scope, cost, risk, and what happens if it is not funded. One page, and no notation to "
   "learn first."),
]

# entry name -> (primary audience, [also useful to])
AUDIENCE = {
 "System context diagram (C4 level 1)":       ("management",["architect","business"]),
 "Container diagram (C4 level 2)":            ("developer",["architect"]),
 "Component diagram (C4 level 3)":            ("developer",["architect"]),
 "Code diagram (C4 level 4)":                 ("developer",[]),
 "Solution architecture diagram":             ("management",["architect"]),
 "Logical architecture diagram":              ("architect",["management"]),
 "Physical architecture diagram":             ("operations",["architect"]),
 "Cloud architecture diagram":                ("architect",["operations","developer"]),
 "Reference architecture":                    ("architect",["developer"]),
 "System landscape diagram":                  ("management",["architect"]),

 "Class diagram":                             ("developer",["architect"]),
 "Object diagram":                            ("developer",[]),
 "Package diagram":                           ("developer",["architect"]),
 "Composite structure diagram":               ("developer",["architect"]),
 "Component diagram (UML)":                   ("developer",["architect"]),
 "Profile diagram":                           ("architect",[]),
 "Use case diagram":                          ("business",["architect"]),
 "Activity diagram":                          ("business",["developer"]),
 "State machine diagram":                     ("developer",["architect","business"]),
 "Communication diagram":                     ("developer",[]),
 "Timing diagram":                            ("developer",["operations"]),
 "Interaction overview diagram":              ("architect",["developer"]),

 "Sequence diagram":                          ("developer",["architect"]),
 "Request flow diagram":                      ("operations",["developer"]),
 "Message flow diagram":                      ("architect",["developer"]),
 "Data flow diagram":                         ("security",["architect","data"]),

 "Entity relationship diagram":               ("developer",["data","architect"]),
 "Conceptual, logical & physical data models":("data",["architect","business"]),
 "Data pipeline / ETL–ELT architecture": ("data",["architect"]),
 "Data lineage diagram":                      ("data",["management"]),
 "Data warehouse architecture":               ("data",["architect"]),
 "Data lake / lakehouse architecture":        ("data",["architect"]),
 "Data mesh architecture":                    ("architect",["data","management"]),
 "Streaming data architecture":               ("data",["developer","architect"]),

 "Deployment diagram":                        ("operations",["architect"]),
 "Network / VPC diagram":                     ("operations",["security"]),
 "Kubernetes architecture diagram":           ("operations",["developer"]),
 "Container architecture diagram":            ("operations",["developer","security"]),
 "High availability architecture":            ("operations",["architect","management"]),
 "Multi-region architecture":                 ("architect",["operations"]),

 "OAuth 2.0 / OIDC flow":                     ("developer",["security","architect"]),
 "Identity architecture":                     ("security",["architect"]),
 "Authorisation model diagram":               ("security",["developer"]),
 "Trust boundary diagram":                    ("security",["architect"]),
 "Threat model (STRIDE)":                     ("security",["architect"]),
 "Zero trust architecture":                   ("security",["architect"]),
 "Data classification diagram":               ("security",["business","data"]),
 "Encryption & key management diagram":       ("security",["operations"]),

 "Domain model":                              ("developer",["architect","business"]),
 "Bounded context map":                       ("architect",["management"]),
 "Event storming board":                      ("business",["architect","developer"]),
 "Business capability map":                   ("management",["business"]),
 "Value stream map":                          ("business",["management"]),

 "Event topology diagram":                    ("architect",["developer"]),
 "Saga diagram":                              ("developer",["architect"]),
 "CQRS diagram":                              ("developer",["architect"]),
 "Event sourcing diagram":                    ("developer",["architect"]),
 "Kafka topic architecture":                  ("developer",["operations"]),
 "Outbox pattern diagram":                    ("developer",[]),
 "Pub/sub diagram":                           ("developer",["architect"]),

 "Integration architecture diagram":          ("architect",["management"]),
 "API gateway & BFF diagram":                 ("architect",["developer"]),
 "Webhook flow diagram":                      ("developer",["architect"]),
 "ESB / middleware architecture":             ("architect",["operations"]),
 "Service mesh diagram":                      ("operations",["architect"]),

 "Swimlane diagram":                          ("business",["architect"]),
 "BPMN process model":                        ("business",["developer"]),
 "Flowchart":                                 ("operations",["business","developer"]),

 "CI/CD pipeline diagram":                    ("developer",["operations"]),
 "Release strategy diagram":                  ("operations",["developer","management"]),
 "GitOps architecture":                       ("operations",["developer"]),
 "DevSecOps pipeline":                        ("security",["operations","developer"]),

 "Observability architecture":                ("operations",["architect"]),
 "Metrics architecture":                      ("operations",["developer"]),
 "Distributed tracing diagram":               ("developer",["operations"]),
 "Logging architecture":                      ("operations",["security"]),
 "Alerting & on-call routing":                ("operations",["management"]),

 "Failover / DR diagram":                     ("operations",["management","architect"]),
 "Active/active architecture":                ("architect",["operations"]),
 "Circuit breaker diagram":                   ("developer",["architect"]),
 "Retry & backoff flow":                      ("developer",["operations"]),
 "Bulkhead architecture":                     ("developer",["operations"]),
 "Failure mode diagram (FMEA)":               ("architect",["operations"]),
 "Fault tree analysis":                       ("architect",["operations","management"]),
 "Reliability block diagram":                 ("architect",["management"]),

 "Architecture decision record":              ("architect",["developer"]),
 "Trade-off / decision matrix":               ("management",["architect"]),
 "Decision tree":                             ("developer",["architect"]),

 "Service dependency diagram":                ("operations",["architect"]),
 "Serverless architecture":                   ("developer",["architect"]),
 "RAG architecture":                          ("architect",["developer","security"]),
 "LLM application & agent architecture":      ("architect",["developer","security"]),
 "ML pipeline & MLOps architecture":          ("data",["developer","operations"]),
 "IoT architecture":                          ("architect",["operations"]),
 "Edge computing architecture":               ("architect",["operations"]),

 "Hexagonal architecture (ports & adapters)": ("developer",["architect"]),
 "Concurrency & process view":                ("operations",["developer","architect"]),
 "Data partitioning & sharding strategy":     ("data",["architect","developer"]),
 "Team topologies map":                       ("management",["architect","business"]),
 "Wardley map":                               ("management",["architect","business"]),
 "Rate limiting & quota architecture":        ("architect",["developer","operations"]),
 "Backup & restore architecture":             ("operations",["management","data"]),
 "Quality attribute scenario model":          ("architect",["management","business"]),
 "Multi-tenancy isolation model":             ("architect",["security","developer"]),
 "Caching architecture":                      ("developer",["operations","architect"]),
 "Cost & FinOps attribution view":            ("management",["architect","operations"]),
 "Migration & transition-state architecture": ("architect",["management","developer"]),
 "API versioning & deprecation lifecycle":    ("developer",["architect","business"]),
 "Schema evolution & compatibility":          ("developer",["data","architect"]),
}

# UML 2.5 defines 14 diagram types. Three of them are filed in this dictionary by the job
# they do rather than by their notation — a sequence diagram is reached for as a runtime
# tool, not as "a UML diagram" — so the UML category itself holds 12. This maps the
# canonical set so the category page can show all 14 and say where each one lives.
UML_14 = [
 ("Structural", ["Class diagram", "Object diagram", "Component diagram (UML)",
                 "Composite structure diagram", "Deployment diagram", "Package diagram",
                 "Profile diagram"]),
 ("Behavioural", ["Use case diagram", "Activity diagram", "State machine diagram",
                  "Sequence diagram", "Communication diagram",
                  "Interaction overview diagram", "Timing diagram"]),
]

# C4 defines four levels of zoom plus a supplementary set. Three of the supplementary
# diagrams are filed in this dictionary by the job they do rather than by the model —
# you reach for a sequence diagram as a runtime tool, not as “the C4 dynamic view” — so
# the C4 category itself holds four. This maps the whole set and says where each lives.
C4_SET = [
 ("Core — four levels of zoom", ["System context diagram (C4 level 1)",
                                 "Container diagram (C4 level 2)",
                                 "Component diagram (C4 level 3)",
                                 "Code diagram (C4 level 4)"]),
 ("Supplementary", ["System landscape diagram", "Sequence diagram",
                    "Deployment diagram"]),
]

# ---------------------------------------------------------------------------
# A diagram can belong in more than one category, and several genuinely do — the
# source notes cross-list them themselves. An entry keeps one canonical home (its
# `cat`, which sets its NN.n plate number and its URL) and is *also shown* on the
# category pages listed here, at the given position in that category's order.
#   entry name -> [(category, position in that category's list), ...]
ALSO_IN = {
 "Sequence diagram":       [(3, 1), (10, 3), (2, 6)],
 "Deployment diagram":     [(3, 4), (2, 7)],
 "Activity diagram":       [(11, 3)],
 "State machine diagram":  [(11, 5)],
 "Decision tree":          [(11, 6)],
 "Data flow diagram":      [(5, 2), (7, 5)],
 "Swimlane diagram":       [(4, 5)],
 "Message flow diagram":   [(9, 4), (10, 4)],
 "Event storming board":   [(9, 8)],
 "Service mesh diagram":   [(16, 2)],
 "Multi-tenancy isolation model":             [(7, 6)],
 "Migration & transition-state architecture": [(1, 6)],
 "Schema evolution & compatibility":          [(9, 4)],
 "Caching architecture":                      [(4, 4)],
 "Backup & restore architecture":             [(5, 4)],
 # Not UML. It shares the ports-and-interfaces vocabulary with the composite structure
 # and UML component diagrams, but it is an architectural pattern, not a notation — and
 # category 2 asserts it holds UML 2.5's canonical fourteen. The kinship is a see-also.
 # C4’s supplementary set: filed by the job each does, shown on the C4 page too
 "System landscape diagram":                  [(2, 5)],
 "System context diagram (C4 level 1)":       [(1, 1)],
 "Container diagram (C4 level 2)":            [(1, 2)],
}

E = []
def add(cat,name,tier,defn,answers,when,must,fail,fn,cap,alias=None):
    E.append(dict(cat=cat,name=name,tier=tier,defn=defn,answers=answers,when=when,
                  must=must,fail=fail,svg=fn(),cap=cap,alias=alias or []))

# ================= 1. Architecture & system-level =================
add(2,"System context diagram (C4 level 1)",1,
 "The whole system as a single box, surrounded by every person and external system that touches it. C4 adopted it as level 1, but the context diagram is older than C4 and stands on its own — it is the only architecture diagram a non-technical audience should ever be shown.",
 "Who and what interacts with our system, and where does our responsibility end?",
 "Kickoff, scoping, executive briefings, and the first page of any architecture document.",
 "One box for your system. Every human role. Every external system, marked as external. A short verb on each arrow.",
 "Drawing internal services on it. The moment a second box of yours appears, it is a container diagram.",
 d_context,"A context diagram for an order platform. Five external actors, one system, no internals.",
 ["Context diagram","Scope diagram","Level 1 diagram"])

add(2,"Container diagram (C4 level 2)",1,
 "The deployable units inside your system — applications, services, databases, brokers — and the technology each one is built on. This is the default answer to “explain the architecture”.",
 "What are the separately deployable pieces, and how do they talk?",
 "Almost every architecture conversation with engineers. Keep it current; this is the diagram people actually use.",
 "Technology in brackets on every box. Protocol on every arrow. Solid for synchronous calls, dashed for events.",
 "Boxes with no technology annotation — that is a picture of nouns, not an architecture.",
 d_container,"Containers for the same order platform. Note sync vs async arrows and the external system.",
 ["Application architecture diagram","Level 2 diagram"])

add(2,"Component diagram (C4 level 3)",1,
 "One container opened up: the major structural parts inside a single service and the responsibilities they hold. Worth drawing only for a service whose internals are genuinely non-obvious.",
 "What is inside this one service, and what depends on what?",
 "Onboarding someone to a complex service, or arguing about a refactor.",
 "The container boundary drawn explicitly, so the level of zoom is unambiguous. Layer or responsibility labels.",
 "Drawing one per service as a matter of routine. Most services do not earn a component diagram.",
 d_component,"Inside the Order Service. The aggregate root is the emphasised box.",
 ["Level 3 diagram"])

add(1,"Cloud architecture diagram",1,
 "The system drawn in the provider's own vocabulary — named managed services, wired together as they will really be configured. The most requested diagram in a cloud estate, and the one most often drawn too vaguely.",
 "How do the AWS, Azure or GCP resources fit together, and what does each one guarantee?",
 "Any design on a public cloud, every cost review, and every well-architected-style review.",
 "Real service names, region and AZ boundaries, managed-versus-self-hosted, and where identity is enforced.",
 "Generic boxes — “database”, “queue”, “cache”. The named service is the contract for failover, quotas and price.",
 d_cloud,"Named services, not categories. “Aurora Multi-AZ” answers questions “database” cannot.",
 ["Cloud infrastructure diagram","AWS architecture diagram","Azure architecture diagram","GCP architecture diagram"])

add(1,"Hexagonal architecture (ports & adapters)",2,
 "One service drawn as a core with a boundary: business logic in the middle, a named port for every way in and out, and an adapter outside the boundary for each real technology. The same idea travels as clean architecture and onion architecture.",
 "What is business logic here, what is plumbing, and what could we replace without touching the core?",
 "Any service expected to outlive its current database, broker or web framework — and any codebase where the tests need infrastructure to run.",
 "Which side of the boundary each thing sits on, a named port per interaction, and the direction of every dependency.",
 "Drawing the hexagon and letting an ORM entity leak into the core anyway. If the rule is not asserted in a build test, the picture is aspirational.",
 d_hexagonal,"Driving adapters call in, driven adapters are called out — and the dependency points inward either way.",
 ["Ports and adapters","Clean architecture","Onion architecture","Hexagonal architecture"])

add(1,"Solution architecture diagram",2,
 "One page that puts business capability, applications, integration and data in the same frame — the diagram a steering committee approves before anything is built.",
 "How does the whole solution fit together, and what are we building versus buying?",
 "Programme initiation, funding decisions, vendor selection, and the front page of a solution design document.",
 "Build / buy / reuse on every application, the scope boundary of this programme, and which capability each piece serves.",
 "Drawing it at container-diagram detail. If it needs a protocol label, it belongs on a different page.",
 d_solution,"Four bands on one sheet. The build/buy marks are the decisions the page carries.",
 ["Solution overview","Conceptual architecture","Solution blueprint"])

add(1,"Logical architecture diagram",2,
 "The major building blocks and their responsibilities, with every vendor, product and hostname deliberately removed. The view that survives a re-platforming.",
 "What are the logical building blocks, independent of how they are implemented?",
 "Early design, technology-neutral RFPs, and any conversation that must not become a product argument.",
 "Layers or domains with clear responsibilities, and dependencies flowing in one direction.",
 "Letting a product name creep in. One “Kafka” box and the whole diagram becomes a physical one.",
 d_logical,"Five logical bands. Not one vendor name — that is the discipline the view depends on.",
 ["Logical view","Building block view","Technology-neutral architecture"])

add(1,"System landscape diagram",2,
 "Every system in the organisation on one page, grouped by domain, each marked with who owns it and whether it is being invested in, tolerated or retired.",
 "What systems exist across the organisation, and which ones are we still paying for?",
 "Portfolio review, M&A integration, decommissioning programmes, and your first month in a new organisation.",
 "Ownership, build/buy, lifecycle state, and the integrations — especially the batch jobs nobody claims.",
 "Trying to be complete. A landscape that needs a page of legend is not read; a lossy one-pager is.",
 d_landscape,"Three domains, nine systems, one unowned nightly batch. That last one is the finding.",
 ["Organisation landscape","Application portfolio","Service landscape","Estate map","C4 system landscape"])

add(1,"Physical architecture diagram",3,
 "The same architecture expressed as hardware and capacity: instance types, core counts, IOPS, link speeds — the numbers that decide the bill.",
 "What infrastructure actually hosts this, and how much of it do we need?",
 "Capacity planning, cost modelling, procurement, and data-centre or landing-zone design.",
 "Sizes and counts on everything, plus current utilisation. Otherwise headroom cannot be judged.",
 "Confusing it with the logical view. Stakeholders shown instance types stop hearing the architecture.",
 d_physical,"Named instance classes and storage numbers — capacity arguments settle here.",
 ["Server architecture diagram","Infrastructure diagram","Physical view"])

add(1,"Reference architecture",3,
 "A blueprint teams are expected to follow by default, published once, together with the rule for how to deviate from it.",
 "What architecture pattern should teams follow without asking?",
 "Once you are answering the same design question for the fourth team in a quarter.",
 "The conformance levels — adopt, extend, deviate — and the cost of deviating, which should be one written ADR.",
 "Publishing it as a mandate with no exception path. Teams then deviate silently, and you stop finding out.",
 d_reference,"The standard, and the three honest ways to relate to it.",
 ["Architecture blueprint","Standard pattern","Golden path"])

add(2,"Code diagram (C4 level 4)",3,
 "The innermost C4 ring: the classes and interfaces inside one component. The level the C4 model itself tells you to skip most of the time.",
 "How is this one component actually put together?",
 "A component with a deliberate pattern worth explaining — and generated on demand, not maintained.",
 "The interface boundaries, so the dependency direction is visible. Nothing that an IDE could tell you faster.",
 "Checking it in. A hand-maintained code diagram is wrong within a sprint and misleads everyone who trusts it.",
 d_c4_code,"One component in UML class notation. Note the dependency inversion at the repository boundary.",
 ["Class-level view","Code-level diagram","Level 4 diagram"])


# ================= 2. UML =================
add(3,"State machine diagram",1,
 "Every state an entity can occupy and every legal transition between them. The cheapest bug-finding tool in architecture: drawing one raises the questions nobody asked.",
 "What states exist, and which transitions are legal?",
 "Any entity with a lifecycle — order, payment, subscription, ticket, claim.",
 "The initial state, every terminal state, and the event or method that causes each transition.",
 "A state with no exit. In production that is an entity stuck forever and a support ticket nobody can close.",
 d_state,"An order lifecycle. Can a shipped order be cancelled? The diagram forces the question.",
 ["State transition diagram","Statechart","UML state machine"])

add(3,"Class diagram",3,
 "UML's structural workhorse: types, their attributes and operations, and the relationships between them — with cardinality and ownership carried in the notation itself.",
 "How is the domain model structured, and what owns what?",
 "A domain model that is genuinely subtle. Not for CRUD entities, where an ERD says the same thing faster.",
 "Cardinality on every association, and composition versus aggregation where ownership matters.",
 "Reverse-engineering the whole codebase into UML and checking it in. It is stale the next sprint.",
 d_class,"Three classes and their relationships. Cardinality is the content, not decoration.",
 ["UML class diagram","Structural model"])

add(3,"Activity diagram",2,
 "A flow with real concurrency notation: fork, join, and parallel branches that must all complete. A flowchart that can express “at the same time”.",
 "What are the steps, which run in parallel, and where do they have to synchronise?",
 "Any process with genuine concurrency, and as the behaviour spec behind an orchestration.",
 "Fork and join bars, the decision conditions, and where each path terminates.",
 "Using it where a flowchart or swimlane is clearer. The bars are the reason to choose it — if there are none, do not.",
 d_activity,"Stock and payment run concurrently; the join says both must finish before the order proceeds.",
 ["UML activity diagram","Workflow diagram","Process flow diagram"])

add(3,"Use case diagram",3,
 "Actors outside a boundary, goals inside it. A scoping tool that deliberately says nothing about how anything works.",
 "Who needs what from this system, and what is in this release?",
 "Requirements framing and scope negotiation — particularly with stakeholders who do not read technical diagrams.",
 "The system boundary, every actor including other systems, and goals phrased as outcomes.",
 "Writing UI steps in the ovals. “Place order” is a goal; “click submit” is not.",
 d_usecase,"Scope as a boundary. Every actor outside it is someone whose needs you owe.",
 ["UML use case diagram","Actor–goal diagram"])

add(3,"Component diagram (UML)",3,
 "Components with the interfaces they provide and require, fitted together ball into socket. UML's structural view of replaceable parts — and not the same diagram C4 means by the word.",
 "What does this component offer, what does it need, and what could I swap it for?",
 "Component-based and plug-in designs, and published libraries where the contract is the deliverable.",
 "A named provided and required interface on every connection, so the contract is readable without opening the code.",
 "Confusing it with the C4 component diagram. Same word, different diagram — say which you mean before anyone draws.",
 d_uml_component,"Balls are provided interfaces, sockets required. Where they meet is the contract you can swap either side of.",
 ["UML component diagram","Provided and required interfaces","Lollipop notation"])

add(3,"Package diagram",3,
 "Modules and the dependencies between them — the diagram that makes an architectural rule checkable.",
 "What may depend on what, and where has that been violated?",
 "Layered or hexagonal codebases, modular monoliths, and any rule you intend to enforce in a build test.",
 "Dependency direction on every edge, and the packages that are allowed no outgoing dependencies at all.",
 "Drawing the rule but never asserting it. Encode it as a test or it decays within two sprints.",
 d_package,"Dependencies point inward; Domain depends on nothing. One reversed arrow is a build failure.",
 ["UML package diagram","Module dependency diagram","Layer diagram"])

add(3,"Object diagram",3,
 "A snapshot of specific instances at one moment, with their actual values — a class diagram frozen at runtime.",
 "What does the model look like for this particular case?",
 "Pinning down a confusing example: an edge case in a review, a bug nobody can describe, a test fixture.",
 "Underlined instance names, real values, and only the objects the example needs.",
 "Using it as documentation. It describes one case; the class diagram describes all of them.",
 d_object,"One order on one day. Concrete enough to argue about.",
 ["Instance diagram","UML object diagram","Snapshot diagram"])

add(3,"Communication diagram",3,
 "The same interaction as a sequence diagram, arranged by topology instead of time, with numbered messages carrying the order.",
 "What is the shape of the call graph for this interaction?",
 "When the coupling between participants is the point — showing that one object talks to six others.",
 "Numbering that reflects nesting (1, 1.1, 1.2), and every link the messages travel over.",
 "Using it for anything time-sensitive. Timeouts, retries and alt branches are unreadable in this form.",
 d_communication,"Four participants and nested numbering — 1.1 and 1.2 both happen inside 1. Topology visible; timing not.",
 ["UML collaboration diagram","Object interaction diagram"])

add(3,"Timing diagram",3,
 "State on the vertical axis, real time on the horizontal — the only UML diagram where duration is drawn to scale.",
 "How long does this stay in that state, and what is happening elsewhere while it does?",
 "Timeouts, cooldowns, protocol timing, hard real-time constraints, and embedded work.",
 "A labelled time axis with real units, and every lane sharing it.",
 "Drawing it without units. An unscaled timing diagram is just an awkward state machine.",
 d_timing,"A breaker tripping, waiting out its cooldown, and closing only once the dependency is healthy again. The axis is linear, which is the whole point.",
 ["UML timing diagram","Protocol timing chart"])

add(3,"Composite structure diagram",3,
 "The internals of one component expressed as parts, ports and connectors — what it contains and what it requires to run.",
 "What does this component need wired to it before it works?",
 "Reusable components, plug-in architectures, and embedded or automotive designs where this notation is standard.",
 "Provided and required interfaces on the boundary, so the component's contract is readable from outside.",
 "Reaching for it when a component diagram would do. The extra notation only pays when ports genuinely vary.",
 d_composite,"Ports on the boundary, parts inside, connectors between. Balls are provided, sockets required — the contract is the boundary.",
 ["Composite structure","Internal block diagram","Parts and ports"])

add(3,"Interaction overview diagram",3,
 "An activity diagram whose nodes are entire sequence diagrams — the index page for a flow too big for one sheet.",
 "Which of our twelve sequence diagrams applies here, and in what order?",
 "Large end-to-end flows already documented in pieces: onboarding, claims, settlement.",
 "A reference frame per sub-interaction, and the conditions that route between them.",
 "Inlining the details. The moment a message appears on it, you have drawn a bad sequence diagram.",
 d_interaction_overview,"Four referenced interactions and the branch between them. No messages on this level.",
 ["Interaction overview","Sequence diagram index"])

add(3,"Profile diagram",3,
 "The one UML diagram about UML: it defines the stereotypes and tagged values your other models are allowed to use.",
 "What modelling vocabulary is standard here, and what must every element carry?",
 "Organisations with a mandated modelling tool and a governance function that audits the models.",
 "Each stereotype, the metaclass it extends, and the tagged values it makes mandatory.",
 "Building an elaborate profile nobody adopts. If the tool does not enforce it, it does not exist.",
 d_profile,"A «Service» stereotype that forces every service box to carry an SLA and a tier.",
 ["UML profile","Stereotype definition","Metamodel extension"])


# ================= 3. Interaction & runtime =================
add(4,"Sequence diagram",1,
 "Participants across the top, time running down, messages between them in order. For distributed systems this is the highest-value diagram there is — structure diagrams show what exists, this shows what happens.",
 "What calls what, in what order, and what happens when a step fails?",
 "Any flow with three or more participants. Auth, checkout, saga steps, retries, incident reconstruction.",
 "Timeouts and retries on network hops, idempotency keys, and at least the declined and timed-out branches.",
 "Happy path only. And treating a timeout as a decline — on a timeout you do not know whether it happened.",
 d_sequence,"An order placement with three outcomes, each its own alt operand with a guard. The timeout branch returns 202, not 402.",
 ["UML sequence diagram","Interaction diagram","Call flow diagram","C4 dynamic diagram"])

add(4,"Data flow diagram",1,
 "Processes, data stores, external entities and the data moving between them — with trust boundaries drawn in. The foundation layer for threat modelling and for privacy review.",
 "How does data move through the system, and where does it cross a boundary?",
 "Privacy and compliance reviews, and as the first step of a STRIDE threat model.",
 "Numbered processes, named data stores, and a dashed line wherever trust changes.",
 "Mixing control flow into it. A DFD shows data movement, not the order steps execute in.",
 d_dfd,"A level-1 DFD. Every arrow crossing the dashed boundary is a threat-model question.",
 ["DFD","Level-0 / level-1 data flow","Privacy flow diagram"])

add(4,"Request flow diagram",2,
 "One request traced across every hop, with a latency number on each — a sequence diagram optimised for the performance conversation.",
 "Where does the time actually go?",
 "Performance work, SLO design, and any argument that starts “the API feels slow”.",
 "A measured number per hop, the p99 rather than the mean, and the client-side time as well as the server's.",
 "Measuring only your own services. Most of a page-load budget is usually spent outside them.",
 d_requestflow,"45 ms of server time inside a 255 ms experience. The budget is where the argument ends.",
 ["Call path diagram","Latency budget","Critical path diagram"])

add(4,"Message flow diagram",2,
 "Who sends what to whom: the wiring list of messages, formats and delivery guarantees between systems. No time axis, no request.",
 "What messages exist between these systems, and what does each one promise?",
 "Integration design between teams or companies, and the contract review before either side writes code.",
 "Name and version, payload format, delivery guarantee and ordering scope on every arrow.",
 "Arrows labelled only with a system name. Four unstated properties then get discovered in production.",
 d_messageflow,"Five links, each carrying its contract. This is the artefact two teams sign.",
 ["Event flow diagram","Interface catalogue","Integration contract diagram"])


# ================= 4. Data architecture =================
add(5,"Entity relationship diagram",1,
 "Entities, their attributes, and the cardinality of the relationships between them. The workhorse of data modelling, and the artefact where several consequential decisions get made almost silently.",
 "How is data structured, and what are the real business rules about quantity?",
 "Before any schema exists, and once per bounded context thereafter.",
 "Keys, cardinality on both ends, and — in a microservices estate — which service owns each entity.",
 "One diagram of eighty tables. Split by context and link at the boundaries.",
 d_erd,"An order model. One-or-more line items means an order cannot be empty — a rule in two characters.",
 ["ER diagram","ERD","Schema diagram"])

add(4,"Concurrency & process view",3,
 "What runs as a process, what runs as a thread inside it, what they share, and which of those pools runs out first. The 4+1 view that structure diagrams cannot express.",
 "What is running at once, and which limit do we hit before any of the others?",
 "Capacity work, connection-pool exhaustion, deadlocks, and any service where autoscaling made things worse rather than better.",
 "Pool sizes and replica counts as arithmetic, the shared resource they all contend for, and its ceiling.",
 "Counting threads and forgetting connections. The bound that bites is almost never CPU — it is a pool somebody sized once, for one replica.",
 d_processview,"Two processes, four pools, and fifty connections against a limit of a hundred. Double the replicas and the arithmetic breaks.",
 ["Process view","4+1 process view","Concurrency model","Threading model"])

add(5,"Data pipeline / ETL–ELT architecture",2,
 "How data gets from where it is produced to where it is consumed: ingestion, landing, transformation, serving — and how it is reprocessed when something was wrong.",
 "How does data arrive, get shaped and reach a consumer, and what happens on a rerun?",
 "Every analytics platform, every reporting programme, every migration.",
 "Freshness per path, whether transformation runs before or after loading, and the backfill route.",
 "No immutable raw landing zone. Without one, a bad transform is data loss rather than a re-run.",
 d_datapipeline,"Batch above, stream below, with the two paths that make it operable: contracts and backfill.",
 ["Data pipeline diagram","ETL architecture","ELT architecture","Ingestion architecture"])

add(5,"Data lineage diagram",2,
 "The path a value takes from the system that produced it to the report someone is questioning, through every hop and transform along the way.",
 "Where did this number come from?",
 "The day the pipeline is designed — not the day the auditor asks.",
 "Every hop, the transform at each one, and where the data lands for each consumer.",
 "Treating it as a documentation chore. It is the answer to the most expensive question finance asks.",
 d_lineage,"Source to dashboard. Two consumers off one warehouse, which is where reconciliation disputes start.",
 ["Data provenance diagram","Impact analysis diagram"])

add(5,"Conceptual, logical & physical data models",2,
 "The same data at three altitudes: business concepts, a vendor-neutral normalised model, and the actual DDL with its types and indexes.",
 "Which version of the data model is this, and who is it for?",
 "Any modelling effort that involves both business stakeholders and a DBA — which is most of them.",
 "A stated level. Conceptual carries no keys; logical carries no types; physical carries everything.",
 "Showing a physical model to business stakeholders and calling the review done.",
 d_datamodels,"One domain, three audiences. Mixing the levels is what makes data reviews go badly.",
 ["Conceptual data model","Logical data model","Physical data model"])

add(5,"Data warehouse architecture",2,
 "Staging, a dimensional core, and marts per consumer — the classic analytical stack and the grain decisions inside it.",
 "How is analytical data organised, and at what grain?",
 "Reporting platforms, financial reconciliation, and anywhere “the numbers disagree” is a recurring complaint.",
 "The grain of each fact table written in words, and how slowly-changing dimensions are handled.",
 "Leaving the grain implicit. Nearly every warehouse dispute is two people assuming different grains.",
 d_warehouse,"A star schema with its grain stated. “One row per order line per day” ends most arguments.",
 ["Dimensional model","Star schema diagram","Kimball architecture"])

add(5,"Streaming data architecture",3,
 "Continuous data through a partitioned log into stateful processing and out to serving stores — with windows, keys and late arrivals made explicit.",
 "How is data processed continuously, and what is ordered relative to what?",
 "Sub-minute freshness requirements: fraud, telemetry, pricing, personalisation.",
 "The partition key, the window definition, and the late-arrival policy.",
 "A box labelled “Kafka” and nothing else. None of the three decisions that matter is visible.",
 d_streaming,"Ingest, window, join, serve. The key and the window are the design.",
 ["Event streaming architecture","Real-time pipeline","Stream processing diagram"])

add(5,"Data lake / lakehouse architecture",3,
 "Raw, cleaned and business-ready tiers over one open-format storage layer, queried by SQL and ML alike.",
 "Where does raw data live, and how does it become trustworthy?",
 "Large or semi-structured estates, and anywhere a warehouse and a lake are drifting into two truths.",
 "What each tier promises about quality, the table format, and who may read which tier.",
 "A lake with no catalogue or tiering. That is a swamp, and the term is not affectionate.",
 d_lakehouse,"Bronze, silver, gold over one transactional storage layer. The tier names are a promise.",
 ["Data lake architecture","Lakehouse","Medallion architecture"])

add(5,"Data mesh architecture",3,
 "Analytical data owned by the domains that produce it, published as products with SLOs, on a self-serve platform under federated governance.",
 "Who owns this data, and to what standard?",
 "Large organisations where a central data team has become the bottleneck for every domain.",
 "All four pillars. Domain ownership without a platform and governance is just a decentralised mess.",
 "Adopting the label without the platform. Domains cannot own products they have no tooling to publish.",
 d_datamesh,"Domains in the middle, governance above, platform below. Remove either band and it fails.",
 ["Data mesh","Data product architecture"])


# ================= 5. Deployment & infrastructure =================
add(6,"Deployment diagram",1,
 "Where the software actually runs: regions, availability zones, nodes, instance counts, and the replication between data stores. Where availability and cost arguments are finally settled.",
 "Where does everything run, and what survives when part of it dies?",
 "Every production design, and every conversation about an SLA.",
 "Zone and region boundaries, replication direction and mode, where state lives, and rough instance counts.",
 "Omitting availability zones. Without them the diagram cannot answer a single HA question.",
 d_deploy,"Multi-AZ with one primary. The picture admits that an AZ-A failure means a write pause.",
 ["Deployment view","Runtime infrastructure diagram","UML deployment diagram","C4 deployment diagram","Microservices deployment"])

add(5,"Data partitioning & sharding strategy",3,
 "How one logical dataset is split across many physical stores, chosen by a key — and what that key costs you at every query and every rebalance thereafter.",
 "How is this data split, and what happens when we outgrow the number of shards we picked?",
 "Any dataset that will not fit one node, any residency requirement, and every “the database is the bottleneck” conversation.",
 "The shard key, the strategy it implies, the query shapes it makes cheap and expensive, and the rebalance plan.",
 "Choosing the key for the write path. You write a row once and query it for years; optimise for the read you cannot avoid.",
 d_sharding,"Three strategies and their real trade-offs. The rebalance plan is what decides whether the choice survives growth.",
 ["Sharding diagram","Partitioning strategy","Horizontal partitioning","Shard key design"])

add(6,"Network / VPC diagram",1,
 "Subnets, routing and reachability: what can talk to what, on which port, across which boundary.",
 "What is reachable from where?",
 "Security review, connectivity debugging, and anything that has to satisfy an auditor.",
 "CIDR ranges, public versus private subnets, ports on the arrows, and the egress path.",
 "Drawing intended connectivity rather than actual. Generate it from your IaC where you can.",
 d_vpc,"A three-tier VPC. CIDR per subnet, ports on the arrows and the egress path drawn — that is what makes it reviewable.",
 ["Network diagram","VPC diagram","Subnet diagram","Network security diagram"])

add(6,"High availability architecture",2,
 "Redundancy inside one region, drawn with the arithmetic: how many instances, spread how, at what utilisation.",
 "What can fail here without users noticing?",
 "Any availability target above about 99.5 %, and every capacity review.",
 "Per-zone utilisation, the N+1 or N+2 sizing rule, and the quorum requirement for stateful components.",
 "Three zones at 70 % utilisation. Losing one means the survivors need 105 % — the diagram shows it, words do not.",
 d_ha,"Redundancy as arithmetic: 45 % per zone survives losing one, 70 % does not. Same topology, different number.",
 ["Redundancy diagram","Fault tolerance diagram"])

add(6,"Multi-region architecture",2,
 "The system in more than one region, and the data decision that follows: partitioned by region, or replicated everywhere.",
 "How do we serve two continents, and what happens to data written in both?",
 "Latency requirements across geographies, data residency law, and region-level resilience.",
 "How traffic is routed, whether any request crosses regions synchronously, and the replication lag.",
 "Skipping the data decision. Every unresolved multi-region design is really an unresolved conflict question.",
 d_multiregion,"Two active regions, data partitioned by customer home. No synchronous cross-region hop.",
 ["Global architecture","Geo-distributed architecture"])

add(6,"Kubernetes architecture diagram",3,
 "Control plane, nodes, pods and services — and the reconciliation loop that is the whole mental model.",
 "How does a workload actually get scheduled and reached in this cluster?",
 "Onboarding onto Kubernetes, cluster design, and debugging why something is not where you expected.",
 "The control-plane components, how pods are selected by services, and where ingress terminates.",
 "Drawing it as a deployment pipeline. Nothing is deployed here; state is declared and continuously reconciled.",
 d_k8s,"Control plane left, workers right. The arrow that matters is the watch, not the deploy.",
 ["Kubernetes cluster diagram","K8s architecture","Container orchestration diagram"])

add(6,"Container architecture diagram",3,
 "Image build, registry and runtime, plus the layer structure and the base-image policy behind them.",
 "What is in the image we are running, and how does a fix reach every service?",
 "Supply-chain reviews, CVE response planning, and standardising build practice across teams.",
 "Base image ownership and patch cadence, layer ordering, and pinning by digest rather than tag.",
 "Deploying by mutable tag. Then nobody can answer what is actually running in production.",
 d_containerarch,"Build, registry, runtime — and the layer order that decides your rebuild cost.",
 ["Image supply chain","Docker architecture diagram"])


# ================= 6. Security =================
add(7,"OAuth 2.0 / OIDC flow",1,
 "The exact sequence by which a caller obtains a token and a service decides to trust it. Being able to draw this from memory is a real differentiator.",
 "How does a caller prove who they are, and what does the token actually authorise?",
 "Any federated, delegated or multi-tenant access design.",
 "PKCE for public clients, token lifetimes, refresh, and which party validates which claim.",
 "Implicit grant in a new design — it is deprecated. And assuming the gateway's authentication is also authorisation.",
 d_oauth,"Authorisation code flow with PKCE. The service still authorises after the gateway authenticates.",
 ["Authentication flow diagram","OAuth 2.0 flow","OIDC flow","SSO flow","Security / auth flow"])

add(7,"Trust boundary diagram",2,
 "Concentric zones of decreasing exposure, with the assets and controls in each. The canvas a threat model is drawn on.",
 "Where does data cross into a less-trusted zone, and what protects it there?",
 "Design review of anything internet-facing, and as the starting point for STRIDE.",
 "What crosses each boundary, in what form, and the encryption state in transit and at rest.",
 "Showing security only at the perimeter. Internal service calls need authentication too.",
 d_trust,"Three nested boundaries. Each crossing is one round of spoofing, tampering and disclosure questions.",
 ["Security architecture diagram","Security zones diagram"])

add(7,"Identity architecture",2,
 "Where identities come from, how they are provisioned and de-provisioned, and what issues the tokens everything else trusts.",
 "Who is the source of truth for identity, and what happens the hour someone leaves?",
 "Workforce and customer identity design, mergers, and any audit involving access control.",
 "The directory of record, provisioning path, token lifetimes and audience, and the break-glass account.",
 "Designing sign-in beautifully and leaving de-provisioning manual. That is the control auditors actually test.",
 d_identity,"Sign-in is the easy half. The bottom row is where audits are lost.",
 ["IAM architecture","Federation diagram","Directory architecture"])

add(7,"Authorisation model diagram",2,
 "How a permission decision is made and where: roles, attributes or relationships, with the decision point separated from enforcement.",
 "Who can do what to which record, and where is that decided?",
 "Multi-tenant systems, anything with delegated administration, and the first time “can they see this?” takes a day to answer.",
 "The model actually implemented, where the decision is made, and what is cached and for how long.",
 "Scattering ad-hoc rules across services. Nobody can then answer who has access to a record.",
 d_authz,"Enforcement stays local, the decision is centralised — and the two are not the same thing.",
 ["Authorization flow diagram","RBAC diagram","ABAC model","Permission model"])

add(7,"Threat model (STRIDE)",3,
 "A data flow diagram with boundaries, walked flow by flow through six threat categories, each row ending in a named mitigation and an owner.",
 "What can go wrong here, and what are we doing about each one?",
 "Before build for anything internet-facing or handling regulated data — and again after a significant change.",
 "A numbered flow per row, the threat, the mitigation, and where that mitigation lives in the code.",
 "Producing the diagram and skipping the table. The diagram is the canvas; the rows are the work.",
 d_threat,"Three flows walked through all six STRIDE categories, each row ending in a mitigation with a home. Unmitigated rows are accepted risk — in writing.",
 ["Threat model diagram","STRIDE analysis","Attack surface diagram"])

add(7,"Zero trust architecture",3,
 "No implicit trust from network position: every request authenticated, authorised and encrypted, against live signals about user, device and resource.",
 "Why is a request from inside the network treated no differently from one outside it?",
 "Remote-first estates, contractor and partner access, and any programme retiring a flat internal network.",
 "The enforcement point on the request path, the signals feeding the decision, and the TTL on a cached answer.",
 "A VPN at the edge and free movement behind it. That is a perimeter with new branding.",
 d_zerotrust,"Enforcement inline, decision central, signals live. The TTL is the part people forget.",
 ["Zero trust network access","BeyondCorp architecture"])

add(7,"Data classification diagram",3,
 "The sensitivity tiers your data falls into, and the concrete handling rule for each: access, residency, retention.",
 "How sensitive is this, and what does that oblige us to do?",
 "Privacy programmes, regulated data, and any residency or retention commitment already in a contract.",
 "A named control per class, not an adjective. Engineers must be able to read off what to build.",
 "Seven classes. Anything beyond about four collapses into “internal” for everything.",
 d_classification,"Four classes, each with a control an engineer can implement without asking legal.",
 ["Sensitivity matrix","Data handling policy diagram"])

add(7,"Encryption & key management diagram",3,
 "Envelope encryption drawn out: root key, key-encrypting keys, per-object data keys, and who can use which.",
 "Where are the keys, who can use them, and how do we rotate or destroy them?",
 "Regulated data, multi-tenant isolation, and any contract promising deletion or key separation.",
 "The key hierarchy, rotation cadence per level, and what deletion of a key actually destroys.",
 "One key for everything. Rotation then means re-encrypting everything, so it never happens.",
 d_keymgmt,"Rotation becomes a re-wrap; deletion becomes crypto-shredding. Both are contractual promises.",
 ["Key management architecture","Envelope encryption diagram","KMS architecture"])


# ================= 7. Business & domain =================
add(8,"Domain model",1,
 "Aggregates, entities and value objects with the invariants each aggregate enforces — the model the code should be shaped like, not a picture of tables.",
 "How is the domain structured, and where does consistency have to hold?",
 "Any non-trivial business domain, and before deciding transaction boundaries or service boundaries.",
 "The aggregate boundary, the root, the invariants it enforces, and references to other aggregates by id only.",
 "An anaemic model — boxes of fields with no behaviour. That is a schema wearing a domain model's clothes.",
 d_domainmodel,"One aggregate, its invariants, and id-only references outward. One transaction, one aggregate.",
 ["DDD aggregate diagram","Domain map","Rich domain model"])

add(8,"Bounded context map",2,
 "The distinct models in a domain and the relationships between the teams that own them. This is the diagram that decides your service boundaries — and a wrong boundary costs more than any technology choice.",
 "Where should the seams between systems and teams fall?",
 "Before deciding on services. Always before, never after.",
 "The relationship pattern on each edge: customer/supplier, conformist, anti-corruption layer, shared kernel.",
 "Deriving services from the database schema instead of from where the language changes.",
 d_context_map,"Four contexts. The anti-corruption layer is what keeps a vendor's model out of yours.",
 ["Context mapping diagram","DDD context map","Domain boundary map"])

add(8,"Team topologies map",2,
 "The organisation drawn as an architecture: four kinds of team, three ways they are allowed to interact, and the platform underneath. The socio-technical half of every boundary decision.",
 "Who owns what, and how are these teams allowed to talk to each other?",
 "Alongside the bounded context map, never after it — and before any reorganisation justified by an architecture goal.",
 "The team type of every box, the interaction mode on every edge, and whether any team’s cognitive load is plainly impossible.",
 "Drawing the teams you have and calling it a design. The point is to choose the shape you want the system to take.",
 d_teamtopo,"Four team types, three interaction modes, one platform. If it disagrees with the context map, one of the two is wrong.",
 ["Team topologies","Socio-technical architecture","Inverse Conway diagram","Team interaction model"])

add(8,"Event storming board",3,
 "A wall of coloured stickies built with the business in the room: events in time order, the commands that cause them, the policies that react. A discovery technique whose real output is the boundaries you find.",
 "What actually happens in this business, in what order?",
 "Early discovery, with domain experts present. It does not work as a solo exercise.",
 "Events in past tense, on a timeline. Hot spots marked where the room disagrees.",
 "Treating the board as the deliverable. The deliverable is the contexts you spotted.",
 d_storming,"Seven colours, no two alike, on a timeline — plus the hot spot the room could not agree on. Language shifts along the line are where contexts divide.",
 ["Event storming model","Big picture workshop","Process modelling workshop"])

add(8,"Business capability map",3,
 "What the business does, expressed as stable capabilities rather than teams or systems, shaded by how well each is served today.",
 "What does this organisation actually do, and where are we weakest?",
 "Portfolio planning, investment cases, and mapping systems to purpose during a reorganisation.",
 "Two levels at most, a maturity or coverage colour, and no org-chart names anywhere on it.",
 "Drawing the org chart with different words. Capabilities outlive both teams and systems — that is the point.",
 d_capability,"Colour by how well each capability is served and the funding conversation writes itself.",
 ["Capability model","Business architecture map"])

add(8,"Value stream map",3,
 "A process with the clock attached: work time and wait time on every step, and the ratio between them.",
 "Where does the time really go in this process?",
 "Process improvement, automation business cases, and lead-time complaints.",
 "Process time and wait time separately per step, and the totals. The gap between them is the finding.",
 "Optimising the work. Efficiency is usually under 5 % — the queues are the problem, not the steps.",
 d_valuestream,"Fifteen minutes of work inside 6.4 days of elapsed time. Automate the approval, not the typing.",
 ["Value stream","Lead time analysis"])


# ================= 8. Event-driven =================
add(9,"Event topology diagram",2,
 "Which services publish which events and which consume them — the map of an event-driven estate.",
 "If I change this event's schema, who breaks?",
 "The moment you have more than a handful of topics and more than one team.",
 "Schema version per event, the partition key, and where the registry lives.",
 "Naming events as commands. OrderPlaced is a fact; ShipOrder is an instruction to one handler.",
 d_topology,"Publishers, broker, consumers. The fan-out on the right is your blast radius for a schema change.",
 ["Event-driven architecture diagram","Event flow diagram","Publish/subscribe map"])

add(8,"Wardley map",3,
 "A value chain plotted against how evolved each part is, from a one-off invention to a metered commodity. The only diagram here that tells you what to stop building.",
 "Which parts of this are worth our engineers, and which are we about to be undercut on?",
 "Investment cases, build-versus-buy at portfolio scale, and any argument about a platform team’s remit.",
 "Both axes — anchored on a real user need, and each component placed honestly on the evolution axis rather than where it flatters you.",
 "Placing components where you wish they were. A map on which everything you own is novel is a map drawn to justify a budget.",
 d_wardley,"A value chain against evolution. Build to the left of the line, rent to the right — and everything drifts right.",
 ["Wardley mapping","Value chain map","Evolution map"])

add(9,"Saga diagram",2,
 "A business transaction spanning several services, drawn with its compensating actions. There is no rollback across services — only a second transaction that undoes the first.",
 "How does a multi-service transaction complete, or unwind when a step fails?",
 "Any process that must stay consistent across service boundaries.",
 "The compensation for every forward step, and a timeout branch for any step that may never answer.",
 "No compensation arrows. Then it is not a saga, it is a wish.",
 d_saga,"Choreographed saga. Inventory rejects, so payment compensates — the forward path never completes.",
 ["Distributed transaction diagram","Compensation flow","Process manager diagram"])

add(9,"CQRS diagram",2,
 "Separate models for writing and for reading, connected by events or a projection. Sold as a scaling pattern; bought as a consistency problem.",
 "How do the write and read models differ, and how far apart can they drift?",
 "Read-heavy contexts where query shapes and write invariants genuinely conflict.",
 "The projection lag, stated as a number, and what the UI does while the read model is behind.",
 "Adopting it estate-wide. Most contexts want one model and a well-indexed table.",
 d_cqrs,"Command side, event, projection, query side — and the lag between them.",
 ["Command query responsibility segregation","Read model diagram"])

add(9,"Outbox pattern diagram",2,
 "A local table written in the same transaction as the business change, drained afterwards by a relay — the standard answer to the dual-write problem.",
 "How do we change the database and publish an event without losing one of them?",
 "Every service that both owns data and publishes events. Which is most of them.",
 "One transaction spanning both writes, the relay mechanism, and at-least-once delivery stated plainly.",
 "Publishing inside the transaction and hoping. A crash between the two leaves silent, permanent divergence.",
 d_outbox,"One transaction, two rows, a relay after the fact. Consumers must be idempotent.",
 ["Transactional outbox","Dual-write pattern"])

add(9,"Kafka topic architecture",3,
 "Topics, partitions, keys and consumer groups — the four facts that determine ordering and parallelism.",
 "What is ordered relative to what, and how far can this scale out?",
 "Any serious Kafka design, and every “why is this consumer lagging?” investigation.",
 "Partition count, the key that chooses the partition, replication factor, and each consumer group's assignment.",
 "Assuming global ordering. Kafka orders within a partition only — the key is the ordering decision.",
 d_kafka,"One topic, six partitions, two independent groups. Partition count caps parallelism.",
 ["Kafka topology","Partition diagram","Consumer group diagram"])

add(9,"Event sourcing diagram",3,
 "State stored as an append-only sequence of events, with current state derived by replaying them and snapshots as an optimisation.",
 "What is the system of record, and can we reconstruct any past state?",
 "Domains where the audit trail is the product: finance, trading, claims, regulated workflows.",
 "The event store as the source of truth, the replay path, snapshotting, and how projections are rebuilt.",
 "Not planning for schema evolution. Old event shapes live forever and must stay readable.",
 d_eventsourcing,"Append, fold, project. Correcting data means a new event, never an update.",
 ["Event log architecture","Append-only store diagram"])

add(9,"Pub/sub diagram",3,
 "One topic, many independent subscriptions, each with its own filter and failure handling — publisher unaware of all of them.",
 "Who receives this, and what happens to the messages that cannot be processed?",
 "Notification fan-out, integration hubs, and anywhere new consumers are expected to appear.",
 "The filter per subscription, the delivery guarantee, and the dead-letter destination.",
 "A publisher that must change to add a subscriber. That is point-to-point integration wearing a topic.",
 d_pubsub,"Fan-out with per-subscription filters and one DLQ. Adding a fourth consumer costs the publisher nothing.",
 ["Publish/subscribe diagram","Topic fan-out diagram"])


# ================= 9. Integration & API =================
add(10,"Integration architecture diagram",2,
 "How systems are wired together across an estate: point-to-point or mediated, synchronous or asynchronous, and who owns each contract.",
 "How do these systems talk, and how many integrations are we really maintaining?",
 "Enterprise integration design, M&A, and the moment integration work starts dominating delivery.",
 "The count of links, the pattern per link, and the owner of each contract.",
 "Reaching for a hub reflexively. Below roughly six systems, point-to-point with good contracts wins.",
 d_integration,"The same estate wired both ways. The pairwise link count is the argument.",
 ["System integration diagram","API architecture diagram","Interface architecture"])

add(10,"API gateway & BFF diagram",2,
 "The edge of your system: what happens to a request before it reaches a service, and how each client gets an API shaped for it.",
 "How do clients reach the system, and who owns each contract?",
 "Any public or partner-facing API, and any estate with more than one kind of client.",
 "Protocol and version on each edge, plus which team owns each BFF.",
 "A gateway that grew business logic, or one BFF shared by every client — that is just a gateway again.",
 d_bff,"Clients, gateway, per-client BFFs, services. One BFF per client team, not one for all.",
 ["API gateway diagram","BFF architecture","Edge architecture"])

add(10,"Rate limiting & quota architecture",2,
 "Where a request is counted, against which key, what the caller is told when they exceed it, and how the tiers map onto what they pay.",
 "Who is allowed how much, where is that enforced, and what does the caller see when they hit it?",
 "Any public or partner API, any multi-tenant service, and the day one customer’s retry loop takes the platform down.",
 "The dimension counted, the store the counters live in, the tiers as numbers, and response headers a caller can act on.",
 "A per-instance limiter behind a load balancer. Eight instances quietly multiply your published limit by eight.",
 d_ratelimit,"Counted per key in a shared store, with the tiers and the 429 contract written down.",
 ["Throttling architecture","Quota management","API rate limits","Token bucket diagram"])

add(10,"Webhook flow diagram",2,
 "Outbound HTTP callbacks drawn end to end: registration, signing, delivery, retries and replay.",
 "How do partners find out something happened, and what happens when their endpoint is down?",
 "Any partner or public integration where you are the event producer.",
 "The signature and timestamp, a stable event id for deduplication, the retry schedule, and the replay path.",
 "Fire-and-forget with no signature and no retries. That is a notification, not a delivery guarantee.",
 d_webhook,"Register, sign, deliver, retry, replay. Four properties separate this from a POST and a prayer.",
 ["Callback integration","Outbound event delivery"])

add(10,"Service mesh diagram",3,
 "Sidecar proxies and a control plane taking over service-to-service concerns — mTLS, retries, timeouts, traces — without application code changing.",
 "How is east-west traffic secured and controlled?",
 "Large Kubernetes estates where those concerns are being reimplemented per service.",
 "The control plane, the data plane, and which policies are enforced where.",
 "Adopting it for three services. The operational cost lands long before the benefit does.",
 d_mesh,"Control plane above, sidecars beside each service. The proxies carry mTLS between pods.",
 ["Service mesh architecture","Sidecar diagram","Istio / Linkerd architecture"])

add(10,"ESB / middleware architecture",3,
 "A mediating layer that adapts protocols, transforms to a canonical model, routes and orchestrates — the traditional enterprise integration shape.",
 "How do incompatible enterprise systems get connected without touching either of them?",
 "Estates full of packaged software and legacy protocols that cannot be changed.",
 "Which capabilities live in the bus and — crucially — which do not.",
 "Business logic in the bus. It becomes one deployable that every team must queue to change.",
 d_esb,"Adapters and canonical model, yes. Orchestration in the middle is where these estates ossify.",
 ["ESB architecture","Middleware architecture","Hub and spoke integration"])


# ================= 10. Process & workflow =================
add(11,"Swimlane diagram",2,
 "A process laid out with one lane per actor, so every handoff between people and systems is visible as a line crossing.",
 "What are the steps, and who owns each one?",
 "Any process crossing team or system boundaries. Your shared language with business stakeholders.",
 "Decision points, rejection and timeout branches, and which steps are manual versus automated.",
 "Modelling the process as it should be while everyone reads it as how it is. Label it as-is or to-be.",
 d_swimlane,"A returns process. Each lane crossing is a queue and a delay — count them.",
 ["Cross-functional flowchart","Business process diagram","Workflow diagram"])

add(11,"BPMN process model",2,
 "A precise, standardised process notation that a workflow engine can execute. Worth its formality only when the model really is the implementation.",
 "What is the exact, executable definition of this process?",
 "Enterprise processes running on Camunda, Temporal or similar.",
 "Gateways, boundary events — especially timers — and where each path terminates.",
 "Full BPMN for a five-step flow. A swimlane sketch is clearer and takes a tenth of the time.",
 d_bpmn,"Six symbols carry most real models: start, task, gateway, timer boundary, end.",
 ["BPMN 2.0","Executable process model","Orchestration diagram"])

add(11,"Flowchart",3,
 "The oldest notation here and still the right one for a single actor working through sequential steps with branches.",
 "What are the steps and the decisions, in order?",
 "Runbooks, troubleshooting guides, and any procedure one person follows start to finish.",
 "One entry point, an unambiguous condition on every branch, and a terminator on every path.",
 "Using it for two actors or for concurrency. That is a swimlane and an activity diagram respectively.",
 d_flowchart,"A cache-aside read path. Every branch resolves; no path just stops.",
 ["Process flow diagram","Program flowchart","Decision flowchart"])


# ================= 11. DevOps & CI/CD =================
add(12,"CI/CD pipeline diagram",2,
 "The path from a commit to running production software, and the gates along it. Architecture that cannot be deployed safely is not finished architecture.",
 "How does a change reach production, and how does it come back out?",
 "Every project. It is the delivery contract between teams.",
 "One immutable artefact promoted across environments, and what each gate actually checks.",
 "Rebuilding the artefact per environment, so what you tested is not what you shipped.",
 d_pipeline,"Build once, promote the same artefact, and roll back on an SLO signal rather than a human noticing.",
 ["CI/CD diagram","Deployment pipeline","Environment promotion diagram"])

add(12,"Release strategy diagram",2,
 "How new code meets real traffic: rolling, blue/green, canary, or behind a flag — and how quickly you can undo it.",
 "What is the blast radius of this release, and how fast is the rollback?",
 "Whenever downtime or a bad release has a real cost.",
 "The traffic split, the automated promotion or rollback signal, and the database migration plan.",
 "Forgetting that two app versions run against one schema. Expand, backfill, then contract.",
 d_release,"Canary above, blue/green below. Both need backward-compatible migrations.",
 ["Blue/green deployment","Canary deployment","Rollout strategy"])

add(12,"GitOps architecture",3,
 "Desired state in git, pulled and continuously reconciled by an agent inside the cluster — deployment as convergence rather than a push.",
 "What should be running, who changed it, and how is drift corrected?",
 "Kubernetes estates, multi-cluster fleets, and anywhere pipeline credentials for production are a concern.",
 "The config repo as desired state, the reconciler, and what happens when live state drifts.",
 "Keeping a manual kubectl path alongside it. The reconciler will silently revert the change, at the worst moment.",
 d_gitops,"The cluster pulls; git is the desired state; rollback is a revert. Drift is undone automatically.",
 ["Pull-based deployment","Argo CD architecture","Flux architecture"])

add(12,"DevSecOps pipeline",3,
 "Security checks placed along the delivery pipeline, each with a threshold, an owner and an honest exception path.",
 "Where is security actually enforced between commit and production?",
 "Regulated environments, supply-chain hardening, and after any incident traced to a dependency.",
 "Which gates block and which advise, plus the admission control that cannot be bypassed.",
 "Gates with no exception path. Teams route around the pipeline entirely rather than argue with it.",
 d_devsecops,"Six gates, two severities, one unbypassable control at admission.",
 ["Secure SDLC diagram","Supply chain security pipeline","Shift-left diagram"])


# ================= 12. Observability =================
add(13,"Observability architecture",2,
 "How logs, metrics and traces get from services to the humans who need them at three in the morning, and what they cost to keep.",
 "How do we find out something broke, and then why?",
 "Before go-live, not after the first incident.",
 "Retention and sampling rates, cardinality limits, alert routing, and one correlation ID propagated everywhere.",
 "Alerting on causes rather than symptoms. Page on user-visible SLO burn; keep CPU for the dashboard.",
 d_observability,"Instrument once with OpenTelemetry, route anywhere. The collector is the architectural decision.",
 ["Telemetry architecture","Monitoring architecture","OpenTelemetry architecture"])

add(13,"Metrics architecture",2,
 "Numeric time series from collection to long-term storage, and the label discipline that keeps it affordable.",
 "Is it broken, how badly, and what is the trend?",
 "Every service. Metrics are the cheapest signal per answer and the basis for every SLO.",
 "Scrape or push, resolution, retention, and the label sets — bounded and low-arity.",
 "Labelling a metric with a user id or raw URL path. That is a log with a billing surprise attached.",
 d_metrics,"RED for services, USE for resources — and cardinality as the cost function.",
 ["Monitoring architecture","Prometheus architecture","Time series architecture"])

add(13,"Alerting & on-call routing",2,
 "How a breached objective becomes a page for a specific human — burn rate, grouping, routing and escalation.",
 "Who gets woken up, for what, and how quickly?",
 "Before go-live. Retrofitting alerting after the first incident is how alert fatigue starts.",
 "The SLO and error budget, the burn rate thresholds, ownership-based routing, and the escalation timer.",
 "Paging on causes. Nobody has ever filed a complaint about CPU — page on what the user feels.",
 d_alerting,"Fast burn pages a human; slow burn opens a ticket. Everything else is a dashboard.",
 ["Alerting architecture","On-call escalation diagram","Incident routing"])

add(13,"Distributed tracing diagram",2,
 "One request as a tree of timed spans across every service it touched, joined by a single propagated id.",
 "Which hop is slow, and what did this request actually do?",
 "Any estate above a handful of services, and every latency investigation that crosses a boundary.",
 "Context propagation across every hop including brokers, and the sampling strategy — head or tail.",
 "Breaking propagation at the async boundary. The trace then stops exactly where the mystery starts.",
 d_tracing,"A span waterfall drawn to scale at 1 px per millisecond. Over a third of the request sits inside one third-party call — visible in seconds.",
 ["Tracing architecture","Span waterfall","Request trace diagram"])

add(13,"Logging architecture",3,
 "Structured events from services to an index, with redaction, sampling and tiered retention along the way.",
 "What exactly happened, in detail, and what does keeping that cost?",
 "Compliance and audit requirements, and debugging that metrics and traces cannot finish.",
 "The required fields on every line — trace id and tenant especially — plus redaction and retention tiers.",
 "Indexing everything at full fidelity forever. Logs are the easiest telemetry to over-collect and the priciest.",
 d_logging,"Redact and sample before you pay to index, and tier what survives.",
 ["Log pipeline","Log aggregation architecture","ELK architecture"])


# ================= 13. Reliability & resilience =================
add(14,"Failover / DR diagram",2,
 "What runs where in normal operation, what takes over when a region is lost, and the two numbers that follow from the picture.",
 "How much data do we lose, and how long are we down?",
 "Any RTO or RPO commitment, and any SLA you are asked to sign.",
 "Replication mode and lag, the failover trigger, and every step between detection and serving traffic.",
 "A DR plan that has never been executed. Untested failover is a hope, not a plan.",
 d_failover,"Warm standby. RPO is the replication lag; RTO is everything between detection and serving.",
 ["Disaster recovery diagram","DR architecture","Active/passive architecture"])

add(14,"Backup & restore architecture",2,
 "What is copied, how often, where it is kept, how far back you can go — and, the part that matters, evidence that the restore has actually been run.",
 "Someone dropped a table at 14:05. How much do we lose, and how long until we are back?",
 "Every system with state. Especially every one where the answer today is “we have snapshots”.",
 "The RPO the copy interval really gives you, the measured RTO of a real restore, immutability against ransomware, and the date of the last test.",
 "Confusing replication with backup. A replica faithfully reproduces the DELETE within a second, which is precisely the problem.",
 d_backup,"Base backup plus WAL gives point-in-time restore. The tested-monthly box is the only one an auditor believes.",
 ["Backup architecture","Point-in-time recovery","PITR diagram","Restore strategy"])

add(14,"Circuit breaker diagram",2,
 "A three-state machine that stops a slow or failing dependency from consuming your threads and taking you down with it.",
 "What happens to us when a dependency degrades?",
 "Every synchronous call that crosses a network boundary.",
 "The trip threshold, the cooldown, and — most importantly — what you serve while the breaker is open.",
 "Retries with no backoff and no jitter. That is a synchronised retry storm aimed at your own dependency.",
 d_breaker,"Closed, open, half-open. The degraded response is a product decision, not a library setting.",
 ["Circuit breaker flow","Resilience pattern diagram"])

add(14,"Retry & backoff flow",2,
 "How many times, how far apart, and under what total budget a failed call is repeated — plus what makes repeating it safe.",
 "When do we retry, and how do we avoid making the outage worse?",
 "Every network call. It is the default failure behaviour whether or not anyone designed it.",
 "Which status codes are retryable, the backoff schedule with jitter, a cluster-wide budget, and the idempotency key.",
 "Retrying a 400 forever, or retrying a payment without an idempotency key and charging twice.",
 d_retry,"Backoff, jitter, a cap and a budget — and an idempotency key underneath all of it.",
 ["Retry flow","Exponential backoff diagram"])

add(14,"Bulkhead architecture",2,
 "Resources partitioned so that one saturated dependency, tenant or workload cannot consume the capacity the others need.",
 "When one thing gets slow, what else goes down with it?",
 "Any service with mixed workloads — fast reads beside slow reports, or shared tenants of different sizes.",
 "The partitions, the size of each pool, and the fail-fast behaviour when a pool is exhausted.",
 "Partitioning without resizing. If the pools still sum to the old shared pool, nothing has been isolated.",
 d_bulkhead,"Separate pools, bounded blast radius. Reports degrade; search keeps serving.",
 ["Pool isolation","Compartmentalisation diagram"])

add(14,"Active/active architecture",2,
 "Both sites live and serving, which removes the failover step and introduces the hardest problem in distributed data.",
 "Can we serve from two places at once, and what happens when both write the same row?",
 "Global low-latency requirements, and availability targets a failover procedure cannot meet.",
 "Ownership of each data partition, or an explicit conflict-resolution rule if there is none.",
 "Last-write-wins by default. That is silent data loss with a respectable-sounding name.",
 d_activeactive,"Both regions live, each row with one home. The conflict rule belongs on the diagram.",
 ["Multi-master architecture","Active-active deployment"])

add(14,"Failure mode diagram (FMEA)",3,
 "Each way the system can fail, its immediate effect, what that effect becomes if unhandled, and how it is detected.",
 "What can break, and what does each break turn into?",
 "Design review of anything critical, and as the structured follow-up after an incident.",
 "The second-order consequence, not just the immediate one — plus detection before mitigation.",
 "Listing failures and stopping at the immediate effect. Incidents are made of the consequence nobody traced.",
 d_fmea,"Five failure modes and what each becomes. The third column is where the meeting earns its cost.",
 ["FMEA","Failure mode and effects analysis","Failure catalogue"])

add(14,"Fault tree analysis",3,
 "The failure you fear at the top, decomposed downward through AND and OR gates to the individual causes.",
 "What combinations of failures produce this outcome?",
 "Safety-critical systems, availability targets that are being missed, and post-incident structural analysis.",
 "Correct gate types, and — where you have them — probabilities on the leaves.",
 "Everything an OR gate. If nothing is an AND, you have documented a system with no redundancy at all.",
 d_faulttree,"OR gates are single points of failure; AND gates are redundancy that works. Read downward.",
 ["FTA","Fault tree","Root cause tree"])

add(14,"Reliability block diagram",3,
 "Components in series and parallel, with availability figures — so the target can be checked with arithmetic rather than asserted.",
 "Does this design actually reach the availability number we promised?",
 "SLA negotiation, and any time someone claims four nines for a chain of three-nines dependencies.",
 "Availability per block, series versus parallel arrangement, and the independence assumption stated out loud.",
 "Assuming independence. Two instances sharing one config store or one certificate are one block, not two.",
 d_rbd,"Series multiplies availability down; parallel multiplies unavailability down. Independence is the catch.",
 ["RBD","Availability model","Redundancy calculation"])


# ================= 14. Decision =================
add(15,"Architecture decision record",1,
 "One page per consequential decision: the context, what was decided, what was rejected, and what it now costs you. Immutable — superseded, never edited.",
 "Why is the architecture this way, and what would make us change our minds?",
 "Every decision that would be expensive to reverse. Written when it is made, not reconstructed later.",
 "The alternatives with the reason each was rejected, and consequences that include the downsides.",
 "A consequences section listing only benefits. If there is no downside, no trade-off was made.",
 d_adr,"Two endings, not a queue — superseded and deprecated both hang off Accepted. Four sections below. Supersede rather than edit.",
 ["ADR","Decision log","Design decision record"])

add(15,"Trade-off / decision matrix",2,
 "Options scored against criteria that were weighted before anyone looked at the scores.",
 "Which option wins once we are explicit about what we value?",
 "Vendor selection, platform choices, and any decision where two camps have already formed.",
 "Weights fixed before scoring, and reversibility as an explicit criterion.",
 "Weighting after scoring. The matrix then documents a decision already made rather than informing one.",
 d_matrix,"Weights above the columns, scores inside, weighted total on the right. Fix the weights first or you will score toward the answer you already wanted.",
 ["Decision matrix","Option comparison diagram","Weighted scoring model"])

add(15,"Decision tree",3,
 "Branching guidance that encodes a standard so teams can apply it themselves, instead of asking you in every design review.",
 "Which option applies, given these conditions?",
 "Recurring choices you have already made several times the same way.",
 "Conditions phrased as questions with unambiguous answers, and a named outcome at every leaf.",
 "Branches that overlap, so two paths give different answers to the same situation.",
 d_tree,"Sync or async, and which broker. Publish it once and stop re-answering it.",
 ["Selection guide","Choice tree"])


# ================= 15. Specialised =================
add(16,"Service dependency diagram",2,
 "The call graph of an estate, generated from real traffic — read for two things only: cycles, and the node everything depends on.",
 "What breaks when this service does, and what is our real availability ceiling?",
 "Microservice estates past about ten services, and every incident review that crosses a boundary.",
 "Direction on every edge, criticality tier per node, and inbound edge counts.",
 "Drawing it by hand. The hand-drawn version omits the dependency that causes the outage.",
 d_servicedep,"One cycle and one tier-0 node with six inbound edges. Both are findings.",
 ["Service interaction diagram","Microservices landscape","Call graph"])

add(16,"Serverless architecture",3,
 "Functions, managed services and the events that connect them — a container diagram where the containers are invocations.",
 "What triggers what, and what happens to the messages that fail?",
 "Event-driven and spiky workloads on managed platforms.",
 "The trigger on every arrow, concurrency limits, retry counts, and the dead-letter queue.",
 "Hiding the triggers. Without them the diagram cannot explain either the cost or the failure behaviour.",
 d_serverless,"Triggers labelled, retries bounded, DLQ alarmed — the three things this diagram exists to show.",
 ["Function dependency diagram","Event trigger diagram","FaaS architecture"])

add(16,"RAG architecture",3,
 "Retrieval-augmented generation drawn as what it actually is: a data flow diagram with an ingestion path, a query path, and an access-control decision in the middle.",
 "How does retrieval ground the model's answer, and who is allowed to see what?",
 "Any assistant answering from a document corpus with more than one class of reader.",
 "Chunking and refresh strategy, the retrieval filter that enforces permissions, and what happens on no relevant hit.",
 "Applying access control in the prompt. Filter at retrieval, per user, or the model will happily quote a document they cannot open.",
 d_rag,"Ingestion above, query below. The permission filter belongs at the vector store, not the prompt.",
 ["Retrieval-augmented generation","Vector database architecture","Grounded search architecture"])

add(16,"LLM application & agent architecture",3,
 "A model behind an orchestrator, with tools, retrieval and memory around it, and guardrails on both sides of the loop.",
 "What can this agent actually do, how many times, and at what cost per request?",
 "Anything giving a model tools with side effects, or letting it loop without a human in between.",
 "The loop bound, the tool allow-list, the cost ceiling, and where output is validated before it is acted on.",
 "Trusting model output downstream. Treat it as untrusted input — because that is exactly what it is.",
 d_llmapp,"Orchestrator, model, tools, guardrails — and the loop between them, drawn with the turn, time and cost ceilings that bound it.",
 ["AI agent architecture","LLM application architecture","AI/LLM architecture"])

add(16,"ML pipeline & MLOps architecture",3,
 "Training and serving as one loop: data to features to model to registry to production, with drift monitoring closing it.",
 "How does a model get built, shipped, and known to still be good?",
 "Any model in production. Especially the second one — the first can survive on manual process.",
 "Both feature paths, model versioning and promotion, and the drift signals that trigger retraining.",
 "Two implementations of the same feature, one for training and one for serving. They will diverge silently.",
 d_mlops,"One feature store used by both paths, and monitoring as the trigger that closes the loop.",
 ["ML architecture","ML pipeline","MLOps architecture"])

add(16,"IoT architecture",3,
 "Devices, an edge tier that keeps working when the link drops, cloud ingestion, and a twin holding intent for things that are offline.",
 "How do a hundred thousand intermittently connected devices stay useful and updatable?",
 "Connected products, industrial telemetry, and anything with firmware in the field.",
 "The offline behaviour, per-device identity and credential rotation, and the firmware update path.",
 "No OTA update path. A device you cannot patch is a liability you own for a decade.",
 d_iot,"Field, edge, cloud — with buffering, twins and OTA, which are the parts that make it work.",
 ["Device-to-cloud architecture","Connected product architecture"])

add(16,"Edge computing architecture",3,
 "Compute placed at tiers by latency and locality: device, point of presence, region, core — with the split written down.",
 "What gets decided close to the user, and what has to travel?",
 "Latency-sensitive products, bandwidth-expensive telemetry, and data-residency constraints.",
 "Round-trip latency per tier, and the rule for what may be decided with local knowledge only.",
 "Pushing stateful logic outward for its own sake. Consistency gets much harder at every tier you move out.",
 d_edge,"Four tiers with real latencies. The dividing line is the design.",
 ["Fog computing","CDN compute architecture","Edge tier diagram"])


# ================= 16. Quality & cross-cutting =================
add(17,"Quality attribute scenario model",2,
 "The requirements side of architecture, written so they can be tested: each quality attribute broken down into scenarios with a source, a stimulus, an environment, a response and — the part that matters — a number.",
 "What does “fast enough” actually mean here, and how would we know we missed it?",
 "Before the first structural diagram. Again whenever someone says “it needs to be scalable” in a funding conversation.",
 "A measurable response on every leaf, and two rankings per scenario: business importance and technical risk.",
 "Adjectives. “Fast”, “secure” and “scalable” cannot be tested, cannot be budgeted, and cannot be traded off against each other.",
 d_qascenario,"Four attributes, one scenario written out in full. Only the (H, H) leaves should shape the architecture.",
 ["Utility tree","ATAM utility tree","Non-functional requirements model","NFR model","Quality scenarios"])

add(17,"Multi-tenancy isolation model",2,
 "How far apart two customers' data and compute are kept: a separate stack each, a shared application over separate databases, or one of everything with a tenant column. The decision that quietly sets your schema, your backups, your blast radius and your price list.",
 "How isolated is one tenant from another, and what does that cost per tenant?",
 "The first SaaS design, the first enterprise customer who reads your security questionnaire, and every pricing-tier conversation after that.",
 "Which model applies to which tier, where the tenant boundary is enforced, and what a bug in that enforcement exposes.",
 "Discovering which model you have by reading a WHERE clause. Isolation enforced by developer discipline is isolation you do not have.",
 d_tenancy,"Silo, bridge, pool — and the four consequences that follow from picking one.",
 ["Tenancy model","Silo / bridge / pool","SaaS isolation model","Tenant isolation diagram"])

add(17,"Caching architecture",2,
 "Every layer that holds a copy of an answer, what each one promises about freshness, and what happens to the tier behind them when the copies all disappear at once.",
 "Where are the copies, how stale may they be, and what happens when the cache is cold?",
 "Any read-heavy path, and immediately after the first incident caused by stale data or a cache restart.",
 "TTL and invalidation trigger per layer, the hit rate, and the origin's capacity for the miss storm rather than the average.",
 "Sizing the origin for the steady-state miss rate. The same 6 % arriving in one second when Redis restarts is an outage.",
 d_caching,"Four layers, one read path, and the stampede that is the actual failure mode.",
 ["Cache architecture","Cache-aside diagram","CDN and cache layers","Caching strategy diagram"])

add(17,"Cost & FinOps attribution view",3,
 "The architecture with money on it: what each part costs per month, which team owns that line, how shared cost is allocated, and the unit cost that turns all of it into a number the business recognises.",
 "What does this cost, who owns that, and what is our cost per unit of work?",
 "Any cloud estate past a handful of services, every cost-reduction programme, and every pricing conversation.",
 "The tagging scheme, direct versus shared cost with the allocation rule stated, and a unit cost — cost per order, per tenant, per request.",
 "Reporting total spend. Total spend rising while cost per order falls is a healthy growing business; the total alone cannot tell you which you are.",
 d_finops,"Tags, lines, allocation and the unit cost. The allocation rule is an incentive, so choose it deliberately.",
 ["FinOps diagram","Cloud cost model","Cost allocation diagram","Unit economics view"])


# ================= 17. Evolution & migration =================
add(18,"Migration & transition-state architecture",2,
 "Three architectures on one page — where you are, where you are going, and the shape you will actually run for the next year while you get there. The middle one is the one nobody designs.",
 "How do we get from this to that without a big-bang cutover?",
 "Every modernisation, every re-platforming, every acquisition integration. Which is most architecture work.",
 "The transition state drawn as carefully as the target, a facade or seam that makes each move incremental, and a date the middle column ends.",
 "Drawing only as-is and to-be. The gap between them is where the programme lives, and leaving it undrawn is how it becomes permanent.",
 d_migration,"As-is, transition, to-be. The routing facade is what turns a rewrite into a sequence of reversible steps.",
 ["Strangler fig pattern","Transition architecture","Target state architecture","As-is / to-be diagram","Modernisation roadmap"])

add(18,"API versioning & deprecation lifecycle",2,
 "The stages a published interface moves through and what each one promises a caller — including the only stage most teams skip, which is the one where it is switched off.",
 "How does a caller find out this endpoint is going away, and when can we actually delete it?",
 "The moment an API has a consumer you do not control. Partner APIs, public APIs, and internal ones across team boundaries.",
 "The lifecycle stages with the notice period, the machine-readable deprecation signal, and per-caller usage telemetry.",
 "Publishing a version with no retirement path. You will then support it forever, because you have no way to prove nobody is using it.",
 d_apiversion,"Four stages, two versions in flight, and the three headers that make a deprecation a contract rather than an email.",
 ["API lifecycle","Deprecation policy diagram","Versioning strategy","Sunset policy"])

add(18,"Schema evolution & compatibility",3,
 "Which changes to a message or table shape are safe, which order producers and consumers may be upgraded in, and why the answer is a setting in your schema registry rather than a matter of opinion.",
 "Can I change this field without breaking anyone, and who has to deploy first?",
 "Before the first event is published. Retrofitting a compatibility mode onto a live topic is a migration of its own.",
 "The compatibility mode in force, what it permits, and the deployment order that follows from it.",
 "Treating a type change as a widening. int to decimal is a different type, and the consumer that has been parsing it for two years will not agree with you.",
 d_schemaevo,"Four modes and the deployment order each one buys. The safe change and the unsafe change look almost identical.",
 ["Schema compatibility","Avro compatibility modes","Contract evolution","Event versioning"])

# ---------------------------------------------------------------------------
# See also. An alias tells you what a diagram is called; this tells you which
# diagram to open next, which is the thing a dictionary otherwise cannot say.
# Links are one-directional on purpose — "read the ERD next" and "read the domain
# model next" are different pieces of advice — but most pairs earn both.
RELATED = {
 "System context diagram (C4 level 1)": ["Container diagram (C4 level 2)","Solution architecture diagram","Use case diagram"],
 "Container diagram (C4 level 2)": ["System context diagram (C4 level 1)","Component diagram (C4 level 3)","Deployment diagram","Sequence diagram"],
 "Component diagram (C4 level 3)": ["Hexagonal architecture (ports & adapters)","Package diagram","Code diagram (C4 level 4)","Component diagram (UML)"],
 "Hexagonal architecture (ports & adapters)": ["Component diagram (C4 level 3)","Package diagram","Domain model","Code diagram (C4 level 4)"],
 "Cloud architecture diagram": ["Deployment diagram","Network / VPC diagram","Physical architecture diagram","Cost & FinOps attribution view"],
 "Solution architecture diagram": ["System landscape diagram","Business capability map","Logical architecture diagram"],
 "Logical architecture diagram": ["Physical architecture diagram","Solution architecture diagram","Reference architecture"],
 "System landscape diagram": ["Business capability map","Migration & transition-state architecture","Service dependency diagram"],
 "Physical architecture diagram": ["Logical architecture diagram","Deployment diagram","Concurrency & process view"],
 "Reference architecture": ["Architecture decision record","Team topologies map","GitOps architecture"],
 "Code diagram (C4 level 4)": ["Class diagram","Component diagram (C4 level 3)","Hexagonal architecture (ports & adapters)"],

 "State machine diagram": ["Timing diagram","Activity diagram","Circuit breaker diagram"],
 "Class diagram": ["Domain model","Entity relationship diagram","Object diagram"],
 "Activity diagram": ["Swimlane diagram","BPMN process model","Flowchart"],
 "Use case diagram": ["System context diagram (C4 level 1)","Quality attribute scenario model"],
 "Component diagram (UML)": ["Composite structure diagram","Component diagram (C4 level 3)","Hexagonal architecture (ports & adapters)"],
 "Package diagram": ["Hexagonal architecture (ports & adapters)","Component diagram (C4 level 3)"],
 "Object diagram": ["Class diagram","Domain model"],
 "Communication diagram": ["Sequence diagram","Service dependency diagram"],
 "Timing diagram": ["State machine diagram","Circuit breaker diagram","Request flow diagram"],
 "Composite structure diagram": ["Component diagram (UML)","Hexagonal architecture (ports & adapters)"],
 "Interaction overview diagram": ["Sequence diagram","Activity diagram"],
 "Profile diagram": ["Reference architecture"],

 "Sequence diagram": ["Request flow diagram","Communication diagram","Saga diagram","Distributed tracing diagram"],
 "Request flow diagram": ["Distributed tracing diagram","Sequence diagram","Caching architecture","Concurrency & process view"],
 "Message flow diagram": ["Event topology diagram","Schema evolution & compatibility","Integration architecture diagram"],
 "Data flow diagram": ["Threat model (STRIDE)","Trust boundary diagram","Data classification diagram"],
 "Concurrency & process view": ["Physical architecture diagram","Bulkhead architecture","High availability architecture"],

 "Entity relationship diagram": ["Conceptual, logical & physical data models","Domain model","Data partitioning & sharding strategy"],
 "Conceptual, logical & physical data models": ["Entity relationship diagram","Data warehouse architecture"],
 "Data pipeline / ETL–ELT architecture": ["Data lineage diagram","Data warehouse architecture","Streaming data architecture"],
 "Data lineage diagram": ["Data pipeline / ETL–ELT architecture","Data warehouse architecture","Data mesh architecture"],
 "Data warehouse architecture": ["Data lake / lakehouse architecture","Data lineage diagram","Conceptual, logical & physical data models"],
 "Data lake / lakehouse architecture": ["Data warehouse architecture","Data mesh architecture"],
 "Data mesh architecture": ["Bounded context map","Team topologies map","Data lineage diagram"],
 "Streaming data architecture": ["Kafka topic architecture","Data pipeline / ETL–ELT architecture","Schema evolution & compatibility"],
 "Data partitioning & sharding strategy": ["Multi-tenancy isolation model","Entity relationship diagram","Multi-region architecture"],

 "Deployment diagram": ["Cloud architecture diagram","High availability architecture","Network / VPC diagram"],
 "Network / VPC diagram": ["Trust boundary diagram","Cloud architecture diagram","Zero trust architecture"],
 "Kubernetes architecture diagram": ["GitOps architecture","Service mesh diagram","Container architecture diagram"],
 "Container architecture diagram": ["DevSecOps pipeline","Kubernetes architecture diagram","CI/CD pipeline diagram"],
 "High availability architecture": ["Failover / DR diagram","Reliability block diagram","Multi-region architecture"],
 "Multi-region architecture": ["Active/active architecture","Failover / DR diagram","Data partitioning & sharding strategy"],

 "OAuth 2.0 / OIDC flow": ["Identity architecture","Authorisation model diagram","Zero trust architecture"],
 "Identity architecture": ["OAuth 2.0 / OIDC flow","Authorisation model diagram","Zero trust architecture"],
 "Authorisation model diagram": ["Multi-tenancy isolation model","Identity architecture","OAuth 2.0 / OIDC flow"],
 "Trust boundary diagram": ["Threat model (STRIDE)","Data flow diagram","Zero trust architecture"],
 "Threat model (STRIDE)": ["Data flow diagram","Trust boundary diagram","Failure mode diagram (FMEA)"],
 "Zero trust architecture": ["Identity architecture","Trust boundary diagram","Service mesh diagram"],
 "Data classification diagram": ["Encryption & key management diagram","Data lineage diagram","Multi-tenancy isolation model"],
 "Encryption & key management diagram": ["Data classification diagram","Multi-tenancy isolation model","Backup & restore architecture"],

 "Domain model": ["Bounded context map","Entity relationship diagram","Event storming board","Hexagonal architecture (ports & adapters)"],
 "Bounded context map": ["Team topologies map","Domain model","Event storming board","Integration architecture diagram"],
 "Team topologies map": ["Bounded context map","Wardley map","Service dependency diagram"],
 "Event storming board": ["Domain model","Bounded context map","Event topology diagram"],
 "Business capability map": ["Wardley map","System landscape diagram","Value stream map"],
 "Value stream map": ["Swimlane diagram","Business capability map"],
 "Wardley map": ["Business capability map","Team topologies map","Trade-off / decision matrix"],

 "Event topology diagram": ["Schema evolution & compatibility","Kafka topic architecture","Pub/sub diagram","Message flow diagram"],
 "Saga diagram": ["Outbox pattern diagram","Sequence diagram","Retry & backoff flow"],
 "CQRS diagram": ["Event sourcing diagram","Outbox pattern diagram","Caching architecture"],
 "Outbox pattern diagram": ["Saga diagram","CQRS diagram","Event topology diagram"],
 "Kafka topic architecture": ["Event topology diagram","Streaming data architecture","Data partitioning & sharding strategy"],
 "Event sourcing diagram": ["CQRS diagram","Schema evolution & compatibility","Data lineage diagram"],
 "Pub/sub diagram": ["Event topology diagram","Webhook flow diagram","Kafka topic architecture"],

 "Integration architecture diagram": ["ESB / middleware architecture","API gateway & BFF diagram","Bounded context map"],
 "API gateway & BFF diagram": ["Rate limiting & quota architecture","OAuth 2.0 / OIDC flow","API versioning & deprecation lifecycle"],
 "Rate limiting & quota architecture": ["API gateway & BFF diagram","Bulkhead architecture","Multi-tenancy isolation model"],
 "Webhook flow diagram": ["Pub/sub diagram","Retry & backoff flow","API versioning & deprecation lifecycle"],
 "Service mesh diagram": ["Kubernetes architecture diagram","Zero trust architecture","Circuit breaker diagram"],
 "ESB / middleware architecture": ["Integration architecture diagram","Event topology diagram"],

 "Swimlane diagram": ["BPMN process model","Value stream map","Activity diagram"],
 "BPMN process model": ["Swimlane diagram","Saga diagram","Activity diagram"],
 "Flowchart": ["Activity diagram","Decision tree","Swimlane diagram"],

 "CI/CD pipeline diagram": ["Release strategy diagram","DevSecOps pipeline","GitOps architecture"],
 "Release strategy diagram": ["CI/CD pipeline diagram","Alerting & on-call routing","Migration & transition-state architecture"],
 "GitOps architecture": ["Kubernetes architecture diagram","CI/CD pipeline diagram"],
 "DevSecOps pipeline": ["CI/CD pipeline diagram","Container architecture diagram","Threat model (STRIDE)"],

 "Observability architecture": ["Metrics architecture","Distributed tracing diagram","Logging architecture","Alerting & on-call routing"],
 "Metrics architecture": ["Observability architecture","Alerting & on-call routing","Cost & FinOps attribution view"],
 "Distributed tracing diagram": ["Request flow diagram","Observability architecture","Sequence diagram"],
 "Logging architecture": ["Observability architecture","Data classification diagram"],
 "Alerting & on-call routing": ["Metrics architecture","Quality attribute scenario model","Observability architecture"],

 "Failover / DR diagram": ["Backup & restore architecture","Active/active architecture","High availability architecture"],
 "Backup & restore architecture": ["Failover / DR diagram","Data classification diagram","Encryption & key management diagram"],
 "Circuit breaker diagram": ["Retry & backoff flow","Bulkhead architecture","Timing diagram"],
 "Retry & backoff flow": ["Circuit breaker diagram","Saga diagram","Rate limiting & quota architecture"],
 "Bulkhead architecture": ["Circuit breaker diagram","Concurrency & process view","Rate limiting & quota architecture"],
 "Active/active architecture": ["Multi-region architecture","Failover / DR diagram","Data partitioning & sharding strategy"],
 "Failure mode diagram (FMEA)": ["Fault tree analysis","Threat model (STRIDE)","Reliability block diagram"],
 "Fault tree analysis": ["Failure mode diagram (FMEA)","Reliability block diagram"],
 "Reliability block diagram": ["High availability architecture","Fault tree analysis","Quality attribute scenario model"],

 "Architecture decision record": ["Trade-off / decision matrix","Decision tree","Reference architecture"],
 "Trade-off / decision matrix": ["Architecture decision record","Quality attribute scenario model","Wardley map"],
 "Decision tree": ["Architecture decision record","Reference architecture","Flowchart"],

 "Service dependency diagram": ["Distributed tracing diagram","Reliability block diagram","Bounded context map"],
 "Serverless architecture": ["Cloud architecture diagram","Pub/sub diagram","Cost & FinOps attribution view"],
 "RAG architecture": ["LLM application & agent architecture","Data classification diagram","Authorisation model diagram"],
 "LLM application & agent architecture": ["RAG architecture","Rate limiting & quota architecture","Cost & FinOps attribution view"],
 "ML pipeline & MLOps architecture": ["Data pipeline / ETL–ELT architecture","Streaming data architecture","Observability architecture"],
 "IoT architecture": ["Edge computing architecture","Streaming data architecture","Identity architecture"],
 "Edge computing architecture": ["IoT architecture","Multi-region architecture","Caching architecture"],

 "Quality attribute scenario model": ["Trade-off / decision matrix","Reliability block diagram","Alerting & on-call routing"],
 "Multi-tenancy isolation model": ["Authorisation model diagram","Data partitioning & sharding strategy","Encryption & key management diagram"],
 "Caching architecture": ["Request flow diagram","CQRS diagram","Edge computing architecture"],
 "Cost & FinOps attribution view": ["Physical architecture diagram","Metrics architecture","Wardley map"],

 "Migration & transition-state architecture": ["System landscape diagram","Bounded context map","Release strategy diagram","API versioning & deprecation lifecycle"],
 "API versioning & deprecation lifecycle": ["Schema evolution & compatibility","API gateway & BFF diagram","Webhook flow diagram"],
 "Schema evolution & compatibility": ["API versioning & deprecation lifecycle","Event topology diagram","Event sourcing diagram"],
}

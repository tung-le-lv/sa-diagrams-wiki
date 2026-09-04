# Software Architect Diagram Dictionary

A reference for one job: working out which diagram to draw, drawing it well enough to be
useful, and knowing when to stop.

**110 diagram types across 18 categories.** Each one carries a worked sample plate and
answers five questions about itself:

| | |
|---|---|
| **What it is** | in a sentence, without the notation lecture |
| **The question it answers** | the only real reason to reach for it |
| **When to reach for it** | and, just as often, when not to |
| **It must show** | the things that make it usable rather than decorative |
| **The common failure** | the version that turns up in review and wastes the meeting |

## Who it is for

Software architects — people expected to produce these diagrams, defend them in a design
review, and read someone else's at speed during an incident.

That audience is a real constraint, not a label. A business analyst, a UX designer and an
SRE would each rank the same 110 types completely differently, and each would be right
about their own job. This one is ranked from an architect's chair, and says so.

## The premise

**Choose the diagram by the question you are trying to settle, not by its name.** Then
draw only what that question needs, and stop.

Most bad architecture diagrams are not badly drawn. They are the wrong diagram, drawn
carefully — a container diagram asked to answer an availability question, a flowchart
standing in for a process with two actors, a picture of nouns where somebody needed a
protocol and a timeout. Picking correctly is most of the work, so the dictionary is
organised around that choice rather than around notation families.

## Four ways in

| | |
|---|---|
| **By how often you will draw it** | the front page, grouped from *the everyday five* down to *worth recognising* |
| **By the question** | 20 common questions, plus all 110 types listed by what each one answers |
| **By audience** | 7 audiences — who a diagram is drawn *for* is often what decides between two similar ones |
| **By category** | 18 of them, from C4 and UML through to evolution and migration |

Plus search across every field, including the prose — "idempotency", "grain",
"crypto-shredding" and "shard key" all find their entries.

## The practical bar

C4 plus the sequence, deployment, ERD and state machine diagrams cover roughly nine
architecture conversations out of ten. Everything else here you should be able to
recognise and read; you will draw it occasionally at best — which is exactly what a
dictionary is for.

Presenting all 110 as equals would not be honest about that, so the front page does not.

## What it is deliberately not

- **Not a tutorial.** It assumes you can already draw a box and an arrow. It is about
  which boxes, and what has to be written on the arrow.
- **Not a notation reference.** Where a standard matters — UML 2.5's fourteen, C4's four
  levels and its supplementary set — the canonical set is mapped. Elsewhere the plates
  use one house style, chosen for legibility over conformance.
- **Not a tool.** No editor, no export, no round-tripping. Draw these wherever you
  already draw things.
- **Not the UX half.** Wireframes and visual design are somebody else's craft. The one
  place the two meet — which service owns each field on each screen — is in here, because
  that is where API shape actually gets decided.

## Reading the plates

Every sample is a plausible design rather than an abstract shape, because the mistakes
worth warning about only appear once a diagram has content. They show the notation, not a
real system: no plate describes anything anyone is running.

Fill carries meaning throughout — the system's own components, data at rest, anything
asynchronous, external managed services, failure paths, out of scope. Numbers on a plate
are internally consistent and are usually the whole point of it: the utilisation figure
that decides whether losing an availability zone is survivable, the partition count that
caps consumer parallelism, the fifteen minutes of real work sitting inside 6.4 days of
elapsed time.

---

Static HTML, no backend, no build step at serve time. See [BUILD.md](BUILD.md) for how the
generator works and how to add a diagram type.

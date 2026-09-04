# SA Diagrams Wiki

A single-page diagram dictionary for software architects: **95 diagram types across 15
categories**, each with a sample plate, the question it answers, when to reach for it,
what it must show, and the mistake that shows up in review.

Every named diagram type in `docs/` is covered — either as its own entry or as a listed
alias on the entry that subsumes it, so alternative vocabulary stays searchable.

The page also carries a **learning path**: 34 of the types arranged into three levels
that build on one another — Foundation (describe any system), Core practice (design and
operate a distributed one), Specialist (depth where the domain requires it) — plus a
question → diagram lookup table. It is a nav filter of its own, alongside the levels and
the 15 categories.

## Site structure

The build emits **27 static pages** — one per category and per level, so no page carries
the whole dictionary:

| Page | Contains |
|---|---|
| `index.html` | Overview: level cards, the question → diagram table, and the category index |
| `pages/learning-path.html` | The three levels sequenced, plus the 34 path entries in order |
| `pages/level-<slug>.html` | Every entry at one level (3 pages) |
| `pages/audience-<key>.html` | Every entry drawn primarily for one audience, plus the ones they also read (7 pages) |
| `pages/<category-slug>.html` | Every entry in one category (15 pages) — an entry's canonical home |

`index.html` stays at the repo root because GitHub Pages needs it there; every other page
lives in `pages/`. Links are generated through `P(target, root)`, which knows whether the
page being written sits at the root or inside `pages/` — never hard-code a page link.

Each entry appears on three axes: its category page (the canonical URL and anchor), its
level page, and its audience page. Search is global — every page embeds a small index of
all 94 types and links results to their canonical page and anchor, so searching from any
page finds everything.

## Ordering within a category

Entries appear in declaration order, and that order is meaningful: **each category runs
most-used first**. It also sets the `NN.n` plate numbers and the order entries appear on
a category page, so there is one source of truth — move the `add(...)` call to change the
order.

Order mostly tracks level (foundation before core practice before specialist) but does
not have to. UML deliberately puts the class diagram (specialist) second, ahead of the
activity diagram (core practice), because it is far more often reached for in practice.

`python build.py` prints each category's level sequence at the end of the run, so an
out-of-place entry is easy to spot:

```
   02 UML                            13233333333
```

## A diagram can be in more than one category

An entry has one **canonical home** — its `cat`, which sets its `NN.n` plate number and
its URL — and may also be *shown* on other category pages. `ALSO_IN` in `entries.py` maps
an entry name to `[(category, position)]`, where position is its slot in that category's
ordering:

```python
ALSO_IN = {
 "Sequence diagram":  [(2, 1), (9, 3)],   # first in UML, third in Integration & API
 "Deployment diagram":[(2, 4)],
}
```

There is nothing to gain from being strict here: entries already render on three axes
(category, level, audience), so a fourth appearance costs only page weight. Several
diagrams genuinely belong in two places, and the source notes cross-list them too.

A borrowed entry keeps its canonical plate number and links back to where it is filed, and
is marked *also shown here*, so the reader can tell which page owns it. Nav counts show
what a page actually contains, so they sum to more than the entry count.

`UML_14` lists UML 2.5's fourteen types in their two groups of seven; the UML page renders
that panel and, thanks to `ALSO_IN`, all fourteen entries are on the page.

Note that a UML component diagram and a C4 component diagram are different things that
share a word: the UML one shows provided and required interfaces, the C4 one shows what
is inside a container. They are separate entries; do not alias one onto the other.

## Audience tags

Every entry declares a primary audience and any secondary ones in `AUDIENCE` in
`entries.py`, keyed by entry name. `AUDIENCES` defines the seven: architect, developer,
operations, security, data, business, management.

Audience is often what actually decides between two similar diagrams — a context diagram
and a container diagram show the same system, but one is for a steering committee and the
other for the engineers building it.

Tags are searchable by the words people really type, not only the label: `AUDSYN` in
`build.py` maps each audience to its synonyms, so "BA", "SRE", "on-call", "CISO",
"exec" and "product" all find the right entries. Add a synonym there rather than
inventing a new audience.

No build step at serve time, no backend, no runtime dependencies. Only Google Fonts is
loaded externally; everything else, including all 95 sample diagrams, is inline SVG.

## Build

```bash
python build.py       # writes all 27 pages
```

No third-party packages. Python 3.8+.

## Layout

| File | Contains |
|---|---|
| `svg_kit.py` | Palette, SVG primitives (`node`, `arr`, `poly`, `frame`, `cyl`, `pill`, `classbox`, `lifelines`, `msg`, `dia`, `stick`, `oval`, `note`, `grid`), the `ICONS` glyph set and its box variants (`icon`, `inode`, `ihead`, `ilifelines`), arrowhead defs |
| `diagrams.py` | One `d_*()` function per diagram type, returning a complete `<svg>` string |
| `entries.py` | The 15 categories, the `STAGES` level definitions, the ordered `PATH`, the `QUESTIONS` table, and the 94 entries — all prose lives here |
| `build.py` | CSS, page assembly, nav, the learning-path panel, client-side filter/search, plate validation |
| `index.html`, `pages/*.html` | Generated output — 27 pages. Do not edit by hand; every build overwrites them |

## Adding a diagram type

1. Write `d_yourthing()` in `diagrams.py` using the primitives. Canvas is 640 wide;
   height is whatever the drawing needs. Colours come from the module constants
   (`ACC`, `FLAG`, `GRN`, `AMB`, `VIO`, `MUTED`, `LINE`) — do not hard-code hex.
2. Add an `add(...)` call in `entries.py`:

```python
add(cat, name, level, defn, answers, when, must, fail, d_yourthing, caption,
    ["Other name it travels under", "…"])
```

   `cat` is 1–15 (see `CATS`), `level` is 1 (foundation), 2 (core practice) or
   3 (specialist) — see `STAGES`. The trailing alias list is optional but is what
   makes a synonym findable.
3. Tag it in `AUDIENCE` — `(primary, [also useful to])`. The build fails loudly if an
   entry is missing from that dict or names an audience that does not exist.
4. To put it on the learning path, add a row to `PATH` — `(level, step, label, entry
   name)`. `step` orders it within its level; the entry name must match exactly, and
   `build.py` resolves it to an anchor.
5. `python build.py`

## House style for the plates

Every sample renders on a fixed white sheet in both light and dark themes — the
drawing is always "on paper". Consequences:

- SVG colours are literal hex from `svg_kit.py`, never theme tokens.
- Text labels use `paint-order="stroke"` with a white halo so they stay legible
  where they cross a line.
- Boxes carry a title and an optional smaller subtitle (technology, cardinality,
  a constraint). Arrows carry a verb or a protocol, not nothing.
- Fill carries meaning. Give each box a semantic style rather than leaving it white:
  `acc` for the system's own components, `grn` for data at rest and success paths, `amb`
  for anything asynchronous, `vio` for external managed services, `flag` for failure,
  `soft` for out of scope. A drawing of white boxes reads as a wireframe, not a design.
- Keep text inside the shape that holds it. A long sentence belongs in a `note()`
  or in the footnote lines under the drawing, not in a `node()` subtitle.

### Zones and bands

`frame()` fills with a light wash of its own colour (`TINT`), so a grouping box reads as a
region and nesting is visible at a glance — a VPC inside a region, a trust boundary inside
the internet. Pass `fill="none"` for the old outline-only behaviour.

`band(x, y, w, h, title, colour)` draws a solid title bar over a tinted body: use it for
layered architectures, pipeline stages and swimlane headers.

### Icons

Infrastructure, deployment, DevOps, security and observability plates use `inode()`
instead of `node()`: a glyph on the left, text left-aligned after it. Those domains are
a vocabulary of recognisable things — a queue, a shield, a load balancer — and flat
boxes make them all look alike.

```python
inode(x, y, w, h, title, sub, style, "server")     # glyph left, text left-aligned
ihead(x, y, w, h, title, "shield")                 # glyph above a centred caption
ilifelines([(x, w, name, glyph, style), ...])      # sequence headers with glyphs
grid(..., rowicons=[("lock", ACC), ...])           # a glyph per table row
```

Glyphs live in `ICONS` as path data on a 24×24 grid, stroked and never filled, so the
weight stays even at any size. They take the box's own accent (`ICON_COLOR`), which
adds colour without adding noise. Add one by appending path strings to `ICONS`.

Budget roughly 37px of the box width for `pad + icon + gap` at the default size — a
title that fitted a centred `node()` may not fit an `inode()` of the same width.

### Validation

`build.py` runs two checks before writing.

`check_plates()` fails the build if any plate emits an invalid `fill` or `stroke`.
This catches the easiest mistake to make with these primitives: passing a value into
the wrong positional slot — for example `stick(x, y, "Payment provider", "«system»")`,
where the fourth argument is `color`, not `sub`. Browsers drop an invalid paint value
silently, so the shape simply disappears with no error.

`check_text_fit()` warns (does not fail) when a left-aligned `inode()` label looks
like it runs past its box. The estimate is rough — ~0.5em per character — so treat it
as a prompt to look, not a verdict.

Worth checking by eye after adding a plate: nothing drawn outside the `viewBox`
(it is clipped without warning), and no two boxes overlapping.

## Theming

The page supports light, dark and unset (`prefers-color-scheme`). All colours are
CSS custom properties declared on bare `:root`, then redefined in
`@media (prefers-color-scheme: dark)` guarded as `:root:not([data-theme="light"])`,
and again under `:root[data-theme="dark"]`. Never define a colour only inside one
of those blocks.

Body copy is IBM Plex Sans; headings, nav and the plate labels are IBM Plex Sans
Condensed; metadata is IBM Plex Mono.

## Publishing

All pages are flat files at the repo root with relative links, so GitHub Pages from the
root works with no configuration, and the site also browses correctly over `file://`.

Renaming a category or level changes its filename; the old page is not deleted
automatically, so remove stale `.html` files by hand after a rename.

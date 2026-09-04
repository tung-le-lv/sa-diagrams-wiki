# Building this site

How the generator works. What the site is *for* is in [README.md](README.md).

## Site structure

The build emits **27 static pages** and three shared assets — one per category and per
audience, so no page carries the whole dictionary:

| Page | Contains |
|---|---|
| `index.html` | Overview: the frequency panel, the question → diagram table, and the category index |
| `pages/questions.html` | Question → diagram, and every type by the question it answers |
| `pages/audience-<key>.html` | Every entry drawn primarily for one audience, plus the ones they also read (7 pages) |
| `pages/<category-slug>.html` | Every entry in one category (18 pages) — an entry's canonical home |

`index.html` stays at the repo root because GitHub Pages needs it there; every other page
lives in `pages/`. Links are generated through `P(target, root)`, which knows whether the
page being written sits at the root or inside `pages/` — never hard-code a page link.

Each entry appears on two axes: its category page (the canonical URL and anchor) and its
audience page. Search is global — every page loads one shared index of
all 110 types and links results to their canonical page and anchor, so searching from any
page finds everything.

## The overview's fourth axis

`FREQUENCY` in `entries.py` is the panel on the front page that answers the question the
other axes dodge: not what a diagram is or who it is for, but **how often a software
architect actually draws it**. Five types carry most of the work; presenting all 110 as
equals is not honest about that, and a newcomer deserves the shortlist.

`FREQUENCY_LEAD` says whose chair the ranking is made from, because it is not a neutral
ordering — a BA, a UX designer and an SRE would each sort the same 110 types differently,
and each would be right about their own job. Stating the perspective is more useful than
implying there isn't one.

Each row is `(label, target, gloss)`. `target` is an entry name, `"cat:<slug>"` for a whole
category (C4 points at its category, not at one of its four levels), a list of names
rendered as several links, or `""` for something deliberately *not* in the dictionary.
`label` of `None` reuses the target's own name. `check_frequency()` fails the build on a
target that no longer resolves, so renaming an entry cannot leave the front page lying.

## Ordering within a category

Entries appear in declaration order, and that order is meaningful: **each category runs
most-used first**. It also sets the `NN.n` plate numbers and the order entries appear on
a category page, so there is one source of truth — move the `add(...)` call to change the
order.

`python build.py` prints what each category holds at the end of the run — `.` for an
entry filed there, `+` for one it only borrows — so an entry in the wrong place is easy
to spot:

```
   03 UML                         +.+...........  14 types
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
(category, audience), so a third appearance costs only page weight. Several
diagrams genuinely belong in two places, and the source notes cross-list them too.

A borrowed entry keeps its canonical plate number and links back to where it is filed, and
is marked *also shown here*, so the reader can tell which page owns it. Nav counts show
what a page actually contains, so they sum to more than the entry count.

`UML_14` lists UML 2.5's fourteen types in their two groups of seven; the UML page renders
that panel and, thanks to `ALSO_IN`, all fourteen entries are on the page.

`C4_SET` does the same job for the C4 model: four levels of zoom plus the supplementary
views, mapped so the C4 page can show all seven and say where each one is filed. Both
panels are rendered by `canon_cols()` and located by slug (`CAT_C4`, `CAT_UML`) rather
than by a hard-coded number, so inserting a category ahead of them cannot silently point
a panel at the wrong page.

Note that a UML component diagram and a C4 component diagram are different things that
share a word: the UML one shows provided and required interfaces, the C4 one shows what
is inside a container. They are separate entries; do not alias one onto the other.

For the same reason, hexagonal architecture is **not** cross-listed onto the UML page.
It shares the ports-and-interfaces vocabulary with the composite structure and UML
component diagrams, but it is an architectural pattern rather than a notation, and
category 3 asserts that it holds UML 2.5's canonical fourteen. That kinship belongs in
`RELATED`, not in `ALSO_IN` — which is the general rule: cross-list by *category*, link
by *relationship*.

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

## See also

`RELATED` in `entries.py` maps an entry name to the entries worth opening next. Aliases
say what a diagram is *called*; this says what to read after it, which is what a
dictionary otherwise cannot express — a saga makes no sense without the outbox, and a
bounded context map is half an answer without the team topology beside it.

Links are one-directional on purpose. "Read the ERD next" and "read the domain model
next" are different pieces of advice, so most pairs are listed both ways but not all.
Keep it to three or four per entry; a see-also list of nine is a list nobody follows.

No build step at serve time, no backend, no runtime dependencies. Only Google Fonts is
loaded externally; everything else, including all 110 sample diagrams, is inline SVG.

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
| `entries.py` | The 18 categories, the `QUESTIONS` table, `FREQUENCY`, the `RELATED` see-also graph, and the 110 entries — all prose lives here |
| `build.py` | CSS, page assembly, nav, the frequency panel, the on-this-page TOC, client-side filter/search, plate validation |
| `index.html`, `pages/*.html` | Generated output — 27 pages. Do not edit by hand; every build overwrites them |
| `assets/` | Generated output — `site.css`, `search-index.js`, `site.js`. Written once, cached by the browser |
| `sitemap.xml`, `robots.txt` | Generated output — needs an absolute base URL (see **Publishing**) |

## Adding a diagram type

1. Write `d_yourthing()` in `diagrams.py` using the primitives. Canvas is 640 wide;
   height is whatever the drawing needs. Colours come from the module constants
   (`ACC`, `FLAG`, `GRN`, `AMB`, `VIO`, `MUTED`, `LINE`) — do not hard-code hex.
2. Add an `add(...)` call in `entries.py`:

```python
add(cat, name, defn, answers, when, must, fail, d_yourthing, caption,
    ["Other name it travels under", "…"])
```

   `cat` is 1–18 (see `CATS`). The trailing alias list is optional but is what makes a
   synonym findable.
3. Tag it in `AUDIENCE` — `(primary, [also useful to])`. The build fails loudly if an
   entry is missing from that dict or names an audience that does not exist.
4. If it belongs on the front page, add a row to `FREQUENCY` in the group that matches
   how often it is really drawn.
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

`check_related()` fails the build on a `RELATED` entry pointing at a name that does not
exist, or at itself. A see-also is rendered on every page an entry appears on, so one
typo is a dead link on every page it appears.

`check_audiences()` fails the build if an entry is untagged or names an audience that
does not exist.

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

## Page weight

CSS, the search index and the search script are written once to `assets/` rather than
inlined into every page. That matters more than it sounds: the boilerplate is ~117 KB,
and inlining it into twenty-seven pages cost about 3.4 MB of duplicated bytes and re-downloaded
it on every navigation. The pages themselves carry only their own plates.

## Publishing

All pages are flat files with relative links, so GitHub Pages from the repo root works
with no configuration and the site also browses correctly over `file://`.

Canonical links, Open Graph tags and `sitemap.xml` need an absolute base URL. `build.py`
derives one from the `origin` git remote (`https://<user>.github.io/<repo>`); override it
when the site is served from somewhere else:

```bash
SITE_URL=https://diagrams.example.com python build.py
```

With no remote and no `SITE_URL`, the build still succeeds — it just skips `sitemap.xml`,
`robots.txt` and the absolute-URL tags, and says so.

Renaming a category changes its filename; the old page is not deleted
automatically, so remove stale `.html` files by hand after a rename.

## The right-hand column

Every page that lists entries gets a third column: what is on this page, in page order,
with the entry currently under the header highlighted as you scroll. `toc()` in
`build.py` builds it from the same list the page renders, so it cannot drift, and the
scroll-spy is a plain scroll handler rather than an `IntersectionObserver` — the rule is
"the last entry whose top has passed under the sticky header", which is what a reader
means by *where am I*.

Pages carrying a TOC get `.shell.has-toc`, which widens the grid to 1400px rather than
squeezing the middle column: the plates have a `min-width` of 560px and would otherwise
start scrolling sideways. Below 1300px the column is dropped and the shell reverts to
two columns. It is also hidden while search results are showing, since the results have
replaced the page the contents list describes.

`index.html` and the question page have no entries, so they have no TOC and stay at the
narrower two-column width.

## Accessibility and print

Every plate is `role="img"` with `aria-labelledby` pointing at its own `<figcaption>`, so
a screen reader announces the caption instead of skipping an unlabelled graphic. The page
declares `<html lang="en">`.

There is a print stylesheet: it drops the nav, header and search, and prevents entries,
plates and fact tables from breaking across pages. This is a reference — people save it
as a PDF.

# SA Diagrams Wiki

A single-page diagram dictionary for software architects: **94 diagram types across 15
categories**, each with a sample plate, the question it answers, when to reach for it,
what it must show, and the mistake that shows up in review.

Every named diagram type in `docs/` is covered — either as its own entry or as a listed
alias on the entry that subsumes it, so alternative vocabulary stays searchable.

The page also carries **the architect's shortlist**: the 34 types ranked in the source
notes under *"The diagrams I'd prioritize for a Software Architect"*, plus the
question → diagram lookup table. It is a nav filter of its own, alongside the tiers and
the 15 categories.

The output is one self-contained `index.html` — no build step at serve time, no backend,
no runtime dependencies. Only Google Fonts is loaded externally; everything else,
including all 94 sample diagrams, is inline SVG.

## Build

```bash
python build.py       # writes index.html
```

No third-party packages. Python 3.8+.

## Layout

| File | Contains |
|---|---|
| `svg_kit.py` | Palette, SVG primitives (`node`, `arr`, `poly`, `frame`, `cyl`, `pill`, `classbox`, `lifelines`, `msg`, `dia`, `stick`, `oval`, `note`, `grid`), arrowhead defs |
| `diagrams.py` | One `d_*()` function per diagram type, returning a complete `<svg>` string |
| `entries.py` | The 15 categories, the ranked `PRIORITY` shortlist, the `QUESTIONS` table, and the 94 entries — all prose lives here |
| `build.py` | CSS, page assembly, nav, the shortlist panel, client-side filter/search, plate validation |
| `index.html` | Generated output. Do not edit by hand — it is overwritten by every build |

## Adding a diagram type

1. Write `d_yourthing()` in `diagrams.py` using the primitives. Canvas is 640 wide;
   height is whatever the drawing needs. Colours come from the module constants
   (`ACC`, `FLAG`, `GRN`, `AMB`, `VIO`, `MUTED`, `LINE`) — do not hard-code hex.
2. Add an `add(...)` call in `entries.py`:

```python
add(cat, name, tier, defn, answers, when, must, fail, d_yourthing, caption,
    ["Other name it travels under", "…"])
```

   `cat` is 1–15 (see `CATS`), `tier` is 1 (must know), 2 (very important) or
   3 (know when to use). The trailing alias list is optional but is what makes a
   synonym findable. Entries are numbered `NN.n` automatically by category and
   position, so order within `entries.py` sets the plate numbers.
3. To put it on the shortlist, add a row to `PRIORITY` — `(tier, rank, label, entry name)`.
   The entry name must match exactly; `build.py` resolves it to an anchor.
4. `python build.py`

## House style for the plates

Every sample renders on a fixed white sheet in both light and dark themes — the
drawing is always "on paper". Consequences:

- SVG colours are literal hex from `svg_kit.py`, never theme tokens.
- Text labels use `paint-order="stroke"` with a white halo so they stay legible
  where they cross a line.
- Boxes carry a title and an optional smaller subtitle (technology, cardinality,
  a constraint). Arrows carry a verb or a protocol, not nothing.
- Emphasis is the `acc` style, spent on at most one or two boxes per drawing.
- Keep text inside the shape that holds it. A long sentence belongs in a `note()`
  or in the footnote lines under the drawing, not in a `node()` subtitle.

### Validation

`build.py` runs `check_plates()` before writing, and fails the build if any plate
emits an invalid `fill` or `stroke`. This catches the easiest mistake to make with
these primitives: passing a value into the wrong positional slot — for example
`stick(x, y, "Payment provider", "«system»")`, where the fourth argument is `color`,
not `sub`. Browsers drop an invalid paint value silently, so the shape simply
disappears with no error.

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

`index.html` is standalone, so GitHub Pages from the repo root works with no
configuration.

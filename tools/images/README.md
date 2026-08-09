# tools/images — index

✅ VENDORED + PROVEN 2026-08-09. Source: storybook pipeline — **neutral tooling only**, no
commercial content crosses over (AGENTS.md §1).

| File | Role |
|---|---|
| `make_strips.py` | Generates the four reusable white partition-strip assets (torn edges, faint paper grain). Run once |
| `apply_strips.py` | Applies a strip through a living being per `placements.json`; images marked `null` are copied through byte-identical |
| `verify_strip.py` | Measures band centre, span and coverage **on the output raster** and fails if the band is not where it was asked to be |
| `pick_placements.py` | Interactive click-tool that produces `placements.json`. **VENDORED-UNPROVEN** — GUI, needs tkinter and a display |
| `crop_edges.py` | Batch-crops a percentage from all four edges (removes the AI-tool corner sparkle) |
| `SMOKE.md` | The runs, the fixture geometry, the calibration note and the negative tests |

Pipeline order: `crop_edges` → upscale (external) → `pick_placements` → `apply_strips` →
`verify_strip`.

## The rules this tooling serves live in canon, not here

`canon/image-rules/IMAGE_RULES.md` is the authority — objects-first, faceless figures where a
depiction is unavoidable, mahram-only grouping, C-05 applied last. **Cite it; do not restate it**
(AGENTS.md §8).

Note the boundary: **CD-007 ruled the storybook stripe doctrine out of scope for school canon.**
These scripts are the *mechanism*; when and where a stripe belongs for school output is not
settled by this folder and may not be inferred from it.

## Two things to know

**`verify_strip.py` was written here, not vendored.** The checklist expected pdftoppm
verification helpers from the storybook pipeline; none arrived, and none of the four vendored
scripts touches pdftoppm. Without a checker `apply_strips.py` could only be shown to run, not
to place the band correctly — which is not proof.

**Tolerance floor ~0.025.** Strip ends are feathered, so a measured span reads ~2% inside the
requested one. `--tol 0.03` is the working default; tightening below ~0.025 fails on geometry
that is actually correct. See `SMOKE.md`.

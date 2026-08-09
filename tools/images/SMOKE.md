# SMOKE.md — tools/images

Evidence that these tools have been **run**, not merely placed (AGENTS.md §5, CD-009).
Run 2026-08-09. Neutral tooling only — no storybook content crosses into this repo.

## Test fixture — a known largest-being region

A synthetic 1000×1000 page was built rather than using real artwork, so the being's geometry
is **known exactly** and placement can be asserted numerically instead of judged:

| Element | Region |
|---|---|
| Being (head + body) | x **0.30 – 0.62**, y **0.12 – 0.88**, midline x = 0.46 |
| Non-living object | x 0.70 – 0.85 (must NOT be striped) |
| Second image | no living being at all — must copy through untouched |

Placement spec: `{"x": 0.46, "y0": 0.12, "y1": 0.88, "strip": "strip-b"}` and `null`.

## Test 1 — `make_strips.py`

```
wrote strips/strip-a.png  (29x1200)
wrote strips/strip-b.png  (34x1200)
wrote strips/strip-c.png  (26x1200)
wrote strips/strip-d.png  (39x1200)
EXIT=0
```

## Test 2 — `apply_strips.py`

```
  STRIPED  being-01.png  (1 strip(s))
  copied   object-02.png  (no living being)

done -> out/  (2 images)
EXIT=0
```

## Test 3 — `verify_strip.py`, measured on the OUTPUT raster

Placement is asserted against the rendered pixels, not against the spec that produced them.

```
verify_strip — out/being-01.png  (1000x1000)
  band centre x = 0.460  (expected 0.460, tol 0.03)
  band width    = 0.005 of page
  band span y   = 0.142 .. 0.858  (expected 0.120 .. 0.880)
  coverage      = band INSIDE being region [0.300, 0.620]
RESULT: PASS (0 fail)
EXIT=0
```

**Calibration note, recorded rather than tuned away.** The measured span sits ~2% inside the
requested span (0.142 vs 0.120, 0.858 vs 0.880) because the strip's ends are feathered — the
torn-paper mask fades before the nominal edge, so near-white detection begins slightly inside.
It passes at `--tol 0.03`; a tolerance below ~0.025 would fail on geometry that is actually
correct. **The band still fully crosses the being**, which is what the rule requires.

## Test 4 — copy-through path is byte-identical

```
src sha dfc4d1644eb519cc
out sha dfc4d1644eb519cc
IDENTICAL
```

A no-living-being image is copied, not re-encoded. Worth asserting: silent re-encoding would
degrade artwork on every pipeline run.

## Test 5 — eyeball on the raster

Evidence committed permanently (CD-024): `evidence/fixture-before.png`,
`evidence/fixture-after.png`, `evidence/placements.json`.

Before/after compared visually. The band runs vertically **through the being only**, head-top
to feet, with irregular torn edges, and does **not** cross the whole page. The non-living object
beside the figure is untouched.

## Negative tests — the checker goes red when it should

A checker that has never failed proves nothing.

| Case | Result |
|---|---|
| Expected x=0.80, band actually at 0.46 | `FAIL (2 fail)` exit 1 — centre off, and outside being region |
| No strip applied at all (before vs before) | `FAIL (1 fail)` exit 1 — "no band detected" |
| Strip applied at x=0.05, off the being | `FAIL (2 fail)` exit 1 — centre off, outside being region |

## Test 6 — `crop_edges.py`

```
  being-01.png: (1000, 1000) -> (940, 940)  (cropped 3.0% + corner covered)
  object-02.png: (1000, 1000) -> (940, 940)  (cropped 3.0% + corner covered)
EXIT=0
```

3% per side on a 1000px image gives 940px — correct, and squareness preserved.

## Not proven here

**`pick_placements.py` is vendored but UNPROVEN — and cannot be proven headlessly.** It is an
interactive GUI (click head-top, click feet) and requires tkinter plus a display:

```
ModuleNotFoundError: No module named 'tkinter'
```

This is expected, not a defect: it is a human-in-the-loop placement tool, so "executed" would
mean a person clicking through real artwork. Its MANIFEST row stays **VENDORED-UNPROVEN**
(CD-020) until it is run on a workstation with a display.

## Commands

```
python3 tools/images/make_strips.py --height 2500 --out strips/
python3 tools/images/apply_strips.py --src images-approved --dst images-compliant \
        --strips strips --placements placements.json
python3 tools/images/verify_strip.py --before <src.png> --after <out.png> \
        --expect-x 0.46 --expect-y0 0.12 --expect-y1 0.88 --being-x0 0.30 --being-x1 0.62
python3 tools/images/crop_edges.py --src images-approved --dst images-cropped --percent 3
```

#!/usr/bin/env python3
"""verify_strip.py — measure a compliance strip on the OUTPUT raster.

Written for this repo (2026-08-09). The checklist expected "pdftoppm verification helpers"
from the storybook pipeline; none arrived and none of the four vendored scripts touches
pdftoppm. Without a checker, `apply_strips.py` can only be shown to *run*, not to have put the
band where it was asked to — which is not proof (AGENTS.md §5, CD-009).

What it measures, on the output image itself rather than on the placement spec:

  1. WHERE   — the horizontal centre of the detected white band, as a fraction of width.
  2. SPAN    — the topmost and bottommost rows the band occupies, as fractions of height.
  3. COVER   — whether the band actually crosses the declared being-region: does it fall
               inside [x0,x1] horizontally, and cover the region's vertical extent.

Detection: a column is "band" if, within the being's vertical range, its pixels are
near-white for most of that range. Compared against the ORIGINAL image so that white already
present in the artwork is not mistaken for the strip.

Usage:
    python3 verify_strip.py --before a.png --after b.png \
        --expect-x 0.46 --expect-y0 0.12 --expect-y1 0.88 \
        --being-x0 0.30 --being-x1 0.62 [--tol 0.03]

Exit 0 = every assertion passed. Exit 1 = at least one failed.
"""
import argparse
import sys

from PIL import Image

NEAR_WHITE = 235          # per-channel threshold
COL_FRACTION = 0.60       # a column counts as band if this share of the span is near-white


def near_white_mask(img):
    px = img.convert("RGB").load()
    w, h = img.size
    return [[all(c >= NEAR_WHITE for c in px[x, y]) for y in range(h)] for x in range(w)]


def detect_band(before, after, y0f, y1f):
    """Columns that became near-white in `after` but were not in `before`, within the span."""
    w, h = after.size
    y0, y1 = int(h * y0f), max(int(h * y1f), int(h * y0f) + 1)
    mb, ma = near_white_mask(before), near_white_mask(after)
    span = y1 - y0
    cols = []
    for x in range(w):
        gained = sum(1 for y in range(y0, y1) if ma[x][y] and not mb[x][y])
        if gained >= COL_FRACTION * span:
            cols.append(x)
    return cols, ma


def band_rows(ma, cols, h):
    if not cols:
        return None, None
    c = cols[len(cols) // 2]
    rows = [y for y in range(h) if ma[c][y]]
    return (min(rows), max(rows)) if rows else (None, None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--before", required=True)
    ap.add_argument("--after", required=True)
    ap.add_argument("--expect-x", type=float, required=True)
    ap.add_argument("--expect-y0", type=float, default=0.0)
    ap.add_argument("--expect-y1", type=float, default=1.0)
    ap.add_argument("--being-x0", type=float)
    ap.add_argument("--being-x1", type=float)
    ap.add_argument("--tol", type=float, default=0.03)
    args = ap.parse_args()

    before, after = Image.open(args.before), Image.open(args.after)
    if before.size != after.size:
        sys.exit(f"FAIL: size changed {before.size} -> {after.size}")
    w, h = after.size

    cols, ma = detect_band(before, after, args.expect_y0, args.expect_y1)
    fails = []
    print(f"verify_strip — {args.after}  ({w}x{h})")

    if not cols:
        print("  FAIL  no band detected: no column became near-white inside the span")
        print("RESULT: FAIL (1 fail)")
        sys.exit(1)

    centre = (cols[0] + cols[-1]) / 2 / w
    width_frac = (cols[-1] - cols[0] + 1) / w
    top, bot = band_rows(ma, cols, h)
    top_f, bot_f = top / h, (bot + 1) / h

    print(f"  band centre x = {centre:.3f}  (expected {args.expect_x:.3f}, tol {args.tol})")
    print(f"  band width    = {width_frac:.3f} of page")
    print(f"  band span y   = {top_f:.3f} .. {bot_f:.3f}  "
          f"(expected {args.expect_y0:.3f} .. {args.expect_y1:.3f})")

    if abs(centre - args.expect_x) > args.tol:
        fails.append(f"band centre {centre:.3f} is off expected {args.expect_x:.3f}")
    if abs(top_f - args.expect_y0) > args.tol:
        fails.append(f"band top {top_f:.3f} is off expected {args.expect_y0:.3f}")
    if abs(bot_f - args.expect_y1) > args.tol:
        fails.append(f"band bottom {bot_f:.3f} is off expected {args.expect_y1:.3f}")

    if args.being_x0 is not None and args.being_x1 is not None:
        inside = args.being_x0 <= centre <= args.being_x1
        print(f"  coverage      = band {'INSIDE' if inside else 'OUTSIDE'} being region "
              f"[{args.being_x0:.3f}, {args.being_x1:.3f}]")
        if not inside:
            fails.append("band does not fall within the declared being region")

    for f in fails:
        print(f"  FAIL  {f}")
    print(f"RESULT: {'FAIL' if fails else 'PASS'} ({len(fails)} fail)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()

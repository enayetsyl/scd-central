#!/usr/bin/env python3
"""grid_count_check.py — the coloured-grid figure, counted by machine · P-018 / CD-076

**Why this exists.** In অধ্যায় ৫ the figure IS the number. A ১০×১০ শতাংশ-ছক with ৪৮ cells
shaded *is* the value ০.৪৮, and a question authored from that page rests entirely on the count
being right. `math_arith_check.py` has nothing to say about it — there is no printed arithmetic
to check. It is CR-002's failure class (counting, not reading) at 100 cells per figure.

**What it is not.** It is not a replacement for the crop. PENDING-P-018's interim ruling stands
and is now permanent doctrine: **the 400 dpi crop is the authority; this is the second pair of
eyes.** On disagreement the crop wins and the disagreement is logged — but the disagreement is
now *produced*, which is the whole point. An ad-hoc sampler run once (CD-020) proves nothing;
a gate with seeded errors does.

**How it counts.** The lattice is located from the figure's own rules — the long dark runs that
bound it — and each cell is sampled at its centre, inside a margin that keeps the rules
themselves out of the sample. A cell counts as filled when its centre patch is darker or more
saturated than the page white by a stated threshold. Cells that land between the two (a cell
the sampler cannot call) are reported and the whole figure REFUSEs; a figure whose lattice
cannot be located REFUSEs. **Never silent** (§7.17(a)).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

try:
    from PIL import Image, ImageDraw
except Exception:                                            # pragma: no cover
    Image = None
    ImageDraw = None

# A cell is FILLED if its centre patch differs from paper white by more than FILL; it is EMPTY
# if it differs by less than EMPTY. Between the two the sampler declines to call it, and the
# figure REFUSEs rather than guessing — the one thing a counting gate must never do is round.
FILL = 0.28
EMPTY = 0.10
MARGIN = 0.28        # fraction of a cell ignored on each side, so a rule is never sampled


class GridResult:
    def __init__(self, status, detail, count=None, unsure=(), box=None):
        self.status, self.detail, self.count = status, detail, count
        self.unsure, self.box = tuple(unsure), box


def _gray(img):
    return img.convert("L")


def locate_grid(img, min_run=0.30):
    """-> (x0, y0, x1, y1) of the lattice, or None.

    Found from the figure's own rules: the longest dark horizontal and vertical runs. Deliberately
    dumb — it does not know how many cells there are, so it cannot be talked into a lattice that
    is not there. If the caller hands it a page with no grid it returns None and the caller
    REFUSEs.
    """
    g = _gray(img)
    w, h = g.size
    px = g.load()
    dark_cols = [x for x in range(w)
                 if sum(1 for y in range(h) if px[x, y] < 128) > min_run * h]
    if len(dark_cols) < 2:
        return None
    x0, x1 = dark_cols[0], dark_cols[-1]
    # **Two passes, and the second one is why this is not a toy.** Measuring dark rows across
    # the whole raster picked up the caption and the exercise's triangle above the figure, so
    # the located box was 482×592 on a square grid — every cell centre then landed on a rule
    # and the gate REFUSEd 21 cells. A grid's own rule spans essentially the whole grid width;
    # a line of text does not. So rows are measured **inside the located columns** and must
    # span most of them.
    span = max(1, x1 - x0)
    dark_rows = [y for y in range(h)
                 if sum(1 for x in range(x0, x1 + 1) if px[x, y] < 128) > 0.85 * span]
    if len(dark_rows) < 2:
        dark_rows = [y for y in range(h)
                     if sum(1 for x in range(x0, x1 + 1) if px[x, y] < 128) > min_run * span]
    if len(dark_rows) < 2:
        return None
    return x0, dark_rows[0], x1, dark_rows[-1]


def sample(img, rows, cols, box=None):
    """Count filled cells on an r×c lattice. -> GridResult."""
    if Image is None:
        return GridResult("REFUSE", "Pillow is not available in this environment")
    if rows < 1 or cols < 1:
        return GridResult("REFUSE", f"nonsensical lattice {rows}×{cols}")
    if box is None:
        box = locate_grid(img)
        if box is None:
            return GridResult("REFUSE",
                              "lattice could not be located — no long horizontal/vertical rule")
    x0, y0, x1, y1 = box
    if x1 - x0 < cols or y1 - y0 < rows:
        return GridResult("REFUSE", f"located box {x1-x0}×{y1-y0}px too small for {rows}×{cols}")
    rgb = img.convert("RGB")
    pr = rgb.load()
    cw, ch = (x1 - x0) / cols, (y1 - y0) / rows
    count, unsure = 0, []
    for r in range(rows):
        for c in range(cols):
            ax = x0 + c * cw + MARGIN * cw
            bx = x0 + (c + 1) * cw - MARGIN * cw
            ay = y0 + r * ch + MARGIN * ch
            by = y0 + (r + 1) * ch - MARGIN * ch
            n, acc = 0, 0.0
            for yy in range(int(ay), max(int(ay) + 1, int(by))):
                for xx in range(int(ax), max(int(ax) + 1, int(bx))):
                    R, G, B = pr[xx, yy]
                    # Distance from paper white, on both axes a shaded cell can move along:
                    # it may be darker (grey fill) or more saturated (colour fill).
                    dark = 1.0 - (R + G + B) / 765.0
                    sat = (max(R, G, B) - min(R, G, B)) / 255.0
                    acc += max(dark, sat)
                    n += 1
            v = acc / n if n else 0.0
            if v >= FILL:
                count += 1
            elif v > EMPTY:
                unsure.append((r + 1, c + 1, round(v, 3)))
    if unsure:
        return GridResult("REFUSE",
                          f"{len(unsure)} cell(s) between the filled and empty thresholds — "
                          f"the sampler declines to call them: "
                          + " · ".join(f"r{r}c{c}={v}" for r, c, v in unsure[:6]),
                          count, unsure, box)
    return GridResult("OK", f"{count} of {rows*cols} cell(s) filled", count, (), box)


def check(img, rows, cols, declared, box=None):
    res = sample(img, rows, cols, box)
    if res.status != "OK":
        return res
    if declared is None:
        return GridResult("REFUSE", res.detail + " — no declared count to compare against",
                          res.count, (), res.box)
    if res.count != declared:
        return GridResult("RED",
                          f"declared {declared} filled cell(s), sampler counts {res.count} "
                          f"on a {rows}×{cols} lattice — the crop is the authority (P-018), so "
                          f"re-count at 400 dpi and log the disagreement either way",
                          res.count, (), res.box)
    return GridResult("CLEAN", f"declared {declared} = sampled {res.count} "
                               f"on a {rows}×{cols} lattice", res.count, (), res.box)


# ------------------------------------------------------------------------ selftest
#
# Rasters are drawn in-test rather than read from disk. A fixture that lives in the repo can
# drift, be renamed, or quietly stop being regenerated; one that is drawn by the test cannot,
# and it bites on every run on every machine. CD-057.

def _draw_grid(rows, cols, filled, cell=24, rule=2, colour=(120, 190, 235), pad=6):
    img = Image.new("RGB", (cols * cell + 2 * pad, rows * cell + 2 * pad), "white")
    d = ImageDraw.Draw(img)
    for (r, c) in filled:
        d.rectangle([pad + c * cell, pad + r * cell,
                     pad + (c + 1) * cell, pad + (r + 1) * cell], fill=colour)
    for i in range(rows + 1):
        d.line([pad, pad + i * cell, pad + cols * cell, pad + i * cell], fill="black", width=rule)
    for j in range(cols + 1):
        d.line([pad + j * cell, pad, pad + j * cell, pad + rows * cell], fill="black", width=rule)
    return img


def selftest() -> int:
    if Image is None:
        print("grid_count_check: Pillow unavailable — selftest cannot run")
        return 1
    ok = True

    def report(good, label, got):
        nonlocal ok
        ok = ok and good
        print(f"[{'PASS' if good else 'FAIL':4}] {label} -> {got}")

    cells48 = [(r, c) for r in range(10) for c in range(10)][:48]
    img48 = _draw_grid(10, 10, cells48)

    r = check(img48, 10, 10, 48)
    report(r.status == "CLEAN", "control · a correct declared count (৪৮ of ১০০) -> CLEAN", r.status)

    r = check(img48, 10, 10, 47)
    report(r.status == "RED", "seed · declared one too few (৪৭) -> RED", r.status)

    r = check(img48, 10, 10, 49)
    report(r.status == "RED", "seed · declared one too many (৪৯) -> RED", r.status)

    # The চ্যানেল-অমিল case that started this: three grids on one printed page, ৪৮ · ৬০ · ৪৯.
    for n in (60, 49):
        im = _draw_grid(10, 10, [(r_, c_) for r_ in range(10) for c_ in range(10)][:n])
        res = check(im, 10, 10, n)
        report(res.status == "CLEAN", f"control · ছাপা ৬৩'s other grid ({n}) -> CLEAN", res.status)
        res = check(im, 10, 10, n - 1)
        report(res.status == "RED", f"seed · that grid declared {n-1} -> RED", res.status)

    blank = Image.new("RGB", (240, 240), "white")
    r = check(blank, 10, 10, 0)
    report(r.status == "REFUSE", "seed · no lattice on the page -> REFUSE, never a silent 0",
           r.status)

    # A cell shaded so faintly that the sampler cannot honestly call it must stop the figure,
    # not be rounded to empty. Rounding is how a counting gate lies.
    faint = _draw_grid(10, 10, cells48, colour=(246, 246, 246))
    faint2 = _draw_grid(10, 10, [], colour=(255, 255, 255))
    d = ImageDraw.Draw(faint2)
    d.rectangle([6, 6, 30, 30], fill=(228, 228, 228))
    for i in range(11):
        d.line([6, 6 + i * 24, 246, 6 + i * 24], fill="black", width=2)
        d.line([6 + i * 24, 6, 6 + i * 24, 246], fill="black", width=2)
    r = check(faint2, 10, 10, 1)
    report(r.status == "REFUSE", "seed · a cell between the thresholds -> REFUSE, not rounded",
           r.status)

    r = check(img48, 10, 10, None)
    report(r.status == "REFUSE", "seed · no declared count given -> REFUSE", r.status)

    r = check(img48, 0, 10, 48)
    report(r.status == "REFUSE", "seed · nonsensical lattice 0×10 -> REFUSE", r.status)

    # A 5×4 figure is not a 10×10 one: the gate must not silently accept the wrong lattice.
    small = _draw_grid(5, 4, [(0, 0), (0, 1), (1, 0)])
    r = check(small, 5, 4, 3)
    report(r.status == "CLEAN", "control · a 5×4 lattice counts too -> CLEAN", r.status)
    r = check(small, 5, 4, 4)
    report(r.status == "RED", "seed · 5×4 declared one too many -> RED", r.status)

    print("-" * 78)
    print("SELFTEST: " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("image", nargs="?", help="PNG of the figure (or of a page, cropped)")
    ap.add_argument("--rows", type=int, default=10)
    ap.add_argument("--cols", type=int, default=10)
    ap.add_argument("--declared", type=int, default=None,
                    help="the count the extraction states")
    ap.add_argument("--box", help="x0,y0,x1,y1 to skip lattice location")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.image:
        ap.error("an image is required unless --selftest")
    if Image is None:
        print("Pillow is not available")
        return 1
    box = tuple(int(v) for v in a.box.split(",")) if a.box else None
    img = Image.open(a.image)
    r = check(img, a.rows, a.cols, a.declared, box)
    print("grid_count_check.py — the coloured grid, counted (P-018 · CD-076)")
    print(f"image  : {a.image}")
    print(f"lattice: {a.rows}×{a.cols}" + (f" · box {r.box}" if r.box else ""))
    print("-" * 78)
    print(f"[{r.status:7}] {r.detail}")
    print("-" * 78)
    print("LIMITS : the 400 dpi crop is the authority (P-018); this is the second channel.")
    print("         On disagreement the crop wins and the disagreement is logged.")
    return {"CLEAN": 0, "RED": 2, "REFUSE": 3}.get(r.status, 3)


if __name__ == "__main__":
    sys.exit(main())

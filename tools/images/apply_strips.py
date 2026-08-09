#!/usr/bin/env python3
"""
apply_strips.py — Step 7 compliance pass.

Reads every image in images-approved/, applies a white partition strip
at the specified x-position for images flagged as containing a living
being, and writes everything to images-compliant/ (untouched images are
copied through unchanged).

Placement comes from placements.json — one line per image:

{
  "img-01.png": {"x": 0.46, "y0": 0.12, "y1": 0.88, "strip": "auto"},
  "img-02.png": null,                      <- no living being: copy through
  "img-03.png": {"x": 0.38, "y0": 0.30, "y1": 0.75, "strip": "strip-b"},
  ...
}

  x      : horizontal center of the line as a FRACTION of image width
           (0.0 = left edge, 0.5 = center, 1.0 = right edge) — the main
           character's vertical midline.
  y0, y1 : vertical START and END of the line as fractions of image
           height — the top of the character's head and the bottom of
           their feet. The line is drawn only inside this range, so it
           runs through the body, not across the whole page.
           Defaults: y0 = 0.0, y1 = 1.0 (full height) if omitted.
           Eyeball all three numbers in any image viewer;
           two decimals is plenty of precision.
  strip  : "auto" picks a variant deterministically per file (so re-runs
           are reproducible), or name one explicitly ("strip-a" ... "strip-d").
  null   : contains_living_being = false -> copied through unchanged.

Usage:
    python3 apply_strips.py --src images-approved --dst images-compliant \
                            --strips strips --placements placements.json

Tip: generate a skeleton placements.json first with --init, then fill in x:
    python3 apply_strips.py --src images-approved --init placements.json
"""

import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path

from PIL import Image

VARIANT_NAMES = ["strip-a", "strip-b", "strip-c", "strip-d"]
IMG_EXTS = {".png", ".jpg", ".jpeg", ".webp"}


def pick_variant(filename: str) -> str:
    """Deterministic 'random' variant per filename — reproducible re-runs."""
    h = int(hashlib.md5(filename.encode()).hexdigest(), 16)
    return VARIANT_NAMES[h % len(VARIANT_NAMES)]


def load_strip(strips_dir: Path, name: str, target_h: int) -> Image.Image:
    p = strips_dir / f"{name}.png"
    if not p.exists():
        sys.exit(f"ERROR: strip asset not found: {p} (run make_strips.py first)")
    strip = Image.open(p).convert("RGBA")
    if strip.height != target_h:  # scale to the page image height
        w = round(strip.width * target_h / strip.height)
        strip = strip.resize((w, target_h), Image.LANCZOS)
    return strip


def apply_one(img_path: Path, dst: Path, strips_dir: Path, x_frac: float,
              strip_name: str, y0: float = 0.0, y1: float = 1.0):
    img = Image.open(img_path).convert("RGBA")
    name = strip_name if strip_name != "auto" else pick_variant(img_path.name)
    top = round(img.height * y0)
    seg_h = max(1, round(img.height * (y1 - y0)))
    strip = load_strip(strips_dir, name, seg_h)   # scaled to the body span
    x = round(img.width * x_frac - strip.width / 2)
    x = max(0, min(x, img.width - strip.width))  # clamp inside the page
    img.alpha_composite(strip, (x, top))
    out = dst / img_path.name
    img.convert("RGB").save(out) if img_path.suffix.lower() in (".jpg", ".jpeg") \
        else img.save(out)
    print(f"  STRIPED  {img_path.name}  (x={x_frac:.2f}, y={y0:.2f}-{y1:.2f}, {name})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="images-approved")
    ap.add_argument("--dst", default="images-compliant")
    ap.add_argument("--strips", default="strips")
    ap.add_argument("--placements", default="placements.json")
    ap.add_argument("--init", metavar="FILE",
                    help="write a skeleton placements file for --src and exit")
    args = ap.parse_args()

    src = Path(args.src)
    images = sorted(p for p in src.iterdir()
                    if p.suffix.lower() in IMG_EXTS) if src.exists() else []
    if not images:
        sys.exit(f"ERROR: no images found in {src}/")

    if args.init:
        skeleton = {p.name: {"x": 0.50, "y0": 0.0, "y1": 1.0, "strip": "auto"}
                    for p in images}
        Path(args.init).write_text(json.dumps(skeleton, indent=2))
        print(f"wrote skeleton {args.init} — set x per image "
              f"(fraction of width), or null for no-living-being images")
        return

    placements = json.loads(Path(args.placements).read_text())
    dst = Path(args.dst)
    dst.mkdir(parents=True, exist_ok=True)
    strips_dir = Path(args.strips)

    missing = [p.name for p in images if p.name not in placements]
    if missing:
        sys.exit(f"ERROR: images missing from {args.placements}: {missing}")

    for p in images:
        spec = placements[p.name]
        if spec is None:
            shutil.copy2(p, dst / p.name)
            print(f"  copied   {p.name}  (no living being)")
        else:
            specs = spec if isinstance(spec, list) else [spec]
            img = Image.open(p).convert("RGBA")
            for s in specs:
                name = s.get("strip", "auto")
                name = name if name != "auto" else pick_variant(
                    p.name + str(round(float(s["x"]) * 100)))
                span_px = max(1, round(img.height *
                                       (float(s.get("y1", 1.0)) -
                                        float(s.get("y0", 0.0)))))
                strip = load_strip(strips_dir, name, span_px)
                x = round(img.width * float(s["x"]) - strip.width / 2)
                x = max(0, min(x, img.width - strip.width))
                y = round(img.height * float(s.get("y0", 0.0)))
                img.alpha_composite(strip, (x, y))
            out = dst / p.name
            img.convert("RGB").save(out) if p.suffix.lower() in (".jpg", ".jpeg") \
                else img.save(out)
            print(f"  STRIPED  {p.name}  ({len(specs)} strip(s))")

    print(f"\ndone -> {dst}/  ({len(images)} images)")


if __name__ == "__main__":
    main()

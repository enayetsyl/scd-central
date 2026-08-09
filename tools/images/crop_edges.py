#!/usr/bin/env python3
"""
crop_edges.py — batch-crop a small percentage from all four edges.

Removes the AI-tool sparkle watermark in the corner (and trims painted
cream borders) while keeping the image square. Run BEFORE upscaling.

Usage:
    python crop_edges.py --src images-approved --dst images-cropped --percent 3

--percent 3 removes 3% from EACH side (1024px image -> ~963px).
Use --percent 0 --only-corner to instead paint over just the corner
sparkle with a sampled background color (when you can't afford to lose
edge content, e.g., the cover).
"""

import argparse
import sys
from pathlib import Path

from PIL import Image

IMG_EXTS = {".png", ".jpg", ".jpeg", ".webp"}


def crop_percent(img: Image.Image, pct: float) -> Image.Image:
    w, h = img.size
    dx, dy = round(w * pct / 100), round(h * pct / 100)
    return img.crop((dx, dy, w - dx, h - dy))


def cover_corner(img: Image.Image) -> Image.Image:
    """Paint over the bottom-right sparkle with color sampled nearby."""
    img = img.convert("RGB")
    w, h = img.size
    # sparkle sits in roughly the last 6% square of the bottom-right
    box = (round(w * 0.93), round(h * 0.93), w, h)
    # sample the color just left of the box as the fill
    sample = img.getpixel((round(w * 0.90), round(h * 0.965)))
    patch = Image.new("RGB", (box[2] - box[0], box[3] - box[1]), sample)
    img.paste(patch, (box[0], box[1]))
    return img


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="images-approved")
    ap.add_argument("--dst", default="images-cropped")
    ap.add_argument("--percent", type=float, default=3.0,
                    help="percent to crop from each side (default 3)")
    ap.add_argument("--only-corner", action="store_true",
                    help="don't crop; just paint over the corner sparkle")
    args = ap.parse_args()

    src, dst = Path(args.src), Path(args.dst)
    images = sorted(p for p in src.iterdir()
                    if p.suffix.lower() in IMG_EXTS) if src.exists() else []
    if not images:
        sys.exit(f"ERROR: no images found in {src}/")
    dst.mkdir(parents=True, exist_ok=True)

    for p in images:
        img = Image.open(p)
        if args.only_corner:
            out = cover_corner(img)
            note = "corner covered"
        else:
            out = crop_percent(img, args.percent)
            if args.percent < 5:          # sparkle may survive small crops
                out = cover_corner(out)
                note = f"cropped {args.percent}% + corner covered"
            else:
                note = f"cropped {args.percent}%"
        out.save(dst / p.name)
        print(f"  {p.name}: {img.size} -> {out.size}  ({note})")

    print(f"\ndone -> {dst}/  ({len(images)} images)")


if __name__ == "__main__":
    main()

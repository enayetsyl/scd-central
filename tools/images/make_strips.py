#!/usr/bin/env python3
"""
make_strips.py — generate reusable white partition-strip assets.

Creates 4 variants of a vertical white band with irregular torn-paper
edges and a faint paper texture, on a transparent background.
Run once; the strips are then reused by apply_strips.py forever.

Usage:
    python3 make_strips.py [--height 2500] [--out strips/]
"""

import argparse
import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

# ---------------------------------------------------------------- settings
# Each variant: (base width as fraction of height, edge roughness px, seed)
VARIANTS = [
    {"name": "strip-a", "width_frac": 0.006, "rough": 3, "seed": 11},
    {"name": "strip-b", "width_frac": 0.009, "rough": 4, "seed": 42},
    {"name": "strip-c", "width_frac": 0.005, "rough": 2, "seed": 77},
    {"name": "strip-d", "width_frac": 0.011, "rough": 5, "seed": 123},
]
WHITE = (255, 253, 250)          # warm white, sits well on cream watercolor
TEXTURE_OPACITY = 14             # 0-255; very subtle paper grain
EDGE_SOFTNESS = 0.6              # gaussian blur radius on the mask edges


def torn_edge_offsets(height: int, rough: int, seed: int, points: int = 60):
    """Return a smooth list of per-row horizontal offsets for one torn edge."""
    rng = random.Random(seed)
    # control points, then cosine-interpolate between them
    ctrl = [rng.uniform(-rough, rough) for _ in range(points)]
    offsets = []
    seg = height / (points - 1)
    for y in range(height):
        i = min(int(y / seg), points - 2)
        t = (y - i * seg) / seg
        t = (1 - math.cos(t * math.pi)) / 2  # smooth
        base = ctrl[i] * (1 - t) + ctrl[i + 1] * t
        # add fine jitter for the fibrous torn look
        base += rng.uniform(-0.8, 0.8)
        offsets.append(base)
    return offsets


def make_strip(height: int, width_frac: float, rough: int, seed: int) -> Image.Image:
    width = int(height * width_frac)
    pad = rough + 8                       # room for the torn edges
    W = width + pad * 2
    img = Image.new("RGBA", (W, height), (0, 0, 0, 0))

    # --- build the opaque mask with two independent torn edges
    mask = Image.new("L", (W, height), 0)
    d = ImageDraw.Draw(mask)
    left = torn_edge_offsets(height, rough, seed)
    right = torn_edge_offsets(height, rough, seed + 1000)
    for y in range(height):
        x0 = pad + left[y]
        x1 = pad + width + right[y]
        d.line([(x0, y), (x1, y)], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(EDGE_SOFTNESS))
    # taper the top and bottom 3% so the line fades in/out naturally
    taper = int(height * 0.03)
    px = mask.load()
    for y in range(taper):
        f = y / taper
        for x in range(W):
            px[x, y] = int(px[x, y] * f)
            px[x, height - 1 - y] = int(px[x, height - 1 - y] * f)

    # --- fill with warm white
    white = Image.new("RGBA", (W, height), WHITE + (255,))
    img = Image.composite(white, img, mask)

    # --- faint paper texture (random speckle, blurred)
    rng = random.Random(seed + 5)
    tex = Image.new("L", (W, height), 0)
    td = ImageDraw.Draw(tex)
    for _ in range(int(W * height / 900)):
        x, y = rng.randrange(W), rng.randrange(height)
        td.point((x, y), fill=rng.randint(40, 110))
    tex = tex.filter(ImageFilter.GaussianBlur(0.8))
    grain = Image.new("RGBA", (W, height), (180, 172, 160, 0))
    grain.putalpha(tex.point(lambda v: min(v, TEXTURE_OPACITY)))
    img = Image.alpha_composite(img, Image.composite(
        grain, Image.new("RGBA", (W, height), (0, 0, 0, 0)), mask))

    return img


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--height", type=int, default=2500,
                    help="strip height in px (match your page image height)")
    ap.add_argument("--out", default="strips", help="output folder")
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for v in VARIANTS:
        strip = make_strip(args.height, v["width_frac"], v["rough"], v["seed"])
        p = out / f'{v["name"]}.png'
        strip.save(p)
        print(f"wrote {p}  ({strip.width}x{strip.height})")


if __name__ == "__main__":
    main()

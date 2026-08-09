#!/usr/bin/env python3
"""
pick_placements.py — fill placements.json with two clicks per image.

Shows each image in a window. For each image:

  CLICK 1  on the TOP of a character's head
  CLICK 2  on the BOTTOM of their feet/body
           -> records ONE strip for that character (drawn as a blue line).
  Repeat the click-pair for additional living beings if your rule
  requires striping more than the main character.
  Press ENTER to save this image's strips and advance.

  Keys:
    ENTER = save strips for this image, next image
    n  = no living being in this image (writes null), advances
    k  = keep existing saved entry, advance (skip)
    u  = undo last click
    r  = redo this image from scratch
    b  = go back one image
    q  = save what's done so far and quit

placements.json is saved after EVERY image, so quitting mid-way is safe.
Existing entries are loaded, so you can resume or fix single images.

Usage:
    python pick_placements.py --src images-upscaled --out placements.json
"""

import argparse
import json
import sys
import tkinter as tk
from pathlib import Path

from PIL import Image, ImageTk

IMG_EXTS = {".png", ".jpg", ".jpeg", ".webp"}
MAX_VIEW = 820  # window size for the preview


class Picker:
    def __init__(self, images, out_path):
        self.images = images
        self.out_path = out_path
        self.data = {}
        if out_path.exists():
            try:
                self.data = json.loads(out_path.read_text())
            except Exception:
                pass
        self.i = 0
        self.clicks = []

        self.root = tk.Tk()
        self.root.title("placements picker")
        self.label = tk.Label(self.root, font=("Segoe UI", 11))
        self.label.pack(pady=4)
        self.canvas = tk.Canvas(self.root, width=MAX_VIEW, height=MAX_VIEW,
                                cursor="crosshair", bg="#222")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        self.root.bind("n", lambda e: self.mark_null())
        self.root.bind("k", lambda e: self.keep())
        self.root.bind("<Return>", lambda e: self.commit())
        self.root.bind("u", lambda e: self.undo())
        self.root.bind("r", lambda e: self.redo())
        self.root.bind("b", lambda e: self.back())
        self.root.bind("q", lambda e: self.quit())
        self.show()
        self.root.mainloop()

    # ---------------------------------------------------------------- ui
    def show(self):
        if self.i >= len(self.images):
            self.save()
            done = sum(1 for v in self.data.values() if v is not None)
            nul = sum(1 for v in self.data.values() if v is None)
            self.label.config(
                text=f"ALL DONE — {done} striped, {nul} null. "
                     f"Saved to {self.out_path.name}. Press q to close.")
            self.canvas.delete("all")
            return
        p = self.images[self.i]
        self.clicks = []
        self.segments = []
        img = Image.open(p)
        self.orig_w, self.orig_h = img.size
        self.scale = min(MAX_VIEW / img.width, MAX_VIEW / img.height, 1.0)
        view = img.resize((round(img.width * self.scale),
                           round(img.height * self.scale)), Image.LANCZOS)
        self.tkimg = ImageTk.PhotoImage(view)
        self.canvas.delete("all")
        self.canvas.config(width=view.width, height=view.height)
        self.canvas.create_image(0, 0, anchor="nw", image=self.tkimg)
        existing = ""
        if p.name in self.data:
            v = self.data[p.name]
            existing = "  [saved: null]" if v is None else \
                f"  [saved: x={v['x']} y0={v['y0']} y1={v['y1']}]"
        self.label.config(
            text=f"{self.i+1}/{len(self.images)}  {p.name}{existing}   "
                 f"— click pairs: HEAD then FEET per character  |  "
                 f"ENTER=save+next  n=null  k=keep  u=undo  b=back  q=quit")

    def on_click(self, ev):
        self.clicks.append((ev.x, ev.y))
        r = 5
        self.canvas.create_oval(ev.x-r, ev.y-r, ev.x+r, ev.y+r,
                                outline="red", width=2)
        if len(self.clicks) == 2:
            (x1, y1), (x2, y2) = self.clicks
            self.clicks = []
            if y2 < y1:                     # clicked feet first — swap
                y1, y2 = y2, y1
            x = ((x1 + x2) / 2) / self.scale / self.orig_w
            y0 = y1 / self.scale / self.orig_h
            y1f = y2 / self.scale / self.orig_h
            self.segments.append({"x": round(x, 2), "y0": round(y0, 2),
                                  "y1": round(y1f, 2), "strip": "auto"})
            # draw the recorded strip as a blue line for feedback
            vx = round(x * self.orig_w * self.scale)
            self.canvas.create_line(vx, y1, vx, y2, fill="#2a7fff", width=3)

    def commit(self):
        if not self.segments:
            return
        name = self.images[self.i].name
        self.data[name] = self.segments[0] if len(self.segments) == 1             else self.segments
        self.save()
        self.i += 1
        self.show()

    # ------------------------------------------------------------ actions
    def mark_null(self):
        self.data[self.images[self.i].name] = None
        self.save()
        self.i += 1
        self.show()

    def keep(self):
        """Advance without changing this image's saved entry."""
        self.i += 1
        self.show()

    def undo(self):
        if self.clicks:
            self.clicks.pop()
        elif self.segments:
            self.segments.pop()
        self.redraw_all()

    def redraw_all(self):
        keep_clicks, keep_segs = self.clicks[:], self.segments[:]
        self.show()
        self.clicks, self.segments = keep_clicks, keep_segs
        for (x, y) in self.clicks:
            r = 5
            self.canvas.create_oval(x-r, y-r, x+r, y+r,
                                    outline="red", width=2)
        for s in self.segments:
            vx = round(s["x"] * self.orig_w * self.scale)
            vy0 = round(s["y0"] * self.orig_h * self.scale)
            vy1 = round(s["y1"] * self.orig_h * self.scale)
            self.canvas.create_line(vx, vy0, vx, vy1, fill="#2a7fff", width=3)

    def redo(self):
        self.show()

    def back(self):
        if self.i > 0:
            self.i -= 1
            self.show()

    def redraw_clicks(self):
        self.show_keep_clicks = self.clicks[:]
        self.show()
        for (x, y) in self.show_keep_clicks:
            self.clicks.append((x, y))
            r = 5
            self.canvas.create_oval(x-r, y-r, x+r, y+r,
                                    outline="red", width=2)

    def save(self):
        self.out_path.write_text(json.dumps(self.data, indent=2))

    def quit(self):
        self.save()
        self.root.destroy()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="images-upscaled")
    ap.add_argument("--out", default="placements.json")
    args = ap.parse_args()
    src = Path(args.src)
    images = sorted(p for p in src.iterdir()
                    if p.suffix.lower() in IMG_EXTS) if src.exists() else []
    if not images:
        sys.exit(f"ERROR: no images found in {src}/")
    Picker(images, Path(args.out))


if __name__ == "__main__":
    main()

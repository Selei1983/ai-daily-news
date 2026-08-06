#!/usr/bin/env python3
"""Crop first-viewport screenshots: top-left 1280x720 region of the raw screenshot."""
import sys
from PIL import Image

def crop_top_left(src, dst, w=1280, h=720):
    im = Image.open(src)
    im = im.crop((0, 0, min(w, im.width), min(h, im.height)))
    im.save(dst)
    print(f"{dst}: {im.size}")

if __name__ == "__main__":
    crop_top_left(sys.argv[1], sys.argv[2])

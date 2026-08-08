#!/usr/bin/env python3
"""Analyze PNG: count unique colors and average brightness to detect blank screenshots."""
import sys
from PIL import Image

for path in sys.argv[1:]:
    im = Image.open(path).convert("RGB")
    small = im.resize((64, 36))
    colors = small.getcolors(64 * 36)
    n_unique = len(colors)
    # brightness
    px = list(small.getdata())
    avg = sum(sum(p) for p in px) / (len(px) * 3)
    # most common color share
    top = max(c for c, _ in colors) if colors else 0
    print(f"{path}: unique_colors={n_unique} avg_brightness={avg:.0f} top_color_share={top/ (64*36):.2%}")

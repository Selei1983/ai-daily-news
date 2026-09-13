#!/usr/bin/env python3
"""Generate the 0913 daily digest cover image (doubao, article size)."""
import subprocess, sys
from pathlib import Path

TOOLKIT = Path.home() / ".hermes/skills/openclaw-imports/wewrite/toolkit"
OUT = Path.home() / ".hermes/workspace/ai-daily-news/daily/images/cover-0913.png"

PROMPT = (
    "科技产品插画封面，主题「AI产业的油门与刹车：资本把智能推向公开资本市场的同时，造AI的人集体踩下刹车」。"
    "画面中央：一辆由发光蓝色电路与数据流构成的未来智能战车/机车，正沿着一条笔直的高速公路奔向远方地平线上一座巍峨的、灯火通明的古典交易所大楼（大楼尖顶悬浮着巨大的金色铜钟与翻滚的K线光柱，象征万亿美元IPO定价）；"
    "战车车头引擎喷射出汹涌的金色能量洪流与无数发光数据粒子，车身一半向前疾驰；"
    "车底伸出两只巨大的发光脚掌，同时踩在同一块金属踏板上——左脚是金色油门踏板，右脚是红色刹车踏板，刹车处迸溅出橙红色火花与减速光痕，形成鲜明的加速与刹车对撞；"
    "公路两侧：左侧是堆积如山的金色硬币、上升的火箭与账本（资本狂热），右侧是悬浮的红色警告三角、盾牌、减速带与悬停的巨大红色刹车盘（安全制动）；"
    "远景是横跨天际的数据中心与全息发光的城市轮廓，天空一半是炙热的金橙色晚霞、一半是冷静的深蓝紫夜色；"
    "整体深蓝紫科技色调配金色与红色高光，立体感与写实结合，构图饱满，电影级光照，高清渲染，画面内无文字。"
)

cmd = [sys.executable, "image_gen.py", "--prompt", PROMPT, "--output", str(OUT), "--size", "article"]
print("Running:", " ".join(cmd))
r = subprocess.run(cmd, cwd=str(TOOLKIT), capture_output=True, text=True, timeout=420)
print(r.stdout[-3000:])
if r.returncode != 0:
    print("STDERR:", r.stderr[-2000:])
    sys.exit(r.returncode)
print("Cover written:", OUT, OUT.exists())

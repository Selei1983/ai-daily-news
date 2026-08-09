#!/usr/bin/env python3
"""Generate cover image for the 0809 daily digest."""
import subprocess, sys

PROMPT = (
    "科技新闻杂志封面，主题：AI经济的管道时刻。"
    "画面中央是一个由光缆与光纤组成的发光网络枢纽，无数金色与蓝色数据流沿光纤向四周蔓延，"
    "象征AI数据中心的光互连成为新的瓶颈与机会；"
    "左侧一台悬浮的笔记本电脑发出蓝光，一束数据流接入其中，象征国行AI生态接入；"
    "右侧无数货币符号与广告位图形组成的数据瀑布，象征AI广告与变现经济；"
    "背景是深蓝紫的科技空间，点缀小型机器人剪影沿管线奔跑，"
    "构图大气，电影感打光，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0809.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

#!/usr/bin/env python3
"""Generate the 0908 daily digest cover image (doubao, 2560x1440 article size)."""
import subprocess, sys
from pathlib import Path

TOOLKIT = Path.home() / ".hermes/skills/openclaw-imports/wewrite/toolkit"
OUT = Path.home() / ".hermes/workspace/ai-daily-news/daily/images/cover-0908.png"

PROMPT = (
    "科技产品插画封面，主题「机器与机器对话」。画面中央：两台发光的AI主机/机器人头部面对面，"
    "它们之间没有文字气泡，而是由一条明亮的半透明数据光桥直接相连——光桥内部流动着粒子与神经网络波形，"
    "象征模型之间跳过语言直接交换隐藏状态；左侧主机屏幕上是简洁的即时通讯界面与绿色对话光点（AI替人社交），"
    "右侧是服务器机架与GPU芯片阵列，芯片之间同样有细小的光流相连（Agent互相协作）；"
    "背景顶部漂浮着两个遥相呼应的巨大半透明「大脑」，一个由电路构成、一个由星云构成，中间隔着若隐若现的黑色幕布，"
    "暗示人类越来越难读懂AI的思维。整体深蓝紫色科技色调配橙色与青绿色高光，扁平化与写实结合，构图饱满，高清渲染，画面内无文字。"
)

cmd = [sys.executable, "image_gen.py", "--prompt", PROMPT, "--output", str(OUT), "--size", "article"]
print("Running:", " ".join(cmd))
r = subprocess.run(cmd, cwd=str(TOOLKIT), capture_output=True, text=True, timeout=420)
print(r.stdout[-3000:])
if r.returncode != 0:
    print("STDERR:", r.stderr[-2000:])
    sys.exit(r.returncode)
print("Cover written:", OUT, OUT.exists())

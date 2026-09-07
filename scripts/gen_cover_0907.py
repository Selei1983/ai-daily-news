#!/usr/bin/env python3
"""Generate the 0907 daily digest cover image (doubao, 2560x1440 article size)."""
import subprocess, sys
from pathlib import Path

TOOLKIT = Path.home() / ".hermes/skills/openclaw-imports/wewrite/toolkit"
OUT = Path.home() / ".hermes/workspace/ai-daily-news/daily/images/cover-0907.png"

PROMPT = (
    "科技产品插画封面，主题「AI的动手时刻」。画面中央：一只发光的半透明机械手握着鼠标，"
    "光标正在点击电脑屏幕上的一款3D打印切片软件界面（Bambu Studio风格），屏幕旁边一台小型桌面3D打印机"
    "正在打印一个精巧的多孔格栅结构零件，零件泛着橙色高光；背景左侧是版权分账的抽象视觉：天平、合约纸张、"
    "金币与音乐音符在蓝色数据流中漂浮；背景右侧是视频社区与弹幕数据流的抽象视觉：播放按钮、弹幕光点、"
    "小机器人剪影。整体深蓝紫色科技色调配橙色高光，扁平化与写实结合，构图饱满，高清渲染，画面内无文字。"
)

cmd = [sys.executable, "image_gen.py", "--prompt", PROMPT, "--output", str(OUT), "--size", "article"]
print("Running:", " ".join(cmd))
r = subprocess.run(cmd, cwd=str(TOOLKIT), capture_output=True, text=True, timeout=420)
print(r.stdout[-3000:])
if r.returncode != 0:
    print("STDERR:", r.stderr[-2000:])
    sys.exit(r.returncode)
print("Cover written:", OUT, OUT.exists())

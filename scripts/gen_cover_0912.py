#!/usr/bin/env python3
"""Generate the 0912 daily digest cover image (doubao, 2560x1440 article size)."""
import subprocess, sys
from pathlib import Path

TOOLKIT = Path.home() / ".hermes/skills/openclaw-imports/wewrite/toolkit"
OUT = Path.home() / ".hermes/workspace/ai-daily-news/daily/images/cover-0912.png"

PROMPT = (
    "科技产品插画封面，主题「AI的出口时刻：当智能的产能已经在前面，竞争的焦点转向把智能变成资本、收入、分发与署名」。"
    "画面中央：一座由发光数据流浇筑而成的巨大智能水坝/闸门，闸门后蓄积着汹涌澎湃的蓝紫色智能洪流，"
    "洪流中奔腾着密密麻麻发光的AI Agent小机器人与数据碎片（象征过剩的智能产能）；"
    "水坝前方，洪流被精确地分流进四条奔向地平线的发光通道——"
    "第一条是金色管道，尽头悬浮着IPO铜钟、硬币堆与上升的K线柱（资本出口）；"
    "第二条是青蓝色管道，尽头是银行柜台、无代码应用工厂的齿轮与客服耳麦（收入出口）；"
    "第三条是洋红色管道，尽头是一只手握着手机、屏幕里飞出无数可交互发光卡片汇入信息流（分发出口）；"
    "第四条是白色知识光带，尽头是写满数学公式的黑板、奖章与一支悬空的粉笔（署名与功劳出口）；"
    "远景是横向延展的数据中心与全息发光的城市天际线；近景水面倒映出四条通道的光晕；"
    "整体深蓝紫色科技色调配金色与青绿高光，立体感与写实结合，构图饱满，电影级光照，高清渲染，画面内无文字。"
)

cmd = [sys.executable, "image_gen.py", "--prompt", PROMPT, "--output", str(OUT), "--size", "article"]
print("Running:", " ".join(cmd))
r = subprocess.run(cmd, cwd=str(TOOLKIT), capture_output=True, text=True, timeout=420)
print(r.stdout[-3000:])
if r.returncode != 0:
    print("STDERR:", r.stderr[-2000:])
    sys.exit(r.returncode)
print("Cover written:", OUT, OUT.exists())

#!/usr/bin/env python3
"""Generate the 0911 daily digest cover image (doubao, 2560x1440 article size)."""
import subprocess, sys
from pathlib import Path

TOOLKIT = Path.home() / ".hermes/skills/openclaw-imports/wewrite/toolkit"
OUT = Path.home() / ".hermes/workspace/ai-daily-news/daily/images/cover-0911.png"

PROMPT = (
    "科技产品插画封面，主题「AI的承载力：当智能的产能跑在供电、内存、制度与防线前面」。"
    "画面中央：一座由发光数据流浇筑而成的巨大「承重高架平台/桥梁」，桥面上奔跑着密密麻麻发光的AI Agent小机器人与数据流（象征暴涨的产能与需求），"
    "但支撑平台的四根巨型立柱都出现了橙红色裂纹与火花——第一根是噼啪冒弧光的电力高压线杆（供电），第二根是发烫发红的内存芯片条与内存模组（HBM与内存），"
    "第三根是排着长队、文件堆成山的政务窗口柜台（制度与公共服务拥堵），第四根是布满裂痕却仍发光的盾牌与锁链（安全防线）；"
    "桥下的深蓝色数据海洋里，漂浮着几台蒙尘、指示灯暗淡的GPU服务器机柜（象征吃灰闲置的算力中心）；"
    "远景一边是横向延展到地平线的座座数据中心与冷却管道、另一边是全息发光的城市与卫星地形的三维数字地球（世界模型）；"
    "近景有一条明亮的青色内存光带在一块小型计算芯片与一部手机之间流动（用手机级内存绕开HBM短缺）；"
    "整体深蓝紫色科技色调配青绿色高光与橙红色裂纹警示，立体感与写实结合，构图饱满，电影级光照，高清渲染，画面内无文字。"
)

cmd = [sys.executable, "image_gen.py", "--prompt", PROMPT, "--output", str(OUT), "--size", "article"]
print("Running:", " ".join(cmd))
r = subprocess.run(cmd, cwd=str(TOOLKIT), capture_output=True, text=True, timeout=420)
print(r.stdout[-3000:])
if r.returncode != 0:
    print("STDERR:", r.stderr[-2000:])
    sys.exit(r.returncode)
print("Cover written:", OUT, OUT.exists())

#!/usr/bin/env python3
"""Generate cover image for the 0810 daily digest."""
import subprocess, sys

PROMPT = (
    "科技新闻杂志封面，主题：AI的造物时代。"
    "画面中央是一座发光的未来工厂，传送带上源源不断产出金蓝色光点组成的Token数据方块，"
    "象征Token超级工厂把智能变成可规模化生产的工业品；"
    "左侧一台白色双轮人形机器人正在折叠收纳自己，旁边悬浮着一个甜甜圈形状的智能音箱，"
    "象征具身智能进入家庭与前沿实验室开始做消费硬件；"
    "右侧一块半透明的数字仪表盘显示着AI支出与ROI曲线，象征企业开始像管理预算一样管理AI成本；"
    "背景是深蓝紫色的工业穹顶与星空，光线硬朗，电影感打光，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0810.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

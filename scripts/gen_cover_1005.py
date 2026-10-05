#!/usr/bin/env python3
"""Generate the 1005 daily digest cover image (doubao, article size)."""
import subprocess, sys
from pathlib import Path

TOOLKIT = Path.home() / ".hermes/skills/openclaw-imports/wewrite/toolkit"
OUT = Path.home() / ".hermes/workspace/ai-daily-news/daily/images/cover-1005.png"

PROMPT = (
    "科技产品插画封面，主题「AI开始自己造AI：智能爆炸的临界点」。"
    "画面中央：一台由发光蓝色电路与金色神经元构成的巨型智能机器人，正坐在一条全息流水线前，亲手组装、打印出一台更小、更亮、更精密的迷你AI机器人；"
    "迷你机器人身上又伸出发光的机械臂，正在组装出第三代更小的机器人，形成一层层递归自复制、向无穷延伸的「AI造AI」视觉循环，螺旋状嵌套、层层发光；"
    "机器人背后，一条耀眼的金色指数曲线陡然上升，托起一座高速旋转的发光飞轮（象征研发自动化飞轮），飞轮上环绕着无数流动的数据粒子与代码符号；"
    "流水线的另一侧：堆积如山的白色文件、报告与漏洞清单如潮水般涌向一个瘦小的、坐在桌前的人类审核员，人显得渺小而被淹没（象征人类的验证体系被AI产出压垮）；"
    "整体深蓝紫科技色调，配金色与青蓝色高光，电影级打光，立体写实与插画结合，构图饱满，画面内无任何文字。"
)

cmd = [sys.executable, "image_gen.py", "--prompt", PROMPT, "--output", str(OUT), "--size", "article"]
print("Running:", " ".join(cmd))
r = subprocess.run(cmd, cwd=str(TOOLKIT), capture_output=True, text=True, timeout=420)
print(r.stdout[-3000:])
if r.returncode != 0:
    print("STDERR:", r.stderr[-2000:])
    sys.exit(r.returncode)
print("Cover written:", OUT, OUT.exists())

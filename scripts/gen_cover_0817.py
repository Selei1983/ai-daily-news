#!/usr/bin/env python3
"""Generate cover image for the 0817 daily digest."""
import subprocess, sys

PROMPT = (
    "科技新闻杂志封面，主题：AI的「数据重估×定价转身」时刻——具身智能数据荒漠被资本重估、大模型从价格战转向峰谷定价与不可替代性、巨头开始联合训练专属模型。"
    "画面中央是一座巨大的「数据矿场」：一台机械臂正在从无边的书本堆与传感器阵列中采集金色数据颗粒，数据颗粒汇聚成发光的数据河流，"
    "象征具身智能数据「平台型供给」成为新基础设施、AI公司批量收购2022年前旧书作为纯净训练语料、数据成为AI产业的新稀缺资源；"
    "画面左侧是一座巨大的时钟与天平：天平一端是正在上涨的价格标签（标注峰谷曲线），另一端是排成一列的模型徽标（GLM、Qwen、DeepSeek），"
    "象征中国大模型从「谁更便宜」转向「谁更不可替代」、峰谷定价成为新定价范式；"
    "画面右侧是两枚正在熔接的芯片与苹果形轮廓，象征苹果与阿里联合训练中国专属大模型、苹果成为首家在华提供自有AI模型的外国科技公司；"
    "背景是深蓝紫渐变夜空与城市数据光点，硬朗的电影感打光，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0817.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

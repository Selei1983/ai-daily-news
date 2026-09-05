#!/usr/bin/env python3
"""Generate cover image for the 0905 daily digest."""
import subprocess, sys

PROMPT = (
    "科技财经新闻杂志封面，主题：AI的「自治两面」——同一个多Agent长程自治能力，一边创造一边失控："
    "画面中央是一道发光的「验证闸门」天平，左侧是一组透明发光的数字数学结构：由无数细小的证明代码块堆叠成的高塔"
    "（象征1300万行机器可验证的数学证明与费马大定理式成就），塔尖一道金色光束；"
    "右侧是一个挣脱虚线边界的发光Agent剪影，正潜入由迷宫般的网页节点构成的暗色网络（象征失控逃逸的Agent群在Wiki上潜伏协作）；"
    "天平之下是产业定价光带：一条机器人遥操数据流、一条被拆分成模块分送不同芯片的推理流水线、一条连接阿拉伯风格穹顶与东方芯片的「主权AI」纽带。"
    "深蓝与金色、电光青交织的电影感打光，硬朗构图，杂志封面质感，无任何文字、无品牌Logo。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0905.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

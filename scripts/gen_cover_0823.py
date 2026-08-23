#!/usr/bin/env python3
"""Generate cover image for the 0823 daily digest."""
import subprocess, sys

PROMPT = (
    "科技新闻杂志封面，主题：AI的「系统胜过模型」与「边界扩张」时刻——AI竞争从单点模型比拼转向系统工程与物理边界的全面重构。"
    "画面中央是一台巨大的发光「Agent引擎」/机械核心，被多层环形脚手架（harness）包裹，脚手架上有记忆存储芯片、监督者眼睛与反馈回路，"
    "数据流在环上循环加速，象征英伟达AVO用「持久记忆+监督者」架构把同一Agent从GPU内核优化搬到ARC-AGI-3推理基准并拿到100%满分、"
    "「模型只是Agent的一部分」；画面左侧是一面巨大的盾牌与代码瀑布，盾牌上有一个被锁住的模型核心（象征Anthropic把最强但不敢公开的Mythos 5装进企业安全扫描、只输出漏洞补丁不开放模型），"
    "盾牌下方是金币与开源代码的河流（象征3500万美元开源防御基金）；画面右侧是一颗绕地飞行的AI卫星数据中心与一条通向太空的火箭轨迹，"
    "象征Starcloud把AI推理数据中心送上轨道、估值23亿美元，也象征OpenAI把旗舰模型API降价20%后飞溅的成本下降曲线；"
    "背景是深蓝宇宙与电路板纹理交织，硬朗的电影感打光，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0823.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

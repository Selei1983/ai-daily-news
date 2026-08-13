#!/usr/bin/env python3
"""Generate cover image for the 0813 daily digest."""
import subprocess, sys

PROMPT = (
    "科技新闻杂志封面，主题：AI的「纵深」时刻——算力被金融化、Agent开始有记忆、机器人潜入深海、医疗AI下沉基层。"
    "画面中央是一个巨大的发光GPU芯片，表面流动着金色金融数据流与股票K线图，象征AI算力被华尔街金融化、证券化（按揭买GPU）；"
    "芯片左侧悬浮着一个半透明的发光的记忆数据库立方体，无数记忆光点汇聚成一条长河，象征AI Agent的长期记忆成为新基础设施；"
    "画面下方是深蓝色的深海场景，一台白色深海作业机器人在海底灯光中工作，象征具身智能从陆地走向深海；"
    "右上角隐约可见乡村诊室的剪影与心电监护仪曲线，象征医疗AI下沉到基层；"
    "背景是深蓝紫色渐变，光线硬朗，电影感打光，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0813.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

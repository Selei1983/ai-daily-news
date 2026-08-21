#!/usr/bin/env python3
"""Generate cover image for the 0821 daily digest."""
import subprocess, sys

PROMPT = (
    "科技新闻杂志封面，主题：AI的「算力路由与资本军备」时刻——AI基础设施的每一层都在被重新定价。"
    "画面中央是一个巨大的发光路由器/交换机，多条数据流从路由器流向不同的芯片与模型图标，数据流上标注着跳动的成本曲线与路由箭头，"
    "象征Callosum拿到1亿美元种子轮打造「可编程异构」算力路由平台、把每个AI任务分发给最合适的模型与芯片，也象征Ramp推出自研模型路由器Router；"
    "画面左侧悬浮着一颗低功耗AI芯片，芯片表面泛着幽蓝冷光、周围环绕着发光的电网与插头，象征Velaura AI用1.1亿美元A轮以「每瓦性能2-4倍」解决AI的电力瓶颈、估值破10亿美元；"
    "画面右侧是一座正在燃烧的资本大楼与上升的资本开支曲线，两座大楼（象征阿里与腾讯）之间堆满服务器与算力塔，空中飘落着人民币符号与财务报表，"
    "象征阿里+腾讯单季度AI资本开支超过1000亿元、自由现金流转负的军备竞赛；"
    "背景是深蓝紫渐变夜空与数字瀑布，硬朗的电影感打光，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0821.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

#!/usr/bin/env python3
"""Generate cover image for the 0906 daily digest."""
import subprocess, sys

PROMPT = (
    "科技财经新闻杂志封面，主题：AI行业的「系统战」——单点智能见顶后，行业开始重构规则、供给、生态与成本架构："
    "画面中央上空悬浮一架发光的「规则天平」，一侧托盘是一本正在展开的发光法典书页（象征AI事故披露框架与治理标准），"
    "另一侧托盘是一枚巨大的金色筹码被一双手交出的剪影（象征用控制权换取芯片供给的主权AI重组）；"
    "中景是一座放射状连接的开放式「中央枢纽」车站，无数能力光缆从车站流向眼镜、耳机、手表与屏幕等端点设备（象征办公Agent开放生态）；"
    "远景底部是一排轻盈的机器人剪影正从一座巨大的半透明「训练沙盘」中走出，沙盘化作细小数据流汇入掌心大小的芯片（象征世界模型训练完即退场、部署保持轻量）；"
    "画面边缘流动着网格状表格数据光带。深蓝与金色、电光青交织的电影感打光，硬朗构图，杂志封面质感，无任何文字、无品牌Logo。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0906.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

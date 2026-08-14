#!/usr/bin/env python3
"""Generate cover image for the 0814 daily digest."""
import subprocess, sys

PROMPT = (
    "科技新闻杂志封面，主题：AI的「工程×速度×价格」时刻——Agent框架开源、模型半价、资本重新定价。"
    "画面中央是一个巨大的发光模块化「洞洞板」式框架，无数可插拔的发光模块（芯片、代码块、工具卡）像积木一样插在框架上，"
    "象征DeepSeek Harness「一切皆插件」的Agent工程框架正式开源；"
    "框架上方悬浮着一个被划掉原价的半价价格标签（绿光闪烁），象征Gemini 3.7 Flash半价首发掀起的模型价格战；"
    "画面右侧是曼哈顿式摩天楼群与一个巨大的金色「2T」符号，象征Anthropic被投资人喊出2万亿美元IPO估值、AI资产被重新定价；"
    "画面左下角，一个被拆开的蓝色盒子正在被两只手重新组装，象征Manus被20亿美元收购后又因监管被回购、腾讯接盘；"
    "无数数据光点从云端下沉汇聚到终端设备，背景是深蓝紫渐变，硬朗的电影感打光，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0814.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

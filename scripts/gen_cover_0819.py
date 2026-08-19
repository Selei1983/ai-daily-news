#!/usr/bin/env python3
"""Generate cover image for the 0819 daily digest."""
import subprocess, sys

PROMPT = (
    "科技新闻杂志封面，主题：AI的「平价革命与入口合流」——硬件价格坍塌、推理芯片重估、Agent打通所有办公入口。"
    "画面中央是一只精致的银色机械灵巧手（仿人手五指的机器人手），指尖捏着一张红色降价标签，标签上的价格从「5万」一路滑落到「1万」以下，"
    "标签下方是一串上扬的销量曲线，象征灵巧手从5万元降到万元以内、销量与融资同时暴涨；"
    "画面左侧悬浮着一块发出冷蓝色光芒的AI推理芯片，芯片表面浮现细密的电路与低电压光纹，芯片后方是一根上扬的金融K线图与交易行情数字，"
    "象征Etched低电压推理芯片估值翻倍至210亿美元、量化交易巨头成为首个客户；"
    "画面右侧是一个巨大的半透明对话框，对话框内依次浮现三座办公大楼的剪影与协作图标，对话框下方是一道声波曲线，"
    "象征千问办公打通钉钉、飞书、企业微信三大办公平台、语音成为下一个交互界面；"
    "背景是深蓝紫渐变夜空与城市数据光点，硬朗的电影感打光，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0819.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

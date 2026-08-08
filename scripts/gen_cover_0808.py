#!/usr/bin/env python3
"""Generate cover image for the 0808 daily digest."""
import subprocess, sys

PROMPT = (
    "科技新闻杂志封面，主题：AI Agent能力的临界点。"
    "画面中央是一台悬浮在半空中的先进AI芯片，芯片表面一道发光的红色警戒线正在亮起，"
    "警戒线前有一道半透明的能量闸门正在关闭，象征暂停与安全闸；"
    "芯片周围环绕着无数金色数据流与小型机器人剪影，象征Agent经济的加速狂奔。"
    "背景是深空蓝与紫的科技感环境，左侧冷蓝光线代表能力扩张，右侧暖橙光线代表资本涌入，"
    "构图大气，电影感打光，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.openclaw/skills/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0808.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

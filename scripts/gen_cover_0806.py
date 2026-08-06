#!/usr/bin/env python3
"""Generate cover image for the 0806 daily digest."""
import subprocess, sys, os

PROMPT = (
    "科技新闻杂志封面，主题：AI Agent的成年礼。"
    "画面中央是一个年轻的半透明发光机器人，正站在巨型屏幕前自主编写代码，"
    "发光的代码瀑布从屏幕倾泻而下；机器人身后是一面巨大的玻璃观察窗，"
    "窗外有佩戴徽章的人类安全员在监控它，象征治理与风险。"
    "背景是未来主义的数据中心，深蓝与紫色主色调，金色光线勾勒机器人轮廓，"
    "构图大气，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0806.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "cover"]
print("Running:", " ".join(cmd[:4]) + " ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

#!/usr/bin/env python3
"""Generate cover image for the 0812 daily digest."""
import subprocess, sys

PROMPT = (
    "科技新闻杂志封面，主题：AI的「感知」时刻——智能开始长出触觉与身体，下沉到物理世界。"
    "画面中央是一只灵巧的白色机械手，指尖泛起橙红色的触觉传感波纹与光点网络，象征触觉感知成为机器人的新感官；"
    "机械手前方悬浮着一个半透明蓝色全息地球，数字与物理两个世界的轮廓交织，象征横跨数字与物理世界的下一代智能体；"
    "左侧是一位华人青年科学家的剪影，面前悬浮着代码与模型架构图，象征大模型人才出走创业潮；"
    "右侧有一块发光的「黑匣子」记录仪，表面流动着Agent行动日志数据流，象征AI智能体事故追踪机制；"
    "背景是深蓝紫色的实验室与城市夜景，光线硬朗，电影感打光，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0812.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

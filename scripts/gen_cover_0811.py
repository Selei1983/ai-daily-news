#!/usr/bin/env python3
"""Generate cover image for the 0811 daily digest."""
import subprocess, sys

PROMPT = (
    "科技新闻杂志封面，主题：AI的「个人化」时刻——智能离开云端，下沉到个人设备与真实世界。"
    "画面中央是一台发光的笔记本电脑，屏幕上浮现一个半透明蓝色光球形态的个人AI Agent，正在替主人执行任务，"
    "光球延伸出数字触手伸向一台小型家用机器人，象征Agent开始替人动手做事；"
    "左侧一位工程师佩戴轻量头戴式采集设备，头环上方悬浮着全景视觉与人体骨骼线条数据流，象征「作业即采集」的具身数据新范式；"
    "右侧一台白色机械臂正在用触觉传感器轻柔抓取物体，指尖泛起触觉波纹，象征不依赖海量数据的「本能驱动」机器人；"
    "背景是深蓝紫色的城市夜空与实验室剪影，光线硬朗，电影感打光，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0811.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

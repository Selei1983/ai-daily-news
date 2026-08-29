#!/usr/bin/env python3
"""Generate cover image for the 0829 daily digest."""
import subprocess, sys

PROMPT = (
    "科技新闻杂志封面，主题：AI的「接管物理世界」时刻——Anthropic发布模型硬件标准MHS让AI Agent直接操控机械臂与精密仪器、特危化工业机器人批量落地、具身世界模型基础设施兴起、物理AI资本化加速。"
    "画面中央是一个巨大的发光机械臂，正与显微镜、实验仪器、工厂设备等多种硬件相连，象征「物理世界的MCP」——AI无需固定身体，可以临时调用任意硬件（分布式具身）；"
    "机械臂上方悬浮着一个抽象的半透明大脑与神经网络光球，从大脑延伸出无数条光线连接到周围的各种设备：摄像头、机械臂、显微镜、旋转的工业阀门；"
    "左侧是一台防爆工业巡检机器人（履带式、带防爆认证标识）在油气田与化工厂场景中执行任务，背景有输油管道与储罐，象征特危化工业场景的机器人落地与中石油订单；"
    "右侧是抽象的三维世界模型网格与手-物交互数据流、触觉反馈光点，象征具身世界模型基础设施与Real-to-Sim-to-Real训练管线；"
    "前景底部是一条陡峭上升的金色资金曲线，点缀美元符号与投资徽章，象征物理AI的资本化浪潮与百亿美元基金；"
    "深蓝与金色交织的电影感打光，硬朗构图，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0829.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

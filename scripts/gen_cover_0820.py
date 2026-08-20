#!/usr/bin/env python3
"""Generate cover image for the 0820 daily digest."""
import subprocess, sys

PROMPT = (
    "科技新闻杂志封面，主题：AI的「操作系统化」时刻——AI开始接管行业软件、绑定硬件供应链、走进真实世界接订单。"
    "画面中央是一本翻开的总账本，账本页面化为发光的数据界面，数据流上升起一座财务大厦的轮廓与上升的营收曲线，"
    "象征AI原生财务软件Rillet把企业总账变成财务的「操作系统」、两年做到10亿美元估值、ARR三个月翻倍；"
    "画面左侧悬浮着一块银蓝色的AI推理芯片，芯片表面浮现细密电路与冷光纹路，芯片后方是一根暴涨的估值曲线与芯片采购订单图标，"
    "象征Fractile拿到Anthropic约2.5亿美元芯片订单后估值三个月从10亿冲到65亿美元；"
    "画面右侧是一台正在打乒乓球的双足人形机器人，挥拍动作流畅、乒乓球在空中划出光轨，机器人脚下散落着合同文件与工厂剪影，"
    "象征2026世界机器人大会从「秀肌肉」转向「接订单」、机器人产业营收突破3000亿元；"
    "背景是深蓝紫渐变夜空与代码数据瀑布，硬朗的电影感打光，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0820.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

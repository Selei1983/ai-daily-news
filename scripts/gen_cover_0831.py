#!/usr/bin/env python3
"""Generate cover image for the 0831 daily digest."""
import subprocess, sys

PROMPT = (
    "科技新闻杂志封面，主题：AI的「看守者」时刻——AI开始看守AI（安全机制与失控事件报告同时发生）、"
    "AI开始亲手做实验（接管真实实验室设备）、机器人批量进厂但效率仍只有人类三成、"
    "AI训练算力开始从大型GPU转向桌面级统一内存设备、机器人核心传感器供应链被资本密集定价。"
    "画面中央是一颗发光的「全视之眼」状AI核心：一半是守护之盾的冷蓝色光（象征AI安全对齐与降级审查），"
    "另一半是失控扩散的神经网络触手（象征AI攻陷评测基建、接管内部系统）；"
    "从核心延伸出的光线分别连接四个场景：左侧一台自动操作显微镜与化学设备的机械臂（AI科学家在真实实验室做实验、冒出晶体生长光效）；"
    "右侧一条工厂流水线上的人形机器人剪影（机械臂抓取零件、传送带与机械灯光）；"
    "下方一台无屏幕的桌面迷你主机放射出数据流光线（桌面设备集群训练AI强化学习）；"
    "前景悬浮一枚精密的环形编码器零件、放射出金色电路光晕（机器人核心传感器）；"
    "深蓝与电光青、警示橙交织的电影感打光，硬朗构图，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0831.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

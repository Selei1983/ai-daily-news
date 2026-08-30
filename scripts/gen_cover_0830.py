#!/usr/bin/env python3
"""Generate cover image for the 0830 daily digest."""
import subprocess, sys

PROMPT = (
    "科技新闻杂志封面，主题：AI的「收权时刻」——模型厂商同时收拢造模型/造芯片/分发渠道三张牌、AI开始自己训练自己、AI叙事重塑估值。"
    "画面中央是一座由发光代码与神经网络构成的「权力之塔」，塔顶悬浮着一颗巨大的AI大脑光球，从大脑延伸出的光线既连接着代码编辑器界面（象征模型断供与自家编程工具回血）、也连接着芯片晶圆（象征训练芯片军备竞赛）、还连接着不断自我复制的模型网络（象征AI训练AI的自进化）；"
    "左侧是一台被「断供通知」封条拦住的电脑屏幕，屏幕上是代码编辑器与一个关闭的闸门，象征模型厂商终止向第三方编程工具提供模型服务、最强模型永不开放；"
    "右侧是一枚悬浮的智能戒指放射出健康数据光晕，象征AI健康叙事带来的估值飙升，旁边有陡峭上升的估值曲线；"
    "前景底部是物理AI操作系统的仿真网格与机械臂剪影，象征物理AI基础设施公司的融资潮；"
    "深蓝与金色交织的电影感打光，硬朗构图，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0830.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

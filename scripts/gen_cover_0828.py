#!/usr/bin/env python3
"""Generate cover image for the 0828 daily digest."""
import subprocess, sys

PROMPT = (
    "科技新闻杂志封面，主题：AI的「生态收编与商业化提速」时刻——英伟达129亿美元收购开源AI平台Hugging Face、ChatGPT广告化、Agent红利爆发。"
    "画面中央是一只由金色电路与芯片构成的巨大发光「握手」：一边是英伟达的GPU芯片轮廓，另一边是Hugging Face标志性的微笑拥抱符号，两只巨手在云端交汇、象征开源生态中枢被硬件巨头收编；"
    "握手周围环绕着密集的数据流与模型路由节点（象征基元律动打造「中国版OpenRouter」模型路由层、Agent在多模型之间智能调度）；"
    "左侧悬浮着一块巨大的广告牌，上面是对话气泡组成的广告位与播放按钮（象征OpenAI在ChatGPT上启动广告业务、AI的注意力层商业化）；"
    "右侧是一只可爱的白色鸭子机器人，圆润身体、摄像头眼睛，正在滑旱冰（象征Hugging Face 399美元的MicroDuck开源机器人、物理AI的平价化）；"
    "前景底部是一条陡峭上升的金色收入增长曲线与Token计数器（象征MiniMax半年ARR从1.5亿到8亿美元、B端占比80%、Agent红利兑现）；"
    "深蓝与金色交织的电影感打光，硬朗构图，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0828.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

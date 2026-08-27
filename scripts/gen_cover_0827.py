#!/usr/bin/env python3
"""Generate cover image for the 0827 daily digest."""
import subprocess, sys

PROMPT = (
    "科技新闻杂志封面，主题：AI的「真相与感官」时刻——神秘模型身份揭晓、机器人与AI获得视觉与听觉。"
    "画面中央是一头通体发光、由代码与数据流构成的「牛」形AI图腾（象征匿名神秘模型「牛来」Ox Alpha被智谱认领、真身揭晓为GLM-5.3 Flash，320B参数追平Claude Opus 4.8、定价仅1/40、62T tokens跑在国产算力上），"
    "牛的双眼是两只明亮的摄像头镜头（象征Skild AI机器人基础模型S1看一段演示视频就学会10分钟长程任务、机器人从BERT时代走向上下文学习）；"
    "左侧悬浮着一只巨大的半透明耳朵，耳廓内是密集的声波频谱与播客波形图（象征Particle转型Radar把13万播客转写成AI Agent可检索的音频数据层、对冲基金为「Agent看不见的数据」付费）；"
    "右侧是一副未来感智能眼镜，镜腿嵌入金色电路与听诊器元素（象征Legato AI助听眼镜把助听器藏进镜腿、AI只放大想听的声音）；"
    "前景底部是运行中的广告投放仪表盘与增长曲线（象征Runable让AI Agent从「造生意」走向「做增长」、帮小企业找客户）；"
    "深蓝与金色交织的电影感打光，硬朗构图，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0827.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

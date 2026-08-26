#!/usr/bin/env python3
"""Generate cover image for the 0826 daily digest."""
import subprocess, sys

PROMPT = (
    "科技新闻杂志封面，主题：AI的「地基与记忆」时刻——模型厂商自建芯片与检索地基、Agent的记忆成为产品。"
    "画面中央是一颗发光的辣椒形状AI芯片（象征OpenAI自研推理芯片Jalapeño「小辣椒」，700W功耗在SemiAnalysis推理基准上碾压英伟达Blackwell），"
    "辣椒芯片表面电路化为金色数据流，插在一座由搜索引擎索引柱与数据节点构成的发光地基上（象征Keenable为AI Agent重建千亿文档级Web索引、挑战谷歌）；"
    "右侧一台银白色人形机器人手臂正观看一段短视频演示后做出新动作（象征Generalist机器人大脑以30亿美元估值融资、看3-12秒示范即学会任务、机器人的ChatGPT时刻）；"
    "背景悬浮着金色音乐音符、胶片与游戏手柄元素（象征Stability AI获得环球/索尼/华纳/EA等娱乐巨头7600万美元B轮投资、版权方入股模型厂）；"
    "前景是一颗半透明的记忆水晶球，球内漂浮着可读可编辑的对话气泡与笔记本（象征Claude Cowork记忆统一、记忆可查看可管理）；"
    "深蓝与金色交织的电影感打光，硬朗构图，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0826.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

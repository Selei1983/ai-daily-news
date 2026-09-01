#!/usr/bin/env python3
"""Generate cover image for the 0901 daily digest."""
import subprocess, sys

PROMPT = (
    "科技财经新闻杂志封面，主题：AI的「利润分配权」时刻——大模型商业化的账本正在被重新分配："
    "开源模型开始向云平台收取「模型版税」分成、AI对话产品开始用广告变现、推理利润率大幅提升、"
    "云厂商从模型公司的每100美元收入中拿走35-40美元。"
    "画面中央是一台发光的金色「结算天平」与摊开的数字账本：天平一端堆着代表模型授权的金色芯片与代码方块，"
    "另一端堆着代表云算力的银色服务器机架，两端的金币与数据流在空中交汇对撞、溅出火星；"
    "账本页面上悬浮着发光的百分比符号与分成箭头；"
    "背景左侧是一座巨大的云端数据中心剪影（霓虹蓝光），右侧是一块AI对话界面里弹出的广告卡片光效（暖橙色）；"
    "深蓝与金色、电光青交织的电影感打光，硬朗构图，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0901.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

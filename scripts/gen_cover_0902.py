#!/usr/bin/env python3
"""Generate cover image for the 0902 daily digest."""
import subprocess, sys

PROMPT = (
    "科技财经新闻杂志封面，主题：AI的「重资产化」时刻——AI行业正在从轻资产软件故事变成重资产基础设施游戏："
    "模型公司一周签下800亿美元算力租约（金库般的巨型数据中心）、开始自研推理芯片（电路与芯片蓝图）、"
    "AI长剧登上卫视黄金档（摄影棚里没有真人演员只有服务器阵列）、3D基座模型被产业资本密集定价。"
    "画面中央是一座正在浇筑的「AI重资产大厦」：地基由成排的GPU服务器机架与数据中心机柜浇筑而成，"
    "大厦主体是半透明的数字结构，内部可见发光的芯片电路、跳动的算力数据流与正在生成的3D模型线框；"
    "大厦一侧延伸出巨大的算力租约合同卷轴（金色印章），另一侧是放映AI长剧的巨幕（霓虹光）；"
    "工人们（剪影）正在把一块块GPU芯片砌进大厦墙体；"
    "深蓝与金色、电光青交织的电影感打光，硬朗构图，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0902.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

#!/usr/bin/env python3
"""Generate cover image for the 0818 daily digest."""
import subprocess, sys

PROMPT = (
    "科技新闻杂志封面，主题：AI的「落地兑现」时刻——人形机器人进入资本市场定价、AI开始直接收钱、智能终端迈入物理世界。"
    "画面中央是一座巨大的「上市钟塔」：钟塔顶端立着一台银白色人形机器人，正在敲响一尊金色上市铜钟，钟声化作金色的数字瀑布与K线图，"
    "象征宇树科技「人形机器人第一股」登陆科创板、A股首次给人形机器人定价（市盈率219倍、中签率万分之1.8）；"
    "钟塔左侧是一只巨大的购物车形状的聊天窗口：一个AI对话气泡正在扫码结账，吐出信用卡与收银小票，"
    "象征ChatGPT与信用卡公司合作变成「AI购物车」、代理式电商（Agentic Commerce）开始兑现；"
    "钟塔右侧是一部悬浮的手机，手机顶部伸出一只精巧的机械云台镜头，镜头前方飘着电影感的光斑，"
    "象征荣耀Robot Phone首销、AI终端从「数字智能」迈向「具身智能」；"
    "背景是深蓝紫渐变夜空与城市数据光点，硬朗的电影感打光，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0818.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

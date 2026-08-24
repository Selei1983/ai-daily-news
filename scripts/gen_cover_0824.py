#!/usr/bin/env python3
"""Generate cover image for the 0824 daily digest."""
import subprocess, sys

PROMPT = (
    "科技新闻杂志封面，主题：AI的「入口与账本」时刻——AI产业从「谁的模型强」转向「谁的账本健康、谁的入口便宜」。"
    "画面中央是一头神秘的发光「牛」（牛头抽象机械体，象征匿名模型Ox Alpha「牛来」），站在一本巨大的发光账本天平上，"
    "账本左侧是陡峭上升的红色成本曲线与发光存储芯片（HBM内存颗粒，象征英伟达AI服务器涨价15%、「存储定义算力」），"
    "右侧是金色资本洪流与硬币（象征阿里巴巴800亿港元港股配售、主权基金超额认购、AI军备竞赛资本化）；"
    "牛身后悬浮着一面数字镜像（象征Twin1「数字分身」成为企业AI新界面），前景是一台88厘米高的小型家庭人形机器人"
    "（象征上纬新材启元Q1开启预订、个人机器人叩开家庭消费大门），背景是云雾与问号（匿名模型身份之谜）；"
    "深蓝与金色交织的电影感打光，硬朗构图，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0824.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

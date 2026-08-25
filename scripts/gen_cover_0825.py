#!/usr/bin/env python3
"""Generate cover image for the 0825 daily digest."""
import subprocess, sys

PROMPT = (
    "科技新闻杂志封面，主题：AI的「卖铲人买矿」时刻——英伟达从卖算力到买应用与模型，AI价值重心从基础设施下沉到应用层。"
    "画面中央是一把巨大的发光金色铲子（卖铲人意象）深深插入一座由GPU芯片与数据流构成的矿山（象征英伟达算力帝国），"
    "铲柄上缠绕着美元符号与股权结构图（象征英伟达以300亿美元估值投资Perplexity、60亿美元购买Poolside模型授权）；"
    "矿山旁是一台银白色金属质感的高自由度人形机器人IRON（76个关节、双手灵巧，象征小鹏机器人9亿美元A轮、具身智能量产资本化），"
    "机器人手中托着一块发光的代码界面与规格文档（象征OpenAI GPT-5.6进驻AWS编码Agent Kiro、spec-driven开发）；"
    "背景右侧悬浮着一部手机与一把打开的锁（象征Instinct全能个人助理的权限与信任争议），"
    "前景是一叠法律文书与数据流汇入一个发光的编排层管道（象征Newcode法律AI编排层）；"
    "深蓝与金色交织的电影感打光，硬朗构图，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0825.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

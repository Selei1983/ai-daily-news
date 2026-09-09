#!/usr/bin/env python3
"""Generate the 0909 daily digest cover image (doubao, 2560x1440 article size)."""
import subprocess, sys
from pathlib import Path

TOOLKIT = Path.home() / ".hermes/skills/openclaw-imports/wewrite/toolkit"
OUT = Path.home() / ".hermes/workspace/ai-daily-news/daily/images/cover-0909.png"

PROMPT = (
    "科技产品插画封面，主题「信任与验证」。画面中央：一台发光的个人AI助理设备（悬浮的全息界面显示邮件、日历、支付卡片与购物车图标，"
    "象征Agent开始接管邮箱与钱包），它前方悬浮着一座巨大的半透明天秤——左端托盘上是发光的钥匙与盾牌（信任与安全），"
    "右端托盘上是暗红色锁链缠绕的二进制代码与漏洞符号（风险与攻击），天秤指针指向一本翻开的巨型「审计账本」，"
    "账本页面中浮现出微缩的DNA双螺旋数据流（基因变异全图谱）与机器人仿真测试场（虚拟世界里的机械臂在跑测试），"
    "暗示验证层正在成为新的基础设施；背景左侧是明亮的客厅与手机界面（消费级Agent的日常），"
    "右侧是幽暗机房中蔓延的红色数据流（攻击者Agent在无人值守地作业）；整体深蓝紫色科技色调配青绿色高光与橙红色警示点缀，"
    "扁平化与写实结合，构图饱满，高清渲染，画面内无文字。"
)

cmd = [sys.executable, "image_gen.py", "--prompt", PROMPT, "--output", str(OUT), "--size", "article"]
print("Running:", " ".join(cmd))
r = subprocess.run(cmd, cwd=str(TOOLKIT), capture_output=True, text=True, timeout=420)
print(r.stdout[-3000:])
if r.returncode != 0:
    print("STDERR:", r.stderr[-2000:])
    sys.exit(r.returncode)
print("Cover written:", OUT, OUT.exists())

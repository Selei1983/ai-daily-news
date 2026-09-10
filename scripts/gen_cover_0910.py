#!/usr/bin/env python3
"""Generate the 0910 daily digest cover image (doubao, 2560x1440 article size)."""
import subprocess, sys
from pathlib import Path

TOOLKIT = Path.home() / ".hermes/skills/openclaw-imports/wewrite/toolkit"
OUT = Path.home() / ".hermes/workspace/ai-daily-news/daily/images/cover-0910.png"

PROMPT = (
    "科技产品插画封面，主题「单位智能成本与算力账单」。画面中央：一座由发光数据流构成的巨大「算力秤/账本」，"
    "左端托盘是密集的GPU服务器阵列与冷却水冷的发光管道（象征算力供给墙与散热），右端托盘是一枚小巧却发亮的芯片与手机（象征端侧推理与成本下压），"
    "秤杆下方翻开一本巨大的「成本账本」，页面上浮现蠕动的数字曲线与价格标签、账单明细；"
    "背景左侧是幽暗数据中心里蓝色液冷管道与闪烁的金刚石散热片（散热技术），右侧是一条向下俯冲的绿色降价箭头与向上飙升的红色需求曲线交汇（供需剪刀差）；"
    "远处是排列成行的发光智能终端设备（象征25亿台设备分发AI），近景有几只抽象的机械手在给一台小型AI代理戴上发光的「权限项圈与锁链」（象征Agent治理与责任边界）；"
    "整体深蓝紫色科技色调配青绿色高光与橙红色警示点缀，扁平化与写实结合，构图饱满，高清渲染，画面内无文字。"
)

cmd = [sys.executable, "image_gen.py", "--prompt", PROMPT, "--output", str(OUT), "--size", "article"]
print("Running:", " ".join(cmd))
r = subprocess.run(cmd, cwd=str(TOOLKIT), capture_output=True, text=True, timeout=420)
print(r.stdout[-3000:])
if r.returncode != 0:
    print("STDERR:", r.stderr[-2000:])
    sys.exit(r.returncode)
print("Cover written:", OUT, OUT.exists())

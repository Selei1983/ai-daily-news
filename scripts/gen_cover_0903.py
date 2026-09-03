#!/usr/bin/env python3
"""Generate cover image for the 0903 daily digest."""
import subprocess, sys

PROMPT = (
    "科技财经新闻杂志封面，主题：AI的「入口争夺战」——AI产业的钱与权正涌向六个「入口收费站」："
    "开源模型分发平台（象征：巨大的模型仓库闸门）、云端模型调用入口（象征：超高速流动的代码与Agent数据流汇成光河）、"
    "资本市场入口（象征：交易所上市钟与K线）、空间与物理世界入口（象征：发光的3D网格世界与机器人）、"
    "AI训练数据入口（象征：无数专家思维链光点汇入数据库）、能源控制入口（象征：电厂与电网在AI调度下节能发光）。"
    "画面中央是一座多车道「超级入口枢纽/未来收费站」：六条发光的道路从不同方向汇聚到中央一道环形光门，"
    "每辆车/数据流通过光门后都变成发光的Token颗粒；闸机上悬浮着发光的开关与钥匙图标，"
    "远景是数据中心、港交所大楼剪影、机器人厂房与发电塔的轮廓交织在地平线上；"
    "深蓝与金色、电光青交织的电影感打光，硬朗构图，杂志封面质感，无任何文字、无品牌Logo。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0903.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

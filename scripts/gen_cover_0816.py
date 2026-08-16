#!/usr/bin/env python3
"""Generate cover image for the 0816 daily digest."""
import subprocess, sys

PROMPT = (
    "科技新闻杂志封面，主题：AI的「并购×开源×算力金融化」时刻——史上最大创业公司收购、开源模型登顶全球、算力金融化的中美双轨。"
    "画面中央是一艘银白色火箭（SpaceX风格）正将一个巨大的发光光标/代码编辑器图标拖入地球轨道，象征SpaceX以600亿美元正式完成对AI编程工具Cursor的收购、"
    "创下史上最大规模创业公司收购纪录，火箭尾部拖出金色轨迹；"
    "画面左侧，无数橙色与金色的开源模型卡片从云端倾泻而下堆成发光山丘，每张卡片上隐约有「Q」形徽标，象征阿里千问Qwen3.8系列开源后全球下载量突破30亿次登顶第一；"
    "画面右侧是一座悬空天平：一端是一份正在收缩断裂的美元担保合同（2500→1200数字若隐若现），另一端是不断叠高的Token硬币与贷款凭证，"
    "象征算力金融化在美国踩下刹车（英伟达缩减2500亿美元担保）、在中国却以「Token贷/算力贷」加速铺开；"
    "背景是深蓝紫渐变夜空与城市数据光点，硬朗的电影感打光，杂志封面质感，无任何文字。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0816.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

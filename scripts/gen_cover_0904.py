#!/usr/bin/env python3
"""Generate cover image for the 0904 daily digest."""
import subprocess, sys

PROMPT = (
    "科技财经新闻杂志封面，主题：AI的「AGI官宣时刻」——AI从「大脑」长出「身体」并开始真正干活："
    "画面中央是一位半透明的未来「数字员工」：发光的机械手正在操作悬浮的全息屏幕与软件界面（象征会自己干活的GPT-6 Astra级Agent），"
    "机械手的另一侧连接着一个正在组装的类人机器人躯干轮廓（象征大模型公司自研人形机器人）；"
    "周围环绕四条产业定价光带：一条通向巨大的电商平台橱窗（货架上摆着发光的Token硬币，象征Token渠道化零售），"
    "一条通向发光的网络安全闸门（象征AI进入真实世界的「控制层」），"
    "一条通向由电路与电网构成的数据中心天际线（象征AI基建的巨额贷款与合同融资），"
    "还有一条是资本市场K线光带。深蓝与金色、电光青交织的电影感打光，硬朗构图，杂志封面质感，无任何文字、无品牌Logo。"
)

TOOLKIT = "/Users/jowe_macmini/.hermes/skills/openclaw-imports/wewrite/toolkit/image_gen.py"
OUT = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images/cover-0904.png"

cmd = [sys.executable, TOOLKIT, "--prompt", PROMPT, "--output", OUT, "--size", "article"]
print("Running cover generation ...")
r = subprocess.run(cmd, capture_output=True, text=True, timeout=280)
print(r.stdout[-3000:] if r.stdout else "")
print(r.stderr[-3000:] if r.stderr else "")
sys.exit(r.returncode)

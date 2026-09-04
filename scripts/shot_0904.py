#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) for the 0904 daily digest."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT_DIR = Path("/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images")

# (primary_url, fallback_url, output_name)
targets = [
    ("https://36kr.com/p/3968299418415362",  # GPT-6 Astra 智东西
     "https://www.36kr.com/p/3968299418415362",
     "0904-astra.png"),
    ("https://36kr.com/p/3967488289183367",  # OpenAI 人形机器人 芯智能头条
     "https://www.36kr.com/p/3967488289183367",
     "0904-openai-robot.png"),
    ("https://36kr.com/p/3967597474869507",  # 智谱天猫开店 三易生活
     "https://www.36kr.com/p/3967597474869507",
     "0904-tmall-token.png"),
    ("https://36kr.com/p/3967576824061441",  # 网安AI红利 硅基观察Pro
     "https://www.36kr.com/p/3967576824061441",
     "0904-cyber.png"),
    ("https://techcrunch.com/2026/09/03/accel-reportedly-in-talks-to-lead-1b-round-for-thinking-machines-at-40b-valuation/",
     "https://techcrunch.com/2026/09/03/accel-reportedly-in-talks-to-lead-1b-round-for-thinking-machines-at-40b-valuation/?utm_source=feed",
     "0904-thinkingmachines.png"),
    ("https://36kr.com/p/3968346621751812",  # 8点1氪 字节贷款
     "https://www.36kr.com/p/3968346621751812",
     "0904-bytedance-loan.png"),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 720}, device_scale_factor=1,
                              user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36")
    for primary, fallback, name in targets:
        out = OUT_DIR / name
        done = False
        for url in (primary, fallback):
            page = ctx.new_page()
            try:
                try:
                    page.goto(url, wait_until="domcontentloaded", timeout=45000)
                    page.wait_for_timeout(7000)
                except Exception as e1:
                    print(f"  domcontentloaded fail {url}: {type(e1).__name__} {str(e1)[:80]}; retry commit+12s")
                    page.goto(url, wait_until="commit", timeout=45000)
                    page.wait_for_timeout(12000)
                text_len = page.evaluate("document.body ? document.body.innerText.length : 0")
                if text_len < 150:
                    print(f"WARN low content ({text_len}) {url}")
                    continue
                page.screenshot(path=str(out), clip={"x": 0, "y": 0, "width": 1280, "height": 720})
                print(f"OK {name} <- {url} (text={text_len})")
                done = True
            except Exception as e:
                print(f"FAIL {url}: {type(e).__name__} {str(e)[:120]}")
            finally:
                page.close()
            if done:
                break
        if not done:
            print(f"BOTH_FAIL {name}")
    browser.close()

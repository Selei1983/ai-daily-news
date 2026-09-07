#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) for the 0907 daily digest."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT_DIR = Path("/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images")

# (primary_url, fallback_url, output_name)
targets = [
    ("https://techcrunch.com/2026/09/06/authors-push-back-as-publishers-and-agents-seek-share-of-anthropic-settlement/",  # TC Anthropic settlement distribution dispute
     "https://www.36kr.com/p/3971524976849160",  # 爱范儿 索尼华纳围剿Anthropic
     "0907-anthropic-settlement.png"),
    ("https://www.36kr.com/p/3971642425372930",  # MIT Grok Bot 造零件 (新智元)
     "https://www.36kr.com/p/3971642425372930",
     "0907-grokbot-mit.png"),
    ("https://www.36kr.com/p/3970578244792582",  # AI投资人盯上B站UP主 (晓曦)
     "https://www.36kr.com/p/3970578244792582",
     "0907-bilibili-ai.png"),
    ("https://techcrunch.com/2026/09/06/travis-kalanicks-atoms-might-be-getting-into-the-robotaxi-business/",  # TC Atoms robotaxi
     "https://siliconangle.com/2026/09/06/former-uber-ceo-travis-kalanick-is-returning-to-the-robotaxi-race/",
     "0907-atoms-robotaxi.png"),
    ("https://www.36kr.com/p/3971642393686535",  # 果蝇全脑仿真 (新智元)
     "https://www.36kr.com/p/3971642393686535",
     "0907-fruitfly.png"),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 720}, device_scale_factor=1,
                              user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36",
                              locale="zh-CN")
    for primary, fallback, name in targets:
        out = OUT_DIR / name
        done = False
        for url in (primary, fallback):
            page = ctx.new_page()
            try:
                try:
                    page.goto(url, wait_until="domcontentloaded", timeout=45000)
                    page.wait_for_timeout(8000)
                except Exception as e1:
                    print(f"  domcontentloaded fail {url}: {type(e1).__name__} {str(e1)[:80]}; retry commit+12s")
                    page.goto(url, wait_until="commit", timeout=45000)
                    page.wait_for_timeout(12000)
                text_len = page.evaluate("document.body ? document.body.innerText.length : 0")
                if text_len < 120:
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

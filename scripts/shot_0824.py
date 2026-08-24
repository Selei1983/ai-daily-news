#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) for the 0824 daily digest."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT_DIR = Path("/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images")

# (primary_url, fallback_url, output_name)
targets = [
    ("https://openrouter.ai/stealth/ox-alpha",
     "https://www.qbitai.com/2026/08/478191.html",
     "0824-oxalpha.png"),
    ("https://twin1.ai",
     "https://techstartups.com/2026/08/20/twin1-ai-emerges-from-stealth-with-20m-in-funding-to-give-every-professional-an-ai-powered-digital-twin/",
     "0824-twin1.png"),
    ("https://www.jfdaily.com/news/detail?id=1164628",
     "https://www.jiemian.com/article/14970490.html",
     "0824-qiyuan.png"),
    ("https://www.cls.cn/detail/2461729",
     "https://www.reuters.com/business/retail-consumer/alibaba-proposes-hong-kong-share-placement-worth-10-billion-2026-08-23/",
     "0824-alibaba.png"),
    ("https://www.qbitai.com/2026/08/478164.html",
     "https://finance.sina.com.cn/stock/t/2026-08-23/doc-iniphhay2625440.shtml",
     "0824-nvidia.png"),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 720}, device_scale_factor=1)
    for primary, fallback, name in targets:
        out = OUT_DIR / name
        done = False
        for url in (primary, fallback):
            page = ctx.new_page()
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=45000)
                page.wait_for_timeout(6000)
                page.screenshot(path=str(out), clip={"x": 0, "y": 0, "width": 1280, "height": 720})
                print(f"OK {name} <- {url}")
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

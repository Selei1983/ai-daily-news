#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) for the 0830 daily digest."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT_DIR = Path("/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images")

# (primary_url, fallback_url, output_name)
targets = [
    ("https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/",
     "https://36kr.com/p/3960079349054855",
     "0830-openai-cursor.png"),
    ("https://www.qbitai.com/2026/08/480940.html",
     "https://qoder.com/",
     "0830-qoder.png"),
    ("https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures",
     "https://36kr.com/p/3960005089770887",
     "0830-anthropic-aar.png"),
    ("https://36kr.com/p/3960108652297353",
     "https://www.reuters.com/business/finance/anthropic-planned-then-abandoned-7-billion-purchase-matx-sources-say-2026-08-27/",
     "0830-anthropic-matx.png"),
    ("https://36kr.com/p/3960323709894016",
     "https://ouraring.com/",
     "0830-oura-ipo.png"),
    ("https://news.pedaily.cn/202608/568254.shtml",
     "https://www.pedaily.cn/",
     "0830-songying.png"),
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

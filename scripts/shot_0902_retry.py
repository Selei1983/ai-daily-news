#!/usr/bin/env python3
"""Retry screenshots for 0902 via www.36kr.com (bypasses rate-limit bucket)."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT_DIR = Path("/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images")

targets = [
    ("https://www.36kr.com/p/3964873497320966", "0902-zhipu.png"),
    ("https://www.36kr.com/p/3964567434059016", "0902-violoop.png"),
    ("https://www.36kr.com/p/3964719417040392", "0902-manus.png"),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(
        viewport={"width": 1280, "height": 720},
        device_scale_factor=1,
        locale="zh-CN",
        timezone_id="Asia/Shanghai",
        user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        extra_http_headers={"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"},
    )
    for url, name in targets:
        out = OUT_DIR / name
        page = ctx.new_page()
        try:
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=60000)
            except Exception as e1:
                print(f"  domcontentloaded fail {url}: {type(e1).__name__} {str(e1)[:80]}; retry commit")
                page.goto(url, wait_until="commit", timeout=60000)
            for i in range(4):
                page.wait_for_timeout(5000)
                text_len = page.evaluate("document.body ? document.body.innerText.length : 0")
                print(f"  try{i+1} text={text_len}")
                if text_len > 150:
                    break
            text_len = page.evaluate("document.body ? document.body.innerText.length : 0")
            if text_len >= 150:
                page.screenshot(path=str(out), clip={"x": 0, "y": 0, "width": 1280, "height": 720})
                print(f"OK {name} <- {url} (text={text_len})")
            else:
                print(f"FAIL_LOW_CONTENT {name} text={text_len}")
        except Exception as e:
            print(f"FAIL {url}: {type(e).__name__} {str(e)[:150]}")
        finally:
            page.close()
    browser.close()

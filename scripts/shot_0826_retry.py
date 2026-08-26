#!/usr/bin/env python3
"""Retry screenshots for pages that timed out (0826)."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT_DIR = Path("/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images")

targets = [
    ("https://techcrunch.com/2026/08/25/robotics-startup-generalist-reaches-3b-valuation-sources-say/",
     "0826-generalist.png"),
    ("https://techcrunch.com/2026/08/25/claude-cowork-finally-remembers-what-you-told-the-app-in-chat/",
     "0826-claude-memory.png"),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 720}, device_scale_factor=1,
                              user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36")
    for url, name in targets:
        page = ctx.new_page()
        try:
            page.goto(url, wait_until="commit", timeout=60000)
            page.wait_for_timeout(12000)
            text_len = page.evaluate("document.body ? document.body.innerText.length : 0")
            title = page.title()
            print(f"{name}: text={text_len} title={title[:80]}")
            if text_len > 150:
                page.screenshot(path=str(OUT_DIR / name), clip={"x": 0, "y": 0, "width": 1280, "height": 720})
                print(f"OK {name}")
            else:
                print(f"LOW {name}")
        except Exception as e:
            print(f"FAIL {name}: {type(e).__name__} {str(e)[:150]}")
        finally:
            page.close()
    browser.close()

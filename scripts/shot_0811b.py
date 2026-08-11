#!/usr/bin/env python3
"""Retry screenshots for failed URLs."""
from playwright.sync_api import sync_playwright

urls = [
    ("https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model", "/tmp/0811-glimmer-raw.png"),
    ("https://www.abc.net.au/news/2026-08-10/ai-assistant-hacks-gym-website-aus-cyber-attack/107007986", "/tmp/0811-gymhack-raw.png"),
    ("https://news.pedaily.cn/202608/567473.shtml", "/tmp/0811-acorn2-raw.png"),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 720}, device_scale_factor=1,
                              user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36")
    for url, out in urls:
        page = ctx.new_page()
        try:
            page.goto(url, wait_until="commit", timeout=60000)
            page.wait_for_timeout(8000)
            page.screenshot(path=out, clip={"x": 0, "y": 0, "width": 1280, "height": 720})
            print(f"OK {out}")
        except Exception as e:
            print(f"FAIL {url}: {e}")
        finally:
            page.close()
    browser.close()

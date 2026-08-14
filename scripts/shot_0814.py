#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) of today's 5 digest URLs using local Playwright."""
from playwright.sync_api import sync_playwright

urls = [
    ("https://tech.ifeng.com/c/8vYGCajr2EJ", "/tmp/0814-gemini-raw.png"),
    ("https://news.pedaily.cn/202608/567675.shtml", "/tmp/0814-harness-raw.png"),
    ("https://news.pedaily.cn/202608/567689.shtml", "/tmp/0814-lightorigins-raw.png"),
    ("https://tech.ifeng.com/c/8vZj0SOdaWO", "/tmp/0814-manus-raw.png"),
    ("https://tech.ifeng.com/c/8vYGCajr2EQ", "/tmp/0814-anthropic-raw.png"),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 720}, device_scale_factor=1,
                              user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36")
    for url, out in urls:
        page = ctx.new_page()
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(8000)
            page.screenshot(path=out, clip={"x": 0, "y": 0, "width": 1280, "height": 720})
            print(f"OK {out}")
        except Exception as e:
            print(f"FAIL {url}: {e}")
        finally:
            page.close()
    browser.close()

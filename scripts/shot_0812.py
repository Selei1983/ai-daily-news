#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) of today's 5 digest URLs using local Playwright."""
from playwright.sync_api import sync_playwright

urls = [
    ("https://www.bjnews.com.cn/detail/1786420754129093.html", "/tmp/0812-latentverse-raw.png"),
    ("https://finance.sina.cn/tech/2026-08-12/detail-inimzivu5384770.d.html", "/tmp/0812-pragmatik-raw.png"),
    ("https://www.qbitai.com/2026/08/470674.html", "/tmp/0812-daimon-raw.png"),
    ("https://finance.sina.com.cn/jjxw/2026-08-11/doc-inimxrni0743693.shtml", "/tmp/0812-dyna-raw.png"),
    ("https://www.ithome.com/0/988/612.htm", "/tmp/0812-safeframe-raw.png"),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 720}, device_scale_factor=1)
    for url, out in urls:
        page = ctx.new_page()
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(6000)
            page.screenshot(path=out, clip={"x": 0, "y": 0, "width": 1280, "height": 720})
            print(f"OK {out}")
        except Exception as e:
            print(f"FAIL {url}: {e}")
        finally:
            page.close()
    browser.close()

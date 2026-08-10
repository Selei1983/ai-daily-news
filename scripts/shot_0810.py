#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) of given URLs using local Playwright."""
from playwright.sync_api import sync_playwright

urls = [
    ("https://www.moxing.ai/", "/tmp/0810-moxing-raw.png"),
    ("https://www.knowin.ai/", "/tmp/0810-knowin-raw.png"),
    ("https://unitree.com/", "/tmp/0810-unitree-raw.png"),
    ("https://9to5mac.com/2026/08/06/report-shares-new-pricing-and-design-details-about-openais-first-device/", "/tmp/0810-openai00-raw.png"),
    ("https://www.rippling.com/platform/ai/ai-spend-console", "/tmp/0810-rippling-raw.png"),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 720}, device_scale_factor=1)
    for url, out in urls:
        page = ctx.new_page()
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(5000)
            page.screenshot(path=out, clip={"x": 0, "y": 0, "width": 1280, "height": 720})
            print(f"OK {out}")
        except Exception as e:
            print(f"FAIL {url}: {e}")
        finally:
            page.close()
    browser.close()

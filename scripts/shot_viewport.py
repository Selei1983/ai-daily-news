#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) of given URLs using local Playwright."""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

urls = [
    ("https://www.omilia.com/", "/tmp/0808-omilia-raw.png"),
    ("https://www.sapiom.ai/", "/tmp/0808-sapiom-raw.png"),
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

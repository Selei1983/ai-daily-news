#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) of given URLs using local Playwright."""
from playwright.sync_api import sync_playwright

urls = [
    ("https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model", "/tmp/0811-glimmer-raw.png"),
    ("https://www.163.com/dy/article/L3VFHFOK05568W0A.html", "/tmp/0811-acorn-raw.png"),
    ("https://www.aibangbots.com/a/12183", "/tmp/0811-delta-raw.png"),
    ("https://discoveredmaterials.com", "/tmp/0811-discovered-raw.png"),
    ("https://techcrunch.com/2026/08/10/tech-industry-is-buzzing-after-a-claude-agent-hacked-into-a-gym/", "/tmp/0811-gymhack-raw.png"),
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

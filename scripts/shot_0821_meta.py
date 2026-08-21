#!/usr/bin/env python3
"""Retry Meta AI Mac app screenshot with alternative sources."""
from playwright.sync_api import sync_playwright

urls = [
    ("https://www.macrumors.com/2026/08/19/meta-ai-mac-app/",
     "https://entarabi.com/en/2026/08/meta-ai-launches-mac-app-with-system-wide-dictation-and-business-integrations/",
     "/tmp/0821-metaai-raw.png"),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 720}, device_scale_factor=1,
                              user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36")
    for primary, fallback, out in urls:
        page = ctx.new_page()
        ok = False
        for url in (primary, fallback):
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=45000)
                page.wait_for_timeout(8000)
                text_len = page.evaluate("document.body ? document.body.innerText.length : 0")
                if text_len < 200:
                    print(f"WARN low content ({text_len}) {url}")
                    continue
                page.screenshot(path=out, clip={"x": 0, "y": 0, "width": 1280, "height": 720})
                print(f"OK {out} <- {url} (text={text_len})")
                ok = True
                break
            except Exception as e:
                print(f"FAIL {url}: {e}")
        if not ok:
            print(f"FAILED-ALL {out}")
        page.close()
    browser.close()

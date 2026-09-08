#!/usr/bin/env python3
"""Retry SA screenshot for 0908 (Pachocki essay)."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT_DIR = Path("/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images")
URL = "https://siliconangle.com/2026/09/07/openai-chief-scientist-argues-for-ai-research-slowdown/"
OUT = OUT_DIR / "0908-pachocki.png"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 720}, device_scale_factor=1,
                              user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36",
                              locale="en-US")
    page = ctx.new_page()
    try:
        try:
            page.goto(URL, wait_until="domcontentloaded", timeout=60000)
        except Exception as e1:
            print("dcl fail", str(e1)[:100])
            page.goto(URL, wait_until="commit", timeout=60000)
        page.wait_for_timeout(15000)
        # disable further font loading to unblock screenshot
        page.evaluate("document.fonts && document.fonts.ready.then(()=>{})")
        text_len = page.evaluate("document.body ? document.body.innerText.length : 0")
        print("text_len", text_len)
        page.screenshot(path=str(OUT), clip={"x": 0, "y": 0, "width": 1280, "height": 720}, timeout=60000)
        print("OK", OUT)
    except Exception as e:
        print("FAIL", type(e).__name__, str(e)[:200])
    finally:
        page.close()
    browser.close()

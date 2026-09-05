#!/usr/bin/env python3
"""Retry SA screenshots with multiple attempts (SA intermittently blocks headless)."""
from pathlib import Path
from playwright.sync_api import sync_playwright
import time

OUT_DIR = Path("/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images")

targets = [
    ("https://siliconangle.com/2026/09/04/anthropic-uses-claude-to-formalize-proof-of-fermats-last-theorem/", "0905-fermat.png"),
    ("https://siliconangle.com/2026/09/04/gimlet-labs-nabs-300m-for-its-disaggregated-inference-platform/", "0905-gimlet.png"),
    ("https://siliconangle.com/2026/09/04/resect-launches-with-25m-to-reduce-hallucinations-in-ai-models/", "0905-resect.png"),
]

UAS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
    for url, name in targets:
        out = OUT_DIR / name
        done = False
        for attempt in range(1, 4):
            if done:
                break
            ua = UAS[attempt % len(UAS)]
            ctx = browser.new_context(viewport={"width": 1280, "height": 720}, device_scale_factor=1,
                                      user_agent=ua, locale="en-US")
            page = ctx.new_page()
            try:
                try:
                    page.goto(url, wait_until="domcontentloaded", timeout=60000)
                except Exception as e1:
                    print(f"  [{name}] attempt{attempt} domcontentloaded fail: {str(e1)[:60]}; try commit")
                    try:
                        page.goto(url, wait_until="commit", timeout=60000)
                    except Exception as e2:
                        print(f"  [{name}] attempt{attempt} commit fail too: {str(e2)[:60]}")
                text_len = 0
                for i in range(8):
                    page.wait_for_timeout(5000)
                    try:
                        text_len = page.evaluate("document.body ? document.body.innerText.length : 0")
                    except Exception:
                        text_len = 0
                    if text_len > 400:
                        break
                print(f"  [{name}] attempt{attempt} text_len={text_len} url={page.url}")
                if text_len > 400:
                    page.screenshot(path=str(out), clip={"x": 0, "y": 0, "width": 1280, "height": 720})
                    print(f"  OK {name} (attempt {attempt})")
                    done = True
                else:
                    time.sleep(5)
            except Exception as e:
                print(f"  [{name}] attempt{attempt} ERR {type(e).__name__} {str(e)[:100]}")
            finally:
                page.close()
                ctx.close()
        if not done:
            print(f"BOTH_FAIL {name}")
    browser.close()

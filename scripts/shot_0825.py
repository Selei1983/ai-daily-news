#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) for the 0825 daily digest."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT_DIR = Path("/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images")

# (primary_url, fallback_url, output_name)
targets = [
    ("https://cnevpost.com/2026/08/24/xpeng-carves-out-robotics-business/",
     "https://www.roboticstomorrow.com/news/2026/08/24/xpeng-robotics-business-raises-over-us900-million-at-a-post-money-valuation-of-over-us63-billion-accelerating-physical-ai-deployment/26985/",
     "0825-xpeng.png"),
    ("https://newcode.ai/",
     "https://www.law.com/legaltechnews/2026/08/24/legal-ai-startup-newcode-announces-135m-series-a-round-with-investment-from-relativity/",
     "0825-newcode.png"),
    ("https://instinct.co/",
     "https://techcrunch.com/2026/08/24/instincts-powerful-ai-assistant-is-raising-privacy-and-security-concerns/",
     "0825-instinct.png"),
    ("https://openai.com/index/gpt-5-6-in-kiro/",
     "https://kiro.dev/changelog/models/gpt-5-6/",
     "0825-kiro.png"),
    ("https://www.163.com/dy/article/L54ONJ5M0511D6RL.html",
     "https://www.163.com/dy/article/L543AS2I05118O8G.html",
     "0825-nvidia-perplexity.png"),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 720}, device_scale_factor=1,
                              user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36")
    for primary, fallback, name in targets:
        out = OUT_DIR / name
        done = False
        for url in (primary, fallback):
            page = ctx.new_page()
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=45000)
                page.wait_for_timeout(7000)
                text_len = page.evaluate("document.body ? document.body.innerText.length : 0")
                if text_len < 150:
                    print(f"WARN low content ({text_len}) {url}")
                    continue
                page.screenshot(path=str(out), clip={"x": 0, "y": 0, "width": 1280, "height": 720})
                print(f"OK {name} <- {url} (text={text_len})")
                done = True
            except Exception as e:
                print(f"FAIL {url}: {type(e).__name__} {str(e)[:120]}")
            finally:
                page.close()
            if done:
                break
        if not done:
            print(f"BOTH_FAIL {name}")
    browser.close()

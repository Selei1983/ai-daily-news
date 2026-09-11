#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) for the 0911 daily digest."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT_DIR = Path("/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images")

# (primary_url, output_name)
targets = [
    ("https://techcrunch.com/2026/09/10/openai-puts-pro-subscriptions-on-hold-due-to-astra-demand/",
     "0911-openai-pro.png"),
    ("https://siliconangle.com/2026/09/10/deepseek-releases-v4-1-flash-says-it-outperforms-flagship-v4-pro/",
     "0911-deepseek-flash.png"),
    ("https://techcrunch.com/2026/09/10/anthropic-details-distillation-campaigns-from-alibaba-moonshot-ai-and-deepseek/",
     "0911-anthropic-distill.png"),
    ("https://siliconangle.com/2026/09/10/chipmaker-positron-nabs-875m-to-speed-up-inference-with-consumer-grade-memory/",
     "0911-positron.png"),
    ("https://news.pedaily.cn/202609/568848.shtml",
     "0911-compute-idle.png"),
    ("https://techcrunch.com/2026/09/10/ai-agents-are-flooding-public-services-with-new-requests/",
     "0911-agent-flooding.png"),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 720}, device_scale_factor=1,
                              user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36",
                              locale="zh-CN")
    for url, name in targets:
        out = OUT_DIR / name
        page = ctx.new_page()
        try:
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=45000)
                page.wait_for_timeout(9000)
            except Exception as e1:
                print(f"  domcontentloaded fail {url}: {type(e1).__name__} {str(e1)[:80]}; retry commit+12s")
                page.goto(url, wait_until="commit", timeout=45000)
                page.wait_for_timeout(12000)
            text_len = page.evaluate("document.body ? document.body.innerText.length : 0")
            if text_len < 120:
                print(f"WARN low content ({text_len}) {url}")
            page.screenshot(path=str(out), clip={"x": 0, "y": 0, "width": 1280, "height": 720})
            print(f"OK {name} <- {url} (text={text_len})")
        except Exception as e:
            print(f"FAIL {url}: {type(e).__name__} {str(e)[:120]}")
        finally:
            page.close()
    browser.close()

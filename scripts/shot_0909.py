#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) for the 0909 daily digest."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT_DIR = Path("/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images")

# (primary_url, output_name)
targets = [
    ("https://techcrunch.com/2026/09/08/meta-debuts-its-muse-ai-agent-will-consumers-trust-it/",  # Meta Muse agent (TechCrunch)
     "0909-meta-muse.png"),
    ("https://siliconangle.com/2026/09/08/google-deepminds-alphagenome-atlas-maps-all-9-billion-possible-human-dna-changes/",  # AlphaGenome Atlas (SA)
     "0909-alphagenome.png"),
    ("https://news.pedaily.cn/202609/568694.shtml",  # Agent安全成为第一命题 (产业家 via pedaily)
     "0909-agent-security.png"),
    ("https://siliconangle.com/2026/09/08/ai-coding-startup-cognition-raises-2b-at-48b-valuation-as-revenue-nears-900m/",  # Cognition $2B @ $48B (SA)
     "0909-cognition.png"),
    ("https://www.qbitai.com/2026/09/485555.html",  # 王云鹤创业首秀 NeoHorse (量子位)
     "0909-neohorse.png"),
    ("https://siliconangle.com/2026/09/08/antioch-raises-32m-to-move-robot-testing-into-simulation/",  # Antioch Series A (SA)
     "0909-antioch.png"),
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

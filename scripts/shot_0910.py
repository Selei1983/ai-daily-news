#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) for the 0910 daily digest."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT_DIR = Path("/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images")

# (primary_url, output_name)
targets = [
    ("https://news.pedaily.cn/202609/568773.shtml",   # OpenAI Astra 供给墙/暂停Pro订阅 (投资界·硬AI)
     "0910-openai-compute.png"),
    ("https://news.pedaily.cn/202609/568754.shtml",   # DeepSeek降价60% (机器之心 via 投资界)
     "0910-deepseek.png"),
    ("https://techcrunch.com/2026/09/09/harvey-hits-15-5b-valuation-months-after-reaching-11b/",  # Harvey $15.5B (TC)
     "0910-harvey.png"),
    ("https://siliconangle.com/2026/09/09/cymphony-launches-with-30m-to-track-what-ai-agents-can-reach/",  # Cymphony $30M (SA)
     "0910-agent-governance.png"),
    ("https://news.pedaily.cn/202609/568768.shtml",   # Anthropic研究员辞职 (字母榜 via 投资界)
     "0910-safety-resign.png"),
    ("https://www.qbitai.com/2026/09/486450.html",    # 苹果首款折叠屏 iPhone Duo (量子位)
     "0910-apple.png"),
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

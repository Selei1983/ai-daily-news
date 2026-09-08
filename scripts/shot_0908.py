#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) for the 0908 daily digest."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT_DIR = Path("/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images")

# (primary_url, output_name)
targets = [
    ("https://finance.sina.cn/stock/jdts/2026-09-07/detail-iniqyzxu6346380.d.html",  # 微信内测AI社交 (界面 via sina)
     "0908-wechat-a2a.png"),
    ("https://www.qbitai.com/2026/09/485108.html",  # Mostik 桥 (量子位)
     "0908-mostik.png"),
    ("https://www.qbitai.com/2026/09/485431.html",  # GPT-6 Sol 内测 (量子位)
     "0908-openai-sol.png"),
    ("https://siliconangle.com/2026/09/07/openai-chief-scientist-argues-for-ai-research-slowdown/",  # Pachocki essay (SiliconANGLE)
     "0908-pachocki.png"),
    ("https://news.pedaily.cn/202609/568644.shtml",  # DeepSeek 扩招150人 (投资界/量子位)
     "0908-deepseek.png"),
    ("https://news.pedaily.cn/202609/568645.shtml",  # 深度智控 B+ (投资界)
     "0908-deepcontrol.png"),
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

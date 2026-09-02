#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) for the 0902 daily digest."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT_DIR = Path("/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images")

# (primary_url, fallback_url, output_name)
targets = [
    ("https://36kr.com/p/3965405241204228",  # Fable 5.1 新智元
     "https://news.pedaily.cn/202609/568403.shtml",
     "0902-fable51.png"),
    ("https://36kr.com/p/3965568457514501",  # 后西游记
     "https://news.pedaily.cn/202609/568412.shtml",
     "0902-houxiyouji.png"),
    ("https://36kr.com/p/3964719241305607",  # VAST 30亿
     "https://36kr.com/p/3964567434059016",
     "0902-vast.png"),
    ("https://36kr.com/p/3964873497320966",  # 智谱财报
     "https://36kr.com/p/3965507243891976",
     "0902-zhipu.png"),
    ("https://36kr.com/p/3964567434059016",  # Violoop
     "https://36kr.com/p/3964719417040392",
     "0902-violoop.png"),
    ("https://36kr.com/p/3964719417040392",  # Manus
     "https://36kr.com/p/3965506148652681",
     "0902-manus.png"),
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
                try:
                    page.goto(url, wait_until="domcontentloaded", timeout=45000)
                    page.wait_for_timeout(7000)
                except Exception as e1:
                    print(f"  domcontentloaded fail {url}: {type(e1).__name__} {str(e1)[:80]}; retry commit+12s")
                    page.goto(url, wait_until="commit", timeout=45000)
                    page.wait_for_timeout(12000)
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

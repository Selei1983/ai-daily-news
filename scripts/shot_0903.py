#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) for the 0903 daily digest."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT_DIR = Path("/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images")

# (primary_url, fallback_url, output_name)
targets = [
    ("https://36kr.com/p/3966935532412416",  # Gemini 3.8 新智元
     "https://www.36kr.com/p/3966935532412416",
     "0903-gemini38.png"),
    ("https://36kr.com/p/3966094074600965",  # NVIDIA x Hugging Face 界面/财联社
     "https://www.36kr.com/p/3966094074600965",
     "0903-nvidia-hf.png"),
    ("https://36kr.com/p/3966927971325573",  # 月之暗面 字母榜
     "https://www.36kr.com/p/3966927971325573",
     "0903-moonshot-ipo.png"),
    ("https://36kr.com/p/3965806085053961",  # World Labs Atlas 机器之心
     "https://www.36kr.com/p/3965806085053961",
     "0903-worldlabs-atlas.png"),
    ("https://36kr.com/p/3966110624537860",  # AfterQuery 智东西
     "https://www.36kr.com/p/3966110624537860",
     "0903-afterquery.png"),
    ("https://36kr.com/p/3966955457519111",  # 蘑菇物联 投资界
     "https://www.36kr.com/p/3966955457519111",
     "0903-mushroom.png"),
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

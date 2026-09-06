#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) for the 0906 daily digest."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT_DIR = Path("/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images")

# (primary_url, fallback_url, output_name)
targets = [
    ("https://techcrunch.com/2026/09/05/openai-confirms-wiki-incident-says-its-working-on-a-framework-for-more-disclosure/",  # OpenAI framework statement
     "https://36kr.com/newsflashes/3970189273248260",
     "0906-openai-framework.png"),
    ("https://www.36kr.com/newsflashes/3970040744227336",  # G42 US majority stake talks
     "https://36kr.com/newsflashes/3970040744227336",
     "0906-g42.png"),
    ("https://www.36kr.com/p/3969940251209993",  # 光象科技 ActEffect (量子位)
     "https://36kr.com/p/3969940251209993",
     "0906-guangxiang.png"),
    ("https://www.36kr.com/p/3970051115266306",  # WorkBuddy 开放生态 (Tech星球)
     "https://36kr.com/p/3970051115266306",
     "0906-workbuddy.png"),
    ("https://www.36kr.com/newsflashes/3970039177359622",  # 小米 Xiaomi-TabLDM
     "https://36kr.com/newsflashes/3970039177359622",
     "0906-xiaomi-tablldm.png"),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 720}, device_scale_factor=1,
                              user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36",
                              locale="zh-CN")
    for primary, fallback, name in targets:
        out = OUT_DIR / name
        done = False
        for url in (primary, fallback):
            page = ctx.new_page()
            try:
                try:
                    page.goto(url, wait_until="domcontentloaded", timeout=45000)
                    page.wait_for_timeout(8000)
                except Exception as e1:
                    print(f"  domcontentloaded fail {url}: {type(e1).__name__} {str(e1)[:80]}; retry commit+12s")
                    page.goto(url, wait_until="commit", timeout=45000)
                    page.wait_for_timeout(12000)
                text_len = page.evaluate("document.body ? document.body.innerText.length : 0")
                if text_len < 120:
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

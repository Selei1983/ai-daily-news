#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) for the 0901 daily digest."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT_DIR = Path("/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images")

# (primary_url, fallback_url, output_name)
targets = [
    ("https://36kr.com/p/3963330012970116",  # Kimi 30%分成 模型版税
     "https://36kr.com/p/3963162610734721",
     "0901-kimi-royalty.png"),
    ("https://36kr.com/p/3964128883054209",  # ChipAgents 9亿A轮
     "https://news.pedaily.cn/202609/568371.shtml",
     "0901-chipagents.png"),
    ("https://36kr.com/p/3963248919795330",  # 豆包工作 AI办公
     "https://www.qbitai.com/",
     "0901-doubao-work.png"),
    ("https://siliconangle.com/2026/08/31/openai-says-its-ad-business-has-already-hit-1b-in-annualized-rev/",  # OpenAI广告1B
     "https://techcrunch.com/2026/08/31/",
     "0901-openai-ads.png"),
    ("https://news.pedaily.cn/202609/568370.shtml",  # DeepSeek V4
     "https://news.pedaily.cn/202609/568364.shtml",
     "0901-deepseek-v4.png"),
    ("https://36kr.com/p/3963233115257984",  # Claude Max 20x
     "https://www.jiqizhixin.com/",
     "0901-claude-max20x.png"),
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

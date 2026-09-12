#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) for the 0912 daily digest."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT_DIR = Path("/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images")
OUT_DIR.mkdir(parents=True, exist_ok=True)

targets = [
    ("https://news.pedaily.cn/202609/568893.shtml", "0912-ai-distribution.png"),
    ("https://techcrunch.com/2026/09/11/openais-feud-with-mathematicians-is-only-escalating/", "0912-math-feud.png"),
    ("https://siliconangle.com/2026/09/11/chinese-ai-chip-developer-enflame-raises-912m-in-ipo/", "0912-enflame-ipo.png"),
    ("https://techcrunch.com/2026/09/11/mecka-ai-nears-500m-valuation-in-sequoia-led-deal-amid-rush-for-robot-training-data/", "0912-mecka.png"),
    ("https://siliconangle.com/2026/09/10/openai-targets-wall-street-bankers-with-a-new-version-of-chatgpt/", "0912-chatgpt-finance.png"),
    ("https://siliconangle.com/2026/09/11/salesforce-introduces-new-ai-agents-to-automate-sales-support-tasks/", "0912-salesforce-agents.png"),
    ("https://www.qbitai.com/2026/09/487631.html", "0912-mybank-agent.png"),
    ("https://techcrunch.com/2026/09/11/kimi-maker-moonshot-ai-targets-2-billion-in-annual-revenue/", "0912-moonshot.png"),
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

# variance check
try:
    from PIL import Image
    import statistics
    for _, name in targets:
        f = OUT_DIR / name
        if f.exists():
            im = Image.open(f).convert("L")
            px = list(im.getdata())
            print(f"VAR {name}: {statistics.pvariance(px):.0f} size={im.size}")
except Exception as e:
    print("variance check skipped:", e)

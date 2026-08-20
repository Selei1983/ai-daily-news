#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) of today's 5 digest URLs using local Playwright."""
from playwright.sync_api import sync_playwright

# (primary, fallback, output)
urls = [
    ("https://techcrunch.com/2026/08/19/rillet-raises-100m-series-c-at-1b-valuation-2-years-after-emerging-from-stealth/",
     "https://www.rillet.com/",
     "/tmp/0820-rillet-raw.png"),
    ("https://finance.yahoo.com/technology/ai/articles/chip-firm-fractile-seeks-6-183158545.html",
     "https://finance.sina.com.cn/7x24/2026-08-20/doc-ininwtuc6915440.shtml",
     "/tmp/0820-fractile-raw.png"),
    ("https://finance.sina.com.cn/tech/digi/2026-08-19/doc-ininvfsz9494660.shtml",
     "https://m.sohu.com/a/1064690957_100117963",
     "/tmp/0820-glm-raw.png"),
    ("https://www.bjnews.com.cn/detail/1783328835129622.html",
     "https://xinwen.bjd.com.cn/content/s6a852397e4b0e45f3fd635ad.html",
     "/tmp/0820-wrc-raw.png"),
    ("https://finance.yahoo.com/technology/ai/articles/openai-q2-growth-trails-anthropic-102250259.html",
     "https://thenextweb.com/news/openai-q2-revenue-anthropic-surpasses",
     "/tmp/0820-openai-raw.png"),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 720}, device_scale_factor=1,
                              user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36")
    for primary, fallback, out in urls:
        page = ctx.new_page()
        ok = False
        for url in (primary, fallback):
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=45000)
                page.wait_for_timeout(8000)
                # check page has real content
                text_len = page.evaluate("document.body ? document.body.innerText.length : 0")
                if text_len < 200:
                    print(f"WARN low content ({text_len}) {url}")
                    continue
                page.screenshot(path=out, clip={"x": 0, "y": 0, "width": 1280, "height": 720})
                print(f"OK {out} <- {url} (text={text_len})")
                ok = True
                break
            except Exception as e:
                print(f"FAIL {url}: {e}")
        if not ok:
            print(f"FAILED-ALL {out}")
        page.close()
    browser.close()

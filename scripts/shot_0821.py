#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) of today's 5 digest URLs using local Playwright."""
from playwright.sync_api import sync_playwright

# (primary, fallback, output)
urls = [
    ("https://www.callosum.com/",
     "https://sifted.eu/articles/callosum-raise-atomico-plural-uk-sovereign-ai",
     "/tmp/0821-callosum-raw.png"),
    ("https://velaura.ai/",
     "https://techstartups.com/2026/08/18/velaura-ai-raises-110m-series-a-at-1b-valuation-to-tackle-ais-growing-power-problem/",
     "/tmp/0821-velaura-raw.png"),
    ("https://router.com/",
     "https://techcrunch.com/2026/08/20/ramp-launches-its-own-ai-model-router-called-router/",
     "/tmp/0821-router-raw.png"),
    ("https://www.meta.ai/",
     "https://techcrunch.com/2026/08/20/meta-ais-new-mac-app-wants-you-to-talk-to-your-apps/",
     "/tmp/0821-metaai-raw.png"),
    ("https://www.36kr.com/p/3947745360592003",
     "https://www.aihehuo.com/blog/9253-news-2026-08-20",
     "/tmp/0821-ali-tencent-raw.png"),
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

#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) of today's 5 digest URLs using local Playwright."""
from playwright.sync_api import sync_playwright

urls = [
    ("https://www.36kr.com/p/3943674198218376", "/tmp/0818-unitree-raw.png"),
    ("https://finance.sina.com.cn/stock/usstock/c/2026-08-17/doc-ininqxur7019218.shtml", "/tmp/0818-higgsfield-raw.png"),
    ("https://www.cls.cn/detail/2456537", "/tmp/0818-chatgpt-raw.png"),
    ("https://www.163.com/dy/article/L45N47EH05118MCQ.html", "/tmp/0818-honor-raw.png"),
    ("https://finance.sina.com.cn/tech/digi/2026-08-17/doc-ininrzhc6720534.shtml", "/tmp/0818-jiuguang-raw.png"),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 720}, device_scale_factor=1,
                              user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36")
    for url, out in urls:
        page = ctx.new_page()
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(9000)
            page.screenshot(path=out, clip={"x": 0, "y": 0, "width": 1280, "height": 720})
            print(f"OK {out}")
        except Exception as e:
            print(f"FAIL {url}: {e}")
        finally:
            page.close()
    browser.close()

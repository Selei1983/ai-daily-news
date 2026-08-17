#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) of today's 5 digest URLs using local Playwright."""
from playwright.sync_api import sync_playwright

urls = [
    ("https://finance.sina.com.cn/stock/t/2026-08-17/doc-ininqpeu0374642.shtml", "/tmp/0817-mifeng-raw.png"),
    ("https://www.163.com/dy/article/L4H8RFKJ05198R3E.html", "/tmp/0817-pandaai-raw.png"),
    ("https://finance.sina.cn/stock/jdts/2026-08-16/detail-ininnkfv7988038.d.html", "/tmp/0817-openai-raw.png"),
    ("https://news.ifeng.com/c/8vYt8W2gwqO", "/tmp/0817-deepseek-raw.png"),
    ("https://www.163.com/dy/article/L4FLL5MI0511A6N9.html", "/tmp/0817-apple-raw.png"),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 720}, device_scale_factor=1,
                              user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36")
    for url, out in urls:
        page = ctx.new_page()
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(8000)
            page.screenshot(path=out, clip={"x": 0, "y": 0, "width": 1280, "height": 720})
            print(f"OK {out}")
        except Exception as e:
            print(f"FAIL {url}: {e}")
        finally:
            page.close()
    browser.close()

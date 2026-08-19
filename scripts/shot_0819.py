#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) of today's 5 digest URLs using local Playwright."""
from playwright.sync_api import sync_playwright

urls = [
    ("https://www.tmtpost.com/nictation/8107835.html", "/tmp/0819-hand-raw.png"),
    ("https://finance.sina.com.cn/roll/2026-08-19/doc-ininukpm9825537.shtml", "/tmp/0819-etched-raw.png"),
    ("https://www.sohu.com/a/1064388271_120988576", "/tmp/0819-qwenoffice-raw.png"),
    ("https://www.163.com/dy/article/L4IMPLLD05118UGF.html", "/tmp/0819-wispr-raw.png"),
    ("https://k.sina.com.cn/article_5953189932_162d6782c06704vk22.html", "/tmp/0819-baidu-raw.png"),
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

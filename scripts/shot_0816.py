#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) of today's 5 digest URLs using local Playwright."""
from playwright.sync_api import sync_playwright

urls = [
    ("https://finance.sina.com.cn/tech/roll/2026-08-15/doc-ininkfhq3608278.shtml", "/tmp/0816-cursor-raw.png"),
    ("https://www.ithome.com/0/990/187.htm", "/tmp/0816-qwen-raw.png"),
    ("https://www.cls.cn/detail/2455062", "/tmp/0816-nvidia-raw.png"),
    ("https://www.leiphone.com/category/industrynews/TASeafIbnXXY0YSg.html", "/tmp/0816-moliang-raw.png"),
    ("https://news.ifeng.com/c/8vaD3kx26UZ", "/tmp/0816-kukuai-raw.png"),
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

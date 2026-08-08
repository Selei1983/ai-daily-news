#!/usr/bin/env python3
"""Screenshot Omilia article on pulse2 (lighter site)."""
from playwright.sync_api import sync_playwright
from PIL import Image

def score(path):
    im = Image.open(path).convert("RGB")
    small = im.resize((64, 36))
    colors = small.getcolors(64 * 36)
    n = len(colors)
    top = max(c for c, _ in colors) / (64 * 36)
    return n, top

urls = [
    "https://pulse2.com/omilia-raises-67-million-series-b-to-expand-agentic-customer-experience-platform/",
    "https://cxm.world/uncategorized/omilia-raises-67m-agentic-voice-ai/",
]
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 720}, device_scale_factor=1)
    for url in urls:
        page = ctx.new_page()
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(6000)
            page.screenshot(path="/tmp/0808-omilia-raw.png", clip={"x": 0, "y": 0, "width": 1280, "height": 720})
            n, top = score("/tmp/0808-omilia-raw.png")
            print(f"{url} -> colors={n} top={top:.2%}")
            if n > 150:
                print("KEEPING")
                break
        except Exception as e:
            print(f"FAIL {url}: {e}")
        finally:
            page.close()
    browser.close()

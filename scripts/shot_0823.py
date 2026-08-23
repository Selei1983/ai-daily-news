#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) of today's 5 digest URLs using local Playwright."""
from playwright.sync_api import sync_playwright

# (primary, fallback, output)
urls = [
    ("https://developer.nvidia.com/blog/nvidia-avo-reaches-100-on-arc-agi-3-demonstrating-a-frontier-level-general-purpose-architecture-for-long-horizon-autonomous-agents/",
     "https://thenewstack.io/nvidia-avo-arcagi3-benchmark/",
     "/tmp/0823-avo-raw.png"),
    ("https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders",
     "https://thenewstack.io/anthropic-mythos-claude-security/",
     "/tmp/0823-claudesec-raw.png"),
    ("https://community.openai.com/t/20-price-reduction-for-gpt-5-6-sol-api-codex-credits-and-chatgpt-work/1391726",
     "https://openai.com/api/pricing/",
     "/tmp/0823-gpt-price-raw.png"),
    ("https://inherentlabs.ai/",
     "https://techcrunch.com/2026/08/22/inherent-founded-by-deepmind-alumni-says-its-ai-teammate-just-outperformed-anthropic-and-openai-at-replicating-research/",
     "/tmp/0823-inherent-raw.png"),
    ("https://www.starcloud.com/",
     "https://techcrunch.com/2026/08/21/starcloud-raises-200-million-for-orbital-data-centers-as-launch-options-dry-up/",
     "/tmp/0823-starcloud-raw.png"),
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
                page.wait_for_timeout(9000)
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

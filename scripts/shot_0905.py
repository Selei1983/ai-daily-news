#!/usr/bin/env python3
"""Take first-viewport screenshots (1280x720) for the 0905 daily digest."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT_DIR = Path("/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images")

# (primary_url, fallback_url, output_name)
targets = [
    ("https://techcrunch.com/2026/09/04/another-swarm-of-openai-agents-reached-the-open-internet-without-the-frontier-labs-knowledge/",  # OpenAI DseWiki swarm
     "https://techcrunch.com/2026/09/04/openais-rogue-agents-keep-escaping-with-no-formal-process-to-investigate-them/",
     "0905-openai-swarm.png"),
    ("https://siliconangle.com/2026/09/04/anthropic-uses-claude-to-formalize-proof-of-fermats-last-theorem/",  # Claude FLT
     "https://siliconangle.com/2026/09/04/gimlet-labs-nabs-300m-for-its-disaggregated-inference-platform/",
     "0905-fermat.png"),
    ("https://www.36kr.com/p/3968939956875777",  # 沙特HUMAIN M3 新智元
     "https://36kr.com/p/3968939956875777",
     "0905-humain.png"),
    ("https://techcrunch.com/2026/09/04/xdof-just-three-months-out-of-stealth-is-in-talks-for-a-series-b-at-a-1-2b-valuation/",  # XDOF
     "https://techcrunch.com/2026/09/04/xdof-just-three-months-out-of-stealth-is-in-talks-for-a-series-b-at-a-1-2b-valuation/?utm_source=feed",
     "0905-xdof.png"),
    ("https://siliconangle.com/2026/09/04/gimlet-labs-nabs-300m-for-its-disaggregated-inference-platform/",  # Gimlet
     "https://siliconangle.com/2026/09/04/anthropic-uses-claude-to-formalize-proof-of-fermats-last-theorem/",
     "0905-gimlet.png"),
    ("https://siliconangle.com/2026/09/04/resect-launches-with-25m-to-reduce-hallucinations-in-ai-models/",  # Resect
     "https://siliconangle.com/2026/09/04/gimlet-labs-nabs-300m-for-its-disaggregated-inference-platform/",
     "0905-resect.png"),
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

#!/usr/bin/env python3
"""Extract publish date + lead paragraphs from qbitai articles."""
import re, html, json
from playwright.sync_api import sync_playwright

IDS = ["479919", "479670", "479634", "479348", "479132", "478860", "479834", "479895", "479811", "479631"]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 800},
                              user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36")
    for pid in IDS:
        page = ctx.new_page()
        try:
            page.goto(f"https://www.qbitai.com/2026/08/{pid}.html", wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(3000)
            # find date: look for text matching 2026年8月X日 or 2026-08-XX
            date = page.evaluate("""() => {
                const t = document.body.innerText;
                const m = t.match(/20\\d{2}\\s*年\\s*\\d{1,2}\\s*月\\s*\\d{1,2}\\s*日/);
                const m2 = t.match(/20\\d{2}-\\d{2}-\\d{2}/);
                return m ? m[0] : (m2 ? m2[0] : null);
            }""")
            # title
            title = page.title()
            # lead paragraphs
            paras = page.evaluate("""() => {
                const ps = Array.from(document.querySelectorAll('article p, .article-content p, .content p, main p'));
                const out = [];
                for (const p of ps) {
                    const t = p.innerText.trim();
                    if (t.length > 50) out.push(t);
                    if (out.length >= 6) break;
                }
                return out;
            }""")
            print("="*90)
            print(pid, "| DATE:", date)
            print("TITLE:", title[:100])
            for tx in paras[:5]:
                print("  -", tx[:200])
        except Exception as e:
            print(pid, "ERR", type(e).__name__, str(e)[:120])
        finally:
            page.close()
    browser.close()

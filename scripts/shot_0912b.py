#!/usr/bin/env python3
"""Re-shoot US-article screenshots (1280x720): strip ads, scroll headline text into view."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT_DIR = Path("/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images")

# (url, output_name, headline substring)
targets = [
    ("https://techcrunch.com/2026/09/11/openais-feud-with-mathematicians-is-only-escalating/", "0912-math-feud.png", "feud with mathematicians"),
    ("https://siliconangle.com/2026/09/11/chinese-ai-chip-developer-enflame-raises-912m-in-ipo/", "0912-enflame-ipo.png", "Chinese AI chip developer Enflame raises"),
    ("https://techcrunch.com/2026/09/11/mecka-ai-nears-500m-valuation-in-sequoia-led-deal-amid-rush-for-robot-training-data/", "0912-mecka.png", "Mecka AI nears"),
    ("https://siliconangle.com/2026/09/10/openai-targets-wall-street-bankers-with-a-new-version-of-chatgpt/", "0912-chatgpt-finance.png", "OpenAI targets Wall Street bankers"),
    ("https://siliconangle.com/2026/09/11/salesforce-introduces-new-ai-agents-to-automate-sales-support-tasks/", "0912-salesforce-agents.png", "Salesforce introduces new AI agents"),
    ("https://techcrunch.com/2026/09/11/kimi-maker-moonshot-ai-targets-2-billion-in-annual-revenue/", "0912-moonshot.png", "Moonshot AI targets"),
]

CLEAN = """() => {
  const kill = (el) => { try { el.style.setProperty('display','none','important'); } catch(e){} };
  document.querySelectorAll('[class*="advert" i], [id*="advert" i], [class*="google-ad" i], ins, [class*="ad-slot" i], [class*="taboola" i], [class*="-ads-" i], [id*="-ads-" i]').forEach(kill);
  document.querySelectorAll('aside').forEach(kill);
  document.querySelectorAll('div,section').forEach(d => {
    const t=(d.innerText||'').trim();
    if(t==='Advertisement' || t==='ADVERTISEMENT') kill(d);
  });
  window.scrollTo(0,0);
}"""

SCROLL_TPL = """(needle) => {
  const all=[...document.querySelectorAll('h1,h2,h3,p,span,div')];
  let best=null;
  for(const el of all){
    const t=(el.innerText||'').trim();
    if(t.includes(needle) && t.length < needle.length+120 && el.getBoundingClientRect().height>10){
      if(!best || el.getBoundingClientRect().height < best.getBoundingClientRect().height) best=el;
    }
  }
  if(best){ const y=best.getBoundingClientRect().top + window.scrollY - 110; window.scrollTo(0, Math.max(0,y)); return best.innerText.slice(0,90); }
  return 'NOTFOUND';
}"""

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 720}, device_scale_factor=1,
                              user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36",
                              locale="en-US")
    for url, name, needle in targets:
        out = OUT_DIR / name
        page = ctx.new_page()
        try:
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=45000)
                page.wait_for_timeout(8000)
            except Exception:
                page.goto(url, wait_until="commit", timeout=45000)
                page.wait_for_timeout(12000)
            page.evaluate(CLEAN)
            page.wait_for_timeout(600)
            htxt = page.evaluate(SCROLL_TPL, needle)
            page.wait_for_timeout(1200)
            page.screenshot(path=str(out), clip={"x": 0, "y": 0, "width": 1280, "height": 720})
            print(f"OK {name} -> {htxt[:70]!r}")
        except Exception as e:
            print(f"FAIL {url}: {type(e).__name__} {str(e)[:120]}")
        finally:
            page.close()
    browser.close()

from PIL import Image
import statistics
for _, name, _ in targets:
    f = OUT_DIR / name
    if f.exists():
        im = Image.open(f).convert("L")
        print(f"VAR {name}: {statistics.pvariance(list(im.get_flattened_data())):.0f} {im.size}")

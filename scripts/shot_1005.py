#!/usr/bin/env python3
"""First-viewport screenshots (1280x720) for the 1005 daily digest."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT_DIR = Path("/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/images")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# (url, output_name, headline substring)
targets = [
    ("https://casp.ac/reports/intelligence-explosion", "1005-casp-explosion.png", "intelligence explosion"),
    ("https://techcrunch.com/2026/10/01/amazon-releases-its-own-jev-clone-as-decision-models-flood-the-web/", "1005-decision-models.png", "Amazon releases its own Jev clone"),
    ("https://news.pedaily.cn/202610/569841.shtml", "1005-startlux.png", "Jev被请下王座"),
    ("https://www.anthropic.com/news/claude-frontier-academy", "1005-anthropic-fde.png", "Claude Frontier Academy"),
    ("https://news.pedaily.cn/202610/569845.shtml", "1005-anthropic-health.png", "OpenEvidence"),
    ("https://hwbusters.com/news/google-pauses-its-open-source-bug-bounty-for-product-flaws-as-ai-slop-buries-maintainers/", "1005-bugbounty.png", "Google Pauses"),
    ("https://9to5mac.com/2026/10/02/apples-new-homeos-will-launch-this-month-heres-whats-coming/", "1005-apple-homeos.png", "homeOS"),
    ("https://www.tavus.io/griffin", "1005-tavus-griffin.png", "Griffin"),
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
                              locale="zh-CN")
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

#!/usr/bin/env python3
"""Fetch 36kr article pages via local playwright and dump article body text."""
import sys, json
from pathlib import Path
from playwright.sync_api import sync_playwright

URLS = [
    "https://36kr.com/p/3973222378877184",  # 微信内测AI社交
    "https://36kr.com/p/3973262998384902",  # 虚幻引擎CEO Code World Model (新智元)
    "https://36kr.com/p/3973125912572161",  # 李飞飞 三张照片 (AI科技大本营)
    "https://36kr.com/p/3972970929009154",  # 童欣加入Meshy (极客公园)
    "https://36kr.com/p/3974040294388232",  # DeepSeek扩招150人 (量子位)
    "https://36kr.com/p/3973285667467522",  # 400亿AI短剧 (铅笔道)
    "https://36kr.com/p/3973910125457667",  # GPT-6 Astra 验证码 (鲸选AI)
    "https://36kr.com/p/3966062388780290",  # AICRON 金特务 (兰芥)
    "https://36kr.com/p/3973128237363717",  # OpenAI首席科学家 slowdown letter (基础人生)
]

def get_text(page, url):
    try:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(7000)
        except Exception as e1:
            page.goto(url, wait_until="commit", timeout=45000)
            page.wait_for_timeout(10000)
        # retry if empty shell
        for _ in range(2):
            ln = page.evaluate("document.body ? document.body.innerText.length : 0")
            if ln > 500:
                break
            page.wait_for_timeout(4000)
        title = page.evaluate("document.title || ''")
        # find article container text
        text = page.evaluate("""(() => {
            const sels = ['.article-content','.articleDetailContent','.article-detail-content','#article-content','.common-width','article','main'];
            for (const s of sels) {
                const el = document.querySelector(s);
                if (el && el.innerText.length > 300) return el.innerText;
            }
            return document.body ? document.body.innerText : '';
        })()""")
        return {"url": url, "title": title, "text": text}
    except Exception as e:
        return {"url": url, "error": f"{type(e).__name__}: {str(e)[:200]}"}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(
        viewport={"width": 1280, "height": 800},
        user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36",
        locale="zh-CN",
    )
    out = []
    for url in URLS:
        page = ctx.new_page()
        r = get_text(page, url)
        out.append(r)
        page.close()
        print(f"DONE {url} len={len(r.get('text',''))} err={r.get('error','')}", flush=True)
    browser.close()

with open("/tmp/36kr_dump.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("saved /tmp/36kr_dump.json")

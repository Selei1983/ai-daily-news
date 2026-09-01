#!/usr/bin/env python3
"""Publish today's digest to WordPress (aipmclub.com) via REST API."""
import base64
import sys
import requests

try:
    import markdown
    HAS_MD = True
except ImportError:
    HAS_MD = False

MD_PATH = "/Users/jowe_macmini/.hermes/workspace/ai-daily-news/daily/2026-09-01-ai-daily-digest.md"
WP_URL = "https://aipmclub.com/wp-json/wp/v2/posts"
USER = "jowelin"
APP_PASSWORD = "yRR6 WTG6 XWUU kvn3 QTg7 bWpX".replace(" ", "")
CATEGORY_ID = 136  # ai-daily

with open(MD_PATH, encoding="utf-8") as f:
    md_text = f.read()

# Title = first H1 line
title = md_text.splitlines()[0].lstrip("# ").strip()

if HAS_MD:
    html = markdown.markdown(md_text, extensions=["extra", "nl2br"])
else:
    import re, html as htmlmod
    lines = []
    in_list = False
    for line in md_text.splitlines():
        if line.startswith("# "):
            lines.append(f"<h1>{line[2:]}</h1>")
        elif line.startswith("## "):
            lines.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("### "):
            lines.append(f"<h3>{line[4:]}</h3>")
        elif line.startswith("![") and "](" in line:
            alt, url = line[2:].split("](", 1)
            url = url.rstrip(")")
            lines.append(f'<p><img src="{url}" alt="{alt}" style="max-width:100%;height:auto;"/></p>')
        elif line.startswith("!["):
            continue
        elif line.startswith("[") and "](" in line:
            pass
        elif line.strip() == "---":
            lines.append("<hr/>")
        elif line.strip().startswith("- "):
            if not in_list:
                lines.append("<ul>")
                in_list = True
            lines.append(f"<li>{line.strip()[2:]}</li>")
        elif line.strip() == "":
            if in_list:
                lines.append("</ul>")
                in_list = False
            continue
        else:
            if in_list:
                lines.append("</ul>")
                in_list = False
            lines.append(f"<p>{line}</p>")
    if in_list:
        lines.append("</ul>")
    html = "\n".join(lines)

# Convert relative image paths to GitHub raw URLs
html = html.replace('src="images/', 'src="https://raw.githubusercontent.com/Selei1983/ai-daily-news/main/daily/images/')

auth = base64.b64encode(f"{USER}:{APP_PASSWORD}".encode()).decode()
headers = {
    "Authorization": f"Basic {auth}",
    "Content-Type": "application/json",
}
data = {
    "title": title,
    "content": html,
    "status": "publish",
    "categories": [CATEGORY_ID],
}

print(f"Publishing: {title[:80]}...")
r = requests.post(WP_URL, json=data, headers=headers, timeout=60,
                  proxies={"http": None, "https": None})
print(f"HTTP {r.status_code}")
if r.status_code in (200, 201):
    j = r.json()
    print(f"OK post id={j.get('id')} link={j.get('link')} status={j.get('status')}")
    import re
    imgs = re.findall(r'src="([^"]+)"', j.get("content", {}).get("rendered", ""))
    print(f"img count in rendered: {len(imgs)}")
    for u in imgs[:10]:
        print("  ", u[:110])
    sys.exit(0)
else:
    print(r.text[:1500])
    sys.exit(1)

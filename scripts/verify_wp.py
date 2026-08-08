#!/usr/bin/env python3
"""Verify WordPress post 3006 content."""
import base64, requests

USER = "jowelin"
APP_PASSWORD = "yRR6 WTG6 XWUU kvn3 QTg7 bWpX".replace(" ", "")
auth = base64.b64encode(f"{USER}:{APP_PASSWORD}".encode()).decode()
headers = {"Authorization": f"Basic {auth}"}

r = requests.get("https://aipmclub.com/wp-json/wp/v2/posts/3006",
                 headers=headers, timeout=60, proxies={"http": None, "https": None})
if r.status_code == 200:
    d = r.json()
    print("TITLE:", d["title"]["rendered"][:80])
    print("STATUS:", d["status"])
    print("CATS:", d.get("categories"))
    content = d["content"]["rendered"]
    print("LEN:", len(content))
    print("IMG COUNT:", content.count("<img"))
    print("H2 COUNT:", content.count("<h2"))
    print("HAS GH IMAGES:", "raw.githubusercontent.com" in content)
    print("FIRST IMG:", content[content.find("<img"):content.find("<img")+180] if "<img" in content else "NONE")
else:
    print("HTTP", r.status_code, r.text[:300])

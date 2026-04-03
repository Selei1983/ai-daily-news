#!/usr/bin/env python3
"""
AI 每日新闻生成器
- 搜索最新 AI 产品
- 生成 HTML 页面
- 推送到 Gitea 仓库
"""

import os
import sys
import json
import subprocess
from datetime import datetime
from pathlib import Path

# Gitea 配置
GITEA_URL = "https://git.zjpb.net"
GITEA_USER = "jowelin83"
GITEA_TOKEN = "2882a85f18cdd6fcfcda5a64603dbf5bfa46947d"
REPO_NAME = "ai-daily-news"

# 临时目录
TEMP_DIR = Path("/tmp/ai-news-gen")
REPO_DIR = TEMP_DIR / REPO_NAME

def search_ai_products():
    """搜索最新AI产品（使用 web_search）"""
    # 这里需要调用 OpenClaw 的 web_search 工具
    # 现在返回示例数据
    return [
        {
            "name": "示例产品",
            "category": "AI工具",
            "desc": "示例描述",
            "company": "Example Inc",
            "date": "1天前",
            "tags": ["热门", "AI"]
        }
    ]

def generate_html(products, date_str):
    """生成HTML页面"""
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🔥 AI每日新闻 - {date_str}</title>
    <style>
        /* 复用之前的样式 */
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }}
        .product-card {{ /* 样式 */ }}
    </style>
</head>
<body>
    <!-- 内容 -->
</body>
</html>
"""
    return html

def push_to_gitea(date_str, html_content):
    """推送到Gitea"""
    # 克隆仓库
    repo_url = f"https://{GITEA_TOKEN}@{GITEA_URL.replace('https://', '')}/{GITEA_USER}/{REPO_NAME}.git"
    
    if not REPO_DIR.exists():
        subprocess.run(["git", "clone", repo_url], cwd=TEMP_DIR, check=True)
    
    # 创建日期目录
    date_dir = REPO_DIR / date_str
    date_dir.mkdir(exist_ok=True)
    
    # 写入HTML
    (date_dir / "index.html").write_text(html_content)
    
    # 提交推送
    subprocess.run(["git", "add", "."], cwd=REPO_DIR, check=True)
    subprocess.run(["git", "commit", "-m", f"feat: 添加 {date_str} AI新闻"], cwd=REPO_DIR, check=True)
    subprocess.run(["git", "push", "origin", "main"], cwd=REPO_DIR, check=True)

def main():
    # 获取日期
    today = datetime.now().strftime("%Y-%m-%d")
    
    # 搜索产品
    products = search_ai_products()
    
    # 生成HTML
    html = generate_html(products, today)
    
    # 推送到Gitea
    push_to_gitea(today, html)
    
    print(f"✅ {today} AI新闻已推送")

if __name__ == "__main__":
    main()

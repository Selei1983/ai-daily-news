#!/usr/bin/env python3
"""
每日AI新产品发现 - 生成报告并推送到GitHub
由 OpenClaw cron job 调用，agent 完成
"""
# 这个文件只是说明文档，实际工作由 cron agent turn 完成
#
# 数据源：
# 1. YC 最新投资批次 / YC AI 公司列表
# 2. Product Hunt AI 类别热门
# 3. TechCrunch / VentureBeat AI 新品报道
# 4. GitHub Trending AI 项目
# 5. a16z / Sequoia 等头部基金投资动态
#
# 输出格式：
# - 每日 Markdown 文件：YYYY-MM-DD-ai-daily-digest.md
# - 推送到 GitHub: https://github.com/Selei1983/ai-daily-news
# - 飞书通知：发送摘要到用户
#
# 每个产品包含：
# - 产品名称 + 官网链接
# - 一句话描述
# - 推荐理由（为什么值得关注）
# - 判断依据（投资背景/用户增长/技术创新等）
# - 类别标签（基础设施/应用层/开发工具/垂直场景等）

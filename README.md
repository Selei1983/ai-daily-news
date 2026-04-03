# 🤖 AI Daily News

> 每日AI产品新闻，由 BB01 (OpenClaw Agent) 自动生成

[![GitHub Pages](https://img.shields.io/badge/GitHub-Pages-brightgreen)](https://selei1983.github.io/ai-daily-news/)
[![更新频率](https://img.shields.io/badge/更新-每日20:00-blue)](https://selei1983.github.io/ai-daily-news/)
[![OpenClaw](https://img.shields.io/badge/Powered%20By-OpenClaw-orange)](https://openclaw.ai)

## 📍 访问地址

**在线预览**：https://selei1983.github.io/ai-daily-news/

## 📋 项目简介

这是一个自动化AI新闻聚合项目，每天晚上 20:00 自动：

1. 🔍 搜索最新AI产品（Product Hunt, TechCrunch等）
2. 📝 生成精美的HTML页面
3. 🚀 推送到GitHub Pages和Gitea
4. 📱 发送微信通知

## ✨ 特性

- **自动化**：每天定时更新，无需人工干预
- **多数据源**：Product Hunt、TechCrunch、LabLa、Reuters
- **现代化设计**：
  - 毛玻璃导航栏
  - 渐变配色方案
  - 悬停动画效果
  - 响应式布局
- **多平台同步**：GitHub + Gitea 双仓库
- **智能通知**：微信推送更新结果

## 📅 新闻存档

- [2026-04-03 - 热门AI产品周报](./2026-04-03/index.html)
  - 10款热门产品
  - AI代理治理、多代理协作、中国厂商加速

## 🛠️ 技术栈

- **生成工具**：OpenClaw Agent (BB01)
- **模型**：GLM-5 (z.ai)
- **前端**：纯HTML + CSS（无框架）
- **托管**：GitHub Pages + Gitea
- **自动化**：OpenClaw Cron

## 📊 项目结构

```
ai-daily-news/
├── index.html              # 主页索引
├── README.md               # 项目说明
├── scripts/                # 自动化脚本
│   └── generate_daily.py   # 每日生成脚本
└── YYYY-MM-DD/             # 按日期分类
    └── index.html          # 每日新闻
```

## 🔧 配置

### Gitea 配置
- 仓库：https://git.zjpb.net/jowelin83/ai-daily-news
- 用户：jowelin83

### GitHub 配置
- 仓库：https://github.com/Selei1983/ai-daily-news
- Pages：https://selei1983.github.io/ai-daily-news/

### 定时任务
- 任务ID：`85364fd0-b4eb-4d3d-9736-41f9faa0cdbd`
- 执行时间：每天 20:00 (Asia/Shanghai)
- 模型：zai/glm-5
- 超时：600秒

## 📱 订阅更新

每天晚上 20:00 自动更新，你可以：

1. 访问在线页面：https://selei1983.github.io/ai-daily-news/
2. Watch 本仓库获取更新通知
3. 微信接收自动推送（需配置）

## 🤝 贡献

本项目由 BB01 (OpenClaw Agent) 自动维护，暂不接受手动贡献。

## 📄 许可证

MIT License

---

**🤖 Powered by [OpenClaw](https://openclaw.ai)**

*最后更新：2026-04-03 21:38 (GMT+8)*
# 🤖 AI Daily News

> 每日AI产品新闻，由 BB01 (OpenClaw Agent) 自动生成

[![GitHub Pages](https://img.shields.io/badge/GitHub-Pages-brightgreen)](https://selei1983.github.io/ai-daily-news/)
[![更新频率](https://img.shields.io/badge/更新-每日20:00-blue)](https://selei1983.github.io/ai-daily-news/)
[![OpenClaw](https://img.shields.io/badge/Powered%20By-OpenClaw-orange)](https://openclaw.ai)

## 📍 访问地址

**在线预览**：https://selei1983.github.io/ai-daily-news/

## 📋 项目简介

422产品实验室出品的 AI 产品日报，每个工作日早上 9:00 自动生成：

1. 🔍 多渠道搜集最新AI产品/融资动态（Product Hunt、TechCrunch、GitHub Trending、YC 等）
2. 📝 筛选 5-10 个最值得关注的产品，生成 Markdown 日报
3. 📸 自动截取产品页面截图
4. 🚀 推送到 GitHub + 发布到 WordPress + 微信公众号草稿箱
5. 📱 飞书通知推送结果

### 📂 目录结构
- [`daily/`](./daily/) — 所有日报 Markdown 文件（`YYYY-MM-DD-ai-daily-digest.md`）
- [`list.md`](./list.md) — **推荐入口** 📋 日报索引，含每期洞察摘要和跳转链接

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

👉 查看 [`list.md`](./list.md) 获取完整日报索引（含洞察摘要）

## 🛠️ 技术栈

- **生成工具**：OpenClaw Agent (BB01)
- **模型**：GLM-5 (z.ai)
- **发布渠道**：GitHub + [WordPress](https://aipmclub.com) + 微信公众号（422labs）
- **自动化**：OpenClaw Cron + GLM-5

## 📊 项目结构

```
ai-daily-news/
├── list.md                 # 📋 日报索引（推荐入口）
├── README.md               # 项目说明
├── daily/                  # 所有日报（按日期命名）
│   ├── 2026-05-16-ai-daily-digest.md
│   ├── 2026-05-15-ai-daily-digest.md
│   └── ...
└── scripts/                # 自动化脚本
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
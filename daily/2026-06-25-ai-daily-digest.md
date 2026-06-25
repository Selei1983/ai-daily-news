# 0625日报 | Agent基础设施全面成熟

## 今日洞察

今天的信号指向一个清晰的转折点：**AI Agent 的基础设施层正在全面成熟**。Vercel 发布 Eve 框架（9 天 2500+ star），用「文件系统即框架」的理念把 Agent 开发标准化；shadcn-labs 推出 agentcn（shadcn/ui for agents），让 Agent 的 UI 组件可以复制粘贴；Mindstone 的 Rebel 做到了 Agent 自动记忆哪个模型适合哪个任务；Lelu 开源了 Agent 专用的授权引擎，让每个动作都有权限边界。再加上 iart.ai 的 50 个运动图形技能包，以及 Plaudit Labs 开辟的「AI 推荐优化」新品类——**2026 年中，Agent 生态的每一层（框架、UI、编排、权限、技能、获客）都有人填上了。这意味着做 Agent 产品的门槛正在快速降低，但也意味着纯 Agent 套壳的窗口期即将关闭**。

---

## 1. [Hang Ten Systems](https://hnt.ai/)（融资 / AI 企业服务）

![Hang Ten Systems](/tmp/daily-screenshots/hang-ten-systems.png)

🔗 链接：[官网](https://hnt.ai/) | [TechCrunch 报道](https://techcrunch.com/2026/06/24/former-infosys-chief-has-a-new-startup-that-wants-to-challenge-the-it-services-world/)

**融资信息**：**3200 万美元种子轮**，由 **Mayfield** 领投，**Aramco Ventures** 战略投资，天使投资人参与。董事会成员包括 **Yahoo 联合创始人 Jerry Yang**。

**做什么的**：用 AI 持续构建、修改和运营企业软件——直接挑战价值数千亿美元的 IT 外包服务行业。创始人 **Vishal Sikka** 是 Infosys 前 CEO（任期内推动 Infosys 从传统外包向数字化转型），此前在 SAP 工作 12 年，深度参与企业软件架构演进。

**为什么值得关注**：
- 这是**第一次有 IT 服务行业 insider 用 AI 从内部颠覆这个行业**。Sikka 不是硅谷创业者猜「IT 服务能不能被 AI 替代」，而是这个行业的前 No.1 亲自下场验证。
- 已有客户包括 **Siemens Gamesa Renewable Energy** 和 **Fresenius**，成立仅一个月就有真实收入。
- 核心团队来自 SAP、Infosys、VianAI（Sikka 此前的 AI 创业，融了 $190M），工程交付能力极强。
- 对创业者的启发：**AI 颠覆传统服务业的时机已到，但赢家可能是最懂行业的人，而不是最懂 AI 的人**。

**类比参考**：**「IT 外包行业的 Stripe / AI 原生的 Infosys」**

---

## 2. [Vercel Eve](https://vercel.com/eve)（开源 / Agent 框架）

![Vercel Eve](/tmp/daily-screenshots/vercel-eve.png)

🔗 链接：[GitHub](https://github.com/vercel/eve) | [官网](https://vercel.com/eve)

**融资信息**：Vercel（估值 $32 亿）官方开源项目，Apache 2.0 协议。GitHub **2,536 star**，190 fork，9 天内爆发增长。

**做什么的**：文件系统优先的 AI Agent 框架——Agent 的所有能力（指令、工具、技能、频道、定时任务）都以约定文件的方式存在于目录中。`npx eve@latest init my-agent` 一键创建可运行的 Agent 骨架，支持 Slack/Discord/HTTP 频道和 cron 定时任务。

**为什么值得关注**：
- **Vercel 的 Next.js 定义了前端开发的标准范式，Eve 可能会定义 Agent 开发的标准范式**。文件系统即框架的理念让 Agent 项目可检查、可扩展、可运维。
- 内置文档随包发布（`node_modules/eve/docs`），coding agent 可以直接本地读取——这是一个非常聪明的设计，让 AI 辅助开发 Agent 变得无缝。
- TypeScript 原生 + Zod 类型校验，工具定义极简（`defineTool` 一行搞定），对前端开发者极为友好。
- 对创业者的启发：**Agent 框架赛道正在从「SDK 集成」走向「约定优于配置」，类似 Next.js 之于 React**。

**类比参考**：**「Agent 界的 Next.js / Vercel 的 Agent 版 React Framework」**

---

## 3. [Mindstone Rebel](https://www.producthunt.com/products/mindstone-rebel)（产品发布 / Agent 编排）

![Mindstone Rebel](/tmp/daily-screenshots/mindstone-rebel.png)

🔗 链接：[Product Hunt](https://www.producthunt.com/products/mindstone-rebel) | [VentureBeat 报道](https://venturebeat.com/orchestration/your-enterprise-ai-agents-should-automatically-remember-which-model-is-right-for-which-task-mindstone-built-the-capability-with-rebel)

**融资信息**：伦敦 AI 转型初创公司 Mindstone 出品，具体融资未披露。VentureBeat 专题报道评价为「最 promising 的 Agent 编排平台之一」。

**做什么的**：企业级 AI Agent 工作空间——核心能力是**自动记忆哪个模型适合哪类任务**。Agent 在执行过程中学习任务与模型的匹配关系，下次遇到类似任务自动路由到最优模型。支持「先问再做」的安全交互模式。

**为什么值得关注**：
- 解决了多模型时代企业最痛的问题：**不知道什么任务该用什么模型，手动切换太低效**。Rebel 让模型选择变成 Agent 的自动行为，而不是人的决策。
- 「Ask First」设计理念——Agent 在不确定时会主动请求人类确认，而不是盲目执行。这是企业采用 AI Agent 的关键信任门槛。
- 对创业者的启发：**Agent 编排的价值不在「连接多个模型」，而在「学习什么任务需要什么模型」——这是一个数据飞轮**。

**类比参考**：**「Agent 版 Rubrik（自动路由）+ 带护栏的 LangChain」**

---

## 4. [agentcn](https://agentcn.run)（开源 / Agent UI 组件）

![agentcn](/tmp/daily-screenshots/agentcn.png)

🔗 链接：[GitHub](https://github.com/shadcn-labs/agentcn) | [官网](https://agentcn.run)

**融资信息**：shadcn-labs 出品（shadcn/ui 作者），MIT 协议。GitHub **250 star**，13 fork，8 天内新建。

**做什么的**：**shadcn/ui 的 Agent 版**——为构建 AI Agent 界面提供可复制粘贴的 React 组件库。聊天窗口、工具调用展示、Agent 状态指示器、流式输出渲染等 Agent UI 常用组件，直接 copy-paste 到项目中。

**为什么值得关注**：
- shadcn/ui 已经成为 React 生态最受欢迎的 UI 方案之一（80K+ star），**agentcn 可能会成为 Agent UI 的默认标准**。
- 核心洞察精妙：做 Agent 产品的开发者 80% 的 UI 工作是重复的（聊天框、消息流、工具调用卡片），与其每次重写不如标准化。
- 对创业者的启发：**Agent 时代的「卖铲子」机会不仅在 infra，UI 组件层同样有巨大的标准化需求**。

**类比参考**：**「shadcn/ui 的 Agent 版 / Agent 界面的 Tailwind UI」**

---

## 5. [Lelu](https://github.com/Lelu-ai/lelu)（开源 / Agent 安全）

![Lelu](/tmp/daily-screenshots/lelu.png)

🔗 链接：[GitHub](https://github.com/Lelu-ai/lelu) | [PyPI](https://pypi.org/project/lelu-agent-auth-sdk/)

**融资信息**：开源项目（MIT），GitHub **37 star**，提供 Python SDK 和 npm 包。HN Show HN 首发获得关注。

**做什么的**：AI Agent 专用的开源授权引擎——每个 Agent 动作都经过置信度评估，低置信度动作自动触发人工审核，支持 Policy-as-Code 和完整审计日志。内置 **Prompt Injection 检测**。

**为什么值得关注**：
- Agent 安全是一个**被严重低估的创业赛道**。随着 Agent 被授予越来越多的系统权限（文件操作、API 调用、支付），权限控制和审计成为刚需。
- 产品设计精准：不是做通用安全，而是专注「**Agent 动作授权**」这一个点——置信度评分 → 自动门控 → 人工审核 → 审计日志，形成完整链路。
- 对创业者的启发：**Agent 治理（governance）是下一个要爆发的品类，类似 SaaS 时代的 Okta/IAM**。每个使用 Agent 的企业都需要这种中间层。

**类比参考**：**「Agent 版 Okta / AI 时代的 SentinelOne——但聚焦权限治理」**

---

## 6. [iart.ai Motion Skills](https://github.com/iart-ai/motion-skills)（开源 / Agent 技能扩展）

![iart.ai Motion Skills](/tmp/daily-screenshots/motion-skills.png)

🔗 链接：[GitHub](https://github.com/iart-ai/motion-skills) | [官网](https://iart.ai)

**融资信息**：iart.ai 出品，开源（协议待确认）。GitHub **169 star**，14 个可安装技能包。

**做什么的**：50 个开源技能，教 AI coding agent 制作运动图形、动画和视频——包括动态排版、数据可视化、TikTok/Reels 格式内容、WebGL 和 Manim 动画。分为 14 个可安装包，直接在 Claude Code / Cursor 等 agent 中使用。

**为什么值得关注**：
- **开辟了 Agent 技能市场（Skill Market）的新品类**。之前 Agent 技能主要围绕代码/文档，Motion Skills 把 Agent 的能力扩展到了创意内容生产。
- 产品形态极为创新：不是做一个 AI 视频工具，而是**把视频/动画能力变成 coding agent 的插件**，让开发者在编码环境中直接生成视觉内容。
- 50 个技能 + 14 个安装包的模块化设计，让用户可以按需选用，降低了采用门槛。
- 对创业者的启发：**Agent 技能市场正在从「通用工具」走向「垂直创意工具」，每个内容格式（视频、动画、PPT）都可能有自己的技能包**。

**类比参考**：**「Agent 版 Adobe After Effects 插件市场 / 可安装的 Sora 能力包」**

---

## 7. [Plaudit Labs](https://plauditlabs.com)（产品发布 / AI 搜索优化）

![Plaudit Labs](/tmp/daily-screenshots/plaudit-labs.png)

🔗 链接：[官网](https://plauditlabs.com) | [HN 讨论](https://news.ycombinator.com/item?id=48666441)

**融资信息**：未披露。HN Show HN 首发即获得讨论。

**做什么的**：**AI 推荐优化工具**——输入你的网站，立即检测 ChatGPT、Perplexity 等 AI 助手是否会推荐你的产品/服务。提供可操作的建议来提升 AI 可见度。免费开始，无需注册。

**为什么值得关注**：
- 开辟了一个全新品类：**Answer Engine Optimization（AEO）**，即「让 AI 推荐你」。当用户从 Google 搜索转向 ChatGPT 提问，传统 SEO 正在失效。
- 创始人在 HN 上分享：发现自己一个产品从 ChatGPT 获得大量流量，另一个却完全没有——这说明 AI 推荐不是随机的，而是有规律可优化的。
- 产品设计极为增长导向：免费 + 即时结果 + 无需注册，典型的 PLG 入口。
- 对创业者的启发：**当买家从「搜索」转向「提问」，获客渠道的底层逻辑正在改变。谁能帮企业在 AI 回答中获得推荐位，谁就是 AI 时代的 SEO 公司**。

**类比参考**：**「AI 时代的 SEMrush / ChatGPT 版 SEO 工具」**

---

## 值得重点跟踪的 3 个信号

1. **Agent 基础设施层已经填满**：Vercel Eve（框架）、agentcn（UI 组件）、Mindstone Rebel（编排）、Lelu（权限）、Motion Skills（技能包）——Agent 开发的每一层都有标准化方案了。**做 Agent 产品的门槛正在急剧降低，但纯套壳的窗口在关闭**。

2. **IT 服务行业面临 AI 原生颠覆**：Hang Ten Systems 用 $32M 种子轮和 Infosys 前 CEO 的背景，宣告 AI 不是在帮 IT 外包行业提效，而是要重新定义这个行业。**2 万亿美元的全球 IT 服务市场，是 AI 最大的待颠覆行业之一**。

3. **AEO（Answer Engine Optimization）成为新赛道**：Plaudit Labs 验证了一个真实痛点——企业不知道 AI 助手是否推荐自己。当 ChatGPT/Perplexity 成为新的搜索入口，**「AI 可见度」正在成为新的营销刚需**。

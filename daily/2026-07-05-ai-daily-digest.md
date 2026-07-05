# 0705日报 | 石油美元入局AI基建，隐私AI赛道跑出独角兽

## 今日洞察

今天的五个字：「钱在换方向。」

**Together AI 以 $8 亿 C 轮刷新 AI Neocloud 纪录，领投方是沙特阿美（Aramco Ventures）**——这是石油美元大规模进入 AI 基建的标志性事件。当一家国家石油公司的风投部门掏出 8 亿美金押注 GPU 租赁生意，信号再清晰不过：**AI 算力正在从「科技公司的成本项」变为「国家主权级的战略资产」**。

与此同时，Venice AI 以 $65M A 轮拿到独角兽估值（$10 亿），创始人 Erik Voorhees（ShapeShift 创始人，比特币早期布道者）做了一个完全相反的赌注：**不是更开放，而是更隐私。** 200+ 模型、零数据留存、TEE 加密、端到端匿名——且已盈利（$70M ARR，300 万+ 活跃用户）。当所有人都在卷模型能力和 Agent 自主性时，Venice 证明「隐私」本身就是一条可行的差异化路径。

Neo 则展示了第三种可能性：**不用 VC 的钱。** 印度连续创业者 Bhavin Turakhia 自掏 $3000 万，从零打造 AI 原生的企业工作平台，直接对标 Google Workspace / Office 365。他拒绝 VC 的理由是「做的是长期产品，不需要被增长压力扭曲判断」。

三个案例合在一起，回答了当前 AI 创业者最核心的问题：**做 AI 基建（Together）、做隐私差异化（Venice）、做长期产品（Neo）——三条路都能走通，但每条路需要的资金策略、产品定位和退出预期完全不同。**

产品侧，Agent 生态的基础设施层继续加速：Banger Mail 把「AI Agent 参与团队协作」做到产品级——Agent 干活、人类 review，像 GitHub PR 一样的工作流；Mcpsnoop 给 MCP 协议做 Wireshark；ctx 让你的编码 Agent 历史可搜索；Token Diet 帮编码 Agent 省 31% Token 费用。**Agent 不仅在工作，还需要被调试、被搜索、被优化——这些「管理 Agent」的工具正在成为一个独立品类。**

---

## 1. [Together AI](https://www.together.ai/)（融资 / AI Neocloud）

![Together AI](/tmp/daily-screenshots/together-ai.png)

🔗 链接：[官网](https://www.together.ai/) | [TechCrunch](https://techcrunch.com/2026/07/01/together-ai-raises-800m-series-c-from-aramco-ventures-at-8-3b-valuation/)

**融资信息**：**$8 亿 C 轮**，估值 **$83 亿**。领投方 **Aramco Ventures**（沙特阿美风投），跟投方包括 Vista Equity Partners、General Catalyst、Emergence Capital、Nvidia、March Capital、和硕（Pegatron）、SentinelOne S Ventures 等。累计融资超 $15 亿。

**做什么的**：AI 云服务商（Neocloud），提供 Nvidia GPU 集群租赁和开源 AI 模型托管。2026 年上季度年化合同金额超 **$11.5 亿**。客户包括 Cursor、Cognition（Devin 背后公司）、Decagon 等。

**为什么值得关注**：

- **石油美元正式入局 AI 基建**。Aramco Ventures 领投 8 亿美金，是全球主权财富基金对 AI 基础设施最大的一笔单投。沙特在赌 AI 算力需求 10 年不会退潮——这对所有 AI 创业者都是宏观层面的利好信号。
- $8.3B 估值对应 ~7x 年化合同收入（$11.5 亿），比传统云厂商（AWS 3-4x）贵不少，说明**资本市场愿意为「AI 原生云」支付溢价**。
- Nvidia 跟投 + 和硕（全球最大电子代工厂之一）参与，说明整个 GPU 供应链都在下注 Together AI 的分发能力。
- 对创业者的启发：**AI 基础设施的「国家化」才刚刚开始。中东、东南亚、拉美的主权基金都会陆续入场。如果你的产品需要重资产投入，考虑主权财富基金作为战略投资人。**

**类比参考**：**「AI 初创版 AWS / 带 GPU 的 Cloudflare」**

---

## 2. [Venice AI](https://venice.ai/)（融资 / 隐私优先 AI）

![Venice AI](/tmp/daily-screenshots/venice-ai.png)

🔗 链接：[官网](https://venice.ai/) | [TechCrunch](https://techcrunch.com/2026/07/01/venice-ai-raises-65m-series-a-at-1b-valuation-for-private-uncensored-ai-platform/)

**融资信息**：**$6500 万 A 轮**（首次外部融资），估值 **$10 亿**（新晋独角兽）。领投方 **Dragonfly**（加密领域顶级 VC），跟投方包括 Coinbase Ventures、North Island Ventures 等。

**做什么的**：隐私优先、无审查的 AI 平台——提供 200+ AI 模型（开源 + 闭源）的访问权限。关键技术特性：所有用户输入经过加密、客户端解密、通过外部代理路由、**零数据留存**。提供文本、图像、视频、音乐、语音、代码生成和 Agent 构建能力。**已盈利**，年化收入超 **$7000 万**，300 万+ 活跃用户，日均 170 万次 API 调用。

**为什么值得关注**：

- **隐私即差异化，这是一个被严重低估的策略。** 当 OpenAI、Anthropic、Google 都在卷模型能力时，Venice 的定位是「不看你数据的 AI 平台」。对注重隐私的企业客户和个人用户来说，这个卖点极具穿透力。
- 创始人 **Erik Voorhees** 的身份本身就是品牌——ShapeShift 创始人、比特币早期布道者。他从加密货币领域跨入 AI，证明了隐私技术人才在 AI 时代的稀缺价值。
- **加密 VC（Dragonfly）+ 交易所 VC（Coinbase Ventures）共同押注**——说明加密圈认为 AI 和加密的交集是真实的。Venice 的「无审查」定位背后是去中心化精神。
- 对创业者的启发：**当所有人都往一个方向冲时，往反方向走也是可行的。隐私、无审查、匿名——这些「政治不正确」的定位在大量用户群体中是真实的刚需。且因为大厂不敢做，这是创业公司的天然护城河。**

**类比参考**：**「DuckDuckGo版的ChatGPT / 加密世界版的 Hugging Face」**

---

## 3. [Neo](https://neo.xyz/)（产品发布 / AI 原生企业工作平台）

![Neo](/tmp/daily-screenshots/neo.png)

🔗 链接：[官网](https://neo.xyz/) | [TechCrunch](https://techcrunch.com/2026/07/01/indian-tech-billionaire-bhavin-turakhia-is-building-an-ai-native-workspace-that-could-replace-google-microsoft/)

**融资信息**：创始人 **Bhavin Turakhia** 自掏 **$3000 万**（个人出资），不拿 VC。公司设于印度班加罗尔，约 45 名员工。

**做什么的**：AI 原生企业工作平台，融合项目管理、文档、文件存储和 AI 功能。**模型无关**——用户可在不同 AI 模型间自由切换。4 月内部启动，计划年底扩至 100 人。

**为什么值得关注**：

- **用 VC 的钱做增长 vs. 用自己的钱做产品**——Turakhia 选择了后者。他拒绝 VC 的理由值得每位创始人思考：VC 追求 10 倍回报和快速增长，而他要打造的是一款可能 5-10 年才能成熟的长期产品。**慢就是快。**
- 他的创业履历本身就是最好的 BP：Directi（$9000 万被 Endurance 收购）→ Radix（全球最大新顶级域注册局之一）→ Zeta（AI 银行平台，$20 亿+ 估值）。这是第三次做平台级产品。
- 产品思路极为清醒：不是试图替代某个工具，而是**替代整个工作套件**。项目管理+文档+文件存储+AI——对标 Google Workspace + Office 365 + Notion + Asana 的集合体。
- 对创业者的启发：**AI 时代最大的机会不是做更好的工具，而是做更好的「工作环境」。当所有应用都有 AI 入口，真正需要的是一个**协调所有 AI 的工作操作系统**。**

**类比参考**：**「印度版 Notion + Asana + AI / AI 原生的 Google Workspace」**

---

## 4. [Banger Mail](https://www.bangermail.com/)（新产品 / AI Agent 协作邮箱）

![Banger Mail](/tmp/daily-screenshots/banger-mail.png)

🔗 链接：[官网](https://www.bangermail.com/) | [Product Hunt](https://www.producthunt.com/products/banger-mail)

**融资信息**：7 月 1 日上 Product Hunt，来自 Much Better Apps（Tiago Loureiro & Luiz Gualberto）。原生 macOS 应用。

**做什么的**：为团队和 AI Agent 设计的共享邮箱——将自定义域名、Gmail、Google Workspace 统一到一个原生应用中。AI Agent 可以协作**分类、起草回复、打标签**，但每项 Agent 操作必须通过**人类 review** 后才能发出。

**为什么值得关注**：

- **Agent 参与团队协作的「PR 模式」**——Banger Mail 最精妙的设计是：Agent 的操作像 GitHub Pull Request 一样需要人工审核。这解决了 AI 引入团队时最大的信任问题：「不是不让你做，但你做了我要看得见，且我能批准或拒绝。」**这是 AI Agent 进入企业工作流的正确姿势。**
- 产品定位精准：不是替代邮件，而是让邮件**更适合团队协作**。团队共享地址（support@、sales@、marketing@）天然就需要多人协作 + AI 辅助，Banger 在这个场景中找到了完美的 PMF。
- 原生 macOS + 离线优先 + 快速搜索——这些细节意味着创始团队是懂「用户体验」的，不是 AI 吹出来的花架子。
- 对创业者的启发：**Agent 进入企业的最佳方式是「辅助」而不是「替代」，且每一步都要可审计、可撤回。把 Agent 当作一个需要代码 review 的 junior 工程师来设计产品。**

**类比参考**：**「Superhuman 做团队版 / AI Agent 版的 Front」**

---

## 5. [Mcpsnoop](https://github.com/kerlenton/mcpsnoop)（开源 / MCP 调试工具）

![Mcpsnoop](/tmp/daily-screenshots/mcpsnoop.png)

🔗 链接：[GitHub](https://github.com/kerlenton/mcpsnoop) | [HN 讨论](https://news.ycombinator.com/item?id=48685323)

**融资信息**：开源项目（MIT），HN **61 分**，GitHub **182 star**。活跃开发中。

**做什么的**：MCP（Model Context Protocol）的透明代理 + TUI——像 Wireshark 一样实时展示 AI 客户端和 MCP 服务器之间的每一次真实工具调用。支持从 Flipper 到 VS Code 再到 Claude Desktop 的任何 MCP 客户端。

**为什么值得关注**：

- **MCP 是 Agent 生态的 HTTP 协议**——如果类比 Web 时代，MCP 就像 HTTP，而 Mcpsnoop 就是 Wireshark。当 MCP 成为 Agent 调用工具的通用标准，调试 MCP 就是 Agent 时代的刚需。
- 产品设计极为「Unix 哲学」：透明代理模式，无需修改客户端或服务器配置，启动即用。`brew install mcpsnoop` 一键安装。**这是经典的工具思维——做一件事，做到极致。**
- 开发者正在更新中（4 小时前还有新 commit），说明了 MCP 生态的活跃度。
- 对创业者的启发：**Agent 协议层的工具需求正在爆发。MCP、A2A、Figma API——每个协议都需要自己的调试、监控、安全审计工具。这些工具可能不大，但每个都是稳定现金牛。**

**类比参考**：**「Wireshark for MCP / Agent 版的 tcpdump」**

---

## 6. [ctx](https://github.com/ctxrs/ctx)（开源 / Agent 历史搜索）

![ctx](/tmp/daily-screenshots/ctx.png)

🔗 链接：[GitHub](https://github.com/ctxrs/ctx) | [HN 讨论](https://news.ycombinator.com/item?id=48677218)

**融资信息**：开源项目，HN **65 分**，GitHub **627 star**，42 Branches，活跃开发。

**做什么的**：搜索本地编码 Agent 历史——支持 Claude Code（~/.claude/projects）、Codex（~/.codex/projects）等 Agent 的历史记录索引和全文搜索。自带 Claude 插件和 Cursor 插件，支持智能搜索意图识别。

**为什么值得关注**：

- **解决了编码 Agent 用户最痛的痛点之一**：你让 Agent 两周前改了一段代码，记不得具体改了啥。现在你有了 `ctx search "那个bug fix"`。**这是编码 Agent 的「Google Desktop Search」。**
- 跨 Agent 支持（Claude Code + Codex + Cursor + Windsurf + Cline）是关键差异化——**单一 Agent 的历史搜索已经有人在做了，但跨 Agent 的统一搜索引擎是全新的需求。**
- 产品思路值得借鉴：不是做一个新 Agent，而是**做 Agent 的索引层**。随着 Agent 使用频率增加，历史数据的管理、搜索和复用会成为越来越关键的基础设施。
- 对创业者的启发：**信息管理是 Agent 时代的核心痛点。Agent 产出了大量代码、决策记录、对话历史，但「怎么找到之前的东西」完全没有好的解决方案。这可能是 Notion 级别的机会。**

**类比参考**：**「Agent 历史的 Google Desktop / macOS Spotlight for AI Coders」**

---

## 7. [Token Diet](https://github.com/Kulaxyz/token-diet)（开源 / Agent Token 优化）

![Token Diet](/tmp/daily-screenshots/token-diet.png)

🔗 链接：[GitHub](https://github.com/Kulaxyz/token-diet)

**融资信息**：开源项目，GitHub **456 star**，一天内快速增长。支持 Claude Code、Codex、Cursor、Windsurf、Cline。

**做什么的**：编码 Agent 的「全时段 Token 效率 Skill」——在 Agent 的整个会话过程中（回复、文档、测试、代码、上下文、工具使用）自动精简 Token 使用。平均节省 **~31% 费用**，根据任务类型优化幅度从 17% 到 54% 不等。

**为什么值得关注**：

- **直接解决编码 Agent 的第二大痛点：成本。** 第一大痛点是质量，第二大就是 Token 账单。Token Diet 本质上是一个**零侵入的成本优化层**——安装后 Agent 不知不觉地少用 1/3 的 Token。
- 「Skill」化的设计思路很聪明：不是改 Agent 的代码，而是作为一个**可插拔的优化层**。类似浏览器装广告屏蔽插件。
- 有 benchmark 数据验证（-17% 到 -54%），不是空口说省钱。这种量化验证在开源项目中极为稀缺。
- 对创业者的启发：**Agent 经济的「降低成本层」是一个大市场。当 Agent 使用量每季度翻倍，任何能降低 30% API 成本的工具都有百亿市场。除了 Token 优化，还有模型路由、缓存层、批量推理——每个方向都值得做。**

**类比参考**：**「Agent 版的 Adblock / API 成本版的 Green Software」**

---

## 值得重点跟踪的 3 个信号

1. **主权资本正在重新定义 AI 基建的玩法。** Together AI 的 $8 亿 C 轮由沙特阿美领投，标志着石油美元正式进入 AI 算力军备竞赛。这不仅仅是融资——这是地缘政治层面的转移：**AI 算力正在从「硅谷资产」变成「主权资产」。** 对创业者意味着：中东主权基金将成为 AI 公司融资的新增重要来源，尤其是在重资产模式（芯片、数据中心）中。

2. **隐私定位是一条被低估的差异化路径。** Venice AI 以独角兽估值完成 A 轮，已盈利 $70M ARR——证明了「隐私优先」不是一个 niche 定位，而是一个可持续的商业模式。当大厂被合规和审查束缚手脚时，隐私定位为创业公司提供了天然壁垒。**在 AI 时代，「不收集数据」可能是比「收集最多数据」更好的商业策略。**

3. **Agent 管理工具正在成为一个独立品类。** Mcpsnoop（调试 MCP）、ctx（搜索 Agent 历史）、Token Diet（优化 Agent 成本）——这三个产品各自切入了 Agent 使用生命周期中的一个环节。**不是 Agent 本身，而是「管理 Agent」的工具。** 类比 Web 时代：Web 本身值多少钱？但 hosting、CDN、analytics、security 加起来是万亿美元市场。**Agent 时代的管理工具才刚刚开始。**

---

*统计信息：收录 7 个产品 | 融资总额 $8.65 亿 | 覆盖赛道：AI 基建、隐私 AI、企业协作、Agent 工具链、开源*

# 0701日报 | AI推理芯片与编码Agent吸金

## 今日洞察

今天释放了一个极为明确的信号：**AI 的钱正在从「训练」加速流向「推理」和「垂直执行」。** Etched（AI 推理芯片）以 $5B 估值宣布 $1B 订单，累计融资 $800M——Andrej Karpathy、Geoffrey Hinton、Fei-Fei Li 全部入场。EquiLibre Technologies（前 DeepMind 扑克 AI 团队）以 $500M 估值完成 Series A，用强化学习跑真金白银的量化交易，与 Tower Research 合作每日交易数十亿。Chamath Palihapitiya 的 8090 Labs 拿下 $135M Series A 做企业级 AI 编码 Agent，亲自出任 CEO。

同时，Agent 经济的基础设施层正在成型：OKX 推出 Agent 市场，让 AI Agent 互相雇佣、结算；Arena（AI 榜单）8 个月做到 $100M ARR，证明「AI 评测」是一门大生意；Pocket 以 $129 的硬件 + 零订阅模式卖出 13 万台；Proception 刚和 Tesla 和解就拿到 $11M 做 robot hand。**结论：推理芯片、编码 Agent 和 Agent 经济基础设施，是当下资本最集中的三条赛道。**

---

## 1. [Etched](https://www.etched.com/)（融资 / AI 推理芯片）

![Etched](/tmp/daily-screenshots/etched.png)

🔗 链接：[官网](https://www.etched.com/) | [TechCrunch 报道](https://techcrunch.com/2026/06/30/nvidia-competitor-etched-hits-5b-valuation-1b-in-sales-for-ai-chip/)

**融资信息**：累计融资 **$800M**，最新一轮 $500M（2025年12月关闭），估值 **$50 亿**。投资方包括 VentureTech Alliance、Jane Street、Hudson River Trading、Two Sigma、Ribbit Capital、Stripes。天使投资人：**Andrej Karpathy、Geoffrey Hinton、Fei-Fei Li、Arthur Mensch、Scott Wu**。Stanley Druckenmiller、Peter Thiel 也在 cap table 中。

**做什么的**：设计专用 AI 推理芯片（Sohu），将芯片 + 定制机架 + 软件打包成「前沿推理集群」，帮助前沿模型跑推理更快、更便宜、更省电。TSMC 已成功流片。

**为什么值得关注**：
- **$1B 合同订单**——这不是「可能的市场」，而是已签约的真金白银。当推理成为 AI 公司最大的成本中心时，任何能降低推理成本的方案都会被疯狂抢购。
- **投资方阵容是最强信号**：Jane Street、Hudson River Trading、Two Sigma——全球最精明的量化基金都在投。天使名单中 Karpathy + Hinton + Fei-Fei Li = AI 学术界 + 工业界的天花板组合。
- 创始人 Gavin Uberti 和 Robert Wachen 都是哈佛辍学生，2022 年创立。从「大学宿舍到 $50 亿估值」只用了 4 年。
- 对创业者的启发：**推理是 AI 的后半场。训练芯片（Nvidia）的战已经打完，推理芯片的战才刚开始。专用芯片 > 通用芯片，在推理领域这个定律正在被验证**。

**类比参考**：**「推理版的 Nvidia / AI 芯片界的 Cerebras」**

---

## 2. [EquiLibre Technologies](https://equilibre.ai/)（融资 / AI 量化交易）

![EquiLibre](/tmp/daily-screenshots/equilibre.png)

🔗 链接：[官网](https://equilibre.ai/) | [TechCrunch 报道](https://techcrunch.com/2026/06/30/the-deepmind-trio-who-built-a-poker-ai-are-now-making-money-for-quant-hedge-funds/)

**融资信息**：**Series A**（金额未披露），估值 **$5 亿**。由 **Creandum** 领投——这是该 VC 历史上最大单笔投资。

**做什么的**：用强化学习做量化交易。三位前 DeepMind 研究员（含 CEO Martin Schmid）曾打造击败人类的扑克 AI，现在将同样的 RL 技术应用于股市。与 Tower Research Capital 合作，每天在标普 500 和纳斯达克交易数十亿美金，自 2025 年以来「每月正收益，零负月」。

**为什么值得关注**：
- **从扑克到交易**是 RL 最自然的商业化路径：评分标准极为清晰——赚了多少钱。不需要人工标注数据，不需要主观评估，市场直接给出 reward。
- 合作模式极聪明：不是自己开基金，而是与 Tower Research（顶级量化公司）合作提供技术。**技术授权 > 自己下场**，风险更低，规模化更快。
- Creandum 是 Spotify、Klarna 的早期投资人，他们押下史上最大单注说明信心极强。
- 对创业者的启发：**RL 在游戏中的成功可以平移到任何有明确评分标准的领域。金融是第一个，接下来可能是供应链优化、能源调度、广告竞价**。

**类比参考**：**「DeepMind 版的 Renaissance Technologies / RL 版的 Tower Research」**

---

## 3. [8090 Labs](https://8090labs.com/)（融资 / 企业级 AI 编码）

🔗 链接：[TechCrunch 报道](https://techcrunch.com/2026/06/29/chamath-palihapitiya-raises-135m-series-a-for-his-ai-coding-startup-takes-ceo-role/)

**融资信息**：**$1.35 亿 Series A**。由 **Salesforce Ventures** 领投，WndrCo、Craft Ventures（David Sacks）、The Production Board（David Friedberg）、Launch（Jason Calacanis）跟投。天使：Palo Alto Networks CEO Nikesh Arora、Quora CEO Adam D'Angelo。

**做什么的**：AI 编码 Agent「Software Factory」，专为企业编程团队设计，强调生产级代码质量（而非 vibe-coded 原型），提供审计追踪等企业级管控。

**为什么值得关注**：
- **Chamath 亲自出任 CEO**——这位 All-In Podcast 主持人和 Social Capital 创始人说「自离开 Facebook 以来，一直在等待这样的时刻回归全职运营」。当一线 VC 从「投资人」变回「创始人」，信号极为强烈。
- 产品定位精准：不是做通用编码助手，而是**专攻企业级代码**——审计追踪、合规管控、生产质量。这正好击中大企业用 AI 编码时最大的顾虑。
- 融资结构本身就是信号：Salesforce Ventures 领投意味着企业渠道的即时接入。Craft Ventures（David Sacks）+ All-In 主持人集体下注。
- 对创业者的启发：**AI 编码的下一个战场不是「能不能写代码」，而是「能不能在企业环境里安全地写代码」。合规和审计是进入大企业的入场券**。

**类比参考**：**「企业版 Cursor / 合规版 GitHub Copilot」**

---

## 4. [Arena](https://lmarena.ai)（商业模式 / AI 评测）

![Arena](/tmp/daily-screenshots/arena.png)

🔗 链接：[Arena 榜单](https://arena.ai/leaderboard) | [TechCrunch 报道](https://techcrunch.com/2026/06/29/arena-the-ai-leaderboard-everyone-uses-is-now-a-100m-business/)

**融资信息**：起源于 UC Berkeley 2023 年的研究项目。商业化仅 8 个月，已达 **$1 亿年化收入**（ARR）。

**做什么的**：运营全球最受欢迎的 AI 模型性能排行榜（1000 万+ 用户评测），并向模型实验室和企业提供深度性能分析服务（AI Evaluations）。

**为什么值得关注**：
- **从研究项目到 $100M ARR 只用了 8 个月**——这可能是 2026 年最快的商业化路径。免费的众包榜单（获客）→ 付费的企业深度分析（变现），堪称教科书级的 PLG（Product-Led Growth）。
- 竞争对手 Yupp（另一个 AI 榜单）已经在 3 月关闭——**这个赛道有极强的赢家通吃效应**。社区一旦形成规模，新进入者极难追赶。
- CEO Anastasios Angelopoulos 说「很多人甚至不知道我们在赚钱」——这说明免费产品的品牌效应远超付费服务。
- 对创业者的启发：**「评测」本身可以是一个大生意。任何存在选择困难的品类（AI 模型、SaaS 工具、云服务），谁拥有最权威的评测平台，谁就掌握流量入口**。

**类比参考**：**「AI 版 Niche / G2 / AI 模型的 Michelin Guide」**

---

## 5. [Acti](http://openacti.com)（新产品 / AI 键盘 Agent）

![Acti](/tmp/daily-screenshots/acti.png)

🔗 链接：[官网](http://openacti.com) | [iOS](https://apps.apple.com/us/app/acti-agentic-keyboard/id6745523677) | [TechCrunch 报道](https://techcrunch.com/2026/06/30/acti-puts-ai-agents-directly-into-your-smartphone-keyboard/)

**做什么的**：新加坡初创公司推出的 AI Agent 键盘（iOS + Android），不只是预测下一个词，还能在所有 app 中代你执行操作——推荐餐厅、查股票、翻译、生成回复。由 Google Gemini 驱动。

**为什么值得关注**：
- **产品形态极为大胆**：不做一个新的 AI app，而是**占领你已有的输入入口**。键盘是手机上使用频率最高的「软件」，每个 app 都离不开它。这意味着 Acti 不需要用户切换应用就能提供 AI 能力。
- 「键盘作为 Agent 入口」的思路解决了一个核心问题：用户不想为了用 AI 而打开另一个 app。**AI 应该在你已经工作的地方出现，而不是要求你去它那里**。
- 跨 app 的上下文层设计精妙：Acti 能看到你在微信聊什么、在邮件写什么、在搜索什么——这是构建个性化 AI 助手最丰富的数据源（当然也引发隐私问题）。
- 对创业者的启发：**最高频的入口往往不是新场景，而是已经存在的「系统级」界面。键盘、通知栏、分享菜单——这些都是 AI Agent 的潜在入口**。

**类比参考**：**「Agent 版的 SwiftKey / 键盘层的 Apple Intelligence」**

---

## 6. [Base44](https://base44.com/)（产品战略 / 自研模型）

![Base44](/tmp/daily-screenshots/base44.png)

🔗 链接：[官网](https://base44.com/) | [TechCrunch 报道](https://techcrunch.com/2026/06/29/vibe-coding-platform-base44-launches-own-model-as-ai-startups-seek-defensibility/)

**融资信息**：Wix 以 **$8000 万**收购（收购时公司仅成立 6 个月，团队 8 人）。目前已达 **$1.5 亿 ARR**。

**做什么的**：Vibe-coding 平台（用自然语言创建应用），最近开始训练自有 AI 模型 **Base1**，用平台积累的「数千万真实用户交互」数据训练，目标是超越前沿模型的性价比。

**为什么值得关注**：
- **「 Wrapper 」反义词**：当所有人质疑 AI 应用层只是「GPT wrapper」时，Base44 用行动回答——从 wrapper 走向自研模型，用专有数据训练垂直 LLM。**这是 AI 应用公司建立护城河的模板路径**。
- $80M 被收购时仅 8 人团队、6 个月历史——然后迅速做到 $150M ARR。**这是 AI 时代「并购后增长」的新范式**：大平台收购小团队，小团队借助大平台的分发渠道实现爆发式增长。
- Base44 的创始人 Maor Shlomo 说：「有足够规模和速度的玩家最终都会训练自己的模型」——这意味着 AI 应用层的终局不是调用 API，而是**数据飞轮 + 自研模型**。
- 对创业者的启发：**先用别人的模型快速起量，积累专有数据，然后训练自己的模型——这是 AI 应用的经典三段式护城河建设路径**。

**类比参考**：**「Vibe-coding 版的 Character.AI / 自研模型的 Lovable」**

---

## 7. [Pocket](https://www.heypocket.com/)（融资 / AI 硬件）

![Pocket](/tmp/daily-screenshots/pocket.png)

🔗 链接：[官网](https://www.heypocket.com/) | [TechCrunch 报道](https://techcrunch.com/2026/06/29/pocket-raises-11m-in-bet-on-rising-demand-for-ai-note-taking-devices/)

**融资信息**：**$1100 万**融资，由 **Accel** 领投，YC、ElevenLabs CEO Mati Staniszewski 参投。

**做什么的**：$129 的信用卡大小的录音贴片，贴在手机背面，提供无限录音、转录和待办生成。**无订阅费**。已售超 **13 万台**。

**为什么值得关注**：
- **$129 一次性买断 + 零订阅**——在 AI 硬件领域几乎是一股清流。当所有 AI 产品都在收月费时，「一次购买，永久免费」成为极强的差异化卖点。
- 13 万台的销量证明了 AI 硬件不是伪命题。关键在于选对了场景：**会议录音 + 转录**是职场刚需，比 Rabbit 和 Humane 的「通用 AI 设备」靠谱得多。
- 竞争对手众多（Plaud、Mobvoi、Anker、Viaim、Vibe），但 Pocket 用**设计 + 定价**取胜。$129 的信用卡贴片比一个独立的录音笔更自然——它利用了你已有的设备（手机）。
- 对创业者的启发：**AI 硬件的最佳策略是「贴片式」而非「独立式」。不要做新设备，而是做已有设备的增强配件。价格要一次性买断，不要订阅**。

**类比参考**：**「AI 版 Plaud Note / 会议版的 AirTag」**

---

## 8. [Omen AI](https://www.omen.ai/)（融资 / AI 基建运维）

![Omen AI](/tmp/daily-screenshots/omen-ai.png)

🔗 链接：[官网](https://www.omen.ai/) | [TechCrunch 报道](https://techcrunch.com/2026/06/29/omen-ais-plan-to-optimize-data-centers-is-all-wet/)

**融资信息**：**$3100 万 Series A**，由 **Nava Ventures** 领投，CRV、Vanderbilt University、Mann+Hummel、Starhill Holdings、Hard Launch Capital 参投。

**做什么的**：用微型光谱仪实时监测数据中心液冷液体的化学健康——检测细菌滋生，避免停机清洗造成的数百万损失。

**为什么值得关注**：
- **切入了一个极为隐蔽但极其昂贵的痛点**：AI 算力爆发 → GPU 功耗上升 → 液冷温度升高 → 冷却液中水比例增加 → 细菌滋生 → 系统堵塞 → 停机 5-6 小时 → 损失数百万。这是 AI 基础设施的「蝴蝶效应」。
- 创始人 **Zach Laberge**，2020 年创立第一家公司时年仅 **14 岁**，融了 $300 万后从高中辍学。2024 年创立 Omen AI。这种「连续创业少年」的故事本身就是品牌。
- 产品逻辑清晰：不是卖软件订阅，而是**硬件（光谱仪传感器）+ 实时监测软件**的组合。数据中心的运维预算极大，且决策链短。
- 对创业者的启发：**AI 基建不只意味着芯片和算力，还意味着围绕算力的一切物理基础设施——冷却、电力、网络、安全。这些「基建的基建」往往是最大的盲区，也是最大的机会**。

**类比参考**：**「数据中心版的 Casana / AI 基建版的 Predictive Maintenance」**

---

## 9. [Proception](https://proception.ai/)（融资 / 机器人手）

🔗 链接：[官网](https://proception.ai/) | [TechCrunch 报道](https://techcrunch.com/2026/06/29/robot-hand-company-settles-tesla-trade-secret-suit-and-announces-11m-raise/)

**融资信息**：**$1100 万种子轮**，由 **First Round Capital** 领投，YC、BoxGroup 参投。

**做什么的**：制造高灵巧度机器人手，首批产品已发货给研究机构和机器人公司。目标是成为「不想自己造手」的机器人公司的顶级供应商。

**为什么值得关注**：
- 创始人 Jay Li 是 **Tesla Optimus 前技术负责人**，被 Tesla 起诉窃取商业机密后达成和解。Elon Musk 自己说过「机器人手是最大的工程难题之一」——Li 正面攻这个难题。
- **定位为「组件供应商」而非「整机厂商」**——这是极为聪明的市场定位。当所有人都在做完整的人形机器人时，Proception 专注于最难的那个部件（手），卖给所有需要的人。
- 与 Tesla 的诉讼和解本身就是一个「压力测试」——Li 说「杀不死你的让你更强」。和解后立刻宣布融资和发货，节奏控制得极好。
- 对创业者的启发：**在人形机器人赛道，「卖铲子」可能比「挖金子」更稳。做所有人都不愿意自己做但都需要的核心部件，就是最大的议价权**。

**类比参考**：**「机器人版 Intel / 人形机器人手的 Tier 1 供应商」**

---

## 值得重点跟踪的 3 个信号

1. **推理芯片赛道正式进入「订单验证」阶段**：Etched 的 $1B 合同订单 + Nvidia 对手密集涌现，说明 AI 芯片的竞争从「架构设计」进入「商业交付」。训练芯片看 Nvidia，推理芯片的胜负未定——这是半导体领域十年来最大的开放窗口。

2. **AI 编码 Agent 的「企业级」分层正在形成**：8090 Labs（$135M Series A）专攻企业级编码合规，Base44 从 wrapper 走向自研模型。通用编码 Agent（Cursor、Copilot）已经成熟，下一个战场是「能通过企业审计的 AI 编码」。

3. **Agent 经济的基础设施正在从概念走向产品**：OKX 的 Agent 市场（互相雇佣和结算）、Arena 的 $100M 评测生意、Acti 的键盘 Agent 入口——这些不是 Agent 本身，而是 **Agent 经济的「银行、评级机构和操作系统」**。谁建好了这些基础设施，谁就掌握了 Agent 时代的流量入口。

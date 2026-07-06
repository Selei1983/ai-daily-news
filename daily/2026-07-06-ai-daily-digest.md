# 0706日报 | Mechanical Turk 落幕，AI代理攻占华尔街和药厂

## 今日洞察

今天的五个字：「**旧神退位，新王登基。**」

**Amazon Mechanical Turk 宣布不再接受新客户（7月30日生效）**——这个2005年上线的众包平台，名字源自18世纪那个假装会下棋的「机械土耳其人」骗局，本身就是 AI 行业最大的反讽：**它让人类假装成 AI（标注数据、做验证），而今天 AI 终于进步到不再需要人类来扮演它了。** 一个时代的句号。

与此同时，AI 正在进入最受监管、最需要信任的两个行业。

**金融侧，LinqAlpha 以 $2200 万 A 轮融资证明了「AI 投研代理」的 PMF**——70+ 金融机构买单，客户管理超过 $5 万亿资产。不是更快地查资料，而是「在信息 priced in 之前就抓住信号」。**生物医药侧，Anthropic Claude Science 上周将药物研发从 12 年压缩到 7-8 年**，直接启动内部药物发现项目。

企业级 AI 的落地也在加速。**Celonis 收购 Ikigai Labs**，把流程挖掘变成了企业 AI 的「上下文层」——没有业务上下文的 Agent 就像没有地图的司机。**Vaudit 的 TokenAudit** 则在 AI 账单中精准挖出 5% 的计费错误，揭示了一个残酷事实：**AI 支出增长太快，财务团队根本跟不上。**

C 端同样热闹。Meta 的 **Pocket** 把 AI 生图/生视频推到了**生游戏**，一个社交 feed 全是 AI 生成的迷你游戏。南非杂货巨头 Pick n Pay 的 **Penny** 则成为非洲第一个对话式 AI 购物助手——AI 零售已经从「会推荐」进化到「能下单」。

**结论：AI 取代了人类标注员（MTurk），但正在创建新的高价值工种——AI 投研分析师、AI 药物开发者、AI 零售助手。而所有信任敏感行业的共同瓶颈，从「AI 能不能做」变成了「AI 有没有足够的上下文」。**

---

## 1. [Amazon Mechanical Turk](https://www.mturk.com/)（行业洞察 / AI 标注终结）

![Amazon Mechanical Turk](/tmp/daily-screenshots/mturk.png)

🔗 链接：[官网](https://www.mturk.com/) | [TechCrunch 报道](https://techcrunch.com/2026/07/05/amazon-will-stop-accepting-new-customers-for-mechanical-turk/)

**动态**：7月5日，Amazon 宣布 Mechanical Turk 将于 **7月30日起停止接受新客户**。现有客户可继续使用，但 AWS 明确表示「不会引入新功能」，仅维护安全性和可用性。

**做什么的**：21年历史的众包微任务平台——让人完成 AI 做不好的事（验证码识别、情感分析、数据标注）。2018年后转向 AI 训练数据标注，与 AWS SageMaker 深度集成。

**为什么值得关注**：

- **一个时代的句号。** MTurk 的名字本身就是 AI 最大的反讽——18世纪的「机械土耳其人」让人类假装成机器下棋，21世纪的 Mechanical Turk 让人类假装成 AI 做标注。**当真正的 AI 成熟到可以替代标注员时，这个骗局终于结束了。** 这对于所有 AI 创业者来说是一个极具象征意义的事件。
- **2023年已有 33%-46% 的 MTurk 工人开始用 LLM 完成任务**——人类标注员的「标注」本身已经被 AI 污染，你花钱买到的「人类数据」其实也是 AI 生成的。这个 data quality 危机加速了平台消亡。
- 对创业者的启发：**所有「伪 AI」业务都有保质期。如果你的商业模式是「用低成本人工假装 AI」，那真正的 AI 就是你的保质期终点。Mechanical Turk 的落幕是一个警示，也是一个提醒——真正的 AI 时代比所有人想象的都要快。**
- 它参与了 Facebook-Cambridge Analytica 丑闻（作为数据收集渠道），见证了 AI 行业从「人工智障」到「真 AI」的完整周期。**一个平台的生与死，就是一部 AI 简史。**

**类比参考**：**「AI 时代的诺基亚时刻 / 硅谷最讽刺的创业骗局终于落幕」**

---

## 2. [Pocket by Meta](https://play.google.com/store/apps/details?id=com.facebook.gizmo)（新产品 / AI 游戏社交）

![Pocket](/tmp/daily-screenshots/pocket-meta.png)

🔗 链接：[Google Play](https://play.google.com/store/apps/details?id=com.facebook.gizmo) | [TechCrunch 报道](https://techcrunch.com/2026/07/02/meta-quietly-launches-vibe-coded-gaming-app-pocket/)

**动态**：Meta 于6月29日静默上线 Pocket（iOS + Android），7月2日被开发者发现并公开报道。Meta 尚未官方回应。

**做什么的**：AI 驱动的创意平台——用户输入文字提示，AI 直接生成可交互的迷你游戏（称为 "gizmos"），并提供一个社交 feed 让用户浏览和游玩其他人创建的游戏。**本质上是一个 TikTok 式的游戏 feed，但所有内容都是 AI 生成的。**

**为什么值得关注**：

- **Meta 把「vibe coding」做成了社交产品。** 这不是一个生产力工具，而是一个**娱乐平台**——你不需要会写代码，只需要会「描述你想要什么游戏」，AI 就帮你做出来，然后你的朋友可以玩。**这是 AI 内容创作从「生产力」向「娱乐」的转折点。**
- **前身 Gizmo 已被 Meta 收购**，Gizmo 在被收购前有 63.5 万次安装和 98% 的正面评价。Meta 没有重造轮子，而是直接买了市场上最好的产品并用自己的分发能力放大。**这种「收购+内化」的模式是 Big Tech 渗透 AI 新品类的最快路径。**
- **Meta 的策略清晰可见**：Meta AI（生图）→ Vibes（生视频）→ Pocket（生游戏）。**每一层 AI 内容都更复杂、更有交互性、更社交化。** 这是 ChatGPT 式聊天机器人之外的另一种 AI 战略——让 AI 创造 Content，而不是回答问题。
- 对创业者的启发：**AI 内容创作的下一个爆发点不是「更好看的图」，而是「更好玩的交互」。「让用户用自然语言创造可分享的交互体验」可能是比「AI 视频」更大的市场。**

**类比参考**：**「Roblox 遇见了 AI / TikTok for AI-powered mini games」**

---

## 3. [Celonis + Ikigai Labs](https://www.celonis.com/)（行业洞察 / 企业 AI 上下文层）

![Celonis](/tmp/daily-screenshots/celonis.png)

🔗 链接：[Celonis 官网](https://www.celonis.com/) | [官方新闻稿](https://www.celonis.com/news/press/celonis-launches-the-context-model-to-eliminate-enterprise-ais-operational-blind-spots-agrees-to-acquire-ai-decision-intelligence-leader-ikigai-labs)

**动态**：7月1日，Celonis 正式发布 **Celonis Context Model (CCM)**，并宣布签署最终协议收购 **Ikigai Labs**（MIT 孵化，AI 决策智能平台）。MIT 成为 Celonis 股东。

**做什么的**：Celonis 是全球流程挖掘（Process Mining）领域的领导者（估值约 $130 亿）。CCM 将企业运营流程（订单到现金、采购到付款等）转化为 AI 可以理解的「数字孪生」。收购 Ikigai Labs 后，叠加了规划、模拟和预测能力。

**为什么值得关注**：

- **这是「企业 AI 落地」最务实的解法。** 行业共识是：企业 AI 最大的障碍不是模型能力，而是**上下文缺失**——AI 不知道业务怎么跑、决策链是什么、审批流程怎么走。Celonis 的 Context Model 直接解决这个问题：**把 20 年的流程数据变成 AI 的「教科书」。**
- **收购 Ikigai 的 MIT 基因是关键**。Ikigai 的创始人 Devavrat Shah 是 MIT 教授，近 20 年专注于时间序列建模和因果推断。将「预测+模拟」能力叠加到「流程理解」上，构成了企业 AI 的完整能力层。
- **客户阵容说明一切**：Cardinal Health、Cosentino、Mondelez 等 CIO 亲自背书。他们的共识高度一致：**没有上下文的 AI，只是好玩的 demo。** 这句话值得每一位做企业 AI 的创始人贴在墙上。
- 对创业者的启发：**企业 AI 的终局不是「更好的模型」，而是「模型的运营上下文」。如果你能帮企业把 20 年的 ERP 数据变成 AI 能理解的上下文，你就是这个时代的 Oracle。**

**类比参考**：**「企业 AI 的 Google Maps / 流程挖掘 + 决策智能 = 企业 AI 的操作系统」**

---

## 4. [LinqAlpha](https://linqalpha.com/)（融资 / AI 投研代理）

![LinqAlpha](/tmp/daily-screenshots/linqalpha.png)

🔗 链接：[官网](https://linqalpha.com/) | [TechNode 报道](https://technode.global/2026/07/02/linqalpha-raises-22m-series-a-to-build-ai-layer-for-institutional-investors/)

**融资信息**：**$2200 万 Series A**，由 **AVP** 领投，**Atinum Investment、GFT Ventures** 跟投。战略投资方涵盖日本（SBI Investment）、东南亚（East Ventures）、韩国（Samsung Securities、Mirae Asset）、印度（NuVentures）等。

**做什么的**：面向机构投资者的 AI 多 Agent 平台——每个 Agent 学习用户的投研框架，跨 139 个国家、57,000+ 公司、30+ 语言实时分析市场和另类数据，输出「尚未被市场定价的差异化信号」。

**为什么值得关注**：

- **PMF 已经验证**：70+ 金融机构已签约，包括卖方的顶级投行研究/交易团队和买方的 Causeway Capital Management、Schonfeld Strategic Advisors。买方客户管理资产总计超 **$5 万亿**。**这不是概念验证，这是已经签了大客户的生意。**
- **产品定位极为锋利**：CEO Hojun Choi 说「第一波 AI 让分析师更快，下一波改变他们**能知道什么**」——LinqAlpha 的差异化不是「更快检索信息」，而是「在信息被市场定价前就抓住」。**这是 AI 在量化金融领域最性感的定位。**
- **全球化的投资人阵容**反映了 **Wall Street 正在全面拥抱 AI 投研**：从日本的 SBI 到韩国的 Samsung Securities、Mirae Asset，从东南亚到印度——**全球资本市场都在赌 AI 投研会取代传统的研究方法。**
- 对创业者的启发：**「AI Agent + 专业领域知识」的商业模式已经被金融行业验证。70 个客户、$5 万亿资产管理的信任，比任何融资数字都更有说服力。下一个垂直在哪里？法律、医疗、咨询——任何需要「专业化判断」的行业都值得重做一遍。**

**类比参考**：**「Bloomberg Terminal 遇见了 AI Agent / GPT 时代的 FactSet」**

---

## 5. [Vaudit TokenAudit](https://vaudit.com/)（新产品 / AI 账单审计）

![Vaudit](/tmp/daily-screenshots/vaudit-dash.png)

🔗 链接：[官网](https://vaudit.com/) | [Las Vegas Sun 报道](https://lasvegassun.com/news/2026/jun/30/vaudit-launches-tokenaudit-to-recover-millions-in-/)

**动态**：6月30日发布 **TokenAudit**——专注 AI Token 消费的账单审计工具。已审计 $3400 万 AI 账单，发现约 **$170 万误收费**。

**做什么的**：在企业 AI 环境中安装 SDK，自动捕获原始用量数据并与发票对账，识别五大类计费错误（高级模型按低价计费的逆向错误、零输出请求计费、重试风暴、停机期间计费、编排错误）。

**为什么值得关注**：

- **企业 AI 支出正在失控。** 2026 年全球 AI 支出预计达 **$2.59 万亿**（同比 +47%），AI 基础设施占比 >45%。当企业 AI 账单增长比任何其他预算都快时，「审计」从 nice-to-have 变成了 must-have。**Vaudit 发现 $3400 万中有 $170 万错误——5% 的错账率意味着全球 AI 市场有 $1300 亿计的「幽灵支出」。**
- 五种计费错误模式揭示了行业问题：**AI 计费黑箱**。客户常常不知道哪个模型处理了请求，是否有缓存、重试或去重。对于使用 Agent 的团队来说，「重试风暴」是致命问题——Agent 自动重试失败请求，账单悄悄翻倍。
- Vaudit 的创始人背景值得关注：Michael Hahn 此前做过广告技术和营收运营公司。**跨行业的「支出审计」能力——从广告到云到 AI——是一种可以标准化的能力。**
- 对创业者的启发：**每一个新的大额支出品类都会催生「审计」品类。AI Token 计费，就像云成本优化（CloudHealth、Vantage）和广告审计一样，是一个实打实的现金牛市场。** 而且壁垒清晰——不是谁都能让 Anthropic 和 OpenAI 退款。

**类比参考**：**「AI 版的 CloudHealth / LLM 账单的 Mint.com」**

---

## 6. [Pick n Pay Penny](https://www.pnp.co.za/)（新产品 / AI 零售购物助手）

🔗 链接：[Reuters 报道](https://www.reuters.com/world/africa/pick-n-pay-launches-ai-grocery-shopping-assistant-south-africa-2026-07-02/) | [BizCommunity](https://www.bizcommunity.com/article/pick-n-pay-rolls-out-gemini-powered-grocery-assistant-penny-175696a)

**动态**：南非零售巨头 Pick n Pay 于 **7月6日（今天）** 正式上线 **Penny**——由 Google Gemini 驱动的 AI 购物助手，集成在其 asap! 应用中。

**做什么的**：对话式 AI 购物助手——用户可以用语音、文字甚至照片与 Penny 交互，让它推荐食谱、生成购物清单、建议替代品、在预算内装购物车，并直接下单。支持南非多种语言。

**为什么值得关注**：

- **AI 零售从「推荐」进化到「执行」。** 过去的 AI 购物工具只是推荐商品——Penny 不一样，**它可以直接完成购物并在应用内下单**。这不仅是一个聊天机器人，而是一个「能购物的对话式助手」。这是零售 AI 的一个关键转折点。
- **南非是新兴市场的「试验田」**。当美国和欧洲的零售 AI 还停留在「聊天机器人+推荐」时，非洲的零售商已经直接跳到「AI 代理全流程执行」——从发现到下单，一步完成。**新兴市场没有 legacy 系统的包袱，往往能更快地拥抱 AI-native 体验。**
- Penny vs Pixie（竞争对手）的竞争，正在把 **AI 零售变成一个可观察的战场**。当 AI 助理能直接生成订单时，零售商对平台的控制力会减弱——**消费者以后可能不再是「去 Pick n Pay 买东西」，而是「问 Penny 我要买什么，Penny 帮我搞定」**。这个转变对零售业的影响深远。
- 对创业者的启发：**C 端 AI 的最大机会不是「更好的推荐」，而是「替代决策」。当 AI 从「推荐你买什么」进化到「帮你直接买好」，用户体验提升了一个数量级——但对现有零售体系的颠覆也是数量级的。**

**类比参考**：**「Instacart 遇见了 ChatGPT / 非洲第一个能购物的 AI Agent」**

---

## 值得重点跟踪的 3 个信号

1. **Mechanical Turk 的落幕是 AI 行业的分水岭事件。** 2005-2026，21 年，一个让「人类假装成 AI」的平台被「真正的 AI」杀死。这不仅仅是 Amazon 砍掉一个老业务——这是 AI 行业从「需要人类拐杖」到「自己能走路」的成人礼。**对所有 AI 创业者而言，这意味着：你的产品如果还需要大量人工介入才能工作，你最好有一个比 MTurk 更好的退出路径。**

2. **「上下文层」正在成为企业 AI 的兵家必争之地。** Celonis（流程上下文）+ Ikigai（决策上下文）的结合，LinqAlpha（投研上下文）的 70+ 客户，都在证明同一件事：**没有业务上下文的 AI Agent 是玩具，有上下文的才是工具。** 对于做企业 AI 的创业者，与其卷模型能力，不如思考「我能不能帮客户把数据和流程变成 AI 的上下文」。

3. **AI 支出正在催生「AI 时代的四大会计师事务所」。** Vaudit 的 $3400 万审计覆盖只是冰山一角——$2.59 万亿的全球 AI 支出意味着「AI 账单审计」是一个真实的大市场。类比 20 年前的云计算，CloudHealth 等成本优化工具造就了数十亿美元的品类。**AI 时代的「成本优化+审计+安全」工具链才刚刚开始形成。下一个 AI 时代的 CrowdStrike 或 Datadog 可能就是这个方向。**

---

*统计信息：收录 6 个产品 | 融资总额 $2200 万 | 覆盖赛道：AI 行业变迁、AI 游戏社交、企业 AI 上下文、AI 投研、AI 账单审计、零售 AI*

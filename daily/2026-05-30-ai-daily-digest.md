# AI 产品日报 | 2026-05-30

> 🔬 422产品实验室 · AI新产品日报 · 每日精选

## 今日洞察

今天最值得创业者注意的信号，不是又有哪个模型更强，而是 **AI 的「落地效率层」正在快速成形**。

一头是基础设施端在解决成本与吞吐问题：**XCENA** 把计算往内存侧搬，押注「AI 真正的瓶颈不是算力，而是 memory movement」；**Tensormesh** 把 KV Cache 直接做成 SaaS 产品，并给出「缓存 token 永久免费」这种极具穿透力的定价；**Slamcore** 则把视觉定位数据沉淀成 physical AI 的训练资产。另一头是应用层在解决 adoption 与交互问题：**Sesame** 用更自然的语音 Agent 重新定义 AI 入口，**Atheni** 把“买了 AI 工具但团队不会用”这件事产品化，**Integuru** 用“直连内部 API”替代浏览器自动化，直接切进企业自动化的效率黑洞。

这背后的共同点是：**新一波 AI 创业，不再只比模型能力，而是在比谁能把推理成本、组织采用成本、系统接入成本压得更低。** 对产品经理和创业者来说，真正值得做的层，往往不在最显眼的模型层，而在那些能把 AI 变成“可部署、可复制、可规模化”能力的中间层。

---

## 1. XCENA — $1.35亿 Series B，押注 AI 的真正瓶颈不是算力，而是内存

**融资信息**：$1.35亿 Series B，估值约 $5.7 亿；累计融资 $1.85 亿。Atinum、IMM Investment 联合领投，Corstone Asia，以及 SBI Investment、Mirae Asset Capital 等老股东参投。

**做什么的**：一家韩美两地布局的芯片创业公司，做 memory-centric AI 基础设施。XCENA 的 MX1 芯片把一部分数据处理放到靠近 DRAM 的位置完成，减少 CPU / GPU / 内存之间反复搬运数据的成本。

**为什么值得关注**：
- **这不是“再造一个 GPU”，而是重写 AI 推理栈里最贵的搬运环节**。当上下文越来越长、KV cache 越来越大，memory bandwidth 和数据搬运成本会越来越像天花板。
- **它切的是 hyperscaler 的真痛点**。如果 10 台服务器能缩成 1 台，哪怕只有部分场景成立，对云厂商和大模型服务商都是立刻可量化的 ROI。
- **创业启发：别总盯着模型本身，模型周围的“数据流动效率”同样是大市场**。当所有人都在卷更强推理时，优化 memory path 反而可能是更好的基础设施机会。

**类比参考**：像是 AI 时代的“内存侧 DPU / SmartNIC”——不是替代主算力，而是把最浪费钱的搬运和调度先吞掉。

![XCENA](/tmp/daily-screenshots/xcena.png)

🔗 [TechCrunch](https://techcrunch.com/2026/05/29/xcena-secures-135m-at-570m-valuation-betting-on-memory-as-ais-real-bottleneck/) | [官网](https://xcena.com/)

---

## 2. Tensormesh — $2000万 extended seed，把 KV Cache 产品化，还把缓存 token 定价打到 0

**融资信息**：extended seed $2000万，总融资达 $2450万。投资方包括 AMD Ventures、CoreWeave、NVentures、Valley Capital Partners、Laude Ventures。

**做什么的**：做 inference optimization 平台。Tensormesh 的核心是把 KV caching 从“论文/底层优化技巧”变成企业可直接采购的 SaaS 推理服务，减少重复计算，降低延迟和 GPU 开销。

**为什么值得关注**：
- **方向很准：推理成本正在成为企业 AI 的第一性约束**。不是每家公司都缺模型，更多公司缺的是“怎么把 inference bill 降下来”。
- **定价策略极强**：缓存命中的 input token 直接按 **$0** 计费，这不是功能描述，而是非常清晰的 GTM 语言。
- **开源到商业的路径很标准**：团队来自 8K+ GitHub Star 的 LMCache 项目，先做社区心智，再做企业级托管与可观测性，路径非常像很多基础设施公司的成功模板。
- **创业启发**：如果你做 AI infra，不要只卖“性能更好”，要卖“账单更低且透明”。Tensormesh 最聪明的地方，是把底层技术优势翻译成 CFO 听得懂的价格模型。

**类比参考**：像是“AI 推理版的 CDN / Redis”——复用已经算过的结果，而不是每次都从头烧 GPU。

![Tensormesh](/tmp/daily-screenshots/tensormesh.png)

🔗 [The AI Insider](https://theaiinsider.tech/2026/05/29/tensormesh-secures-20m-from-investors-including-amd-ventures-coreweave-nventures-launches-tensormesh-inference-to-fix-ais-most-expensive-problem/) | [官网](https://www.tensormesh.ai/)

---

## 3. Slamcore — $1400万，做工业车辆的“视觉 RTLS”，顺手积累 physical AI 最稀缺的数据

**融资信息**：$1400万新融资，累计融资 $4000万。ROKStar Ventures（Rockwell Automation 旗下）领投，Toyota Ventures、Interwoven Ventures、MMC Ventures、Amadeus Capital Partners、IP Group 跟投。

**做什么的**：用双目相机 + 视觉 AI，让叉车等工业车辆在没有 GPS、信标、地标改造的情况下完成室内定位、轨迹追踪、风险监控和车队可视化。

**为什么值得关注**：
- **它卖的不是机器人梦想，而是立刻可上线的工业可视化 ROI**。不用改造工厂基础设施，是最关键的落地条件。
- **Rockwell 和 Toyota Ventures 同时下注，说明这不是 demo 型 AI，而是工业链条认可的产品形态**。
- **更有意思的是数据飞轮**：每一次部署都在积累真实工业操作数据，这些数据未来可以反哺 physical AI / robotics 模型训练。
- **创业启发**：在具身智能里，先卖“安全、追踪、效率”这种近收益产品，再慢慢长成数据平台，往往比一上来卖通用机器人更现实。

**类比参考**：像是工业车辆版的“视觉地图 + 车队分析 OS”，介于 Samsara 和 physical AI 数据层之间。

![Slamcore](/tmp/daily-screenshots/slamcore.png)

🔗 [The AI Insider](https://theaiinsider.tech/2026/05/29/slamcore-raises-14m-in-funding-to-scale-visual-ai-that-tracks-industrial-vehicles/) | [官网](https://www.slamcore.com/)

---

## 4. StackAI — 被 Asana 收购，no-code AI Agent builder 进入主流程软件分发体系

**融资/并购信息**：Asana 收购 StackAI；据 The AI Insider 报道交易金额约 **$7500万**。StackAI 此前累计融资接近 $2000万，最近一轮为 $1600万 Series A。

**做什么的**：一个面向企业的 no-code AI workflow / agent builder，让团队用拖拽方式连接 Salesforce、Slack、G Suite 等系统，把 AI Agent 嵌进现有流程。

**为什么值得关注**：
- **这次收购的意义不只在金额，而在分发**。Agent builder 不再只是独立工具，而是被主流程软件吸收进“human-agent team OS”。
- **说明 AI 工作流工具的终局之一，是并入已有工作协同平台**。独立创业公司如果没有强分发，最后很可能要接入 Asana、Monday、Notion 这类平台。
- **创业启发**：如果你做企业 Agent 产品，要想清楚自己是“平台型终局”，还是“被大平台并购的能力模块”。StackAI 显然证明后者也可以是很合理的路径。

**类比参考**：像是“Zapier + AI Agent builder”的企业版，然后被 Asana 当成工作流智能化底座吸收。

![StackAI](/tmp/daily-screenshots/stackai.png)

🔗 [TechCrunch](https://techcrunch.com/2026/05/28/asana-acquires-no-code-agent-builder-stack-ai/) | [The AI Insider](https://theaiinsider.tech/2026/05/29/asana-acquires-ai-workflow-startup-stackai-for-75m-to-build-human-agent-os/) | [官网](https://www.stackai.com/)

---

## 5. Sesame — Oculus 创始团队把 conversational AI Agent 推到 iOS 公测

**产品动态**：iOS app public preview 上线，覆盖 39 个国家，现阶段免费开放。

**做什么的**：Sesame 做的是更自然的 conversational AI agent，不强调“聊天框问答”，而是强调像真人一样持续说话、思考中插入检索结果、保留记忆，并逐步走向可执行任务的 personal agent。

**为什么值得关注**：
- **它在重新定义 AI 的交互壳层**。很多产品还停留在“更强聊天机器人”，Sesame 已经开始逼近“可以持续陪你思考的语音 agent”。
- **从 Research Preview 到 iOS app，是典型的消费级 AI 产品化一步**：先用技术惊艳早期用户，再把交互、记忆、搜索卡片、深度模式、隐私模式做成完整产品。
- **创始团队背景强，但更重要的是路线判断对**：如果未来 AI 入口从文本框转向语音 / 可穿戴，Sesame 很可能是在卡一个新的终端位。
- **创业启发**：模型能力趋同后，消费级 AI 竞争会越来越像“体验设计竞争”——语音节奏、人格一致性、记忆机制，都会变成真正的产品壁垒。

**类比参考**：像是“Her 的早期版本 + ChatGPT 语音模式”，但从一开始就按 personal agent 在设计。

![Sesame](/tmp/daily-screenshots/sesame.png)

🔗 [TechCrunch](https://techcrunch.com/2026/05/28/sesame-the-conversational-ai-startup-from-oculus-founders-launches-its-ios-app/) | [官网](https://www.sesame.com/)

---

## 6. Atheni — £35万，切入一个很真实但常被忽视的市场：组织明明买了 AI，却根本不会用

**融资信息**：£350K，投资方包括 Zoopla / Cazoo 创始人 Alex Chesterman OBE，并获得 Innovate UK 支持。

**做什么的**：Atheni 不是再做一个 AI 工具，而是做 **AI adoption platform**。它通过浏览器侧平台和角色化引导，帮助员工在真实工作流里提升 AI 使用能力，而不是只上几堂培训课。

**为什么值得关注**：
- **这家公司抓的是“AI 采购后遗症”**：企业买了 ChatGPT、Claude、Copilot，但员工不知道怎么把它用进业务决策，结果 ROI 很差。
- **它卖的是 capability，不只是 access**。这个定位非常聪明，因为“有账号”不等于“会产出结果”。
- **90 天 adoption rate 超过 90% 的叙述非常有杀伤力**。对 ToB 创业者来说，这种业务结果导向的表述，比任何模型参数都更容易成交。
- **创业启发**：围绕 AI 的培训、流程、治理、 adoption，本身就是一条足够大的软件赛道。未来会有很多公司不是做 AI 本身，而是做“让组织真正用起来”。

**类比参考**：像是“企业 AI 教练 + 轻量 workflow layer”，介于咨询公司、LMS 和 AI copilot 之间。

![Atheni](/tmp/daily-screenshots/atheni.png)

🔗 [Tech Funding News](https://techfundingnews.com/female-founded-atheni-backed-by-zooplas-founder-lands-350k-to-help-businesses-actually-use-ai/) | [官网](https://atheni.ai/)

---

## 7. Integuru — 用源码和 HTTP 直连替代浏览器自动化，切进企业集成的老问题

**产品动态**：5 月 29 日以 Show HN 形式发布新版本。官网主张非常直接：**Generate fast, reliable APIs for any platform. No RPA. No browsers.**

**做什么的**：Integuru 帮开发者为既有平台生成可用 API，但不是靠浏览器自动化/RPA 去“点页面”，而是尽可能走源码理解、直接 HTTP 请求和内部接口还原的路线。

**为什么值得关注**：
- **切中一个老痛点**：大量企业系统没有好用 API，传统 RPA 又脆、慢、难维护。
- **“不用浏览器”本身就是很清晰的差异化口号**。它把一类技术替代方案，包装成了用户立刻能理解的价值主张。
- **这类产品很适合 AI 来做**：过去逆向和接口抽取更像手工活，现在模型可以帮助识别前端代码、请求结构和依赖关系。
- **创业启发**：AI 最有价值的地方之一，不是创造新工作流，而是把那些老旧系统里的“脏集成”自动化掉。谁能把接入成本降下来，谁就能吃到大量存量软件预算。

**类比参考**：像是“Postman + Reverse API Generator”的 AI 版，和传统 RPA / browser automation 走的是完全不同的技术路线。

![Integuru](/tmp/daily-screenshots/integuru.png)

🔗 [Show HN](https://news.ycombinator.com/item?id=44133863) | [官网](https://www.integuru.com/)

---

## 8. 乘物机器人 — 天使轮完成，先靠富士康等工业客户做交付，再反哺工业 VLA 模型

**融资信息**：完成天使轮融资，由中国台湾工业自动化与智能机器人解决方案企业**和椿科技**战略投资，华君资本担任独家财务顾问。

**做什么的**：深圳工业具身智能公司，面向工业场景做软硬件一体化机器人解决方案，同时自研工业垂类 VLA 模型、遥操数据采集装置和远程操作系统。成立于 2025 年，半年营收已超两千万元，客户包括富士康。

**为什么值得关注**：
- **这不是 PPT 机器人，而是先拿订单、再做模型**。对中国具身智能创业者来说，这种路径尤其重要。
- **真实 industrial delivery 经验本身就是壁垒**。很多团队会做模型 demo，但很少团队真正知道工厂现场怎么交付、怎么迭代、怎么持续收费。
- **它的路线很务实**：先用成熟供应链拼出可交付方案，再把数据采集、模型训练、跨本体泛化能力往上叠。
- **创业启发**：具身智能最可行的商业路径之一，可能不是先造通用机器人，而是先从工业非标项目切进去，用项目现金流和现场数据把模型养起来。

**类比参考**：像是“工业场景版的 embodied AI 系统集成商 + 垂直模型公司”。

![乘物机器人](/tmp/daily-screenshots/chengwu-robotics.png)

🔗 [36氪](https://36kr.com/p/3831135917107075?f=rss)

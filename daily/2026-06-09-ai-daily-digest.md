# 0609日报 | AI垂类重做旧系统

## 今日洞察

今天最值得创业者注意的，不是又多了一个通用 Agent，而是**一批 AI 创业公司开始直接重做老行业的软件骨架**：有的把合规层塞进模型与用户之间，有的把护理机构、医院、酒类零售、浏览器自动化、语音外呼这些老工作流整包重写。一个清晰信号是，AI 产品的下一波机会正在从“外挂式 copilot”转向**“AI 原生操作系统 + 行业专用基础设施”**。谁能把旧系统里最重、最慢、最贵的一段流程吃下来，谁就更容易拿到真正持续的预算。

---

## 1. [ZeroDrift](https://www.zerodrift.ai/)（融资）

![ZeroDrift](/tmp/daily-screenshots/zerodrift.png)

🔗 链接：[官网](https://www.zerodrift.ai/) | [TechCrunch 融资报道](https://techcrunch.com/2026/06/02/zerodrift-raises-10-million-to-protect-ai-models-from-themselves/)

**融资信息**：Seed 轮 **1000 万美元**；投资方包括 **a16z Speedrun、Reign Ventures、Pitchdrive、U&I Ventures** 等。

**做什么的**：在模型和终端用户之间加一层“AI 合规防火墙”，先用确定性规则识别 SOC 2、GDPR 等合规风险，再用 LLM 重写成合规输出。

**为什么值得关注**：
- 它不是做“更安全的聊天机器人”，而是在做 **模型外部的治理执行层**。
- 这类产品的价值不在回答更聪明，而在 **更低延迟、更高可控性、更强审计性**。
- 对创业者的启发是：高监管行业里，AI 的预算往往不先给生成层，而是先给 **风控、拦截、审计和责任归属层**。

**类比参考**：**“Cloudflare / Palo Alto 的 AI 输出合规版”**

---

## 2. [TakeCareOS](https://www.takecareos.com/)（YC / 新产品）

![TakeCareOS](/tmp/daily-screenshots/takecareos.png)

🔗 链接：[官网](https://www.takecareos.com/) | [YC 页面](https://www.ycombinator.com/companies/takecareos)

**融资信息**：YC Spring 2026 批次，融资金额未披露。YC 页面显示其已与 **6 家护理机构、200+ 员工**合作试跑整套业务运营。

**做什么的**：面向 home care、aged care、disability services 机构的 AI 原生操作系统，覆盖 rostering、CRM、notes、messaging、timesheets、invoicing、compliance，并用 AI agents 接管文书和后台 admin。

**为什么值得关注**：
- 它不是在旧护理软件上加一个 copilot，而是直接把 **“业务系统 + AI 执行层”** 一起重做。
- 护理与照护行业长期被高频低效 admin 工作拖住，TakeCareOS 切的是最容易形成 ROI 的部分。
- 对创业者的启发是：很多垂直行业真正缺的不是一个 AI 助手，而是一套 **默认把 AI 当员工来设计的软件底座**。

**类比参考**：**“Home care 版 ServiceTitan / AI-native ERP”**

---

## 3. [Eos AI](https://www.helloeos.ai/)（YC / 创新模式）

![Eos AI](/tmp/daily-screenshots/eos-ai.png)

🔗 链接：[官网](https://www.helloeos.ai/) | [YC 页面](https://www.ycombinator.com/companies/eos-ai) | [Launch YC](https://www.ycombinator.com/launches/Pct-eos-ai-autonomous-os-for-hospitals)

**融资信息**：YC Spring 2026 批次，融资金额未披露。YC Launch 页面披露，早期诊所场景中已看到 **约 3 倍 admin productivity improvement** 与 **37% revenue recovery**。

**做什么的**：把医院/诊所分散在 EHR、影像、实验室、排班、计费等系统中的数据重新串起来，做成可搜索、可分析、可触发运营动作的 healthcare autonomous OS。

**为什么值得关注**：
- 医疗 AI 里最难的一步常常不是模型，而是 **把碎片化数据拼成可执行上下文**。
- Eos AI 不是单点做 scribe 或病历总结，而是先做 **数据协调层 + 运营动作层**。
- 对创业者的启发是：如果一个行业数据极碎，先拿下“统一上下文”这一层，后面的 agent、推荐、自动化才有复利。

**类比参考**：**“Palantir / Snowflake 的医院运营 Agent 版”**

---

## 4. [Prana](https://www.pranadoc.com/ai-doctor)（YC / 新产品）

![Prana](/tmp/daily-screenshots/prana-health.png)

🔗 链接：[官网](https://www.pranadoc.com/ai-doctor) | [YC 页面](https://www.ycombinator.com/companies/prana-health) | [Launch YC](https://www.ycombinator.com/launches/PPg-prana-an-ai-doctor-that-monitors-you-24-7)

**融资信息**：YC Winter 2026 批次，融资金额未披露；YC 页面显示产品 **已进入 beta 并开始上线真实用户**。

**做什么的**：做“口袋里的 AI 家庭医生”，连接病历与 wearable 数据，持续监测用户健康变化，并把传统一年一次的被动体检改成持续式、主动式初级医疗。

**为什么值得关注**：
- 它的切法不是“在线问诊聊天”，而是试图重做 **primary care 的服务频率与交互范式**。
- 医疗产品里，连续监测 + 风险早筛，比一次性问答更容易建立长期使用场景。
- 对创业者的启发是：AI 最有机会重做的，不只是效率，而是把原本低频的服务改成 **持续关系型产品**。

**类比参考**：**“One Medical + wearable intelligence 的 AI 版”**

---

## 5. [Scotch](https://scotchpos.com/)（融资）

![Scotch](/tmp/daily-screenshots/scotch.png)

🔗 链接：[官网](https://scotchpos.com/) | [Crunchbase News](https://news.crunchbase.com/venture/scotch-raises-ai-funding-liquor-retail-tech/) | [PR Newswire](https://www.prnewswire.com/news-releases/scotch-raises-20m-series-a-to-modernize-liquor-stores-surpasses-1b-in-payment-volume-302790781.html)

**融资信息**：Series A **2000 万美元**；由 **VMG Partners** 领投，**First Round Capital、Lerer Hippeau、Toba Capital** 跟投。公司披露其 annual run rate gross payment volume 已超过 **10 亿美元**。

**做什么的**：为酒类零售店提供 AI-native POS、back office、inventory、invoice reconciliation、pricing intelligence 与 e-commerce 一体化系统。

**为什么值得关注**：
- 酒类零售是典型“看起来小众、其实极复杂”的行业，SKU 多、分销链长、合规和进销存都很重。
- Scotch 的产品策略不是做通用零售 SaaS，而是把一个被忽视行业的核心工作流 **从底层完全重构**。
- 对创业者的启发是：最好的垂直 SaaS 机会，往往藏在 **被主流软件长期服务不好的细分行业**。

**类比参考**：**“Drizly 之后的 liquor retail OS / 酒类零售版 Toast”**

---

## 6. [Mecka](https://www.mecka.ai/)（融资）

![Mecka](/tmp/daily-screenshots/mecka.png)

🔗 链接：[官网](https://www.mecka.ai/) | [Fortune 报道](https://fortune.com/2026/06/01/mecka-ai-series-a-60-million-robotics-data-training/) | [BetaKit 报道](https://betakit.com/mecka-ai-announces-60-million-usd-to-power-physical-ai/)

**融资信息**：累计宣布 **6000 万美元 Series A 相关融资**，包括 **2500 万美元 Series A** 与 **3500 万美元 Series A extension**；公开报道显示由 **Framework Ventures** 领投，并获 **SV Angel、Ted Xiao** 等支持。

**做什么的**：做 physical AI 的数据与部署层，采集第一视角真实任务视频、做人类动作理解与评估，把机器人从实验室 demo 推向真实场景部署。

**为什么值得关注**：
- Physical AI 最缺的不是再多一个模型，而是 **足够真实、可训练、可评估、可部署的数据闭环**。
- Mecka 的定位不是造机器人，而是做机器人生态里的 **integrator + data engine**。
- 对创业者的启发是：具身智能的高价值层，未必在整机，更可能在 **数据、评估、集成与商业交付中间层**。

**类比参考**：**“Scale AI / Anduril 在 Physical AI 数据层的结合体”**

---

## 7. [AethexAI](https://www.aethexai.com/)（融资 / 新产品）

![AethexAI](/tmp/daily-screenshots/aethexai.png)

🔗 链接：[官网](https://www.aethexai.com/) | [TechCrunch 报道](https://techcrunch.com/2026/06/03/these-two-founders-left-goldman-and-meta-to-build-voice-ai-for-markets-everyone-else-overlooked/) | [Tech.eu 报道](https://tech.eu/2026/06/04/aethexai-raises-3m-to-build-voice-ai-infrastructure-for-africa-and-the-middle-east/)

**融资信息**：Pre-seed **300 万美元**；由 **4DX Ventures** 领投，**Enza Capital、Dorm Room Fund、Mojo Ventures、Stanford GSB 26 Fund** 等参投。

**做什么的**：面向中东和非洲市场做方言友好的 voice AI 基础设施，覆盖法语、阿拉伯语、英语的本地口音与低延迟语音交互，并同步推出 API / SDK。

**为什么值得关注**：
- 它没有沿用通用 voice stack，而是自己做小模型和 orchestration，解决 emerging markets 下的 **高延迟、口音复杂、基础设施不均衡** 问题。
- 这类公司抓住的是“被全球主流模型忽略的市场空白”，不是正面卷美国标准场景。
- 对创业者的启发是：全球化 AI 创业不一定靠更大模型，很多时候靠 **更本地化的数据、更小的模型、更懂区域约束的工程**。

**类比参考**：**“Vapi / ElevenLabs 的新兴市场本地化版本”**

---

## 8. [Intuned](https://intunedhq.com/)（新产品 / 值得借鉴）

![Intuned](/tmp/daily-screenshots/intuned.png)

🔗 链接：[官网](https://intunedhq.com/) | [YC Launch](https://www.ycombinator.com/launches/PxK-intuned-code-first-browser-automation-built-and-maintained-by-ai) | [Hacker News](https://news.ycombinator.com/item?id=48445171)

**融资信息**：YC S22 公司，本次为新产品/新能力曝光，融资金额本轮未披露。

**做什么的**：让用户用自然语言描述需求，由 AI 生成 production-ready 的 Playwright 浏览器自动化代码、部署到平台，并在网站结构变化后自动修复与重部署。

**为什么值得关注**：
- 它不是普通的“AI 帮你录制 RPA”，而是把 **生成代码、运行基础设施、观测日志、故障修复** 做成一体化闭环。
- 对很多企业来说，重复执行的浏览器任务需要的是代码级稳定性，而不是一次性演示型 agent。
- 对创业者的启发是：AI 最有价值的形态之一，不是完全替代代码，而是把 **代码生产、维护、诊断** 这几个最贵环节压缩掉。

**类比参考**：**“Retool Workflows + Playwright Cloud + self-healing agent”**

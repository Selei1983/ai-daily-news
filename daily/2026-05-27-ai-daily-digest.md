# AI 产品日报 | 2026-05-27

> 🔬 422产品实验室 · AI新产品日报 · 每日精选

## 今日洞察

今天的融资信号指向一个清晰的判断：**AI产业的「模型路由层」正在成为新基础设施**。OpenRouter用一年时间从$5.47亿估值翻倍到$13亿，月处理100万亿token——Alphabet旗下CapitalG领投$1.13亿，本质上下注的是「企业不会把自己锁死在单一模型供应商上」。这对创业者的启示是：**做多模型兼容的产品，而不是赌某一个模型的未来**。

与此同时，**企业级AI Agent正从「单机」走向「多人协作」**：Dust拿$4000万做「multiplayer AI」——不是一个人用AI助手，而是整个组织共享Agent的知识和上下文，零流失率+240% NRR说明产品已经嵌入企业工作流。另一边，Ocean用$2800万做「用AI Agent对抗AI钓鱼攻击」——Wiz CEO和Armis创始人集体天使投资，以色列安全老兵的直觉是：AI生成钓鱼邮件的威胁已经超出了传统安全产品的应对能力。

国内方面，华为「具身大脑一号位」朱森华创办的具脑磐石完成亿元级新融资，选择与杨立昆同源的JEPA路线做类脑认知世界模型。用1/10数据量达到同等效果——这条「反Scaling Law」的路线正在全球范围内获得资本背书。

---

## 1. OpenRouter — $1.13亿Series B，$13亿估值，AI模型的「交换机」成为基础设施

**融资信息**：$1.13亿Series B。CapitalG（Alphabet成长基金）领投。此前a16z、Menlo Ventures、Sequoia参投的Series A为$4000万（2025年6月），估值约$5.47亿。一年内估值翻倍至约$13亿

**做什么的**：AI模型路由网关——帮助企业和开发者在一个平台上接入400+AI模型（Anthropic、Google、OpenAI、xAI、DeepSeek等），根据任务需求智能选择最合适的模型。8百万全球用户，月处理约100万亿token（半年前5万亿/周→现在25万亿/周，5倍增长）

**为什么值得关注**：
- **CapitalG领投——Google在自己的AI之外，投资了「多模型未来」**：Alphabet的投资部门投了一个让企业可以在Google模型和竞品之间自由切换的平台。这说明Google相信：AI产业的终局不是一家模型独大，而是多模型共存
- **100万亿token/月——数据证明了「模型商品化」趋势**：企业不会把自己锁死在单一模型上。OpenRouter的5倍增长说明，多模型策略已经从「先进做法」变成了「标准做法」
- **从训练→推理→Agent，每一步都在推高路由层价值**：当Agent需要调用多个模型完成复杂任务时，模型路由器就是Agent时代的DNS
- **创业者启示**：**如果你的AI产品只接了一个模型，你正在给自己挖坑**。OpenRouter的增长证明：模型层在快速商品化，真正的差异化在产品层和用户体验层。做多模型兼容不是「nice to have」而是「must have」

**类比参考**：AI模型版的「Cloudflare」——Cloudflare让网站在多个CDN之间智能路由，OpenRouter让应用在多个模型之间智能路由。或者「AI模型界的API Gateway + CDN」

![OpenRouter](/tmp/daily-screenshots/openrouter.png)

🔗 [TechCrunch](https://techcrunch.com/2026/05/26/openrouter-more-than-doubles-valuation-to-1-3b-in-a-year/) | [官网](https://openrouter.ai)

---

## 2. Ocean — $2800万，Lightspeed领投，用AI Agent对抗AI生成的钓鱼攻击

**融资信息**：$2800万。Lightspeed Venture Partners领投，Picture Capital、Cerca Partners参投。天使投资人包括Wiz CEO Assaf Rappaport和Armis联合创始人Yevgeny Dibrov、Nadir Izrael。创始人Shay Shwartz为前以色列国防网络安全专家（参与铁穹系统相关工作）

**做什么的**：AI Agent驱动的邮件安全平台——部署专用小型语言模型（SLM）分析邮件上下文、评估发送者意图、与组织行为模式比对。已为Kayak、Kingston Technology、Headspace等客户每月处理数十亿封邮件。核心理念：AI已经自动化了鱼叉式钓鱼攻击，传统安全产品无法应对

**为什么值得关注**：
- **Wiz CEO + Armis创始人天使投资——以色列安全圈的集体判断**：这三个名字代表以色列网络安全领域的顶尖成功案例。他们同时投一个邮件安全项目，说明他们看到了现有安全产品的系统性盲区
- **「AI对抗AI」——安全赛道的新范式**：攻击者用AI生成高度个性化的钓鱼邮件，防御者也必须用AI Agent来识别AI生成的攻击。这不是工具升级，是范式转换
- **专用小模型（SLM）而非通用大模型——工程选择的智慧**：邮件安全不需要GPT-4级别的推理，需要的是「低延迟、高精度、可审计」的判断。Ocean选择专用SLM，意味着更低的成本和更快的响应
- **月处理数十亿封邮件——已经是production规模**：Kayak和Headspace不是试点客户，是生产环境部署。这说明产品在真实场景中已经验证
- **创业者启示**：**「AI增强的攻击」正在创造一个全新的安全品类**。传统邮件安全（Proofpoint、Mimecast）是用规则和签名检测，AI钓鱼攻击绕过这些规则就像绕过一个红绿灯一样简单。这是一个被AI创造出来的新市场

**类比参考**：邮件安全版的「CrowdStrike」——CrowdStrike用AI检测端点威胁，Ocean用AI Agent检测邮件威胁。或者「AI时代的Proofpoint，但安全架构从零重建」

![Ocean](/tmp/daily-screenshots/ocean.png)

🔗 [The AI Insider](https://theaiinsider.tech/2026/05/26/ocean-closes-28m-to-fight-ai-powered-phishing-with-agentic-email-security/)

---

## 3. Dust — $4000万Series B，零流失率+240% NRR，「多人AI」重新定义企业Agent

**融资信息**：$4000万Series B。Abstract和Sequoia联合领投，Snowflake Ventures和Datadog参投。总融资超过$6000万

**做什么的**：「多人」企业AI Agent平台——让AI Agent在整个组织内协作，而非服务于单个用户。连接100+数据源，内置记忆、反馈循环和企业治理。3000+组织使用，周活跃率70%+，2025年NRR 240%、零流失。Vanta 900人团队每周节省数千小时，Persona 11个部门部署300+Agent

**为什么值得关注**：
- **零流失率——企业SaaS的圣杯**：任何企业SaaS产品如果能做到零流失，说明它已经从「工具」变成了「基础设施」。Dust在3000+组织中做到了这一点
- **「多人AI」vs「单机AI」——Viktor之后的第二个信号**：昨天日报的Viktor做「团队AI同事」，今天Dust做「组织AI协作」。两个独立公司在同一周融资，说明「多人AI」是一个趋势而非个案
- **240% NRR——客户在疯狂扩容**：净收入留存率240%意味着客户第二年的付费是第一年的2.4倍。这只能用「产品深入企业工作流」来解释
- **创始人来自OpenAI——Stanislas Polu曾是Greg Brockman团队的研究工程师**：他从OpenAI离开时认为「模型已经足够强，缺的是产品层」。这个判断正在被验证
- **创业者启示**：**「AI Agent的最大价值不在个人效率，而在组织协作」**。如果你的AI产品只服务个人用户，天花板是效率工具；如果你能让Agent在团队间共享上下文和知识，天花板是组织操作系统

**类比参考**：AI Agent版的「Slack」——Slack让团队沟通从邮件变成实时协作，Dust让AI从个人助手变成团队协作系统。或者「企业版的ChatGPT，但有组织记忆」

🔗 [The AI Insider](https://theaiinsider.tech/2026/05/25/dust-raises-40m-to-make-ai-multiplayer-inside-the-enterprise/) | [官网](https://dust.tt)

---

## 4. Perceptic — $1200万Seed，Accel领投，前Palantir三人组做AI药物发现的「操作系统」

**融资信息**：$1200万Seed。Accel领投，Air Street Capital、Elder Gull参投。伦敦

**做什么的**：端到端AI药物发现平台——不是优化药物发现流程中的某个环节（蛋白质结构预测、分子设计、临床试验），而是做连接所有环节的「操作系统」。模型和数据无关（model agnostic），药企可以接入自己的数据和模型。已有CSL等顶级药企客户，将科学尽调从数周压缩到数小时

**为什么值得关注**：
- **Accel从「团队还在Palantir时」就开始跟踪——投资人的前瞻性**：Accel合伙人Sonali De Rycker在Perceptic创始人还没离职时就开始关注他们。这说明顶级VC的投资逻辑是「赌人」而非「赌项目」
- **「连接层」而非「点工具」——AI在制药行业的正确姿势**：大多数AI制药公司（Isomorphic、Recursion、Insilico）专注某个环节。Perceptic选择做「连接所有环节的操作系统」——这个定位在SaaS领域已经被证明（ERP之于制造业）
- **可溯源、零幻觉——制药行业的刚需**：药企不能容忍AI幻觉。Perceptic的每一个结论都可以追溯到源头数据。这个「审计能力」是进入药企的门票
- **50倍临床数据提取效率提升——ROI不是PPT上的数字**：具体的效率提升数据让产品价值可量化
- **创业者启示**：**在垂直行业中，「连接层」的价值可能大于「点解决方案」**。当一个行业有太多孤立的AI工具时，做把它们连起来的平台往往比做第N个点工具更有价值

**类比参考**：药物发现版的「Palantir Foundry」——Palantir帮政府和金融连接分散的数据源，Perceptic帮药企连接分散的AI工具和数据。或者「制药行业的AI中间件」

![Perceptic](/tmp/daily-screenshots/perceptic.png)

🔗 [Fortune独家](https://fortune.com/2026/05/26/exclusive-perceptic-a-startup-automating-drug-discovery-end-to-end-for-big-pharma-emerges-from-stealth-with-12-million-in-seed-funding/)

---

## 5. Commure — $7000万，$70亿估值，医疗AI Agent完成85%收入周期工作

**融资信息**：$7000万，$70亿post-money估值。General Catalyst领投，Sequoia Capital、Morgan Stanley、Kirkland & Ellis参投

**做什么的**：医疗管理AI Agent平台——覆盖500+医疗机构和3000+诊疗站点，AI Agent完成85%以上的收入周期工作（电话、笔记、编码、理赔、申诉）无需人工干预。客户包括HCA Healthcare和Tenet Healthcare

**为什么值得关注**：
- **$70亿估值——医疗AI赛道最大的公司之一**：Commure不是初创公司了，而是一个成熟平台。但$7000万新融资说明投资人认为它还有巨大的增长空间
- **85%自动化——不是copilot，是autonomous agent**：CEO Tanay Tandon明确说「AI现在可以完成过去30年软件都没能自动化的工作」。这个数字如果准确，说明AI Agent在医疗管理场景已经越过了「可用」的临界点
- **General Catalyst的CEO亲自背书**——「不是copilot功能，而是全新方式」：Hemant Taneja的措辞非常刻意——他在强调Commure不是在旧系统上加AI，而是用AI重建工作流
- **HCA Healthcare是客户——美国最大医院系统之一**：如果Commure进入了HCA，它实际上已经进入了美国医疗体系的核心
- **创业者启示**：**医疗管理是美国最肥的AI垂直场景之一——$1万亿年度行政成本**。不是临床AI（FDA审批难），而是管理AI（理赔、编码、账单），这块市场大、合规要求低、ROI可量化

**类比参考**：医疗管理版的「UiPath」——UiPath用RPA自动化企业流程，Commure用AI Agent自动化医疗管理流程。或者「医疗行业的AI收入周期管理平台」

![Commure](/tmp/daily-screenshots/commure.png)

🔗 [The AI Insider](https://theaiinsider.tech/2026/05/26/commure-secures-70m-at-7b-valuation-to-deploy-ai-agents-across-healthcare-administration/) | [官网](https://www.commure.com)

---

## 6. Avrea — $470万Pre-Seed，Earlybird领投，Aiven联合创始人做AI代码时代的CI/CD

**融资信息**：$470万Pre-Seed。Earlybird Venture Capital领投。赫尔辛基。创始人Hannu Valtonen（Aiven联合创始人，曾打造独角兽）和Juha Valvanne（Nosto联合创始人）。10人团队来自Spotify和Hoxhunt。融资在几周内完成，没有使用Pitch Deck

**做什么的**：AI代码时代的CI/CD加速平台——解决AI编码工具（GitHub Copilot、Cursor、Claude Code）带来的代码量爆炸导致CI/CD成为瓶颈的问题。接入现有部署平台，用AI Agent自动发现测试质量问题、构建卡点、资源瓶颈。目标是让开发者减少等待、更多时间写代码

**为什么值得关注**：
- **Aiven联合创始人的第二次创业——从基础设施到开发工具**：Aiven是开源数据库托管领域的独角兽。Valtonen的第二次创业选了CI/CD赛道，说明他认为「AI编码→CI/CD瓶颈」是一个基础设施级别的问题
- **没有Pitch Deck就拿到term sheet——「赌人」型投资的极致**：Earlybird是Aiven的投资人，再次投了同一个创始人。几周完成融资，没有PPT——这是「创始人 reputational capital」的最好证明
- **「AI编码的副产品是CI/CD崩溃」——一个被低估的二阶效应**：Google CEO说75%新代码是AI生成的。代码量爆炸意味着CI/CD管道需要处理更多构建——而现有的GitHub Actions和GitLab CI/CD不是为这个量级设计的
- **GitHub和GitLab的潜在威胁**——它们建于2000年代末**：Avrea不是在现有CI/CD上加AI功能，而是重新思考「AI代码时代的软件交付流程应该长什么样」
- **创业者启示**：**当你看到一个大趋势（AI编码），不要只关注趋势本身，要关注它的二阶效应**。AI编码→代码量爆炸→CI/CD瓶颈→需要新的交付基础设施。这个因果链就是Avrea的商业逻辑

**类比参考**：CI/CD版的「Aiven」——Aiven把开源数据库变成托管服务解决运维瓶颈，Avrea把CI/CD重建为AI原生解决交付瓶颈。或者「AI代码时代的GitHub Actions替代品」

🔗 [官网](https://avrea.com) | [TFN](https://techfundingnews.com/avrea-preseed-earlybird-ai-generated-code/)

---

## 7. 具脑磐石 — 亿元级新融资，华为「具身大脑一号位」创业，对标杨立昆JEPA路线

**融资信息**：亿元级新融资。具深厚类脑与具身产业背景的顶尖产业资本领投，老股东及多家顶尖基金复投跟投。更新一轮融资同步交割中。创始人朱森华，前华为云AI算法创新Lab主任、华为具身智能大脑开创者

**做什么的**：类脑认知世界模型——不采用行业主流的VLA（视觉-语言-动作）路线，而选择与Yann LeCun同源的JEPA（联合嵌入预测架构），构建能理解物理因果、具备抽象学习能力的「认知世界模型」。用1/10的数据量达到传统路线同等效果。目标是具身智能2.0——低功耗、高泛化、终身学习

**为什么值得关注**：
- **华为「具身大脑一号位」创业——团队含金量极高**：朱森华不仅搭建了华为云脑平台，还是「华为天才少年」面试官。核心团队来自华为、清华、北大、中科院、旷视、极智嘉——这是工程化能力+学术深度的罕见组合
- **JEPA路线——杨立昆刚拿到$10.3亿融资验证方向**：Yann LeCun的AMI Labs在2026年3月完成$10.3亿种子轮，$35亿估值。具脑磐石在中国走同一路线，意味着全球AI领域对「反Scaling Law」路线的资本共识正在形成
- **1/10数据量达到同等效果——如果成立，是颠覆性的**：具身智能1.0的问题是数据饥渴——需要海量演示数据训练机器人。如果JEPA路线真的能用1/10数据达到同等效果，它将大幅降低具身智能的落地成本
- **「海外优先突破」的商业策略——差异化定价**：国内客户看ROI，海外客户为劳动力短缺买单。这个策略很务实——在机器人能力还不够替代人工的阶段，先卖给那些「没有选择」的市场
- **创业者启示**：**在具身智能赛道，「跟VLA大流」是红海，「走类脑路线」是蓝海但高风险**。具脑磐石的选择说明：当行业共识走向一个方向时，站在共识的对立面可能需要更多勇气，但也可能收获更大的回报

**类比参考**：具身智能版的「DeepSeek」——DeepSeek在LLM领域用更低成本达到同等效果，具脑磐石在具身智能领域用更少数据达到同等效果。或者「中国的LeCun路线具身智能团队」

🔗 [36氪/投中网](https://36kr.com/p/3824043619012996)

---

## 8. Mirage — GitHub 2677 Stars，AI Agent的统一虚拟文件系统

**融资信息**：独立开源项目（strukto-ai开发）。GitHub 2677 Stars。TypeScript + Python双SDK。Apache 2.0开源协议

**做什么的**：AI Agent的统一虚拟文件系统——把S3、Google Drive、Slack、Gmail、GitHub、Redis等所有后端服务挂载到一个虚拟文件树上。AI Agent用同一套Unix命令（grep、cat、cp）操作所有服务，无需学习N个SDK和M个MCP。兼容OpenAI Agents SDK、LangChain、Pydantic AI、Claude Code等主流框架

**为什么值得关注**：
- **「把所有服务变成文件系统」——极简的抽象**：AI模型最擅长的是什么？是bash和Unix命令（因为训练数据里最多）。Mirage不教Agent新词汇，而是让Agent用最熟悉的工具操作所有服务。这个设计哲学太对了
- **2677 Stars——开发者社区的快速验证**：不是营销驱动的增长，是开发者看到「bash everywhere」的理念后自发star
- **解决了Agent开发的「碎片化」痛点**：当前Agent开发者最大的痛苦之一就是——每个服务有不同API、不同认证、不同数据格式。Mirage把它们统一成文件操作，大幅降低了Agent的开发门槛
- **「Agent时代的Plan 9」——操作系统层面的创新**：Plan 9是Unix团队做的实验性OS，核心理念是「everything is a file」。Mirage把这个理念带入了Agent世界
- **创业者启示**：**在Agent生态中，「抽象层」比「功能层」更有价值**。Mirage不做Agent本身，它做的是让所有Agent都能更简单地访问所有服务的基础设施。类似Docker之于容器——Docker不运行应用，它让应用更容易运行

**类比参考**：AI Agent版的「Docker + FUSE」——Docker统一了应用部署环境，Mirage统一了Agent的数据访问接口。或者「Agent的虚拟操作系统」

🔗 [GitHub](https://github.com/strukto-ai/mirage) | [文档](https://docs.mirage.strukto.ai)

---

## 9. allO — $1400万Series A，慕尼黑，AI原生餐厅操作系统

**融资信息**：$1400万Series A。Zigg Capital领投，LifeX Ventures、Aperture、Wecken & Cie.、20VC、Keen Venture Partners参投。慕尼黑

**做什么的**：AI原生餐厅操作系统——把预订、POS、库存、扫码点餐、会计、支付、外卖集成在一个AI驱动的平台上。核心策略：服务于被现有SaaS忽视的本地餐厅和民族餐厅。Munich-based

**为什么值得关注**：
- **Zigg Capital领投——餐饮科技赛道的专业VC**：Zigg Capital专注餐饮科技投资，投allO说明他们认为「AI原生」比「传统SaaS+AI」在餐饮赛道有结构性优势
- **服务被忽视的餐厅——差异化定位**：大多数餐饮SaaS瞄准连锁品牌，allO聚焦本地小餐厅和民族餐厅。这些餐厅数量庞大但数字化程度低，AI可以帮他们跳过传统SaaS阶段直接进入AI时代
- **「一站式」vs「碎片化」——餐饮SaaS的终局之争**：餐厅通常用20个不同工具（OpenTable预订、Square POS、DoorDash外卖...）。allO用AI把这些功能全部集成，对小餐厅来说这比拼凑20个工具便宜得多
- **从德国出发，瞄准欧洲——地缘优势**：德国和欧洲的餐饮数字化程度远低于美国，市场空间更大
- **创业者启示**：**AI原生SaaS最大的机会在「数字化程度低的行业」**：美国SaaS已经渗透了大部分行业，但在欧洲和亚洲的本地服务业，很多还是Excel+纸质流程。AI可以帮他们直接从「前数字化」跳到「AI时代」

**类比参考**：餐厅版的「Shopify」——Shopify帮小商家建立在线商店，allO帮小餐厅建立AI驱动的运营系统。或者「Toast（美国餐饮SaaS）的欧洲AI版」

🔗 [TFN](https://techfundingnews.com/allo-14m-series-a-zigg-capital/) | [官网](https://allo.restaurant)

---

## 📊 今日趋势总结

| 趋势 | 信号 |
|------|------|
| 🔀 模型路由层成为基础设施 | OpenRouter $1.13亿、一年估值翻倍——企业不做单模型赌徒，多模型是标配 |
| 👥 企业AI从「单机」到「多人」 | Dust零流失+240% NRR、Viktor 10周$15M ARR——「组织AI」不是概念，是数据验证的现实 |
| ⚔️ AI vs AI安全对抗 | Ocean $2800万、Wiz/Armis创始人集体投资——攻击者用AI钓鱼，防御者也必须用AI |
| 🏥 医疗管理AI Agent越界 | Commure $70亿估值、85%自动化——30年未自动化的医疗行政被AI攻破 |
| 🧠 类脑路线资本共识形成 | 具脑磐石亿元融资、杨立昆$10.3亿——「反Scaling Law」不再只是论文，是创业路线 |
| 🔧 AI编码的二阶效应 | Avrea $470万——AI生成代码爆炸→CI/CD崩溃→需要新基础设施 |

---

> 📌 **422产品实验室**出品 | 每日精选AI新产品、融资、创新模式
>
> 关注我们，获取面向创业者的AI产品情报

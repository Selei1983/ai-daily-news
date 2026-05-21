# AI 产品日报 | 2026-05-21

> 🔬 422产品实验室 · AI新产品日报 · 每日精选

## 今日洞察

今天最重要的信号是**「AI Agent正在从软件界面渗透进每一个已存在的工作流」**。同一天内三条线索交汇：Viktor把AI Coworker嵌入Slack/Teams，10周做到$15M ARR——这是2026年ToB SaaS最快增速之一；Unframe用预构建模块化组件让企业「一天上线定制AI应用」，12个月拿下$100M合同额；Contrario不替代猎头而是「武装」猎头，6个月$6M ARR。

与此同时，**「AI对抗AI」的安全赛道正式进入资本加速期**：Ocean以$28M从隐身出来，用Agent对抗AI钓鱼攻击——创始人曾是少年黑客和以色列铁穹系统研究员。Stilta以「Cursor for Patent Lawyers」拿到a16z和YC的$10.5M——不是AI替代律师，而是AI让律师的每个动作都自带上下文。

对创业者来说，今天的核心判断是：**最高ROI的AI产品不是「创造新场景」，而是「嵌入现有工作流，让已有动作变快10倍」**。Viktor没有做新App，而是住在Slack里；Contrario没有替代猎头，而是给猎头装上AI外骨骼。找到用户已经每天在做的事，把AI嵌进去——这是2026年最被验证的go-to-market策略。

---

## 1. Viktor — $75M Series A，住在Slack里的AI同事，10周$15M ARR

**融资信息**：$75M Series A，Accel领投，Bek Ventures、Kaya VC、Inovo VC等跟投。波兰华沙+慕尼黑，波兰历史上最大A轮。创始人Fryderyk Wiatrowski，团队来自Meta

**做什么的**：AI Coworker——直接运行在Slack和Microsoft Teams（即将支持）里，连接3000+企业工具，不只是回答问题，而是「做工作」：拉报表、管理广告活动、建Dashboard、研究客户线索、写代码。理念是「Not a tool. A hire.」（不是工具，是员工）。已有13,000+ workspace安装。

**为什么值得关注**：
- **10周$15M ARR——SaaS创业史上最快增速之一**：从0到$15M年化收入只用了10周。这个数字比大多数SaaS公司3年的增长都快。信号是：**用户不需要「又一个AI App」，他们需要AI住进他们已经在用的工具里**
- **13,000+ workspace——「嵌入vs独立」的路线之争有了答案**：Viktor没有做独立App，而是选择住在Slack里。CEO说得很清楚：「Slack beats web apps for AI coworkers by redefining 'fast'」。用户不需要切换窗口，在已有对话流里直接@Viktor就能做事
- **3000+工具集成——Agent的「手」越多越有用**：能连Salesforce、HubSpot、Jira、GitHub、Notion等3000+工具。这意味着Viktor不是聊天机器人，而是真正能操作你公司系统的AI员工
- **$75M A轮——Accel押注「AI原生SaaS」的定价**：波兰创始团队拿到该国历史最大A轮。Accel的判断是：AI Coworker不是功能增强，而是新的企业软件品类
- **创业者启示**：**「住在用户已经在用的界面里」是AI Agent最被低估的分发策略**。不需要教育用户打开新App，只需要在他们每天停留的Slack/Teams/微信里出现。Viktor证明了「嵌入」比「独立」的获客成本低一个数量级

**类比参考**：Slack版的「Devin」——Devin在浏览器里做开发者的事，Viktor在Slack里做运营/销售/市场的事。或者「企业版的Siri，但真的能做事」

![Viktor](/tmp/daily-screenshots/viktor.png)

🔗 [官网](https://getviktor.com) | [TNW报道](https://thenextweb.com/news/viktor-75-million-series-a-accel-ai-coworker-slack-teams)

---

## 2. Decart — $300M，实时世界模型，估值$40亿，为物理AI造基础设施

**融资信息**：$300M融资，估值约$40亿。Radical Ventures领投，Nvidia、Sequoia参投。以色列团队。同时发布DOS 2.0平台

**做什么的**：实时世界模型（Real-time World Models）+ AI优化基础设施。核心产品包括：DOS平台（AI推理优化中间件，让模型在任意芯片上高效运行）和实时世界模型（让AI系统实时理解和预测物理世界，为机器人和自动驾驶服务）。目标是为「Physical AI」提供底层基础设施。

**为什么值得关注**：
- **$300M + $40亿估值——「物理AI基础设施」被重注**：当大多数AI投资还在LLM应用层时，Decart拿到了2026年最大单笔之一去建「AI理解物理世界」的基础设施。Nvidia亲自参投，说明芯片巨头认为这是计算需求的下一个增长引擎
- **「世界模型」vs「语言模型」——AI的下一个范式**：语言模型理解文字，世界模型理解物理空间。如果LLM是AI学会了「读」，世界模型就是AI学会了「看和感知」。这对机器人、自动驾驶、工业自动化是质变
- **DOS 2.0——让模型在任何芯片上跑得更快**：不只做模型，还做模型的「编译器」。DOS平台让AI推理在任意芯片（Nvidia/AMD/Amazon Trainium）上高效运行。这是「AI时代的操作系统」
- **实时是关键差异**：不是离线生成，而是实时推理和预测。这对自动驾驶（毫秒级反应）、机器人（实时避障）等场景是刚需
- **创业者启示**：**「AI基础设施层」正在从「模型训练」向「推理优化」和「世界模型」两个方向分化**。推理优化是让现有模型跑得更快更便宜，世界模型是让AI理解物理世界。两者都是百亿级市场

**类比参考**：AI版的「英伟达CUDA + 虚幻引擎」——CUDA让GPU计算标准化，DOS让AI推理标准化；虚幻引擎模拟虚拟世界，Decart的World Model模拟物理世界。或者「Physical AI的基础设施三件套：编译器+运行时+世界引擎」

![Decart](/tmp/daily-screenshots/decart.png)

🔗 [官网](https://decart.ai) | [TNW报道](https://thenextweb.com/news/decart-300-million-radical-ventures-world-models)

---

## 3. Unframe — $50M Series B，企业AI「乐高」，12个月$100M合同额

**融资信息**：$50M Series B，Highland Europe领投。累计融资$100M。创始人Shay Levi，以色列公司。12个月内Total Contract Value突破$100M，400%净收入留存率（NRR）

**做什么的**：企业AI交付平台——通过预构建的模块化组件（pre-built modular components），让企业快速定制和部署AI应用。不需要从零开发，而是像搭乐高一样组合已有模块，一天内上线定制化AI解决方案。解决的是企业「想用AI但不知道从哪里开始、也不想等6个月开发」的痛点。

**为什么值得关注**：
- **12个月$100M TCV——企业AI赛道最快的商业化记录之一**：大多数AI初创公司第一年在找PMF，Unframe第一年已经在签百万级合同。400% NRR说明客户不仅续约，还在大幅加购
- **「乐高式AI应用」解决了企业的两个核心恐惧**：企业怕什么？一是开发周期长（Unframe说一天上线），二是锁定在某个模型上（Unframe是模型无关的）。这两个恐惧的解法就是「预构建模块+即插即用」
- **400% NRR——客户在疯狂扩展使用场景**：净收入留存率400%意味着现有客户每年的支出是前一年的4倍。这说明Unframe不是做一单生意，而是成为企业的「AI操作系统」，每个新场景都是加购机会
- **模型无关——在模型战争中最安全的位置**：不绑定GPT或Claude，企业可以随时切换底层模型。在模型快速迭代的2026年，这个灵活性是刚需
- **创业者启示**：**「AI应用的模块化交付」是一个正在形成的独立品类**。当每个企业都想用AI但不想从零开发时，提供一个「AI应用模板商店+快速定制能力」的平台就能吃到这个爆发需求。Unframe做的是「AI版的Shopify」——Shopify让开网店变简单，Unframe让上AI变简单

**类比参考**：AI版的「Shopify + Zapier」——Shopify让开店变简单，Unframe让AI应用上线变简单；Zapier串联SaaS，Unframe串联AI能力。或者「企业AI的CMS（内容管理系统）」

![Unframe](/tmp/daily-screenshots/unframe.png)

🔗 [官网](https://www.unframe.ai) | [TNW报道](https://thenextweb.com/news/unframe-50-million-highland-europe-enterprise-ai-delivery)

---

## 4. Ocean — $28M出隐身，用AI Agent对抗AI钓鱼攻击，前少年黑客+铁穹研究员创办

**融资信息**：$28M总融资（$20M Series A + 早期资金）。Lightspeed Venture Partners领投，Picture Capital参投。纽约，创始人Shay Shwartz

**做什么的**：Agentic Email Security Platform——用AI Agent对抗AI生成的钓鱼邮件。当攻击者用AI批量生成个性化钓鱼邮件时，传统规则匹配的邮件安全方案已经不够用。Ocean部署AI Agent实时分析每封邮件的意图、上下文和行为模式，检测AI生成的钓鱼攻击。

**为什么值得关注**：
- **「AI攻击AI」——安全赛道的新范式**：当攻击者开始用AI生成钓鱼邮件（个性化、语法完美、上下文精准），传统基于规则和签名匹配的安全方案彻底失效。Ocean的逻辑是：只有AI才能打败AI
- **创始人的「黑客→铁穹→创业者」路径**：Shay Shwartz少年时是黑客，被抓后在以色列国防军研发铁穹（Iron Dome）反导系统的网络安全部门工作。从攻击者视角到防御者视角到产品化——这个路径本身就是竞争力
- **Agentic安全——不只是检测，是自主响应**：Ocean的Agent不只是发现可疑邮件，还能自主采取行动——隔离、分析、溯源、生成防御策略。这是从「告警工具」到「自主防御系统」的升级
- **邮件是最大的攻击面**：91%的网络攻击始于钓鱼邮件。AI让钓鱼攻击的成本降低了100倍——以前需要人工写的个性化邮件现在可以批量生成。需求是刚性的、增长的
- **创业者启示**：**「AI生成的攻击需要AI驱动的防御」——这是一个供需同步爆发的市场**。当AI降低了攻击成本，防御也必须升级。同样的逻辑适用于：AI生成假视频→AI检测假视频，AI生成假评论→AI识别假评论

**类比参考**：邮件安全版的「CrowdStrike」——CrowdStrike用AI保护终端，Ocean用AI保护邮箱。或者「铁穹系统的企业邮件版——导弹是钓鱼邮件，拦截弹是AI Agent」

![Ocean](/tmp/daily-screenshots/ocean.png)

🔗 [官网](https://www.ocean.security) | [TechCrunch报道](https://techcrunch.com/2026/05/19/from-teen-hacker-to-iron-dome-researcher-this-founder-raised-28m-to-fight-ai-phishing/)

---

## 5. Stilta — $10.5M Seed，专利律师的Cursor，a16z + YC联合押注

**融资信息**：$10.5M Seed轮。a16z领投，YC参投，OpenAI、Lovable、Legora等战略投资人跟投。斯德哥尔摩，YC 2025批次

**做什么的**：专利诉讼和检索的AI Agent平台——自称为「Cursor for Patent Practitioners」。AI Agent能深度分析prior art（现有技术文献）、生成专利申请、辅助专利诉讼。核心是「source-backed, auditable analysis at scale」——每个AI分析都有可追溯的来源引用，这在法律领域是刚需。

**为什么值得关注**：
- **a16z + YC + OpenAI三方联合——法律AI赛道获顶级资本共识**：三个AI领域最重要的玩家同时出现在一轮Seed里，说明「AI+法律」不再是小众赛道。特别是OpenAI作为投资方出现，暗示Stilta可能深度集成GPT能力
- **「Cursor for X」的品类验证**：Stilta的成功进一步验证了「把Cursor的模式复制到垂直领域」是一个可复制的创业方法论。Cursor让开发者AI-native地写代码，Stilta让专利律师AI-native地做检索和申请
- **可审计性（Auditability）是法律AI的生死线**：律师不能引用AI的幻觉。Stilta的每个分析都附带源文件引用，这在法律领域不是nice-to-have而是must-have。这个设计选择决定了产品能不能真正被律师使用
- **专利诉讼是法律的「高利润区」**：一个专利诉讼案子动辄数百万美元律师费。Stilta切入的是法律领域最赚钱的细分市场
- **创业者启示**：**「Cursor for X」是一个已被验证的创业公式**。找到专业知识密集、信息检索量大、错误成本高的垂直领域，把Cursor的「AI-native编辑+Agent辅助」模式复制过去。下一个可能是：Cursor for Compliance、Cursor for Tax、Cursor for Audit

**类比参考**：法律版的「Cursor」——Cursor让开发者AI写代码，Stilta让专利律师AI做检索。或者「Harvey AI的专利专用版，但更像IDE而非聊天框」

![Stilta](/tmp/daily-screenshots/stilta.png)

🔗 [官网](https://www.stilta.com) | [TechCrunch报道](https://techcrunch.com/2026/05/19/legal-tech-announced-stilta-announces-10m-seed-backed-by-yc-and-a16z-months-after-launch/) | [YC](https://www.ycombinator.com/companies/stilta)

---

## 6. Quartermaster — $43M，给全球商船装AI传感器，打造「海洋蜂群思维」

**融资信息**：$43M融资，Steel Atlas领投。产品SmartMast™。美国公司

**做什么的**：海事AI感知网络——在商用船只上安装SmartMast传感器硬件（摄像头+信号监测），把全球商船变成分布式感知节点，实时构建全球海洋的「共享态势感知」。目标是成为海洋的实时情报层——让每一艘船都能「看到」周围的海域发生了什么。

**为什么值得关注**：
- **「把现有船变成传感器」vs「发射卫星」——1000倍成本优势**：传统海洋监控靠卫星和巡逻机，成本极高。Quartermaster的思路是：全球有数百万艘商船在海上跑，给它们装上便宜传感器就能实现全球覆盖。据说比传统方案便宜1000倍
- **「蜂群思维」是AI+IoT的终极形态**：不是一艘船的AI，而是所有船共享感知数据的集体智能。每艘船既是数据生产者也是消费者——上传自己看到的，下载别人看到的。这是去中心化AI的物理实现
- **海事是AI最未被渗透的万亿级市场**：全球90%的贸易走海运，但海洋的实时感知能力接近零。走私、海盗、非法捕捞、海上事故——这些问题在AI之前几乎没有技术方案
- **硬件+软件+网络的整合壁垒**：不是纯软件公司，需要造传感器、装到船上、建数据网络、做AI分析。这个整合壁垒比纯SaaS高得多，但护城河也深得多
- **创业者启示**：**「给现有物理资产加装AI感知能力」是一个被低估的品类**。Quartermaster的思路可以复制到：给卡车装AI感知（公路蜂群）、给农场装AI感知（农业蜂群）、给建筑工地装AI感知（工地蜂群）。关键是找到「已有大量分布资产但缺乏智能」的场景

**类比参考**：海洋版的「Waze + Starlink」——Waze让每辆车变成交通传感器，Quartermaster让每艘船变成海洋传感器；Starlink建天基网络，Quartermaster建海基网络。或者「海洋的Nest摄像头网络」

![Quartermaster](/tmp/daily-screenshots/quartermaster.png)

🔗 [官网](https://www.quartermaster.us) | [TechCrunch报道](https://techcrunch.com/2026/05/20/quartermaster-is-building-a-maritime-hive-mind/)

---

## 7. Contrario — $6M ARR半年达成，AI武装猎头而非替代猎头，斯坦福辍学生创办

**融资信息**：$2.3M Pre-seed/Seed。YC校友。斯坦福辍学生Arya和Adi创办。旧金山

**做什么的**：AI驱动的招聘平台——核心模式是「AI Agent + 人类猎头」协同。Contrario不是替代猎头，而是给猎头装上AI外骨骼：AI做候选人筛选、简历分析、面试排期、跟进提醒，猎头做关系维护和最终判断。已向平台猎头支付超过$100万佣金。

**为什么值得关注**：
- **6个月$6M ARR + 支付$100万+佣金——单位经济模型被验证**：不是VC烧钱换增长，而是平台已经产生了真实的佣金流动。$100万+支付给猎头说明这个模式不是「AI取代人」而是「AI赋能人」
- **「AI武装人」vs「AI替代人」——哪个商业模式更好？**：Contrario选择了后者。结果：猎头变成了超级猎头（效率10x），候选人得到更好的匹配，企业更快招到人。三赢
- **人才池已有2000+常春藤申请者**：从高端人才切入，确保平台上有「买方想买的人」。这是双边市场的经典启动策略
- **Stanford辍学生——又一个「辍学创业」故事**：YC的基因在Contrario身上很明显——快速上线、用数据说话、不过度设计
- **创业者启示**：**「AI增强而非替代」可能是被低估的商业模式**。大多数人想到AI + 某行业时，第一反应是「用AI替代这个行业的从业者」。但Contrario证明了：让从业者变强10倍，比替代他们，商业化路径更短、信任壁垒更低、客户转化更容易

**类比参考**：招聘版的「Copilot」——GitHub Copilot没有替代程序员而是让他们变快，Contrario没有替代猎头而是让他们变强。或者「猎头行业的外骨骼」

![Contrario](/tmp/daily-screenshots/contrario.png)

🔗 [官网](https://contrario.ai) | [VentureBeat报道](https://venturebeat.com/business/contrario-launches-the-case-for-pairing-ai-agents-with-human-recruiters-instead-of-replacing-them)

---

## 📊 今日趋势总结

| 趋势 | 信号 |
|------|------|
| 🏢 AI嵌入已有工作流 | Viktor 10周$15M ARR——住在Slack里比做独立App获客快10倍 |
| 🏗️ Physical AI基础设施崛起 | Decart $300M建世界模型——从语言AI到物理AI的范式切换 |
| 🛡️ AI对抗AI安全赛道 | Ocean $28M——AI钓鱼攻击催生AI防御Agent |
| 📐 AI应用模块化交付 | Unframe 12个月$100M TCV——企业AI的「乐高化」 |
| ⚖️ 垂直专业AI工具爆发 | Stilta $10.5M——「Cursor for X」创业公式持续验证 |
| 🤝 AI增强而非替代 | Contrario $6M ARR半年——「给从业者装外骨骼」比「替代从业者」ROI更高 |
| 🌊 物理世界AI化 | Quartermaster $43M——给全球商船装AI传感器，海洋变成可感知的网络 |

---

> 📌 **422产品实验室**出品 | 每日精选AI新产品、融资、创新模式
>
> 关注我们，获取面向创业者的AI产品情报

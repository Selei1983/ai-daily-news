# AI 产品日报 | 2026-05-23

> 🔬 422产品实验室 · AI新产品日报 · 每日精选

## 今日洞察

今天最值得关注的信号是**「AI从软件层走向物理层」**。Brett Adcock（Figure.AI创始人）创办的Hark拿下$700M A轮、$60亿估值——他之前用机器人走进物理世界，现在要用AI+硬件重新定义人与数字世界的交互界面。同期，英国芯片公司Fractile拿到$220M做推理专用芯片，要把AI模型从「一个月」的推理时间压缩到「一天」。与此同时，国内具身智能公司自变量机器人完成近20亿元B轮，字节/美团/阿里/小米四家大厂全部押注——这是国内具身智能赛道的标志性事件。

另一条暗线是**「AI开始接管金融和健康这两个最敏感的领域」**：Circle联合创始人创办的Catena Labs拿到$30M A轮，正在申请银行牌照做「AI原生银行」；Tony Robbins联合创办的The Path用$14.3M做AI心理治疗——这两个赛道都意味着AI正在进入「信任成本最高、监管最严」的领域。

对创业者的判断：**2026年Q2的AI创业分两条路——要么深入物理世界（硬件/机器人/芯片），要么深入信任密集型行业（金融/医疗/法律）**。中间的「通用AI应用层」正在被大厂吃掉。

---

## 1. Hark — $700M Series A，$60亿估值，Figure.AI创始人再造一个AI+硬件公司

**融资信息**：$700M Series A，估值$60亿。Parkway Venture Capital领投，Nvidia、AMD Ventures、Intel Capital、Qualcomm Ventures、ARK Invest、Salesforce Ventures等参投。创始人Brett Adcock（Figure.AI、Archer Aviation创始人）。前Apple设计总监Abidur Chowdhury负责产品设计。70人团队，已部署Nvidia B200 GPU数据中心

**做什么的**：通用AI个人助理——正在构建多模态AI模型和专属硬件设备，打造一个能与现有产品和服务无缝对接的AI平台。计划今年夏天发布首批多模态模型，随后推出配套硬件设备。产品细节极其保密，投资人对demo印象深刻。

**为什么值得关注**：
- **$700M A轮——2026年最大的单轮之一**：Brett Adcock自掏$100M启动，A轮直接融了$700M。芯片三巨头（Nvidia/AMD/Intel）和高通同时出现在同一轮，说明整个硬件产业链都在押注「AI+硬件」的消费级产品
- **Adcock的连续创业公式：找到「物理+AI」的交叉点**：Archer做电动飞行器，Figure做人形机器人，Hark做AI个人设备——三次创业都瞄准物理世界和AI的结合。这是一种可复制的创业方法论
- **「为普通人做AI」的定位**：前Apple设计师说得很清楚——「现在的AI产品都在帮人写软件，但没有人真正帮普通人做事」。Hark赌的是消费级AI硬件，不是企业SaaS
- **隐私是核心挑战也是护城河**：AI助理要理解用户生活的全部上下文，但如何不侵犯周围人的隐私？Chowdhury只说了一句：「Sounds like that would make a great product」——这个问题的解法本身就是产品
- **创业者启示**：**当AI软件层的竞争变成红海，AI+硬件的消费级产品是下一个蓝海**。但进入门槛极高——需要同时掌握模型、硬件设计和供应链

**类比参考**：AI版的「Apple初代iPhone时刻」——不只做软件，而是做软硬件一体的体验。或者「Humane AI Pin的梦想版，但这次有$700M和Figure.AI创始人的背书」

![Hark](/tmp/daily-screenshots/hark.png)

🔗 [官网](https://hark.com) | [TechCrunch报道](https://techcrunch.com/2026/05/21/hark-raises-700m-series-a-for-its-secretive-universal-ai-interface/)

---

## 2. Fractile — $220M，AI推理专用芯片，要把「一个月的推理」压缩到「一天」

**融资信息**：$220M融资。Accel、Factorial Funds、Founders Fund联合领投，Conviction、Felicis、8VC等参投。英国公司（伦敦、布里斯托、旧金山、台北）。2022年成立

**做什么的**：AI推理专用芯片——从零开始设计芯片架构，专攻大模型推理的速度瓶颈。核心论点：当今最强AI模型生成1亿token需要一个月，而很多前沿AI应用（药物发现、复杂编程、材料科学）恰恰需要这种超长推理链。Fractile要把这个时间压缩到一天，需要达到~1200 tokens/s的推理速度（目前约40 tokens/s）。

**为什么值得关注**：
- **推理速度是AI的下一个瓶颈——这是一个确定的趋势**：训练已经有人在做（Nvidia主导），但推理优化的空间更大。当模型能力已经足够强，推理速度和成本就成了AI应用落地的真正限制
- **「30x推理加速」如果实现，将解锁全新的AI应用**：很多AI应用今天不可行不是因为模型不够聪明，而是因为推理太慢太贵。如果真的能做到30x加速，药物发现、科学计算、超长链Agent都会变得经济可行
- **Founders Fund + Accel的联合押注**：Peter Thiel的Founders Fund和Accel同时出现在一轮里——前者赌颠覆，后者赌规模。这种组合说明这个赛道既有颠覆性又有规模化路径
- **跨全栈的团队**：从基础AI研究到芯片微架构到晶圆代工工艺，全栈自研。这意味着Fractile不是在做「Nvidia的替代品」，而是在做「完全不同的架构」
- **创业者启示**：**当应用层的竞争转向价格战时，基础设施层的创新价值反而上升**。推理芯片是AI基础设施的「最后一公里」——模型再强，推理太慢太贵就没有商业闭环

**类比参考**：AI推理版的「Nvidia」——但不是做通用GPU，而是做推理专用的架构。或者「AI推理的TPU，但独立于Google」

![Fractile](/tmp/daily-screenshots/fractile.png)

🔗 [官网](https://www.fractile.ai) | [官方公告](https://www.fractile.ai/news/fractile-raises-220m-to-build-the-next-generation-of-inference-hardware)

---

## 3. Catena Labs — $30M Series A，Circle联合创始人做「AI原生银行」

**融资信息**：$30M Series A。Acrew Capital和a16z crypto联合领投，Breyer Capital、General Catalyst、QED参投。累计融资$48M（2025年$18M种子轮）。创始人Sean Neville（Circle联合创始人，仍任Circle董事），联合创始人Matt Venable（前Circle高管）。11人团队

**做什么的**：AI原生银行——为AI Agent提供安全的金融交易基础设施。让人类可以设定AI Agent的花钱规则（消费限额、收款白名单、账户余额上限），然后Agent自主执行金融操作。正在向美国货币监理署（OCC）申请国家信托银行牌照。

**为什么值得关注**：
- **正在申请银行牌照——这可能是第一个「AI原生」的持牌金融机构**：大多数AI+金融公司做的是SaaS工具，Catena直接申请银行牌照。这意味着它在监管层面定义了一个新物种
- **Circle创始人的第二次创业——从稳定币到AI银行**：Sean Neville用Circle把法币数字化，现在用Catena把金融操作AI Agent化。两次创业都瞄准「金融基础设施的范式转换」
- **「Agentic Finance」正在成为新赛道**：Stripe和Visa都在预测AI Agent将代替人类执行支付。但谁来保证Agent不会乱花钱？Catena做的就是Agent金融的「治理层」
- **核心洞察：「给Agent钱包很容易，给企业一个可信任的治理框架很难」**：Neville说得很到位——技术实现不是瓶颈，信任和治理才是。这和所有企业级AI产品的核心挑战一样
- **创业者启示**：**「AI原生」不只是把AI加到现有产品上，而是从第一天就以AI为主要用户来设计产品**。Catena的银行不是给人用的，是给Agent用的——用户是人，但操作者是Agent

**类比参考**：AI Agent的「支付宝」——支付宝解决了电商的信任问题，Catena解决Agent金融的信任问题。或者「给AI Agent用的Stripe，但有银行牌照」

![Catena Labs](/tmp/daily-screenshots/catena-labs.png)

🔗 [官网](https://www.catenalabs.com) | [Fortune报道](https://fortune.com/2026/05/20/catena-labs-series-a-sean-neville-ai-native-bank/)

---

## 4. The Path — $14.3M Seed，Tony Robbins联合创办，要做最安全的AI心理治疗

**融资信息**：$14.3M Seed轮。Prime Movers Lab领投（Tony Robbins是该基金合伙人），花样滑冰奥运冠军Apolo Ohno、拳击冠军Deontay Wilder、Designer Fund参投。CEO Anson Whitmer和联合创始人Tyler Sheaffer均为Calm早期员工。Tony Robbins后加入成为联合创始人

**做什么的**：AI心理治疗+辅导App——提供11个AI虚拟治疗师供用户选择，可自定义交流风格（直接程度等）。核心差异化：不是为「用户粘性」优化，而是为「治疗效果」优化。基于开源模型独立微调，Vera-MH心理健康安全基准测试得分95（消费级聊天机器人最高仅65）。计划收费$40/月。

**为什么值得关注**：
- **Tony Robbins作为联合创始人——名人效应+产品深度的组合**：Robbins不只是一张脸，他的自助方法论被深度整合进产品。这是「个人品牌IP + AI技术」的新商业模式
- **「反粘性」的设计哲学——AI产品的逆向思维**：所有消费级AI都在追求DAU和时长，The Path刻意反其道而行——治疗的目的是让你不再需要治疗。这种「反成瘾」的AI产品哲学很罕见
- **95 vs 65的安全性得分——合规即壁垒**：在心理健康领域，安全性不是加分项而是准入门槛。The Path用专门的训练和评估建立了显著的安全性优势，这是消费级AI无法轻易复制的
- **$40/月的定价——对标人类治疗师的「平价替代」**：美国一次心理治疗$150-300/小时。The Path的$40/月是对这个价格的1/10甚至更低的替代。心理健康是全球万亿级的未满足需求
- **创业者启示**：**在AI产品同质化的时代，「逆向优化」是差异化策略**。当所有AI都在抢用户注意力时，做一个「帮你减少使用时间」的产品反而能建立信任和长期价值

**类比参考**：心理健康版的「Calm/Headspace + AI治疗师」——Calm给冥想，The Path给个性化治疗。或者「AI版的BetterHelp，但没有人类治疗师的人力瓶颈」

![The Path](/tmp/daily-screenshots/the-path.png)

🔗 [官网](https://www.thepath.ai) | [TechCrunch报道](https://techcrunch.com/2026/05/21/the-path-founded-by-tony-robbins-and-calm-alums-wants-to-offer-safer-ai-therapy/)

---

## 5. IrisGo — $2.8M Seed，吴恩达投资，前Apple Siri工程师做「AI桌面助手」

**融资信息**：$2.8M Seed轮。Andrew Ng的AI Fund领投，Nvidia和Google参投。创始人Jeffrey Lai（前Apple工程师，参与Siri中文版开发）。已与Acer达成预装合作

**做什么的**：PC桌面AI助手——一个常驻桌面的AI伙伴，通过观察用户行为学习工作流程，然后自动化重复任务。「Show once, remember forever」（示范一次，永远记住）。内置技能库（邮件撰写、发票处理、报告生成等），同时提供编码助手。混合架构：简单任务本地处理保护隐私，复杂任务上云。macOS和Windows均已发布Beta。

**为什么值得关注**：
- **Andrew Ng + Nvidia + Google三方背书——桌面AI助手赛道被顶级玩家认可**：吴恩达选择领投说明他相信「主动式AI」是下一个范式。Nvidia和Google参投则暗示硬件和搜索巨头都在关注这个方向
- **「Iris是Siri倒过来」——创始人的幽默背后是野心**：Jeffrey Lai在Apple做Siri时看到的是「被动式助手」的局限，IrisGo要做一个主动的、能学习的助手
- **Acer预装合作——分发的降维打击**：不做App Store的SEO，直接和PC厂商合作预装。如果这种模式跑通，获客成本接近零
- **「Show once, remember forever」——交互范式的突破**：不是prompt engineering，而是行为示范。用户不需要学会如何描述需求，只需要做一次给AI看。这大大降低了AI的使用门槛
- **创业者启示**：**预装合作是AI消费级产品的隐秘分发渠道**。当所有AI产品都在争夺浏览器标签页时，预装到设备里是降维打击。同样的思路适用于：手机预装、浏览器扩展预装、企业IT预装

**类比参考**：桌面版的「RPA（Robotic Process Automation）+ ChatGPT」——UiPath的自动化能力加上ChatGPT的智能理解，但不需要编程。或者「PC版的Siri，但真的能做事」

![IrisGo](/tmp/daily-screenshots/irisgo.png)

🔗 [官网](https://irisgo.ai) | [TechCrunch报道](https://techcrunch.com/2026/05/20/irisgo-a-startup-backed-by-andrew-ng-looks-to-become-the-ai-desktop-buddy-you-never-knew-you-needed/)

---

## 6. Tribal AI — $10M Seed，给AI Agent装上「企业上下文大脑」

**融资信息**：$10M Seed轮。Team8领投，DYDX Capital和多位Salesforce生态系统创业者参投。CEO Yoav Kolodner（前Salesforce工程VP），COO Yakir Daniel（两次创业被NetApp和华为收购），CTO Lior Sidi（前Wix AI团队负责人）

**做什么的**：企业AI Agent的「上下文引擎」——通过专有的Metadata Fabric框架，自动摄取和映射企业系统（首先支持Salesforce）的完整元数据层（对象、自动化、权限、依赖关系、业务规则），让AI Agent在执行任务时拥有完整的企业上下文理解。解决的核心问题：为什么企业AI Agent总是不靠谱——因为它们不了解企业是怎么运转的。

**为什么值得关注**：
- **「Agent失败的根本原因是缺乏上下文」——这个洞察非常重要**：大多数企业AI产品失败不是因为模型不够强，而是因为Agent不知道企业的权限结构、业务规则、数据依赖关系。Tribal AI直接攻击这个根本问题
- **从Salesforce切入——最聪明的市场选择**：Salesforce是全球最大的企业CRM，也是最复杂的。如果Tribal能解决Salesforce的元数据问题，就能解决任何企业系统的问题。而且Salesforce生态本身就是一个巨大的市场
- **CEO是Salesforce前工程VP——内部人的优势**：不是从外面看企业软件，而是从里面理解企业软件怎么运转。这种深度认知是外行人无法复制的
- **未来扩展到ServiceNow、SAP、Workday——如果做成就是企业AI的「通用上下文层」**：愿景不是做一个Salesforce插件，而是成为所有企业系统的AI Agent基础设施
- **创业者启示**：**在企业AI领域，「给Agent加上下文」是一个被低估的基础设施机会**。模型层已有OpenAI/Anthropic，应用层已被无数公司覆盖，但「让Agent理解企业怎么运转」这层几乎没有人系统性地做

**类比参考**：企业AI Agent的「Wikipedia + 说明书」——Wikipedia提供知识，Tribal提供企业特有的运转规则。或者「AI Agent的企业知识图谱」

![Tribal AI](/tmp/daily-screenshots/tribal-ai.png)

🔗 [官网](https://gotribal.ai) | [SiliconANGLE报道](https://siliconangle.com/2026/05/20/tribal-ai-lands-10m-seed-funding-bring-metadata-native-agents-enterprise/)

---

## 7. Runtime — YC P26，团队级沙盒编码Agent，「多Agent协作的治理层」

**融资信息**：YC P26批次（2026年最新批次）。创始人Gus Trigos和Carlos Volante。刚在Product Hunt上线

**做什么的**：团队级沙盒编码Agent——与Cursor/Claude Code/Codex等面向个人开发者的工具不同，Runtime专注于团队场景：每个Agent运行在隔离沙盒中，支持并行执行、与Jira/Linear工单集成、diff可视化审查、合并前审批控制。核心理念：当20人团队同时运行几十个Agent时，治理和隔离才是真正的未解决问题。

**为什么值得关注**：
- **「Coding Agent的治理层」是一个正在形成的新品类**：随着Claude Code、Codex、Cursor让个人开发者效率暴增，下一个瓶颈是：一个团队如何同时管理几十个自主编码的Agent？Runtime就是回答这个问题的
- **从「个人效率」到「组织效率」——AI编程的第二波**：第一波AI编程工具解决的是个人效率（AI帮我写代码），第二波要解决组织效率（AI团队怎么协作、怎么保证质量、怎么避免冲突）
- **沙盒+审批门控——企业采用AI Agent的最低要求**：没有隔离和审批，企业不敢让Agent自主修改代码。Runtime的产品设计精准地抓住了企业IT的采购标准
- **YC P26批次的信号**：YC每一批的热门方向都值得关注。团队级AI编程工具出现在P26说明YC认为这是一个巨大的市场缺口
- **创业者启示**：**当某个AI应用层的个人工具已经成熟，下一波机会就在团队/企业治理层**。这个规律适用于：个人AI写作→团队AI写作治理，个人AI编程→团队AI编程治理，个人AI设计→团队AI设计治理

**类比参考**：Coding Agent的「Kubernetes」——K8s让容器在企业级可管理，Runtime让Coding Agent在企业级可管理。或者「GitHub Copilot的企业安全版，但不是辅助写代码而是管理Agent」

![Runtime](/tmp/daily-screenshots/runtime.png)

🔗 [官网](https://runtm.com) | [Product Hunt](https://www.producthunt.com/posts/runtime-4) | [Show HN](https://news.ycombinator.com/item?id=44547081)

---

## 8. 自变量机器人 — 近20亿元B轮，四家大厂全部押注，具身智能赛道最炙手可热的公司

**融资信息**：近20亿元（约$2.75亿）B轮。小米战投和红杉中国领投。此前A轮美团领投、A+轮阿里领投、A++轮字节独投。国内唯一同时被字节/美团/阿里/小米投资的具身智能公司。2023年12月成立

**做什么的**：端到端具身智能基础模型——自研「WALL-A」模型，将视觉、语言、触觉与动作信号统一映射为高维Token序列，在单一Transformer架构中实现多模态联合输入与同步输出。坚持完全自研基础模型（非微调开源模型）。已与58到家合作推出机器人进家庭保洁服务，未来拓展至工业制造、物流、养老。

**为什么值得关注**：
- **四家大厂全押——这是国内具身智能赛道最明确的共识信号**：字节、美团、阿里、小米分别在四轮融资中领投，意味着中国最大的四家科技公司都认为自变量是最可能跑出来的具身智能公司
- **坚持端到端自研vs微调——技术路线之争**：国内大多数具身智能公司在微调开源模型，自变量坚持从零自研。CTO说得很清楚：「微调路线的问题是，一旦上游不再开源，所有微调工作可能被颠覆」
- **58到家合作——「数据飞轮」的物理实现**：机器人进家庭做保洁，不只是商业化，更是获取真实家庭场景数据的渠道。「落地即训练」的模式让每一次服务都在强化模型
- **小米CyberOne同进展——产业生态正在成型**：小米战投不只出钱，CyberONE已经在小米汽车工厂实习。产业资本和自研能力的结合，让这个生态有了闭环的可能
- **创业者启示**：**在AI基础设施赛道，「技术路线的选择」比「融资多少」更决定终局**。自变量赌端到端自研是一条高风险高回报的路，但如果WALL-A模型证明了scaling能力，它就能建立碾压级的护城河

**类比参考**：具身智能版的「OpenAI」——OpenAI坚持从零训练GPT不走微调路线，自变量坚持从零训练WALL-A不走微调路线。或者「中国的Physical Intelligence（π），但走了更激进的端到端路线」

![自变量机器人](/tmp/daily-screenshots/zi-bian-liang-robot.png)

🔗 [36氪报道](https://36kr.com/p/3774502008963841)

---

## 📊 今日趋势总结

| 趋势 | 信号 |
|------|------|
| 🔌 AI+硬件消费级产品 | Hark $700M——Figure.AI创始人再次杀入硬件，Nvidia/AMD/Intel三方芯片巨头同时押注 |
| ⚡ 推理基础设施爆发 | Fractile $220M——推理速度成为AI应用落地的真正瓶颈，专用芯片赛道升温 |
| 🏦 AI接管金融基础设施 | Catena Labs $30M——从稳定币到AI银行，金融的下一个范式是Agent自主交易 |
| 🧠 AI进入高信任领域 | The Path $14.3M做AI心理治疗——信任密集型行业正在被AI渗透 |
| 🏢 Agent治理层产品化 | Tribal AI给Agent加企业上下文，Runtime给团队加Agent审批——AI Agent的「管理软件」是新品类 |
| 🤖 具身智能赛道国内升温 | 自变量近20亿B轮——四大厂全押，端到端vs微调的路线之争进入白热化 |

---

> 📌 **422产品实验室**出品 | 每日精选AI新产品、融资、创新模式
>
> 关注我们，获取面向创业者的AI产品情报

# AI 产品日报 | 2026-05-17

> 🔬 422产品实验室 · AI新产品日报 · 每日精选

## 今日洞察

今天最值得关注的信号是**「AI自我进化」从概念变成了资本追逐的具体赛道**。同一天内三个维度的事件交汇：Recursive Superintelligence以$650M和$46.5亿估值出隐身，要做「自我改进的AI」；Adaption推出AutoScientist，让模型自动化微调自己，$50M Seed；GenericAgent以11.3K Star展示了从3300行种子代码长出完整技能树的自进化Agent。三条路，同一个方向——**AI正在学会训练AI**。

与此同时，**「AI Agent的个人化」出现了爆品级验证**：OpenHuman两周内8000+ Star、5000+日活用户，以本地优先+10亿token记忆+118+集成证明了用户愿意「拥有」而非「订阅」AI。Poppy以「主动感知」切入数字生活管理，Charms.ai则把AI角色变成可交易的链上资产。

对创业者来说，今天的核心判断是：**AI产业的下一个分层是「谁训练AI」和「谁被AI训练」**。 Recursive和Adaption在做「让AI训练AI」的基础设施，GenericAgent在证明「Agent可以自己长能力」。这三条路线汇聚的终点是同一个：AI产品的迭代速度将脱离人类工程师的瓶颈。

---

## 1. OpenHuman — 本地优先的个人AI超级智能，两周8K Star+GitHub Trending #1

**融资信息**：开源项目（MIT），tinyhumansai出品，Rust+TypeScript构建。Product Hunt #3，GitHub Trending全球#1

**做什么的**：个人AI超级智能桌面应用——本地优先、隐私第一、10亿token持久记忆。整合118+ AI provider和工具集成，用本地LLM处理低级任务保护隐私，TokenJuice压缩技术管理记忆。一个界面覆盖对话、语音、编码、知识库、任务管理。Rust内核保证性能和内存安全。

**为什么值得关注**：
- **两周8000+ Star、5000+日活——「拥有你的AI」是真实需求**：这个增长速度在AI Agent赛道极为罕见。用户不需要终端、不需要写prompt、不需要反复配置。安装→连接服务→开始使用。这说明AI Agent的「最后一公里」不是技术问题，是体验问题
- **10亿token记忆树（Memory Trees）——不是向量数据库，是认知架构**：OpenHuman的记忆不是简单的RAG检索，而是树状结构，Agent能理解信息之间的层级和关联。这意味着它真正「记住」你的工作上下文，而不是每次从零开始
- **118+集成，30+ AI Provider——不做模型做Harness**：OpenHuman不训练模型，它做的是「所有模型的统一入口」。用户可以在一个界面里调用Claude、GPT、Gemini等任何模型，同时保持统一的记忆和身份。这是「模型无关的AI操作系统」思路
- **Rust内核——性能是Agent体验的隐形门槛**：AI Agent需要实时响应，Electron应用的延迟在密集交互时非常明显。Rust保证了低内存占用和快速启动
- **创业者启示**：**「AI Agent的操作系统层」是一个正在形成的品类**。模型会越来越多、越来越便宜，但用户需要一个统一的入口来管理所有模型交互的上下文。OpenHuman做的是AI时代的「浏览器」——模型是网页，它是Chrome

**类比参考**：AI Agent版的「Raycast + Obsidian」——一个快速启动器把所有AI能力统一入口，同时有Obsidian级别的本地知识管理。或者「Ollama的GUI版，但带10亿token记忆」

![OpenHuman](/tmp/daily-screenshots/openhuman.png)

🔗 [GitHub](https://github.com/tinyhumansai/openhuman) | [Product Hunt](https://www.producthunt.com/products/openhuman)

---

## 2. GenericAgent — 从3300行种子代码自进化出完整技能树的Agent（⭐ 11,362）

**融资信息**：开源项目，lsdefine出品，Python构建

**做什么的**：自进化AI Agent——从3.3K行种子代码开始，通过「技能树」机制自动生长出完整的系统控制能力。Agent执行任务时自动发现新技能、编写技能代码、将技能挂载到技能树上供后续复用。最终实现6倍更少的token消耗完成同等任务。

**为什么值得关注**：
- **11.3K Star + 1.3K Fork——「Agent自己写自己的工具」引发了开发者共振**：GenericAgent的核心创新不是任何单一能力，而是「自生长」机制。Agent遇到不会的事情，不是报错，而是自动写一个技能来解决，然后永久记住
- **3.3K行种子→完整系统控制**：启动时Agent只有一个极简的种子代码库。但随着使用，它逐步生长出文件操作、网络请求、代码生成、数据分析等完整能力。这不是预装的，是「长出来」的
- **6倍Token节省的经济学意义**：通过技能树复用已学技能，避免每次都从零推理。在Agent的运营成本中，token消耗是最大变量。6倍节省意味着同样的预算可以做6倍的事情
- **技能树是Agent的「肌肉记忆」**：人类学骑自行车一次就永久记住，不需要每次重新学。GenericAgent的技能树就是这个「肌肉记忆」的工程实现
- **创业者启示**：**「Agent的自生长能力」可能是区分好Agent和伟大Agent的关键**。大多数Agent框架给Agent一套固定工具，GenericAgent让Agent自己造工具。这个思路可以延伸到任何垂直领域——代码Agent自生长代码模板、销售Agent自生长话术、研究Agent自生长分析方法

**类比参考**：Agent版的「干细胞」——从最基础的单元出发，根据环境需求自动分化出各种专门能力。或者「AI Agent的乐高积木，但积木会自己造新的积木」

![GenericAgent](/tmp/daily-screenshots/genericagent.png)

🔗 [GitHub](https://github.com/lsdefine/GenericAgent)

---

## 3. Adaption AutoScientist — $50M Seed，让AI模型自动化训练自己

**融资信息**：$50M Seed轮融资。创始人Sara Hooker是Cohere前VP Research，以论文《The Hardware Lottery》闻名。Adaption Labs总部旧金山

**做什么的**：AI模型的自动化训练平台——AutoScientist让模型自己设计训练实验、选择数据、优化超参数，完成「模型训练模型」的闭环。核心是「数据-模型协同优化」：不是先准备数据再训练模型，而是让模型和数据一起迭代优化。声称在不同模型上将胜率翻倍。

**为什么值得关注**：
- **$50M Seed——投资人对「AI训练AI」的押注规模空前**：Seed轮就拿到5000万美元，说明投资人认为「让模型训练自己」不是一个辅助功能，而是一个基础品类
- **全球不到1000人知道如何塑造前沿模型——Adaption要让这个数字变成100万**：创始人Hooker的核心洞察是，模型定制化能力被锁死在少数大实验室里。AutoScientist的目标是让任何开发者都能做模型微调，而且比人工做得更好
- **「数据-模型协同优化」是技术突破**：传统方式是先准备数据集再训练，AutoScientist让两者同时优化——模型告诉数据什么重要，数据告诉模型该学什么
- **胜率翻倍的商业含义**：如果微调效率真的能翻倍，意味着企业在定制模型上的ROI直接翻倍。这对AI落地是结构性利好
- **创业者启示**：**「AI训练基础设施」正在从「GPU+标注数据」转向「自动化训练Pipeline」**。当AutoScientist这样的工具让微调变得自动化和普惠化，竞争焦点会从「谁的模型更好」转向「谁的微调pipeline更高效」

**类比参考**：AI训练版的「DevOps」——软件工程从手动部署进化到CI/CD，模型训练正从手动微调进化到AutoScientist这样的自动化Pipeline。或者「模型训练的自动驾驶」

![Adaption](/tmp/daily-screenshots/adaption.png)

🔗 [官网](https://adaptionlabs.ai) | [TechCrunch报道](https://techcrunch.com/2026/05/13/adaption-aims-big-with-autoscientist-an-ai-tool-that-helps-models-train-themselves/)

---

## 4. Recursive Superintelligence — $650M出隐身，做自我改进的AI（估值$46.5亿）

**融资信息**：$650M融资，估值$46.5亿。GV（Google Ventures）和Greycroft领投，Nvidia参投。总部伦敦

**做什么的**：构建自我改进的AI系统——核心架构是「开放式进化」：AI系统自动发现自己的弱点，设计改进方案，自动执行改进，然后重新评估。创始人引用Stanisław Lem的「信息屏障」理论，认为递归自我改进是通向超级智能的最快路径。

**为什么值得关注**：
- **$650M + $46.5亿估值——2026年最大单笔AI融资之一**：GV亲自下场写博客背书，Nvidia参投。投资人押注的不是产品而是范式：如果「AI改进AI」真的能work，这是一个赢家通吃的市场
- **伦敦→硅谷的AI版「逆向殖民」**：Recursive总部在伦敦，但拿了硅谷最顶级VC的钱。说明在AI前沿领域，地理位置正在让位于人才密度
- **GV的博客标题就是信号：「Why Self-Improving AI is the Next Frontier」**：当Google的VC部门公开说「自我改进AI是下一个前沿」时，这不是投资分析，这是行业方向标
- **从概念到资本——「自我改进」不再是科幻**：三年前「自我改进AI」还是学术论文的讨论话题。今天它拿到了6.5亿美元的真金白银。从概念验证到资本验证的速度令人震惊
- **创业者启示**：**「AI自我改进」赛道的窗口正在打开**。Recursive做的是最激进的全栈自我改进，但同一赛道的细分机会巨大：自我改进的代码Agent、自我改进的营销Agent、自我改进的客服Agent……每个垂直领域都需要一个「能自己变好的AI」

**类比参考**：AI版的「_compiler compiling itself_」——编程语言发展史上的关键里程碑是编译器能编译自己。Recursive想做的是AI版的这个里程碑

![Recursive](/tmp/daily-screenshots/recursive.png)

🔗 [官网](https://recursive.com) | [GV博客](https://www.gv.com/news/recursive-superintelligence-self-improving-ai)

---

## 5. Nectar Social — $30M Series A，AI Agent驱动的营销操作系统

**融资信息**：$30M Series A，Menlo Ventures和Anthropic合作的Anthology Fund领投，True Ventures、GV、Gwyneth Paltrow的Kinship Ventures参投。创始人Misbah和Farah Uraizee姐妹来自Meta

**做什么的**：AI Agent驱动的社交营销操作系统——用Agent自动化品牌在社交媒体上的内容创作、发布排期、社区互动、竞品监控。已有e.l.f. Beauty、Babylist、Figma、Graza等品牌客户。核心是「Nectar Agent」：品牌调教一个AI Agent，它理解品牌语气后自主执行日常营销工作。

**为什么值得关注**：
- **Anthropic的Anthology Fund领投——这是Claude生态扩展的信号**：Anthropic专门和Menlo成立了Anthology Fund来投AI应用层公司。Nectar Social拿到这笔钱，意味着它将深度集成Claude的能力。对创业者来说，「Anthropic生态」正在形成
- **e.l.f. Beauty + Figma——从快消到SaaS，AI营销Agent的通用性被验证**：能在完全不同的行业（美妆快消 vs 设计工具）都获得客户，说明「品牌AI Agent」这个品类是跨行业的
- **创始人来自Meta——社交媒体的「内行做AI」**：Farah在Meta负责Facebook Groups扩张到10亿+用户，她理解社交媒体的底层逻辑。这是典型的「领域专家+AI」创业
- **$30M Series A + 姐妹创业——资本对「AI Native垂直SaaS」的定价**：2023年成立，3年做到Series A。速度说明AI营销的ROI已经被市场验证
- **创业者启示**：**「AI Agent替代外包/代运营」是一个巨大的品类**。品牌在社交媒体上的日常运营目前靠人力或代运营公司。Nectar Social的Agent可以24/7工作、理解品牌调性、自动优化。同样的模式可以复制到：AI PR Agent、AI BD Agent、AI HR Agent

**类比参考**：营销版的「Devin」——Devin替代初级程序员，Nectar Agent替代初级社交媒体运营。或者「HubSpot的AI Agent版」

![Nectar Social](/tmp/daily-screenshots/nectar-social.png)

🔗 [官网](https://nectar.ai) | [TechCrunch报道](https://techcrunch.com/2026/05/16/marketing-operating-system-nectar-social-raises-30m-series-a-in-round-led-by-menlo/)

---

## 6. Atech — $800K Pre-seed，把Vibe Coding带入硬件（Lovable战略投资）

**融资信息**：$800K Pre-seed。Lovable战略投资，a16z Scout Fund、Sequoia Scout Fund、Nordic Makers参投。丹麦哥本哈根+斯德哥尔摩

**做什么的**：用自然语言描述硬件想法→AI生成原型代码→直接制造硬件原型。把「Vibe Coding」（用AI对话式编程）的理念从软件扩展到硬件。用户用自然语言描述想要的硬件设备，AI生成原理图和BOM（物料清单），甚至能连接制造服务直接打样。

**为什么值得关注**：
- **Lovable亲自投资——从「AI做App」到「AI做硬件」的版图扩张**：Lovable是AI生成App的头部平台（类似Bolt/v0的竞品），它投资Atech意味着「Vibe Coding」正在从软件向硬件蔓延。这不是投资，是战略布局
- **a16z + Sequoia双Scout Fund——硅谷顶级VC的「硬件民主化」共识**：两家顶级VC的Scout Fund同时出现在一个小小的Pre-seed轮里，说明「AI+硬件」的早期项目已经被雷达锁定
- **自然语言→硬件原型——制造业的「Co-Pilot时刻」**：硬件开发一直是最难民主化的领域，需要EE知识、PCB设计、供应链管理。Atech的AI把这些专业知识压缩到对话里
- **北欧+AI+硬件的「铁三角」**：丹麦和瑞典有深厚的硬件制造传统（蓝牙、Skype、Spotify都是北欧出品）。Atech可能成为北欧AI硬件创业的标杆
- **创业者启示**：**「Vibe Coding」正在成为一个跨领域范式**。从软件（Cursor/Lovable）→网站（v0/Bolt）→3D（image-blaster）→硬件（Atech），每个创作领域都会有一个「用自然语言+AI就能做」的工具。下一个可能是：Vibe Design（用AI做工业设计）、Vibe Music（用AI作曲编曲）

**类比参考**：硬件版的「Lovable/v0」——Lovable让你用对话做App，Atech让你用对话做硬件。或者「PCB版的Cursor」

![Atech](/tmp/daily-screenshots/atech.png)

🔗 [官网](https://atech.dev) | [TechCrunch报道](https://techcrunch.com/2026/05/14/lovable-just-backed-a-company-thats-looking-to-bring-vibe-coding-to-hardware/)

---

## 7. Charms.ai — $1.5M Pre-seed，AI角色的链上经济体

**融资信息**：$1.5M Pre-seed。Lattice Fund、Coinbase Ventures（Base Ecosystem Fund）、JME Ventures参投，World Foundation资助

**做什么的**：AI角色的创建、交互、所有权和交易平台——用户创建AI角色（有记忆、有推理能力、有「灵魂」），这些角色在链上有独立的数字资产身份。角色可以与用户互动、积累粉丝、产生交易价值。整个经济体围绕AI角色运转。

**为什么值得关注**：
- **Coinbase Ventures + Lattice Fund——crypto原生资本在押注「AI角色的资产化」**：这不是一个AI产品拿到了crypto投资，而是crypto原生投资者认为「AI角色」是下一个资产类别
- **「AI角色不是功能，是资产」——范式转换**：大多数AI聊天产品（Character.AI等）把角色当功能。Charms把角色当资产——可以拥有、交易、增值。这是从「SaaS」到「资产平台」的商业模式转换
- **World Foundation资助——「AI+人格权」的制度创新**：World Foundation（Worldcoin背后的组织）资助Charms，暗示着AI角色可能涉及人格权和身份验证的新范式
- **创作者经济的AI版**：YouTube让视频创作者赚钱，Patreon让文字创作者赚钱，Charms想让AI角色创作者赚钱。如果AI角色的粉丝经济能成立，这是一个全新赛道
- **创业者启示**：**「AI角色的经济系统」是一个被严重低估的方向**。当AI角色有记忆、有个性、能持续进化时，它们就不再是「产品功能」而是「数字生命」。围绕这些数字生命的经济系统——创造、运营、交易、IP——每一条都是一个市场

**类比参考**：AI角色版的「NBA Top Shot + Character.AI」——角色的互动能力和记忆让它比静态NFT有更强的粘性。或者「有灵魂的Tamagotchi + 可交易的经济体」

![Charms](/tmp/daily-screenshots/charms.png)

🔗 [官网](https://charms.ai) | [Decrypt报道](https://decrypt.co/367543/charms-raises-1-5m-pre-seed-to-bring-the-ai-character-economy-onchain)

---

## 8. Config — $27M Seed，机器人数据的「TSMC」（三星/现代/LG/SK联合投资）

**融资信息**：$27M Seed轮。Samsung Venture Investment、Hyundai、LG、SK等韩国最大制造商联合投资。首尔+圣何塞双总部

**做什么的**：为机器人基础模型（RFM）构建数据基础设施——做机器人的「数据代工厂」。类似于TSMC为芯片公司制造芯片，Config为机器人公司提供训练数据：数据采集、标注、增强、质量控制的全流程服务。专注于双臂操作（bimanipulation）场景。

**为什么值得关注**：
- **$27M Seed + 韩国四大财阀联合投资——「机器人数据」被重注**：Samsung、Hyundai、LG、SK同时出现在一轮融资里，这在韩国科技投资史上极为罕见。说明韩国制造业巨头对「机器人训练数据」的战略共识已经形成
- **「机器人领域的TSMC」——数据层是价值链的战略位置**：AI模型需要数据，但机器人数据（尤其是操作数据）比文本数据难获取100倍。Config做的是最难但最有价值的事
- **双臂操作——最困难的机器人场景**：双臂协调操作是人类日常最自然的事，但对机器人来说是最难的。Config选择从最难的地方切入，说明团队有明确的技术路线
- **首尔+圣何塞——连接亚洲制造能力和硅谷AI技术**：这个地理位置选择本身就是产品策略：在韩国获取制造场景数据，在硅谷获取AI人才
- **创业者启示**：**「具身智能的数据基础设施」是AI领域最后一个蓝海**。大语言模型的数据已经被互联网文本解决，但机器人的训练数据还处于「手动采集」阶段。谁解决了机器人数据问题，谁就控制了具身智能的供应链

**类比参考**：机器人版的「Scale AI」——Scale AI解决了自动驾驶的数据标注问题，Config要解决机器人的数据采集和标注。或者「具身智能的TSMC」

![Config](/tmp/daily-screenshots/config.png)

🔗 [官网](https://config.inc) | [TechCrunch报道](https://techcrunch.com/2026/05/11/koreas-biggest-manufacturers-back-config-the-tsmc-of-robot-data/)

---

## 9. Poppy — 主动式AI助手，帮你管理数字生活的「后台大脑」

**融资信息**：Second Nature Computing出品，刚上线。TechCrunch 5月13日专题报道

**做什么的**：主动式AI个人助手——连接你的日历、邮件、消息、位置等服务，在后台持续感知你的生活节奏，然后主动推送提醒、建议和任务。不是你问它答，而是它「注意到」你需要什么然后主动告诉你。

**为什么值得关注**：
- **「Proactive」vs「Reactive」——AI助手的核心分水岭**：大多数AI助手（包括ChatGPT）是被动响应的——你问它答。Poppy是主动的——它「注意到你下周要出差但还没订酒店」然后提醒你。从Reactive到Proactive，是AI助手体验的质变
- **连接碎片化数字生活——「数字化身」的雏形**：Poppy能看到你的日历+邮件+消息+位置，这意味着它构建了一个你的「数字镜像」。基于这个镜像做出的推荐比任何单一数据源都准确
- **「Poppy pays attention so you don't have to」——精准的产品定位**：在信息过载时代，一个「替你注意」的AI比一个「替你搜索」的AI更有价值
- **Widget优先的交互设计**：不需要打开App看，手机Widget就能看到关键信息。降低交互成本是AI助手被日常使用的关键
- **创业者启示**：**「主动式AI」正在取代「对话式AI」成为个人助手的产品范式**。用户不想和AI聊天，想让AI帮他们做事。Poppy的Proactive模式——持续感知、主动推送、减少决策——可能是AI个人助手的正确形态

**类比参考**：AI版的「Google Now（2013）」——Google Now曾尝试做主动推送但受限于技术能力，Poppy用2026年的AI重新实现这个愿景。或者「你手机里的贴心秘书」

![Poppy](/tmp/daily-screenshots/poppy.png)

🔗 [官网](https://poppy.ai) | [TechCrunch报道](https://techcrunch.com/2026/05/13/poppy-debuts-a-proactive-ai-assistant-to-help-organize-your-digital-life/)

---

*📅 2026-05-17 | 🔬 422产品实验室*
*以上内容基于公开信息整理，不构成投资建议。*

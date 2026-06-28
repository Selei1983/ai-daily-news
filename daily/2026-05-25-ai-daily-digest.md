# AI 产品日报 | 2026-05-25

> 🔬 422产品实验室 · AI新产品日报 · 每日精选

## 今日洞察

本周最值得深挖的趋势是**「AI从辅助工具走向自主员工」**——Viktor拿到Accel $75M做Slack/Teams里的「AI同事」，10周冲到$15M ARR，Slack创始人亲自天使投资；Blitzy用$200M和$14亿估值做全自动软件重构，让AI Agent并行改写百万行代码；Recursive Superintelligence更激进，$650M + $46.5亿估值，目标让AI自主发现自身弱点并重写自己。三条线指向同一个终局：**AI不是在帮你做事，而是在替你做事**。

另一条暗线是**「Agent经济的金融基础设施」正在成型**：AEON拿$8M做Agent之间的支付结算层，Moment拿$78M做财富管理的AI操作系统——一个解决Agent「怎么付钱」，一个解决AI「怎么管钱」。结合上周Catena Labs申请AI银行牌照的信号，Agent金融赛道的拼图正在快速完整。

对创业者的判断：**「AI同事」是2026年Q2最确定的品类，但窗口极短。** 大厂（微软Copilot、Salesforce Agentforce）已经在自家的平台里嵌入Agent。创业公司的唯一机会是：跨平台、有记忆、能主动——而不是等用户下指令。

---

## 1. Viktor — $75M Series A，10周冲$15M ARR，AI「同事」住进Slack和Teams

**融资信息**：$75M Series A。Accel领投，Bek Ventures、Kaya VC、Inovo VC、Tenacity Capital参投。天使投资人包括Slack联合创始人Stewart Butterfield和Cal Henderson、Synthesia CEO Victor Riparbelli，以及Google DeepMind、Figma、ElevenLabs高管。2026年2月公开发布，3个月内达到$15M年化收入run rate，2000+组织使用

**做什么的**：团队级AI Agent同事——嵌入Slack和Microsoft Teams，像真正的同事一样参与工作。能连接Google Drive、Meta Ads、Airtable、Notion、Shopify等数十个企业工具，构建对公司运转方式的「持久记忆」。不只是被动等指令，还会主动扫描公开频道，发现可以接手的工作流。曾帮客户发现Meta Ads配置问题，每周节省$10,000广告支出

**为什么值得关注**：
- **10周$15M ARR——史上最快的B2B AI产品之一**：这不是渐进式增长，是爆发式。说明市场对「AI同事」的需求不是「nice to have」而是「必须现在有」
- **Slack创始人投了「杀死Slack的产品」**——不，是投了「让Slack更有价值的产品」：Stewart Butterfield和Cal Henderson投的是嵌入Slack的Agent。这不是威胁，是共生——AI Agent让消息平台从「通讯工具」变成「工作操作系统」
- **前Meta工程师团队，先做邮箱Agent再做团队Agent——PMF的教科书**：他们先做了JaceAI（邮箱Agent），发现邮箱不是Agent的最佳载体，转而做团队协作工具里的Agent。这个pivot本身就是创业方法论：**先做最小可行产品，快速发现正确的场景**
- **Accel的选择标准很有启发性**：Accel合伙人Zhenya Loginov说得很清楚——他们要的是「团队级助手」而非「个人助手」。这个定位选择决定了产品的分发方式（组织采购 vs 个人订阅）和天花板（协作工具市场 vs 效率工具市场）
- **创业者启示**：**当AI从「个人效率工具」变成「组织成员」，产品的设计逻辑、定价模式、分发渠道都会完全不同**。Viktor的「按组织收费+主动发现工作流」模式，是AI Agent从工具到同事的关键设计

**类比参考**：AI版的「新员工」——不是Copilot那种「写代码的助手」，而是「入职三个月的新人，知道公司所有系统怎么用，24/7在线，主动找活干」。或者「Slack/Teams里的RPA + ChatGPT，但有记忆」

![Viktor](/tmp/daily-screenshots/viktor.png)

🔗 [Fortune独家](https://fortune.com/2026/05/19/viktor-ai-startup-raises-75-million-for-virtual-coworker-exclusive/) | [官网](https://viktor.com)

---

## 2. Recursive Superintelligence — $650M + $46.5亿估值，Richard Socher联合Peter Norvig要做AI自我进化

**融资信息**：$650M融资，$46.5亿估值。GV（Google Ventures）和Greycroft联合领投，AMD Ventures、NVIDIA参投。创始人Richard Socher（you.com创始人、ImageNet核心贡献者），联合创始人包括Peter Norvig（前Google研究总监、AI教科书作者）和Tim Shi（Cresta联合创始人）、Tim Rocktäschel（前DeepMind开放性研究负责人）

**做什么的**：递归自我改进AI——不是让AI帮人改进工具，而是让AI自主发现自身弱点、设计改进方案、验证效果，形成「自我进化」的闭环。核心技术路线是「开放性」（Open-endedness）——借鉴生物进化的逻辑，让AI在持续的对抗与合作中无限进化。Rainbow Teaming（彩虹团队）就是其联合创始人提出的概念：两个AI互相对抗，一个负责攻击一个负责防御，经过百万轮迭代后变得更强更安全

**为什么值得关注**：
- **$650M出stealth——2026年最疯狂的赌注之一**：Richard Socher在you.com之后没有选择做应用，而是回到最前沿的基础研究。GV和NVIDIA同时出现说明：Google和英伟达都认为「自我改进AI」是值得押注的方向
- **Peter Norvig的加入是强信号**——AI教科书《Artificial Intelligence: A Modern Approach》的作者，在Google工作了20年。他选择加入Recursive而不是留在Google，说明他相信这条路线
- **「开放性」vs「Scaling Law」——两种AI进化路线的对抗**：OpenAI/Anthropic走的是「更多数据+更大模型」路线，Recursive走的是「AI自己发现自己弱点并改进」路线。如果Recursive成功，它可能用更少的算力实现更强的AI——因为改进来自智慧而非暴力
- **Richard Socher的关键洞察**：「自动改进≠递归自我改进」——让AI帮你优化一个系统是改进，让AI自主完成「发现弱点→设计实验→验证→部署」的完整循环才是真正的自我进化。这个区分非常重要
- **创业者启示**：**「AI自我进化」不是创业者的赛道（需要$650M），但它定义了AI产业的天花板**。如果Recursive成功，所有AI应用都会受益——模型能力会加速提升，应用层的创业空间反而更大

**类比参考**：AI版的「生物进化」——不是人工选择（人类告诉AI怎么改进），而是自然选择（AI自己发现适者生存的路径）。或者「AlphaGo的自我对弈，但应用在AI模型本身的改进上」

![Recursive Superintelligence](/tmp/daily-screenshots/recursive-superintelligence.png)

🔗 [TechCrunch专访](https://techcrunch.com/2026/05/14/what-happens-when-ai-starts-building-itself/) | [GV博客](https://www.gv.com/news/recursive-superintelligence-self-improving-ai)

---

## 3. AEON — $8M Pre-Seed，YZi Labs领投，Agent经济的「支付结算层」

**融资信息**：$8M Pre-Seed。YZi Labs（原Binance Labs）领投。香港注册。2026年5月18日公布

**做什么的**：AI Agent之间的支付结算层——为「Agent经济」构建金融基础设施。让AI Agent可以自主完成支付、结算交易，连接5000万+真实世界商户。核心论点：当AI Agent开始互相购买服务（一个Agent调用另一个Agent的API、一个Agent向另一个Agent付费获取数据），需要专门的结算基础设施

**为什么值得关注**：
- **「Agent经济」的金融基础设施——一个被低估的品类**：上周Catena Labs在做Agent的银行牌照，AEON在做Agent的支付网络。两者互补：Catena解决「Agent怎么管钱」，AEON解决「Agent之间怎么交易」。这个分工正在定义一个新赛道
- **$8M Pre-Seed——币圈资本杀入Agent赛道**：YZi Labs（原Binance Labs）领投说明加密货币资本正在从DeFi转向Agent经济。这不意外——Agent之间的微支付天然适合链上结算
- **5000万商户连接——不是白皮书而是真实网络**：AEON声称已连接5000万真实商户。如果属实，这意味着Agent不需要「学会」用现有的支付系统，而是直接用AEON的网络完成交易
- **香港注册——亚洲Agent金融赛道的信号**：和Catena Labs在美国申请银行牌照平行，AEON在香港做链上结算。两个司法管辖区、两种技术路线，同时瞄准同一个市场
- **创业者启示**：**Agent经济的「金融层」可能比Agent本身的「AI层」更有商业价值**。就像visa的市值超过了大多数银行——支付网络的护城河比银行更深

**类比参考**：Agent版的「Visa/Stripe」——Visa连接人和商户，AEON连接Agent和商户。或者「AI Agent之间的SWIFT，但在区块链上」

![AEON](/tmp/daily-screenshots/aeon.png)

🔗 [PR Newswire](https://www.prnewswire.com/news-releases/aeon-raises-8m-led-by-yzi-labs-to-build-the-settlement-layer-for-agentic-economy-302774809.html) | [Crypto.news](https://crypto.news/aeon-raises-8m-to-wire-ai-agents-into-50m-real-world-merchants/)

---

## 4. SPARQ — $8.5M Seed，a16z参投，从阿联酋挑战Unreal Engine和Roblox的AI游戏引擎

**融资信息**：$8.5M Seed。a16z（Andreessen Horowitz）参投。总部位于阿联酋Ras Al Khaimah的Innovation City

**做什么的**：AI原生游戏引擎和创作者平台——让创作者用自然语言描述就能生成完整的游戏世界、角色和玩法。对标Unreal Engine和Roblox，但从第一天就以AI为核心而非后期加入AI功能。从阿联酋新兴的Innovation City孵化

**为什么值得关注**：
- **a16z投游戏引擎——硅谷最聪明的钱在押注「AI+游戏」**：a16z不只是投了一个游戏公司，而是投了「内容创作方式」的范式转换。如果AI能从自然语言生成完整游戏，游戏开发从「专业技能」变成「想象力竞赛」
- **从阿联酋出发——AI创业不需要硅谷**：SPARQ选择在Ras Al Khaimah的Innovation City而不是硅谷或伦敦。中东正在成为AI创业的新枢纽——资本充裕、政策友好、税收优势
- **「AI原生」vs「AI增强」——Unreal和Roblox的阿喀琉斯之踵**：Unreal Engine和Roblox是先有引擎再加AI，SPARQ从第一天就以AI为内核。这种「native vs bolt-on」的竞争在CRM（Salesforce vs 钉钉）、数据库（Oracle vs MongoDB）等领域反复出现过——native往往最终胜出
- **创作者经济的下一个台阶**：Roblox证明了UGC游戏是可行的，但创作门槛仍然很高。AI原生引擎可能把游戏创作门槛降到「说话就行」——这将释放数十亿潜在创作者
- **创业者启示**：**在已有巨头（Unreal/Unity/Roblox）的市场里，最好的策略不是做更好的产品，而是用新技术重新定义产品的形态**。SPARQ赌的不是「更好的游戏引擎」，而是「完全不同的创作方式」

**类比参考**：游戏版的「Midjourney」——Midjourney用AI把图像创作从专业技能变成自然语言对话，SPARQ用AI把游戏创作从专业技能变成自然语言对话。或者「AI原生的Roblox」

![SPARQ](/tmp/daily-screenshots/sparq.png)

🔗 [Gulf News](https://gulfnews.com/business/andreessen-horowitz-joins-sparqs-85m-seed-round-as-ai-native-game-engine-launches-from-innovation-city-1.500548344) | [Khaleej Times](https://www.khaleejtimes.com/business/innovation-city/sparq-takes-aim-at-unreal-engine-and-roblox-with-ai-native-game-platform-built-in-uae)

---

## 5. OpenHuman — 开源桌面AI Agent，GitHub 26K Stars，24小时3000星

**融资信息**：独立开源项目。tinyhumansai开发团队。GitHub 26,000+ Stars，Product Hunt #3。Rust + TypeScript

**做什么的**：开源桌面AI Agent——定位为「你的个人AI超级智能」。核心差异化：不是等你输入prompt才开始工作，而是先「读取你」——通过记忆树（Memory Tree）架构理解你的上下文、习惯和需求，在你开口之前就准备好。本地优先、隐私优先

**为什么值得关注**：
- **24小时3000 Stars——开源社区的爆发力**：不是KOL推荐、不是公司推广，纯粹靠产品力在GitHub社区引发病毒式传播。这种「纯社区驱动」的增长在AI工具领域越来越常见
- **「先读你，再回答」——交互范式的转变**：当前所有主流AI Agent（OpenClaw、Hermes等）都是「等用户输入→处理→输出」。OpenHuman反过来了：先理解你是谁、你在做什么、你需要什么，然后主动提供。这个范式转变可能是Agent从「工具」到「助手」的关键
- **Rust写的——性能和隐私的承诺**：选择Rust而不是Python/Electron意味着：运行速度快、内存占用低、本地运行安全。这和「隐私优先」的定位一致
- **开源AI Agent赛道的「Linux时刻」？**：OpenClaw是商业化的，OpenHuman是开源的。这个格局像极了操作系统领域的Windows vs Linux——最终可能各有各的市场，但开源版本会推动整个行业标准化
- **创业者启示**：**开源AI Agent可能是2026年最值得关注的「基础设施级」机会**。如果OpenHuman继续增长，它可能成为Agent生态的「操作系统」——第三方开发者为它构建技能/插件，形成生态

**类比参考**：AI Agent版的「Linux」——Linux是开源操作系统，OpenHuman是开源Agent系统。或者「本地版的Siri/Google Assistant，但开源、有记忆、真的能用」

![OpenHuman](/tmp/daily-screenshots/openhuman.png)

🔗 [GitHub](https://github.com/tinyhumansai/openhuman) | [DEV Community](https://dev.to/neocortexdev/openhuman-just-launched-on-product-hunt-and-its-already-trending-3-and-1-github-trending-4n4a)

---

## 6. Moment — $78M Series C，前Citadel量化团队做华尔街「AI操作系统」

**融资信息**：$78M Series C。Index Ventures领投（10个月内第二次领投）。Edward Jones和LPL Financial（美国最大财富管理公司之一）为客户。纽约

**做什么的**：投资管理的AI操作系统——为财富管理行业提供统一的AI基础设施。将交易、投资组合构建、再平衡、合规报告整合在一个AI驱动的平台上。创始团队来自Citadel Securities（全球最大做市商之一）的量化交易部门

**为什么值得关注**：
- **Index Ventures 10个月内两次领投——VC的「全押」信号**：第一次领投后不到一年就再次领投更大一轮，说明Moment的增长超出了所有人的预期。这种速度在ToB SaaS领域非常罕见
- **Edward Jones和LPL是客户——华尔街巨头在买单**：Edward Jones管理$2万亿+资产，LPL是最大的独立经纪商。这些公司不会轻易切换基础设施供应商。如果Moment进入了这些客户，它的护城河极深
- **财富管理是AI最好的垂直场景之一**：高频数据、结构化决策、合规要求严格、利润率高——这些特征让AI在财富管理领域的ROI比大多数行业都高
- **Citadel量化团队做ToB——从「赚钱」到「帮人赚钱」**：量化交易者最擅长的是「用数据做决策」，现在他们把这个能力产品化，卖给没有自建AI团队的传统财富管理公司
- **创业者启示**：**「用最聪明人的方法论，武装传统行业」是AI垂直SaaS的最佳策略**。不是从零开始教AI做财富管理，而是把顶级量化团队的方法论封装成产品。创始人的行业认知就是最大的护城河

**类比参考**：财富管理版的「Bloomberg Terminal」——但不是给交易员用的终端，而是给财富顾问用的AI操作系统。或者「Citadel的量化能力SaaS化」

![Moment](/tmp/daily-screenshots/moment.png)

🔗 [TNW](https://thenextweb.com/news/moment-78-million-citadel-quants-ai-trading-wealth-management) | [Index Ventures](https://www.indexventures.com/perspectives/from-300b-to-10-trillion-how-moment-became-the-ai-operating-system-for-investment-management/)

---

## 7. Graphon AI — $8.3M Seed，把AI的「理解」从模型内移到模型外

**融资信息**：$8.3M Seed。Novera Ventures领投，Samsung Next、Hitachi Ventures、Perplexity Fund、GS Futures参投。旧金山。创始人来自Amazon、Meta、MIT、Google、Apple、NVIDIA、NASA

**做什么的**：「预模型智能层」（Pre-Model Intelligence Layer）——在企业数据进入AI模型之前，先构建一层关系图谱。用图论（graphon functions）自动发现跨模态数据（文本、视频、音频、图像、数据库、工业传感器）之间的深层关系，形成「持久化结构化记忆」。让模型不用每次都从头理解数据，而是直接使用已经建好的关系网络

**为什么值得关注**：
- **「智能在模型外」vs「智能在模型内」——一个根本性的架构转变**：当前AI产业的主流假设是「更大的模型=更强的智能」。Graphon认为智能不应该只存在于模型内部，也应该存在于数据层——即「模型处理数据之前，数据层已经理解了数据之间的关系」
- **图论+AI——数学工具的正确应用**：Graphon用的是「graphon functions」——图论中的经典工具。在社交网络分析中已经非常成熟，现在被应用到企业数据的关系建模上。这是一个「老数学工具解决新AI问题」的好案例
- **Samsung + Hitachi参投——工业场景的信号**：三星和日立都不是纯软件公司，它们代表的是制造业和工业领域。Graphon的技术在工业场景（传感器数据+CCTV+运维日志的联合分析）可能比纯文本场景更有价值
- **韩国GS Group已经在用——零售场景的落地**：分析零售环境中顾客移动模式、建筑工地的安全监控。这些都是「多模态数据联合推理」的经典场景
- **创业者启示**：**当所有人都在做更大的模型时，「模型外的智能层」可能是一个被低估的基础设施机会**。类似CDN之于互联网——不在服务器端提升性能，而是在网络层提升效率

**类比参考**：AI版的「知识图谱+CDN」——知识图谱负责建立关系，CDN负责把关系放在离模型最近的地方。或者「给AI模型装上『长期记忆』，但记忆存在模型外面」

![Graphon AI](/tmp/daily-screenshots/graphon-ai.png)

🔗 [TNW](https://thenextweb.com/news/graphon-ai-pre-model-intelligence-layer-seed-funding) | [Unite.AI](https://www.unite.ai/graphon-ai-emerges-from-stealth-with-8-3m-to-build-an-intelligence-layer-for-enterprise-ai/)

---

## 8. 智象未来 (HiDream) — 2000亿参数图像大模型发布 + 新一轮亿级融资

**融资信息**：新一轮亿级融资。深创投、金浦投资、财鑫资本、复聚资本等多家机构参与。这是公司半个月内的第二次融资

**做什么的**：原生全模态图像大模型HiDream-O1-Image-Pro——参数量超过2000亿（200B），在多个基准测试中刷新SOTA。不是文本模型加图像能力，而是从架构层面原生支持「全模态」。在5月19日北京开放日发布

**为什么值得关注**：
- **200B参数的图像模型——国内最大的视觉大模型**：目前国内大多数图像模型在10-50B参数级别，HiDream直接拉到200B。如果性能匹配参数量级，它可能成为国内视觉AI的基础设施
- **半个月两次融资——资本对「视觉大模型」赛道的共识**：15天内完成两轮融资说明机构投资者认为「视觉大模型」是和LLM同等重要的赛道
- **深创投领投——国资的信号**：深创投是深圳国资背景的顶级VC。国资连续加注说明视觉大模型被定位为「战略性AI基础设施」
- **「原生全模态」vs「拼接式多模态」——技术路线之争**：大多数多模态模型是把视觉编码器「接」到语言模型上，HiDream从架构层面原生设计多模态能力。这个路线之争的结果将决定视觉AI的性能上限
- **创业者启示**：**「视觉大模型」是国内AI创业的一个独特机会**：由于LLM领域的竞争已经被DeepSeek等大玩家主导，视觉大模型赛道仍有创业公司的空间。如果你的产品依赖图像/视频理解，关注HiDream的能力边界

**类比参考**：视觉版的「DeepSeek」——DeepSeek在LLM领域用开源挑战OpenAI，HiDream在视觉领域用原生全模态挑战现有方案。或者「国内的DALL-E基础模型」

![智象未来](/tmp/daily-screenshots/hidream.png)

🔗 [新浪财经](https://finance.sina.com.cn/jjxw/2026-05-20/doc-inhypxki6878911.shtml)

---

## 📊 今日趋势总结

| 趋势 | 信号 |
|------|------|
| 👔 AI从工具变成同事 | Viktor $75M做「团队里的AI员工」、10周$15M ARR——企业不想要AI助手，想要AI同事 |
| 🧠 AI自我进化赛道升温 | Recursive $650M——Richard Socher+Peter Norvig押注「AI自己改进自己」，GV和NVIDIA买单 |
| 💳 Agent金融基础设施成型 | AEON做Agent支付、Moment做AI财富管理——Agent经济的「银行」和「Visa」同时出现 |
| 🎮 AI重构内容创作 | SPARQ挑战Unreal/Roblox、HiDream做2000亿视觉模型——AI正在重写「创作」的定义 |
| 🔓 开源Agent的Linux时刻 | OpenHuman 26K Stars——开源桌面Agent的爆发力，可能成为Agent生态的操作系统 |
| 📐 「模型外智能」新思路 | Graphon AI做「预模型智能层」——不是更大的模型，而是模型之外的关系理解 |

---

> 📌 **422产品实验室**出品 | 每日精选AI新产品、融资、创新模式
>
> 关注我们，获取面向创业者的AI产品情报

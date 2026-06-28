# AI 产品日报 | 2026-05-24

> 🔬 422产品实验室 · AI新产品日报 · 每日精选

## 今日洞察

本周AI赛道最震撼的两条消息同时指向一个事实：**中国AI产业正在完成从「技术跟随」到「资本自主」的战略转型**。DeepSeek以700亿元人民币（~$100亿）完成首轮外部融资、估值冲至$450-500亿——梁文锋明确告诉投资人「AGI优先、盈利其次」；而Manus AI在被中国监管部门否决Meta $20亿收购后，创始人正在筹措$10亿买回自己的公司。两条线，一个信号：**中国不再允许核心AI资产被美元资本定义，但也不缺钱让这些公司独立跑下去**。

与此同时，**AI Agent的「安全与信任层」正在产品化**：NanoCo从开源项目NanoClaw出发，6周内拿下$12M融资并拒绝了$20M收购，要做企业级Agent沙盒；Foundation从比特币硬件钱包跨界，推出Passport Prime让人类用硬件实时授权AI Agent的操作；CortexDB发布V1，用五层记忆架构解决Agent的「失忆症」，在LongMemEval-S上击败Mem0。三个不同维度——沙盒、授权、记忆——都在回答同一个问题：**Agent怎么才能被信任？**

对创业者的判断：**本周的信号很清楚——要么做足够底层的技术（芯片、模型、记忆架构）让大公司离不开你，要么做足够安全的治理层（沙盒、授权、审计）让企业敢用你**。中间的「套壳应用」窗口正在关闭。

---

## 1. DeepSeek — 700亿元首轮外部融资，估值$450-500亿，梁文锋宣告「AGI优先」

**融资信息**：约700亿元人民币（~$100亿）首轮外部融资，估值$450-500亿。中国国家集成电路产业投资基金（大基金）领投，CATL（宁德时代）据报道计划参投。此前阿里、腾讯曾洽谈但估值从$200亿迅速攀升。这是DeepSeek成立以来的首次外部融资。创始人梁文锋告诉潜在投资人：公司将优先前沿研究而非营收

**做什么的**：开源AI大模型——从DeepSeek-V2到R1推理模型，以极低成本实现了接近OpenAI的水平。DeepSeek的模型架构创新（MoE、多token预测等）让它用远低于同行的算力成本达到SOTA性能，并完全开源。R1推理模型在2025年初引爆全球关注

**为什么值得关注**：
- **$100亿首轮——全球AI史上最大单笔融资之一**：更关键的是，这是DeepSeek第一次接受外部资金。此前梁文锋用对冲基金利润自费运营整个实验室。从「完全自费」到「接受$100亿外部资金」，意味着DeepSeek正从研究项目转型为产业基础设施
- **大基金领投——这不是商业决策，是国家战略**：中国国家集成电路产业投资基金的参与，说明DeepSeek被定位为AI产业的「国家级基础设施」。与半导体大基金同一体系，暗示AI芯片+AI模型将形成国家层面的整合
- **宁德时代参投——产业资本的信号**：全球最大电池公司投资AI模型公司，这不是跨界多元化，而是「AI+制造」的战略布局。具身智能、工业AI、自动驾驶——这些场景需要电池也需要模型
- **「AGI优先、盈利其次」——和OpenAI早期一样的叙事**：梁文锋的表态说明DeepSeek不会走商业化SaaS路线，而是继续押注基础研究。这意味着开源社区将继续受益于DeepSeek的技术突破
- **创业者启示**：**当国家级资本进入AI基础层，创业者的机会在「应用层」而非「模型层」**。DeepSeek的开源策略降低了模型门槛，但提高了竞争门槛——你的应用必须比DeepSeek自身做得更好，才能生存

**类比参考**：AI界的「台积电」——不做应用、专注基础设施，靠国家战略支撑。或者「中国的OpenAI + 国家主权AI基础设施」

![DeepSeek](/tmp/daily-screenshots/deepseek.png)

🔗 [TNW报道](https://thenextweb.com/news/deepseek-agi-goal-10bn-funding-round) | [Business Times](https://www.businesstimes.com.sg/startups-tech/startups/deepseek-founder-declares-artificial-general-intelligence-goal-70-billion-yuan-funding-round)

---

## 2. Manus AI — 被中国否决Meta $20亿收购后，创始人筹$10亿买回自己的公司

**融资信息**：正在探索$10亿融资以买回公司。估值至少与Meta原收购价$20亿持平。创始人Xiao Hong（肖弘）、Ji Yichao（季逸超）、Zhang Tao可能自掏资金补足差额。此前9个月突破$1亿ARR。2025年从中国迁至新加坡

**做什么的**：通用AI Agent——被称为「全球第一个通用AI Agent」，能自主完成复杂的数字任务和工作流。2025年3月上线即引爆全球，数百万人排队等候。被Meta于2025年12月以$20亿+收购

**为什么值得关注**：
- **地缘政治直接干预商业交易——创始人在调查期间被禁止离开中国**：这不是普通的反垄断审查。两位创始人在监管调查期间被限制出境，说明中国对AI核心技术外流的管控已经到了「物理限制」的程度
- **$10亿买回——创始人的决心和代价**：从$20亿卖给Meta到自筹$10亿买回来，这是一个戏剧性的反转。创始人在承担巨大的个人财务风险——但这也意味着他们对Manus的未来有极强的信心
- **9个月$1亿ARR——产品力是硬道理**：不管地缘政治怎么变，Manus的商业数据是真实的。9个月突破$1亿ARR的速度，在SaaS历史上也是顶尖水平
- **可能转向中国合资+香港IPO**：据报道Manus可能以「中国关联合资企业」的形式重新出现，最终瞄准香港上市。这是一个全新模式：西方技术市场+中国资本结构+香港资本市场
- **创业者启示**：**如果你的AI公司有中国基因，要做好「去哪里」的选址决策**。Manus从中国→新加坡→被Meta收购→被否决→买回，每一步都是地缘政治的棋子。创始人的选择空间正在缩小——要么完全脱离中国，要么接受中国资本结构

**类比参考**：AI版的「TikTok困局」——TikTok面对美国的强制出售，Manus面对中国的强制否决。或者「反向的Bytedance」——Bytedance保住了TikTok，Manus要买回自己

![Manus AI](/tmp/daily-screenshots/manus-ai.png)

🔗 [TFN报道](https://techfundingnews.com/china-said-no-to-metas-2b-deal-now-manus-ai-needs-1b-to-reclaim-what-it-built/) | [Bloomberg](https://techfundingnews.com/china-said-no-to-metas-2b-deal-now-manus-ai-needs-1b-to-reclaim-what-it-built/)

---

## 3. NanoCo (NanoClaw) — $12M Seed，拒绝$20M收购，Karpathy背书，6周从沙发到term sheet

**融资信息**：$12M超额认购Seed轮。Valley Capital Partners领投，Docker、Vercel、Monday.com、Slow Ventures参投，Hugging Face CEO Clem Delangue天使投资。以色列兄弟Gavriel和Lazer Cohen创办

**做什么的**：企业级AI Agent沙盒平台——从开源项目NanoClaw商业化而来。NanoClaw是OpenClaw的安全替代方案，AI Agent运行在隔离的容器沙盒中而非直接访问主机。250,000+下载。Andrej Karpathy推特点赞引爆，新加坡外长称其为「第二大脑」。现已开始签约企业客户

**为什么值得关注**：
- **6周从第一行代码到term sheet——2026年最快的创业故事**：Gavriel在沙发上写下NanoClaw的第一行代码，6周内拿到融资。而且拒绝了两次收购——一次六位数，一次$20M。「开源项目随社区增长而指数级增值」——这个来自朋友的关键建议改变了他们的决策
- **拒绝$20M收购——开源创业者的新范式**：传统的创业路径是build→被收购。NanoCo选择了build→开源→社区爆发→商业化。这个路径更慢但天花板更高。NanoClaw的250K下载量证明了社区的力量
- **Karpathy + 新加坡外长——KOL驱动的冷启动**：一个AI学术大V和一个国家政要同时为开源项目背书，这种冷启动方式不需要一分钱营销预算
- **企业客户的发现来自社区**：Big Tech高管在NanoClaw社区里用个人版，然后要求企业版。这是「bottom-up enterprise adoption」的教科书案例——先让技术人员用爽了，他们会帮你在公司里推
- **创业者启示**：**2026年最被低估的创业策略：先做开源项目，让社区验证需求，再商业化**。NanoCo证明了：250K下载 = 250K个潜在用户，其中包含大量企业决策者。获客成本几乎为零

**类比参考**：AI Agent版的「HashiCorp」——Vagrant/Nomad从开源到企业版的路径。或者「安全的OpenClaw，但走Docker式开源商业化路线」

![NanoCo](/tmp/daily-screenshots/nanoco.png)

🔗 [官网](https://nanoco.ai) | [TechCrunch](https://techcrunch.com/2026/05/20/nanoclaw-creator-turns-down-20m-buyout-offer-raises-12m-seed-instead/)

---

## 4. 维泛智能 — 数亿元种子轮，北大孵化，国内首家原生机器人「大脑芯片」

**融资信息**：数亿元人民币种子轮。中关村资本及旗下启航投资联合领投，上海未来产业基金、石溪资本、佰维存储、燕创集团、海益投资、探元创投共同投资。北京大学项目孵化

**做什么的**：原生机器人「大脑芯片」——融合类脑计算与通用GPU计算能力，为具身智能SOTA大模型原生设计。不是通用芯片改造成机器人用，而是从第一天起就为机器人AI模型设计芯片架构。国内首家定位「原生机器人芯片」的企业

**为什么值得关注**：
- **「原生」vs「改造」——芯片架构的路线之争**：目前大多数机器人公司用Nvidia GPU跑AI模型，维泛智能认为这是「用通用CPU跑手机App」——能用但不是最优。原生设计的芯片可以在功耗、延迟、推理速度上有数量级的优势
- **类脑计算+GPU的混合架构——技术路线很有想象力**：纯类脑芯片缺乏灵活性，纯GPU功耗太高。维泛试图把两者结合——类脑部分处理感知和直觉决策，GPU部分处理复杂推理。如果成功，将显著降低机器人AI的计算成本
- **北大孵化+中关村资本领投——高校→产业的标准路径**：中关村资本是北京国资背景的硬科技基金。高校技术成果转化+国资基金支持+产业资本跟进——这是中国硬科技创业的标准模型
- **佰维存储参投——产业链协同**：存储芯片公司投资计算芯片公司，说明产业链上下游在具身智能赛道形成了共识
- **创业者启示**：**在具身智能赛道，「算力层」可能是比「模型层」更好的切入点**。大家都在训练更大的模型，但很少有人优化模型运行的芯片。如果原生机器人芯片能大幅降低推理成本和功耗，它将成为具身智能的基础设施——就像Nvidia GPU之于LLM

**类比参考**：具身智能版的「Nvidia」——Nvidia为GPU计算设计专用芯片（CUDA生态），维泛为机器人AI设计专用芯片。或者「机器人领域的地平线（Horizon Robotics）」

![维泛智能](/tmp/daily-screenshots/weifan-intelligent.png)

🔗 [36氪首发](https://36kr.com/p/3821371042877575)

---

## 5. CortexDB V1 — AI Agent的记忆层，五层架构解决Agent「失忆症」

**融资信息**：独立开发者/初创公司产品。开源可用。2026年5月16日发布V1

**做什么的**：AI Agent的「体验层」（Experience Layer）——为Agent提供持久化的记忆系统。五层架构：Events（原始事件）→ Episodes（事件集）→ Facts（结构化事实）→ Beliefs（带置信度的信念）→ Understanding（综合理解）。模拟人脑的记忆循环：捕获→提取→协调→遗忘→巩固。在LongMemEval-S基准上93.8%（超过Mem0的93.4%），LoCoMo上86.9%

**为什么值得关注**：
- **「三层模型」的洞察非常精准**：CortexDB把AI系统分为三层——Layer 1 Intelligence（LLM，已商品化）、Layer 2 Knowledge（RAG，正在标准化）、Layer 3 Experience（记忆，缺失）。这个框架帮助创业者理解AI产品的价值链——你在哪一层？
- **五层记忆架构——不是数据库，是认知系统**：大多数AI记忆方案就是一个向量数据库。CortexDB做了五层，最独特的是「Beliefs」层——Agent不仅要记住事实，还要维护「置信度」和「证据链」。当Agent说「这笔交易有风险」时，它能回答「为什么这么想？」——这是企业信任Agent的前提
- **模拟人脑的「遗忘」机制——反直觉但正确**：不是所有记忆都有价值。CortexDB主动遗忘无关信息，只保留重要的。这和人脑的睡眠巩固机制类似——睡眠不是为了记住更多，而是为了筛选出真正重要的
- **93.8% LongMemEval-S——用数字说话**：不是概念验证，而是公开基准测试上的SOTA。在AI基础设施领域，benchmark是说服开发者的最好方式
- **创业者启示**：**AI Agent的记忆层是2026年被低估的基础设施机会**。模型越来越强、RAG越来越标准，但Agent的「体验记忆」几乎是空白。如果你做Agent产品，记忆是你必须自己解决的难题——除非有专门的记忆基础设施

**类比参考**：AI Agent版的「海马体」——人脑的海马体负责记忆的形成和巩固，CortexDB做的是Agent的海马体。或者「Agent的Mem0，但架构更完整、benchmark更强」

![CortexDB](/tmp/daily-screenshots/cortexdb.png)

🔗 [官网](https://cortexdb.ai) | [V1发布博文](https://cortexdb.ai/blog/v1)

---

## 6. Foundation (Passport Prime) — $6.4M，比特币硬件钱包公司转身做「AI Agent的人体授权器」

**融资信息**：$6.4M。Fulgur领投。波士顿。同时发布Passport Prime硬件设备

**做什么的**：「人类权威硬件设备」（Human Authority Hardware Device）——为AI Agent时代设计的硬件授权器。核心概念：当AI Agent要执行敏感操作（转账、签署合同、发送邮件），Passport Prime要求人类通过物理硬件实时确认。把比特币硬件钱包的安全理念迁移到AI Agent的权限管理上。KeyOS操作系统用Rust编写，微内核架构，应用沙盒隔离

**为什么值得关注**：
- **从比特币钱包到AI Agent授权——安全需求是相通的**：比特币硬件钱包解决的问题是「只有持有物理设备的人才能签名交易」。Passport Prime解决的问题是「只有持有物理设备的人才能授权AI Agent执行敏感操作」。安全逻辑完全一致，只是应用场景从金融扩展到了AI
- **「Human Authority」——AI信任的硬件层**：软件级别的Agent权限管理不够安全——密码可以被破解、session可以被劫持。但物理硬件不行。Foundation赌的是：随着Agent权限越来越大，企业会需要硬件级别的授权保障
- **Rust微内核——安全不是营销口号而是架构选择**：KeyOS用Rust写的微内核操作系统意味着：即使某个应用被攻破，主密钥和授权逻辑仍然安全。这是军事/金融级别的安全架构
- **波士顿比特币社区→AI安全赛道的桥梁**：Foundation来自比特币硬件钱包社区，这个社区对「trustless security」有深刻的理解。他们把这种思维带入了AI Agent安全赛道
- **创业者启示**：**当AI Agent获得越来越多自主权时，「谁能授权Agent」将成为核心安全问题**。纯软件的授权方案（API key、OAuth）不够——你不会用API key来保护你的银行账户。AI Agent的权限管理可能需要同样级别的硬件安全

**类比参考**：AI Agent版的「YubiKey」——YubiKey用硬件令牌保护人类登录，Passport Prime用硬件设备保护Agent授权。或者「AI时代的Ledger/Trezor」

![Foundation Passport Prime](/tmp/daily-screenshots/foundation-passport.png)

🔗 [官网](https://foundation.xyz) | [发布公告](https://foundation.xyz/blog/foundation-raises-6-4m-human-authority-hardware-launch)

---

## 7. Sapient Intelligence (HRM-Text) — 1B参数的类脑模型，用1/1000的数据达到强推理

**融资信息**：具体融资信息未公开。Sapient Intelligence是一家AI研究公司。MIT合作研究

**做什么的**：类脑推理语言模型HRM-Text——1B参数的小模型，基于Hierarchical Reasoning Module（层级推理模块）架构，仅用~400亿token训练（对比LLaMA的4万亿+token），实现了同等参数量下领先的推理能力。完全开源。核心创新：不是简单缩小大模型，而是用受大脑启发的架构从根本上改变训练方式

**为什么值得关注**：
- **「1000倍数据效率」——如果成立，将颠覆Scaling Law信仰**：当前AI产业的主流信仰是「更多数据+更大模型=更强能力」。HRM-Text挑战了这个前提：用1/1000的数据，通过不同的架构设计，也能达到强推理。这不是微调，是从预训练阶段就走上不同的路
- **1B参数的推理能力——「小模型大智慧」的范式**：当所有人都在追逐千亿万亿参数时，Sapient证明1B参数就够了。如果这个结论成立，它意味着：AI推理不需要巨大的算力——这对边缘计算、移动端、IoT设备是革命性的
- **类脑架构的工程化——不只是论文**：类脑计算已经谈了十年，但很少看到实际可用的模型。HRM-Text把类脑架构变成了一个开源模型，开发者可以直接用。这是从「研究」到「产品」的关键一步
- **完全开源——给社区验证的机会**：论文+代码+模型全部开源。这说明Sapient有信心经受社区检验。在AI领域，开源是建立信任最快的方式
- **创业者启示**：**「反Scaling Law」是2026年值得关注的赌注**。当大公司都在烧钱做大模型时，小团队有机会通过架构创新实现「少即是多」。如果你的目标不是通用AI而是特定领域的推理，小模型+类脑架构可能是更好的路线

**类比参考**：AI推理版的「AlphaGo」——AlphaGo用完全不同的方式（强化学习+搜索）打败了传统的「暴力计算」，HRM-Text用完全不同的架构（类脑+层级推理）挑战「暴力Scaling」。或者「1B参数的DeepSeek R1」

![Sapient HRM-Text](/tmp/daily-screenshots/sapient-hrm-text.png)

🔗 [官网](https://sapient.inc/hrm-text/) | [论文](https://arxiv.org/html/2605.20613) | [PR Newswire](https://www.prnewswire.com/news-releases/sapient-intelligence-launches-hrm-text-challenging-the-llm-monopoly-with-a-brain-inspired-foundation-model-trained-on-up-to-1000x-fewer-tokens-302774638.html)

---

## 📊 今日趋势总结

| 趋势 | 信号 |
|------|------|
| 🇨🇳 中国AI资本自主化 | DeepSeek $100亿+大基金领投，Manus $10亿买回自己——核心AI资产不再流向美元资本 |
| 🛡️ Agent安全与信任层产品化 | NanoCo沙盒、Foundation硬件授权、CortexDB记忆——三个维度解决「Agent怎么被信任」 |
| 🧠 类脑/反Scaling Law | 维泛智能类脑芯片、Sapient 1B参数模型——挑战「越大越好」的主流信仰 |
| 🔓 开源→商业化的验证 | NanoCo 250K下载→$12M、CortexDB开源→SOTA——开源是最好的冷启动 |
| 🏭 具身智能的底层分化 | 维泛智能做芯片、自变量做模型——具身智能不再是「一家公司全做」 |

---

> 📌 **422产品实验室**出品 | 每日精选AI新产品、融资、创新模式
>
> 关注我们，获取面向创业者的AI产品情报

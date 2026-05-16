# AI 产品日报 | 2026-05-07

> 🔬 422产品实验室 · AI新产品日报 · 每日精选

## 今日洞察

今天的AI创业圈释放了三个强信号：**「Agent的上下文基础设施」正式成为一个投资赛道**——SageOx拿了1500万美元种子轮做「Agentic Context Infrastructure」，AWS EC2创始团队下场，用硬件设备+软件层解决Agent「不知道团队在讨论什么」的问题；**「Agent编排层」进入战国时代**——Ruflo以45K Star和日增2,192的速度证明了多Agent编排的巨大需求，32个插件+联邦协作+自学习能力，正在成为Claude生态的「Kubernetes」；**「为Agent设计的后端」成为一个新品类**——InsForge把Postgres包装成Agent可理解的语义层，本质上是做Agent时代的基础设施。对创业者来说，**AI的机会正从「模型能力」转向「Agent基础设施」**——编排、路由、上下文、记忆、后端，每一层都值得重新做一遍。

---

## 1. SageOx — $1500万种子轮，让AI Agent拥有「团队记忆」（融资）

**融资信息**：种子轮 $15M，Canaan领投，A.Capital、Pioneer Square Labs、Founders' Co-op参投

**做什么的**：Agentic Context Infrastructure——通过硬件设备（Ox Dot）捕获会议室、站会、白板讨论等「非结构化上下文」，结合开源Ox CLI，让Claude Code、Codex等编码Agent在写代码之前就能知道「团队在之前的会议上决定了什么」。

**为什么值得关注**：
- **AWS EC2创始团队**：CEO Ajit Banerjee是AWS EC2原始团队成员，CTO Ryan Snodgrass是Amazon最早的微服务架构师之一。用「做云基础设施」的思路做Agent基础设施
- **硬件+软件的组合拳**：Ox Dot硬件设备支持「Auto Rewind」——会议忘记录音没关系，事后可以回溯捕获。这个思路比纯软件方案更贴合企业实际使用场景
- **「Open Work」激进透明**：公开所有内部prompt、规划会议、甚至未过滤的内部争论，用户可以实时观看团队构建产品
- **创业者启示**：**「Agent的上下文工程」正在从一个工程问题变成一个投资赛道**。当Agent能力越来越强，瓶颈从「能不能做」变成了「知不知道该做什么」

**类比参考**：Agent版的「Slack + 会议记录仪 + 知识库」，或者「给Agent装的耳朵和记忆」

🔗 [sageox.ai](https://sageox.ai/) | [Ox CLI (GitHub)](https://github.com/sageox/ox)

---

## 2. Ruflo — 45K Star的Claude多Agent编排平台（⭐ 45,270，日增2,192）

**融资信息**：开源项目（MIT协议），由rUv个人开发者维护

**做什么的**：Claude Code的多Agent编排平台——支持100+专业Agent、蜂群协作（Swarm）、自学习记忆、联邦通信（跨机器安全协作）、32个原生插件，让Agent不仅是「运行」而是「协作」。

**为什么值得关注**：
- **45K Star + 日增2,192**，GitHub Trending全球第一——这是Agent编排领域目前最受关注的开源项目
- **32个插件覆盖全链路**：从蜂群协调（swarm）到自驾驶（autopilot）、从安全审计到成本追踪、从知识图谱到IoT设备管理，堪称Agent生态的「App Store」
- **自学习架构（SONA）**：Agent从历史成功案例中学习，ReasoningBank + 轨迹学习——这不是简单的工具调用，而是真正的Agent能力进化
- **联邦协作**：Agent可以跨机器、跨组织安全协作，零信任架构，这在多团队协作场景中是刚需
- **创业者启示**：**Agent编排层正在形成类似Kubernetes的生态位**——当单Agent能力足够强时，多Agent协调、调度、记忆管理就是下一个瓶颈

**类比参考**：Agent界的「Kubernetes + Plugin Marketplace」，Claude版的「AutoGPT但真正能用的」

🔗 [GitHub](https://github.com/ruvnet/ruflo) | [Web UI](https://flo.ruv.io/)

---

## 3. Manifest — AI Agent的智能模型路由器（⭐ 6,238，日增71）

**融资信息**：开源项目（MIT协议）

**做什么的**：智能模型路由器——每个查询自动分配到最合适的模型，最高节省70% AI成本。支持16个提供商、300+模型，统一通过 `/auto` 端点路由。

**为什么值得关注**：
- **模型路由是一个真实且增长迅速的痛点**：企业同时使用OpenAI、Anthropic、Google、DeepSeek等多个模型，手动切换效率低且成本不透明。Manifest把这个过程自动化
- **订阅复用是杀手锏**：可以复用已有的ChatGPT Plus/Claude Pro/GitHub Copilot订阅，不需要额外API Key——直接把付费订阅变成可路由的推理资源
- **本地模型无缝接入**：Ollama、LM Studio、llama.cpp统一接入，本地+云端混合路由
- **成本追踪**：精确追踪每一分钱，支持通知和预算限制——企业合规的刚需
- **创业者启示**：**「模型路由层」可能是AI Infra的下一个大品类**——类似CDN在Web架构中的位置，不是内容本身，但决定了成本和性能

**类比参考**：AI模型版的「Cloudflare Load Balancer」，或者「LLM的智能DNS」

🔗 [GitHub](https://github.com/mnfst/manifest) | [manifest.build](https://manifest.build)

---

## 4. Local Deep Research — 本地运行的AI深度研究助手（⭐ 5,657，日增532）

**融资信息**：开源项目

**做什么的**：完全本地运行的AI研究助手——在SimpleQA基准上达到~95%准确率（与GPT-4.1-mini+云搜索相当），但所有数据不出本机。支持20+研究策略、10+搜索引擎、加密个人知识库。

**为什么值得关注**：
- **「本地≈云端」的性能里程碑**：用Qwen3.6-27B在单张3090上跑出接近云端大模型的研究质量，这标志着本地AI能力的临界点
- **LangGraph Agent策略**：新增自主Agent模式，LLM自行决定搜索什么、用哪个专业引擎、何时综合——自适应地在arXiv、PubMed、Semantic Scholar之间切换
- **知识复利**：每次研究会将有价值的论文/网页下载到加密知识库，下次研究可以同时搜索个人文档和实时网络——知识随时间复利增长
- **SQLCipher加密**：每个用户独立加密数据库，AES-256级别安全，零知识架构
- **创业者启示**：**「隐私优先的AI研究」在金融、法律、医疗等合规行业有巨大市场**——这些行业的数据不能上传到云端，但研究需求一点不比互联网公司少

**类比参考**：本地版的「Perplexity Pro」，或者「AI研究界的Obsidian——知识管理+AI推理」

🔗 [GitHub](https://github.com/LearningCircuit/local-deep-research)

---

## 5. InsForge — 为AI Coding Agent设计的后端平台（⭐ 8,451，日增230）

**融资信息**：开源项目（Apache 2.0）

**做什么的**：基于Postgres的后端开发平台，专门为AI Coding Agent和AI代码编辑器设计。通过语义层（Semantic Layer）让Agent理解、配置和操作数据库、认证、存储、函数等后端原语。

**为什么值得关注**：
- **「Agent可理解的后端」是一个新品类**：传统后端（Supabase、Firebase）是为人类开发者设计的API，InsForge是为Agent设计的语义接口——Agent不需要看文档，直接通过MCP协议理解可用的操作
- **一站式后端**：认证、数据库、存储、Edge函数、AI模型网关、计算、部署——七个后端原语统一在一个平台
- **部署体验极佳**：支持Railway、Zeabur、Sealos一键部署，Docker Compose本地运行
- **创业者启示**：当Agent负责越来越多的编码工作，**「Agent能理解的基础设施」比「人类能理解的API」更重要**。Supabase和Firebase的下一个版本可能不是给程序员用的，而是给Agent用的

**类比参考**：Agent版的「Supabase」，或者「给Claude Code用的后端操作系统」

🔗 [GitHub](https://github.com/InsForge/InsForge) | [insforge.dev](https://insforge.dev)

---

## 6. TabPFN — 表格数据的基础模型（⭐ 6,575，日增218）

**融资信息**：开源项目，PriorLabs出品，AAAI 2026论文

**做什么的**：首个专为表格数据（Tabular Data）设计的基础模型——不需要特征工程、数据预处理，直接fit/predict，在分类和回归任务上超越XGBoost、Random Forest等传统方法。

**为什么值得关注**：
- **「表格数据」是企业AI最大的未开发市场**：80%的企业数据是表格形式的（销售、用户、财务、供应链），但AI一直不擅长处理。TabPFN用Foundation Model的思路重新做表格学习
- **零预处理**：不需要标准化、不需要独热编码，直接fit——这对非ML工程师极其友好
- **性能惊艳**：在中小数据集（<100K样本）上全面超越XGBoost，训练速度秒级
- **PriorLabs团队背景**：来自斯坦福/剑桥，AAAI 2026接收，学术+工程双强
- **创业者启示**：**传统ML的「特征工程」环节可能被Foundation Model吃掉**——就像LLM吃掉了NLP的特征工程。做垂直行业AI的创业者应该关注这个趋势

**类比参考**：表格数据界的「GPT」——不需要调参，直接用的通用模型

🔗 [GitHub](https://github.com/PriorLabs/TabPFN) | [文档](https://priorlabs.ai/docs)

---

## 7. Kronos — 金融市场K线的基础模型（AAAI 2026）

**融资信息**：开源项目，AAAI 2026接收论文

**做什么的**：首个专为金融K线序列设计的基础模型——将OHLCV数据量化为分层离散Token，用自回归Transformer预训练，覆盖全球45+交易所数据。可用于预测、回测、量化策略。

**为什么值得关注**：
- **「金融市场的语言」被形式化了**：K线一直是量化的核心数据，但没有统一的「模型」来理解它。Kronos做了金融版的「Tokenizer + Foundation Model」
- **实时Demo可用**：可以在线查看BTC/USDT未来24小时的预测，不是PPT
- **完整的模型家族**：从4.1M的mini到499.2M的large，覆盖不同计算预算
- **创业者启示**：**垂直领域的基础模型是一个可持续的创业方向**——通用LLM做不好金融时序预测，但专门为K线训练的模型可以。这个思路可以复制到气象、供应链、能源等其他时序场景

**类比参考**：金融时序版的「GPT」，量化交易的「预训练基座」

🔗 [GitHub](https://github.com/shiyu-coder/Kronos) | [在线Demo](https://shiyu-coder.github.io/Kronos-demo/)

---

## 8. Agent Skills by Addy Osmani — AI编码Agent的生产级技能包

**融资信息**：开源项目，Google工程负责人Addy Osmani个人项目

**做什么的**：为AI Coding Agent（Claude Code、Cursor、Copilot等）提供的20+生产级工程技能——覆盖从需求定义（/spec）到交付（/ship）的完整开发生命周期，每个技能都包含结构化工作流、质量门禁和反模式表。

**为什么值得关注**：
- **Addy Osmani的背书**：Google Chrome团队工程负责人，写了《JavaScript设计模式》等经典，他的工程实践就是行业标准
- **7个阶段命令**：/spec → /plan → /build → /test → /review → /code-simplify → /ship，把高级工程师的工作流编码成Agent可执行的流程
- **跨Agent平台**：同时支持Claude Code、Cursor、Windsurf、Gemini CLI、Copilot、Kiro、OpenCode——不绑定单一生态
- **创业者启示**：**「Agent的行为标准化」是一个被低估的方向**——当Agent能力足够强时，约束Agent「怎么做」比让Agent「随便做」更有价值。这就像编码规范对人类开发者的意义

**类比参考**：AI编码Agent版的「Google Engineering Practices」，或者「Agent的SOP手册」

🔗 [GitHub](https://github.com/addyosmani/agent-skills)

---

## 📊 今日趋势总结

| 趋势 | 信号 |
|------|------|
| 🧠 Agent上下文基础设施 | SageOx $15M种子轮，AWS EC2创始团队做「给Agent的团队记忆」 |
| 🔀 Agent编排层竞争白热化 | Ruflo 45K Star日增2K，32插件+联邦协作，成Claude生态最热项目 |
| 💰 模型路由降本 | Manifest统一16提供商300+模型，最高省70%成本 |
| 🏗️ Agent原生后端 | InsForge为Agent设计语义层，Supabase的Agent-first版本 |
| 📊 垂直基础模型 | TabPFN（表格）、Kronos（金融K线）——Foundation Model思路渗透到每个数据类型 |
| 🔒 本地AI能力临界点 | Local Deep Research在3090上达到~95% SimpleQA准确率 |

---

> 📌 **422产品实验室**出品 | 每日精选AI新产品、融资、创新模式
> 
> 关注我们，获取面向创业者的AI产品情报

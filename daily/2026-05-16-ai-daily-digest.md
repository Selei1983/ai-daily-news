# AI 产品日报 | 2026-05-16

> 🔬 422产品实验室 · AI新产品日报 · 每日精选

## 今日洞察

今天最值得关注的信号是**「本地优先（Local-first）AI」正在从理念走向产品化**。Osaurus以5.3K Star和11.4万下载量证明了「推理是你唯一需要的云端能力，其他一切都可以属于你」——原生Swift、Mac本地运行Agent、记忆和工具全在本机。HermesPet把AI塞进MacBook的刘海里，零依赖开箱即用。两者共同指向一个趋势：**AI的「拥有权」正在成为用户核心诉求**。

与此同时，**Agent生态的「包管理器」赛道正式开跑**。Sx以HN 32赞切入「团队的AI技能私有npm」——把最优秀的开发者摸索出的AI使用模式打包、版本化、按角色分发。image-blaster以2048 Star展示了Claude Skills的产品化威力：一张图片→3D环境+音效+网格，5分钟完成。ExploitBench为Agent安全建立了量化基准——不是问「Agent是否安全」，而是测「Agent能爬到利用链的第几级」。

对创业者来说，今天的核心判断是：**AI的下一波竞争不是谁的模型更大，而是谁能让用户「拥有」AI**——本地推理、私有记忆、可控身份、团队级技能管理，每一条都是一个正在形成的独立品类。

---

## 1. Osaurus — Mac本地优先的AI Agent运行器，原生Swift、5.3K Star（⭐ 5,300）

**融资信息**：Osaurus, Inc.出品，MIT开源，TechCrunch 5月15日专题报道。联合创始人Terence Pae此前做过AI桌面伴侣Dinoki

**做什么的**：macOS原生AI Agent运行器——在Apple Silicon上通过MLX原生速度运行本地模型，同时可选接入云端模型。提供持久化记忆、沙箱代码执行、Agent身份管理、技能导入。所有数据（记忆、历史、密钥）全部留在本机，不上传任何内容除非用户主动选择。

**为什么值得关注**：
- **5.3K Star + 11.4万下载——「拥有你的AI」是真实需求**：TechCrunch专题报道中，创始人Pae的起点是用户质问「为什么我买了你的App还要付token费？」。这个痛点驱动了Osaurus的核心理念：推理是唯一需要云端的环节，其他一切（记忆、工具、身份）都归用户所有
- **原生Swift，非Electron——产品品质决定用户留存**：在AI桌面工具几乎全是Electron的时代，Osaurus选择了纯Swift原生开发。这意味着更低的内存占用、更快的启动速度、更原生的macOS体验。产品语言本身就是竞争力
- **MLX + 云端模型自由切换**：本地跑MLX（Apple Silicon原生优化），需要更强推理时无缝切换到云端。用户不绑定任何provider，推理自由
- **Agent不仅是聊天，还能执行代码**：沙箱执行环境让Agent可以真正做事——运行代码、管理文件、执行任务。这是从「AI助手」到「AI Agent」的关键跃迁
- **创业者启示**：**「AI的拥有权」是一个正在爆发的消费者需求**。当用户发现他们的AI记忆、对话历史、偏好都锁在某个SaaS里时，迁移成本会驱动他们寻找本地优先的替代品。同样的逻辑适用于：本地优先的AI笔记、本地优先的AI编程助手、本地优先的AI邮件

**类比参考**：AI Agent版的「Obsidian vs Notion」——Obsidian把文件留在你本机，Notion把数据锁在云端。或者「Ollama的Agent版，但带完整GUI和技能系统」

![Osaurus](/tmp/daily-screenshots/osaurus.png)

🔗 [官网](https://osaurus.ai) | [GitHub](https://github.com/osaurus) | [TechCrunch报道](https://techcrunch.com/2026/05/15/osaurus-brings-both-local-and-cloud-ai-models-to-your-mac/)

---

## 2. image-blaster — 一张图生成完整3D环境+音效+网格，Claude Skills的威力展示（⭐ 2,048，HN 125pts）

**融资信息**：开源项目，neilsonnn出品，Claude Code Skills架构

**做什么的**：从单张图片自动生成完整3D场景——包括3D模型（.glb/.obj）、高斯溅射静态环境（.spz）、环境循环音效和物体物理音效（.mp3）。串联World Labs的Marble模型、Hunyuan 3D、ElevenLabs SFX等多个生成模型，通过Claude Code Skills编排整个工作流。5分钟从图片到可导入Unity/Unreal/Godot的完整3D场景。

**为什么值得关注**：
- **2048 Star——Claude Skills生态的标杆案例**：image-blaster不是传统软件，而是一组Claude Code Skills的编排。它证明了「Agent Skills」不只是代码片段，而是一个完整的产品形态——把多个SaaS API串联成一条自动化工作流
- **从2D到3D的「一键转化」**：输入一张童年卧室照片→输出一个可探索的3D环境+独立3D物体模型+环境音效。这不是概念验证，而是可嵌入Unity/Unreal的生产级资产
- **多模型协作的工程范式**：Marble做环境、Hunyuan做3D模型、ElevenLabs做音效、Claude做编排。每个模型做最擅长的事，Agent负责编排。这是「多模型Agent工作流」的最佳实践
- **可调参数暴露了设计意图**：面数（40K-1.5M）、PBR材质、多边形类型——开发者可以精细控制输出，不是黑盒
- **创业者启示**：**「把多模型API编排成一条工作流」本身就是产品**。image-blaster的核心价值不在于任何单一模型，而在于用Agent把5个模型串联成「图片→3D」的一键体验。同样的模式可以复制到：视频→PPT、草图→网站、录音→播客、文档→演示

**类比参考**：3D版的「AI工作流自动化」——Zapier串联SaaS，image-blaster串联生成模型。或者「Claude版的3D建模师，但一图搞定」

![image-blaster](/tmp/daily-screenshots/image-blaster.png)

🔗 [GitHub](https://github.com/neilsonnn/image-blaster)

---

## 3. Sx — AI技能的私有包管理器，把团队最佳实践自动化分发（⭐ 125，HN 32pts）

**融资信息**：开源项目（Apache 2.0），Sleuth出品（YC校友公司），Go语言构建

**做什么的**：为AI编码助手设计的包管理器——团队中最优秀的开发者摸索出的Skills、MCP配置、Slash命令，通过Sx打包成可版本化、可分发的资产。新成员入职时自动继承整个团队的AI playbook。支持按org/team/repo/user/bot五个粒度控制谁能看到哪些技能。兼容Claude Code、Cursor、Copilot、Gemini、Kiro等所有主流AI客户端。

**为什么值得关注**：
- **「团队AI能力的NPM」——一个全新品类**：当AI编码助手的技能（CLAUDE.md、.cursor/rules）还靠人工复制时，Sx做的是把这些碎片化知识变成可管理的包。这和npm之于Node.js、pip之于Python是同一个生态位
- **五层权限粒度说明这不是玩具**：org全员→团队→仓库→路径→个人→Bot——每一层都有独立的安装策略。这说明Sleuth在认真思考企业级场景
- **`sx install --dry-run` 是关键设计**：在安装前就能看到「我会得到什么技能」，这是对可预测性的尊重。企业IT部门需要这种可控性
- **跨客户端兼容是护城河**：不是只给Claude Code用，而是所有AI编码客户端通用。当团队里有人用Claude Code、有人用Cursor、有人用Copilot时，Sx是唯一能把AI知识统一的工具
- **创业者启示**：**「AI知识的版本管理和分发」是一个被严重低估的基础设施需求**。当每个团队都在CLAUDE.md里积累prompt工程经验时，这些知识的共享、版本化、权限控制就是刚需。这和Docker Hub之于容器镜像、npm之于JS包是同一个逻辑

**类比参考**：AI技能版的「npm + Artifactory」——不只是包管理器，还是私有仓库。或者「团队的AI playbook自动化平台」

![Sx](/tmp/daily-screenshots/sx.png)

🔗 [GitHub](https://github.com/sleuth-io/sx) | [官网](https://skills.new)

---

## 4. Elephant Agent — 「大象从不遗忘」的自我进化个人AI，记忆变成关怀（⭐ 109）

**融资信息**：开源项目，agentic-in出品，Python构建，有配套论文

**做什么的**：基于「Personal Model」理念的自我进化AI Agent——不像传统AI每次对话从头开始，Elephant Agent维护四个持续更新的理解维度：Identity（你是谁）、World（你的世界）、Pulse（当前节奏）、Journey（你的经历）。通过「好奇式学习」主动提问填补理解空白，通过「背景学习」在空闲时整理记忆。多个Elephant组成一个Herd。

**为什么值得关注**：
- **「记住更少，但理解更深」——这是对RAG堆砌的反思**：当大多数Agent在追求更长的上下文窗口时，Elephant Agent的核心洞察是：不是记住所有对话，而是识别哪些记忆值得携带。四个Lens（Identity/World/Pulse/Journey）是一个精炼的记忆框架
- **「好奇式学习」让Agent主动提问**：不是被动等待指令，而是在发现理解空白时问一个有用的问题。这让Agent从工具变成伙伴
- **可纠正的记忆是关键创新**：用户可以在Dashboard里直接编辑Agent对自己的理解。Agent展示证据、接受纠正、允许沉默。这不是「AI记住了什么」，而是「用户允许AI知道什么」
- **有配套论文，学术严谨**：有专门的论文页面说明方法论，不是纯工程项目的拍脑袋设计
- **创业者启示**：**「个人AI的记忆管理」是一个全新品类**。当个人AI从工具变成伙伴时，它需要的不只是更大的数据库，而是一套关于「什么值得记住、什么应该遗忘、什么需要纠正」的哲学。Elephant Agent提供了这套框架

**类比参考**：AI版的「私人日记+管家」——不是搜索你的所有对话，而是像一个认识你多年的管家，知道你的习惯、记住重要的事、该忘的忘掉。或者「Personal CRM + 日记 + AI伙伴」

![Elephant Agent](/tmp/daily-screenshots/elephant-agent.png)

🔗 [GitHub](https://github.com/agentic-in/elephant-agent) | [官网](https://elephant.agentic-in.ai/) | [论文](https://elephant.agentic-in.ai/paper/)

---

## 5. Adrian — AI Agent的运行时安全监控引擎，实时检测恶意工具调用（⭐ 43）

**融资信息**：开源项目（Apache 2.0），Secure Agentics出品，Go后端+Python SDK，支持自托管和云托管

**做什么的**：AI Agent的运行时安全监控和控制引擎——分析Agent的工具调用、行为日志和推理轨迹（reasoning traces），检测恶意、失准或越权行为，支持在飞行中拦截。两行代码接入LangChain/LangGraph。自托管版本在本地跑Gemma模型做分类，无需联网。

**为什么值得关注**：
- **「分析推理轨迹」而非只看行为**——比传统安全监控深一层**：传统安全工具监控Agent「做了什么」（工具调用）。Adrian额外分析Agent「为什么这样做」（推理轨迹）。这意味着它能捕获「行为看起来正常但意图恶意」的攻击
- **AARM-aligned——有行业标准支撑**：遵循AARM（Agent Attestation and Runtime Monitoring）标准，不是自造轮子
- **审计模式 vs 阻断模式**：可以先在审计模式下运行，只观察不干预；确认策略有效后再切到阻断模式。这对生产环境渐进式部署非常友好
- **自托管 + 本地Gemma模型 = 数据不外泄**：企业不需要把Agent的安全日志发给第三方。本地Llama.cpp跑Gemma分类器，完全离线
- **创业者启示**：**「Agent的运行时安全」正在从可选项变成必选项**。当Agent开始执行交易、发送邮件、操作数据库时，企业需要的不只是部署前审查（如Scope MCP），更需要运行时的实时监控和拦截。Adrian做的是「Agent世界的杀毒软件+防火墙」

**类比参考**：Agent版的「CrowdStrike + Falco」——CrowdStrike监控终端异常，Adrian监控Agent异常。或者「AI Agent的WAF（Web应用防火墙）」

![Adrian](/tmp/daily-screenshots/adrian.png)

🔗 [GitHub](https://github.com/secureagentics/Adrian) | [文档](https://docs.adrian.secureagentics.ai) | [Dashboard](https://app.adrian.secureagentics.ai)

---

## 6. HermesPet — AI住进MacBook刘海，灵动岛精灵+桌面宠物+文件嗅探（⭐ 29）

**融资信息**：开源项目（Apache 2.0），个人开发者basionwang出品，Swift 6 / SwiftUI原生

**做什么的**：常驻MacBook灵动岛（Dynamic Island）的AI桌面伴侣——按一下刘海呼出聊天、⌘⇧V语音输入、拖文件给AI「吃掉」、Claude模式下小像素精灵Clawd在桌面闲逛嗅你的文件。四引擎并行（DeepSeek/Claude/Codex/在线模型），最多8个对话同时运行。纯原生Swift，无Electron。

**为什么值得关注**：
- **「AI住在你刘海里」——产品直觉惊人**：在所有人做AI聊天框时，HermesPet把AI放进了MacBook硬件上最被忽视的交互入口——灵动岛。这不是隐喻，是字面意思：左耳显示精灵头像，右耳显示任务状态，错误时变琥珀色
- **Clawd桌面精灵不只是卖萌**：空闲3分钟后从灵动岛跳到桌面的像素小人，会自动嗅文件并给短评、会被拖到文件上分析、会把拖入的文件作为附件发送、会被鼠标吸引。这是一个「主动型AI」的物理隐喻
- **敏感文件本地黑名单**：薪资、合同、密码、.env等关键词自动跳过——安全意识融入产品设计
- **零依赖开箱即用**：不需要安装任何CLI工具，DMG双击安装→选服务商→粘API Key→开聊。如果检测到claude/codex CLI则自动解锁高级能力
- **创业者启示**：**「硬件入口+AI」的想象力才刚刚开始**。灵动岛、Touch Bar、键盘灯带、侧边屏——每个硬件的「闲置像素」都可以是AI的入口。HermesPet证明了：不需要做AI硬件，只需要把现有硬件的未用空间变成AI界面

**类比参考**：AI版的「电子宠物（拓麻歌子）+ Clippy」——但不是在屏幕上弹窗，而是住在MacBook的刘海里。或者「macOS版Rabbit R1，但零额外硬件」

![HermesPet](/tmp/daily-screenshots/hermespet.png)

🔗 [GitHub](https://github.com/basionwang-bot/HermesPet)

---

## 7. ExploitBench — 量化测试AI Agent能爬到漏洞利用链的第几级（⭐ 51）

**融资信息**：开源项目（MIT），独立研究团队出品，学术合作开放

**做什么的**：为AI Agent安全能力建立量化基准——不是问「Agent能否发现漏洞」，而是测量Agent在漏洞利用阶梯上能爬到哪一级：到达脆弱代码→触发Bug→构建exploit原语→任意代码执行。首个benchmark针对Chromium V8引擎的16个能力维度。支持所有主流模型API。

**为什么值得关注**：
- **「利用是阶梯，不是开关」——安全评估的范式升级**：传统安全benchmark只有「能/不能」两个答案。ExploitBench把利用过程拆成阶梯，测量Agent每一级的能力。这把「Agent安全」从定性讨论变成了定量科学
- **首个benchmark就选了V8——难度拉满**：Chromium V8是地球上被最严格审计的软件之一。如果Agent能在V8上爬到利用链的高层，那在普通软件上就更不在话下
- **预构建Docker镜像，70GB/个——降低复现门槛**：每个CVE环境打包成Docker镜像推到GHCR，研究者不需要自己构建。这是对学术友好的设计
- **明确禁止RL训练**——保护benchmark不被污染。这是负责任的研究态度
- **创业者启示**：**「AI安全benchmark」是一个正在形成的独立品类**。当企业采购AI Agent产品时，他们需要量化的安全评估。ExploitBench的模式可以复制到：Agent金融安全benchmark、Agent隐私泄露benchmark、Agent合规benchmark

**类比参考**：Agent安全版的「SWE-bench」——SWE-bench测编码能力，ExploitBench测安全利用能力。或者「AI Agent的 penetration testing 标准化」

![ExploitBench](/tmp/daily-screenshots/exploitbench.png)

🔗 [GitHub](https://github.com/exploitbench/exploitbench) | [排行榜](https://exploitbench.ai)

---

## 8. pgGraph — 给Postgres加图数据库超能力，AI Agent的关系查询利器（⭐ 140）

**融资信息**：开源项目（Apache 2.0），Evokoa出品，Rust语言（基于pgrx），PostgreSQL 13-18支持

**做什么的**：PostgreSQL扩展，为现有数据表添加图搜索、遍历、最短路径和关系查询能力。表仍然是数据的唯一真相来源（source of truth），pgGraph在其上构建派生图索引，通过SQL中的`graph` schema函数查询。不需要迁移数据到图数据库。

**为什么值得关注**：
- **「不换数据库，只加能力」——极低迁移成本**：大多数图数据库（Neo4j、Dgraph）要求你迁移数据。pgGraph直接在现有Postgres表上建图索引，SQL里加个`graph.`前缀就能做图查询。这对已有大量Postgres数据的公司来说是零摩擦接入
- **Rust + pgrx = 高性能**：用pgrx框架把Rust写进PostgreSQL扩展，性能接近C扩展。图遍历和最短路径在数据库层完成，不需要把数据拉到应用层
- **AI Agent的「关系推理」需要图数据库**：当Agent需要理解「这个用户认识谁」「这个项目依赖什么」「这个漏洞影响了哪些系统」时，关系查询是核心能力。pgGraph让Agent直接在SQL里做这些查询
- **Early Alpha但有清晰的路线图**：开源态度积极，Discord社区活跃，Product Hunt上有跟踪
- **创业者启示**：**「给现有数据库加AI友好的查询能力」是一个有明确买家的方向**。每个用Postgres的公司都有「关系查询很痛苦」的问题。pgGraph不是要替代Neo4j，而是让8000万Postgres用户不需要迁移就能获得图查询能力

**类比参考**：图数据库版的「PostGIS」——PostGIS给Postgres加了地理空间能力，pgGraph加了图查询能力。或者「Postgres内的Neo4j，但零数据迁移」

![pgGraph](/tmp/daily-screenshots/pggraph.png)

🔗 [GitHub](https://github.com/Evokoa/pgGraph) | [文档](https://docs.evokoa.com/pggraph/user_guide)

---

*🔬 以上为422产品实验室AI产品日报 · 2026年5月16日 · 每日精选，欢迎转发*

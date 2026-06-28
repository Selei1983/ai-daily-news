# 0628日报 | 垂直AI产品密集爆发

## 今日洞察

今天的信号极为清晰：**AI 不再只是写代码和写文案的工具——它正在解决存在了千年的物理世界问题，并在金融和招聘领域产生可量化的 ROI。** HaloBraid 拿下 $7M 种子轮（Reddit 联合创始人 Alexis Ohanian 的 Seven Seven Six 领投），用机器人辅助编发——这个全球每年消耗 80 亿小时的手工活终于有了自动化方案。Fika Jobs 拿 $4M 预种子轮，让 AI Agent 真正执行视频面试，把招聘流程 TikTok 化。AI Berkshire（GitHub 4.1K star）更硬核——用 Claude Code 多 Agent 框架跑真实投资组合，2024 年收益 +69%，连续两年跑赢标普 500 超 46 个百分点。

基建层面，Agent 生态持续纵深演进：Cognee（24K star，日增 780）给 Agent 装上持久记忆；Workweave Router（HN 201 赞）50ms 内智能路由模型，编码 Agent 成本直降 40-70%；OpenSpec（57K star）正在把 spec-driven development 变成 AI 辅助编码的标准方法论。而地缘政治层面，Sakana AI 的 Fugu 模型趁 Anthropic 出口禁令窗口期发布，展示了监管壁垒如何为非美国 AI 公司创造即时市场空隙。**结论：当 AI 开始帮你编头发、面试候选人、管理投资组合——垂直 AI 已经从「新鲜感」跨入「实用工具」阶段。**

---

## 1. [HaloBraid](https://www.halobraid.com/)（融资 / 机器人 + AI）

![HaloBraid](/tmp/daily-screenshots/halobraid.png)

🔗 链接：[官网](https://www.halobraid.com/) | [TechCrunch 报道](https://techcrunch.com/2026/06/23/halobraid-raises-7m-from-seven-seven-six-to-end-the-six-hour-hair-salon-appointment/)

**融资信息**：**700 万美元种子轮**，由 **Seven Seven Six**（Reddit 联合创始人 Alexis Ohanian 的风投基金）领投。

**做什么的**：用机器人辅助编发——发型师起头后，设备能在数秒内完成剩余编发。首个产品将于今年晚些时候上市，面向专业沙龙。

**为什么值得关注**：
- 切入了一个**被科技遗忘的千亿级市场**：全球每年花在编发上的时间估计达 80 亿小时，95% 的受访者表示如果更快就会更频繁地编发。这是一个「人人都知道是痛点，但没人觉得能用技术解决」的领域。
- 创始人 **Yinka Ogunbiyi**，哈佛工程硕士 + MBA，此前创办过智能厨电公司。她把编发视为一个**工程问题**而非美学问题——这种思维方式本身就很稀缺。
- 产品定位极为聪明：不是替代发型师，而是**辅助发型师**。这意味着不会遭到行业抵制，反而被从业者视为救星（减少职业病、提高翻台率）。
- 对创业者的启发：**AI + 硬件的最大的机会不在工厂，而在那些「从来没被自动化过」的服务业。千年手艺 + AI = 新品类**。

**类比参考**：**「编发版的 Da Vinci 手术机器人 / 美业版的 Tesla Optimus」**

---

## 2. [Fika Jobs](https://fikajobs.com/)（融资 / AI 招聘）

![Fika Jobs](/tmp/daily-screenshots/fika-jobs.png)

🔗 链接：[官网](https://fikajobs.com/) | [TechCrunch 报道](https://techcrunch.com/2026/06/23/fika-jobs-raises-4m-to-build-a-video-first-hiring-platform-where-ai-agents-interview-candidates/)

**融资信息**：**400 万美元预种子轮**。Stockholm 团队。

**做什么的**：视频优先的招聘平台——候选人连接 LinkedIn 后，AI Agent 生成个性化面试问题，进行约 10 分钟的视频面试，自动将回答剪辑成短视频档案。雇主像刷 TikTok 一样发现候选人。当前由 Google Gemini 驱动。

**为什么值得关注**：
- **不是用 AI 筛简历，而是用 AI 替代整个初面环节**。这比传统的 ATS（Applicant Tracking System）更激进——AI Agent 直接与候选人对话、追问、生成评价。
- 产品形态融合了三个趋势：AI Agent 做重复性工作 + 短视频内容消费习惯 + LinkedIn 式职业身份。**LinkedIn + TikTok + AI Interviewer** 的组合极为新颖。
- 创始人分享的 aha moment 很有共鸣：差点因为简历不出彩错过一个优秀候选人，因为亲自聊了才发现。**Fika 本质上是在规模化「亲自聊」这个动作**。
- 对创业者的启发：**AI Agent 在 HR 领域的最佳切入角不是「筛选」，而是「对话」。让 Agent 真正和候选人交流，比让它看简历有效 100 倍**。

**类比参考**：**「招聘版的 ChatGPT + TikTok / AI 原生的 HireVue」**

---

## 3. [Sakana AI Fugu](https://sakana.ai/fugu/)（产品发布 / 地缘 AI）

![Sakana Fugu](/tmp/daily-screenshots/sakana-fugu.png)

🔗 链接：[Fugu 官网](https://sakana.ai/fugu/) | [TechCrunch 报道](https://techcrunch.com/2026/06/27/asian-ai-startups-launch-mythos-like-models-as-anthropics-export-ban-drags-on/)

**融资信息**：Sakana AI 此前已获多轮融资（包括 Nvidia 投资），估值超 $10 亿。Fugu 为最新发布的前沿模型。

**做什么的**：以日语「河豚」命名的前沿 AI 模型，声称与 Anthropic 的 Fable 5 和 Mythos Preview 并驾齐驱，专为 Agent 编排设计，能通过 API 调用其他模型。在 Anthropic 出口禁令持续期间打出了「前沿能力，无出口管制风险」的口号。

**为什么值得关注**：
- **教科书级的市场时机把握**：Anthropic 被 Trump 政府禁止向非美国用户提供 Mythos/Fable 模型，全球用户突然失去最强 Agent 模型的访问权。Sakana 在这个窗口期推出对标产品，官网直接写「delivering frontier capability without the risk of export controls」——这不是巧合，是精准的市场卡位。
- Sakana 由前 Google 研究员 Ren Ito、Llion Jones 和 David Ha 于 2023 年在东京创立，专注小数据集和日语优化。Fugu 的发布标志着它从「日本本土 AI 公司」升级为**全球 Agent 模型竞争者**。
- 同期中国 360 公司发布了「屠龙风」网络安全 AI，声称可对标 Mythos。**亚洲 AI 公司正在集体填补 Anthropic 出口禁令留下的真空**。
- 对创业者的启发：**地缘政治的突变会在一夜之间创造巨大的市场缺口。谁准备好了替代方案，谁就能吃下这波红利——这不只是运气，是长期产品积累 + 时机敏锐度的结合**。

**类比参考**：**「日本版 DeepSeek / Agent 编排版的 Hugging Face」**

---

## 4. [Cognee](https://github.com/topoteretes/cognee)（开源 / Agent 记忆层）

![Cognee](/tmp/daily-screenshots/cognee.png)

🔗 链接：[GitHub](https://github.com/topoteretes/cognee) | [官网](https://docs.cognee.ai)

**融资信息**：开源项目（MIT），GitHub **24,000+ star**，日增 **780 star**。已有 Claude Code 插件和 Rust 客户端。

**做什么的**：开源 AI Agent 记忆平台——接入任何格式的数据，自动构建自托管的知识图谱，让 Agent 在跨会话中保持持久长期记忆。结合向量嵌入、图谱推理和认知科学本体论。

**为什么值得关注**：
- **Agent 记忆是 Agent 生态最关键的缺失环节之一**。当前大多数 Agent 每次对话都从零开始，无法积累对用户和业务的认知。Cognee 把「记忆」变成了一个可插拔的基础设施层。
- 技术方案极为扎实：不只是向量搜索，而是**知识图谱 + 向量嵌入 + 认知科学本体论**的三层架构。有相关研究论文发表在学术期刊上。
- 生态布局全面：已有 Claude Code 插件（claude-code-plugin）、Rust 客户端（cognee-rs）、TypeScript 客户端（@cognee/cognee-ts），以及 OpenClaw 插件。**这不是一个 hobby project，而是一个有商业生态野心的基础设施**。
- 对创业者的启发：**Agent 的「大脑」（LLM）已经很强大，但「海马体」（记忆）还是空白。谁能做好 Agent 的记忆层，谁就是 Agent 时代的数据库公司**。

**类比参考**：**「Agent 版的 Pinecone + Neo4j / AI 时代的 Mem0」**

---

## 5. [Workweave Router](https://github.com/workweave/router)（开源 / Agent 成本优化）

![Workweave Router](/tmp/daily-screenshots/workweave-router.png)

🔗 链接：[GitHub](https://github.com/workweave/router) | [HN 讨论](https://news.ycombinator.com/item?id=48644463)

**融资信息**：Weave（工程智能平台，客户含 Robinhood、PostHog、Reducto）出品。HN **201 赞**，GitHub **468 star**。

**做什么的**：模型路由代理——一个本地代理端点，在 **50ms 内**自动为每个 prompt 选择最优模型。支持 Anthropic、OpenAI、Gemini 的原生 API，也支持 DeepSeek、Kimi、GLM、Qwen 等开源模型。一行命令 `npx @workweave/router` 搞定。

**为什么值得关注**：
- 解决了 Agent 时代最痛的问题：**用 GPT-4 做所有事情太贵，手动切模型太累**。Router 用一个基于 Avengers-Pro 1 的集群评分器，在每次请求时自动选择最优模型，声称**降低 40-70% 成本**。
- 产品体验极佳：不需要改代码，只需要把 Claude Code / Codex / Cursor 指向 `localhost:8080`，Router 自动接管所有模型选择。**零代码侵入的成本优化**。
- BYOK（Bring Your Own Key）设计——密钥本地加密存储，不走第三方服务器。对企业安全团队友好。
- 对创业者的启发：**多模型时代，模型路由不是一个功能，而是一个独立品类。类似 CDN 之于 Web——用户不需要知道后端路由逻辑，只需要更快更便宜的结果**。

**类比参考**：**「AI 版 Cloudflare Workers Router / Coding Agent 的 Portkey」**

---

## 6. [PPT Master](https://github.com/hugohe3/ppt-master)（开源 / AI 内容生产）

![PPT Master](/tmp/daily-screenshots/ppt-master.png)

🔗 链接：[GitHub](https://github.com/hugohe3/ppt-master)

**融资信息**：开源项目，GitHub **33,100+ star**，日增 **589 star**。有多个赞助商（PackyCode、APIKEY.FUN 等）。

**做什么的**：AI 从任何文档生成**真正可编辑的 PowerPoint**——原生形状和动画，支持自定义 .pptx 模板，演讲者备注由 AI 语音生成。不是生成图片slide，而是生成可二次编辑的原生 PPT。

**为什么值得关注**：
- **核心差异点极为关键**：市面上大部分 AI 做 PPT 是生成截图/图片，用户无法编辑。PPT Master 生成的是**原生 PowerPoint 格式**——每个文本框、图形、动画都可以在 PowerPoint 中修改。这是「AI 生成」和「AI 赋能」的本质区别。
- 33K+ star 说明痛点极为广泛。在中国市场（项目主语言为中文），PPT 制作是职场最高频的「时间黑洞」之一。
- 开源 + 赞助商模式：项目本身免费，但通过推荐 API 中转服务（PackyCode、APIKEY.FUN 等）变现。**这是一种巧妙的「流量变现」开源商业模式**——项目越火，API 中转的佣金越多。
- 对创业者的启发：**AI 内容生成的下一个竞争维度不是「能不能生成」，而是「生成的东西能不能用」。从图片到原生格式，是质变**。

**类比参考**：**「开源版的 Gamma / 可编辑版的 Beautiful.ai」**

---

## 7. [OpenSpec](https://github.com/Fission-AI/OpenSpec)（开源 / AI 开发方法论）

![OpenSpec](/tmp/daily-screenshots/openspec.png)

🔗 链接：[GitHub](https://github.com/Fission-AI/OpenSpec)

**融资信息**：Fission-AI 出品，开源项目。GitHub **57,100+ star**——今天榜单中 star 数最高的项目。

**做什么的**：为 AI 编码助手设计的**规格驱动开发**（Spec-Driven Development）框架。通过 `/opsx:propose` → `/opsx:apply` → `/opsx:archive` 的工作流，让 AI 编码助手先理解需求、制定方案、生成任务清单，再逐步实现——而非直接盲目写代码。

**为什么值得关注**：
- **57K star 的惊人数字说明了一件事：开发者迫切需要「管理 AI 编码助手」的方法论**。当 AI 可以瞬间生成代码，瓶颈不再是编码速度，而是「让 AI 做对的事」。
- OpenSpec 的哲学与传统 SDD（规格驱动开发）不同：fluid not rigid、iterative not waterfall、built for brownfield not just greenfield。它不是在管理人类开发者，而是在**管理 AI 开发者**。
- 工作流设计极为精妙：`/opsx:explore`（探索）→ `/opsx:propose`（提案）→ `/opsx:apply`（实现）→ `/opsx:archive`（归档）。每一步都有结构化输出（proposal.md、specs/、design.md、tasks.md）。**这实际上是在给 AI 编码助手做项目管理**。
- 对创业者的启发：**AI 编码助手的最大问题不是代码质量，而是需求理解。谁能让 AI 先「听懂」再做，谁就解决了 AI 编码的最后一块拼图**。

**类比参考**：**「AI 编码版 Scrum / Coding Agent 的产品经理」**

---

## 8. [AI Berkshire](https://github.com/xbtlin/ai-berkshire)（开源 / AI 投研）

![AI Berkshire](/tmp/daily-screenshots/ai-berkshire.png)

🔗 链接：[GitHub](https://github.com/xbtlin/ai-berkshire)

**融资信息**：开源项目，GitHub **4,100+ star**，日增 **685 star**。中文社区项目。

**做什么的**：基于 Claude Code / Codex 的价值投资研究框架——将巴菲特、芒格、段永平、李录四位投资大师的方法论系统化，通过多 Agent 并行对抗分析，输出结构化投资建议。**有真实实盘业绩验证**。

**为什么值得关注**：
- **这是目前看到的用 AI Agent 做专业投研最有说服力的案例**。不是回测模拟，是真金白银：2024 年 +69.29%，2025 年至今 +66.38%，连续两年大幅跑赢标普 500、恒生指数和沪深 300。两年累计收益超 146 万元。
- 核心创新是**多大师视角对抗**：不是让 AI 给出平衡分析（「一方面...另一方面...」），而是让四个视角产生真实的矛盾和张力，最后强制给出结论——通过/不通过/灰色地带，带具体价格区间。
- 「镜子测试」设计精妙：5 句话说不清投资逻辑 = 不买，没有例外。**这是把投资纪律编码为 Agent 规则**。
- 对创业者的启发：**AI Agent 在金融领域的最佳实践不是预测股价，而是系统化执行已验证的投资方法论。AI 不创造新智慧，而是严格执行大师的纪律——这比「AI 选股」靠谱 100 倍**。

**类比参考**：**「Claude Code 版的 Bridgewater / 一个人就能运营的伯克希尔」**

---

## 值得重点跟踪的 3 个信号

1. **AI 正在解决「从来没被自动化过」的物理世界问题**：HaloBraid 用机器人编发，切入的是一个存在数千年、全球年耗 80 亿小时的手工活。**AI + 硬件的最大机会不在工厂，而在服务业中被忽视的角落**。

2. **「管理 AI 编码助手」本身正在成为一个品类**：OpenSpec（57K star）管理 AI 需求理解，Workweave Router（201 HN 赞）管理 AI 模型选择，Cognee（24K star）管理 AI 记忆。**当 Agent 越来越强，「谁来管理 Agent」就是最大的新赛道**。

3. **地缘政治正在重塑全球 AI 格局**：Sakana Fugu 趁 Anthropic 出口禁令窗口期推出，中国 360 发布对标 Mythos 的屠龙风——**监管壁垒正在为非美国 AI 公司创造前所未有的市场机会**。对于关注出海的中国 AI 创业者，这是一个值得高度重视的信号。

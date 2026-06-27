# 0627日报 | AI基建赛道百亿融资爆发

## 今日洞察

今天释放了一个极其强烈的信号：**AI 基础设施层正在吸收百亿级资金，而且每一层都有专业玩家填位**。Patronus AI 拿下 $50M B 轮（收入一年涨 15 倍），专门做 Agent 压力测试——几乎所有前沿 AI 实验室都是它的客户；General Intuition 以 $23 亿估值拿了 $3.2 亿，用游戏行为数据训练通用 Agent；Unconventional AI 由 Databricks 前 AI 主管创立，要用振荡器芯片把推理功耗降低 1000 倍；Netris 拿了 a16z 的 $15M A 轮，做 AI 云的网络自动化。与此同时，开源生态也在狂飙：Google Labs 的 design.md 一天 2400+ star，为 Coding Agent 定义设计系统标准；Garry Tan（YC 总裁）开源了自己的 Claude Code 工具栈 gstack。**结论：当所有人都在关注模型层和应用层时，真正赚到大钱的是「让 Agent 可靠运行」的基建层。**

---

## 1. [Patronus AI](https://www.patronus.ai/)（融资 / Agent 测试评估）

![Patronus AI](/tmp/daily-screenshots/patronus-ai.png)

🔗 链接：[官网](https://www.patronus.ai/) | [TechCrunch 报道](https://techcrunch.com/2026/06/25/patronus-ai-lands-50m-to-build-digital-worlds-that-stress-test-ai-agents/)

**融资信息**：**5000 万美元 B 轮**，由 **Greenfield Partners** 领投，**Notable Capital、Lightspeed、Datadog、Samsung** 参投。总融资达 $70M。

**做什么的**：构建「数字世界模型」——为 AI Agent 创建模拟网站和内部系统的复刻环境，用强化学习在这些环境中压测 Agent 的表现，发现 Agent 走捷径、偷懒或出错的行为。

**为什么值得关注**：
- **收入一年增长 15 倍**，几乎所有前沿 AI 实验室和大量初创公司都是客户。投资人形容需求「几乎是永不满足的」。
- 类比 Waymo 用合成世界训练自动驾驶——Patronus 用同样的思路训练和验证 AI Agent。Agent 倾向于「走捷径」，Patronus 最擅长的是「抓住这些偷懒行为并追责」。
- 创始人 Anand Kannappan 和 Rebecca Qian 均来自 Meta AI Research。
- 对创业者的启发：**Agent 评估和测试不是一个辅助工具，而是一个独立赛道。当 Agent 被赋予越来越多自主权，「验证它做得对不对」本身就是刚需**。

**类比参考**：**「AI Agent 版 Waymo 模拟器 / Agent 的渗透测试公司」**

---

## 2. [General Intuition](https://www.generalintuition.ai/)（融资 / 通用 Agent 训练）

![General Intuition](/tmp/daily-screenshots/general-intuition.png)

🔗 链接：[官网](https://www.generalintuition.ai/) | [TechCrunch 深度报道](https://techcrunch.com/2026/06/25/general-intuitions-2-3b-bet-that-video-games-can-train-ai-agents-for-the-real-world/)

**融资信息**：**3.2 亿美元**融资，估值 **23 亿美元**。由 Medal（游戏剪辑分享平台）孵化。

**做什么的**：用数亿小时的游戏行为数据（包含玩家按键的 action label）训练通用 Agent 模型——同一个「大脑」可以在游戏世界中导航，也能驱动物理世界的四足机器人。

**为什么值得关注**：
- 核心洞察：**视频数据不够，action data（行为标签）才是让 AI 理解因果的关键**。竞争对手试图从视频推断行为，General Intuition 直接拥有 Medal 积累的数亿小时带 action label 的游戏数据。
- 在 TechCrunch 记者的实地体验中，仅用 8 分钟真实世界数据就完成了四足机器人的微调——这意味着 sim-to-real 的迁移效率极高。
- 世界模型不是产品，而是训练环境（内部称为「gym」）。最终产品是 Agent 模型本身。
- 对创业者的启发：**行为数据（action data）是下一个「数据金矿」。谁拥有独特的行为数据集，谁就能训练出与众不同的 Agent**。

**类比参考**：**「游戏版 DeepMind / 用 Fortnite 训练出来的 Physical Intelligence」**

---

## 3. [Unconventional AI](https://unconventional.ai/)（产品发布 / AI 芯片）

![Unconventional AI](/tmp/daily-screenshots/unconventional-ai.png)

🔗 链接：[官网](https://unconventional.ai/) | [TechCrunch 报道](https://techcrunch.com/2026/06/25/databricks-former-ai-chief-thinks-he-can-cut-ais-power-bill-by-1000x/)

**融资信息**：具体轮次未披露，团队不到 50 人。创始人 **Naveen Rao** 曾任 Databricks AI 主管、此前创办 Nervana Systems（被 Intel 收购）。

**做什么的**：基于振荡器（oscillator-based）的新计算架构，目标是把 AI 推理功耗降低 **1000 倍**。刚发布首个模型 **Un-0**——用软件模拟新架构跑图像生成，效果对标 Stable Diffusion / GPT Image 1。

**为什么值得关注**：
- 如果 claims 成立，这意味着 AI 推理的能源成本从 $1 降到 $0.001——**这是整个 AI 行业的能源瓶颈破解方案**。
- Naveen Rao 是 AI 芯片赛道的老兵：Nervana Systems 被Intel 以 $4 亿收购，他在 Databricks 管 AI 全局。他的再次创业本身就是一个强信号。
- 当前 Un-0 跑在软件模拟上，但芯片设计图即将发布。计划从芯片到推理栈全部自建。
- 对创业者的启发：**AI 的终极瓶颈不是算力，而是能源。谁能解决能效问题，谁就能定义下一代 AI 基础设施**。

**类比参考**：**「推理版 Cerebras / AI 能效的特斯拉——从芯片到服务全栈自建」**

---

## 4. [Netris](https://www.netris.ai/)（融资 / AI 云网络自动化）

![Netris](/tmp/daily-screenshots/netris.png)

🔗 链接：[官网](https://www.netris.ai/) | [TechCrunch 报道](https://techcrunch.com/2026/06/25/netris-raises-15m-series-a-from-a16z-to-help-ai-neoclouds-go-live-faster/)

**融资信息**：**1500 万美元 A 轮**，由 **a16z** 领投（合伙人 Guido Appenzeller 加入董事会）。**Nvidia** 两年前看到 demo 后主动推荐客户。

**做什么的**：AI neocloud 的网络自动化平台——软件跑在网络交换机上，自动化配置、部署和运维，帮助新兴 AI 云服务商将上线时间从数月缩短到数天。已部署在 **35+ GPU 集群**（约 100 万块 GPU），客户包括 Lightning AI、Foxconn、HPE、TensorWave 等。

**为什么值得关注**：
- **不用 AI 做 AI 基础设施**——创始人明确说：「AI 不是确定性的，配置数千台交换机不需要创造力，需要的是极致的持久和可重复」。这个判断对创业者非常有启发。
- Nvidia 主动背书说明这个方案解决了 GPU 部署的真实瓶颈——**有 GPU 但网络配不通，是 neocloud 最常见的死亡原因**。
- 厂商无关（vendor-agnostic），兼容 Nvidia 和 AMD 的服务器和网络设备。
- 对创业者的启发：**不是所有 AI 时代的基础设施都需要用 AI 来做。确定性算法在特定场景下比 AI 更可靠**。

**类比参考**：**「AI 云版 Cisco DNA Center / neocloud 的 Cloudflare」**

---

## 5. [Aseon Labs](https://aseonlabs.com/)（YC Spring 2026 / 机器人）

![Aseon Labs](/tmp/daily-screenshots/aseon-labs.png)

🔗 链接：[官网](https://aseonlabs.com/) | [TechCrunch 报道](https://techcrunch.com/2026/06/26/this-silicon-valley-startup-has-raised-10m-to-build-pitstops-to-clean-and-charge-robotaxis/)

**融资信息**：**1000 万美元种子轮**，由 **Crane Venture Partners** 领投。YC Spring 2026 批次。

**做什么的**：为 Robotaxi 打造「 robotic pit stops」——停车场大小的自动化舱体，分散在城市中自动检查、清洁和充电 Robotaxi。用 vision-language-action 模型识别问题（如后座融化巧克力不clean，直接送回中央 depot）。

**为什么值得关注**：
- 切入了一个 Robotaxi 行业最大的痛点：**deadhead miles（空驶里程）**——没有乘客的行驶里程，是 Robotaxi 公司无法盈利的核心原因。
- 创始团队来自 Pushme（电池更换网络，被 Tier Mobility 收购），深谙「硬件 + 地产 + 快速部署」的 playbook。舱体被设计为临时建筑，避免了漫长的审批流程。
- 虽未签约 Robotaxi 公司，但 CEO 说「所有人都想试」。
- 对创业者的启发：**当所有人都在做 Robotaxi 本身，做 Robotaxi 的「运营基础设施」可能更有商业价值。补充赛道的机会窗口往往被忽视**。

**类比参考**：**「Robotaxi 版换电站 / 自动驾驶的加油站网络」**

---

## 6. [design.md](https://github.com/google-labs-code/design.md)（开源 / Agent 标准化）

![design.md](/tmp/daily-screenshots/design-md.png)

🔗 链接：[GitHub](https://github.com/google-labs-code/design.md)

**融资信息**：Google Labs 出品，开源项目。GitHub **单日 2407 star**，当日趋势 #1。

**做什么的**：一个格式规范——用 DESIGN.md 文件向 Coding Agent 描述视觉设计系统。类似于 README.md 描述项目、CONTRIBUTING.md 描述贡献规则，DESIGN.md 让 AI 编码 Agent 拥有对设计系统的持久化、结构化理解。

**为什么值得关注**：
- **填补了 Coding Agent 生态的关键空白**：当前 AI 编码 Agent 可以写代码、写测试，但完全不懂设计——每次生成 UI 都需要人工调整。DESIGN.md 让 Agent 有了「设计品味」的参考框架。
- 单日 2400+ star 的爆发速度说明这个痛点极为普遍。
- 对创业者的启发：**Agent 时代的「约定优于配置」正在向设计领域延伸。每个垂直领域都可能需要类似的 Agent 可读标准文件**。

**类比参考**：**「UI 版 .cursorrules / Coding Agent 的设计系统即文档」**

---

## 7. [gstack](https://github.com/garrytan/gstack)（开源 / Agent 工具栈）

![gstack](/tmp/daily-screenshots/gstack.png)

🔗 链接：[GitHub](https://github.com/garrytan/gstack)

**融资信息**：Garry Tan 个人开源项目（MIT）。GitHub **单日 950 star**。

**做什么的**：Garry Tan（Y Combinator 总裁）的 Claude Code 精确配置——23 个工具，分别扮演 CEO、设计师、工程经理、发布经理、文档工程师和 QA 角色。一键安装，让 Claude Code 变成一个完整的「一人公司」团队。

**为什么值得关注**：
- **YC 总裁亲自开源自己的 Agent 工具栈**，本身就是一个巨大的信号。这说明顶级 AI 投资人认为 Agent 工作流标准化是当前最值得关注的方向。
- 23 个工具的角色分工设计极为精妙：不是简单的 prompt 模板，而是把组织管理方法论注入到 Agent 编排中。
- 对创业者的启发：**Agent 不是在替代「开发者」，而是在替代「团队」。设计 Agent 工作流时，应该从组织架构的角度思考，而不是从代码角度**。

**类比参考**：**「开源版 「一人公司」操作系统 / Claude Code 版 Virtual Team」**

---

## 8. [OpenMontage](https://github.com/calesthio/OpenMontage)（开源 / Agent 视频生产）

![OpenMontage](/tmp/daily-screenshots/openmontage.png)

🔗 链接：[GitHub](https://github.com/calesthio/OpenMontage)

**融资信息**：开源项目（协议待确认）。GitHub **单日 1754 star**，Python 趋势 #1。

**做什么的**：全球首个开源的 Agentic 视频制作系统——12 条流水线、52 个工具、500+ Agent 技能。把 AI Coding Assistant（Claude Code、Cursor 等）变成一个完整的视频制作工作站。

**为什么值得关注**：
- 和昨天日报中 iart.ai Motion Skills（50 个动画技能包）形成互补：Motion Skills 做的是创意技能包，OpenMontage 做的是完整的制作流水线。
- 500+ Agent 技能 + 12 条流水线的模块化设计，意味着视频制作的每一个环节（剪辑、特效、配乐、字幕、渲染）都有对应的 Agent 工具。
- 对创业者的启发：**Agent 技能正在从「代码/文档」扩展到「创意内容生产」。Agent 版 Adobe Premiere / Final Cut Pro 的开源实现正在出现**。

**类比参考**：**「Agent 版 Adobe Premiere / 开源的 Sora 工作站」**

---

## 9. [Agent-Reach](https://github.com/Panniantong/Agent-Reach)（开源 / Agent 数据获取）

![Agent-Reach](/tmp/daily-screenshots/agent-reach.png)

🔗 链接：[GitHub](https://github.com/Panniantong/Agent-Reach)

**融资信息**：开源项目（Python）。GitHub **单日 1194 star**。

**做什么的**：给 AI Agent 装上「眼睛」——一个 CLI 工具，让 Agent 能读取和搜索 Twitter、Reddit、YouTube、GitHub、Bilibili、小红书等全互联网内容。零 API 费用。

**为什么值得关注**：
- 解决了 Agent 生态的一个关键瓶颈：**Agent 够聪明但看不到外面的世界**。当前大多数 Agent 只能操作本地文件或调用特定 API，无法主动获取互联网的实时信息。
- 零 API 费用的设计降低了使用门槛——不依赖任何平台的付费 API，直接抓取公开数据。
- 对创业者的启发：**Agent 的「感知层」是被低估的创业方向。让 Agent 能看、能听、能搜索，可能比让 Agent 更聪明更有价值**。

**类比参考**：**「Agent 版 Tavily / 开源的 Perplexity 感知层」**

---

## 10. [page-agent（阿里巴巴）](https://github.com/alibaba/page-agent)（开源 / Web GUI Agent）

![page-agent](/tmp/daily-screenshots/page-agent.png)

🔗 链接：[GitHub](https://github.com/alibaba/page-agent)

**融资信息**：阿里巴巴出品，开源（TypeScript）。GitHub **单日 530 star**。

**做什么的**：JavaScript 页面内 GUI Agent——用自然语言控制网页界面。可以直接嵌入任何网页，让用户通过对话操作页面上的所有功能。

**为什么值得关注**：
- **Web GUI Agent 是 AI 应用层的关键基础设施**。之前 RPA（Robotic Process Automation）需要后端 API，page-agent 直接在浏览器中操作 UI。
- 阿里出品说明大厂也在重视这个方向——不是做通用 Agent，而是做 Agent 操作 Web 的底层能力。
- 对创业者的启发：**Web GUI Agent 是「AI 自动化」落地最快的场景之一。每个有大量 Web 操作的行业（电商运营、数据录入、客服）都是潜在市场**。

**类比参考**：**「开源版 UiPath Web 版 / 浏览器内嵌的 ChatGPT Operator」**

---

## 值得重点跟踪的 3 个信号

1. **Agent 测试与验证已成为独立赛道**：Patronus AI 的 $50M B 轮 + 15 倍收入增长证明，「让 Agent 可靠运行」不是辅助功能，而是刚需。**几乎所有前沿 AI 实验室都是它的客户——这意味着 Agent 可靠性是行业级的痛点**。

2. **AI 基础设施投资进入百亿时代**：General Intuition（$3.2 亿 / $23 亿估值）、Unconventional AI（新芯片架构）、Netris（$15M / a16z 领投）——从训练数据到芯片到网络，AI 基础设施的每一层都在吸收大额资金。**当模型层趋于同质化，基建层成为最确定的投资方向**。

3. **Agent 工具生态标准化加速**：design.md（为 Agent 定义设计标准）、gstack（YC 总裁的 Agent 工具栈）、page-agent（Web GUI 标准）、Agent-Reach（Agent 感知层）——Agent 生态正在从「每个项目自己搭」走向「标准化组件」。**2026 年下半年，Agent 工具链的标准化速度将决定哪些产品能快速规模化**。

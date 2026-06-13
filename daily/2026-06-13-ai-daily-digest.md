# 0613日报 | AI开始直接操作旧系统

## 今日洞察

今天最值得创业者注意的，不是又多了一个更强的通用模型，而是**一批新产品开始绕过“重做软件界面”这条老路，直接进入旧系统、旧流程和旧设备内部干活**：有人让 AI 登录 SAP 和 Oracle 处理制造后台，有人让 AI 直接调度实验室仪器，有人把工业分销、客户运营、医疗影像治理、组织流程梳理都做成可执行层。一个越来越清晰的信号是，下一波 AI 产品的价值，不只是“会回答”，而是**能否真正接管老系统之上的操作工作**。

---

## 1. [Ontora](https://ontora.com/)（融资 / 产品进展）

![Ontora](/tmp/daily-screenshots/ontora.png)

🔗 链接：[官网](https://ontora.com/) | [YC Launch](https://www.ycombinator.com/launches/QiD-ontora-the-discovery-layer-for-ai-transformation)

**融资信息**：公司披露已在正式启动融资前拿到 **70 万美元**，并已排上 **80+** 个 VC 沟通；同时已有 **5 家企业设计合作客户**、**150+ inbound demo**。

**做什么的**：用 AI agents 持续采访企业员工，自动抽取流程、决策规则、工具链和交接关系，生成可供企业自动化和 agent 使用的“活的组织上下文层”。

**为什么值得关注**：
- 它切的不是“再给员工一个聊天框”，而是 **AI 转型前最贵、最慢的 discovery 阶段**。
- 传统流程梳理往往要咨询公司做数月访谈，Ontora 把这一步压缩到几天，且上下文会持续更新，不会很快过时。
- 对创业者的启发是：企业 AI 项目很多不是输在模型，而是输在 **没人先把真实业务怎么运转搞清楚**。

**类比参考**：**“企业流程访谈版 Palantir / AI 转型版组织 discovery layer”**

---

## 2. [Lattice Health](https://www.latticehealthai.com/)（新产品 / 医疗合规）

![Lattice Health](/tmp/daily-screenshots/lattice-health.png)

🔗 链接：[官网](https://www.latticehealthai.com/) | [YC Launch](https://www.ycombinator.com/launches/Qid-lattice-health-monitoring-and-governance-for-deployed-medical-imaging-ai)

**融资信息**：获 **Y Combinator** 支持（Spring 2026），公开页面未披露独立融资金额。

**做什么的**：为医院已部署的医疗影像 AI 提供持续监控与治理层，追踪模型是否 drift、与放射科医生结论的一致性，以及不同患者亚群上的表现差异。

**为什么值得关注**：
- 医疗 AI 真正难的不是模型上线，而是 **上线后还能不能持续安全、合规地工作**。
- Lattice 采用只读接入，不直接影响临床决策，把自己定位成“监控与证据层”，更符合医院采购逻辑。
- 对创业者的启发是：高监管行业里的 AI 新机会，往往来自 **post-deployment governance**，而不是前端体验升级。

**类比参考**：**“医疗影像 AI 版 Datadog / Arize + 合规治理层”**

---

## 3. [Akkari](https://akkari.io/)（新产品 / 客户运营）

![Akkari](/tmp/daily-screenshots/akkari.png)

🔗 链接：[官网](https://akkari.io/) | [YC Launch](https://www.ycombinator.com/launches/Qhc-akkari-autonomous-customer-ops)

**融资信息**：获 **Y Combinator** 支持（Spring 2026），未见独立融资金额披露。

**做什么的**：把 Slack、邮件、会议、Discord、通话中的客户承诺、bug、需求、阻塞和扩容信号自动汇总，并推动后续动作落地，比如建工单、发更新、做挽留、触发扩容流程。

**为什么值得关注**：
- 很多创业团队输给对手，不是产品差，而是 **承诺没人跟、问题没人收口、客户信号分散在各处**。
- Akkari 切的是从首个销售电话到续费扩容的“customer ops 执行层”，比单点客服 bot 更接近收入结果。
- 对创业者的启发是：AI 在 B2B 里最容易形成价值的地方，常常不是回答问题，而是 **替团队把 follow-through 做完**。

**类比参考**：**“客户成功版 Linear + RevOps agent”**

---

## 4. [Hexa](https://www.hexaagents.com/)（新产品 / 工业分销）

![Hexa](/tmp/daily-screenshots/hexa.png)

🔗 链接：[官网](https://www.hexaagents.com/) | [YC Launch](https://www.ycombinator.com/launches/Qfd-hexa-autonomous-operations-for-industrial-distributors)

**融资信息**：获 **Y Combinator** 支持（Spring 2026），公开页面未披露独立融资金额。

**做什么的**：为工业分销商和制造商自动处理 sourcing、报价、订单录入、采购与对账，把原本在邮件、PDF、Excel、传真和 ERP 之间来回切换的流程做成 agent 工作流。

**为什么值得关注**：
- 这是非常典型的“老行业、高频、强 ROI、系统老旧”的切口，客户损失直接体现在 **报价慢导致丢单**。
- Hexa 不要求客户替换 ERP，而是直接嵌进现有系统里，把 reps 从键盘搬运工变成审核者。
- 对创业者的启发是：很多垂直 AI 的最佳 GTM，不是替换旧系统，而是 **先贴着旧系统把最重的人工作业接管掉**。

**类比参考**：**“工业分销版 ServiceNow + ERP 内嵌 agent”**

---

## 5. [Walter](https://www.ycombinator.com/companies/walter)（新产品 / 制造后台）

![Walter](/tmp/daily-screenshots/walter.png)

🔗 链接：[YC 公司页](https://www.ycombinator.com/companies/walter) | [YC Launch](https://www.ycombinator.com/launches/Qdh-walter-ai-employee-for-the-manufacturing-back-office)

**融资信息**：获 **Y Combinator** 支持（Spring 2026），公开页面未披露独立融资金额。

**做什么的**：Walter 不是新建一套系统，而是直接给 AI 一个登录账号，让它像新员工一样进入 SAP、Microsoft Dynamics、Oracle、Teams、Outlook 等现有软件，自动处理 PO 录入、供应商下单、价格错误检查等制造后台任务。

**为什么值得关注**：
- 它最强的产品观点是：**别再做集成了，直接让 AI 去操作现有软件**。
- 这大幅降低企业替换系统的阻力，也说明 agent-native 产品开始从 API-first 走向 **UI / workflow-first automation**。
- 对创业者的启发是：很多传统行业的软件真正问题不是功能缺失，而是 **仍然需要大量人坐在系统前重复点击**。

**类比参考**：**“制造业版 AI 员工 / 给 SAP 和 Oracle 的操作员 Agent”**

---

## 6. [Infera](https://www.infera.bio/)（新产品 / 科研基础设施）

![Infera](/tmp/daily-screenshots/infera.png)

🔗 链接：[官网](https://www.infera.bio/) | [YC Launch](https://www.ycombinator.com/launches/Qdt-infera-control-lab-instruments-with-natural-language)

**融资信息**：获 **Y Combinator** 支持（Spring 2026），公开页面未披露独立融资金额。

**做什么的**：研究人员用自然语言描述实验后，Infera 会把它转成可执行、可校验的 instrument-ready run，涵盖 protocol logic、仪器脚本、数据回传、分析与库存检查。

**为什么值得关注**：
- 它切中的不是“科学家写报告”这种浅层场景，而是 **实验仪器之间长期无法真正协作** 的系统性问题。
- Infera 把 SOP、仪器约束、库存状态、历史实验经验放进同一个上下文层，显著提高实验自动化可信度。
- 对创业者的启发是：在垂直高专业场景，AI 价值不在更会聊天，而在 **把意图翻译成真实世界里的可执行动作**。

**类比参考**：**“实验室版 Claude Code / 科学仪器操作系统”**

---

## 7. [Zenbu](https://tryzenbu.dev/)（新产品 / 开发工具）

![Zenbu](/tmp/daily-screenshots/zenbu.png)

🔗 链接：[官网](https://tryzenbu.dev/) | [YC Launch](https://www.ycombinator.com/launches/Qey-zenbu-the-extensible-ide-for-managing-coding-agents)

**融资信息**：获 **Y Combinator** 支持（Spring 2026），公开页面未披露独立融资金额。

**做什么的**：Zenbu 想做“管理 coding agents 的 IDE”，把多 agent 并行、结果审查、上下文切换、验证和插件扩展做成一套可定制界面。

**为什么值得关注**：
- 当团队开始同时跑多个 coding agents 后，新的问题已经不再是“能不能生成代码”，而是 **怎么管理 agent 之间的复杂度**。
- Zenbu 选择插件化路线，而不是强推单一工作流，说明“agent IDE”可能会像早年的开发环境一样，形成新的生态层。
- 对创业者的启发是：coding agent 赛道的下一步，不只是更强模型，而是 **围绕 agent 协作、审查和编排长出新的工作台**。

**类比参考**：**“Cursor / VS Code 的多 coding-agent orchestration 版本”**

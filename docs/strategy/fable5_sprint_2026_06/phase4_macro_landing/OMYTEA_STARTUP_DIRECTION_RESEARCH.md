# OMYTEA_STARTUP_DIRECTION_RESEARCH — 第一 wedge 方向研究

> 证据基础：本仓库 Phase 1–4 产出（local）+ 2026-06 三组定向 web 搜索（标注 [WEB]）。
> 本机 WMDB 既有研究未能读取（见 SOURCE_GAPS.md），结论中依赖它的部分标 [VERIFY-LOCAL]。
> 全部"willingness to pay"均为 hypothesis，无一已验证。

## 0. 来自 web research 的三个关键外部事实

1. **LLM observability/eval 是大且增长快的预算池，但拥挤**：市场约 $2.69B
   （2026），预计 2030 年 $9.26B；Gartner 预计 2028 年 50% 的 GenAI 部署
   含 observability 投入；已有 15+ 平台（Langfuse/ClickHouse、Maxim、
   Respan、Confident AI 等）。[WEB] **但它们做的是 tracing 和 eval-on-traces，
   没有发现任何一家做"预登记 + 时间维度 + proper-scoring 的校准收据"。**
2. **Metaculus 证明了 track record 机制有效，但只覆盖平台内问题**：
   per-user 校准曲线、proper scoring、按历史准确度加权——全部存在，
   但仅限在 Metaculus 上回答 Metaculus 的问题。你自己的预测流、
   你的 AI agent 的输出，不在任何人的审计范围内。[WEB]
3. **"forecast accuracy"在企业语境里是真实痛点但被销售预测工具占据**：
   销售/财务 forecasting 工具大量存在，87% 企业 miss 收入目标的叙事
   常见——这个池子里"准确性"话语已被 CRM/FP&A 工具垄断，新进入者
   没有结构性优势。[WEB]

**综合推论（hypothesis）**：审计层的空位真实存在——位置在"任意预测源的
跨源校准履历"，最有预算和紧迫感的预测源是 AI agents。

## 1. 八个候选方向评估

评估维度：target user / pain / 现有 workaround / WTP hypothesis /
buyer urgency / 需要的证据 / 合规摩擦 / Omytea edge / kill 条件。

### D1. AI-agent evaluation / claim audit infrastructure ⭐ 推荐第一 wedge
- **Target user**：把 LLM agent 输出当决策依据卖给客户的团队
  （agent 创业公司、AI 咨询交付方、企业内 AI 平台组）
- **Pain**：客户问"你的 agent 历史上靠谱吗"时只能拿 demo 和 eval 分数，
  没有第三方的、时间上不可伪造的履历
- **Workaround**：eval benchmark 分数（一次性、自报、可过拟合）、
  observability dashboard（看得到 trace，看不到"预测 vs 后果"）
- **WTP hypothesis**：中——eval/observability 预算池已存在且在涨 [WEB]，
  "履历证明"挂靠采购更容易；但"收据"是新品类，需教育
- **Buyer urgency**：中高——agent 进入采购流程的团队正在被问这个问题
- **Evidence needed**：3 个 agent 团队访谈确认"被客户问过历史可靠性"；
  1 个愿意试 concierge 版
- **合规摩擦**：低（不碰金融、不碰医疗时）
- **Omytea edge**：评分基础设施已建好（proper scoring + append-only +
  审计纪律文档化）；红海玩家做 traces，没人做 longitudinal receipts；
  中立第三方定位（不卖模型）
- **Kill 条件**：10 个访谈里没人被客户问过历史可靠性；或 eval 平台
  3 个月内推出同等功能且被接受

### D2. Prediction trust layer for public forecasters
- **Target**：公开发预测的个人（newsletter 作者、独立分析师、KOL）
- **Pain**：好的预测者无法证明自己，差的删帖洗记录
- **Workaround**：自建 spreadsheet、置顶截图、Metaculus（但仅平台内问题）[WEB]
- **WTP**：低-中——个人付费意愿弱，但头部分析师有"履历=溢价"动机
- **Urgency**：低（没有 forcing event）
- **Evidence needed**：3 个公开预测者愿意把履历交给第三方登记
- **合规**：低-中（金融类内容创作者会引入边缘问题）
- **Edge**：受众即分发（履历页本身是病毒物）
- **Kill**：头部创作者认为"被审计"是威胁而非资产（FOUNDER_MANUAL_ACTIONS
  第 7 节的 discovery 对话直接检验这一点）
- **定位**：**最佳 demo 面/分发面，不是最佳收入面**——作为 D1 的公开橱窗

### D3. Research integrity / forecasting receipts（科研预登记）
- **Target**：实验室、期刊、资助方
- **Pain**：preregistration 已是规范但工具碎片化（OSF 等已占位）
- **WTP**：低；**机构销售周期与 1-2 人团队不匹配**；OSF 是免费在位者
- **Kill 条件即现状**：在位者免费 + 买家是机构。**排除（本阶段）**

### D4. Institutional decision audit（机构决策审计）
- **Target**：基金/企业战略部门的决策复盘
- **Pain**：真实（决策无 paper trail），但买家是大企业，销售周期 6-12 月
- **WTP**：高（如果买）；**Urgency：低**；需要 references 才能进门
- **判定**：是 D1 成功后的第二幕，不是第一幕。**推迟**

### D5. Risk/compliance decision records
- **Target**：受监管机构的模型风险/合规团队
- **Pain**：真实且有预算（model risk management 是合规要求）
- **摩擦**：极高——卖进银行需要 SOC2、采购流程、领域信誉，全是我们没有的
- **判定**：**排除（本阶段）**，但 schema 设计时保持审计级严谨为将来留门

### D6. Golf / sports scored-outcome wedge
- **状态**：受 GOLF_VERTICAL_DECISION_MEMO 管辖，6/13 落锤
- **在新格局下的角色变化**：从"主线候选"降为"non-owner rows 供给实验 +
  消费级好奇心验证"。即使 GO 也是定位 B/C（数据集/discovery），
  不与 D1 争资源
- **Kill**：已定义于 memo

### D7. Finance calibration as credibility artifact（非交易产品）
- **角色已定**（PHASE4_PIVOT_DECISION）：不是方向，是资产。
  Omytea 自己的公开校准履历 = 最强的销售道具（"我们先审计自己"）
- 不参与排名

### D8. Technical founder / lab notebook for forecasts
- **Target**：爱量化自我的工程师/founder（写下预测→自动追踪→校准曲线）
- **Pain**：弱痛点、强身份认同（"我是校准的人"）
- **WTP**：低（个人工具定价天花板）
- **Edge**：现有 personal console 几乎就是它 [VERIFY-LOCAL]
- **判定**：**D1 的免费入口/PLG 底座候选**，不是独立方向。
  personal console 重构应朝这个形态走（见 PRD）

## 2. 排名与推荐

| 排名 | 方向 | 角色 |
|---|---|---|
| 1 | **D1 AI-agent claim audit / calibration receipts** | 第一 wedge（收入假设所在） |
| 2 | D2 public forecaster trust layer | 公开橱窗 + 分发（与 D1 共享全部基础设施） |
| 3 | D8 forecast lab notebook | 免费产品面 / console 重构的目标形态 |
| 4 | D6 golf | 按 memo 独立判定，资源上限 8h/周 |
| 5 | D4 institutional audit | 第二幕，写进叙事不写进路线图 |
| — | D7 finance artifact | 资产非方向 |
| 排除 | D3 research integrity、D5 compliance | 在位者/销售周期不匹配 |

**推荐第一 wedge：D1，AI-agent 输出的校准收据（calibration receipts for
AI agents）。**

一句话版本：*"你的 agent 说了什么、什么时候说的、后来对没对——
第三方收据，不可改，可评分。"*

**为什么是 D1 而不是 D2 先行**：预算（eval 池已存在 [WEB]）、紧迫感
（采购质询是 forcing event）、合规低摩擦、且 Omytea 的全部已有资产
（评分代码、审计纪律、claim 分级制度）在 D1 语境里都是直接卖点。
D2 免费做、公开做，作为 D1 的可见性引擎。

**这个推荐的最大不确定性（诚实声明）**：D1 的 pain 是从 [WEB] 市场结构
+ 推理得出的 hypothesis，还没有任何一个真实 agent 团队亲口确认。
**接下来 14 天最重要的研究动作不是更多桌面分析，是 5 个 D1 目标用户访谈**
（脚本见 FABLE5_NEXT_PROMPTS FP-5）。

## Sources

- [Top 7 LLM Observability Tools in 2026 - Confident AI](https://www.confident-ai.com/knowledge-base/compare/top-7-llm-observability-tools)
- [15 AI Agent Observability Platforms in 2026 | Latitude](https://latitude.so/blog/15-ai-agent-observability-platforms-2026-agentic-complexity)
- [Gartner: Explainable AI Will Drive LLM Observability Investments](https://www.demandgenreport.com/industry-news/news-brief/gartner-explainable-ai-will-drive-llm-observability-investments/52532/)
- [Top 5 LLM and Agent Observability Tools in 2026 | MLflow](https://mlflow.org/top-5-agent-observability-tools/)
- [Metaculus track record](https://www.metaculus.com/questions/track-record/)
- [A Primer on the Metaculus Scoring Rule](https://www.metaculus.com/notebooks/22486/a-primer-on-the-metaculus-scoring-rule/)
- [Sales Forecasting Accuracy Guide](https://forecastio.ai/blog/sales-forecasting-accuracy-and-analysis)

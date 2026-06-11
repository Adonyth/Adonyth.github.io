# Omytea × Fable 5 战略会话完整总结
## 2026-06-10 → 06-11 ｜ 全部任务、产出、研究成果与待决事项

> 用途：完整信息载体。可转发给任何新会话/新设备/合伙人，
> 读完即可接续全部上下文。
> 所有产出已 commit 至 GitHub：`Adonyth/Adonyth.github.io`
> 分支 `claude/fable5-strategy-sprint-2026-s2oy2b`，
> Draft PR：https://github.com/Adonyth/Adonyth.github.io/pull/1

---

# 一、会话总览

| 阶段 | 任务 | 产出位置 |
|---|---|---|
| Phase 1 | 12 天 sprint 执行系统（8 文档） | docs/strategy/fable5_sprint_2026_06/ |
| Phase 2 | 验收审计 + 7 天行动队列 + 任务包 | 同上（5 文件） |
| Phase 3 | Finance calibration ledger 最小闭环（代码） | ledger/（11/11 测试通过） |
| Phase 4a | 首条真实记录预登记审计 | PHASE4_FIRST_REAL_LEDGER_AUDIT.md |
| Phase 4b | 宏观落地：方向研究/PRD/UI 重构/14 天队列（13 文件） | phase4_macro_landing/ |
| Phase 5 | Master plan 深度审计（先推断版后原文版 v2） | master_plan_deep_audit_2026_06/ |
| 深研 R1 | 文明尺度地基（5 路调研 ~80 claims） | OMYTEA_DEEP_RESEARCH_2026-06.md |
| 深研 R2 | 逐节压力测试（5 路调研 ~85 claims） | OMYTEA_DEEP_RESEARCH_ROUND2.md |

**关键环境事实**：会话运行于云端容器，本机
/Users/chenjiaxuan/Downloads/WMDB 不可达；除 founder 上传的
master plan 原文外，其余本机文件（PROJECT_STATE、console 代码等）
均未读取——相关结论标 [VERIFY-LOCAL]/[INFERRED]，附本机核验协议。
未读取任何敏感文件（legal/、.env、credentials 等）。

**身份更正（2026-06-11 founder 口述）**：已毕业，OPT 阶段，
可实际运营。master plan §2.8 的 F-1 前提需重审；具体工作授权
边界列入 DSO/attorney 问题清单（不构成移民建议）。

---

# 二、核心论题演化（本会话最重要的思想线）

1. **起点（founder 给定）**："AI 预测泛滥后，验证/校准/审计成为
   稀缺层；我们不声称预测更准，做可信记录/校准/审计层。"
2. **Master plan 原文读取后发现"双魂问题"**：plan §1 = 造世界模型
   的选手（ρ 信念态 → GUWM）；plan §2.7.1（2026-06-02 锁定）=
   "预测不稀缺，证明稀缺，做敢被评分的预测者"；sprint 主线 =
   不下场的裁判。三种身份并存。
3. **合题（推荐 ratify）**：**"亮收据的选手 + 开源记分协议"**——
   Omytea 下场预测（世界模型引擎），记分层开源给所有人，信任来源
   从"机构中立"换成"开源可复算"。统一句：
   **"我们不声称更准——我们声称被评分，且你可以复算。"**
4. **深研第一轮把论题钉进历史**：信任基础设施制度化时滞指数压缩
   （记账 ~500 年 → 评审 ~308 年 → 评级 66 年 → 临床预注册 5–7 年）；
   AI 预测的"预注册时刻"被三个强制函数推向 ~2027（保险定价已开始、
   采购合规 2027、污染危机 2027–28）；**强制到来时，成为基础设施的
   是当时已存在的那个 registry**（ClinicalTrials.gov 先例）。
   AI 预测领域今天没有那个 registry——这是 Omytea 的位置和截止日期。
5. **为什么 Tetlock 没做成而现在能成**：超预测科学完备 75 年、
   被验证 15 年，缺的是责任框架。AI 责任险（Armilla $25M、AIUC）
   第一次把可验证预测记录变成成本项——卖美德没人买，卖保费折扣
   和采购通行证有人买。
6. **内部北极星（升级版 N5）**："做 AI 预测时代的 ClinicalTrials.gov
   + 天气预报式校准纪律；GUWM 是这条被收据铺出来的路的远方。"
   对外第一句（N2'）："Omytea 是第一个敢被评分的世界模型。"

---

# 三、Master Plan 审计判决汇总

## 漏洞（P0）
- **V1' 双魂问题**：见上文合题（待 founder ratify）。
- **V2 计划递归病**：WORK_PLAN 迭代 418 版 vs 外部证据 0
  （0 访谈、0 non-owner 数据）。解药 = 证据棘轮：plan 修订必须
  引用新外部事实；Agent Rule 10 改为"不确定就跑最便宜的外部测试"。
- **V3 证据全自产**：plan §14.5 自己的 non-owner gate 无一通过。
  唯一解药 = 访谈 + 第一个外部源接入。
- **N2 规模-产能倒置**：§2.8 承认单人约束，§9–14 却是 50 人议程。
  解药 = Tier-0 脊柱：活跃轨道 ≤2，其余 DORMANT（零对齐成本）。

## 深研第二轮的 §-级判决
- **§7 LLM-as-compiler：验证通过带时限**（2025–27 成立 75%；
  无约束 LLM 在 Spider 2.0 仅 10.1%，结构化约束是可靠性必要条件；
  2030 后受 Bitter Lesson/RLM 威胁，写明重审触发器）。
- **§9 World Console：大众消费形态被证伪**（PredictionBook 关停、
  Fatebook $1.1M 仅 5k 活跃;有效形态只有锦标赛/被动采集/B2B2C；
  个人 SOM 5–20 万认真预测者）。
- **§10 可移植护城河：否决**（全部非常规底座原型期、无概率 IR、
  GPU 够用到 2030、Gartner 共识 late 2020s；降级为 watch-and-wait
  + 2027 Q3 gate，可证伪判据当前 0/6）。
- **§12 学术捕获：强化具名**（资助方与金额见下文"资金路径"）。
- **量子线安放**：HQMM 文献在 ML 界休眠（零交叉引用），实用路径
  是经典 conformal+CRPS;ρ-formalism 归理论论文轨道——plan 的
  "formalism 非性能声明"获文献背书。

## Amendment 草稿（A–L，待 ratify，全文在 MASTER_PLAN_UPGRADE_PROPOSAL.md）
A 身份语序（收据第一句、quantum 降第二句、双魂裁定）｜B 对外词表
（仅 Omytea/world model/receipts;内部代号禁外用）｜C Tier-0 脊柱
（活跃 ≤2：T-A substrate 收据化、T-B 访谈线;SpaceWorld/device 谱/
蒸馏/专利 DORMANT）｜D 证据棘轮 + Rule 10 修订｜E 措辞修正
（uncontested→unoccupied;proven→evidenced;删 ChatGPT 类比）｜
F 价值捕获决断排程（10 访谈后 14 天内）｜G OPT 身份更新｜
H §10 降级｜I §9 三形态｜J §7 时限｜K 协议安全五件套｜
L 资助分发排程。

---

# 四、已交付的可运行资产

## ledger/（纯 stdlib、零联网、零凭证，11/11 测试通过）
- make_forecast.py（B0-flat + B1-ewma 分位数;本地 CSV 或 dry-run）
- score_day.py（pinball-CRPS、PIT、in90/in50;手算用例 0.19 精确匹配）
- validate_ledger.py（schema 白名单 + 券商字段黑名单 + 单调性）
- 运行：`python3 -m unittest discover ledger/tests -v`
- **状态如实**：工具链可运行 ≠ 已运行;真实预登记记录 0 行。
- **首日前必修 R1–R3**：预登记=push 而非 commit（commit 可伪造）;
  resolution 规则先钉死（节假日顺延、EURUSD 收盘定义）;
  late 字段改为对照 13:30 UTC cutoff 计算。

## 收据协议 v1 安全规格（防博弈五件套）
1. append-only 账本+外部锚定｜2. hash-lock 预提交（RFC3161 v1，
OpenTimestamps v2）｜3. 身份成本（防"注册千号删输家"）｜
4. baseline-relative 计分+题目权重（防挑简单题）｜5. 限速+holdout。
攻击先例：ClinicalTrials.gov 62% outcome-switching、Chatbot Arena
被 Meta 27 个私测变体刷榜、UMA oracle 被操纵 $7M、commit stomping。
**对外措辞规范："make gaming detectable"，禁说 tamper-proof。**

---

# 五、研究成果精华（两轮 10 路，~165 claims，全部有来源）

## 历史规律（R1）
- 制度化时滞压缩：1299 记账→500 年｜1665 评审→308 年｜
  1909 评级→66 年｜2000 临床预注册→5–7 年（ICMJE 2005/FDAAA 2007）。
- 腐蚀律：issuer-pays 毁评级（2008:$869B AAA→83% 降级→$864M 和解）;
  咨询费毁审计（Enron:审计 $25M vs 咨询 $27M）;无偿评审长期供给不足。
- 价值流向：发明者不获利（Pacioli/Crockford/Gruber）;价值归强制
  时刻在场的执业层（ICAEW 反向俘获 1900 公司法）。

## 预测科学（R1）
- 校准科学 75 年前完备（Brier 1950→Savage 1971）;天气预报是唯一
  制度化校准领域（即时可验证+单一主管+强制）。
- 超预测验证 15 年（IARPA ACE 胜 35–72%、超密级分析员 30%+）
  仍停留咨询利基——缺责任框架。
- Kalshi ~$50B 年化+Polymarket 合计 97.5% 市场，**双双不发布校准
  统计**——预测市场爆发恰恰没填校准空白。

## 世界模型评测空白（R1，对 Omytea 最关键）
- **[96% 置信] 没有任何主流世界模型（V-JEPA2/Genie 3/Cosmos）被以
  校准概率方式评分于真实未来事件**;视觉指标与下游任务脱节已被量化。
- 最接近占位者只覆盖 LLM 离散事件：ForecastBench（超预测者 Brier
  0.081 vs GPT-4.5 0.101，预计 2026 底持平）、Metaculus FutureEval。
- **"校准纵向世界模型评分"（time-decay 曲线+coverage）是小团队
  2–3 人年可拥有的空白**——这就是 WM-Receipts benchmark 提案
  （本会话唯一新增工作项，放入 T-A）。

## 强制函数（R1）
- 保险（已开始）：Armilla $25M（Lloyd's）、AIUC $50M 保额;
  金融监管已按 books-and-records 追责缺失 AI 审计轨迹。
- 采购：EU AI Act GPAI 2025-08 生效、高风险 2026-08;Colorado
  2027-01;美 2025-12 行政令。
- 污染：清洁集掉 13–16 分;"污染是默认假设"成共识。
- 推断汇合点 ~2027 Q3（研究员自报 82–88%，应打折）。

## 资金路径（R2，可立即行动）
- **首选：Coefficient Giving "AI for Forecasting and Sound
  Reasoning" RFP**（$8–10M 池、单笔 $100K–$1M、8–12 周）。
- 并行：EA Funds LTFF（$50–150K、4–6 周）;NumFOCUS（$10K+托管）。
- 先例：OpenPhil 已给 FRI 同谱系 $1.65M+（含 ForecastBench $100K）。
- 12 个月现实栈：$150–350K。
- **紧急**：arXiv 2026-01-21 收紧 endorsement——需提前锁定 endorser
  （cofounder PhD 网络）。

## 分发剧本（R2）
- LMArena：2 人学术项目→23 个月→$1.7B。
- benchmark 成为引用标准的 12–36 月路径：月 2–4 投 NeurIPS D&B
  （25.3% 接收率）→月 4–6 上自动化 leaderboard 拉 3–5 家模型厂→
  月 12 出现于 50+ 论文。

## 消费产品证据（R2）
- 死亡名单：PredictionBook 2024 关停;Fatebook $1.1M 仅 ~5k 活跃;
  80% 用户 30 天流失。根因：个人决策反馈回路 6–18 个月。
- 活路：锦标赛（Metaculus×Bridgewater 1.7 万人）、被动采集
  （Oura 200 万付费/$110M ARR）、B2B2C。
- $3B 占星市场是娱乐——§2.9.2 禁令是先见，不可碰。

---

# 六、既有死线与行动状态（截至 2026-06-11）

| 事项 | 死线 | 状态 |
|---|---|---|
| V10/V2 gate 填槽冻结 | 6/12（过期 T2 自动 FAIL-budget 关闭） | 待 founder（本机摘录+定阈值） |
| Golf go/no-go 签字 | 6/13（证据不足默认 FAIL） | 待 G1–G3 证据+签字 |
| attorney/DSO/CPA 三邮件 | 6/17（逾期冻结一切对外发布） | 清单已备好,待发出 |
| Ledger 首条真实预登记 | 越早越好（日历价值每天流失） | R1–R3 修复后执行 |
| 5+5 个 D1/买家访谈 | 30 天内 10 个（plan §14.5 自己的 gate） | 消息模板已备,待发出 |
| Amendment A–L ratify | 建议本周 | 待 founder 决断 |
| Coefficient Giving 申请 | 30 天内启动 | 材料清单已列 |

**访谈脚本新增两问**（强制函数验证）："客户/保险/采购有没有要求过
你们 AI 系统的历史可靠性证据？那次对话发生了什么？"

---

# 七、仓库文件全索引

```
docs/strategy/
├── fable5_sprint_2026_06/          Phase 1–4a（21 个文件）
│   ├── 00_README_SOURCE_STATUS.md  源文件状态与 VERIFY-LOCAL 协议
│   ├── FABLE5_MASTER_PLAN.md       12 天计划（D1-7 已被队列取代）
│   ├── PUBLIC_CLAIMS_MATRIX.md     L0–L5 分级+禁止线（持续有效）
│   ├── OMYTEA_EXTERNAL_STORY_PACK.md 5 版本叙事+15 尖锐问答
│   ├── V10_V2_RESEARCH_GATE_PLAN.md  gate 外壳（5 槽位待填）
│   ├── FINANCE_CALIBRATION_LEDGER_PROTOCOL.md 协议 v1.0
│   ├── GOLF_VERTICAL_DECISION_MEMO.md 6/13 落锤
│   ├── CIVILIZATION_TECH_FRAMEWORK_PRODUCTIZATION.md 骨架+本机 prompt
│   ├── AGENT_OPERATING_MANUAL.md   P1–P7 prompt 模板库
│   ├── PHASE2_ACCEPTANCE_AUDIT.md  诚实自我验收
│   ├── NEXT_7_DAYS_ACTION_QUEUE.md（部分被 14 天队列取代）
│   ├── TODAY_TOP3.md / CODEX_TASKS_READY.md / FOUNDER_MANUAL_ACTIONS.md
│   ├── PHASE3_EXECUTION_LOG.md / FINANCE_LEDGER_FIRST_RUN_REPORT.md
│   ├── PHASE4_FIRST_REAL_LEDGER_AUDIT.md（机器审计 PASS WITH FIXES）
│   └── phase4_macro_landing/       13 个文件
│       ├── PHASE4_PIVOT_DECISION.md / OMYTEA_STARTUP_DIRECTION_RESEARCH.md
│       ├── OMYTEA_LANDING_MASTER_PLAN.md（30/60/90 天）
│       ├── PRODUCT_REQUIREMENTS_DOC.md（Omytea Receipts MVP）
│       ├── UI_UX_AUDIT.md / UI_REDESIGN_SPEC.md / DESIGN_SYSTEM.md
│       ├── CURSOR_UI_REFACTOR_TASKS.md（CT-0..11）
│       ├── CODEX_IMPLEMENTATION_TASKS.md（CX-1..8）
│       ├── NEXT_14_DAYS_MACRO_ACTION_QUEUE.md（6/11–6/24）
│       ├── FABLE5_NEXT_PROMPTS.md（FP-1..12）
│       └── SOURCE_GAPS.md / WEB_RESEARCH_BACKLOG.md
└── master_plan_deep_audit_2026_06/ Phase 5 + 深研（12 个文件）
    ├── AUDIT_VERIFICATION_2026-06-10.md（推断版逐条核验）
    ├── MASTER_PLAN_INTERPRETATION.md v2（七版本解释）
    ├── MASTER_PLAN_VULNERABILITY_AUDIT.md v2（P0–P2 漏洞）
    ├── MASTER_PLAN_MISSING_OPPORTUNITIES.md（O1 标准/O2 benchmark/O3 文明收据）
    ├── MASTER_PLAN_UPGRADE_PROPOSAL.md（Amendment A–G+H–L 草稿）
    ├── ULTIMATE_GOAL_REWRITE.md v2（双层北极星 N2'/N5）
    ├── WORKSTREAM_ALIGNMENT_MATRIX.md v2（全工作流处置）
    ├── MASTER_PLAN_GUARDRAILS.md（10 问+反递归+配额）
    ├── BETTER_THAN_CURRENT_PLAN.md / MASTER_PLAN_V2_ROADMAP.md
    ├── FABLE5_MASTER_PLAN_PROMPTS.md（MP-1..10）
    ├── OMYTEA_DEEP_RESEARCH_2026-06.md（R1：文明地基,~80 claims）
    └── OMYTEA_DEEP_RESEARCH_ROUND2.md（R2：逐节压测,~85 claims）
ledger/                              可运行代码（见第四节）
```

---

# 八、给下一个会话的接续指令（复制即用）

```
背景：读取 docs/strategy/SESSION_FULL_SUMMARY_2026-06-11.md
获得全部上下文。当前待办按第六节死线表执行。
核心纪律：claims matrix 禁止线、证据棘轮（无新外部事实不修 plan）、
Tier-0（活跃轨道 ≤2）、隐私边界（不读 legal//.env/credentials）。
主线一句话："我们不声称更准——我们声称被评分，且你可以复算。"
下一个边际价值最高的动作不是更多研究，是第一条 non-owner 收据。
```

---

*本总结生成于云端会话（分支 claude/fable5-strategy-sprint-2026-s2oy2b，
commit 378fb33 之后）。所有研究结论的完整来源列表见两份深研报告文末。
Calibration research context. Not investment / legal / immigration advice.*

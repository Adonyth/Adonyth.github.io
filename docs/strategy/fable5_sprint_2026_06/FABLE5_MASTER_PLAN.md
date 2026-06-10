# FABLE5_MASTER_PLAN — 2026-06-10 → 2026-06-22 执行总计划

> 源文件状态：本计划基于任务描述上下文构建，未读取本机 WMDB 文件。
> 依赖本机文件确认的条目标 `[VERIFY-LOCAL]`。详见 `00_README_SOURCE_STATUS.md`。

## 0. Sprint 主线（一句话）

**在 AI 预测泛滥的时代，验证 / 校准 / 审计是稀缺层。这 12 天把这条主线从
"文档里的论点"变成：一套对外可说的叙事、一本跑起来的校准账本、
一组有 stop rules 的研究 gate、一个 go/no-go 已定的 vertical 决策、
一套可复用的 agent 操作系统。**

## 1. 五条并行轨道

| 轨道 | 交付物 | 性质 |
|---|---|---|
| T1 叙事与 claim discipline | PUBLIC_CLAIMS_MATRIX + EXTERNAL_STORY_PACK 定稿、口头演练 | 写作/审校，Fable 5 强项 |
| T2 研究 gate（V10/V2） | gate 实验跑完或 kill，结论写入 ledger | 实验执行给 Cursor/Codex，判读给 Fable 5 |
| T3 Finance calibration ledger | 连续 ≥10 天的预登记每日分布预测 + 评分 | 每日 30–45 分钟固定仪式 |
| T4 Golf vertical 决策 | go/no-go 落锤 + （若 go）第一批 non-owner resolved rows | 数据探针 + 决策 |
| T5 框架与系统资产 | 文明科技框架文章/worksheet + AGENT_OPERATING_MANUAL | 写作 + 流程固化 |

**轨道优先级（额度紧张时从下往上砍）：T3 > T1 > T4 > T2 > T5。**
理由：T3 是唯一有"日历时间不可压缩"属性的轨道（错过一天就少一行数据）；
T1 是 6 月会议刚需 `[VERIFY-LOCAL: 是否有既定会议日期]`；T5 最可推迟。

## 2. 工具分工总原则

| 任务类型 | 给谁 | 理由 |
|---|---|---|
| 长上下文综合、跨文档一致性审查、claim 分级、叙事写作、决策备忘、对抗性 Q&A 演练 | **Fable 5** | 长程推理 + 长上下文是其相对优势 |
| 明确 spec 的代码实现（ledger 脚本、scoring 函数、数据抓取） | **Codex** | 便宜、快、spec 明确时质量足够 |
| 交互式改代码、小步调试、IDE 内重构 | **Cursor** | 人在环路的快速迭代 |
| 浏览器自动化 / 重复性操作流 | **OpenClaw** | `[VERIFY-LOCAL: OpenClaw 当前可用能力]` |
| 批量算力 / 长时间跑实验 | **scnet** | `[VERIFY-LOCAL: scnet 配额与环境]` |
| 隐私敏感的本地处理（涉及个人信息的文档整理）、离线草稿 | **Ollama 本地模型** | 数据不出本机 |
| 3D/空间类内容 | **OpenSpace** | `[VERIFY-LOCAL: OpenSpace 在你工作流中的实际角色]` |

**反模式：不要用 Fable 5 做** 模板化代码补全、简单格式转换、可以一次写清 spec 的纯执行任务、
需要反复试错的环境调试（先用 Cursor/Codex 把环境跑通，再让 Fable 5 做判读）。

## 3. 每日固定仪式（雷打不动，约 60 分钟）

- **08:30–09:00 Ledger 仪式**：按 `FINANCE_CALIBRATION_LEDGER_PROTOCOL.md`
  生成当日分布预测，commit（预登记），评分昨日预测。
- **21:30–22:00 日终复盘**：用 AGENT_OPERATING_MANUAL 里的复盘模板，
  让 Fable 5 过一遍：今日 done criteria 达成了吗？明天第一件事是什么？
  有没有 claim 越界（说了 matrix 里禁止的话）？

## 4. 每日计划

> 格式：上午（深度工作）/ 下午（执行与委派）/ 晚上（轻任务与复盘）。
> 每天的 ledger 仪式和日终复盘不再重复写。

### D1 · 6/10（周三）— 启动与预登记
- **上午（Fable 5）**：核对本 sprint 包全部 `[VERIFY-LOCAL]` 标记（对照本机文件，≤60 分钟）；
  定稿 `FINANCE_CALIBRATION_LEDGER_PROTOCOL.md` 并完成 ledger repo 初始化 + 第一次预登记 commit。
- **下午（Codex）**：按 protocol 附录 spec 实现 ledger 的 forecast 模板生成脚本 + CRPS/PIT 评分脚本；
  （Cursor）跑通本地数据拉取（收盘价等公开数据）。
- **晚上（Fable 5，轻）**：通读 `PUBLIC_CLAIMS_MATRIX.md`，逐条标注同意/修改。
- **Done criteria**：ledger day-1 预测已 commit（带时间戳）；评分脚本对合成数据跑通；
  claims matrix 进入"待你批准"状态。

### D2 · 6/11（周四）— Claim discipline 定稿
- **上午（Fable 5）**：根据你 D1 晚的批注定稿 claims matrix；
  用 matrix 逐句审查 `OMYTEA_EXTERNAL_STORY_PACK.md`，确保没有越级 claim。
- **下午（Fable 5）**：对抗性演练——让 Fable 5 扮演最不客气的技术投资人，
  用 story pack 的 15 个尖锐问题攻击你，你口头作答，Fable 5 评分并修订答案。
- **晚上**：把 30 秒版本和 2 分钟版本背到脱稿。
- **Done criteria**：matrix 和 story pack 定稿；你能脱稿讲 30 秒版本且不含任何 L3+ 越级 claim。

### D3 · 6/12（周五）— V10/V2 gate 启动
- **上午（Fable 5）**：对照本机 `FOUNDING_SPINE_V10_PROPOSED_NEXT.md` 和
  `QUANTUM_CORE_GATE_V2_PROPOSED_NEXT.md` 核对 `V10_V2_RESEARCH_GATE_PLAN.md` 的
  pass/fail labels 与 kill criteria `[VERIFY-LOCAL]`，**冻结**（之后不许改阈值）。
- **下午（Cursor/Codex）**：搭建 gate 实验脚手架（数据 split、baseline、评测 harness）；
  （scnet）若需要算力，提交首批 run。
- **晚上**：golf 数据源初步排查（公开数据有哪些字段、更新频率）。
- **Done criteria**：gate plan 冻结并 commit；实验脚手架能跑 dummy run。

### D4 · 6/13（周六）— Golf 决策日
- **上午（Fable 5）**：基于 `GOLF_VERTICAL_DECISION_MEMO.md` 的 go/no-go criteria
  和 D3 晚的数据源排查结果，做出落锤决策。
- **下午**：若 GO → （Codex）实现 non-owner rows 抓取/录入的最小管线；
  若 NO-GO → 把腾出的时间划给 T2/T5。
- **晚上**：文明科技框架——在本机让 Fable 5 读三个源文件，产出第一版文章大纲修订。
- **Done criteria**：golf 决策写入 memo 的 DECISION 区并 commit（含理由和复议条件）。

### D5 · 6/14（周日）— 框架写作日
- **上午（Fable 5）**：文明科技框架中文文章完整初稿（不是大纲）。
- **下午（Fable 5）**：worksheet + startup direction scoring template 可用版。
- **晚上（轻）**：V10/V2 首批 run 结果粗看（只记录，不调参——no-tune rule）。
- **Done criteria**：中文初稿 ≥ 可发给一位朋友试读的完成度；worksheet 你自己能填。

### D6 · 6/15（周一）— 中期检查点 ①
- **上午（Fable 5）**：中期审计——5 条轨道各自状态、ledger 连续性检查、
  gate 实验是否触发 kill criteria、额度消耗 vs 预算。
- **下午**：处理审计发现的最大瓶颈（机动时段）。
- **晚上**：AGENT_OPERATING_MANUAL 第一次实测修订（按前 6 天实际用法改）。
- **Done criteria**：中期审计 memo 写入本目录（`CHECKPOINT_D6.md`）；明确后半程砍什么保什么。

### D7 · 6/16（周二）— 研究 gate 推进
- **上午（Fable 5）**：V10/V2 中期结果判读——严格按冻结的 labels 判 pass/fail，
  写"当前证据允许说什么/不允许说什么"。
- **下午（Cursor/Codex/scnet）**：补齐 gate 计划要求的剩余 runs。
- **晚上**：英文版文明科技文章初稿（Fable 5 从中文版改写，不是直译）。
- **Done criteria**：gate 中期判读 commit；英文初稿存在。

### D8 · 6/17（周三）— Golf 执行 / 替代轨道
- **上午**：若 golf GO → 第一批 resolved rows 入库并评分；watch ledger MVP 范围冻结。
  若 NO-GO → 文明科技框架 10 个案例写作。
- **下午（Codex）**：执行向任务（管线、模板、自动化）。
- **晚上**：story pack 第二次口头演练（对真人最好；否则 Fable 5 模拟）。
- **Done criteria**：golf 轨道有可数的 rows（GO 线）或案例 ≥5 个（NO-GO 线）。

### D9 · 6/18（周四）— 系统资产日
- **上午（Fable 5）**：AGENT_OPERATING_MANUAL 定稿（含实测过的模板）；
  把本 sprint 用过的所有有效 prompt 沉淀进模板库。
- **下午**：ledger 第 9 天 + 首次 7 日滚动评分报告（PIT 直方图、coverage 表）。
- **晚上**：professional review questions 清单整理（DSO/attorney/CPA 各一份，
  从 ledger protocol 附录提取，准备发出）。
- **Done criteria**：manual 定稿；7 日评分报告生成；三份 review 问题清单可发送。

### D10 · 6/19（周五）— 收束日 ①
- **上午（Fable 5）**：V10/V2 最终判读 + 写 gate 结论（pass → 下一最小步骤；
  fail/kill → 正式停止声明，写明"不允许再投入的条件"）。
- **下午**：文明科技框架全部产物定稿（两篇文章、worksheet、scoring template、案例）。
- **晚上（轻）**：清理本 sprint 目录，所有文档去掉已核实的 `[VERIFY-LOCAL]` 标记。
- **Done criteria**：gate 有正式结论；T5 全部产物定稿。

### D11 · 6/20（周六）— 收束日 ②
- **上午（Fable 5）**：对外资产终审——用 claims matrix 最后扫一遍所有对外材料
  （story pack、文章、任何准备发布的东西），逐句核 claim 级别。
- **下午**：发布动作（文章发到博客/对外渠道，按 REPO_PUBLIC_SPLIT 的公开/私有边界
  `[VERIFY-LOCAL]`）。
- **晚上**：ledger 第 11 天，预跑 12 天总评分。
- **Done criteria**：至少一份对外资产实际发布；无任何越级 claim 流出。

### D12 · 6/21（周日）— 缓冲日
- 全天：机动。补任何轨道的欠账；若全部达标，则提前做 D13 的复盘。
- **Done criteria**：五条轨道无红色项。

### D13 · 6/22（周一）— Sprint 复盘与下一周期
- **上午（Fable 5）**：sprint 总复盘（`RETRO_2026-06-22.md`）：
  每条轨道的 done criteria 达成率、ledger 12 天评分总结、
  哪些 agent 分工有效/无效、下一个 12 天周期的候选主题。
- **下午**：ledger 决定续跑方案（独自续跑 / 扩 universe / 停止——按 protocol 第 8 节的决策树）。
- **Done criteria**：复盘文档 commit；下周期第一天的任务已写好。

## 5. 额度紧张时的降级表

| 额度状态 | 保留（必须用 Fable 5） | 降级（换工具） | 直接砍 |
|---|---|---|---|
| 轻度紧张（剩 >50%预算但进度落后） | claims 审查、gate 判读、对抗性 Q&A、复盘 | 文章初稿→自己写+Fable 5 只改一轮；代码全部给 Codex | 英文版文章推迟 |
| 中度紧张 | gate 判读、claims 终审 | story pack 演练→录音自评；案例写作→Ollama 草稿+Fable 5 终审 | T5 整条轨道推到下周期 |
| 重度紧张 | 每周 2 次：ledger 周评分判读 + claim 终审 | 其余全部 Codex/Cursor/人工 | T2 暂停（gate 冻结状态保留，不算 kill） |

**判断额度的检查点**：每天日终复盘时记录当日 Fable 5 会话数；D6 检查点正式评估一次。

## 6. 全局 stop rules

- 任何一天 ledger 仪式被跳过 ≥2 次 → T3 流程有设计问题，D6/当晚必须修流程而不是责怪执行。
- 任何轨道连续 3 天没有 commit → 该轨道自动降级一档，腾资源给其他轨道。
- 任何对外材料发现越级 claim → 当天停止该材料的传播，回到 matrix 修订。
- 6/22 无论完成度如何，sprint 准时结束，未完事项进入下周期，不延期。

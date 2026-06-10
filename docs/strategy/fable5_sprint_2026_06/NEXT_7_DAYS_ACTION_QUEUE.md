# NEXT_7_DAYS_ACTION_QUEUE — 2026-06-10 → 2026-06-17

> 本队列**取代** FABLE5_MASTER_PLAN 的 D1–D7 作为实际执行依据
> （依据：PHASE2_ACCEPTANCE_AUDIT 对 master plan 的"压缩"判定）。
> 共 9 个任务，按优先级排序。规则：高优先级任务红色（未完成）时，
> 禁止启动队列下半区的任务。

---

## AQ-1 ｜ Ledger 首条真实预登记记录
- **owner**: founder manual（Fable 5 辅助生成数字）
- **why now**: 全包 1254 行文档对应 0 行真实数据；预登记的日历价值每天流失，
  今天不 commit，60 交易日 L3 路径就顺延一天
- **input**: FINANCE_CALIBRATION_LEDGER_PROTOCOL.md 第 2、3、6 节
- **output**: ledger repo 内 `forecasts/2026-06-11.jsonl`（开盘前 commit）
- **done criteria**: git log 显示带时间戳的 commit，含 10 标的 × ≥2 源（B0、B1
  允许首日手算/粗算，标 `protocol_version: "1.0-manual"`）
- **estimated time**: 90 分钟（首日手工；脚本就位后降至 30 分钟）
- **stop condition**: 若手算 B1-garch 超 30 分钟 → 首日只录 B0-flat，别完美主义

## AQ-2 ｜ Ledger 脚本三件套交付 Codex
- **owner**: Codex
- **why now**: AQ-1 的手工模式不可持续；脚本是仪式 ≤30 分钟的前提
- **input**: CODEX_TASKS_READY.md 任务 C1+C2+C3（spec 已写成可复制 prompt）
- **output**: `scripts/make_forecast_template.py`、`scripts/score_day.py`、
  `scripts/validate_jsonl.py` + 合成数据测试
- **done criteria**: pytest 全绿；对协议文档示例 JSON 算出可手工复核的 CRPS
- **estimated time**: founder 派发 10 分钟；Codex 产出后验收 30 分钟
- **stop condition**: 若 Codex 两轮内未通过验收 → 降范围只要 score_day.py，
  模板生成继续手工

## AQ-3 ｜ [VERIFY-LOCAL] 全量核对
- **owner**: founder manual（本机，对照 WMDB 文件）
- **why now**: 不核完，story pack 投资人版被锁、claims matrix C3–C7 级别悬空、
  后续所有对外动作都带不确定性
- **input**: 00_README_SOURCE_STATUS.md 的核对流程 + 本机 PROJECT_STATE.md、
  STORY_THESIS、PITCH_DECK、REPO_PUBLIC_SPLIT
- **output**: 各文档内标记清除/修正；改动 commit 信息注明 "verify-local pass"
- **done criteria**: `grep -r "VERIFY-LOCAL" docs/strategy/fable5_sprint_2026_06/`
  仅剩 gate 槽位和工具配额类条目
- **estimated time**: 60 分钟
- **stop condition**: 超 90 分钟 → 只核 PUBLIC_CLAIMS_MATRIX 和 STORY_PACK 两份，
  其余标记保留到周末

## AQ-4 ｜ Golf G2/G3 访谈消息发出
- **owner**: founder manual
- **why now**: D4（6/13）落锤死线；访谈有 1–2 天回复延迟，今天不发 = 死线必破，
  且默认判定是 FAIL
- **input**: FOUNDER_MANUAL_ACTIONS.md 第 2 节（消息模板已写好）
- **output**: ≥5 条消息发出；回复记录到 GOLF_VERTICAL_DECISION_MEMO 第 8 节证据区
- **done criteria**: 发出数 ≥5（回复数不受你控制，不作为今日 done 标准）
- **estimated time**: 20 分钟
- **stop condition**: 无（这是全队列摩擦最低的任务，没有合法的不做理由）

## AQ-5 ｜ Golf G1 数据源排查
- **owner**: Cursor（交互式网查）或 Codex（按 C5 prompt）
- **why now**: G1 是 go/no-go 四条中唯一可纯桌面检验的，今晚出结果给 D4 用
- **input**: GOLF_VERTICAL_DECISION_MEMO.md 第 4 节 G1 行 + 第 5 节路径 1/2
- **output**: memo 第 8 节 G1 证据行（数据路径清单：来源、字段、获取方式、成本）
- **done criteria**: 能回答"存在 ≥1 条无需商务谈判即可启动的数据路径"——是/否+证据
- **estimated time**: 45 分钟
- **stop condition**: 2 小时无结论 → G1 记 FAIL（举证责任在 GO 方）

## AQ-6 ｜ Golf go/no-go 落锤
- **owner**: founder manual（Fable 5 用 P4/P5 模板辅助判读，不代签）
- **why now**: 死线 6/13 上午；拖延 = 隐性定位 D 但不承认
- **input**: memo 第 4 节 criteria + AQ-4/AQ-5 的证据
- **output**: GOLF_VERTICAL_DECISION_MEMO.md 第 8 节 DECISION 区填写并 commit
- **done criteria**: 四条 PASS/FAIL 各附证据；定位 A/B/C/D 签字；复议条件写明
- **estimated time**: 30 分钟
- **stop condition**: 证据不足按 memo 规则默认 FAIL，不许"再观察几天"

## AQ-7 ｜ V10/V2 填槽并冻结
- **owner**: founder manual（30 分钟摘录）+ Fable 5（冻结前审查阈值可判性）
- **why now**: gate plan 当前是惰性资产；且按审计新规——
  **6/12 结束仍未填槽，T2 轨道自动按 FAIL-budget 关闭**
- **input**: 本机 FOUNDING_SPINE_V10 / QUANTUM_CORE_GATE_V2 两份文件 +
  V10_V2_RESEARCH_GATE_PLAN.md 第 2 节
- **output**: gate plan 槽位填写 + 冻结 commit
- **done criteria**: 5 个 SLOT 非空；SLOT-4 阈值是具体数字；commit 信息含 "FROZEN"
- **estimated time**: 30–45 分钟
- **stop condition**: 若源文件中实验设计无法在 SLOT-5 预算内执行 →
  直接判 FAIL-by-design，写停止声明，T2 干净关闭（这也是合法的好结局）

## AQ-8 ｜ 30 秒版叙事实战就绪
- **owner**: founder manual + Fable 5（P2 对抗演练）
- **why now**: 叙事是排第 2 的优先级；30 秒版不依赖任何未核信息，可立即背
- **input**: OMYTEA_EXTERNAL_STORY_PACK.md 第 2 节 + 第 6 节 Q1–Q5
- **output**: 无文件——脱稿能力本身是产出；演练记录追加到 daily_log.md
- **done criteria**: 脱稿讲完 30 秒版 + 即兴答出 Q1/Q5/Q6 不越级
- **estimated time**: 两次 20 分钟（D2、D5 各一次）
- **stop condition**: 无需 stop；但投资人版在 AQ-3 完成前禁用

## AQ-9 ｜ 7 日滚动校准报告
- **owner**: Codex（C6 prompt）→ Fable 5 判读
- **why now**: 排在此处因为依赖 AQ-1/AQ-2 跑满一周；6/17 是第一个有意义的报告点
- **input**: ledger repo 一周数据 + CODEX_TASKS_READY C6
- **output**: `reports/2026-06-17_week1.md`（PIT 直方图 + coverage 表 + skill scores）
- **done criteria**: 报告生成且 Fable 5 判读确认"无流程级异常"（不判校准好坏——
  样本量诚实条款）
- **estimated time**: 30 分钟（脚本就位的前提下）
- **stop condition**: 若该周断更 ≥2 次 → 报告改写为流程故障分析，先修流程

---

## 队列外（明确不做清单）

- **AQ-10 候补 ｜ Civilization 框架填充**：仅当 AQ-1 至 AQ-6 全绿时，
  在本机用产品化文档第 7 节的 prompt 跑一次。任何一项红色 → 本周不碰。
- master plan 的晚间时段编排：废弃，不按它执行。
- AGENT_OPERATING_MANUAL 增补：冻结。
- 任何新研究 idea、新 vertical、新文档：拒绝，记到下周期候选清单。

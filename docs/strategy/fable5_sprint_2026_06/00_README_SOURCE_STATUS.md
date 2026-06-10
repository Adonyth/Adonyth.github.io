# Fable 5 Sprint 2026-06 — 源文件状态与使用说明

生成日期：2026-06-10
生成环境：Claude Code 云端容器（仓库 `adonyth/adonyth.github.io`，分支 `claude/fable5-strategy-sprint-2026-s2oy2b`）

## 重要：源文件可用性声明

本 sprint 包的所有文档基于**任务描述中提供的上下文**构建。以下指定源文件位于本机
`/Users/chenjiaxuan/Downloads/`，**云端环境不可达，未能读取**：

| 文件 | 状态 | 原因 |
|---|---|---|
| `WMDB/PROJECT_STATE.md` | 未读取 | 路径在本机，云端不存在 |
| `WMDB/docs/OMYTEA_MASTER_PLAN.md` | 未读取 | 同上 |
| `WMDB/docs/TECH_EXPLAINER_HOW_IT_WORKS_2026-06.md` | 未读取 | 同上 |
| `WMDB/docs/STORY_THESIS_AND_EDGE_2026-06.md` | 未读取 | 同上 |
| `WMDB/docs/MEETING_TALKING_POINTS_AND_QA_2026-06.md` | 未读取 | 同上 |
| `WMDB/docs/PLAIN_EXPLAINER_FOR_COFOUNDER_2026-06.md` | 未读取 | 同上 |
| `WMDB/marketing/PITCH_DECK.md` | 未读取 | 同上 |
| `WMDB/company/REPO_PUBLIC_SPLIT.md` | 未读取 | 同上 |
| `WMDB/docs/research/FINANCE_MARKET_PREDICTION_SURVEY_2026-06-10.md` | 未读取 | 同上 |
| `WMDB/PLAN_AMENDMENT_2026-06-10_QUANT_DESK.md` | 未读取 | 同上 |
| `WMDB/docs/research/FOUNDING_SPINE_V10_PROPOSED_NEXT.md` | 未读取 | 同上 |
| `WMDB/docs/research/QUANTUM_CORE_GATE_V2_PROPOSED_NEXT.md` | 未读取 | 同上 |
| `WMDB/WORK_PLAN_V418.md` | 未读取 | 同上 |
| `civilization-tech-path-research/00-MASTER-SYNTHESIS.md` | 未读取 | 同上 |
| `civilization-tech-path-research/01-physical-path-verdicts.md` | 未读取 | 同上 |
| `civilization-tech-path-research/02-startup-answer.md` | 未读取 | 同上 |

## 因隐私边界主动跳过（按你的指令，即使可达也不会读）

- `legal/OMYTEA_LLC_MASTER_INFO.md`
- `company/opt/`、`.wolf/`、`.env`、`settings.local.json`
- 任何 credentials / secret / raw immigration docs / raw private prediction ledgers
- 本次会话**没有读取任何上述文件**（它们在云端也不存在）。

## `[VERIFY-LOCAL]` 标记约定

所有文档中标记 `[VERIFY-LOCAL]` 的条目，是基于你的任务描述合理推断、
但需要对照本机源文件确认的内容。使用流程：

1. 在本机打开对应源文件；
2. 搜索文档中的 `[VERIFY-LOCAL]` 标记；
3. 确认无误则删除标记，发现出入则修正内容。

预计全部核对一遍 ≤ 60 分钟。这些文档的框架、协议、规则部分
（claims 分级、ledger schema、scoring metrics、stop rules、agent 分工）
不依赖源文件，可直接使用。

## 如何让 Fable 5 读到源文件（下次会话）

任选其一：
- 在本机用 Claude Code CLI 在 `/Users/chenjiaxuan/Downloads/WMDB` 目录下运行本任务；
- 把（脱敏后的）相关 docs 推到一个私有 repo 并加入云端会话的 repo scope；
- 直接把关键文件内容粘贴进对话。

## 文件清单

1. `FABLE5_MASTER_PLAN.md` — 12 天每日执行计划
2. `PUBLIC_CLAIMS_MATRIX.md` — L0–L5 claim 分级与措辞边界
3. `OMYTEA_EXTERNAL_STORY_PACK.md` — 对外叙事包 + 15 个尖锐问答
4. `V10_V2_RESEARCH_GATE_PLAN.md` — 最小实验 gate / kill criteria / no-tune rules
5. `FINANCE_CALIBRATION_LEDGER_PROTOCOL.md` — 零交易校准账本协议
6. `GOLF_VERTICAL_DECISION_MEMO.md` — golf wedge go/no-go 决策备忘
7. `CIVILIZATION_TECH_FRAMEWORK_PRODUCTIZATION.md` — 文明科技框架产品化（源文件未读，含降级方案）
8. `AGENT_OPERATING_MANUAL.md` — 多 agent 协作操作手册

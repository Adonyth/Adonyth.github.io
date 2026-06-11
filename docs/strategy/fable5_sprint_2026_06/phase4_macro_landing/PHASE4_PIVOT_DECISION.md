# PHASE4_PIVOT_DECISION — 暂停 finance 深挖，转向宏观落地

日期：2026-06-10/11 ｜ 性质：founder 决策的执行化记录（决策本身已由你做出）

## 1. Finance ledger 已经完成了什么（verified，本仓库可查证）

- 完整最小闭环：生成 → schema 验证 → 评分 → validator，11/11 测试通过
  （commit c114294，PHASE3_EXECUTION_LOG 有命令级记录）。
- 协议文档（universe、分位格式、CRPS/PIT/coverage、append-only schema、
  no-trading 硬边界、professional review 问题清单）。
- Phase 4 机器审计：PASS WITH FIXES，3 个 required fixes 已知（late 字段、
  resolution 规则钉死、push-not-commit 证据）。
- **未完成且如实记录**：真实预登记记录 0 行。

**机制证明的含义**：收据机制（预登记→不可改→统一评分）在工程上成立且
便宜（纯 stdlib、零依赖）。这是它作为"proof of mechanism"的全部内容——
不多也不少。

## 2. 继续深挖 finance 的风险（为什么现在停）

1. **合规摩擦前置**：下一步任何对外动作都卡在 attorney 意见（已知依赖）；
   投入会堆积在"不能公开的资产"上。
2. **滑向禁区的结构性引力**：finance 语境里每个"改进"（更多标的、更好模型、
   实时数据）都在朝投资建议/交易系统方向滑——matrix C8/C11 的禁止线
   会被工程惯性持续测试。
3. **数据源摩擦**：免费公开数据的获取/许可问题在 60 天尺度必然出现。
4. **它不回答 startup 的核心问题**：自己给自己评分证明机制，
   但不产生 non-owner rows、不产生买家信号。继续深挖是用舒适的工程
   回避不舒适的用户验证。

## 3. 现在更高杠杆的任务

把已验证的收据机制泛化为产品：**方向选择（谁先买单）→ MVP 定义 →
UI 从研究 demo 变成产品 → buyer discovery**。这正是长上下文综合工作，
是 Fable 5 的相对优势区；而 finance 的下一步是合规等待 + 数据管道苦工。

## 4. 保留为 "proof of mechanism" 的产物（冻结状态，不再投入）

| 产物 | 保留理由 | 状态 |
|---|---|---|
| `ledger/` 全部代码+测试 | 机制可行性的可运行证明；schema 直接复用为产品数据模型起点 | 保留，只修 R3（late 字段）后封板 |
| 协议文档 + Phase 4 审计 | 展示 claim discipline 的活证据（对技术合伙人/投资人 Q7 类问题） | 保留 |
| sample dry-run 记录 | demo 用格式演示 | 保留 |

**每日真实运行是否继续**：推荐**降级为可选**——如果 founder 愿意每天
15 分钟（脚本就位后）就跑，它是唯一随日历增值的资产；但不再是队列第一
优先级，断更不触发 stop rule。决定权在你，默认按"可选"执行。

## 5. 冻结到以后的 finance 任务

- M1-llm 预测源、universe 扩展、conditional coverage 自动化 → 冻结
- report.py 周报自动化 → 冻结（手工可替代）
- attorney/DSO/CPA review 发出 → **不冻结但降速**：仍按 FOUNDER_MANUAL_ACTIONS
  执行（问题清单已备好，发邮件成本 30 分钟），因为无论哪个方向落地，
  "校准记录能否公开"都需要这个答案
- 60 交易日 L3 升级路径 → 随每日运行的"可选"状态顺延

## 6. 不变的约束（pivot 不豁免）

- Golf go/no-go 死线（6/13）维持——它现在是"产品 wedge 候选"评估的一部分
- V10/V2 填槽死线（6/12，过期 FAIL-budget 关闭）维持
- claims matrix 全部禁止线维持
- 任何新方向不得宣称用户/收入/部署/优势

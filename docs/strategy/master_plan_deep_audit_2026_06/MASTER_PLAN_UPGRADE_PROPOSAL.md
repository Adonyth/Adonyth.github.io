# MASTER_PLAN_UPGRADE_PROPOSAL — 升级方案与 Amendment 草稿

## 1. 保留 / 删除 / 重写 / 新增

### 保留（plan 的真资产）
- 核心 thesis："验证/校准/审计是 AI 时代的稀缺层" + "我们不声称预测更准"
- claim 分级制度（L0–L5）与全部禁止线
- gate 制度（pass/fail/kill/no-tune）——制度本身优秀，问题在被审对象的地位
- finance ledger 作为机制证明的定位（Phase 4 pivot 已正确处理）

### 删除
- "Grand Unified World Model" 作为**目标**的全部表述（V1 漏洞）
- 任何把 quantum 线描述为"核心/基石"的语言 [INFERRED] → 降为
  "gate 管辖的边缘探索"
- 多 vertical 并行的暗示——改为"一次一个 resolution 供给实验"

### 重写
- 北极星 → ULTIMATE_GOAL_REWRITE 推荐版（世界模型从目标改为客户）
- "calibration ledger = demo" → "= 免疫污染评测装置的原型"（O2）
- civilization research 的定位 → 旗舰收据内容（O3）
- 术语表统一（V7）：对外 Omytea/receipts/ledger 三词；
  WMDB、Quantum-Core、Founding Spine 声明为内部代号，列入公开检查项

### 新增
- 一级章节《Resolution 供给策略》（V4）
- 一级章节《信任的工程化阶梯》（V5：server timestamp → 开源 verifier →
  RFC3161 锚定 → 治理）
- 《修订准入规则》（V2：证据棘轮，见下方 amendment §D）
- 《开放标准轨道》（O1，轻量：spec 整理与发布，≤1 周/季度投入）

### 升格 / 降级
- **升格**：buyer discovery（访谈）→ plan 一级活动；receipt 公开页 →
  第一公开 artifact；O2 position note → 研究叙事主锚
- **降级**：UI 打磨（P0 之外）、i18n、heatmap/conformal 展示、
  一切新研究线提案（冻结默认）

## 2. Amendment 草稿（可直接粘贴进 docs/OMYTEA_MASTER_PLAN.md 文首）

```markdown
---
# AMENDMENT 2026-06 — Master Plan V2（经 deep audit 后的修订）
# 依据：docs/strategy/master_plan_deep_audit_2026_06/（全 10 件）
# 本 amendment 与正文冲突处，以本 amendment 为准。

## A. 北极星（替换原 "Grand Unified World Model" 全部表述）

Omytea 的终极目标不是建造统一的世界模型，而是建造**所有世界模型
（以及所有预测者——人、机构、agent）都必须接受对账的统一账本**：
现实的预登记记录层——什么被预言了、何时、由谁、后来发生了什么、
评分多少。我们不统一模型，我们统一收据。

推论（不变式）：
1. Omytea 永不下场做预测业务——中立性是唯一护城河的根基。
2. 任何"我们的模型/方法更准"类目标自动违宪。
3. 世界模型公司是潜在客户与被审计对象，不是竞争对手，也不是我们。

## B. 角色定义（统一术语）

- 对外名词仅三个：Omytea（公司）、receipt（原子产品物）、
  ledger（累积履历）。
- WMDB、Quantum-Core、Founding Spine、future_reality_ledger 为内部
  代号，禁止出现在任何对外材料（列入发布检查清单）。

## C. 主线与供给（新增一级原则)

- 主线 = 收据机制的外部化：non-owner 预测源 × 干净 resolution 供给。
- Resolution 供给是第一约束：任何 vertical 评估先答
  "谁供给 resolved outcomes、激励是什么、摩擦多大"。
- 同时只允许一个 resolution 供给实验在跑。

## D. 修订准入规则（防计划递归）

- 本 plan 的任何修订必须在 changelog 中引用至少一条**新的外部事实**
  （访谈记录/用户行为/外部数据/第三方反馈），否则修订无效。
- 版本号冻结：本 amendment 后，plan 修订频率上限为每 30 天一次
  （外部事实触发的紧急修订除外，需在 changelog 标注触发事实）。
- 执行类文档（队列/任务包）不受此限，但不得与本 amendment 冲突。

## E. 证据阶梯（plan 级 KPI，替换一切感觉式进度）

唯一进度度量：L 级证据的爬升。
当前状态如实记录：机制=L2（工具链可运行），市场=L0（零访谈），
数据=0 行 non-owner。30/60/90 天目标见 MASTER_PLAN_V2_ROADMAP.md。
---
```

## 3. 边界要更硬的地方

- 合规死线（V6）：6/17 邮件未发出 → 一切对外发布冻结（机械执行）
- gate 死线既有规则不变；任何 gate 外研究提案默认拒绝，
  进 NEXT_CYCLE_CANDIDATES 排队
- 自产数据永不混入 non-owner 统计（dryrun 隔离原则推广到一切计数）

## 4. 路线要更大胆的地方

- O1 标准发布：不要等产品成熟——spec v0.1 在 30 天内公开（先发定义权）
- O3 文明收据：用自己最重的判断当收据示范，比任何营销文案都大胆且诚实
- 公开 build-in-public 的 ledger 自审计月报（attorney 放行后）：
  把自己的纪律变成内容资产

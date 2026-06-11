# UI_REDESIGN_SPEC — 目标态 UI 设计规格（可直接实现）

> 目标态设计，不依赖现状代码（现状处置见 UI_UX_AUDIT §4）。
> 技术形态：**对外面 = 静态生成的 HTML（从 JSONL/数据生成），
> 内部 console = 现有 Streamlit 降级保留**。视觉规范见 DESIGN_SYSTEM.md。

## 1. 产品第一屏（公开 landing）

一屏内只做一件事：让访客理解"预测收据"并看到一张真的。

```
[Logo: Omytea]                              [Receipts] [Research] [About]

  Forecasts are cheap now.
  Receipts make them count.

  Omytea issues tamper-evident receipts for predictions —
  registered before the outcome, scored after it.

  [ See a live receipt ↓ ]        [ Get receipts for your agent → ]

  ┌─ RECEIPT #a3f2 ─────────────────────────────┐
  │  (一张真实的、已 resolved 的收据卡，见 §6)      │
  └─────────────────────────────────────────────┘

  We don't claim better predictions. We make any
  prediction's track record verifiable.
```

- 首屏禁止出现：CRPS/PIT 等术语、量子、任何金融标的、产品截图轮播。
- 第二屏：三步说明（Register → Lock → Score），各一句话一图标。
- 第三屏：诚实区块 "Where we are"（early stage 声明，matrix 校准）+ CTA。

## 2. 导航结构

**公开站（静态）**：`Home / Receipts(示例库) / Track Records / Research / About`
**App（登录后，v1）**：`My Receipts / New Forecast / Track Record / Settings`
导航命名规则：永远用用户对象（receipt/forecast/record），永远不用方法名。

## 3. 页面列表与每页目标

| 页 | 目标（一个） | 核心组件 |
|---|---|---|
| Landing | 30 秒理解 + 一个 CTA 点击 | Hero、live receipt 卡、3 步图、诚实区块 |
| Receipt 详情页 | 陌生人 30 秒看懂这张收据 | Receipt 卡（大）、状态时间线、verify 折叠区 |
| Track Record 页 | 判断"这个作者校准如何" | 校准摘要卡、收据列表、样本量声明 |
| New Forecast（v1） | ≤90 秒完成一次登记 | 单页表单（§7） |
| My Receipts（v1） | 知道哪些待决/已决 | 两组列表 + 倒计时 |
| Research | 收纳方法论/manifesto | 长文排版，从主流程移出的解释都来这 |

## 4. 关键状态（每个数据组件必须定义全六态）

- **empty**：一句话说明 + 单一行动按钮 + 一张 SAMPLE 示例（永远标注 SAMPLE 角标）
- **loading**：骨架屏（不转圈）
- **success/registered**：收据卡 + "Locked at {server time}" 确认条
- **error**：人话 + 可重试；表单错误行内显示
- **resolved**：得分披露 + PIT/正误标记，视觉权重高于 pending
- **unverified/pending**：明确的中性灰标识——"未决"是常态不是缺陷，
  禁止用红色/警告色表示 pending

## 5. 交互与数据可视化原则

- 每屏一个主行动；次行动一律降为文字链接
- 数字优先于图：n<30 时显示数字表格 + "样本量不足"声明，禁止画平滑曲线
  （诚实条款的 UI 化——这是产品的核心差异化，不是限制）
- 校准曲线只在 n≥30 时出现，且必须带对角参考线和置信带
- 所有时间戳显示 UTC + 相对时间（"2h before deadline"）
- 不用动画表达"AI 在思考"之类的拟人效果

## 6. Receipt card 设计（产品的原子单位）

```
┌──────────────────────────────────────────────┐
│ RECEIPT  #a3f2c9        ● RESOLVED: CORRECT  │   ← 状态徽章（§8 配色）
│──────────────────────────────────────────────│
│ "GPT-5 agent will resolve the ticket         │   ← claim 原文，最大字号
│  without human escalation."                  │
│                                              │
│ Forecast   78% yes          by agent-ops-bot │
│ Registered 2026-06-12 14:02 UTC   ⛓ sha256…  │   ← 锁定凭证行
│ Deadline   2026-06-13 00:00 UTC              │
│ Resolved   2026-06-13 09:14 UTC  → YES       │
│ Score      Brier 0.048                       │
│──────────────────────────────────────────────│
│ Evidence grade: ▣▣▢  REGISTERED·RESOLVED      │   ← 证据等级（§8）
│ [Verify this receipt]            [Author ↗]  │
└──────────────────────────────────────────────┘
```

要点：claim 文本是主角；hash+时间戳构成"收据感"；分位数型预测用
迷你区间图（5 个刻度点+实现值箭头）替代 78% 行。
卡片必须在 600px 宽度内完整可读（聊天工具内嵌截图场景）。

## 7. Forecast creation flow（v1，单页完成）

```
1. Claim 文本（占位符示范可判定写法："X will … by {date}"）
2. 可判定性自检行：deadline 选择器 + "谁/什么来判定结果" 单选
   （我自己/指定数据源/对方确认）
3. 预测值：binary 滑条(显示%) 或 切换到分位数模式（5 输入框，实时单调校验）
4. 预览卡（即 receipt 卡的 pending 态）→ [Register & lock] 单按钮
5. 成功态：receipt URL + 一键复制 + "share it or it didn't happen" 微文案
```
拒绝：多步向导、草稿箱、富文本。登记必须 ≤90 秒。

## 8. Evidence / claim-level badge

- 三档起步：`REGISTERED ▣▢▢`（已锁定）→ `RESOLVED ▣▣▢`（已评分）→
  `VERIFIED ▣▣▣`（resolution 来源外部可查）
- 对应 claims matrix 思想但不暴露 L0–L5 术语给外部用户
- SAMPLE 数据永远带橙色斜角标，与真实数据不可混淆（dryrun 隔离原则 UI 化）

## 9. Resolution/scoring flow（v0 concierge → v1 表单）

- resolution 录入者、时间、依据来源三字段必填；录入后收据状态机单向流转
  （pending → resolved，不可逆，改错走 amendment 附注，原值仍可见）
- 评分自动计算（复用 ledger/scripts 数学），UI 不提供任何手工改分入口

## 10. Mobile responsive 原则

- 对外三页（landing/receipt/track record）移动优先设计，>50% 流量假设来自
  聊天分享点击
- receipt 卡单列堆叠；verify 区折叠
- 内部 console 不做移动适配（明确放弃）

## 11. 复用 / 重写清单

| 复用 | 方式 |
|---|---|
| ledger/scripts 评分数学 | 原样作为评分引擎 |
| ledger JSONL schema | 扩展为 PRD §4 数据模型的存储层 |
| conformal/heatmap 代码 | 留在内部 console，不进对外面 |
| 重写 | 全部对外 HTML（landing/receipt/track record，静态生成器方案见 CODEX 任务 CX-2） |

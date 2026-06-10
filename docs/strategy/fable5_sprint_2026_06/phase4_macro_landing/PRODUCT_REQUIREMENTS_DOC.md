# PRODUCT_REQUIREMENTS_DOC — Omytea Receipts MVP PRD v0.1

## 1. 基本信息

- **Working title**: Omytea Receipts（产品面）；内部代号沿用 console 重构
- **一句话**: 给预测开收据——登记时间戳锁定、结果统一评分、履历不可美化
- **Target user（v0）**: ① 向客户交付 AI agent 的小团队（D1，付费假设）
  ② 公开发预测的个人（D2，免费/橱窗） ③ founder 本人（D8，dogfood）
- **Core job-to-be-done**: "当别人质疑我（或我的 agent）的判断是否靠谱时，
  我能甩出一份第三方的、不可篡改的历史成绩单。"

## 2. Top 3 use cases

1. **登记收据**：用户提交一条预测（文本 claim + 可判定 resolution 条件 +
   概率/分位数 + 截止时间）→ 获得带时间戳的 receipt URL。
2. **结果评分**：resolution 条件到期 → 录入结果（v0 手工/concierge）→
   receipt 变为 resolved 态，显示得分。
3. **出示履历**：用户分享自己的 track record 页（校准曲线 + 收据列表 +
   样本量诚实声明）给客户/读者/投资人。

## 3. Non-goals（v0–v1 明确不做）

- 不做预测聚合/众包共识（不是 Metaculus）
- 不做交易/投资任何功能；金融类 claim 仅作为登记对象且带免责声明
- 不做 auth 体系/多租户/billing（v0 concierge：founder 手工开账户）
- 不做自动 resolution 的通用引擎（v1 只接 2-3 个白名单数据源）
- 不做评论/社交功能

## 4. 核心对象（数据模型）

直接泛化 Phase 3 ledger schema（已验证可行）：

```
Claim       {claim_id, author_id, text, domain, resolution_criteria,
             resolution_deadline, created_utc, status}
Forecast    {forecast_id, claim_id, kind: binary_prob | quantiles,
             value(s), created_utc, late}
Receipt     {receipt_id, forecast_id, registered_utc(server-side),
             content_hash, public_url, evidence_grade}
Resolution  {claim_id, outcome, resolved_utc, data_source, resolver}
Score       {forecast_id, rule: brier | crps, value, pit_bucket?, in90?, in50?}
TrackRecord {author_id, n_resolved, calibration_bins, mean_score,
             skill_vs_baseline?, sample_size_disclaimer}
```

关键设计决定：
- **server-side `registered_utc` + content_hash 是收据的灵魂**（Phase 4 审计
  结论：自报时间戳不构成证明）
- binary 概率（Brier）和分位数（CRPS）双轨支持——agent 输出多为 binary，
  finance/golf 多为分位
- `evidence_grade` 字段对齐 claims matrix L0–L5 思想：
  `registered → resolved → externally-verifiable` 三档起步

## 5. User flow（v0）

```
访客 → receipt URL（被分享）→ 看懂收据 → 点 author → track record 页
                                              ↓
作者 → 登录(v0: magic link 或手工) → New Forecast 表单 → 确认预览
     → 提交 → receipt 生成（URL+hash）→ [到期] → resolution 录入
     → receipt 变 resolved → track record 自动更新
```

## 6. Dashboard 必须显示什么（author 视角，按优先序）

1. 未决收据列表（最近截止的在前，倒计时）
2. 已决收据列表（得分 + PIT/正误标记）
3. 校准摘要卡：n_resolved、覆盖率/校准曲线（n<30 时显示
   "样本量不足以下结论"而不是曲线——诚实条款产品化）
4. "分享履历"按钮（生成公开页链接）

**不显示**：排名/排行榜（v0 无社区）、任何"准确度排名世界第 X"类话术。

## 7. Onboarding

- v0 **concierge**：founder 1:1 帮第一批用户登记前 3 条预测（电话/共享屏幕），
  亲眼看卡点
- 产品内：首次进入即一个空状态页，"登记你的第一条预测"单按钮 +
  一条示例收据（标注 SAMPLE，不可与真实混淆——沿用 dryrun 隔离原则）
- 拒绝：教程视频、多步引导浮层

## 8. 什么是"成功使用一次"

> 用户登记了一条**真实的、有截止日的、可判定的**预测，拿到 receipt URL，
> 并把这个 URL 发给了至少一个其他人。
> （发给别人 = 价值被理解的行为信号；没发 = 只是又一个笔记工具）

## 9. Fake-door / concierge 测试（v0 期间，每个 ≤1 天搭建）

1. **Receipt 假门**：landing 上 "Get a receipt for your agent's claims" 按钮
   → 邮箱收集页。测 D1 文案的点击意愿。
2. **Concierge agent audit**：对 1 个 agent 团队，人肉每天从他们的输出里
   摘 5 条 claim 登记 + 周报。测他们是否看报告、是否转发给客户。
3. **公开 forecaster 履历代建**：给 1 个公开预测者手工建履历页，
   问"愿意挂在你的简介里吗"。测 D2 的资产/威胁感知（Kill 条件直测）。

## 10. 版本范围

| | 范围 | 不含 |
|---|---|---|
| **v0**（14 天内） | 静态 receipt 页生成器（从 JSONL → HTML，复用 ledger schema）+ concierge 登记 + 手工 resolution + track record 静态页 | 登录、数据库、API |
| **v1**（60 天内） | 简单 web 表单登记（server-side 时间戳）+ SQLite/Postgres 单库 + magic link + 2 个白名单自动 resolution 源 | billing、团队空间 |
| **v2**（90 天+，仅当 design partner 确认） | API/SDK（agent pipeline 直接 POST claim）+ 团队 track record + 导出审计包 | 仍不做交易类任何功能 |

## 11. 开放问题（需访谈回答，不要桌面拍板）

- agent 团队愿意公开 receipt 还是只要私有审计包？（影响 v1 公开性设计）
- "第三方"要多中立才可信——Omytea 自营评分够吗，要不要开源 verifier？
- 按 seat、按预测条数、按审计报告，哪种计价听起来不反感？

# NEXT_14_DAYS_MACRO_ACTION_QUEUE — 2026-06-11 → 06-24

> 取代 NEXT_7_DAYS_ACTION_QUEUE 中与 finance 深挖相关的条目；
> golf（6/13 落锤）与 V10/V2（6/12 填槽死线）两条既有死线**保留不变**。
> 每天 ≤3 个重点、必有一个可见产物。主题节奏：
> 前 3 天=现状/决策收口，中 5 天=UI+discovery 并行，后 6 天=接入+复盘。

| 日 | 主题 | 重点（owner） | 当日可见产物 |
|---|---|---|---|
| **6/11 四** | 现状收口 | ① CT-0 现状盘点（Cursor）② [VERIFY-LOCAL] 核对+V10/V2 填槽（founder，死线明天）③ CX-1 数据模型派发（Codex） | UI_CURRENT_STATE.md |
| **6/12 五** | 决策日 | ① V10/V2 冻结 commit（founder+Fable 5，**死线**）② D1 访谈名单 5 人圈定+前 2 条消息发出（founder）③ CX-3 late 修复验收（founder 10min） | gate FROZEN commit + 2 条消息发出 |
| **6/13 六** | Golf 落锤 | ① golf go/no-go 签字（founder，**死线**，证据不足=FAIL）② CT-1 receipt 卡（Cursor）③ FP-2 竞品深查（Fable 5） | DECISION 区签字 + receipt 卡四态截图 |
| **6/14 日** | UI 日 | ① CT-2/CT-3 receipt 页+履历页（Cursor）② CX-2 静态生成器派发（Codex）③ D1 访谈消息再发 3 条（founder） | 两个页面模板渲染截图 |
| **6/15 一** | 文案日 | ① CT-4 landing 重写（Cursor+story pack）② FP-6 landing copy 审查（Fable 5 P3）③ 第 1 个 D1 访谈执行（founder） | 新 landing 本地可打开 + 访谈纪要#1 |
| **6/16 二** | 检查点 | ① 中期审计：14 天队列 vs 实际（Fable 5 P6 扩展版）② CT-5 console 首屏任务化（Cursor）③ 访谈#2（founder） | CHECKPOINT_0616.md |
| **6/17 三** | Demo 装配 | ① sample 数据走通 landing→receipt→track record 全链路（founder+Cursor）② FP-3 UI red-team（Fable 5）③ attorney/DSO/CPA 邮件发出（founder，逾期一周了） | 可点击 demo 录屏 ≤90 秒 |
| **6/18 四** | Discovery 日 | ① 访谈#3、#4（founder）② CX-4 one-pager 验收+P3 终审（Fable 5）③ CT-6 empty states（Cursor） | 访谈纪要 ×2 + one-pager 终稿 |
| **6/19 五** | 接入准备 | ① concierge 流程演练：用自己当假客户全流程走一遍（founder）② CX-5 tracker 落地回填已有访谈（Codex+founder）③ CT-7 术语降噪（Cursor） | concierge runbook 一页 |
| **6/20 六** | 公开物 | ① receipt 示例页部署到可分享 URL（founder+Cursor；用 SAMPLE 数据，绕开 attorney 依赖）② FP-8 demo script（Fable 5）③ 轻日 | 一个可分享 URL |
| **6/21 日** | 缓冲 | 补欠账；全绿则 FP-4 PRD critique（Fable 5） | 欠账清零或 critique 报告 |
| **6/22 一** | Sprint 复盘 | ① 12 天 sprint 正式复盘（Fable 5，含 ledger 续跑决策树执行）② 访谈#5（founder）③ 下一周期候选清单 | RETRO_2026-06-22.md |
| **6/23 二** | 接入冲刺 | ① 第 1 个 non-owner 源 concierge 接入开始（founder；候选：访谈中最热者/golf GO 则球友）② CT-9 徽章统一（Cursor） | 外部源第一条登记记录 |
| **6/24 三** | 14 天总结 | ① FP-10 progress review（Fable 5）：访谈证据汇总→D1 假设判定→30 天目标对版 ② 决定 v1 是否立项（founder 签字） | PHASE4_REVIEW_0624.md + v1 决策 |

## 节奏规则

- **UI 日**：6/13–6/17 为主；**research 日**：6/13、6/21；
  **discovery**：贯穿（消息异步发，访谈嵌在 6/15–6/24）；
  **coding**：Codex/Cursor 全程后台，founder 只做派发+验收
- 战略发散防火墙：任何新 idea 写进 `NEXT_CYCLE_CANDIDATES.md` 一行，
  当天不展开
- 每日 21:30 自检沿用（P6 模板）

## Stop conditions

- 访谈 5 次后 pain 全证伪 → 6/24 复盘提前触发，启动 D2 plan B
- Cursor 任务连续 2 天无法验收 → 砍 P1/P2 任务，只保 P0
- founder 当周可投入 <10 小时 → 砍 UI 线，只保 discovery + 每日自检
- 6/24 无任何 non-owner 记录且无任何访谈确认 pain → 暂停产品工作，
  写诚实的 pivot/persevere memo 再继续

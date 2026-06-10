# CODEX_IMPLEMENTATION_TASKS — 非 UI 实现任务（可复制 prompt）

> 通用边界（已嵌入各 prompt）：不碰凭证/敏感文件；不加交易功能；
> 不引入重型依赖；schema 变更必须向后兼容 ledger/ 现有数据。

---

## CX-1 ｜ 统一数据模型：ledger schema → 产品对象

```
读取 ledger/scripts/validate_ledger.py、ledger/sample/*.jsonl 和
docs/strategy/fable5_sprint_2026_06/phase4_macro_landing/PRODUCT_REQUIREMENTS_DOC.md 第 4 节。

任务：设计并实现 PRD 对象层（Claim/Forecast/Receipt/Resolution/Score/TrackRecord）
与现有 ledger JSONL 的映射：
1. 新建 ledger/scripts/models.py：dataclass 定义六个对象 + from_jsonl/to_jsonl；
2. 现有 forecasts/resolutions 行必须无损映射成对象（写 round-trip 测试）；
3. 新增字段（claim text、resolution_criteria、content_hash、evidence_grade）
   全部 optional，保证旧数据可读；
4. content_hash = 对规范化 JSON（排序键、去 hash 字段自身）的 sha256；
5. 纯 stdlib，append-only 原则不变，禁止任何 account/order/position 类字段。
交付：models.py + tests/test_models.py，pytest/unittest 全绿。
```

## CX-2 ｜ 静态 receipt 页生成器

```
读取 ledger/scripts/models.py（CX-1 产物）、web/templates/receipt.html 与
track_record.html（Cursor CT-2/CT-3 产物）。

任务：实现 web/build_pages.py：
1. 输入 JSONL 数据目录 → 输出 web/dist/ 下每张收据一个 HTML
   （receipts/{receipt_id}.html）+ 每作者一个 track record 页；
2. 纯 stdlib（string.Template 或手写替换），无 jinja 等依赖；
3. n<30 的作者页走"数字表+样本量声明"分支，不生成曲线；
4. SAMPLE 数据（protocol_version 含 dryrun）必须渲染 SAMPLE 角标且
   输出到 web/dist/samples/ 隔离目录；
5. 输出确定性（同输入同输出，便于 diff 审计）。
交付：build_pages.py + 用 sample 数据的端到端测试。
```

## CX-3 ｜ Ledger R3 修复（late 字段）

```
读取 ledger/scripts/make_forecast.py 和
docs/strategy/fable5_sprint_2026_06/PHASE4_FIRST_REAL_LEDGER_AUDIT.md 第 1.3 节、R3。

任务：late 字段从硬编码 false 改为：生成时刻 UTC > 当日 13:30 UTC cutoff
则 true。加常量 CUTOFF_UTC = "13:30"。新增测试：mock 时间在 cutoff 前后
各一例。不改其他任何逻辑。交付：diff 最小的修复 + 2 个测试。
```

## CX-4 ｜ One-pager 机械生成（沿用 Phase 2 C4，目标对齐 D1）

```
读取 phase4_macro_landing/OMYTEA_STARTUP_DIRECTION_RESEARCH.md 的 D1 段、
OMYTEA_EXTERNAL_STORY_PACK.md、PUBLIC_CLAIMS_MATRIX.md。

任务：机械拼装 phase4_macro_landing/D1_ONE_PAGER_DRAFT.md：
受众=AI agent 团队。结构：D1 的 pain 原文 → 一句话产品（story pack 第1节
改"prediction"语境为"your agent's claims"，仅此一处允许的措辞替换，标注出来）
→ 三步机制 → "我们不是什么"（matrix 3.3 反向句式）→ 阶段诚实声明 → CTA
（concierge audit 邀请）。规则：不新增 claim；每段标来源；SUGGESTIONS 区
单列你的改进建议。终稿需 Fable 5 P3 审查后才可外用。
```

## CX-5 ｜ Buyer discovery tracker

```
任务：新建 docs/strategy/fable5_sprint_2026_06/phase4_macro_landing/discovery/
TRACKER.md + 模板 INTERVIEW_TEMPLATE.md。

TRACKER.md：markdown 表格（代号|方向D1/D2|日期|渠道|状态|pain确认?|
愿付钱?|金句|下一步），预填 10 个空行。
INTERVIEW_TEMPLATE.md：单次访谈记录模板（背景3问/pain探查5问/方案反应3问/
结尾2问），问题从 FOUNDER_MANUAL_ACTIONS 第7节 和 FABLE5_NEXT_PROMPTS FP-5
脚本提取，不自创诱导性问题。隐私规则写在文件头：只记代号，不记真名/联系方式。
```

## CX-6 ｜ Public/private split checklist

```
读取 phase4_macro_landing/ 全部文件 + ledger/README.md。

任务：生成 phase4_macro_landing/PUBLIC_PRIVATE_SPLIT_CHECKLIST.md：
三列清单（资产|公开/私有/待attorney|理由），覆盖：ledger代码、ledger数据、
web模板、strategy docs、PRD、design system、one-pager、访谈记录。
默认规则：代码可公开、真实数据待attorney、访谈记录永久私有、
strategy docs 私有。与本机 company/REPO_PUBLIC_SPLIT.md 的合并留
[VERIFY-LOCAL] 标记。不读取任何敏感文件。
```

## CX-7 ｜ README 与仓库导航更新

```
读取仓库根目录结构、docs/strategy/fable5_sprint_2026_06/ 文件清单。

任务：新建 docs/strategy/fable5_sprint_2026_06/INDEX.md：
Phase 1–4 全部文档的一页导航（文件|一句话用途|状态 current/superseded/frozen）。
明确标注：FABLE5_MASTER_PLAN 的 D1-D7 已被 NEXT_7_DAYS_ACTION_QUEUE 取代、
7天队列将被 NEXT_14_DAYS_MACRO_ACTION_QUEUE 取代、finance 扩展任务冻结。
只做整理，不改写任何源文档。
```

## CX-8 ｜ 周报生成器（discovery 进展版）

```
读取 CX-5 的 TRACKER.md 结构。

任务：scripts/weekly_summary.py：解析 TRACKER.md 表格 → 输出
本周新增访谈数/pain确认率/愿付费数/金句列表 的 markdown 周报到
phase4_macro_landing/discovery/weekly/。纯 stdlib。空表格时输出
"0 interviews this week — the queue is blocked on founder outreach"
而不是空文件。
```

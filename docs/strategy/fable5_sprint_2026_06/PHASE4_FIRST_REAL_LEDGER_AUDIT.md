# PHASE4_FIRST_REAL_LEDGER_AUDIT — 首条真实预登记记录审计

审计日期：2026-06-10（UTC 23:30 前后）
审计角色：判官模式（按 P5 模板纪律：只判定，不优化，不为结果辩护）

---

## Verdict

**机器审计（协议+脚本+证据链）：PASS WITH FIXES** — 3 个 Required fixes，
其中 2 个必须在**首日真实 commit 之前**完成，否则首条记录带先天缺陷。

**首条真实记录审计：PENDING — 审计对象不存在。**
审计时点 `ledger/forecasts/` 目录为空，真实 forecasts JSONL 尚未生成/提供。
本文档第 7 节是它的待执行终审清单：文件路径提供后 10 分钟内可出终判。

**当前真实预登记记录数：0。**（`ledger/sample/*.dryrun.*` 为合成数据演示，
按 Phase 4 规则和文件自身的 `1.0-dryrun` 标记，永久排除在证据之外。）

---

## 1. 预登记有效性审计（对机器，不是对记录）

### 1.1 时间戳证据链 — 发现真实弱点

| 证据 | 强度 | 判定 |
|---|---|---|
| `created_utc`（记录内字段） | 弱：脚本自报，本地可任意设置 | 仅作参考 |
| git commit 时间戳 | 弱：`GIT_COMMITTER_DATE` 可伪造，本地 commit 不构成第三方证明 | 仅作参考 |
| **push 到远端的服务器接收时间** | 强：远端（GitHub）接收时间不受本地控制，事后不可回填 | **这是唯一的硬证据** |

**结论：预登记的有效性证据 = 开盘前完成 push，而不只是 commit。**
协议 §1.2"commit 时间戳即登记证明"表述不充分——单机 commit 对第三方
不构成证明。修正见 Required Fix R1。

### 1.2 截止时间定义 — 发现歧义

协议说"开盘前"。10 个标的开盘时间不一：美股/ETF 09:30 ET，EURUSD 24 小时
无"开盘"，VIX 09:30 ET（盘前已有期货）。
**判定：文件级单一截止线 = 13:30 UTC（美东 09:30，6 月为 EDT）。**
全文件一个 cutoff，简单、可审计。EURUSD 沿用同一线（保守方向：
它"开盘"更早，统一线只会更严不会更松）。→ Required Fix R2 落档。

### 1.3 `late` 字段 — 发现实现缺陷（Critical）

`make_forecast.py` **硬编码 `"late": false`**，不对照任何 cutoff 检查。
协议 §1.2 要求晚提交标 `late=true` 单独统计——当前工具做不到，
首日如果晚于 13:30 UTC 生成，记录会带着虚假的 `late:false` 入账，
这正是"事后不可修复的先天缺陷"类别。→ Required Fix R3。

### 1.4 记录信息完备性

schema 含 date / ticker / target / source / 5 分位 / created_utc / late /
protocol_version：horizon 由 `target`（`log_return_next_close` /
`level_next_close`）+ `date` 联合无歧义定义 ✓；universe 由 validator
白名单锁死 ✓；method 由 `source` 标识 ✓；版本可追溯 ✓。**判定：足够。**

### 1.5 事后改写空间

- 脚本拒绝覆盖已有文件 ✓；validator 可作 pre-commit hook ✓。
- git 历史本身可被 rebase/force-push 改写 → 堵截方式同 R1（远端留痕 +
  协议已规定不 rebase 此 repo）。残余风险：私有 repo 的 force-push
  只有 remote 的 reflog/API 事件可查——可接受（审计层自身将来公开后
  此风险消失），记入 Nice-to-have N2。

## 2. Schema 合规审计

对现存可检对象执行（sample 文件 + 测试套件）：

- validator 对 sample forecasts/resolutions：**PASS**（命令与输出见
  PHASE3_EXECUTION_LOG）。
- 多余字段：拒绝（`test_extra_field_fails` 绿）✓
- 交易/订单/仓位/券商/建议类字段：黑名单拒绝（`test_brokerage_key_fails`
  绿，黑名单含 account/position/order/api_key/credential/password/secret/token，
  且 schema 本身无任何方向/动作语义字段）✓
- 分位数严格递增：生成端与校验端双重强制 ✓
- 概率定义一致性：5 分位 τ 集合 {.05,.25,.50,.75,.95} 在生成、评分、
  validator 三处硬编码一致 ✓（N3：抽到共享常量更优雅，不紧急）
- ticker/date 一致性：validator 强制 date=文件名、ticker 在白名单 ✓
- `ledger/schema/*.json` 不存在：**判定为可接受**——validator 代码是
  可执行的 schema 单一权威源；独立 JSON Schema 文件利于第三方核验，
  记 N1，不阻塞。

## 3. Scoring 可行性审计

- **能否无歧义 resolve？当前：否——两处歧义未预先钉死（Critical）：**
  (a) 非交易日规则未定义："next close" 遇节假日/周末顺延到下一交易日收盘，
  还是作废该行？(b) EURUSD 无官方收盘价——必须预先指定快照定义
  （建议：指定单一公开来源的固定时点日频价，写死在协议里）。
  **Resolution 规则必须在预测之前钉死，否则 resolution 时点的自由裁量
  本身就是审计层最忌讳的后门。** → 并入 Required Fix R2。
- resolution 文件字段（realized/data_source/resolved_utc/scores）：足够 ✓
- CRPS/PIT/coverage：可从现有字段直接计算（已实现并测试）✓
- Conditional coverage（按前日 VIX 状态分桶）：现字段不存 regime 标记，
  但 VIX 历史公开可复现，可事后重建，**可接受**；N4 建议 resolution 时
  顺手快照 regime 标记。
- Head-to-head：B0-flat 与 B1-ewma 同文件共存 → skill ratio 可算，
  **不缺 baseline** ✓。注意：当前只有 baseline 对 baseline，
  在 M1-llm/H1-human 入账之前，任何"模型表现"类说法都无对象。

## 4. 证据等级判定（对照 PUBLIC_CLAIMS_MATRIX）

**现在（0 行真实记录）可以声称的：**
- "校准账本的工具链已实现并通过测试，全流程可运行。"（L2，限内部/技术语境）
- 仅此而已。

**首条真实记录合格入账后可以声称的：**
- "账本已开始运行，第 1 天，预登记记录公开可审。"（L2 演示，
  附"样本量不支持任何统计结论"）

**现在禁止声称的：**
- "账本在运行"（它还没有）、任何校准好坏、任何预测能力、
  任何含"金融预测"的对外表述（matrix C8/C11 禁止线）。

**60 天后的升级条件（全部满足才到 L3 候选）：**
- ≥60 个交易日、断更 ≤2 次且有 AMENDMENTS 留痕；
- 每日 push 时间戳均早于 13:30 UTC（late 行单独统计）；
- resolution 全部按预先钉死的规则执行，零现场裁量；
- 评分可由第三方用公开数据+开源脚本复算。

**会使记录永久失去证据资格的缺陷（一旦发生不可补救）：**
1. push 晚于当日 cutoff 却未标 late（虚假时间戳性质）；
2. 修改历史行而无 AMENDMENTS 留痕 / force-push 重写历史；
3. resolution 来源或规则在结果已知后才选定（裁量后门）；
4. dry-run/合成数据混入 forecasts/ 或 resolutions/ 目录。

## 5. 合规/安全审计

- **投资建议风险**：schema 无建议语义、零交易、免责声明三层（文件 _meta、
  README、协议）→ 设计层面已隔离；最终定性等 attorney 意见（问题清单已备好）。
- **自动交易暗示**：无网络、无券商、无订单字段、validator 主动封堵——
  代码强制而非口头承诺 ✓。
- **公开前提**：attorney（至少）回复之前不公开——维持 FOUNDER_MANUAL_ACTIONS
  第 5 节纪律。**判定：维持私有。**
- **独立私有 repo**：**建议是**——本 repo 是公开博客站源（GitHub Pages），
  混放增加误公开面；且独立 repo 的 push 历史更干净，利于将来整体公开
  作为审计证据。迁移成本 ≈ 复制 `ledger/` 目录 + git init。

## 6. Findings 汇总

### Critical findings
1. **审计对象缺席**：真实 forecasts 文件不存在，真实记录数 0。
2. **`late` 硬编码 false**（§1.3）——首日 commit 前必须修。
3. **Resolution 规则两处歧义未钉死**（§3）——非交易日规则、EURUSD 收盘定义。
4. **时间戳证据=push 而非 commit**（§1.1）——执行习惯必须按此校正。

### Required fixes before day 1 commit（R1–R3）
- **R1**：预登记操作定义改为"cutoff 前完成 commit **并 push**"；
  README runbook 第 1 步补 `git push` 并注明 13:30 UTC cutoff。
- **R2**：在协议追加一节《Resolution 规则（预先钉死）》：
  (a) 非交易日顺延至下一交易日收盘，horizon 含义不变；
  (b) EURUSD 指定单一公开来源+固定时点的日频价并写明；
  (c) 每个标的的 realized 数据来源表。**此节必须在首条预测 push 之前入库。**
- **R3**：`make_forecast.py` 的 `late` 改为对照 13:30 UTC cutoff 计算
  （date 当日 cutoff 之后生成则 true）。一行逻辑+一个测试，不碰预测数学。
  （按审计纪律本会话不实施；spec 已写清，Codex 10 分钟任务。）

### Nice-to-have（不阻塞）
- N1：导出独立 JSON Schema 文件供第三方核验。
- N2：远端保护（禁 force-push）或定期向第三方时间戳服务锚定。
- N3：τ 集合抽共享常量。
- N4：resolution 时快照 VIX regime 标记。

## 7. 首条真实记录的待执行终审清单（文件路径提供后执行）

```bash
# A. schema 终审
python3 ledger/scripts/validate_ledger.py <真实文件路径>          # 必须 PASS
# B. 内容核对（人工/Fable 5）
#   - protocol_version == "1.0"（不是 -dryrun/-manual 则按实际生成方式核对）
#   - 10 ticker × 预期 source 数，行数对账
#   - late 字段与实际生成时间一致（对照 R3 修复后的逻辑）
# C. 时间证据
git log --format='%cI %h' -1 -- <真实文件路径>                    # commit 时间
#   远端核对：push 是否在 date 当日 13:30 UTC 之前（PR/分支 API 或 push 输出留存）
# D. 终判
#   A–C 全过 → PASS：记录获得 calibration receipt / L3-seed 资格
#   任一不过 → 该行/该文件标记缺陷，当日记录降级为流程演练，明日重来
#   （首日失败不是事故，是审计在工作；隐瞒才是事故）
```

## 8. Day 2 精确命令序列（R1–R3 完成后，每个交易日重复）

```bash
# ── 开盘前（≤13:30 UTC）──
python3 ledger/scripts/make_forecast.py --date YYYY-MM-DD --prices prices.csv
python3 ledger/scripts/validate_ledger.py ledger/forecasts/YYYY-MM-DD.jsonl
git add ledger/forecasts/YYYY-MM-DD.jsonl
git commit -m "Pre-register forecasts YYYY-MM-DD"
git push                       # ← 预登记在 push 成功的这一刻才完成
# ── 次日收盘后 ──
python3 ledger/scripts/score_day.py --forecasts ledger/forecasts/YYYY-MM-DD.jsonl --realized realized.csv
python3 ledger/scripts/validate_ledger.py ledger/resolutions/YYYY-MM-DD.jsonl
git add ledger/resolutions/ && git commit -m "Resolve YYYY-MM-DD" && git push
```

---

*Calibration research record. Not investment advice. 本审计不构成对任何
证券的评价，不包含任何交易建议。*

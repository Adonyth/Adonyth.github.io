# CODEX_TASKS_READY — 可直接复制派发的 Codex 任务包

> 使用方式：每个任务的 prompt 块**原样复制**给 Codex（独立会话）。
> 全部任务都是"spec 已锁死的纯执行"，不需要 Fable 5 级别的判断。
> 验收标准写在每个任务尾部，由 founder 花 ≤10 分钟/任务执行。
> 通用边界（每个 prompt 已内嵌）：不碰凭证、不连券商、不加 schema 外字段。

---

## C1 ｜ make_forecast_template.py

```
实现 scripts/make_forecast_template.py（Python 3.11+，只用 pandas/numpy/
yfinance 或等价公开数据库）。

功能：输入 --date YYYY-MM-DD，对以下 10 个标的：
SPY QQQ IWM XLE GLD TLT AAPL MSFT EURUSD=X ^VIX
1. 拉取截至 date 前一交易日的过去 60 个交易日收盘价（公开数据源，只读）。
2. 计算日对数收益序列（VIX 用水平值，不算收益）。
3. 生成两组预测分位数 [q05,q25,q50,q75,q95]：
   - B0-flat：q50=0（VIX 用最近收盘值），其余分位取 60 日经验分位数
   - B1-garch：EWMA(lambda=0.94) 波动率 + 正态分布分位数（均值 0；
     VIX 用最近值为中心）
4. 输出 forecasts/{date}.jsonl，每行 schema 严格如下，禁止增删字段：
   {"date":...,"ticker":...,"target":"log_return_next_close"（VIX 为
   "level_next_close"）,"source":...,"q05":...,"q25":...,"q50":...,
   "q75":...,"q95":...,"created_utc":<当前UTC ISO8601>,"late":false,
   "protocol_version":"1.0"}
5. 校验每行分位数严格单调递增，violation 则报错退出，不写文件。

约束：无任何网络写操作；无凭证；EURUSD 与 VIX 的 ticker 映射写成常量便于改。
交付：脚本 + tests/test_template.py（用合成价格序列测试分位数单调性、
schema 字段完整性、VIX 特例）。pytest 必须全绿。
```

**验收**：跑一次真实日期，肉眼核对 SPY 的 B0 行分位距与近期波动同量级；pytest 全绿。

---

## C2 ｜ score_day.py

```
实现 scripts/score_day.py（Python 3.11+）。

功能：输入 --date YYYY-MM-DD：
1. 读 forecasts/{date}.jsonl，拉取该日实际收盘（公开数据源），
   计算实现对数收益（VIX 为实现水平值）。
2. 对每行预测计算：
   a. CRPS 的 pinball 近似：对 τ∈{.05,.25,.50,.75,.95}，
      QL_τ = (indicator(y<q_τ) − τ)·(q_τ − y)，取平均。
   b. PIT bucket：实现值落入哪个分位段
      （"<q05","q05-q25","q25-q50","q50-q75","q75-q95",">q95"）。
   c. in90 = q05≤y≤q95；in50 = q25≤y≤q75。
3. 输出 resolutions/{date}.jsonl：
   {"date":...,"ticker":...,"source":...,"realized":...,
   "data_source":<行情源名>,"resolved_utc":<UTC ISO8601>,
   "scores":{"crps":...,"pit_bucket":...,"in90":...,"in50":...}}
4. 文件首行写一条 header 注释行（JSONL 注释用单独 meta 行）：
   {"_meta":"Calibration research record. Not investment advice."}

约束：append-only——若输出文件已存在则报错退出，不覆盖；无凭证；无网络写。
交付：脚本 + tests/test_scoring.py，必须包含一个手算可验的用例：
quantiles=[-2,-1,0,1,2], y=0.5 时逐 τ 的 pinball loss 手算值与代码输出一致。
```

**验收**：用 C1 的合成数据跑通；手工复核测试用例里那个 CRPS 数字。

---

## C3 ｜ validate_jsonl.py（schema 检查器）

```
实现 scripts/validate_jsonl.py：输入一个或多个 .jsonl 路径，逐行校验：
1. 字段集合与 forecasts/resolutions 两种 schema 之一精确匹配（不多不少；
   "_meta" 行豁免）。
2. 分位数严格单调递增。
3. date 与文件名一致；created_utc/resolved_utc 可解析为 UTC ISO8601。
4. ticker 在 10 标的白名单内；source 在 {B0-flat,B1-garch,M1-llm,H1-human} 内。
5. 禁止字段黑名单：任何包含 account/position/order/api_key/credential
   的键名直接 FAIL。
输出：每文件 PASS/FAIL + 违规行号与原因。退出码：全 PASS 为 0。
交付：脚本 + 含坏数据样例的测试。可作为 pre-commit hook 使用（附安装一行命令）。
```

**验收**：故意喂一行乱序分位数和一行多余字段，确认都被抓住。

---

## C4 ｜ Claims matrix → 外部 one-pager（机械整理）

```
读取 docs/strategy/fable5_sprint_2026_06/PUBLIC_CLAIMS_MATRIX.md 和
OMYTEA_EXTERNAL_STORY_PACK.md。

机械整理（不允许新增任何内容、不允许改写任何 claim 措辞）：
生成 docs/strategy/fable5_sprint_2026_06/EXTERNAL_ONE_PAGER_DRAFT.md，
结构：
1. 一句话版本（story pack 第 1 节原文）
2. 30 秒版本（第 2 节原文）
3. "我们不是什么"三连（从 matrix 3.3 节禁止清单反向改写为
   "We do not claim..." 否定句式——这是唯一允许的机械转换）
4. 当前阶段声明（story pack 第 5 节"当前阶段"段原文）
5. 文末免责声明行

规则：每段标注来源文件与节号；任何你想"优化"的冲动 → 写进文末
SUGGESTIONS 区供人审，不得直接改正文。[VERIFY-LOCAL] 标记原样保留。
```

**验收**：diff 检查正文每句都能在源文件找到；SUGGESTIONS 区单独审。
**注意**：此 draft 仍需 Fable 5 按 P3 模板终审后才可外用。

---

## C5 ｜ Golf G1 数据源排查（桌面研究）

```
任务：排查"业余高尔夫球手逐轮/逐洞成绩数据"的获取路径，供 go/no-go 决策用。
逐项回答：
1. Arccos / Garmin Golf / 18Birdies / TheGrint 等 APP：用户能否自助导出
   自己的逐洞数据？格式是什么？是否需要付费档？
2. 公开业余比赛成绩（州/市业余赛、大学赛、俱乐部联赛）：哪些有公开
   results 页面？数据粒度到轮还是到洞？
3. USGA GHIN handicap 系统：第三方可获得什么粒度？
4. 估算：一个"球友自愿转发自己 APP 导出"的路径，每个球友每轮的数据
   获取摩擦有多大（步骤数）？
输出表格：来源 | 粒度 | 获取方式 | 摩擦/成本 | 是否需要商务谈判。
最后一行给出判定建议：是否存在"无需商务谈判即可启动"的路径（是/否+依据）。
只做桌面研究，不注册付费账号，不爬取需登录的数据。
```

**验收**：表格每行有可点开核实的来源；判定行有依据。结果填入
GOLF_VERTICAL_DECISION_MEMO 第 8 节 G1 证据区（founder 签字确认 PASS/FAIL）。

---

## C6 ｜ report.py（7 日滚动报告，D7 前交付即可）

```
实现 scripts/report.py：输入 --start --end 日期范围，读 resolutions/*.jsonl：
1. 按 source 分组输出：平均 CRPS、相对 B0-flat 的 skill ratio、
   90%/50% 区间实际覆盖率、PIT 六段频数表。
2. PIT 直方图 PNG（matplotlib，每 source 一张）。
3. 输出 reports/{end}_weekN.md，文头固定写：
   "Sample size insufficient for statistical conclusions (<60 trading days).
   Process verification only. Not investment advice."
约束：只读 resolutions 文件；不拉外部数据；不输出任何"好/坏/跑赢"评价词。
交付：脚本 + 合成数据测试。
```

**验收**：合成完美校准数据 → PIT 接近均匀、coverage 接近名义值。

---

## C7 ｜ Civilization 源文件读取与填充（条件任务）

> **前置条件（缺一不发）**：AQ-1 至 AQ-6 全绿；且在**本机**会话执行
> （路径仅本机存在）。路径若不存在，记录原因后放弃,不要找替代品。

```
读取以下三个文件（只读这三个，不扫描目录）：
/Users/chenjiaxuan/Downloads/civilization-tech-path-research/00-MASTER-SYNTHESIS.md
/Users/chenjiaxuan/Downloads/civilization-tech-path-research/01-physical-path-verdicts.md
/Users/chenjiaxuan/Downloads/civilization-tech-path-research/02-startup-answer.md

然后完成 docs/strategy/fable5_sprint_2026_06/
CIVILIZATION_TECH_FRAMEWORK_PRODUCTIZATION.md 中所有【FILL】槽位。
规则：
1. 只做忠实提取与改写，禁止新增理论或维度；
2. 每个填充内容标注来源文件与位置；
3. 维度定义、判定、案例与源文件不一致处，以源文件为准；
4. 拿不准的槽位留空并标 [NEEDS-FABLE5]，不要硬填。
产出：填充后的文档。文章成稿不在本任务内（那是 Fable 5 的活）。
```

**验收**：抽查 3 个填充点与源文件原文对照；[NEEDS-FABLE5] 项移交 Fable 5。

---

## 不在本包内的任务（防误派发）

- Gate V10/V2 判读、claims 终审、对抗演练、决策签字 → Fable 5 / founder
- 任何涉及敏感文件（legal/、company/opt/、.env）的处理 → 不派给任何模型
- M1-llm 每日预测生成 → 等 C1–C3 验收后再启动（spec 另发）

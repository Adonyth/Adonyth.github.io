# OMYTEA_DEEP_RESEARCH_ROUND2 — Master Plan 全方位升级与查漏补缺

生成：2026-06-11 ｜ 第二轮 5 路并行调研（消费需求证据 / LLM-as-compiler
架构验证 / 非常规计算成色 / 资助与分发机器 / 防博弈设计），约 85 个
带置信度可证伪 claim。证据分级沿用：[V] 已验证 / [I] 推断 / [H] 待验证。
第一轮（OMYTEA_DEEP_RESEARCH_2026-06.md）回答"为什么和在哪里"；
本轮逐节检验 master plan 的技术与产品支柱，给出 §-级修订。

---

## 0. 执行摘要：五节五个判决

| Plan 章节 | 判决 | 一句话 |
|---|---|---|
| §7 LLM-as-compiler | **验证通过（带时限）** | 2025–27 的可靠性获胜配方；2030 后受 Bitter Lesson 威胁，需写明时限 |
| §9 World Console | **大众消费形态被证伪；改判 demo+利基+锦标赛** | 手动预测记录产品全线死亡，有效钩子只有三种 |
| §10 硬件可移植护城河 | **否决——装饰性论题,非战略护城河** | 全部底座原型期、无概率 IR、GPU 够用到 2030 |
| §12 学术价值捕获 | **强化且具体化** | 资助方有名有钱（Coefficient $8–10M RFP）、分发剧本有 23 个月先例 |
| 收据协议（新） | **获得 v1 安全规格** | 五大攻击向量 + 五件套最小防御，全部有制度先例 |

---

## 1. §9 World Console：需求证据判决

**死亡名单 [V]**：PredictionBook 2024-01 转只读（用户不足）；Fatebook
获 Open Philanthropy $1.1M 仍仅约 5 千活跃（5 万条预测/2.5 万问题）；
Quantified Intuitions 月访客 ~90；80% 移动 app 用户 30 天流失。
**根因 [I]**：个人决策的结果反馈回路 6–18 个月,撑不住注意力——
这正是 plan §15.5 effort-test 想测的东西,证据说默认结局是 fail。

**活着的三种形态 [V]**：
1. **锦标赛**：Metaculus×Bridgewater 1.7 万人（10 倍年增）;ACX 3 千+;
2. **被动采集**：Oura 200 万付费（$110M ARR）/ Whoop $3.6B 估值——
   $6–30/月成立的唯一条件是**零手动输入**;
3. **B2B2C 机构授权**（Metaculus/RAND 模式）。

**反面印证 [V]**：$3B 占星 app 市场（印度 49% CAGR）是娱乐需求——
plan §2.9.2 禁用算命词汇的 negative scope 被证明是先见,
那个市场的钱不可拿（拿了即品类自杀）。

**§9 修订建议**：World Console 保留为 substrate 演示面（plan 原文
本就如此定位,§9 开头的警告是对的）;**产品化路径改写**：
(a) 入口形态 = 校准锦标赛/比赛（有 3k–17k 参与先例,可挂在
WM-Receipts leaderboard 上）;(b) 个人工具 = 利基（全球 SOM 5–20 万
认真预测者）,freemium,不做大众增长指标;(c) Sean Ellis 40% 阈值
仅对利基人群测,对大众人群测必死且无信息量;(d) 删除 ChatGPT 类比
（第一轮已提,本轮证据加固）。

## 2. §7 LLM-as-compiler：架构赌注判决

**有利证据 [V]**：无约束 LLM 在企业级 NL→SQL 几乎全灭
（GPT-4o Spider 2.0 仅 10.1%,SOTA 系统 5.68%,vs Spider 1.0 的 86.6%）;
生产可靠性 70–85% 只在暴露受限"视图"时达成——**DSL 约束是可靠性的
必要条件**;AlphaGeometry 2（84% IMO）/AlphaProof/Aristotle/Leanstral
全部是"LLM 提议+符号系统验证"获胜;JetBrains Databao 靠结构化约束
拿下 Spider 2.0-DBT 榜首;LangGraph 把 2026 叫做"Stateful
Orchestration 之年"——**带状态真相源+LLM 接口正在成为标准模式**,
你 2026-05-14 就 ratify 的 §7 走在了行业确认之前。

**威胁 [V/I]（研究员置信 70%）**：RLM/递归上下文管理 + AMI Labs
$1.03B 押注学习型世界模型——Bitter Lesson 阵营认为手工结构是
短期拐杖。判决：**赌注 2025–27 成立（75%）,2030 后存疑（<60%）**。

**§7 修订建议**：(a) 加一行时限承认："本架构赌注的验证窗口为
2025–2027;若 2027 后端到端模型在无约束条件下达到 Spider 2.0
50%+,§7 需重审";(b) 新增论文机会：研究员给出的"最小证明判据"
（同底座、同任务,结构化 vs 无约束,成功率差 ≥40%,可靠性随约束
收紧而升）正是一篇 substrate 实证论文的实验设计——纳入 §12
论文池（排 WM-Receipts 之后）。

## 3. §10 硬件可移植护城河：否决与诚实重写

**现实成色 [V]**：Extropic X0 是原型、Z1 未交付,10,000× 能效是
厂商自报无第三方验证;Normal CN101 流片后处表征期,$50M A 轮
（2026-03）;神经形态最实在但极小（BrainChip 年收入 $1.89M;
全球神经形态商业收入 ~$50M）;D-Wave 是唯一有真实商业牵引的
非常规底座（314% 用量增长、100+ 客户）;Gartner 共识:主流化在
**late 2020s**。

**结构性否决 [I]（研究员论证充分）**：(a) 不存在跨底座的"概率
IR"——p-bit Gibbs ≠ 神经形态 spiking ≠ 量子退火,移植是研究项目
不是配置切换;(b) 每个底座只解窄问题,组合不成可移植运行时;
(c) GPU 对概率推断"够用"至 2030;(d) **可移植性护城河只属于
拥有移植层的人——而那个层不存在,也没人宣布要做**。

**§10 修订建议（替换"primary moat"表述）**：
- 降级语言："substrate portability 是**研究兴趣与远期对冲**,
  不是当前护城河;Omytea 不声称 substrate-agnostic——为新底座
  移植是 O(weeks) 研究而非 O(days) 配置。"
- 加 go/no-go gate（研究员起草,直接可用）："若 2027 Q3 前没有
  任何非常规底座在概率推断工作负载上出货 >1M units 或年收入
  >$10M,全部降为 research-interest 状态。"当前可证伪成功判据
  0/6。
- **保留的真护城河重述**：§10 的真实价值不是跨异构底座,而是
  "算法层对采样硬件的亲和设计"（Lindblad/Gibbs 到 p-bit 的映射
  文献存在 [V]）——这是论文素材,不是商业护城河。
- 微正面：若未来非要选一个底座关注,D-Wave（已去险）短期、
  p-bit 长期条件性关注（Z1 2027–28 基准为触发器）——零预算
  watch-and-wait。

## 4. §12 + 分发：从抽象策略到具名路径

**资金路径 [V]**：
- **首选**：Coefficient Giving "AI for Forecasting and Sound
  Reasoning" RFP——$8–10M 池,单笔 $100K–$1M,8–12 周周期,
  scope 与 WM-Receipts/收据协议完美重叠;
- **并行**：EA Funds LTFF（$50–150K,4–6 周,epistemics 优先）;
- **基础设施**：NumFOCUS 财政托管 + Small Development Grants
  （$10K）;GitHub Sponsors 做长尾;
- **先例锚**：Open Philanthropy 已给 FRI 同类项目 $1.65M+
  （含 ForecastBench $100K）——你申请的是一条**已被验证的资助
  谱系的下一个空位**;
- 12 个月现实栈估计：$150–350K。[I]

**分发剧本 [V]**：LMArena 2 人学术项目→23 个月→$1.7B 估值;
NeurIPS D&B track 接收率 25.3%（约 500 篇/年）;benchmark 成为
引用标准的 12–36 月路径已拆解为可证伪里程碑（月 2–4 投会、
月 4–6 上 leaderboard 并拉 3–5 家模型厂提交、月 12 出现于 50+
论文）。

**立即行动项 [V]**：arXiv 2026-01-21 收紧 endorsement（需机构
邮箱+发表记录,或既有作者背书）——**founder 需要提前锁定 1–2 位
endorser**（cofounder PhD 网络是天然来源）,进 FOUNDER_MANUAL_ACTIONS。

## 5. 收据协议 v1 安全规格（新增,填补 plan 空白）

**攻击向量证据链 [V]**：ClinicalTrials.gov 被 62% outcome-switching
博弈且期刊拒绝执行（COMPare 58 封信仅 6 发表）;Chatbot Arena 被
Meta 27 个私测变体刷榜;Polymarket UMA oracle 被 25% 投票权操纵
$7M 合约;git commit stomping 是已知攻击（印证 Phase 4 审计的
push-not-commit 结论）。

**v1 必须随身携带的五件套 [I,源自制度先例]**：
1. append-only 账本 + 外部锚定（防事后改写——最致命向量）;
2. 密码学预提交（hash-lock,防时间博弈;RFC 3161 v1 够用,
   OpenTimestamps v2 升级）;
3. 身份成本（防 Sybil 刷履历"注册一千号删输家"——staking/
   实名分层/最低账龄）;
4. baseline-relative 计分 + 题目权重（防 cherry-picking 简单题——
   B0 基线已在 ledger 设计中,获得理论确认）;
5. 提交限速 + holdout（防探测过拟合）。
**可推迟到 v2+**：Sybil 图分析、多签 oracle、DAO 治理、动态难度
加权。

**设计哲学收获 [I]**：ClinicalTrials.gov 的教训不是"registry 没用",
而是"registry 使博弈**可检测**"（outcome switching 之所以有 62%
这个数字,正因为 registry 留了痕）——收据协议的卖点措辞应为
"make gaming detectable",而非"make gaming impossible"（后者是
过度声明）。

---

## 6. 汇总：本轮触发的 master plan 修订（amendment 草稿补充条款）

```markdown
## H. §10 修订（本轮新增）
"substrate portability"从护城河降级为远期对冲。删除 §10 开头
"one of Omytea's primary moats"表述,替换为 watch-and-wait 框架
+ 2027 Q3 go/no-go gate（判据：任一非常规底座在概率推断负载上
>1M units 或 >$10M 年收入;当前 0/6 成功判据达成）。
真护城河重述：收据纪律的时间累积 + 开源可验证 + 标准定义权
（§2.6 修订一致）。

## I. §9 修订（本轮新增）
World Console 产品化路径锁定三形态：校准锦标赛（入口）、
利基个人工具（SOM 5–20万,freemium）、B2B2C（远期）。
大众消费目标移除;Sean Ellis 测试限利基人群;娱乐化/算命化
方向维持 §2.9.2 硬禁。

## J. §7 修订（本轮新增）
加时限条款：架构赌注验证窗口 2025–2027,重审触发器 =
端到端模型无约束达 Spider 2.0 50%+。
新增论文候选："结构化约束 vs 无约束 agent"实证研究
（最小证明判据见 ROUND2 §2）。

## K. 协议安全条款（本轮新增）
收据协议 v1 随附五件套防御（见 ROUND2 §5）;
对外措辞规范："make gaming detectable",禁用
"tamper-proof / gaming-impossible"级别表述。

## L. 资助与分发执行（本轮新增）
30 天内：Coefficient Giving RFP 申请材料启动 + EA Funds LTFF
并行 + arXiv endorser 锁定。WM-Receipts 分发按 LMArena/
ForecastBench 剧本的 12–36 月里程碑执行。
```

## 7. 待验证清单（并入 backlog）

1. Extropic Z1 / Normal CN201 第三方基准（2027–28 触发器）。[H]
2. Coefficient Giving RFP 当前是否开放申请窗口与具体要求。[H]
3. Fatebook/Metaculus 用户数字的二次核验（单源 Medium 置信）。[H]
4. RLM/递归上下文管理的 Spider 2.0 表现追踪（§7 重审触发器）。[H]
5. Bridgewater×Metaculus 锦标赛的商业条款（B2B2C 模板参考）。[H]

## 8. Sources（本轮新增,按节分组）

**§1 消费**：GitHub (PredictionBook read-only)；EA Forum (Fatebook,
Quantified Intuitions)；Manifund (Sage $1.1M)；ACX (竞赛数据)；
Metaculus (Bridgewater)；Nasdaq (Samotsvety)；Yahoo/MarkNtel
(占星市场)；Fortune (Oura)；FMI (журnaling)；Appcues (留存)。
**§2 编译器**：spider2-sql.github.io；Promethium (企业 NL→SQL)；
arXiv 2502.03544 (AlphaGeometry2)；DeepMind (AlphaProof)；arXiv
2510.01346 (Aristotle)；Mistral (Leanstral)；JetBrains (Databao)；
PrimeIntellect (RLM)；CallSphere (LangGraph 2026)。
**§3 硬件**：Vastkind/VKTR (Extropic)；Nature Comms (Camsari)；
PRNewswire/SiliconAngle (Normal $50M)；Intel (Hala Point)；IBM
(NorthPole)；Yahoo/SmallCaps (BrainChip)；D-Wave 新闻室；Gartner
2026 trends；arXiv 2601.16154/2302.06457 (Lindblad/p-bit 映射)。
**§4 资助分发**：OpenPhilanthropy grants 页（FRI 各笔）；
CoefficientGiving (RFP)；Bloomberg/Founded (LMArena)；OpenAI
(SWE-bench Verified)；CRFM (HELM)；NeurIPS blog (D&B 25.3%)；
arXiv blog 2026-01-21 (endorsement)；NumFOCUS；EA Funds。
**§5 防博弈**：PMC (COMPare/outcome switching)；arXiv 2504.20879
(Leaderboard Illusion)；The Register (Llama 4)；arXiv 1803.04585
(Goodhart 分类)；Metaculus scoring 文档；Orochi/RocknBlock
(UMA/Polymarket)；Humanode (Sybil)；Metaspike (RFC 3161)；
zsec.uk (commit stomping)；GitTrustedTimestamps。

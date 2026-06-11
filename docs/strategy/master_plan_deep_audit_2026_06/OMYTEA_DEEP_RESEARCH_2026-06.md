# OMYTEA_DEEP_RESEARCH_2026-06 — 文明尺度的思想地基与战略纵深

生成：2026-06-11 ｜ 方法：5 路并行深度调研（信任基础设施史 / 预测科学
制度史 / 世界模型评测空白 / AI 认识论危机 / 开源价值捕获），
约 80 个带置信度的可证伪 claim，全部带来源。
证据分级：**[V]** 已验证（≥2 独立来源或跨路互证）｜ **[I]** 合理推断 ｜
**[H]** 待验证假设。完整来源见文末。

---

## 0. 执行摘要：一个比"会计制度"更深的论题

此前的审计把 Omytea 类比为"预测的会计制度"。深度调研把这个类比
**升级为一个有日期、有机制、有窗口期的历史定位**：

> **信任基础设施的制度化时滞正在指数级压缩：复式记账用了约 500 年
> （1299→19 世纪），同行评审约 308 年（1665→1973），信用评级 66 年
> （1909→1975），临床试验预注册只用了 5–7 年（2000→2005/2007）。[V]
> AI 预测的"预注册时刻"正在被三个强制函数推向 2027 年：保险定价
> （已开始）、采购合规（2027）、benchmark 污染危机（2027–28）。[I]
> 当强制到来时，成为基础设施的是"当时已经存在的那个 registry"——
> ClinicalTrials.gov 在 ICMJE 强制（2005）之前五年就建好了。
> AI 预测领域今天还没有那个 registry。这就是 Omytea 的位置，
> 和它的截止日期。**

---

## 1. 五大发现

### 发现一：信任层制度化的三条铁律（历史路）

1. **时滞压缩律 [V]**：记账 ~500 年 → 评审 ~308 年 → 评级 66 年 →
   临床预注册 5–7 年。压缩条件：守门人（期刊/监管者）在激励被腐蚀
   **之前**入场。临床案例的精确时间线：ClinicalTrials.gov 2000-02 上线
   （FDA Modernization Act 1997 要求）→ ICMJE 2005-09 把注册定为
   发表前提 → FDAAA 2007 联邦立法（罚则 $10k/天）。
2. **腐蚀律 [V]**：验证者不承担错误成本时，系统在 30–100 年内滑向
   欺诈——issuer-pays 毁了评级（2008：Moody's 对 $869B RMBS 评 AAA,
   后降级 83%，和解 $864M）；咨询收入毁了审计独立性（Enron/Andersen:
   审计费 $25M vs 咨询费 $27M）；无偿评审造成长期供给不足。
3. **价值流向律 [V]**：发明者几乎从不获利（Pacioli、Crockford、Gruber
   分文未取）；价值被**强制时刻在场的执业层/聚合层**捕获（ICAEW 借
   《The Accountant》塑造了 1900 公司法——职业团体反向俘获立法）。

**对 Omytea 的结构性启示 [I]**：①不要做 issuer-pays（被审计者付费
评分=评级业的死亡基因）；②信任来源选"开源可复算"而非"机构中立"——
这是六个案例里唯一没有腐蚀先例的机制（度量衡标准从不腐蚀,因为
测量本身可复现）；③要在强制时刻到来时**已经是那个 registry**,
而不是到时再建。

### 发现二：超预测为什么没有变成基础设施（预测科学路）

- 校准科学完备已 75 年：Brier 1950 → Good 1952 → McCarthy 1956 →
  Savage 1971。[V] 天气预报是唯一制度化校准的领域（即时可验证 +
  单一主管机构 NWS 强制 + 准确性直接降低伤亡成本）。[V]
- 超预测被验证 15 年：IARPA ACE（2011–15）GJP 胜出 35–72%,
  超有密级情报的分析员 30%+；HFC（2019）再胜 20%。[V]
  但 Good Judgment Inc.（2015 商业化）至今是利基咨询。[V]
- 预测市场 2025 年爆发（Kalshi ~$50B 年化、与 Polymarket 合计占
  97.5% 市场）**但两家都不发布校准统计**——爆发由体育博彩流动性
  驱动,不是校准需求。[V] Manifold 衰退至 886 日活、Metaculus 无
  商业模式。[V] "认证预测师"职业不存在。[V]
- **三个结构性原因 [I]**：①验证与组织激励冲突（追踪校准=制造问责,
  威胁专家等级制）；②准确≠可行动（客户买的是为既有决策背书的
  风险量化）；③缺立法/责任框架使校准成为风险管理义务。
- **窗口为什么现在打开 [I]**：Tetlock 缺的那个"责任框架"正在 AI
  侧形成（见发现四）。超预测教训的反面就是 Omytea 的正面：
  **不卖准确性，卖风险管理的合规凭证。**

### 发现三：世界模型评测的制度空白（学术路，对 Omytea 最关键）

- **[V] 没有任何主流世界模型（V-JEPA2/Genie 3/Cosmos）被以校准
  概率方式评分于真实未来事件**（96% 置信,跨 3 个 survey 验证）。
  全部用视觉保真度/下游任务指标,且视觉指标与具身任务表现脱节
  已被 RoboWM-Bench/WorldArena 量化证明。
- 8+ 个世界模型 benchmark 在 2024–26 涌现,无统一标准,全部用
  启发式指标——**没有 time-decay 校准曲线,没有 coverage 保证,
  没有 CRPS。**[V]
- 最接近的占位者只覆盖 LLM 离散事件：ForecastBench（ICLR 2025,
  超预测者 Brier 0.081 vs GPT-4.5 0.101,预计 2026 底持平）、
  Metaculus FutureEval（2026-02 上线）。[V]
- conformal prediction 文献 2020 后爆发（50+ 篇/年）,刚开始触碰
  世界模型（C³, 2025-12）,但远未成为评测标准。[V]
- **[V] HQMM/量子认知文献在 ML 界休眠**：与世界模型文献零交叉
  引用。实用获胜路径是经典 conformal + CRPS + 温度缩放,
  不是量子形式主义。
- **研究员判定 [I]**："校准的纵向世界模型评分"（给定帧 1–10,
  以校准不确定度预测帧 11–50,报告 90% 预测集的实际覆盖率,
  按时间地平线画衰减曲线）是**最少被研究、最高影响、小团队
  2–3 人年可以拥有**的空白。先发者定义未来 2–3 年的评测规范。

**对 Omytea 的含义 [I]**：这是 substrate（T-A）与收据论题的天然
聚点——你的 ρ/conformal/校准技术栈正好是做这个 benchmark 的工具箱;
而 benchmark 论文正好满足 §12 "papers in flight" 义务。
量子线的诚实定位获得外部确认：formalism 可发表（理论联系）,
但绝不能 gate 实用路线。

### 发现四：强制函数正在到来,有日期（市场路）

- **保险（最早,已在发生）[V]**：Armilla（Lloyd's coverholder）
  2026-01 融资 $25M,AI 责任险保到 $25M,**模型验证+持续监控服务
  直接进入保费定价**；AIUC 保 AI agent 损失至 $50M。金融监管
  （FDIC/SEC/FINRA/OCC/NYDFS）已把缺失 AI 审计轨迹按
  books-and-records 违规处理。
- **采购/合规（次之）[V]**：EU AI Act GPAI 义务 2025-08-02 生效,
  高风险系统义务 2026-08-02；Colorado AI Act 2027-01-01（要求
  model cards+性能评估方法文档）；美 2025-12-11 行政令指示 FCC
  90 天内定联邦 AI 披露标准。
- **污染危机（加速器）[V]**：MMLU 类基准污染普遍（清洁集上掉
  13–16 分；多语基准泄漏最高 91.8% [单源,待核]）；"污染是默认
  假设"成为 2026 共识;机构转向私有评测（Scale SEAL、LiveBench,
  Confident AI 称 50%+ 财富 500 采用 [单源,待核]）。
- **汇合点推断 [I]（研究员置信 82–88%）**：三函数 2027 Q3 前后
  汇合——届时"签名的、带时间戳的预测记录"将成为事实市场标准,
  早于美国综合立法（2028–29）。
- **诚实的反面 [H]**：以上时间表是从单源行业报道+监管文本推断的;
  保险条款是否真的要求"预登记式"记录（而非事后日志）待逐条核验。

### 发现五：价值捕获菜单（开源路）

- **[V] 纯 spec 不变现**：JSON/Markdown/RSS 作者从标准本身收入≈0。
  价值在下游：托管层（Elastic Cloud）、服务层（SmartBear SaaS、
  PyMC Labs 咨询）、治理层（品牌控制）。
- **[V] substrate 创始人的四种结局**：平台收编保自治（Gerganov→
  HuggingFace 2026-02,三年走完）；公司化（Oliphant→Anaconda $24M
  A 轮,多轮稀释后离任）；咨询所（PyMC Labs）；纯学术+基金会
  （QuTiP→维护者去了 Rakuten/IBM-Q；Stan→Flatiron/Columbia）。
  警示极：60% 维护者无偿,46% 倦怠,Hunter（Matplotlib）终生未变现。
- **对 OPT 阶段 solo founder 的现实菜单 [I]**：协议+参考实现开源
  建权威（=门票,非收入）；收入设计在**审计/合规服务层**
  （"评分协议免费,签名审计包收费"——恰好对接发现四的保险/采购
  需求）；保留 Gerganov 式被收编为退路而非耻辱。具体雇佣/自雇
  形态的边界归 DSO/attorney 清单。

---

## 2. 大综合：Omytea 在 10–50 年弧线中的位置

把五路证据叠在一张时间轴上：

```
1299 复式记账发明 ──(500年)── 19世纪 制度化
1665 期刊创立 ──(308年)── 1973 强制评审
1909 评级发明 ──(66年)── 1975 NRSRO ──(33年)── 2008 腐蚀爆雷
1950 Brier ──(61年)── 2011 IARPA ACE ──(至今)── 未制度化（缺责任框架）
2000 ClinicalTrials.gov ──(5年)── 2005 ICMJE ──(2年)── 2007 联邦立法
2024-26 AI 预测泛滥 + 污染危机 + 保险入场 ──(推断 1-2年)── ~2027 Q3
                                            强制函数汇合
                  ▲
                  │ Omytea 必须在这个区间内
                  │ 成为"已经存在的那个 registry"
```

**位置判定**：Omytea 不是在发明一个新品类,而是在一条有 700 年
历史、正在指数压缩的制度化曲线的**下一个拐点前**就位。它的三重
身份在这条弧线上各有先例：
- **registry**（ClinicalTrials.gov 之于临床试验）——收据账本；
- **标准方法**（Brier/NWS verification 之于天气）——开源评分协议；
- **第一个敢被评分的建模者**（天气预报员是唯一天天被校准的职业,
  也因此是唯一保住公信力的预测职业）——世界模型 substrate。

**为什么 Tetlock 没做成而现在能做成**：超预测缺的从来不是科学
（75 年前就完备）,是**责任框架**。AI 责任险和 AI 采购合规第一次
把"可验证预测记录"从美德变成成本项。卖美德没人买单,卖保费折扣
和采购通行证有人买单。

**为什么是 Omytea 而不是在位者 [I]**：eval 厂商（Scale/LiveBench/
Confident AI）做的是静态/私有评测,商业模式依赖保密——与"公开
可复算"结构性冲突；预测平台（Kalshi/Polymarket）靠博彩流动性,
无校准动机；模型厂商自审=运动员兼裁判。开源可复算+预登记+
纵向积累的位置,被所有在位者的商业模式各自排除。
（反例风险：Scale 类公司推出"signed eval receipts"产品线——
窗口期内最大的竞争威胁。[H]）

---

## 3. 对 master plan 终极目标的修正建议

### 3.1 北极星措辞获得历史纵深（替换抽象类比）

之前的 N2'（"敢被评分的世界模型"）保留,但内部版本 N5 升级为
有先例、有日期的版本：

> **"做 AI 预测时代的 ClinicalTrials.gov + 天气预报式校准纪律：
> 在强制时刻（~2027）到来之前,成为那个已经在运行的预登记账本、
> 那套开源可复算的评分协议、和第一个天天接受自己协议评分的
> 世界模型。GUWM 是这条路的远方——一个被收据铺出来的研究纲领。"**

### 3.2 Tier-0 修正：增加学术楔子的具体形态

T-A（substrate 收据化）获得一个具体的旗舰产出物——
**Calibrated World-Model Benchmark（工作名 WM-Receipts）**：
按时间地平线评测世界模型的校准衰减曲线与 coverage,
用 CRPS/conformal,数据集滚动收集、未来才 resolve（构造免污染）。
理由：①发现三证实空白且小团队可拥有；②满足 §12 论文义务；
③把 ρ/conformal 技术栈、收据论题、学术价值捕获三者拧成一股；
④是 ForecastBench 的视觉/世界模型对应物,先发可定义规范。
**这是本次调研建议的唯一一个新增工作项**,放入 T-A 而非新开轨道。

### 3.3 商业层定位修正（发现四+五的合流）

收入假设从"卖校准收据给 agent 团队"（Phase 4 D1 原版）精化为：
**"评分协议与 verifier 永久免费开源；收费的是签名审计包——
保险定价与采购合规所需要的那份带时间戳、可复算的证据文件。"**
买家优先级修正：保险生态（Armilla 类 + 被保企业）≥ 采购合规
≥ agent 团队自发需求。D1 访谈脚本相应加两问（保险/采购质询经历）。

### 3.4 量子线的最终安放

外部证据（HQMM 在 ML 休眠、conformal 是实用赢家）确认：
ρ-formalism 的位置是**理论论文线**（学术诚实地连接 HQMM 谱系,
正好是 §12 的一类 artifact）,实用评测与产品线全部走经典
conformal+CRPS。这与 plan 的"formalism 非性能声明"完全一致,
现在有了外部文献的背书。gate 制度不变。

### 3.5 风险登记（新增到 plan 风险节）

- 窗口期风险：强制函数若提前汇合而 Omytea registry 未就位,
  位置被 eval 在位者或新进入者占据（缓解：WM-Receipts 抢学术
  先发,registry 抢日历积累——两者都是今天就能动的）。
- 时间表风险：2027 Q3 汇合是推断（82–88% 为研究员自报,
  实际置信应打折）；若推迟 2–3 年,solo 运营的生存设计
  （ultra-lean+学术捕获）恰好是对冲。
- 单源 claim 风险：91.8% 污染率、Confident AI 财富500渗透率、
  保险条款细节等单源数字,对外引用前须二次核验（已标注）。

---

## 4. 待验证清单（进入 WEB_RESEARCH_BACKLOG）

1. Armilla/AIUC 保单条款是否要求"事前登记式"记录（vs 事后日志）——
   决定 3.3 商业假设的成色。[H]
2. EU AI Act Art.16-17 / Colorado SB24-205 文本中"性能评估方法
   文档"的具体粒度。[H]
3. 91.8% 多语污染率、Confident AI 渗透数字的原始出处复核。[H]
4. ForecastBench/FutureEval 的治理与数据开放度（合作 vs 竞争判定）。
5. MiroFish 事实细节（$4M/24h）外部复核（plan §2.7.1 引用前提）。

## 5. Sources（按发现分组,完整 URL 列表）

**发现一**：Market Histories (Pacioli)；MAA (Manucci 1299)；Wiley EHR
(英国采用史)；Wikipedia (Companies Act 1844/ICAEW/Big Four/Enron)；
Sage (ICAEW 俘获 1900 法案)；Britannica (SOX)；Royal Society
Publishing (Nature 1973)；PMC (评审制度化)；BIPM；Wikipedia ISO；
Wikipedia Moody's/NRSRO；Elgar (issuer-pays 1970/74)；Tavakoli
(2008 评级失败)；NLM (ClinicalTrials.gov 25 年)；NEJM (ICMJE 2005,
FDAAA Final Rule)。
**发现二**：SciRP/SciSpace (Brier 1950)；arXiv 2504.01781 (scoring
rules 史)；NOAA/NWS (verification)；Princeton UP (EPJ 2005)；
Shortform/GoodJudgment (ACE 结果)；IARPA (HFC)；U Iowa (IEM)；
Wikipedia/TIME (InTrade)；PRNewswire (Polymarket QCX $112M、CFTC
designation)；CFTC/Kalshi (DCM)；CoinDesk/KuCoin (volume)；
Wikipedia (Manifold)；Metaculus；IBF (CPF)。
**发现三**：arXiv 2506.09985 (V-JEPA2)；DeepMind (Genie 3)；arXiv
2512.01989 (PAI-Bench)；arXiv 2604.19092 (RoboWM-Bench)；arXiv
2602.08971 (WorldArena)；arXiv 2603.25887 (World Reasoning Arena)；
arXiv 2410.05203 (Beyond FVD)；arXiv 2409.19839 + forecastbench.org
(ForecastBench)；arXiv 2507.04562 (LLM vs 超预测者)；Metaculus
FutureEval；arXiv 1710.09016 + PMLR (HQMM)；Quantum journal
(Riechers)；Cambridge (量子认知)；arXiv 2512.05927 (C³)。
**发现四**：llm-stats/arXiv 2605.19999 (污染)；arXiv 2506.21614
(LastingBench)；VentureBeat (LiveBench)；Scale (SEAL)；Gartner
2026-04-07；Nemko (EU AI Act GPAI)；Kognitos (审计轨迹清单)；
ALM (Colorado)；FinTech Global (Armilla $25M)；aistandardofcare
(AIUC)；fin.ai (金融监管)；NIST AI RMF；Sidley (2025-12 行政令)；
C2PA viewer/SoftwareSeni；Bulletin (学术 AI 渗透 13.5%)。
**发现五**：Simon Willison (ggml→HF)；Sifted/TechCrunch (Probabl)；
NumFOCUS (Stan/PyMC/John Hunter)；Unitary Foundation (QuTiP)；
PyMC Labs；Driverless Crocodile (Crockford)；Daring Fireball
(Markdown)；SmartBear (OpenAPI)；Socket.dev (Redis/Valkey)；
WebProNews (维护者倦怠)；Wikipedia/Quansight (Oliphant)。

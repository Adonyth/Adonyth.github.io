# MASTER_PLAN_INTERPRETATION v2 — 基于原文的理解（取代 v1 推断版）

> 依据：`OMYTEA_MASTER_PLAN_latest_final_20260610.md` 全文（已读）。
> v1 的 [INFERRED] 推断已由 AUDIT_VERIFICATION_2026-06-10.md 逐条核验。

## 1. 你到底在做什么（七个版本）

### 一句话版（忠实于原文 §1+§2.7.1 的合并）
> Omytea 是一个用密度矩阵（ρ）信念态做"校准多未来预测"的流式现实
> 世界模型，其运营铁律是：**预测不稀缺，证明才稀缺——做那个敢被
> 评分的预测者**，长期朝向 Grand Unified World Model 研究纲领。

### 一段话版
> 你在建一个原创架构的世界模型 substrate：观测流 → 状态向量 →
> ρ 信念态 → 算子代数演化 → 多分支预测 → 测量更新 → 校准修正。
> 量子信息是表示形式（formalism）而非性能声明（§1 注，HQMM prior art
> 已诚实承认）。LLM 是编译器不是真相源（§7）。价值捕获主路径是学术
> 发表+开源社区（§12，peer set 是 QuTiP/ggml 而非创业公司）。
> 消费产品 World Console 是 substrate 的演示面而非产品本体（§9）。
> 2026-06-02 起锁定的运营原则把一切产出物定义为"可分享的收据"——
> 因为 MiroFish 证明了生成"可信的未来"易如反掌，被评分的预测者
> 几乎不存在（§2.7.1）。

### 技术版
> 核心合同：`Observation → StateVector → BeliefState → ρ → OperatorGraph
> → Prediction → MeasurementUpdate`（§2.5，不可被外部世界模型替换）。
> 已有 L2/L3 资产（plan 自报）：Lindblad 动力学、张量网络、量子行走、
> p-bit 采样、密度矩阵 DB 查询、Query DSL。可移植性（CPU→量子硬件，
> §10）被定位为复利型护城河。

### 产品版
> 三层：①substrate（Apache 2.0，学术-社区采纳是其 PMF，§15.5 下表）
> ②World Console（Idea 阶段，gate=10 个 non-owner 访谈，§14.5）
> ③收据纪律产物（ledger/receipts——sprint 的产出在此层）。
> 危险的混淆是把 ②当成公司本体（§9 开头自己警告了）。

### 投资人版（注意：plan 本身不是融资导向的）
> 这不是一家典型创业公司——§2.7 明确对标 ggml/QuTiP/scikit-learn，
> §2.8 锁死 ultra-lean 模式，§12 说"发表即产品策略"。如果对投资人
> 讲，唯一诚实的版本是："深科技开源 substrate + 收据纪律，商业分支
> 是保留选项（§2.9 override 机制）而非默认路径。"

### 研究版
> GUWM（§4）是一个研究纲领：跨域统一的**计算协议**，不是物理终极
> 理论。进步形式包括算子库、统计规律、因果模型、可证伪校准记录。
> 论文管线（§12）有十类 artifact，每篇带 claim level 和复现包。

### 创始人内心版（v1 推断被原文部分证实，修正如下）
> v1 推断"你想做关于现实的总账"——半对。原文显示你想要的是**两者**：
> 既造预测现实的引擎（世界模型选手），又立"敢被评分"的纪律（收据）。
> 这不是错，但两个渴望需要一个明确的结构关系，否则就是双魂
> （AUDIT_VERIFICATION N1）。合题在 UPGRADE_PROPOSAL：
> **引擎是 Omytea 的，记分协议是世界的**。

## 2. 准确 / 危险 / 格局不够（基于原文逐条）

| 原文位置 | 说法 | 判定 |
|---|---|---|
| §2.7.1 | "the scarce thing is not the prediction — it is the proof. Be the one who gets scored." | **准确且卓越**——全 plan 最好的一句话，应升为公开第一句 |
| §1 | 一句话身份以 "quantum-information formalism" 开头 | **危险（对外）**：首句即 quantum 触发错误模式识别；内部准确（formalism 限定诚实），但第一接触面应换序（收据先、形式后） |
| §4 | GUWM 作为 research program | **准确（L0 合法）**——前提是永远带 "research program" 限定词；裸用 "Grand Unified" 对外是危险的 |
| §2.6 | "four-axis uncontested niche" | **格局虚胖**：17 玩家样本的空位≠护城河（N4）；可防御的是纪律+可移植性 |
| §2.7.1 | "proven-by-competitor's-absence" | 措辞越界：evidence ≠ proof（N5） |
| §9 | "first daily-life doorway… similar to how ChatGPT made LLMs visible" | **格局错位**：单人+$0 cloud 做消费级 ChatGPT 时刻是资源幻觉；§14.5 自己的 Idea-stage gate 是对的——执行层面尊重 gate 即可 |
| §12 | "publication IS the product strategy" | **准确但后果未被正视**：它和商业 wedge（sprint D1）是两种公司（N3），需要 founder 显式排序 |
| §2.9 | 七条 master negative scope | **准确且优秀**——与 sprint claims matrix 完全兼容 |
| §14 | 三段 roadmap 全宽度推进 | **格局过载**：诚实但不可执行（N2）；需要 Tier-0 脊柱 |
| §15.5 | Sean Ellis 40% 硬地板 + substrate-PMF 区分 | **准确**——执行它（10 个访谈）恰是 sprint 已排的事 |

## 3. 为什么值得做（基于原文+sprint 证据的合并答案）

1. **供给侧事实**：预测生成成本→0（MiroFish 一夜 $4M 而零校准，
   §2.7.1 [待外部核验]）。
2. **稀缺层论证**：被评分的预测者结构性稀缺——评分需要预登记纪律、
   时间成本、被打脸的勇气，三者都无法用算力购买。
3. **你的不对称优势**：约束即位置（§1 "convergence point"）——
   ultra-lean+学术-first+多后端，恰好是资本重玩家不愿占的位置。
4. **足够大吗**：作为"预测经济的记分协议+第一个敢被评分的世界模型"，
   它同时有学术纵深（GUWM 纲领）和制度纵深（收据标准）。够大，
   且大得诚实。

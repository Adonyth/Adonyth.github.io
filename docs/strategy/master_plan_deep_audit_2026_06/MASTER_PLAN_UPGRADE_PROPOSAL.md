# MASTER_PLAN_UPGRADE_PROPOSAL v2 — 基于原文的升级方案与 Amendment 草稿

## 1. 保留 / 删除 / 重写 / 新增（对照原文逐条）

### 保留（不动）
- §2.5 original-first doctrine、§2.9 七条 negative scope、§3 claim
  levels、§8 distillation 合法性框架、§11 dual-use gate、§13 IP 策略、
  §15.5 PMF 仪器区分——全部是高质量纪律，sprint 产物与之兼容
- §4 GUWM research program 表述（位置调整见下，文本保留）
- §2.7.1 操作原则全文——plan 最好的段落

### 删除
- §9 的 "similar to how ChatGPT made LLMs visible" 类比（V9'）
- §2.6 主表中 "uncontested" 一词（改 "unoccupied today"，N4）
- §2.7.1 "proven-by-competitor's-absence" 的 "proven"（改 "evidenced"，N5）

### 重写
- **§1 一句话身份的出场顺序**：收据原则升为第一句，quantum formalism
  降为第二句（全部诚实限定保留）——见 amendment §A
- sprint 主线措辞统一："我们不声称更准——我们声称被评分，
  且你可以复算"（解决与 plan 的双魂冲突）
- agent rule 10：从"不确定就修 plan"改为"不确定就跑最便宜的外部
  测试，拿着结果修 plan"（V2 共因修复）

### 新增
- §C Tier-0 脊柱规则（N2：活跃轨道 ≤2，其余 DORMANT）
- §D 证据棘轮（V2：无新外部事实不得修订）
- 开源记分协议章节（V1' 合题的制度化：schema+评分代码+verifier
  作为 substrate 的一部分 Apache 2.0 发布——这是 §2.7 peer-set
  打法在收据层的自然延伸）

### 升格 / 降级
- **升格**：finance ledger 每日运行（从可选 → "敢被评分"的第一份
  公开日常证据，§2.7.1 的字面实践）；10 个 non-owner 访谈（§14.5
  自己的 gate，全项目第一优先）；记分协议开源（O1，Tier-0 候选）
- **降级**：SpaceWorld、device profiles 全谱、WorldStudent 蒸馏、
  专利管线 → DORMANT（不删除，零对齐成本冻结）；World Console
  consumer 野心 → 严格按 §14.5 Idea-stage gate 执行（访谈前不 build）

## 2. Amendment 草稿（可直接粘贴进 docs/OMYTEA_MASTER_PLAN.md）

```markdown
---
# PLAN_AMENDMENT_2026-06-11 — Deep Audit 修订（待 founder ratify）
# 依据：docs/strategy/master_plan_deep_audit_2026_06/（v2 全件，
# 含 AUDIT_VERIFICATION_2026-06-10.md 的逐条核验）
# 冲突时本 amendment 优先；ratify 后录入 PLAN_CHANGELOG.md。

## A. 身份语序修订（§1 替换，内容不变、顺序重排）

新第一句：
"Omytea is the world model that gets scored: every prediction
pre-registered, baseline-scored, and reproducible by anyone —
because when AI can generate infinite futures, the scarce thing
is not the prediction, it is the proof."
新第二句（原第一句全部限定保留）：
"Under the hood it is a world model for streaming reality built on
a quantum-information FORMALISM (density-matrix ρ belief states;
representational choice, not a performance claim; prior art per
HQMM amendments), toward the Grand Unified World Model research
program (§4)."

双魂裁定：Omytea 是亮收据的选手，不是不下场的裁判。
记分层的可信度来源是开源可验证（任何人可复算任何分数），
不是机构中立性。对外材料相应统一为：
"We don't claim better predictions — we claim scored ones,
and you can recompute the scores."

## B. 对外词汇表（新增）

对外名词锁定：Omytea / world model / receipts（或 scored
predictions）。以下为内部代号，禁止出现在对外材料：
WMDB、OmyteaCompiler-LLM、OmyteaWorldStudent、SpaceWorld、
Founding Spine、Quantum-Core、GUWM 缩写（完整短语仅限研究语境
且必须带 "research program"）。

## C. Tier-0 脊柱规则（新增）

任意时刻活跃轨道 ≤2。当前活跃：
  T-A substrate 收据化：ledger 每日运行 + 记分协议（schema/评分/
      verifier）整理为 Apache 2.0 可发布形态;
  T-B console-MVP 访谈线：10 个 non-owner 访谈（§14.5 gate）+
      receipt 页最小对外形态。
其余 section（SpaceWorld、device 全谱、WorldStudent、专利、
console consumer build）状态为 DORMANT：零实现、零对齐、零修订。
唤醒 DORMANT 轨道需要：一条新外部事实 + 一条活跃轨道转入 DORMANT。

## D. 修订准入（证据棘轮，新增；并修订 Agent Rule 10）

plan 级修订必须在 changelog 引用 ≥1 条新外部事实（non-owner 访谈/
用户行为/外部数据/第三方反馈）。Agent Rule 10 修订为：
"When unsure, run the cheapest external test; amend the plan only
with the result in hand."
修订频率上限：每 30 天一次（外部事实触发的紧急修订除外）。

## E. 措辞修正（小项）

§2.6 "uncontested" → "unoccupied today, contestable at will;
the durable assets are the receipts discipline (time-accumulated,
non-backdatable), substrate portability, and open verifiability."
§2.7.1 "proven-by-competitor's-absence" → "evidenced-by-…"。
§9 删除 ChatGPT 类比句。

## F. 价值捕获决断排程（新增，不预判结论）

学术-社区捕获（§12 现行）与商业收据分支（§2.9.3 override 选项）
的排序决断：在 10 个访谈完成后 14 天内由 founder 作出并记入
changelog。决断前，禁止任何商业承诺性对外表述。
（涉及身份/签证与收入交互的部分以专业意见为准。）
---
```

## 3. 边界更硬 / 路线更大胆

- **更硬**：DORMANT 的定义（零对齐成本）；rule 10 修订；对外词表。
- **更大胆**：①把"每日被评分"做成公开节目（attorney 放行后 ledger
  公开 + 月度自审计报告）——没有竞品敢跟，因为他们没有预登记历史；
  ②记分协议抢先开源（标准先行，O1）；③civilization verdicts 作为
  最长时间尺度收据上线（O3）——三者都是 §2.7.1 原则的字面执行，
  不需要新理论、新基建、新人手。

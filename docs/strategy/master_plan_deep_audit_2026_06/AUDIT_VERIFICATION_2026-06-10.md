# AUDIT_VERIFICATION — 读取 master plan 原文后的核验修订

依据：founder 上传的 `OMYTEA_MASTER_PLAN_latest_final_20260610.md`
（2026-05-14 ratified，含至 2026-06-02 的 amendments）。
仍未读取：PROJECT_STATE.md、PLAN.md、PLAN_CHANGELOG、WORK_PLAN_V418 等
16 个文件——涉及它们的结论维持 [INFERRED]。

## 逐项核验

| 原审计结论 | 判定 | 原文证据 |
|---|---|---|
| V1：北极星 GUWM 与审计层定位自相矛盾 | **REVISED**（见下） | §1 vs §2.7.1 vs sprint 主线 |
| V2：计划递归病（418 版 vs 0 外部证据） | **CONFIRMED** | 文档本身的 amendment/ratification 密度；§14.5 所有 non-owner exit gate 未过 |
| V3：证据全自产 | **CONFIRMED（由 plan 自证）** | §14.5：console gate "≥1 friend Path α"未达、World Console 需"10 个 non-owner 访谈"未做、substrate "first external PR"未有 |
| V4：resolution 供给轻视 | **PARTIAL** | plan 关注校准纪律但确无供给侧章节 |
| V5：中立性无机制保障 | **REVISED**：plan 的路径是开源可验证（Apache 2.0 + reproducibility bundle §12），不是中立性——我的"永不预测"推论不适用 | §2.9.5、§12 |
| V6：合规循环未启动 | CONFIRMED（sprint 记录） | 不在 plan 文本内 |
| V7：命名蔓延 | **CONFIRMED 且低估了** | 原文含 Omytea/OmyteaCompiler-LLM/OmyteaWorldStudent/World Console/SpaceWorld/GUWM/ρ-substrate 等 |
| V8：单点 founder 依赖 | CONFIRMED | §2.8 自己写明 |
| "quantum 线=边缘研究应冻结" | **REFUTED（角色误判）** | §5：ρ-substrate 是核心状态表示，§14.5 列 L3 prototype 研究资产；prior art 诚实处理（§1 注、§2.6 ⚠scope） |
| "GUWM 必须删除" | **REVISED** | §4 把 GUWM 写成 research program（"computational protocol, not completed theory"）——作为 L0 是合法的；问题在公开第一句话的位置，不在其存在 |
| "civilization/golf/finance 角色判定" | 大体 CONFIRMED | finance ledger 与 §2.7.1 "be the one who gets scored" 完全同构——价值上调 |
| O1 receipt 标准玩法 | **STRENGTHENED** | §2.7 peer set（ggml/QuTiP/Stan 模式）正是标准+substrate 打法；O1 是 plan 自己逻辑的延伸 |
| O2 time-locked benchmark | STRENGTHENED | §12 论文类型表 + §2.7.1 receipts 原则的学术化 |
| O5 "世界模型当客户" | **REVISED** | plan 的立场是选手不是裁判；O5 改写为"同行评分协议"（互评而非仲裁） |

## 新发现（只有读了原文才能看到）

### N1 ｜ 双魂问题（取代 V1，升为 P0 之首）
§1 身份 = **造世界模型的选手**（"a world model for streaming reality…
toward a Grand Unified World Model"）；§2.7.1 = 选手必须带收据
（"Be the one who gets scored"）；而 sprint Phase 1 主线（founder 亲自
设定）= **裁判**（"我们不声称预测更准，我们做审计层"）。
裁判与带收据的选手是不同的生意、不同的叙事、不同的护城河。
两份文档都经 founder 批准，矛盾真实存在。**解法见 UPGRADE_PROPOSAL
的合题：'亮收据的选手 + 开源记分协议'——评分层不靠中立性获得信任，
靠开源可验证获得信任（任何人可复算），于是 Omytea 可以既下场又供分牌。**

### N2 ｜ 规模-产能倒置（新 P0）
§2.8 如实承认约束（单 founder、F-1、$0 cloud、async cofounder），
但 §9–§14 同时维持：consumer console、LLM compiler、WorldStudent 蒸馏、
device profiles（含卫星/BCI/船舶）、SpaceWorld、论文管线、专利管线。
这是 50 人实验室的议程。§14.5 的 stage mapping 是优秀的缓解装置，
但"staged"≠"dormant"——每个 section 都在持续产生对齐/修订工作
（V2 病的燃料）。需要 Tier-0 脊柱规则：活跃轨道 ≤2，其余显式休眠。

### N3 ｜ 价值捕获模式冲突（新 P1）
§12："publication IS the product strategy"，peer set 是 QuTiP/ggml
（学术-社区价值捕获）。而 sprint Phase 4 的 D1 wedge 是商业收据服务
（收入价值捕获）。两者都合法，但运营动作完全不同。plan 文本支持
学术-社区模式；D1 商业线若推进，按 §2.9 精神需要显式 amendment。
**这是 founder 必须二选一或排序的决策，本审计不代签。**
（注：身份/签证约束与收入模式的交互属 DSO/attorney 问题清单范畴。）

### N4 ｜ "uncontested niche" 论证强度不足（新 P1）
§2.6 的四轴无人区基于 13+4 玩家普查。样本内无人占位 ≠ 护城河；
plan 自己已对 ρ 轴做了诚实降级（HQMM prior art）。建议措辞从
"uncontested"降为"unoccupied today, contestable at will"；可防御的
部分是 §2.7.1 收据纪律 + §10 可移植性，不是位置本身。

### N5 ｜ MiroFish 论证的措辞越界（新 P2）
§2.7.1 "proven-by-competitor's-absence"——单个竞品的缺位是证据
（evidence）不是证明（proof）。原则本身（scarce thing is the proof）
极好，建议仅把 "proven" 改 "evidenced"。
另：MiroFish "$4M in 24h" 等事实待外部核验（已入 backlog）。

## 对本目录其余文件的影响表

| 文件 | 状态 |
|---|---|
| INTERPRETATION / VULNERABILITY_AUDIT / ULTIMATE_GOAL_REWRITE / UPGRADE_PROPOSAL / WORKSTREAM_ALIGNMENT_MATRIX | **已按原文重写（v2）** |
| GUARDRAILS | 维持有效；§3 反递归条款与 plan agent rule 10 的张力在 UPGRADE §D 处理 |
| MISSING_OPPORTUNITIES | O1/O2/O3 维持且强化；O5 按 N1 改读法（见本文件） |
| BETTER_THAN_CURRENT_PLAN | §1/3/4/6/7 维持；§2（D1 wedge）改为"待 N3 决策后生效" |
| V2_ROADMAP | 0–30 天维持；31 天后里程碑在 N3 决策后修订 |
| FABLE5_MASTER_PLAN_PROMPTS | MP-1 已由本文件执行完毕（限 master plan 本体）；其余维持 |

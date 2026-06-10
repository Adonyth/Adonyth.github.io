# FABLE5_MASTER_PLAN_PROMPTS — 后续 master plan 级 prompt 库

> 使用前提：MP-1 必须最先在**本机**跑（关闭本审计的最大缺口）。
> 全部继承：隐私边界、claims matrix、证据棘轮（GUARDRAILS）。

## MP-1 ｜ 审计落地核验（本机，最优先）

```
读取 docs/OMYTEA_MASTER_PLAN.md、PLAN.md、PLAN_ALIGNMENT_PROTOCOL.md、
docs/PLAN_CHANGELOG.md、PROJECT_STATE.md，对照
docs/strategy/master_plan_deep_audit_2026_06/ 全部 10 个文件：
1. INTERPRETATION 七版本逐节判定符合/冲突，修正 [INFERRED] 项；
2. VULNERABILITY 每条漏洞在原文中找证据或反证（V1 北极星表述原文
   照抄过来；V2 用 changelog 统计实际修订频率和触发原因）；
3. 输出 AUDIT_VERIFICATION.md：每个审计结论标 CONFIRMED / REFUTED /
   PARTIAL + 原文引用。只核验，不重写审计。
```

## MP-2 ｜ Master plan red-team

```
你扮演三个角色轮流攻击 MASTER_PLAN_UPGRADE_PROPOSAL 的 amendment 草稿：
①顶级 deep-tech VC 合伙人（动机：找"这不是生意"的证据）
②曾做过 Metaculus/Kalshi 高管（动机：证明在位者顺手就能做）
③冷静的你自己十年后（动机：找今天会后悔的承诺）。
每角色 5 个最强攻击 + amendment 文本层面的修改建议。
不许攻击稻草人：每个攻击必须引用 amendment 原句。
```

## MP-3 ｜ 相邻领域深查

```
对以下相邻领域各做一轮 web research + 与 Omytea 的关系判定（吸收/
合作/忽略/威胁）：①preregistration 生态（OSF/AsPredicted 的真实使用
数据）②forecasting 学术圈（Tetlock 谱系、IARPA 项目现状）③审计与
鉴证行业的数字化动向 ④AI 安全圈的 eval 基建 ⑤区块链 attestation
（EAS 等）。每个领域：他们已解决什么、未解决什么、Omytea 借什么、
被什么威胁。结论标 [WEB 证实]/[推断]。
```

## MP-4 ｜ Ultimate goal 辩论赛

```
就"N2（会计制度）vs N5（现实账本）哪个该对外"组织一场三轮辩论：
正方=N5 外用（更大叙事吸引同行者），反方=N5 永久内部（matrix 纪律）。
每轮引用真实约束（claims matrix 条款、融资场景、招聘场景）。
辩论后给裁决 + 一个折中方案的可行性评估（如 N5 只在招募 cofounder
的一对一深谈中口头使用）。
```

## MP-5 ｜ Product wedge 决策复核（访谈 ≥5 后）

```
读取 discovery/ 全部纪要 + WORKSTREAM_ALIGNMENT_MATRIX。按预登记的
判定标准（5 访谈 ≥2 pain 确认）判定 D1 假设状态。若证实：下一步
集中化方案；若证伪：启动 D2 plan B 的具体 14 天队列；若不充分：
设计第二批 5 个访谈的差异化抽样（不同 agent 品类/规模）。
判官模式，禁止"再看看"。
```

## MP-6 ｜ Technical moat 审计

```
对 BETTER_THAN_CURRENT_PLAN §4 的四层信任阶梯做工程与博弈双审计：
每层回答①伪造/绕过它需要什么成本②谁有动机③我们的检测手段
④该层被攻破后上层是否连坐。特别审计：自营 registry 与"中立"的
张力（我们自己能不能改自己的账？答案必须是可验证的不能）。
输出修补清单进 CX 任务包。
```

## MP-7 ｜ UI 对齐审计（CT-0 完成后）

```
读取 UI_CURRENT_STATE.md + amendment §A/§B。逐屏判定 console 与
web 模板：①是否出现内部代号（§B 违规）②是否有任何"我们预测"语义
（§A 推论 2 违规）③receipt 是否为第一类对象。输出违规清单 →
直接追加进 CURSOR_UI_REFACTOR_TASKS（带 P 级），不另写报告。
```

## MP-8 ｜ Research agenda 修剪

```
列出当前一切研究性活动（quantum gate、spine、O2 position note、
civilization verdicts、golf Paper A）。按 BETTER §7 的唯一合法研究
主题标准（机制本身）逐项判定：合法保留/改造后保留/gate 外冻结。
对每个"改造后保留"给出改造后的一句话研究问题。配额提醒：
年度版本号预算与文档配额（GUARDRAILS §3/§5）当前余额多少。
```

## MP-9 ｜ 90 天执行复核（9 月初）

```
读取 V2_ROADMAP 31–90 天节 + 全部 discovery/接入数据 + git log。
逐项对 Success/Kill criteria 判定。重点：①付费信号真伪（礼貌性
LOI 不算）②供给飞轮是否真自转（founder 推一把才动的不算）
③若触发 Kill：起草 pivot/persevere memo 框架（决断仍归 founder）。
判官模式。
```

## MP-10 ｜ Founder operating system 复盘（每月）

```
读取本月 daily_log + 周复盘 + git log。只回答：①"每日唯一必做"
完成率 ②founder 时间流向（访谈/验收/不可委派 vs 可委派工作的实际
比例）③哪条 guardrail 被触犯最多、是规则错还是执行错 ④下月唯一
要改的一个流程。≤20 行。禁止产生新任务清单——这个 prompt 的输出
只许做减法。
```

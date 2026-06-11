# FABLE5_NEXT_PROMPTS — 后续直接复制使用的 prompt 库

> 使用规则：本机会话用 FP-1（需读本机文件）；其余云端/本机皆可。
> 所有 prompt 默认继承边界：不读敏感文件、不越 claims matrix、不碰交易。

---

## FP-1 ｜ 现状盘点（本机，最先跑，关闭 SOURCE_GAPS）

```
读取 omytea-personal-console/ 全部 .py 文件、site/index.html、
marketing/landing.html、marketing/pitch.html、PROJECT_STATE.md。
对照 docs/strategy/fable5_sprint_2026_06/phase4_macro_landing/UI_UX_AUDIT.md
第 2 节的 H1–H15 假设，逐条判定命中/未命中并给代码位置证据。
同时输出：future_reality_ledger.py 与 ledger/scripts/models 的 schema 差异表。
更新 UI_UX_AUDIT.md（删除未命中假设，确认命中项），并把
docs/strategy/fable5_sprint_2026_06/ 全部 [VERIFY-LOCAL] 标记一次性核完。
只判定，不重构。
```

## FP-2 ｜ 竞品深查（D1 语境）

```
针对"AI agent 校准收据"定位做竞品研究：Langfuse、Maxim、Confident AI、
Respan、Braintrust、Patronus、Galileo，以及 Metaculus/Manifold/Good Judgment。
对每家回答：①是否有预登记+时间锁定机制 ②是否有跨时间校准履历
③是否第三方中立 ④买家是谁 ⑤定价。输出差异化矩阵 + "他们 3 个月内
复制我们需要什么"的诚实评估。结论区分 [WEB 证实] / [推断]。
更新 OMYTEA_STARTUP_DIRECTION_RESEARCH.md 的 D1 段。
```

## FP-3 ｜ UI red-team

```
你扮演三个连环角色攻击这套 UI 设计（UI_REDESIGN_SPEC + DESIGN_SYSTEM +
CT-1/2/3 产物截图）：①第一次点开 receipt 链接的怀疑型客户
②被要求接受审计的 agent 团队工程师（动机：找借口拒绝）
③合规律师（动机：找投资建议暗示）。每个角色给 5 个最尖锐的攻击点 +
界面层面的修复建议。不重写 spec，输出攻击清单 → 修复项进 CURSOR 任务包。
```

## FP-4 ｜ PRD critique

```
用三个标准批判 PRODUCT_REQUIREMENTS_DOC.md：①每个 v0 功能删掉会怎样
（删了无碍的列为 cut 候选）②"成功使用一次"的定义是否真的是价值时刻
③数据模型有没有为 v2 过度设计的字段。输出：cut 清单、保留理由、
修订后的 v0 范围。原则：v0 再小一半也可以，不许变大。
```

## FP-5 ｜ Buyer discovery 脚本（D1）

```
为"向客户交付 AI agent 的团队"写 30 分钟访谈脚本：开场 2 分钟
（research 定位，不 pitch）、背景 3 问、pain 探查 5 问（必含：
"客户质疑过你们 agent 的历史可靠性吗？那次对话发生了什么？"）、
现有方案 3 问、方案反应 2 问（只在对方主动问时展示 one-pager）、
willingness 试探 1 问（"如果存在 X，你们会怎么评估它"而非"你买吗"）。
全部开放式，禁诱导。附：访谈后 5 分钟自评清单。
```

## FP-6 ｜ Landing page copy 终审

```
用 PUBLIC_CLAIMS_MATRIX 的 P3 流程终审新 landing 文案（CT-4 产物）：
逐句标 claim 级别 vs 证据级别，输出判定表 + 修订稿。特别检查：
"tamper-evident" 是否被当前实现支撑（server-side 时间戳上线前降级为
"timestamped"）、CTA 是否暗示已有服务在运行、阶段诚实区块是否完整。
```

## FP-7 ｜ Pitch deck 重写大纲

```
读取 marketing/PITCH_DECK.md（本机）+ phase4_macro_landing/ 全部决策文档。
按"audit 层 thesis → D1 wedge → 机制证明（finance ledger 工具链+审计纪律）
→ 阶段诚实 → ask"重构 10 页大纲。每页：标题句（结论式）+ 证据点 +
claim 级别标注。投资人版 ask 槽位若仍空 → 停下来向 founder 要数字，
不许编。产出大纲先审，不直接做全稿。
```

## FP-8 ｜ Product demo script（90 秒）

```
基于已部署的 sample 链路（landing→receipt→track record）写 90 秒 demo
脚本：每 15 秒一个画面+一句话，旁白必须含三句：①"这张是 SAMPLE 数据"
②"我们不声称预测更准"③"现在是 concierge 阶段"。附：demo 后最可能被问的
5 个问题 + matrix 校准的回答。
```

## FP-9 ｜ Public/private release review

```
读取 CX-6 的 PUBLIC_PRIVATE_SPLIT_CHECKLIST.md + 待公开资产清单。
对每个"建议公开"项做发布前审查：①含个人信息？②含越级 claim？
③含金融数据（attorney 依赖）？④公开后撤回成本？输出每项
GO/HOLD/REDACT-THEN-GO 判定。任何拿不准的默认 HOLD。
```

## FP-10 ｜ 14 天 progress review（6/24 执行）

```
读取 phase4_macro_landing/ 全部文件 + discovery/TRACKER.md + git log
（6/11–6/24）。回答且仅回答：①5 个访谈的 pain 证据汇总——D1 假设
证实/证伪/不充分 ②30 天目标五项各自红黄绿 ③哪个 owner（Fable 5/Codex/
Cursor/founder）的产出最偏离计划，流程怎么改 ④v1 立项的证据是否充分
（不充分就明说，给"继续 concierge"的具体两周方案）。判官模式：
不为进度辩护。
```

## FP-11 ｜ 访谈纪要批量分析（访谈 ≥3 份后）

```
读取 discovery/ 下全部访谈纪要。提取：①原话级 pain 证据（引用+代号）
②现有 workaround 清单 ③出现 ≥2 次的反对意见 ④意外发现（我们没问
但对方主动说的）。禁止：把礼貌性兴趣计入 pain 证据。输出更新
OMYTEA_STARTUP_DIRECTION_RESEARCH.md D1 段的 evidence 小节。
```

## FP-12 ｜ Concierge 客户周报生成

```
输入：某 concierge 客户本周的登记/resolution JSONL。输出给客户的周报：
本周登记数、已决数、得分表、PIT 分布（n<30 带声明）、下周待决清单。
语气按 DESIGN_SYSTEM §2。硬性规则：无任何建议性语言；金融类 claim
带免责行；报告尾部固定"如何独立验证这些数字"一节。
```

# CIVILIZATION_TECH_FRAMEWORK_PRODUCTIZATION — 文明科技路径框架产品化

## ⚠️ 源文件读取状态：失败（记录在案）

按任务指令尝试读取以下文件，全部失败：

| 文件 | 失败原因 |
|---|---|
| `/Users/chenjiaxuan/Downloads/civilization-tech-path-research/00-MASTER-SYNTHESIS.md` | 路径位于本机，本次会话运行在云端容器，文件系统不可达 |
| `/Users/chenjiaxuan/Downloads/civilization-tech-path-research/01-physical-path-verdicts.md` | 同上 |
| `/Users/chenjiaxuan/Downloads/civilization-tech-path-research/02-startup-answer.md` | 同上 |

**因此本文件不包含任何框架实质内容**——复述未读过的研究等于编造，
违反本 sprint 的 claim discipline。

**本文件提供的是**：一套产品化骨架（文章结构、worksheet、评分模板的格式定义），
全部内容槽位标 `【FILL】`。在本机让 Fable 5 读取上述三个文件后，
用文末的执行 prompt 一次性填充，预计单次会话可完成。
此任务在 MASTER_PLAN 中排在 D4 晚启动、D5 全天执行。

---

## 1. 中文文章结构（目标读者：中文科技/创业社区）

1. **钩子**：一个反直觉的具体判定（从 `01-physical-path-verdicts.md` 选
   最颠覆常识的一条）【FILL】
2. **框架本体**：用 500 字讲清评估科技路径的核心维度
   （从 `00-MASTER-SYNTHESIS.md` 提炼，维度数量以原文为准）【FILL】
3. **三个判定案例**：每个 ≤300 字——路径名、常见叙事、框架判定、判定依据【FILL】
4. **对创业者的含义**（从 `02-startup-answer.md`）【FILL】
5. **自查邀请**：引导读者用 worksheet（第 3 节）评估自己的方向
6. **诚实的局限声明**：框架的失效场景【FILL：原文若无，让 Fable 5 对抗性生成后人工审】

长度目标：3000–4500 字。语气：判定要敢落锤，依据要可检查，禁夸大词。

## 2. 英文文章结构（目标读者：HN / 技术 Twitter）

> 不是中文版直译——英文读者对"framework"类文章免疫力更强，结构倒置：

1. **Verdict first**：开头三行给出 3 个最 spicy 的判定，不解释【FILL】
2. **The framework that produced them**：维度 + 判定规则，压缩到 600 词【FILL】
3. **One worked example**：完整走一遍评分过程（透明展示，可被攻击是特性）【FILL】
4. **Where this framework fails**：主动给出反例【FILL】
5. **Try it**：worksheet 链接

长度目标：1500–2000 词。

## 3. Worksheet 格式定义（一页，可打印/可表单化）

```
科技路径评估 Worksheet v0.1
─────────────────────────────
待评估路径：____________
一句话描述该路径承诺的终局：____________

维度评分（每维度 1–5 分 + 一行证据）：
  D1 【FILL：维度名 + 评分锚点定义（1 分长什么样，5 分长什么样）】
  D2 【FILL】
  ...（维度数量与定义严格取自 00-MASTER-SYNTHESIS.md）

红旗检查（任一命中则总分作废，直接判"叙事陷阱"）：
  □ 【FILL：从 01-physical-path-verdicts.md 的失败模式中提炼 3–5 条】

总分：___ / ___
判定：推进 / 观察 / 回避
本判定的最强反驳是什么：____________
```

**设计规则**：维度必须有评分锚点（否则人人打 3 分）；必须有红旗一票否决区
（防止加权平均掩盖致命缺陷）；必须强制写"最强反驳"（防止 worksheet 变成确认偏误工具）。

## 4. Startup direction scoring template

在 worksheet 基础上加三个创业特有维度（与框架维度分开计分）：

```
S1 时间窗口：该路径的关键瓶颈解除时间 vs 你的资金生存时间（1–5）
S2 个人杠杆：你/团队在该路径上有何不可复制的位置（1–5）
S3 验证成本：获得第一个 kill/continue 信号需要的资金与月数（1–5，越便宜越高分）
```

输出判定四象限：框架分高/低 × 创业分高/低 →
**做 / 写文章但不做 / 等待 / 既不做也不写**。
【FILL：用 02-startup-answer.md 的结论校准四象限的判定线】

## 5. 10 个可展示案例（格式定义）

每个案例固定四行，便于做成卡片/线程：

```
路径：____
流行叙事：____（一句话，引用常见说法）
框架判定：____（推进/观察/回避 + 总分）
一行依据：____（最致命的那一条，不是面面俱到）
```

案例选取规则【FILL 时执行】：
- 6 个取自 `01-physical-path-verdicts.md` 已有判定（直接改写，不新判）；
- 2 个选当下热度最高的路径（即使原文未覆盖，用框架现场评，标注"新判"）；
- 2 个选框架判定与主流共识**一致**的（防止全是逆主流判定，显得为反而反）。

## 6. 与 Omytea 主线的关系（防 scope 蔓延条款）

这条轨道是**独立内容资产**，不是 Omytea 产品线。允许的连接只有一个修辞桥：
"对科技路径的判定也是一种预测，也应该被登记和回头评分"——
文章发布即是一次公开预登记，框架判定可在未来被打分。
除此之外，禁止在本轨道上为 Omytea 添加功能性承诺。

## 7. 执行 prompt（在本机 Fable 5 会话中使用）

```
读取以下三个文件：
/Users/chenjiaxuan/Downloads/civilization-tech-path-research/00-MASTER-SYNTHESIS.md
/Users/chenjiaxuan/Downloads/civilization-tech-path-research/01-physical-path-verdicts.md
/Users/chenjiaxuan/Downloads/civilization-tech-path-research/02-startup-answer.md

然后打开 docs/strategy/fable5_sprint_2026_06/CIVILIZATION_TECH_FRAMEWORK_PRODUCTIZATION.md，
完成所有【FILL】槽位。规则：
1. 维度、判定、案例必须忠实于源文件，不允许新增理论；
2. 标注哪些内容是源文件原有判定、哪些是你按框架现场生成的"新判"；
3. 所有判定语句给出源文件中的依据位置；
4. 完成后输出：中文文章完整初稿、英文文章完整初稿、worksheet 成品、
   scoring template 成品、10 个案例卡片。
```

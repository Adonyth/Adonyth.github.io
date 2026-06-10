# UI_UX_AUDIT — 当前 UI/UX 审计（假设模式）

> **诚实声明**：console 与 site 代码在本机，本会话未能读取（SOURCE_GAPS.md）。
> 本审计 = ①从文件名/上下文可安全推断的结构性判断 + ②研究型 console 的
> 已知失败模式假设清单 + ③30 分钟本机核验流程。
> 所有具体断言均为 [HYPOTHESIS]，本机核验后保留/删除。
> **本文档完成核验前，不得作为重构依据的唯一来源。**

## 1. 从可得信息的结构性推断

- `app.py` 单文件 + 下划线组件 → 大概率 Streamlit 研究 console [HYPOTHESIS]。
  若属实，这本身就是 P0 级判断：**Streamlit 适合内部工具，给外部用户的
  receipt 页和 track record 页需要的是可分享、可索引、秒开的静态/轻页面**——
  与其说"重构 Streamlit"，不如说"把对外面从 Streamlit 里解放出来"。
- `ledger_conformal.py`、`_heatmap_component.py` → UI 以方法（conformal、
  heatmap）而非用户任务命名 [推断]——研究 demo 的典型症状：
  信息架构围绕"我们会算什么"，不是"用户来干什么"。
- `_i18n.py` → 双语维护成本 ×2。产品验证期应锁单语言
  （目标用户 D1 是英文市场 → 对外英文，console 内部随意）。
- `future_reality_ledger.py` 与 Phase 3 `ledger/` schema 大概率不一致
  [HYPOTHESIS] → 必须统一到一个 schema（PRD 第 4 节），否则两套账。

## 2. 失败模式假设清单（本机逐条核验，预期多数命中）

### 信息架构
- [ ] H1 首屏没有回答"这是什么、我能干什么"，而是直接展示数据/图 [P0]
- [ ] H2 导航按内部概念组织（heatmap/conformal/ledger）而非任务
      （登记/查看收据/看履历）[P0]
- [ ] H3 不存在"receipt"作为第一类视觉对象——核心产品物没有视觉形态 [P0]

### 首次困惑点
- [ ] H4 新用户打开即空图表/空表格，无 empty state 引导 [P0]
- [ ] H5 术语未翻译成人话：CRPS、PIT、conformal 直接暴露在主流程 [P1]
- [ ] H6 中英混排造成对外 demo 障碍 [P1]

### 研究 demo 特征
- [ ] H7 过度解释：段落式方法论文字嵌在界面里（应移到 docs/tooltip）[P1]
- [ ] H8 参数旋钮暴露给用户（窗口期、置信度等应是默认值）[P1]
- [ ] H9 视觉层级平：所有数字同字号同色，无"此刻最重要的一个数" [P1]

### 应隐藏/降级/移出主流程
- [ ] H10 conformal 实验性功能 → 移到 /lab 或隐藏 [P2]
- [ ] H11 heatmap 若服务研究探索而非用户任务 → 降级到详情页 [P2]
- [ ] H12 任何含金融标的展示 → 必须挂免责声明或暂时移除（合规）[P0]

### Marketing 面（landing.html / pitch.html / site/）
- [ ] H13 landing 是否含越级 claim（对照 matrix 3.3 禁止清单逐句）[P0]
- [ ] H14 RESEARCH_MANIFESTO 语气是否"研究宣言"而非"产品价值"——
      保留为 /research 页，不做首页 [P1]
- [ ] H15 移动端：Streamlit 移动体验差是结构性的；receipt 分享场景
      大量发生在手机（聊天工具里点开）→ 对外页必须移动优先 [P0]

## 3. 30 分钟本机核验流程（运行后回填本文档）

```
1. (5min) 打开 console 截图：首屏、每个导航项一张 → 存 docs/.../ui_audit_shots/
2. (5min) 数一数：首屏可点击元素数、首屏英文单词数、未解释的术语数
3. (10min) 找一个没见过项目的人（或录屏自己冷启动）：
   "打开它，说出这是干什么的，试着完成一次'记录一个预测'"——记录卡点
4. (5min) 手机打开 site/index.html 和 console，截图
5. (5min) 对照第 2 节勾选命中项，命中即转入 CURSOR_UI_REFACTOR_TASKS
```

## 4. 保留 / 重构判定（基于推断的预案，核验后确认）

| 资产 | 预判 | 理由 |
|---|---|---|
| 评分/账本后端逻辑（future_reality_ledger、conformal 数学） | **保留**（逻辑层） | 数学不需要重写，需要的是从 UI 解耦 |
| Streamlit console | **降级为内部工具**，不再投入对外打磨 | 见 §1 |
| receipt/track record 对外页 | **新建**（静态生成，见 REDESIGN_SPEC） | 对外面的正确载体 |
| landing.html / pitch.html | **重写文案，结构可保留** | 文案按 story pack + matrix 重写 |
| _i18n | **冻结**，对外面英文单语 | 验证期成本 |
| heatmap 组件 | **保留代码、移出主流程** | 研究有用，主流程无用 |

## 5. 对外 demo 前必修清单

- **P0**：H1/H2/H3/H4/H12/H13/H15 — 没修完不约任何外部 demo
- **P1**：H5/H6/H7/H8/H9/H14 — 第一次真实 demo 反馈后修
- **P2**：H10/H11 — 顺手修，不占专门时段

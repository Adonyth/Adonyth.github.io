# SOURCE_GAPS — Phase 4 输入文件缺口记录

生成：2026-06-10/11（云端会话）

## 不可读取（本机路径，云端不可达）— 全部 17 个指定输入

**战略/项目文件**（WMDB 根目录与 docs/、marketing/、company/）：
PROJECT_STATE.md、OMYTEA_MASTER_PLAN.md、TECH_EXPLAINER、STORY_THESIS、
MEETING_TALKING_POINTS、PLAIN_EXPLAINER_FOR_COFOUNDER、PITCH_DECK.md、
landing.html、pitch.html、REPO_PUBLIC_SPLIT.md、WORK_PLAN_V418.md

**产品/UI 文件**（影响最大的缺口）：
omytea-personal-console/app.py、_heatmap_component.py、_i18n.py、
future_reality_ledger.py、ledger_conformal.py、docs/DECISION_LOG.md、
site/index.html、site/RESEARCH_MANIFESTO.md

**civilization-tech-path-research** 三个文件：同样不可达。

## 可读取并已使用

- docs/strategy/fable5_sprint_2026_06/ 全部 Phase 1–4 文档（本仓库，自产）
- ledger/ 全部代码与 sample（本仓库，Phase 3 自产）
- Web research（3 组定向搜索，结果引用于 OMYTEA_STARTUP_DIRECTION_RESEARCH.md）

## 缺口的影响与处理方式

| 产出文件 | 影响 | 处理 |
|---|---|---|
| UI_UX_AUDIT.md | **重大**：无法审计未读的代码 | 改为"假设式审计 + 本机执行清单"，所有具体断言标 [VERIFY-LOCAL]，附 30 分钟本机核验流程 |
| CURSOR_UI_REFACTOR_TASKS.md | 重大：不知道现有组件结构 | CT-0 设为"现状盘点"任务，产出喂给后续任务；其余任务写目标态 spec（不依赖现状细节） |
| UI_REDESIGN_SPEC / DESIGN_SYSTEM | 轻微：目标态设计本就不依赖现状 | 正常产出 |
| 方向研究 / PRD / 落地计划 | 轻微：核心定位已由前三阶段锁定 | 正常产出，具体既有结论留 [VERIFY-LOCAL] 回填位 |
| PIVOT_DECISION | 无：依据是本仓库 Phase 3 实证产出 | 正常产出 |

## 从文件名能安全推断的（标记为推断，非事实）

- `app.py` + 组件下划线命名 → 大概率 Streamlit 单文件应用［推断］
- `_i18n.py` → 双语界面（中/英）［推断］
- `ledger_conformal.py` → conformal prediction 区间相关逻辑［推断］
- `future_reality_ledger.py` → 个人预测登记的早期实现，与 Phase 3 的
  finance ledger 可能存在 schema 不一致［推断，需本机核对后统一］

## 关闭缺口的最快路径

在本机 Claude Code 会话中运行 FABLE5_NEXT_PROMPTS.md 的 FP-1（现状盘点 prompt），
把产物 commit 进本分支，云端即可接力。

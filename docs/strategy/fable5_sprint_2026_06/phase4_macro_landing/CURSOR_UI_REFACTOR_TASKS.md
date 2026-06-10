# CURSOR_UI_REFACTOR_TASKS — UI 重构任务包（P0→P2）

> 前置：CT-0 必须最先执行（现状盘点，喂给后续所有任务）。
> 依赖文档：UI_REDESIGN_SPEC.md（spec）、DESIGN_SYSTEM.md（视觉规范）、
> UI_UX_AUDIT.md（假设清单）。本机执行（代码在本机）。
> 通用 non-goals：不改评分数学、不加交易功能、不优化预测模型。

---

## CT-0 ｜ P0 ｜ 现状盘点（其他任务的输入）
- **goal**: 生成 console 与 site 的真实现状清单，核验 UI_UX_AUDIT §2 假设
- **read**: omytea-personal-console/app.py、_heatmap_component.py、_i18n.py、
  future_reality_ledger.py、ledger_conformal.py、site/index.html、
  marketing/landing.html、marketing/pitch.html
- **edit**: 仅新建 docs/strategy/fable5_sprint_2026_06/phase4_macro_landing/UI_CURRENT_STATE.md
- **changes**: 列出①页面/视图清单 ②每视图组件与数据依赖 ③UI 文案中的术语清单
  ④UI_UX_AUDIT §2 的 H1–H15 逐条命中判定 ⑤future_reality_ledger schema 与
  Phase 3 ledger/ schema 的字段差异表
- **acceptance**: 15 个假设全部有命中/未命中结论；schema 差异表完整
- **verify**: 人工抽查 3 条结论对照代码

## CT-1 ｜ P0 ｜ Receipt 卡静态组件
- **goal**: 实现 REDESIGN_SPEC §6 的 receipt 卡（纯 HTML+CSS，无框架）
- **read**: UI_REDESIGN_SPEC §6/§8、DESIGN_SYSTEM 全文、ledger/sample/*.jsonl
- **edit**: 新建 web/components/receipt_card.html + receipt_card.css
- **changes**: 实现 pending/resolved-correct/resolved-incorrect/sample 四态；
  binary 与分位数两种预测显示；hash/时间戳 mono 字体；600px 内完整可读
- **acceptance**: 四态截图对照 spec；黑白打印（print CSS）可读；无 JS 依赖
- **verify**: 浏览器打开 + 打印预览截图

## CT-2 ｜ P0 ｜ Receipt 详情页模板
- **goal**: 单张收据的完整公开页（REDESIGN_SPEC §3 第 2 行）
- **read**: CT-1 产物、UI_REDESIGN_SPEC §3/§4
- **edit**: 新建 web/templates/receipt.html
- **changes**: receipt 卡(大) + 状态时间线（registered→deadline→resolved）+
  verify 折叠区（hash、原始 JSON、复算说明）+ author 链接；六态齐全
- **acceptance**: 用 sample JSONL 任一行渲染成完整页面；移动端单列正常
- **verify**: 桌面+手机宽度截图各一

## CT-3 ｜ P0 ｜ Track Record 页模板
- **goal**: 作者履历公开页
- **read**: UI_REDESIGN_SPEC §3、DESIGN_SYSTEM §9（n<30 规则）
- **edit**: 新建 web/templates/track_record.html
- **changes**: 校准摘要卡（n<30 时数字表格+声明，无曲线）、收据列表
  （pending/resolved 分组）、样本量诚实声明常驻
- **acceptance**: 用 sample 数据渲染；n<30 路径显示声明而非图表
- **verify**: 两种 n 场景截图

## CT-4 ｜ P0 ｜ Landing 首屏重写
- **goal**: 按 REDESIGN_SPEC §1 重写 landing.html 首屏
- **read**: marketing/landing.html（现状）、REDESIGN_SPEC §1、
  OMYTEA_EXTERNAL_STORY_PACK 第 1/2 节（文案来源，禁自创 claim）
- **edit**: marketing/landing.html（或新建 web/index.html 替代）
- **changes**: hero 两行文案 + 一张内嵌 receipt 卡（CT-1 组件）+ 双 CTA +
  诚实区块；删除所有术语/越级表述
- **acceptance**: 首屏无 CRPS/quantum/金融标的字样；文案每句可溯源至 story pack
- **verify**: 给一个外行看 30 秒复述测试

## CT-5 ｜ P0 ｜ Console 首屏任务化
- **goal**: console 打开第一眼从"数据展示"变为"三个任务入口"
  （登记预测 / 待决列表 / 我的履历）
- **read**: CT-0 产物、app.py
- **edit**: app.py（最小改动：首屏重排，不动子页逻辑）
- **changes**: 首屏 = 三按钮 + 待决收据数 + 最近一条收据卡；
  方法名导航改任务名（matrix：heatmap/conformal → 移入 "Lab" 分组）
- **acceptance**: 冷启动用户 10 秒内能说出"我能在这里干什么"
- **verify**: 冷启动录屏

## CT-6 ｜ P1 ｜ Empty states 全覆盖
- **goal**: console 与 web 模板所有数据视图加 empty 态
- **read**: DESIGN_SYSTEM、REDESIGN_SPEC §4
- **edit**: app.py、web/templates/*
- **changes**: 每个空视图 = 一句话 + 单按钮 + SAMPLE 示例（带橙角标）
- **acceptance**: 清空数据目录后无任何空白图表/裸表格
- **verify**: 清空数据冷启动走查

## CT-7 ｜ P1 ｜ 术语降噪
- **goal**: 主流程 UI 文案去术语化
- **read**: CT-0 的术语清单
- **edit**: app.py、_i18n.py、web/templates/*
- **changes**: CRPS→"distance score (CRPS)" 首次出现带 tooltip；
  PIT/conformal 从主流程文案移除（Lab 内保留）；段落式解释移至 Research 页
- **acceptance**: 主流程页面术语数 ≤3 且全部有即时解释
- **verify**: 文案 diff 审阅

## CT-8 ｜ P1 ｜ 对外面英文单语化
- **goal**: web/ 模板与 landing 锁英文；console 维持现状不投入
- **read**: _i18n.py、web/templates/*
- **edit**: web/templates/*
- **changes**: 移除对外页语言切换；中文文案存档不删除
- **acceptance**: 对外页无混排；i18n 文件未被破坏
- **verify**: 渲染检查

## CT-9 ｜ P1 ｜ 状态徽章组件统一
- **goal**: DESIGN_SYSTEM §7 徽章词表落地为单一组件/CSS class 集
- **edit**: web/components/badges.css、各模板
- **changes**: REGISTERED/PENDING/RESOLVED✓/✗/VERIFIED/SAMPLE/LATE/AMENDED
  八态；pending 必须中性灰
- **acceptance**: 全站徽章视觉一致；无红色 pending
- **verify**: 八态对照表截图

## CT-10 ｜ P2 ｜ 金融展示合规扫描
- **goal**: console 中任何金融标的展示加免责声明行或移出默认视图
- **read**: CT-0 产物、PUBLIC_CLAIMS_MATRIX §3.3
- **edit**: app.py 相关视图
- **acceptance**: 默认视图无裸金融数据；声明行使用协议标准句
- **verify**: 走查截图

## CT-11 ｜ P2 ｜ print CSS 与分享卡截图优化
- **goal**: receipt 页打印可读 + 600px 截图美观（聊天分享场景）
- **edit**: web/ 样式
- **acceptance**: 打印预览 + 600px 截图双合格
- **verify**: 截图

# DESIGN_SYSTEM — Omytea 基础设计系统 v0.1

定位一句话：**像审计报告一样可信，像现代工具一样干净。**
反面清单在最后，与正面规范同等效力。

## 1. Design principles

1. **Receipt-first**：一切视觉服务于"这是一张不可篡改的凭证"的感知
2. **诚实即美学**：样本量声明、未决状态、失败得分都正常展示——
   遮掩坏数据的设计等于产品自杀
3. **冷静默认**：默认界面接近黑白；颜色只用于状态语义，绝不用于装饰
4. **零拟人**：不说"AI 认为"，不用机器人插画，不做思考动画
5. **可打印**：receipt 卡黑白打印后仍完整可读（审计物的基本素养）

## 2. UI copy tone

- 短句、现在时、无感叹号；技术词出现必须当场一句话定义
- 说"registered/locked/scored"，不说"predicted the future"
- 自指谦抑：“This record shows…”，永不 “Our AI accurately…”
- 示例微文案：空状态 "No receipts yet. Register your first forecast."；
  错误 "Couldn't lock this forecast. Nothing was saved — try again."
- 禁词（UI 内）：revolutionary, AI-powered, quantum, alpha, edge,
  accuracy guarantee, beat, win

## 3. Color tokens

```
--ink-900: #16181D   主文字
--ink-600: #565B66   次级文字
--ink-300: #C2C6CE   边框/分隔
--paper:   #FBFBF9   背景（暖白，纸感，刻意非纯白）
--surface: #FFFFFF   卡片
--status-pending:  #6B7280  中性灰（未决=常态，非警告）
--status-resolved-pos: #1A7F4E  绿（限状态徽章，禁大面积）
--status-resolved-neg: #B3422E  赭红（“预测错误”用它，冷静非报警）
--status-verified: #1D4ED8  蓝（外部可验证档）
--sample:  #D97706  橙（仅 SAMPLE 角标专用）
--accent:  #1D4ED8  链接/主按钮（与 verified 同源，强化"可信=行动"）
```
规则：彩色像素占比任何一屏 <10%；红绿仅出现在徽章与得分符号，
不用于背景；禁渐变、禁霓虹、禁深色科幻主题。

## 4. Type scale（系统字体栈，免加载）

```
font-sans: Inter, -apple-system, "Segoe UI", sans-serif   界面
font-mono: "JetBrains Mono", "SF Mono", monospace         hash/时间戳/得分/ID
32/40 bold  页标题 | 24/32 semibold 卡片主文（claim 文本）
16/24 regular 正文 | 13/20 regular 辅助 | 12/16 mono 凭证行
```
凭证类信息（hash、UTC、score）一律 mono——等宽字体本身就是"机器记录"的
视觉语言，这是本系统最重要的字体决定。

## 5. Spacing & layout

- 8px 基准网格：4/8/16/24/32/48/64
- 卡片 padding 24，卡间距 16，页面最大宽 720px（单栏，阅读优先）
- receipt 卡内：区块间 16，凭证行群组间 8

## 6. 组件 patterns

- **Card**：1px ink-300 边框 + 0 阴影（审计感=平实；禁浮起阴影堆叠）；
  receipt 卡顶部 4px 状态色条
- **Table**：行高 40，斑马纹禁用，hover 高亮 paper→surface；数字右对齐 mono
- **Form**：标签置顶、行内校验、必填星号禁用（全部字段必填即不标）
- **Button**：主按钮 accent 实底白字；次按钮文字链接；每屏主按钮 ≤1；
  危险操作无红色大按钮（用文字链接+确认输入）
- **Badge**：12px mono 全大写 + 状态色 + 圆角 4px

## 7. Icons & badges

- 单一线性图标集（Lucide），1.5px 描边，禁多彩图标
- 核心徽章词表：`REGISTERED / PENDING / RESOLVED ✓ / RESOLVED ✗ /
  VERIFIED / SAMPLE / LATE / AMENDED`
- LATE 与 AMENDED 必须显眼——展示瑕疵是可信度设计的一部分

## 8. Claim-level（L0–L5）与 evidence grade 视觉

- 外部 UI 用三档方块 `▣▣▢`（REGISTERED/RESOLVED/VERIFIED），见 REDESIGN_SPEC §8
- 内部文档/console 可显示 L0–L5 全梯：L0–L1 灰、L2 蓝描边、L3 蓝实底、
  L4–L5 仅在取得后设计（现在不画——画了就会想用）
- 任何等级徽章 hover/tap 必须给出该等级的判定标准原句（自解释）

## 9. Chart / heatmap / data-viz rules

- n<30：不画推断性图表，显示数字+声明（不可妥协）
- 校准图：对角参考线必画、置信带必画、轴从真实范围开始（禁截断轴夸大）
- 单色系（ink + accent），红绿仅标注正误点
- heatmap 仅限内部 console；对外页禁用（解释成本高于信息价值）
- 每图必带：n、时间范围、数据来源、"过去≠未来"一行注

## 10. Do-not-use list（一票否决）

- 深空/星云/粒子/电路板背景；任何"量子感"视觉
- 水晶球、骰子、塔罗、先知意象（算命感是头号敌人）
- 仪表盘式多图密铺首屏；3D 图表；饼图
- 倒计时紧迫感营销组件、弹窗、"限时"
- 打字机逐字输出效果、AI 头像/聊天气泡（产品不是 chatbot）
- 绿色大数字涨跌风格（金融终端既视感 → 投资暗示风险）

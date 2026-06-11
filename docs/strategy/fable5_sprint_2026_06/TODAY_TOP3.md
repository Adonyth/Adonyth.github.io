# TODAY_TOP3 — 2026-06-10 今天立刻做的 3 件事

> 排序依据：NEXT_7_DAYS_ACTION_QUEUE 优先级 1–3。
> 今天的成功定义只有一条：**ledger 从 0 行变成 1 天的真实记录。**

---

## 1. 第一件事（必须今天完成）：Ledger 首日预登记 ［AQ-1］

**具体操作**（本机执行）：

```bash
cd /Users/chenjiaxuan/Downloads/WMDB        # 或新建专用 ledger 目录
mkdir -p ledger/forecasts ledger/resolutions
cd ledger && git init                        # 若用独立 repo
# 1) 把 FINANCE_CALIBRATION_LEDGER_PROTOCOL.md 复制进来并 commit
#    —— 这一步本身就是协议的预登记
git add . && git commit -m "Pre-register calibration ledger protocol v1.0"
```

然后生成首日预测（明天 2026-06-11 开盘前必须 commit）：
- 10 个标的（SPY QQQ IWM XLE GLD TLT AAPL MSFT EURUSD VIX）
- 每标的至少 B0-flat 一行：q50=0，分位距用过去 60 交易日收益的经验分位数
  （任何行情网站/本机 Fable 5 会话帮你拉公开收盘价算）
- 写入 `forecasts/2026-06-11.jsonl`（schema 见协议第 6 节），commit

**产出文件**：`ledger/forecasts/2026-06-11.jsonl` + 两个 commit
**不做什么**：不等脚本写完（手算 B0 就够首日）；不加标的；不调"更好看"的分位数
——B0 的全部意义就是无信息。**首日超过 90 分钟 = 你在完美主义，只录 B0 收工。**
**完成后下一步**：把第 2 件事的任务包发给 Codex，明天起脚本接管。

---

## 2. 第二件事（今天推进到可交给 Codex/Cursor）：派发脚本三件套 ［AQ-2 + AQ-5］

**具体操作**：
1. 打开 `CODEX_TASKS_READY.md`，把 **C1、C2、C3** 三个 prompt 原样复制给 Codex
   （三个独立会话或依次派发，prompt 已自含全部 spec，无需你补充）。
2. 把 **C5（golf 数据源排查）** 复制给 Cursor 或 Codex，今晚要结果。

**产出文件**：Codex 侧产出 `scripts/` 三件套 + 测试；C5 产出 golf memo
第 8 节的 G1 证据行草稿。
**不做什么**：不自己写这些脚本（founder 时间今天有更高优先级用途）；
不让 Codex 自由发挥 schema——prompt 里已锁死字段。
**完成后下一步**：明早验收（pytest 全绿 + 手工复核一个 CRPS 数字），
然后 AQ-1 的日常仪式切换到脚本模式。

---

## 3. 第三件事（今天需要 founder 手动做）：发出 5 条 golf 访谈消息 ［AQ-4］

**具体操作**：打开 `FOUNDER_MANUAL_ACTIONS.md` 第 2 节，把消息模板
个性化后发给 5 个球友（微信/短信，每条 <1 分钟）。

**产出文件**：无文件，发出即完成；收到回复后摘记到
`GOLF_VERTICAL_DECISION_MEMO.md` 第 8 节 G3 证据区（用代号，不记个人信息）。
**不做什么**：不解释 Omytea 愿景（只问打球预期登记意愿这一件事）；
不等"想好完美措辞"——模板够用，发出比措辞重要。
**完成后下一步**：6/12 晚汇总回复，6/13 上午 go/no-go 落锤（AQ-6）。

---

## 今天结束时的自检（21:30，1 分钟）

- [ ] ledger repo 存在且有 ≥2 个 commit？
- [ ] Codex 手里有 4 个任务在跑？
- [ ] 5 条消息已发出？

三个全勾 = 今天合格，文档时代正式结束，数据时代开始。
任何一个没勾 = 明早第一件事补上,其他一切顺延。

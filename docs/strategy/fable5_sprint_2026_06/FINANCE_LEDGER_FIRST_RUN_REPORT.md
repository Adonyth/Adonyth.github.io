# FINANCE_LEDGER_FIRST_RUN_REPORT — 首次运行报告

日期：2026-06-10 ｜ 状态：**最小闭环可运行，11/11 测试通过**

**Calibration research record. Not investment advice.**

## 1. 今天实际创建/修改的文件

```
ledger/scripts/make_forecast.py      预测生成（B0-flat + B1-ewma，本地CSV/dry-run）
ledger/scripts/score_day.py          评分（pinball-CRPS、PIT、in90/in50）
ledger/scripts/validate_ledger.py    schema 校验器（白名单+券商字段黑名单）
ledger/tests/test_ledger.py          11 个测试（含手算 CRPS 验证用例）
ledger/README.md                     runbook + 边界声明
ledger/sample/2026-06-11.dryrun.forecasts.jsonl    20 条合成 sample 记录
ledger/sample/2026-06-11.dryrun.resolutions.jsonl  20 条合成评分记录
docs/strategy/fable5_sprint_2026_06/PHASE3_EXECUTION_LOG.md（本次新建）
```

零第三方依赖（纯 Python 3.11 标准库）、零联网、零凭证。
整个 `ledger/` 目录复制到本机即可运行，无安装步骤。

## 2. 如何运行

```bash
# 测试
python3 -m unittest discover ledger/tests -v
# 完整 dry-run 闭环（无需任何数据）
python3 ledger/scripts/make_forecast.py --date 2026-06-11 --dry-run
python3 ledger/scripts/score_day.py --forecasts ledger/sample/2026-06-11.dryrun.forecasts.jsonl --dry-run --out ledger/sample/2026-06-11.dryrun.resolutions.jsonl
python3 ledger/scripts/validate_ledger.py ledger/sample/*.jsonl
# 真实模式（founder 自备 CSV，见 ledger/README.md 每日 runbook）
python3 ledger/scripts/make_forecast.py --date YYYY-MM-DD --prices prices.csv
```

## 3. Sample record 长什么样

```json
{"_meta": "Calibration research record. Not investment advice."}
{"date": "2026-06-11", "ticker": "SPY", "target": "log_return_next_close",
 "source": "B0-flat", "q05": -0.014442, "q25": -0.006138, "q50": 0.0,
 "q75": 0.006791, "q95": 0.014221, "created_utc": "2026-06-10T23:18:35Z",
 "late": false, "protocol_version": "1.0-dryrun"}
```

评分后：

```json
{"date": "2026-06-11", "ticker": "SPY", "source": "B0-flat",
 "realized": 0.013056, "data_source": "synthetic-dryrun",
 "resolved_utc": "2026-06-10T23:18:35Z",
 "scores": {"crps": 0.00349168, "pit_bucket": "q75-q95",
            "in90": true, "in50": false}}
```

注意 `protocol_version: "1.0-dryrun"` 和 `data_source: "synthetic-dryrun"`：
**这是合成数据的格式演示，不是对任何市场的预测**。真实记录必须用
`--prices` 模式生成且 commit 时间戳在开盘前。

## 4. 当前不能声称什么

- 不能声称"账本已运行"——真实预登记记录仍为 **0 行**（sample 不算）。
- 不能声称任何校准好坏——没有真实数据；且按协议 §5，<60 交易日不支持
  任何统计结论。
- 不能声称 B0/B1 有任何预测能力——它们是 baseline，存在意义就是被超越。
- 不能对外宣传"金融预测"任何字样——这是校准研究工具（claims matrix C8/C11 禁止线）。
- 不能在 attorney 意见回来前公开此 repo 的 ledger 部分
  （FOUNDER_MANUAL_ACTIONS 第 5 节纪律）。

## 5. 明天要补什么

1. **真实价格 CSV 流程**：founder 从公开行情源手动导出 10 标的 ≥61 日收盘价
   → 跑 `--prices` 模式 → 开盘前 commit。这是第一条真实记录的最后一公里。
2. M1-llm 源的生成 spec（等三件套本机验收后发给 Codex）。
3. report.py（AQ-9，6/17 前）。

## 6. 必须 founder 手动完成的事

- 把 `ledger/` 目录拉到本机（`git pull` 本分支即可）。
- 准备 prices.csv 并执行明早第一次**真实**预登记 commit——
  按下 commit 的必须是你（FOUNDER_MANUAL_ACTIONS 第 1 节）。
- 决定真实 ledger 的最终居所：本 repo / WMDB / 独立私有 repo
  （建议独立私有 repo，与 REPO_PUBLIC_SPLIT 核对 `[VERIFY-LOCAL]`）。
- 今天的另外两件事不受本报告影响：5 条 golf 访谈消息、[VERIFY-LOCAL] 核对。

## 7. 需要 attorney / DSO / CPA review 的事

清单已备好（FINANCE_CALIBRATION_LEDGER_PROTOCOL.md 第 10 节），本次新增一条
给 attorney 的补充问题：
- sample/dry-run 记录（明确标注合成数据+免责声明）若出现在公开 repo，
  是否仍有被解读为金融信息发布的风险？
发出动作在 FOUNDER_MANUAL_ACTIONS 第 5 节，本周内完成；
**回复未到之前 ledger 保持私有**。

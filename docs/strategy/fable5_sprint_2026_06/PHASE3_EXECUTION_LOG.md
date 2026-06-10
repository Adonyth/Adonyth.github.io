# PHASE3_EXECUTION_LOG — 执行日志

> 只记录真实发生的执行动作和命令输出，不写战略。

## 2026-06-10 ｜ Session 1（云端，Claude Code）

### 执行前检查（任务 2）

- `scripts/finance_forecast_daily.py`：**不存在**（仓库内无 scripts/ 目录）。
- 仓库内已有 finance/ledger/forecast 文件：**无**（仅 docs/strategy 下的协议文档）。
- `publish.sh` 审查：只操作 `content/posts`，新增 `ledger/` 不影响 Hugo 自动发布。
- Python 3.11.15 可用 → `statistics.NormalDist` 在标准库内，
  实现 EWMA 正态分位数**零第三方依赖**。
- 本机 `/Users/chenjiaxuan/Downloads/WMDB` 仍不可达（云端容器）；
  本闭环构建在本仓库 `ledger/`，目录可整体复制到本机使用（纯 stdlib，无安装步骤）。

### 任务选择（任务 1）

CODEX_TASKS_READY 的 C1（forecast 生成）、C2（评分）、C3（validator）正是
finance ledger 三件套 → 直接在本会话实现（不等外部 Codex），按 Phase 3 约束
做了两处 spec 收紧：
1. **去掉联网**：C1 原 spec 允许 yfinance 拉数据；Phase 3 禁止联网 →
   改为本地 CSV 输入 + `--dry-run` 合成数据。数据获取留给 founder 控制的独立步骤。
2. **B1 命名诚实化**：实现的是协议 §4 允许的 EWMA 变体，source id 用
   `B1-ewma`（不冒名 `B1-garch`），validator 白名单两者都收。

### 创建的文件

| 文件 | 内容 |
|---|---|
| `ledger/scripts/make_forecast.py` | B0-flat + B1-ewma 分位数生成；本地 CSV 或 dry-run；拒绝覆盖已有文件 |
| `ledger/scripts/score_day.py` | pinball-CRPS、PIT bucket、in90/in50；输出带免责 _meta 行 |
| `ledger/scripts/validate_ledger.py` | 精确字段集、单调性、白名单、券商字段黑名单、日期/文件名一致性 |
| `ledger/tests/test_ledger.py` | 11 个测试，含 C2 spec 的手算 CRPS 用例 |
| `ledger/README.md` | runbook + 代码强制执行的边界声明 |
| `ledger/sample/2026-06-11.dryrun.*.jsonl` | dry-run 产物（合成数据，标记 1.0-dryrun） |

### 本地验证（任务 5）

```
$ python3 -m unittest discover ledger/tests -v
Ran 11 tests in 0.011s — OK
（含 test_hand_computed_case：quantiles=[-2,-1,0,1,2], y=0.5 → CRPS=0.19 精确匹配）

$ python3 ledger/scripts/make_forecast.py --date 2026-06-11 --dry-run
wrote 20 forecast records -> ledger/sample/2026-06-11.dryrun.forecasts.jsonl

$ python3 ledger/scripts/validate_ledger.py ledger/sample/2026-06-11.dryrun.forecasts.jsonl
PASS

$ python3 ledger/scripts/score_day.py --forecasts ledger/sample/...forecasts.jsonl --dry-run --out ...resolutions.jsonl
scored 20 records -> ledger/sample/2026-06-11.dryrun.resolutions.jsonl

$ python3 ledger/scripts/validate_ledger.py ledger/sample/...resolutions.jsonl
PASS
```

闭环状态：**生成 → 验证 → 评分 → 验证 全链路可运行**。
负面用例已测：乱序分位数、多余字段、券商字段（order_size）、日期不匹配均被拒。

### 边界合规自查（任务 7 约束）

- 无买卖建议：schema 无方向/动作字段；评分输出无评价性语言 ✓
- 无券商接入/自动下单：无任何网络调用 ✓
- 未读取任何 credentials/敏感文件 ✓
- sample 记录标记 `1.0-dryrun` + 免责 _meta 行，不可能被误读为真实预测 ✓
- 未扩张为交易系统：拒绝覆盖、append-only、白名单锁死 ✓

### 未完成 / 顺延

- 真实数据 CSV 的获取流程（founder 控制，明日）
- M1-llm 预测源（等三件套在本机验收后另发 spec）
- report.py 周报（队列 AQ-9，6/17 前交付即可）

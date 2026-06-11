# Finance Calibration Ledger — minimal runnable loop

**Calibration research record. Not investment advice.**

This directory implements the minimal loop defined in
`docs/strategy/fable5_sprint_2026_06/FINANCE_CALIBRATION_LEDGER_PROTOCOL.md`:
pre-registration-style daily distribution forecasts → schema validation →
proper-rule scoring (CRPS / PIT / interval coverage).

## Hard boundaries (enforced in code, not just stated)

- **Zero trading**: no buy/sell/hold output exists anywhere in the schema.
  The validator rejects any record containing brokerage-shaped keys
  (`account`, `position`, `order`, `api_key`, `credential`, ...).
- **Zero network**: scripts never fetch data. Price history and realized
  values come from local CSV files you provide, or from deterministic
  synthetic data in `--dry-run` mode.
- **Zero credentials**: nothing here reads or stores any secret.
- **Append-only**: scripts refuse to overwrite existing ledger files.
- **No accuracy claims**: scores measure distributional calibration only.
  Per protocol §5, fewer than 60 trading days supports no statistical
  conclusion of any kind.

## Requirements

Python 3.11+ standard library only. No third-party packages.

## Daily runbook (~5 min once data CSV routine exists)

```bash
# 1. BEFORE market open: generate + pre-register today's forecasts
python3 ledger/scripts/make_forecast.py --date YYYY-MM-DD --prices prices.csv
python3 ledger/scripts/validate_ledger.py ledger/forecasts/YYYY-MM-DD.jsonl
git add ledger/forecasts/YYYY-MM-DD.jsonl
git commit -m "Pre-register forecasts YYYY-MM-DD"   # the commit IS the registration

# 2. NEXT day after close: score yesterday against realized values
python3 ledger/scripts/score_day.py \
  --forecasts ledger/forecasts/YYYY-MM-DD.jsonl --realized realized.csv
python3 ledger/scripts/validate_ledger.py ledger/resolutions/YYYY-MM-DD.jsonl
git add ledger/resolutions/ && git commit -m "Resolve YYYY-MM-DD"
```

`prices.csv` columns: `date,ticker,close` (≥61 trading days per ticker).
`realized.csv` columns: `ticker,realized` (log return; VIX: closing level).
Obtaining these CSVs from a public source is a separate, founder-controlled
step — deliberately outside these scripts.

## Dry-run (no data needed, fully offline)

```bash
python3 ledger/scripts/make_forecast.py --date 2026-06-11 --dry-run
python3 ledger/scripts/score_day.py \
  --forecasts ledger/sample/2026-06-11.dryrun.forecasts.jsonl --dry-run \
  --out ledger/sample/2026-06-11.dryrun.resolutions.jsonl
python3 ledger/scripts/validate_ledger.py ledger/sample/*.jsonl
python3 -m unittest discover ledger/tests -v
```

Dry-run records carry `protocol_version: "1.0-dryrun"` and synthetic data
only — they are demonstrations of the record format, **not** market
forecasts, and must never be mixed into `forecasts/` or `resolutions/`.

## Forecast sources in this minimal version

- `B0-flat` — no-information baseline: median 0, spread from 60-day
  empirical quantiles. Everything else must beat this to matter.
- `B1-ewma` — EWMA(λ=0.94) volatility + normal quantiles (the EWMA variant
  permitted by protocol §4 for B1).
- `M1-llm` / `H1-human` — schema-supported, not yet generated here.

## File layout

```
ledger/
  forecasts/    YYYY-MM-DD.jsonl       (real pre-registered records)
  resolutions/  YYYY-MM-DD.jsonl       (scored outcomes)
  sample/       *.dryrun.*.jsonl       (synthetic demos, never real)
  scripts/      make_forecast.py  score_day.py  validate_ledger.py
  tests/        test_ledger.py
```

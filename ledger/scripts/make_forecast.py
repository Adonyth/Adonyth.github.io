#!/usr/bin/env python3
"""Generate one day of pre-registration-style distribution forecasts.

Calibration research tooling. NOT investment advice. Produces no buy/sell
signals, connects to nothing, and never touches credentials. Offline only:
price history comes from a local CSV (date,ticker,close) or, with
--dry-run, from deterministic synthetic data.

Per FINANCE_CALIBRATION_LEDGER_PROTOCOL.md v1.0:
forecast target is next-close log return (VIX: next-close level), expressed
as five quantiles [q05,q25,q50,q75,q95].
"""

import argparse
import csv
import json
import math
import random
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path

TICKERS = ["SPY", "QQQ", "IWM", "XLE", "GLD", "TLT", "AAPL", "MSFT", "EURUSD", "VIX"]
LEVEL_TICKERS = {"VIX"}  # forecast level_next_close instead of log return
QUANTILE_TAUS = [0.05, 0.25, 0.50, 0.75, 0.95]
LOOKBACK = 60
EWMA_LAMBDA = 0.94
DISCLAIMER = "Calibration research record. Not investment advice."


def log_returns(closes):
    return [math.log(b / a) for a, b in zip(closes, closes[1:])]


def empirical_quantiles(data):
    """5th/25th/50th/75th/95th percentiles via inclusive interpolation."""
    cuts = statistics.quantiles(data, n=20, method="inclusive")
    return [cuts[0], cuts[4], cuts[9], cuts[14], cuts[18]]


def ewma_sigma(data):
    var = statistics.fmean(x * x for x in data)
    for x in data:
        var = EWMA_LAMBDA * var + (1 - EWMA_LAMBDA) * x * x
    return math.sqrt(var)


def b0_flat(ticker, closes):
    """No-information baseline: q50 = 0 (VIX: last level), spread empirical."""
    if ticker in LEVEL_TICKERS:
        changes = [b - a for a, b in zip(closes, closes[1:])][-LOOKBACK:]
        q = empirical_quantiles(changes)
        last = closes[-1]
        return [last + q[0], last + q[1], last, last + q[3], last + q[4]]
    rets = log_returns(closes)[-LOOKBACK:]
    q = empirical_quantiles(rets)
    return [q[0], q[1], 0.0, q[3], q[4]]


def b1_ewma(ticker, closes):
    """EWMA-volatility normal quantiles (the EWMA variant of protocol B1)."""
    if ticker in LEVEL_TICKERS:
        changes = [b - a for a, b in zip(closes, closes[1:])][-LOOKBACK:]
        dist = statistics.NormalDist(closes[-1], ewma_sigma(changes))
    else:
        rets = log_returns(closes)[-LOOKBACK:]
        dist = statistics.NormalDist(0.0, ewma_sigma(rets))
    return [dist.inv_cdf(t) for t in QUANTILE_TAUS]


def synthetic_history(seed=42, days=LOOKBACK + 21):
    """Deterministic synthetic closes per ticker, for --dry-run only."""
    rng = random.Random(seed)
    vols = {"SPY": .010, "QQQ": .013, "IWM": .014, "XLE": .016, "GLD": .009,
            "TLT": .008, "AAPL": .017, "MSFT": .015, "EURUSD": .005}
    hist = {}
    for t in TICKERS:
        if t in LEVEL_TICKERS:
            lvl, out = 20.0, []
            for _ in range(days):
                lvl = max(9.0, lvl + rng.gauss(0, 1.1) + 0.05 * (18.0 - lvl))
                out.append(round(lvl, 4))
        else:
            px, out = 100.0, []
            for _ in range(days):
                px *= math.exp(rng.gauss(0, vols[t]))
                out.append(round(px, 4))
        hist[t] = out
    return hist


def load_csv_history(path):
    hist = {t: [] for t in TICKERS}
    with open(path, newline="") as f:
        rows = sorted(csv.DictReader(f), key=lambda r: r["date"])
    for r in rows:
        if r["ticker"] in hist:
            hist[r["ticker"]].append(float(r["close"]))
    return hist


def build_records(date, hist, protocol_version):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    records = []
    for ticker in TICKERS:
        closes = hist.get(ticker, [])
        if len(closes) < LOOKBACK + 1:
            raise SystemExit(f"{ticker}: need >= {LOOKBACK + 1} closes, got {len(closes)}")
        target = "level_next_close" if ticker in LEVEL_TICKERS else "log_return_next_close"
        for source, fn in (("B0-flat", b0_flat), ("B1-ewma", b1_ewma)):
            q = [round(x, 6) for x in fn(ticker, closes)]
            if not all(a < b for a, b in zip(q, q[1:])):
                raise SystemExit(f"{ticker}/{source}: quantiles not strictly increasing: {q}")
            records.append({
                "date": date, "ticker": ticker, "target": target, "source": source,
                "q05": q[0], "q25": q[1], "q50": q[2], "q75": q[3], "q95": q[4],
                "created_utc": now, "late": False, "protocol_version": protocol_version,
            })
    return records


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--date", required=True, help="forecast date YYYY-MM-DD")
    ap.add_argument("--prices", help="CSV with columns date,ticker,close (offline file)")
    ap.add_argument("--dry-run", action="store_true",
                    help="use deterministic synthetic data; writes to sample/ dir")
    ap.add_argument("--ledger-dir", default=str(Path(__file__).resolve().parents[1]))
    args = ap.parse_args(argv)

    if args.dry_run:
        hist, version = synthetic_history(), "1.0-dryrun"
        out_dir = Path(args.ledger_dir) / "sample"
        out_path = out_dir / f"{args.date}.dryrun.forecasts.jsonl"
    elif args.prices:
        hist, version = load_csv_history(args.prices), "1.0"
        out_dir = Path(args.ledger_dir) / "forecasts"
        out_path = out_dir / f"{args.date}.jsonl"
    else:
        ap.error("provide --prices CSV or --dry-run (this tool never fetches data itself)")

    if out_path.exists():
        raise SystemExit(f"refusing to overwrite existing ledger file: {out_path}")
    out_dir.mkdir(parents=True, exist_ok=True)
    records = build_records(args.date, hist, version)
    with open(out_path, "w") as f:
        f.write(json.dumps({"_meta": DISCLAIMER}) + "\n")
        for r in records:
            f.write(json.dumps(r) + "\n")
    print(f"wrote {len(records)} forecast records -> {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

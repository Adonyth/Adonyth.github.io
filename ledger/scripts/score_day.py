#!/usr/bin/env python3
"""Score one day of forecasts against realized values.

Calibration research tooling. NOT investment advice. Scores measure
distributional calibration (CRPS/PIT/coverage) only; no evaluative
language about any security is produced. Offline only: realized values
come from a local CSV (ticker,realized) or --dry-run synthetic data.
"""

import argparse
import csv
import json
import math
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

QUANTILE_TAUS = [0.05, 0.25, 0.50, 0.75, 0.95]
QUANTILE_KEYS = ["q05", "q25", "q50", "q75", "q95"]
DISCLAIMER = "Calibration research record. Not investment advice."


def pinball_crps(quantiles, y):
    """Mean pinball loss over the five quantiles (CRPS approximation)."""
    total = 0.0
    for tau, q in zip(QUANTILE_TAUS, quantiles):
        indicator = 1.0 if y < q else 0.0
        total += (indicator - tau) * (q - y)
    return total / len(QUANTILE_TAUS)


def pit_bucket(quantiles, y):
    labels = ["<q05", "q05-q25", "q25-q50", "q50-q75", "q75-q95", ">q95"]
    for q, label in zip(quantiles, labels):
        if y < q:
            return label
    return labels[-1]


def synthetic_realized(forecasts, seed=43):
    """Deterministic synthetic realized values, for --dry-run only.

    Draws around each ticker's B0 median with a spread tied to its own
    forecast interval, so dry-run output exercises every PIT bucket
    plausibly. Purely synthetic; no market meaning whatsoever.
    """
    rng = random.Random(seed)
    realized = {}
    for r in forecasts:
        if r["source"] != "B0-flat" or r["ticker"] in realized:
            continue
        spread = (r["q95"] - r["q05"]) / 3.29  # implied sigma if normal
        realized[r["ticker"]] = round(rng.gauss(r["q50"], spread), 6)
    return realized


def load_realized_csv(path):
    with open(path, newline="") as f:
        return {r["ticker"]: float(r["realized"]) for r in csv.DictReader(f)}


def score_records(forecasts, realized, data_source):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    out = []
    for r in forecasts:
        y = realized.get(r["ticker"])
        if y is None:
            raise SystemExit(f"no realized value for {r['ticker']}")
        q = [r[k] for k in QUANTILE_KEYS]
        out.append({
            "date": r["date"], "ticker": r["ticker"], "source": r["source"],
            "realized": y, "data_source": data_source, "resolved_utc": now,
            "scores": {
                "crps": round(pinball_crps(q, y), 8),
                "pit_bucket": pit_bucket(q, y),
                "in90": bool(q[0] <= y <= q[4]),
                "in50": bool(q[1] <= y <= q[3]),
            },
        })
    return out


def read_forecast_file(path):
    records = []
    with open(path) as f:
        for line in f:
            row = json.loads(line)
            if "_meta" not in row:
                records.append(row)
    return records


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--forecasts", required=True, help="path to forecasts JSONL")
    ap.add_argument("--realized", help="CSV with columns ticker,realized (offline file)")
    ap.add_argument("--dry-run", action="store_true",
                    help="use deterministic synthetic realized values")
    ap.add_argument("--out", help="output path (default: derived from input path)")
    args = ap.parse_args(argv)

    fpath = Path(args.forecasts)
    forecasts = read_forecast_file(fpath)
    if not forecasts:
        raise SystemExit(f"no forecast records in {fpath}")

    if args.dry_run:
        realized, data_source = synthetic_realized(forecasts), "synthetic-dryrun"
    elif args.realized:
        realized, data_source = load_realized_csv(args.realized), Path(args.realized).name
    else:
        ap.error("provide --realized CSV or --dry-run (this tool never fetches data itself)")

    out_path = Path(args.out) if args.out else Path(
        str(fpath).replace("forecasts", "resolutions", 1))
    if out_path.exists():
        raise SystemExit(f"refusing to overwrite existing ledger file: {out_path}")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    results = score_records(forecasts, realized, data_source)
    with open(out_path, "w") as f:
        f.write(json.dumps({"_meta": DISCLAIMER}) + "\n")
        for r in results:
            f.write(json.dumps(r) + "\n")
    print(f"scored {len(results)} records -> {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Validate ledger JSONL files against the protocol schema.

Calibration research tooling. NOT investment advice.
Exit code 0 iff every file passes. Checks per CODEX task C3:
exact field sets, strictly increasing quantiles, ticker/source/version
whitelists, parseable UTC timestamps, date/filename agreement, and a
blacklist of brokerage-shaped keys that must never appear in this ledger.
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

FORECAST_FIELDS = {"date", "ticker", "target", "source", "q05", "q25", "q50",
                   "q75", "q95", "created_utc", "late", "protocol_version"}
RESOLUTION_FIELDS = {"date", "ticker", "source", "realized", "data_source",
                     "resolved_utc", "scores"}
SCORE_FIELDS = {"crps", "pit_bucket", "in90", "in50"}
TICKERS = {"SPY", "QQQ", "IWM", "XLE", "GLD", "TLT", "AAPL", "MSFT", "EURUSD", "VIX"}
SOURCES = {"B0-flat", "B1-ewma", "B1-garch", "M1-llm", "H1-human"}
VERSIONS = {"1.0", "1.0-manual", "1.0-dryrun"}
PIT_BUCKETS = {"<q05", "q05-q25", "q25-q50", "q50-q75", "q75-q95", ">q95"}
KEY_BLACKLIST = ("account", "position", "order", "api_key", "credential",
                 "password", "secret", "token")
QUANTILE_KEYS = ["q05", "q25", "q50", "q75", "q95"]


def check_timestamp(value):
    datetime.fromisoformat(str(value).replace("Z", "+00:00"))


def validate_row(row, kind, file_date):
    errors = []
    for key in row:
        lk = key.lower()
        hits = [b for b in KEY_BLACKLIST if b in lk]
        if hits:
            errors.append(f"forbidden key name '{key}' (matches {hits[0]})")
    expected = FORECAST_FIELDS if kind == "forecast" else RESOLUTION_FIELDS
    if set(row) != expected:
        missing, extra = expected - set(row), set(row) - expected
        errors.append(f"field set mismatch (missing={sorted(missing)}, extra={sorted(extra)})")
        return errors  # field errors make the remaining checks unreliable
    if row["date"] != file_date:
        errors.append(f"date {row['date']} != filename date {file_date}")
    if row["ticker"] not in TICKERS:
        errors.append(f"ticker '{row['ticker']}' not in whitelist")
    if row["source"] not in SOURCES:
        errors.append(f"source '{row['source']}' not in whitelist")
    if kind == "forecast":
        if row["protocol_version"] not in VERSIONS:
            errors.append(f"unknown protocol_version '{row['protocol_version']}'")
        q = [row[k] for k in QUANTILE_KEYS]
        if not all(isinstance(x, (int, float)) for x in q):
            errors.append("non-numeric quantile")
        elif not all(a < b for a, b in zip(q, q[1:])):
            errors.append(f"quantiles not strictly increasing: {q}")
        try:
            check_timestamp(row["created_utc"])
        except ValueError:
            errors.append(f"bad created_utc '{row['created_utc']}'")
    else:
        if set(row["scores"]) != SCORE_FIELDS:
            errors.append(f"scores field mismatch: {sorted(row['scores'])}")
        elif row["scores"]["pit_bucket"] not in PIT_BUCKETS:
            errors.append(f"bad pit_bucket '{row['scores']['pit_bucket']}'")
        try:
            check_timestamp(row["resolved_utc"])
        except ValueError:
            errors.append(f"bad resolved_utc '{row['resolved_utc']}'")
    return errors


def validate_file(path):
    """Return list of (line_number, message). Empty list means PASS."""
    path = Path(path)
    problems = []
    m = re.match(r"(\d{4}-\d{2}-\d{2})", path.name)
    if not m:
        return [(0, "filename must start with YYYY-MM-DD")]
    file_date = m.group(1)
    kind = "resolution" if "resolution" in str(path) else "forecast"
    with open(path) as f:
        for n, line in enumerate(f, 1):
            try:
                row = json.loads(line)
            except json.JSONDecodeError as e:
                problems.append((n, f"invalid JSON: {e}"))
                continue
            if "_meta" in row:
                continue
            for err in validate_row(row, kind, file_date):
                problems.append((n, err))
    return problems


def main(argv=None):
    paths = argv if argv is not None else sys.argv[1:]
    if not paths:
        print("usage: validate_ledger.py FILE.jsonl [FILE.jsonl ...]")
        return 2
    failed = False
    for p in paths:
        problems = validate_file(p)
        if problems:
            failed = True
            print(f"FAIL {p}")
            for n, msg in problems:
                print(f"  line {n}: {msg}")
        else:
            print(f"PASS {p}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

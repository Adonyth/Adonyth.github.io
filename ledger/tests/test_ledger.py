"""Tests for the minimal calibration ledger loop. Stdlib unittest only.

Run from repo root:  python3 -m unittest discover ledger/tests -v
"""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import make_forecast
import score_day
import validate_ledger


class TestPinballCRPS(unittest.TestCase):
    def test_hand_computed_case(self):
        # Protocol C2 spec case: quantiles [-2,-1,0,1,2], y = 0.5
        # tau=.05,q=-2: (0-.05)(-2.5)=.125 | tau=.25,q=-1: (0-.25)(-1.5)=.375
        # tau=.50,q=0:  (0-.50)(-0.5)=.250 | tau=.75,q=1:  (1-.75)(0.5)=.125
        # tau=.95,q=2:  (1-.95)(1.5)=.075  -> mean = 0.95/5 = 0.19
        self.assertAlmostEqual(score_day.pinball_crps([-2, -1, 0, 1, 2], 0.5), 0.19)

    def test_perfect_median_scores_lower(self):
        wide = score_day.pinball_crps([-2, -1, 0, 1, 2], 0.0)
        narrow = score_day.pinball_crps([-0.2, -0.1, 0, 0.1, 0.2], 0.0)
        self.assertLess(narrow, wide)

    def test_pit_buckets(self):
        q = [-2, -1, 0, 1, 2]
        self.assertEqual(score_day.pit_bucket(q, -3), "<q05")
        self.assertEqual(score_day.pit_bucket(q, 0.5), "q50-q75")
        self.assertEqual(score_day.pit_bucket(q, 3), ">q95")


class TestForecastGeneration(unittest.TestCase):
    def test_synthetic_records_valid_and_monotonic(self):
        hist = make_forecast.synthetic_history()
        records = make_forecast.build_records("2026-06-11", hist, "1.0-dryrun")
        # 10 tickers x 2 sources
        self.assertEqual(len(records), 20)
        for r in records:
            q = [r[k] for k in ["q05", "q25", "q50", "q75", "q95"]]
            self.assertTrue(all(a < b for a, b in zip(q, q[1:])), r)
        vix = [r for r in records if r["ticker"] == "VIX"]
        self.assertTrue(all(r["target"] == "level_next_close" for r in vix))

    def test_deterministic(self):
        a = make_forecast.synthetic_history()
        b = make_forecast.synthetic_history()
        self.assertEqual(a, b)


class TestValidator(unittest.TestCase):
    def _write(self, name, rows):
        d = Path(self.tmp.name)
        p = d / name
        with open(p, "w") as f:
            for row in rows:
                f.write(json.dumps(row) + "\n")
        return p

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.good = {
            "date": "2026-06-11", "ticker": "SPY", "target": "log_return_next_close",
            "source": "B0-flat", "q05": -0.014, "q25": -0.005, "q50": 0.0,
            "q75": 0.005, "q95": 0.014, "created_utc": "2026-06-11T12:00:00Z",
            "late": False, "protocol_version": "1.0",
        }

    def tearDown(self):
        self.tmp.cleanup()

    def test_good_row_passes(self):
        p = self._write("2026-06-11.jsonl", [{"_meta": "x"}, self.good])
        self.assertEqual(validate_ledger.validate_file(p), [])

    def test_unsorted_quantiles_fail(self):
        bad = dict(self.good, q25=0.02)  # q25 > q50
        p = self._write("2026-06-11.jsonl", [bad])
        self.assertTrue(any("strictly increasing" in m for _, m in
                            validate_ledger.validate_file(p)))

    def test_extra_field_fails(self):
        bad = dict(self.good, alpha_signal=1.0)
        p = self._write("2026-06-11.jsonl", [bad])
        self.assertTrue(any("field set mismatch" in m for _, m in
                            validate_ledger.validate_file(p)))

    def test_brokerage_key_fails(self):
        bad = dict(self.good)
        bad["order_size"] = 100
        p = self._write("2026-06-11.jsonl", [bad])
        self.assertTrue(any("forbidden key" in m for _, m in
                            validate_ledger.validate_file(p)))

    def test_date_mismatch_fails(self):
        p = self._write("2026-06-12.jsonl", [self.good])
        self.assertTrue(any("filename date" in m for _, m in
                            validate_ledger.validate_file(p)))


class TestEndToEndDryRun(unittest.TestCase):
    def test_full_loop(self):
        with tempfile.TemporaryDirectory() as d:
            rc = make_forecast.main(["--date", "2026-06-11", "--dry-run",
                                     "--ledger-dir", d])
            self.assertEqual(rc, 0)
            fpath = Path(d) / "sample" / "2026-06-11.dryrun.forecasts.jsonl"
            self.assertEqual(validate_ledger.validate_file(fpath), [])
            out = Path(d) / "sample" / "2026-06-11.dryrun.resolutions.jsonl"
            rc = score_day.main(["--forecasts", str(fpath), "--dry-run",
                                 "--out", str(out)])
            self.assertEqual(rc, 0)
            self.assertEqual(validate_ledger.validate_file(out), [])
            # append-only: second run must refuse to overwrite
            with self.assertRaises(SystemExit):
                make_forecast.main(["--date", "2026-06-11", "--dry-run",
                                    "--ledger-dir", d])


if __name__ == "__main__":
    unittest.main()

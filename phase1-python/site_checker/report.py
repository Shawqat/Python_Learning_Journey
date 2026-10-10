"""Reporting helpers: console table, CSV, JSON, and log."""

import csv
import json
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent
REPORTS_DIR = BASE_DIR / "reports"
LOGS_DIR = BASE_DIR / "logs"


def _timestamp():
    """Return a filesystem-safe timestamp like 2026 01 09 14 30 12."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def print_table(results):
    """Print an aligned table of results to the console."""
    print(f"{'URL':<50} {'EXPECTED':<9} {'ACTUAL':<7} {'RESULT':<7} TIME")
    for r in results:
        actual = "-" if r["actual"] is None else r["actual"]
        print(
            f"{r['url']:<50} {r['expected']:<9} {actual!s:<7} "
            f"{r['result']:<7} {r['seconds']:.2f}s"
        )


def write_csv_report(results):
    """Write results to reports/report_<timestamp>.csv and return the path."""
    REPORTS_DIR.mkdir(exist_ok=True)
    path = REPORTS_DIR / f"report_{_timestamp()}.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["url", "expected", "actual", "result", "seconds", "message"],
        )
        writer.writeheader()
        writer.writerows(results)
    return path


def write_json_summary(summary):
    """Write summary to reports/summary_<timestamp>.json and return the path."""
    REPORTS_DIR.mkdir(exist_ok=True)
    path = REPORTS_DIR / f"summary_{_timestamp()}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    return path


def append_log(results, summary):
    """Append a timestamped summary line to logs/run.log."""
    LOGS_DIR.mkdir(exist_ok=True)
    path = LOGS_DIR / "run.log"
    ts = datetime.now().isoformat(timespec="seconds")
    line = (
        f"{ts} | total={summary['total']} "
        f"passed={summary['passed']} failed={summary['failed']} "
        f"errors={summary['errors']} pass_rate={summary['pass_rate']:.1f}%"
    )
    with open(path, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    return path
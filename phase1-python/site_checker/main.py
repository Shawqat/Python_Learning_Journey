"""Site Checker entry point: load, check, report, exit."""

import sys
from pathlib import Path

from checker import load_checks, check_url, summarize
from report import print_table, write_csv_report, write_json_summary, append_log

BASE_DIR = Path(__file__).parent
CHECKS_FILE = BASE_DIR / "checks.csv"


def run():
    """Run all checks and return the list of results."""
    checks, skipped = load_checks(CHECKS_FILE)
    if not checks:
        print("No checks to run.")
        return [], skipped

    results = []
    for c in checks:
        print(f"Checking {c['url']} ...", flush=True)
        results.append(check_url(c["url"], c["expected_status"]))
    return results, skipped


def main():
    """Entry point: run checks, print report, exit with proper code."""
    results, skipped = run()
    if not results:
        sys.exit(1)

    summary = summarize(results)
    print()
    print_table(results)
    print()
    print(
        f"Summary: {summary['total']} checks | "
        f"{summary['passed']} passed | "
        f"{summary['failed']} failed | "
        f"{summary['errors']} errors | "
        f"pass rate {summary['pass_rate']:.1f}%"
    )

    if skipped:
        print(f"Warning: {skipped} row(s) skipped due to bad data.")
        print("Run failed: skipped rows count as errors.")

    write_csv_report(results)
    write_json_summary(summary)
    append_log(results, summary)

    all_ok = summary["failed"] == 0 and summary["errors"] == 0 and skipped == 0
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
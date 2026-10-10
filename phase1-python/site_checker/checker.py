"""Load URL checks from a CSV file."""

import csv
from pathlib import Path
import time
import requests


def load_checks(path):
    """
        Returns (checks, skipped) where checks is a list of dicts
        with keys 'url' and 'expected_status' (int), and skipped is
        the number of rows that were skipped due to bad data.
    """
    checks = []
    skipped = 0
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader, start=1):
                url = (row.get("url") or "").strip()
                raw = (row.get("expected_status") or "").strip()

                if not url or not raw:
                    print(f"Warning: skipping blank row {i}")
                    skipped += 1
                    continue

                try:
                    expected = int(raw)
                except ValueError:
                    print(f"Warning: skipping row {i}, bad expected_status='{raw}'")
                    skipped += 1
                    continue

                checks.append({"url": url, "expected_status": expected})
    except FileNotFoundError:
        print(f"Error: checks file not found: {path}")
        return [], 0

    return checks, skipped

def evaluate_status(actual, expected):
    """
        Compare actual status against expected.
        Returns 'PASS' if they match, otherwise 'FAIL'.
    """
    return "PASS" if actual == expected else "FAIL"


def check_url(url, expected_status, timeout=10):
    """
        Check a single URL and return a result dict.
        Result keys: url, expected, actual, result, seconds, message.
    """
    start = time.perf_counter()
    try:
        response = requests.get(url, timeout=timeout)
        elapsed = time.perf_counter() - start
        result = evaluate_status(response.status_code, expected_status)
        return {
            "url": url,
            "expected": expected_status,
            "actual": response.status_code,
            "result": result,
            "seconds": elapsed,
            "message": "",
        }
    except requests.exceptions.RequestException as exc:
        elapsed = time.perf_counter() - start
        return {
            "url": url,
            "expected": expected_status,
            "actual": None,
            "result": "ERROR",
            "seconds": elapsed,
            "message": str(exc),
        }
    

def summarize(results):
    """
        Return counts and pass rate for a list of check results.
            Keys: passed, failed, errors, total, pass_rate.
            pass_rate is a percentage (0-100). Empty list gives 0.0.
    """
    passed = sum(1 for r in results if r["result"] == "PASS")
    failed = sum(1 for r in results if r["result"] == "FAIL")
    errors = sum(1 for r in results if r["result"] == "ERROR")
    total = len(results)
    pass_rate = (passed / total * 100) if total else 0.0
    return {
        "passed": passed,
        "failed": failed,
        "errors": errors,
        "total": total,
        "pass_rate": pass_rate,
    }
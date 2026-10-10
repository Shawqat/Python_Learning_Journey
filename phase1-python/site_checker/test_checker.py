"""Simple assert-based tests for checker.py (no pytest)."""

import os
import tempfile

from checker import evaluate_status, summarize, load_checks


def test_evaluate_status_pass():
    """Matching codes should PASS."""
    assert evaluate_status(200, 200) == "PASS"
    assert evaluate_status(404, 404) == "PASS"


def test_evaluate_status_fail():
    """Mismatched codes should FAIL, including None actual."""
    assert evaluate_status(404, 200) == "FAIL"
    assert evaluate_status(200, 404) == "FAIL"
    assert evaluate_status(None, 200) == "FAIL"


def test_summarize_empty():
    """Empty list should not crash and pass_rate should be 0.0."""
    s = summarize([])
    assert s["total"] == 0
    assert s["passed"] == 0
    assert s["failed"] == 0
    assert s["errors"] == 0
    assert s["pass_rate"] == 0.0


def test_summarize_all_pass():
    """All-pass list should give 100% pass rate."""
    results = [
        {"result": "PASS"},
        {"result": "PASS"},
        {"result": "PASS"},
    ]
    s = summarize(results)
    assert s["passed"] == 3
    assert s["failed"] == 0
    assert s["errors"] == 0
    assert s["pass_rate"] == 100.0


def test_summarize_mixed():
    """Mixed results should count each category separately."""
    results = [
        {"result": "PASS"},
        {"result": "FAIL"},
        {"result": "ERROR"},
        {"result": "PASS"},
    ]
    s = summarize(results)
    assert s["passed"] == 2
    assert s["failed"] == 1
    assert s["errors"] == 1
    assert s["total"] == 4
    assert s["pass_rate"] == 50.0


def test_load_checks_ok():
    """A valid CSV should load with int expected_status."""
    with tempfile.NamedTemporaryFile("w", suffix=".csv",
                                     delete=False, newline="") as f:
        f.write("url,expected_status\n")
        f.write("https://example.com,200\n")
        f.write("https://example.com/nope,404\n")
        path = f.name
    try:
        checks, skipped = load_checks(path)
        assert len(checks) == 2
        assert skipped == 0
        assert checks[0]["url"] == "https://example.com"
        assert checks[0]["expected_status"] == 200
        assert isinstance(checks[0]["expected_status"], int)
    finally:
        os.unlink(path)


def test_load_checks_skips_blank_and_bad():
    """Blank rows and non-numeric status should be skipped.

    Edge case: a row with bad data breaks exactly one rule
    (numeric status), so it must be counted as skipped.
    """
    with tempfile.NamedTemporaryFile("w", suffix=".csv",
                                     delete=False, newline="") as f:
        f.write("url,expected_status\n")
        f.write("https://example.com,200\n")
        f.write(",,\n")                    # blank
        f.write("https://example.com,abc\n")  # bad int
        path = f.name
    try:
        checks, skipped = load_checks(path)
        assert len(checks) == 1
        assert skipped == 2
    finally:
        os.unlink(path)


def test_load_checks_missing_file():
    """A missing file should return ([], 0), not raise."""
    checks, skipped = load_checks("this_file_does_not_exist_123.csv")
    assert checks == []
    assert skipped == 0


if __name__ == "__main__":
    test_evaluate_status_pass()
    test_evaluate_status_fail()
    test_summarize_empty()
    test_summarize_all_pass()
    test_summarize_mixed()
    test_load_checks_ok()
    test_load_checks_skips_blank_and_bad()
    test_load_checks_missing_file()
    print("All tests passed.")
# Site Checker

A small CLI tool that reads a list of URLs with expected HTTP status codes,
checks each one, and reports PASS / FAIL / ERROR. It's basically a tiny test
runner for websites.

I built this as a Phase 1 mini-project to practice functions, file I/O,
exceptions, modules, virtual environments, and Git — all in one go.

## Goal

The idea is simple: give it a CSV of URLs and the status code you expect back,
and it will tell you which ones matched and which ones didn't. It's the same
"expected vs actual" pattern used in real test runners and CI pipelines.

If anything doesn't pass, the program exits with code `1` so CI systems can
detect the failure automatically.

## Setup

These are the steps I used on my machine (Python 3.11+).

```bash
# create and activate a virtual environment
python -m venv .venv
source .venv/Scripts/activate    # Windows (Git Bash)
# source .venv/bin/activate      # macOS / Linux
# .venv\Scripts\activate         # Windows (CMD)

# install dependencies
pip install -r requirements.txt
# Python → Playwright Automation: Progress Tracker

**Started:** 2026-10-05
**Current position:** Phase 1 · Day 4 (not started)
**Last updated:** 2026-10-05 (Day 3 complete)

## How to resume in a new chat
Paste this whole file and say: "Continue my Python course from where I left off."

---

## Phase 1 — Python fundamentals and setup (1–3 weeks)
- [x] Day 1: Setup, print, variables, data types, input, f-strings
- [x] Day 2: Conditionals and comparison operators
- [x] Day 3: Loops (for, while, range)
- [ ] Day 4: Lists and tuples
- [ ] Day 5: Dictionaries and sets
- [ ] Day 6: Functions
- [ ] Day 7: Modules and imports
- [ ] Day 8: File I/O
- [ ] Day 9: Exceptions
- [ ] Day 10: Virtual environments and pip
- [ ] Day 11: Git basics
- [ ] Phase 1 mini-project

## Phase 2 — Web and testing basics (1–2 weeks)
- [ ] HTML/CSS and the DOM
- [ ] CSS and XPath selectors
- [ ] Browser DevTools
- [ ] HTTP, status codes, JSON
- [ ] Testing concepts and pytest

## Phase 3 — Playwright core (2–4 weeks)
- [ ] Install and first script
- [ ] Browser / context / page
- [ ] Locators (get_by_role, get_by_text)
- [ ] Actions, waits, assertions
- [ ] Screenshots and traces
- [ ] Multiple pages and authentication

## Phase 4 — Framework and CI (2–4 weeks)
- [ ] Page Object Model
- [ ] Fixtures and parametrization
- [ ] API testing and network interception
- [ ] Parallel execution and reports
- [ ] GitHub Actions

## Phase 5 — Portfolio (ongoing)
- [ ] Form automation
- [ ] Login/logout tests
- [ ] Todo-app CRUD
- [ ] E-commerce checkout
- [ ] API + UI hybrid
- [ ] Scraper
- [ ] CI pipeline
- [ ] Choose and polish 3–4 capstones

---

## Lab log
| Date | Lesson | Result | Notes |
|------|--------|--------|-------|
| 2026-10-05 | Day 1 Lab | A: 5/6, B-D correct | Missed type("3.0") is str; renamed user_age to birth_year |
| 2026-10-05 | Day 1 Quiz | 5/5 (100%) | |
| 2026-10-05 | Day 2 Lab | A 6/6, B correct, C partial (2 of 4 issues), D bug, E correct | D: `if username and password == ""` is not an 'either is empty' check |
| 2026-10-05 | Day 2 Quiz | 4/5 (80%) | Missed question not identified |
| 2026-10-05 | Day 2 Part D fix | Self-reported done | Code not reviewed by instructor |
| 2026-10-05 | Day 3 Lab | A 3/4, B logic bug, C skipped first number, D mostly right (increment placement), E correct, F off-by-one | Needs verification habit: run with known input, compare actual vs expected |
| 2026-10-05 | Day 3 Quiz | 5/5 (100%) | |
| 2026-10-05 | Day 3 fixes (B, C, F) | Self-reported done | Code not reviewed by instructor |

## Weak spots to revisit
- Value vs. type: quotes make something a str (re-check in Day 2 with comparisons like "5" == 5)
- `and`/`or` don't distribute: each side needs a full condition (Day 2 Part D). Fix: `if not username or not password:`
- Reading code for ALL errors, not just the first ones spotted (syntax: missing colons, indentation)
- Tracing code by hand (trace table: one row per loop iteration)
- Off-by-one with range (stop value is excluded)
- Indentation decides what is inside a loop/if
- Verify before submitting: run with known input, compare actual vs expected
- Descriptive variable names (snake_case, say what the value IS)
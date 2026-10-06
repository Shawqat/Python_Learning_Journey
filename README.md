# Python → Playwright Automation: Progress Tracker

**Started:** 2026-10-05
**Current position:** Phase 1 · Day 7 (not started)
**Last updated:** 2026-10-06 (Day 6 complete)
---

## Phase 1 — Python fundamentals and setup (1–3 weeks)
- [x] Day 1: Setup, print, variables, data types, input, f-strings
- [x] Day 2: Conditionals and comparison operators
- [x] Day 3: Loops (for, while, range)
- [x] Day 4: Lists and tuples
- [x] Day 5: Dictionaries and sets
- [x] Day 6: Functions
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
| 2026-10-05 | Day 4 Lab | A 4/6 (missed aliasing, sort() returns None), B/D/F correct, C worked but did not print the list, E fixed correctly | Did not name the 3 bugs in E; did not report actual output for C |
| 2026-10-05 | Day 4 Quiz | 5/5 (100%) | Re-tested aliasing and sort() successfully |
| 2026-10-05 | Day 4 Part C update | Self-reported done | Code not reviewed by instructor |
| 2026-10-05 | Day 5 Lab | A 7/8 (.get() returns None, not error), B small miss (4 skills not 3), C missing, D correct, E bugs named but lamp line left crashing, F(1) union missing, G correct | Pattern: missing requirements and describing fixes in comments instead of applying them |
| 2026-10-05 | Day 5 Quiz | 5/5 (100%) | |
| 2026-10-05 | Day 5 fixes (C, E, F1) | Self-reported done | Code not reviewed by instructor |
| 2026-10-06 | Day 6 Lab | A all correct but missed that show(4) prints 8 as a side effect; B/C/D/E/G correct; F had a hidden bug (checked 'not all digits' instead of 'has a digit') that passed the 4 given tests | Needed one-rule-per-test design to expose the bug; named all bugs in E correctly |
| 2026-10-06 | Day 6 Quiz | 5/5 (100%) | |
| 2026-10-06 | Day 6 Part F fix | Self-reported done; explained any(ch.isdigit() for ch in password) correctly | Code not reviewed by instructor |

## Weak spots to revisit
- Value vs. type: quotes make something a str (re-check in Day 2 with comparisons like "5" == 5)
- `and`/`or` don't distribute: each side needs a full condition (Day 2 Part D). Fix: `if not username or not password:`
- Reading code for ALL errors, not just the first ones spotted (syntax: missing colons, indentation)
- Tracing code by hand (trace table: one row per loop iteration)
- Off-by-one with range (stop value is excluded)
- Indentation decides what is inside a loop/if
- Verify before submitting: run with known input, compare actual vs expected
- Aliasing: b = a shares the list, use .copy() (re-tested OK in Day 4 quiz)
- In-place methods return None: sort() vs sorted() (re-tested OK in Day 4 quiz)
- Re-read the requirements and check every item before submitting
- Name each bug found, don't just fix it silently
- Completeness: copy each requirement into a checklist comment and tick it only when code produces it (flagged Day 4 and Day 5)
- Apply fixes in code, don't just describe them in comments
- Use 4 spaces for indentation, not tabs
- Passing tests don't prove correctness: design each test to break exactly one rule
- Side effects: a function with print inside prints whenever it is called
- Flag the line you're least sure about in predictions (skipped Days 4-6)
- Call each function at least twice / test every branch
- Descriptive variable names (snake_case, say what the value IS)
# Python → Playwright Automation: Progress Tracker

**Started:** 2026-10-05
**Current position:** Phase 1 · Day 11 (not started)
**Last updated:** 2026-10-06 (Day 10 complete)

---

## Phase 1 — Python fundamentals and setup (1–3 weeks)
- [x] Day 1: Setup, print, variables, data types, input, f-strings
- [x] Day 2: Conditionals and comparison operators
- [x] Day 3: Loops (for, while, range)
- [x] Day 4: Lists and tuples
- [x] Day 5: Dictionaries and sets
- [x] Day 6: Functions
- [x] Day 7: Modules and imports
- [x] Day 8: File I/O
- [x] Day 9: Exceptions
- [x] Day 10: Virtual environments and pip
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
| 2026-10-06 | Day 7 Lab | A 4/5 (json.dumps returns str; correctly flagged that line), B sqrt(4) instead of sqrt(144), C multiply used + instead of *, D guard correct, E fixes right but error types not named, F misread the true/True question, G Counter(text) counted characters instead of words | Everything was commented out so nothing could be verified; claimed 'same result' without comparing |
| 2026-10-06 | Day 7 Quiz | 4/5 (80%) | Missed ImportError vs ModuleNotFoundError |
| 2026-10-06 | Day 7 fixes (B, C, F, G) | Self-reported done | Code not reviewed by instructor |
| 2026-10-06 | Day 8 Lab | A modes understood but line counts wrong (2 and 3 lines, not 4 and 5); B printed 'number: 1: A' instead of '1: A'; C never printed total words; D correct; E worked via dumps/loads but never printed final result; F misdiagnosed bug 1 (reading a 'w' file -> io.UnsupportedOperation) so fix still crashed; G wrote log.txt not test_run.log and mixed relative/script-folder paths | Concepts solid; requirement-matching and self-testing still the gap |
| 2026-10-06 | Day 8 Quiz | 4/5 (80%) | Missed json.dump(data, f) vs json.load(f) argument order |
| 2026-10-06 | Day 8 fixes (B, C, E, F, G) | Self-reported done | Code not reviewed by instructor |
| 2026-10-06 | Day 9 Lab | A check() output perfect but exception names 2/6 (int("1.5") is ValueError, {}["a"] is KeyError, [1,2][5] is IndexError, int("12") raises nothing); B/C ok (B didn't test " 7 "); D returned readlines()/error string instead of text/None; E misplaced runtime error (bare except hid it, TypeError at result + 1); F tester missing, 0 wrongly rejected; G not in run_tests(), no edge cases; H finally: raise made retry never retry | Hardest topic so far; exceptions vocabulary and finally semantics need practice |
| 2026-10-06 | Day 9 Quiz | 5/5 (100%) | |
| 2026-10-06 | Day 9 fixes (D, E, F, G, H) | Self-reported done | Code not reviewed by instructor |
| 2026-10-06 | Day 10 Lab | A mostly right (A3 gave freeze command instead of file name + install -r); B good evidence (venv active, folder named env); C worked but failure path (bad domain) untested; F printed a sentence instead of 'requests installed: False'; E 2/3 (PowerShell policy explanation wrong: it blocks script files, not installs); D and G done privately | Best delivery so far: code run, real output pasted |
| 2026-10-06 | Day 10 Quiz | 5/5 (100%) | |
| 2026-10-06 | Day 10 fixes (A3, C, F, E3) | Self-reported done | Not reviewed by instructor |

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
- Import error types: ImportError (name missing inside module) vs ModuleNotFoundError (module missing) vs NameError
- 'Same result' needs evidence: print outputs side by side
- Use the exact input the task gives (e.g. 144, not 4)
- json.dump(data, f) writes to file; json.load(f) reads from file (dumps/loads for strings)
- Match task requirements exactly (filenames, print formats, every requested print)
- Diagnose errors from the message, bottom up (e.g. reading a 'w' file raises io.UnsupportedOperation)
- Exception names: KeyError (dict), IndexError (list), ValueError (right type, wrong content), TypeError (wrong type)
- Never put raise/return in finally; no bare except; return None for 'nothing found' not an error string
- Test the failure path of any try/except (trigger the except branch on purpose)
- Match expected output wording exactly
- venv folder convention: .venv (learner used env)
- Descriptive variable names (snake_case, say what the value IS)
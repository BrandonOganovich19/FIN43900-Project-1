# FIN 43900 Project 1: Accenture plc (ACN)

**Committee question:** should the fund initiate a position in Accenture, place it on watch/defer, or not initiate?
**Current call: WATCH-DEFER.** The model value range is **$171.72–$186.24 per share** (base $182.00) across management's guided FY2027 organic growth. ACN closed at **$229.68 on Oct 16, 2026**, above the whole range. Edition A's own triggers, scored against the FY2026 results, land on HOLD WATCH.

> Educational project for FIN 43900 (AI in Finance, Purdue). Not investment advice. I am not a financial advisor.

## Decision frame

| Item | Value |
| --- | --- |
| Intended user | Investment committee / portfolio manager of a buy-side fund with no ACN position (course scenario) |
| Decision | Initiate, watch/defer, or do not initiate |
| Decision horizon | Initiation decision now; monitoring through Q2 FY2027 results (about March 2027) [confirm] |
| Target / security | Accenture plc Class A ordinary shares, NYSE: ACN |
| Fiscal year | Ends August 31 |
| Valuation date | Model opening balance sheet Aug 31, 2025 (FY2025 10-K); market price as of Oct 16, 2026 |
| Currency and units | USD; statements in USD millions; per-share values in USD |
| Share basis | Lab 10 model: 612M total shares outstanding at May 31, 2026 (basic count). Reverse DCF: 615.593M diluted weighted average. FY2026 10-K: ~595.8M outstanding at Aug 31, 2026. [Edition B: state the basis used] |
| Exclusions | No acquisition spend or bought growth (organic-only forecast); no transaction comps (control/synergy context not defensible); Avanade minority interest via 1.9% earnings-share proxy; excess cash valued only through interest income; share-based pay treated as a real cost |
| Screening | Selected the target. It is not valuation evidence and did not determine the recommendation |

## Read the results without running anything

| File | What it shows |
| --- | --- |
| [ACN_Lab10.md](ACN_Lab10.md) | Source-traced history (L21-46), ratios (L50-79), assumption table (L81-114), output and check block (L140-182), partner review (L184-203), limitations (L218-228) |
| [ACN_Lab11_output.txt](ACN_Lab11_output.txt) / [UTF-8 copy](ACN_Lab11_output_utf8.txt) | Every sensitivity scenario, all 30 balance and cash checks, restored-base check (L76-77) |
| [ACN_Lab11.md](ACN_Lab11.md) | Sensitivity tables, locked changed-input record (L20-26), partner exchanges (L75-113) |
| [ACN_EditionB_checks_output.txt](ACN_EditionB_checks_output.txt) | Boundary, monotonicity, Ke x g grid, break-evens, guided-growth values, mechanical sensitivities |
| [ACN_FY2026_release_check.md](ACN_FY2026_release_check.md) | FY2026 figures with source quotes, Edition A trigger scoring, prices, FY2026 10-K reconciliation |
| [accenture_comps.md](accenture_comps.md) / [accenture_comps_pe_output.txt](accenture_comps_pe_output.txt) | Peer policy written before search, P/E range $177.27-$220.65, earnings-basis check |
| [cold_run_log.txt](cold_run_log.txt) | Clean end-to-end run in a fresh environment, with file hashes and PASS/FAIL |
| [VALIDATION_RECORD.md](VALIDATION_RECORD.md) | Every required validation, its evidence, and status |
| [ASSUMPTION_CHALLENGE_RECORD.md](ASSUMPTION_CHALLENGE_RECORD.md) | Each load-bearing driver: value, basis, challenge, evidence that would change it |
| [AI_USE_RECORD.md](AI_USE_RECORD.md) | Where AI was used, what it produced, what I verified or decided |

## Repository map

| File | Role | Stage |
| --- | --- | --- |
| ACN-2026-09-03.md | Edition A memo, unchanged | Edition A (Sep 3) |
| dcf.py | Week 3 generic FCFF DCF (not an Accenture valuation) | Week 3 |
| Accenture_Reverse_DCF_Analysis.md | First reverse DCF (qualified; see AI_USE_RECORD) | Sep 10 |
| comps_pe.py | Lab 07 ABG training P/E calculator, unchanged | Lab 07 |
| accenture_comps_pe.py | Same engine with the Accenture inputs from accenture_comps.md L48-62 | Edition B |
| accenture_comps.md | Accenture peer policy, P/E range, skeptic review | Sep 15-17 |
| proforma.py | Course ABG engine; known answer $291.75 | Lab 09 |
| accenture_proforma.py | Accenture five-year three-statement pro-forma and FCFE valuation | Lab 10 |
| accenture_sensitivity.py, ACN_Lab11_inputs.json, test_accenture_sensitivity.py | One-at-a-time sensitivity runner, inputs and locked prediction, tests | Lab 11 |
| lab 12.md | Presenter and reviewer notes after the FY2026 release | Lab 12 |
| ACN_EditionB_checks.py | Boundary, grid and break-even checks on the Lab 10 model | Edition B |
| cold_run.py | Runs every check and writes cold_run_log.txt | Edition B |
| [Edition B FCFF model, results file, memo] | FCFF DCF with WACC, terminal value, enterprise-to-equity bridge, EV multiple | Edition B |
| presentation/ | Video 1-3 decks | Edition B |

## Reproduce

Python 3, standard library only. From a fresh clone:

```
python cold_run.py
```

That runs, in order: `proforma.py`, `accenture_proforma.py`, `accenture_proforma.py --break-test` (expected to fail with a -238.3 gap), `accenture_sensitivity.py ACN_Lab11_inputs.json`, the unit tests, `accenture_comps_pe.py`, and `ACN_EditionB_checks.py`.

## Disclosed issues

- `comps_pe.py` holds the Lab 07 ABG inputs, although accenture_comps.md L48-62 describes Accenture inputs. `accenture_comps_pe.py` restores those inputs and reproduces the documented range. The original file is kept unchanged.
- ACN_Lab10.md L178 cites seven tests in `test_accenture_proforma.py`. [Commit that file, or this line stands as a known gap.]
- The Lab 11 locked prediction was analyst-assisted (ACN_Lab11.md L22). The human-authored, AI-off record is in LOCKED_CHANGED_INPUT_RECORD.md.
- `ACN_Lab11_output.txt` is UTF-16; `ACN_Lab11_output_utf8.txt` is an identical UTF-8 copy for browser reading.

## History

Original commit history, including both Edition A commits (8845144, aa1b17b) and the Lab 11 commit (67d5edb), is at [BrandonOganovich19/ACN-Research](https://github.com/BrandonOganovich19/ACN-Research/commits/main). The Brightspace Edition A receipt is the baseline of record.

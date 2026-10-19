# Validation record: Accenture (ACN), Project 1

Status: **[FROZEN on YYYY-MM-DD, after the final recording]**. Do not edit after freezing.

Each row is one validation the project spec requires. Evidence = file and line numbers in this repository.

| # | Required validation | What was done | Evidence | Status |
| --- | --- | --- | --- | --- |
| 1 | Synthetic / known-answer reconciliation | ABG training case rerun before the Accenture model; reproduces $291.75 per share, all years balance | ACN_Lab10.md L9; proforma.py; cold_run_log.txt | PASS |
| 2 | Independent source / definition check on a load-bearing input | FY2025 revenue $69,672,977K hand-checked in 10-K; capex $600.0M vs StockAnalysis $600.04M; provider operating income $10,854M vs filing $10,225.7M left unresolved, filing used; FY2026 optimization input $307.541M equals FY2026 10-K | ACN_Lab10.md L39-44, L65-75; ACN_FY2026_release_check.md L92-100 | PASS |
| 3 | Directional changed-input test written before execution | Growth 3% to 4% FY27-30: predicted direction up for operating profit, FCFE, value; all moved up | ACN_Lab11_inputs.json L2-7; ACN_Lab11.md L22-26 | PASS (direction) |
| 4 | Locked Changed-Input Record, human-authored and AI-off | Lab 11 record was analyst-assisted (ACN_Lab11.md L22), so it does not qualify. Edition B record is written by me with AI closed and committed before the run | LOCKED_CHANGED_INPUT_RECORD.md; commit [hash] | [OPEN until committed] |
| 5a | Pro-forma: balance sheet balances every year | Assets - liabilities - equity = 0.0, FY2026E-FY2030E, every scenario | ACN_Lab10.md L153-166; ACN_Lab11_output.txt L36-75; accenture_proforma.py L215-222 | PASS |
| 5b | Pro-forma: cash flow ties to balance-sheet cash | Cash is computed from the cash flow, never plugged; removing one cash-flow link breaks the balance by exactly that link (-238.3) | accenture_proforma.py L158-170; ACN_Lab10.md L170-176 | PASS |
| 5c | Pro-forma: base year reconciles to the filing | Opening balance sheet built from FY2025 10-K totals ($65,394.9M assets); model refuses to run if the opening sheet does not balance | ACN_Lab10.md L118-136; accenture_proforma.py L94-121 | PASS |
| 6 | DCF boundary / monotonicity | Value falls as discount rate rises, rises with growth and terminal growth; terminal growth >= discount rate blocked | ACN_EditionB_checks_output.txt L8-25 | PASS (FCFE, Ke); [FCFF/WACC: Edition B file] |
| 7 | Enterprise-to-equity bridge checks | Worked example: equity $108,221.3M + debt $5,142.3M - cash $10,165.2M = EV $103,198.3M | Accenture_Reverse_DCF_Analysis.md L26-35 | [Edition B FCFF bridge] |
| 8 | Peer-policy and multiple-definition consistency | Policy written before search; same date, currency, one-share price, reported GAAP EPS; adjusted-basis recheck $169.52-$179.11 keeps the finding | accenture_comps.md L7-19, L158, L170; accenture_comps_pe_output.txt | PASS (P/E); [EV multiple: Edition B] |
| 9a | Highest-risk failure test | Scenario contamination: deep copies per scenario; test asserts inputs unchanged and base restored within 1e-8 | test_accenture_sensitivity.py L15-38; ACN_Lab11_output.txt L76-77 | PASS |
| 9b | Cold-run log | One clean end-to-end run in a fresh environment, recorded | cold_run_log.txt (from python cold_run.py on a fresh clone) | [PASS after your recorded run] |
| 10 | AI output accepted / corrected / qualified / rejected with independent evidence | Sep 10 reverse DCF (-7.69% implied growth) qualified: placeholder CAPM inputs replaced with dated 5.11% / 1.09; 17.48% TTM cash margin vs FY2026 actual 15.6% (~12.8% after SBC) | Accenture_Reverse_DCF_Analysis.md L71-89; ACN_Lab10.md L107-108, L226; ACN_FY2026_release_check.md L29 | PASS |

---
title: Project 1 - Accenture plc (ACN), Edition B
subject: Accenture plc (NYSE: ACN)
author: Brandon
class: FIN 43900 AI in Finance
as_of: October 18, 2026
supersedes: Edition A (ACN-2026-09-03.md, kept unchanged)
---

# Accenture plc (ACN): Edition B Committee Memo

## 0. Evidence convention

Facts carry a source tag ([R#] below, or a repository file and line). My own arithmetic is marked **[calc]** and my judgments **[judgment]**. Model outputs name the file and lines that print them, so a grader can check every number without running code. USD millions unless stated; fiscal years end August 31.

---

## 1. Decision frame

| Item | Value |
| --- | --- |
| User | Investment committee of a buy-side fund holding no ACN position |
| Decision | Initiate, watch/defer, or do not initiate |
| Horizon | Decision now; monitored through Q2 FY2027 results (about March 2027) [judgment] |
| Security | Accenture plc Class A ordinary shares, NYSE: ACN |
| Valuation date | Aug 31, 2026 (opening balance sheet from the FY2026 Form 10-K, filed Oct 16, 2026) [R5] |
| Market price | $229.68, Oct 16, 2026 close [R4] |
| Currency and share basis | USD; 595.8M basic shares outstanding at Aug 31, 2026 (Class A issued less treasury, plus Class X) [R5, calc] |
| Exclusions | No acquisition spend or bought growth; no transaction comps; operating leases kept in operating costs (not added to debt); share-based pay treated as a real cost |

Screening selected Accenture as a test of whether AI grows demand for its work or squeezes pricing and margins. **Screening is not valuation evidence and did not determine this recommendation.** [lab 12.md L7-11]

---

## 2. Recommendation

### WATCH-DEFER: do not initiate at $229.68.

**Edition B value range: $197.17 to $227.49 per share, base $214.73** (five-year FCFF DCF, valuation date Aug 31, 2026) [ACN_EditionB_fcff_output.txt L42-46]. The price sits at the top of the range, 1.0% above even the high case. To justify it, revenue must grow about **4.96% a year** for FY2027-FY2031, against FY2027 guided organic growth of roughly 0.5-4.0% (midpoint about 2.25%) [L59-61; ACN_FY2026_release_check.md L39-40].

Two independent reasons support the call:

1. **Edition A's own triggers point to HOLD WATCH.** Scored clause by clause against the FY2026 results, INITIATE fails on organic growth, and every AVOID condition is unmet [ACN_FY2026_release_check.md L48-62].
2. **There is no margin of safety.** The market is already paying for the high case (organic growth at the top of guidance plus a 32.6% gross margin), before any quarter has shown it [judgment].

### Conditions and triggers

| Move to | Trigger (measurable, dated) |
| --- | --- |
| **INITIATE** | Price at or below about $197 (the low case), or two consecutive quarters of reported organic growth at 4% or more with Consulting book-to-bill at or above 1.0 (Q1 FY27 in Dec 2026, Q2 FY27 in Mar 2027) |
| **HOLD WATCH** | Organic growth 2-4%, overall book-to-bill above 1.10, operating margin tracking the 15.9-16.1% guide |
| **AVOID** | Organic growth below 2%; Consulting book-to-bill below 1.0 for a second quarter; a new optimization program on the FY2025 scale ($600M a year or more); any goodwill impairment on the FY2026 acquisition cohort |

---

## 3. How Edition B fixes Edition A

Edition A stays unchanged as the baseline of record. Every gap it named or showed is closed below.

| # | Edition A weakness (line) | Edition B fix | Where |
| --- | --- | --- | --- |
| 1 | No DCF, so no view on terminal growth (L312) | Five-year FCFF DCF with WACC, Gordon terminal value and a full enterprise-to-equity bridge, driven by the pro-forma; terminal share stated (71.9%) | Section 6 |
| 2 | No date-matched peer set and no comp table (L314-318) | Peer policy written before search; P/E and EV/EBIT on one date, one currency, one share basis | Section 7 |
| 3 | No organic-growth decomposition (L256, L319) | Organic = local-currency guidance less the CFO's 2-2.5% inorganic contribution: about 0.5-4.0% | Section 4 |
| 4 | Two different INITIATE thresholds: >= 4% organic (L65) vs >= 5% (L371) | One trigger table; both thresholds scored, neither met | Sections 2, 4 |
| 5 | Margin trigger basis unclear ("adjusted margin", L65) | Scored on both bases: +50-70 bps GAAP, +10-30 bps adjusted | Section 4 |
| 6 | Triggers had no dates | Every trigger names the quarter or filing that tests it | Section 2 |
| 7 | Valuation rested on single numbers: 13.6x and a 9.7% FCF yield on guidance (L187, L195) | A range with causal low/base/high cases, a WACC x growth grid and a reverse DCF. The FCF yield is updated with actual FCF: $11.6B / $136.9B = 8.5% [calc] | Section 6 |
| 8 | Release date assumed, not confirmed (L364-369) | Release Oct 1, 2026 and 10-K Oct 16, 2026 confirmed; base year reconciled to the audited 10-K | Sections 5, 6 |
| 9 | Fiscal-year labels confusing ("forward" multiple on a finished year, L43-45) | FY2026 actuals and FY2027 guidance labeled explicitly; valuation date and fiscal calendar stated | Sections 1, 5 |
| 10 | User framed as a personal class exercise; no valuation date, horizon or share basis (L25) | Committee decision frame: user, horizon, valuation date, currency, share basis, exclusions | Section 1 |
| 11 | "One-time" optimization costs accepted as one-off (L109-111) | Treated as a recurring risk: $600M a year in the low case | Section 6 |
| 12 | AI thesis test set but not yet scorable (L293-302) | Scored: book-to-bill 1.2, margin guided up, revenue per person rose; Consulting book-to-bill 1.0 is the open warning | Section 4 |

---

## 4. What changed since Edition A

Edition A (Sep 3, 2026) said watch-defer and named the triggers in advance [ACN-2026-09-03.md L61-67]. The FY2026 release (Oct 1) and the FY2026 10-K (Oct 16) answered most of them:

| Edition A clause | Threshold | Evidence | Result |
| --- | --- | --- | --- |
| INITIATE: FY27 organic LC guidance | >= 4% | 3-6% LC less 2-2.5% inorganic = about 0.5-4.0%, midpoint about 2.25% [R1, R2, calc] | Not met |
| INITIATE: Q4 book-to-bill | >= 1.10 | 1.2 ($22.17B bookings / $18.68B revenue) [R1, R2] | Met |
| INITIATE: adjusted margin flat-to-up | flat-to-up | FY27 15.9-16.1%: +50-70 bps GAAP, +10-30 bps adjusted [R1] | Met |
| INITIATE: acquisition spend down from $9B | down | About $5B planned for FY27; FY26 cash actually spent was $4.94B [R1, R2] | Met as written; flat vs actual |
| HOLD WATCH: guidance 2-4%, bookings recovering, M&A elevated | all three | Organic midpoint about 2.25%; book-to-bill 1.2; about $5B M&A | **Matches** |
| AVOID: LC guidance < 2% / second book-to-bill near 1.0 / impairment | any | 3-6%; Q4 1.2; none reported | Not triggered |

I own one inconsistency: Edition A's table says >= 4% organic (L65), but its closing line says >= 5% (L371). I score against the table. Neither threshold is met.

**Edition A's AI thesis test** (L293-302) said the thesis is validated if book-to-bill recovers above 1.10, adjusted margin expands and revenue per employee rises. All three now hold: book-to-bill was 1.2, margin is guided +10-30 bps adjusted, and management said "we increased revenue per person this year" [R2]. The test also named a falsifier: Consulting stalling while AI announcements grow. Consulting's Q4 book-to-bill of 1.0 (against 1.4 for Managed Services) is the one reading that still points that way, so it becomes a trigger [R2, judgment].

**What I changed my mind on:** bookings (answered for now at 1.2); organic growth (now quantifiable, and below my bar); optimization costs (a recurring risk, not a one-off); method (Edition A had no DCF). **What I did not change:** the call.

---

## 5. FY2026 evidence

| Item | FY2026 | Source |
| --- | --- | --- |
| Revenue | $74,183.4M (+6% USD, +5% LC, about 3% organic) | [R5 income statement; R2] |
| Operating income | $11,406.0M (15.4% GAAP; 15.8% adjusted) | [R5; R1] |
| Gross margin | 32.05% [calc] | [R5: revenue less cost of services $50,407.8M] |
| Business optimization | $307.5M (program completed Q1 FY26) | [R5; R1] |
| Free cash flow (company definition) | $11.6B | [R1] |
| Q4 book-to-bill | 1.2 overall; Consulting 1.0; Managed Services 1.4 | [R2] |
| Long-term debt | $9,998.7M (up from $5,034.2M) | [R5 balance sheet] |
| Shares outstanding | about 595.8M [calc] | [R5] |

The FY2026 10-K matches the Oct 1 release on revenue, operating income, the optimization charge and EPS ($13.56) [ACN_FY2026_release_check.md L87-100].

---

## 6. Valuation: five-year FCFF DCF

### Architecture

The Lab 10 three-statement engine (accenture_proforma.py, unchanged) is rolled forward to the audited Aug 31, 2026 balance sheet and projects FY2027E-FY2031E [ACN_EditionB_fcff.py]. The pro-forma's operating forecast drives the DCF. FCFF = EBIT x (1 - tax) + depreciation - capex - change in receivables + change in deferred revenue.

### Load-bearing drivers

| Driver | Value | Basis | Challenge | Evidence that would change it |
| --- | --- | --- | --- | --- |
| Revenue growth | 2.25% FY27, then 3.0% | FY27 guided organic midpoint; 3% long-run organic (Lab 10) | Price implies 4.96% | Reported organic growth, Q1-Q2 FY27 |
| Gross margin | 32.0% | FY26 32.05%; FY23-25 31.9-32.6% | AI pricing pressure on hours | Quarterly gross margin |
| Operating margin | 16.0% FY27 (calibrated), +about 10 bps a year | FY27 GAAP guide 15.9-16.1% [R1] | Guide assumes no new program | FY27 10-Qs |
| Receivable days / deferred revenue | 80.3 days; 38.4% of receivables | FY26 actual [calc] | DSO has drifted up | DSO in FY27 10-Qs |
| Tax rate | 25.5% | FY27 guide 24.5-26.5% [R1] | Pillar Two | FY27 effective rate |
| WACC | 10.10% | Ke 10.56% (5.11% + 1.09 x 5.0%); Kd 5.2% pre-tax; market weights 93/7 | ERP of 5.0% is a judgment | Dated ERP and beta |
| Terminal growth | 3.0% | Long-run nominal GDP | Carries 71.9% of value | Revenue per employee; Consulting growth |

The full record, including partner challenges, is in ASSUMPTION_CHALLENGE_RECORD.md.

### Bridge (base case) [ACN_EditionB_fcff_output.txt L29-40]

| Step | USD M |
| --- | ---: |
| PV of FY27-31 FCFF | 35,440.0 |
| PV of terminal value (71.9% of EV) | 90,525.8 |
| **Enterprise value** | **125,965.7** |
| - Debt | (10,111.8) |
| + Cash and short-term investments | 12,837.8 |
| + Non-current investments | 940.5 |
| - Noncontrolling interests (incl. redeemable) | (1,689.9) |
| **Equity value** | **127,942.4** |
| / Shares (basic) | 595.8M |
| **Value per share** | **$214.73** |

### Causal cases [L42-46]

| Case | Cause | Value |
| --- | --- | ---: |
| Low | AI substitution in Consulting: organic 0.5% (guide low) then 2%; "one-time" optimization recurs at $600M a year | $197.17 |
| Base | Guided organic midpoint 2.25%, then 3%; no new program | $214.73 |
| High | AI demand: organic 4.0% (guide high) every year; gross margin 32.6% (FY24 high) | $227.49 |

### WACC x terminal growth [L48-53]

| WACC \ g | 2.0% | 3.0% | 4.0% |
| --- | ---: | ---: | ---: |
| 9.10% | $221.86 | $249.48 | $287.92 |
| 10.10% | $194.68 | **$214.73** | $241.35 |
| 11.10% | $173.48 | $188.56 | $207.90 |

Value falls with WACC and rises with growth in every row and column. Terminal growth at or above WACC is refused [L55-57].

### Reverse DCF [L59-61]

At $229.68, FY27-31 revenue growth would need to be **4.96% a year**, with everything else at base. That is about twice the guided organic midpoint and above FY26's roughly 3%. This replaces the two earlier reverse DCFs: Sep 10 implied -7.69% on placeholder inputs, and Lab 12 implied about 1.90% on the FCFE model at $177.41.

---

## 7. Cross-checks, and why the methods disagree

| Method | Date | Result | What it answers |
| --- | --- | --- | --- |
| FCFF DCF (Edition B) | Aug 31, 2026 | $197.17-$227.49 | Intrinsic value of operations, rolled forward |
| FCFE DCF (Lab 10-11) | Aug 31, 2025 base | $171.72-$186.24 across guided organic growth | Same engine, older base year, equity flows at Ke [ACN_EditionB_checks_output.txt L40-43] |
| P/E (CTSH, EPAM) | Oct 10, 2025 | $177.27-$220.65 | What the market paid for comparable earnings [accenture_comps.md L106] |
| EV/EBIT (CTSH, EPAM) | Oct 10, 2025 | $183.74-$216.04 | Same peers, enterprise basis [accenture_ev_multiple_output.txt L9-11] |

**I do not average these.** They differ for identifiable reasons:

- **The FCFE model is one year older.** It starts from the FY2025 balance sheet and a $72.46B FY26 forecast. Actual revenue was $74.18B.
- **FCFE versus FCFF.** On the same rolled-forward rows, FCFE gives $191.80 and FCFF gives $214.73. About $12.90 of the gap is the discount rate (Ke 10.56% versus WACC 10.10%). The other $10.03 comes from financing flows inside FCFE: after-tax interest on $10.1B of debt and buyback-driven cash drawdown, versus net cash and book NCI in the FCFF bridge [ACN_EditionB_fcff_output.txt L63-68].
- **The multiples are relative and a year old.** They rest on two peers whose earnings are about nine months staler. Accenture traded above both peers on both multiples (19.83x P/E, 14.38x EV/EBIT).

At $229.68, Accenture trades at about 16.4x FY26 adjusted EPS [ACN_FY2026_release_check.md L82], and its company-defined FCF yield is about 8.5% ($11.6B / $136.9B) [calc], down from Edition A's 9.7% at $187.68. That's context, not a like-for-like comparison.

---

## 8. Downside case and what flips the call

**Named downside:** AI substitution keeps Consulting flat (Q4 Consulting book-to-bill was only 1.0), and "one-time" optimization costs recur, as they did in FY23-FY26 ($1,063M, $438M, $615M, $307.5M). The low case gives **$197.17, 14% below the price** [calc].

The price is already above the range, so the downside confirms the call rather than flipping it. **What flips the call to INITIATE:** a price near or below the low case (about $197), or evidence that organic growth of about 5% is sustainable. That second route needs two quarters of reported organic growth at 4% or more.

---

## 9. Validation

All required validations are mapped to evidence in VALIDATION_RECORD.md. Highlights:

- **Known answer:** the ABG training case reproduces $291.75.
- **Articulation:** every forecast year balances, in both the Lab 10 model and the rolled-forward model [ACN_EditionB_fcff_output.txt L23-27]. The opening balance sheet reconciles to the 10-K [L4-8]. Cash comes from the cash flow, and the break test shows the gap equals the removed link (-238.3).
- **Boundary and monotonicity:** checked on both the FCFE model (Ke) and the FCFF model (WACC).
- **Bridge:** the arithmetic re-adds exactly [L40].
- **Peer policy:** P/E and EV/EBIT use the same date, peers and share basis.
- **Highest-risk test:** scenario contamination is ruled out; the base restores within 1e-8.
- **Cold run:** python cold_run.py runs every check and writes cold_run_log.txt.
- **AI output qualified:** the Sep 10 reverse DCF.
- **Locked Changed-Input Record:** human-authored and AI-off, in LOCKED_CHANGED_INPUT_RECORD.md.

---

## 10. Limitations

- **Terminal value carries 71.9% of value.** A one-point change in WACC moves the base from $188.56 to $249.48.
- **The model's forecast scope is narrow.** It is organic only and spends nothing on acquisitions, yet Accenture plans about $5B for FY27. Inorganic growth is excluded on purpose, because the model doesn't pay for it.
- **Non-operating items use simple bases.** NCI is at book value; operating leases stay in operating costs; non-current investments are at book.
- **The share count is basic.** At 595.8M, the per-share value would be about 1-2% lower on a diluted count [judgment].
- **Timing is close but not exact.** The valuation date is Aug 31, 2026 and the price is from Oct 16, 2026, about seven weeks apart.
- **The peer set is small and dated.** The multiples rest on two peers as of Oct 2025, with denominators about nine months staler than Accenture's.

---

## 11. AI-use disclosure

AI was used as acceleration. The judgments in this memo are mine: the call, the triggers, the assumption choices and the decision not to average methods. Claude (Anthropic) helped build ACN_EditionB_fcff.py, ACN_EditionB_checks.py, accenture_ev_multiple.py and cold_run.py, compile the FY2026 source check, and draft this memo. I verified the figures against the filings. The full record is in AI_USE_RECORD.md. Edition A remains unchanged as the baseline of record.

---

## Sources

- **[R1]** Accenture, [Q4 and full-year FY2026 earnings release](https://investor.accenture.com/~/media/Files/A/accenture-v4/investors/earnings-reports/2026/accentures-fourth-quarter-fiscal-2026-earnings-release.pdf), Oct 1, 2026.
- **[R2]** [Q4 FY2026 earnings call transcript](https://www.fool.com/earnings/call-transcripts/2026/10/01/accenture-acn-q4-2026-earnings-call-transcript/), Oct 1, 2026 (confirm against Accenture's IR transcript).
- **[R3]** [Accenture FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1467373/000146737325000217/acn-20250831.htm).
- **[R4]** [ACN price history](https://stockanalysis.com/stocks/acn/history/), StockAnalysis, Oct 16, 2026 close.
- **[R5]** [Accenture FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/1467373/000146737326000049/acn-20260831.htm), filed Oct 16, 2026: [balance sheet](https://www.sec.gov/Archives/edgar/data/1467373/000146737326000049/R3.htm), [income statement](https://www.sec.gov/Archives/edgar/data/1467373/000146737326000049/R5.htm).
- **[R6]** Cognizant FY2024 Form 10-K: [operations](https://www.sec.gov/Archives/edgar/data/1058290/000105829025000017/R5.htm), [financial position](https://www.sec.gov/Archives/edgar/data/1058290/000105829025000017/R3.htm).
- **[R7]** EPAM FY2024 Form 10-K: [income](https://www.sec.gov/Archives/edgar/data/1352010/000135201025000007/R5.htm), [balance sheet](https://www.sec.gov/Archives/edgar/data/1352010/000135201025000007/R3.htm).

This memo was written for FIN 43900 (AI in Finance, Purdue) as a learning exercise. It is not investment research and it is not financial advice.

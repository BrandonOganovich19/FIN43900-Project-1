# AI-use record: Accenture (ACN), Project 1

Status: **[FROZEN on YYYY-MM-DD, after the final recording]**.

AI was used as acceleration. The judgments are mine: the call, the triggers, every assumption choice, and the decision not to average valuation methods.

## Boundary

Edition A (ACN-2026-09-03.md) was submitted at the Brightspace checkpoint on [date/time of receipt]. Its own disclosure (L377): "drafted with ChatGPT/Codex, resumed from my Lab 03 session; sources gathered and verified by me; the judgments are mine." [Confirm this is consistent with the "AI Closed" checkpoint rules; if unsure, ask the instructor before submitting.]

## Record

| Work | AI tool (as disclosed) | What the AI did | What I did or verified | Record |
| --- | --- | --- | --- | --- |
| Edition A memo (Sep 3) | Codex and Claude  | Drafted the memo from my Lab 03 session | Gathered and verified sources; made the watch-defer call and wrote the triggers | ACN-2026-09-03.md L377 |
| Reverse DCF (Sep 10) | Codex and Claude  | Built the reverse DCF and Excel formulas | Qualified: placeholder CAPM inputs and 17.48% TTM cash margin; not used as evidence | Accenture_Reverse_DCF_Analysis.md L71-89 |
| Peer comps (Sep 15-17) | Codex and Claude  | Proposed peer candidate names | Wrote the policy before search; opened every primary source; set aside Capgemini, Infosys, IBM | accenture_comps.md L19, L31 |
| Lab 10 model (Sep 24) | Codex and Claude  | Adapted the ABG engine; attacked the optimization assumption | Chose every assumption; kept $0 and disclosed the $173.44 case | accenture_proforma.py L319; ACN_Lab10.md L186-197 |
| Lab 11 sensitivity (Sep 29) | Codex and Claude | Runner, tests, locked prediction (analyst-assisted) | Disclosed that the prediction was not mine; reconciled the miss | ACN_Lab11.md L22, L129 |
| Edition B checks, release check, records, decks, scripts (Oct 8-18) | Codex and Claude  | ACN_EditionB_checks.py, cold_run.py, accenture_comps_pe.py; FY2026 source compilation; record templates; slide and script drafts | [Verified each FY2026 figure against the release, call transcript and 10-K; reviewed every slide claim] | ACN_FY2026_release_check.md L102 |
| Edition B FCFF model and memo | [tool, or none] | [what it did] | [what I did] | [file] |
| Edition B changed-input prediction | None (AI off) | None | Written and committed by me before the run | LOCKED_CHANGED_INPUT_RECORD.md; commit [hash] |

## One AI output, evaluated

The Sep 10 reverse DCF concluded that $175.80 implied -7.69% annual revenue growth for ten years. **Qualified.** Independent evidence: the file flags its own CAPM inputs as undated placeholders (L77-78), replaced with the 5.11% Treasury yield (Sep 23, 2026) and 1.09 beta (ACN_Lab10.md L107-108). Its 17.48% trailing cash margin compares with FY2026 actual free cash flow of $11.6B on $74.18B revenue (15.6%), about 12.8% after ~$2.1B of share-based pay.

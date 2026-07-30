# TIA Section → Source Reading Content Map

TIA (The Infinite Actuary) is a study provider for CAS Exam 8. TIA's practice questions
(see `study/practice_questions/`) are organized by **TIA section** (A1, A2, B1, B2, ...),
which does **not** match the source-material paper/chapter structure used in
`study/readings/`. This file is the authoritative cross-reference between the two.

**Use this map whenever a task is scoped by TIA section** (e.g. "quiz me on B3",
"what does section D5 cover") to find the correct files in `study/readings/` before
answering. For concept-scoped questions, use `study/concepts/index.md` instead.

## Map

| TIA Section | Topic (per TIA) | Source Reading(s) | Files |
|---|---|---|---|
| **A1** | Workers Comp background | *Not in source material* — background/context only | — |
| **A2** | Experience rating, risk sharing (intro) | Fisher et al., Ch. 2 | `study/readings/fisher_et_al/02_ch02_risk_sharing_and_loss_sensitive_plans.md` |
| **B1** | Claim size, claim counts, aggregate claims | Bahnemann, Ch. 1–4 | `study/readings/bahnemann/1_ch1_introduction.md`, `2_ch2_claim_size.md`, `3_ch3_claim_counts.md`, `4_ch4_aggregate_claims.md` |
| **B2** | Excess claims | Bahnemann, Ch. 5 | `study/readings/bahnemann/5_ch5_excess_claims.md` |
| **B3** | Limits and deductibles | Bahnemann, Ch. 6 | `study/readings/bahnemann/6_ch6_limits_and_deductibles.md` |
| **B4** | Aggregate excess loss cost estimation, concluding remarks | Fisher et al., Ch. 3–4 | `study/readings/fisher_et_al/03_ch03_aggregate_excess_loss_cost_estimation.md`, `04_ch04_concluding_remarks.md` |
| **C1** | Experience rating; case study application | Fisher et al., Ch. 1 + Fisher case study (Step 3) | `study/readings/fisher_et_al/01_ch01_experience_rating.md`; case study is **not converted to Markdown** — see `source_pdfs/fisher_et_al_case_study.xlsx` (gap, see below) |
| **C2** | ISO manual rules | ISO manual | *Not in current folder structure* (gap, see below) |
| **C3** | Credibility / experience rating structure | Mahler | `study/readings/mahler/` (all files, `01_s01_introduction.md` through `15_appendices.md`) |
| **C4** | Credibility (Bühlmann, classification ratemaking) | Bailey & Simon | `study/readings/bailey_&_simon.md` |
| **D1** | ASOP on ratemaking | ASOP 12 | `study/readings/asop_12.md` |
| **D2** | Credibility procedure development/testing | Couret & Venter | `study/readings/couret_&_venter/` (all files) |
| **D3** | GLMs for insurance rating | Goldburd et al., *Generalized Linear Models for Insurance Rating* | `study/readings/goldburd_et_al/` (all files) |
| **D4** | ASOP on credibility | ASOP 25 | *Not in current folder structure* (gap, see below) — note: `study/readings/holmes_&_casotto/11_appendix_b_alignment_with_asop_25.md` discusses alignment **with** ASOP 25 but is not the standard itself |
| **D5** | Penalized regression, lasso credibility | Holmes & Casotto | `study/readings/holmes_&_casotto/` (all files) |
| **D6** | GLM case studies / practical challenges | Chalk et al. | `study/readings/chalk_et_al/` (all files) |

## Known Gaps

Material TIA covers that has no corresponding file in `study/readings/`:

- **A1** — Workers comp background is supplemental/context only; not tied to an assigned reading.
- **C1** — The Fisher et al. companion case study (referenced in the paper as an exhibit-driven
  worked example) exists only as `source_pdfs/fisher_et_al_case_study.xlsx` and has not been
  converted to Markdown. TIA's "Step 3" refers to a step within that workbook.
- **C2** — The ISO manual is not part of this workspace at all.
- **D4** — ASOP 25 itself is not present as a reading. Only a secondary discussion of alignment
  with ASOP 25 exists (`holmes_&_casotto/11_appendix_b_alignment_with_asop_25.md`).

When a question touches one of these gaps, say so explicitly rather than answering from
outside knowledge without disclosure (per the "Answering Exam Content Questions" rule in
`CLAUDE.md`).

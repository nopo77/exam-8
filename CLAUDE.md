# Exam 8 — Project Context

CAS Exam 8 actuarial exam study workspace. All source material has been converted to Markdown for AI-assisted study.

## Folder Structure

```
Exam 8/
├── CLAUDE.md                       — this file
├── README.md                       — project overview
├── Study Hours Tracker.xlsx        — personal study log
│
├── source_pdfs/                    — original PDFs (READ-ONLY)
├── source_mds/                     — PDFs converted to Markdown (READ-ONLY)
│
└── study/                          — working copies for AI-assisted study
    ├── syllabus.md
    ├── word_counts.md
    ├── concepts/
    │   └── index.md               — cross-reference map: concept → files that cover it
    ├── flashcards/                 — generated Anki flashcard CSVs
    └── readings/                   — all source papers
        ├── asop_12.md
        ├── bailey_&_simon.md
        ├── bahnemann/              — multi-chapter papers are split into files
        ├── chalk_et_al/
        ├── couret_&_venter/
        ├── fisher_et_al/
        ├── goldburd_et_al/
        ├── holmes_&_casotto/
        └── mahler/
```

## Source Texts

All source papers live under `study/readings/`.

| File/Folder | Author(s) | Notes |
|---|---|---|
| `asop_12.md` | Actuarial Standards Board | ASOP No. 12 |
| `bahnemann/` | Bahnemann | Errata applied 2026-06-26 |
| `bailey_&_simon.md` | Bailey & Simon | Discussion merged in |
| `chalk_et_al/` | Chalk et al. | |
| `couret_&_venter/` | Couret & Venter | |
| `fisher_et_al/` | Fisher et al. | |
| `goldburd_et_al/` | Goldburd et al. | Errata applied 2026-06-26 |
| `holmes_&_casotto/` | Holmes & Casotto | Errata applied 2026-06-26 |
| `mahler/` | Mahler | |
| `syllabus.md` | CAS | Exam 8 syllabus |

## File Structure in study/

Every substantive chapter file has been enriched with a YAML frontmatter block and a TL;DR summary. The schema is:

```yaml
---
paper: <snake_case paper name>
chapter: <integer, or null for single-file readings>
title: <chapter title as it appears in the first heading>
topics: [<snake_case concept tags>]
key_formulas: [<named formulas or estimators>]
---
```

Immediately after the frontmatter, each file has a TL;DR block:

```
> **TL;DR**
> - <exam-focused bullet>
> - ...
```

The body content follows unchanged after the TL;DR.

## Answering Exam Content Questions

When answering any question about exam content (concepts, formulas, methods, derivations, distinctions):

- **Pull exclusively from `study/readings/`**. Do not rely on training knowledge to answer.
- If outside knowledge is used (e.g., to fill a gap not covered in the readings), **explicitly disclose it** — state that the information comes from outside the assigned readings.

## Navigation Strategy for AI Agents

When answering a question that may span multiple files:

1. **Start with `study/concepts/index.md`** — look up the relevant concept to find which files cover it, rather than scanning all files blindly.
2. **Read the frontmatter and TL;DR first** — this fits in a fraction of the context of the full chapter and usually tells you whether the file is relevant.
3. **Read the full chapter body** only if the TL;DR confirms it contains what you need.
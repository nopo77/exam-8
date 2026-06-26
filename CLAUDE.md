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
└── modified_mds/                   — working copies for AI-assisted study
    ├── changelog.md                — log of every change made in this folder
    ├── syllabus.md
    ├── asop_12.md
    ├── bailey_&_simon.md
    ├── bailey_&_simon_discussion.md
    ├── mahler.md
    ├── bahnemann/                  — multi-chapter papers are split into files
    ├── chalk_et_al/
    ├── couret_&_venter/
    ├── fisher_et_al/
    ├── goldburd_et_al/
    └── holmes_&_casotto/
```

## Workflow Rules

- **Never modify** anything in `source_pdfs/` or `source_mds/`. These are original, unaltered sources.
- All edits go to `modified_mds/`. Files there are copies of `source_mds/` with `.pdf` removed from the name.
- **Every change** to any file in `modified_mds/` must be logged in `modified_mds/changelog.md`.
- Errata from `source_mds/*_errata.pdf.md` are applied directly into the corresponding `modified_mds/` file.

## Source Texts

| File/Folder | Author(s) | Notes |
|---|---|---|
| `asop_12.md` | Actuarial Standards Board | ASOP No. 12 |
| `bahnemann/` | Bahnemann | Errata applied 2026-06-26 |
| `bailey_&_simon.md` | Bailey & Simon | |
| `bailey_&_simon_discussion.md` | Bailey & Simon | Discussion paper |
| `chalk_et_al/` | Chalk et al. | |
| `couret_&_venter/` | Couret & Venter | |
| `fisher_et_al/` | Fisher et al. | |
| `goldburd_et_al/` | Goldburd et al. | Errata applied 2026-06-26 |
| `holmes_&_casotto/` | Holmes & Casotto | Errata applied 2026-06-26 |
| `mahler.md` | Mahler | |
| `syllabus.md` | CAS | Exam 8 syllabus |

## Custom Skills & Agents

Custom slash commands live in `.claude/commands/` and custom agents in `.claude/agents/`.

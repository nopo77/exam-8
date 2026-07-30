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
├── tia_pdfs/                       — original TIA lecture PDFs (READ-ONLY)
├── tia_excel/                      — original TIA practice workbooks (READ-ONLY, source of practice_questions/)
│
├── scripts/tia_convert/            — the tia_excel → practice_questions converter (see below)
│
└── study/                          — working copies for AI-assisted study
    ├── syllabus.md
    ├── word_counts.md
    ├── tia_content_map.md          — cross-reference map: TIA study section (A1, B3, D5, ...) → source reading files
    ├── concepts/
    │   └── index.md               — cross-reference map: concept → files that cover it
    ├── flashcards/                 — generated Anki flashcard CSVs
    ├── practice_questions/             — 348 TIA practice problems, one file each, by TIA section
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

## TIA Study Sections vs. Source Material

`study/practice_questions/` contains practice questions organized by **TIA (The Infinite
Actuary) study section** (e.g. A1, A2, B1–B4, C1–C4, D1–D6), which is a different
organizing scheme than the paper/chapter structure used in `study/readings/`.

- **When a task is scoped by TIA section** (e.g. a question from `practice_questions/`, or a
  request like "quiz me on section B3"), consult `study/tia_content_map.md` first to
  translate the TIA section into the correct file(s) under `study/readings/`.
- Some TIA sections (A1, C2, D4, and part of C1) have no corresponding file in this
  workspace — `study/tia_content_map.md` documents these gaps. Flag the gap rather than
  answering from outside knowledge without disclosure.

## File Structure in study/practice_questions/

348 problems converted from the `tia_excel/` workbooks — **one Markdown file per problem**,
so a task about a single problem never has to load a 90-problem workbook.

```
study/practice_questions/
├── images_manifest.json                    — every extracted image, with its class and transcription
└── section-b/B3_pricing_limits_layers_deductibles/
    ├── index.md                            — problem table for this TIA section
    ├── images/                             — extracted PNGs, named by content hash
    └── 21_2009_exam_9_q24.md               — NN_ prefix = TIA's own problem order
```

Each problem file carries YAML frontmatter and then `## Question`, `## Solution`, and
(where present) `## Examiner Report`. Useful frontmatter fields:

- `tia_section` / `tia_topic` — e.g. `B3`, `pricing_limits_layers_deductibles`
- `source` — `past_exam` or `practice_problem`; plus `exam_year`, `exam_number`,
  `question_number`, `points`, `parts`
- `good_problem` — TIA's own "recommended problem" flag (true on 200 of 348)
- `readings` — the `study/readings/` files this problem tests, per `tia_content_map.md`
- `split_confidence` — `clean`, or `review` on the 10 problems whose source sheet
  interleaved question and solution; content is complete either way, only the reading
  order may be off

Conventions inside the body:

- **Solution formulas are the real ones from the workbook**, rendered as
  `` value — `=SUMPRODUCT(...)` `` or collected in a `<details>Formulas</details>` block
  under a table. They encode the actual method — prefer them over re-deriving.
- **Images**: formula snippets and question exhibits have a text transcription inlined
  directly beneath them, so the PNG never needs opening. Scanned examiner-report pages
  are left as plain image links.

**When quizzing the user, read only the `## Question` section** and withhold the rest.

### Regenerating

`python scripts/tia_convert/emit.py` rebuilds everything from `tia_excel/`;
`python scripts/tia_convert/verify.py` checks it (asserts every source cell and formula
survives). Image transcriptions live in `scripts/tia_convert/transcriptions.py`, keyed by
image hash — add to that file and re-run `emit.py` rather than editing generated Markdown.
**Edits made directly to files under `study/practice_questions/` will be overwritten.**

## Navigation Strategy for AI Agents

When answering a question that may span multiple files:

1. **If the question is scoped by TIA section**, start with `study/tia_content_map.md` to find the relevant reading file(s).
   For practice problems in that section, use the `index.md` in the matching
   `study/practice_questions/section-*/` folder rather than listing the directory.
2. **Otherwise, start with `study/concepts/index.md`** — look up the relevant concept to find which files cover it, rather than scanning all files blindly.
3. **Read the frontmatter and TL;DR first** — this fits in a fraction of the context of the full chapter and usually tells you whether the file is relevant.
4. **Read the full chapter body** only if the TL;DR confirms it contains what you need.
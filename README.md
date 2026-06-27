# Exam 8 Study Materials

CAS Exam 8 actuarial exam source materials, organized for AI-assisted studying.

## How to Use This for Studying

**Ask questions on the readings**
Ask anything about the assigned papers — concepts, derivations, comparisons between methods — and the AI will answer exclusively from the source readings in `study/readings/`, citing the relevant paper and section.

**Answer exam problems with explained reasoning**
Paste any past CAS Exam 8 problem and the AI will work through it step by step, pulling the relevant formulas and reasoning directly from the readings, the same way you would on the actual exam.

**Generate flashcards**
Use the `/flashcards` command to produce Anki-importable CSV flashcards for any reading. Cards focus on testable, exam-style recall — formulas, key distinctions, and definitions.

---

**Coming soon**
- Generate original CAS-style exam questions modeled on the full history of past exam problems, for targeted practice on any reading or topic.

---

## Folder Structure

```
exam-8/
├── CLAUDE.md                    — AI agent instructions
├── README.md                    — this file
├── source_pdfs/                 — original PDFs (read-only)
├── source_mds/                  — PDFs converted to Markdown (read-only)
│
└── study/                       — working copies for AI-assisted study
    ├── syllabus.md              — CAS Exam 8 syllabus
    ├── word_counts.md           — word count summary by reading
    ├── concepts/                — cross-reference map: concept → readings that cover it
    ├── flashcards/              — generated Anki flashcard CSVs
    └── readings/                — enriched source papers (frontmatter + TL;DR added)
```

## Commands

| Command | Description |
|---|---|
| `/enrich-reading <name>` | Add YAML frontmatter and TL;DR summary to a reading, and update the concepts index |
| `/flashcards <name>` | Generate Anki-importable CSV flashcards for a reading |

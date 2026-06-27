# Exam 8 Study Materials

CAS Exam 8 actuarial exam source materials, organized for AI-assisted studying.

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

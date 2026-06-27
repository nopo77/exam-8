Generate Anki-importable flashcards for the Exam 8 reading "$ARGUMENTS", focused on testable, memorizable details.

## Step 1 — Locate the target files

Resolve "$ARGUMENTS" to files in `study/readings/` using this logic:

- If `study/readings/$ARGUMENTS/` is a directory → target all `.md` files inside it
- If `study/readings/$ARGUMENTS.md` exists → target just that one file
- If neither matches → list valid reading names from `study/readings/` and stop

From the resolved files, **skip**:
- Any file whose name starts with `00_` (table of contents files)
- Any file whose name contains `_references`, `_bibliography`, or `_abstract` unless it contains substantive content beyond citations
- `study/syllabus.md`, `study/concepts/index.md`

List the files you will process, then proceed.

## Step 2 — Read the content

For each target file, read it in full. Extract testable, memorizable content by looking for:

### Card Type 1 — Formulas
Any named formula, equation, or estimator. Generate one card per formula.
- **Front**: "State the [formula name] and define each term."
- **Back**: The formula in full, followed by a definition of every variable/symbol.

### Card Type 2 — Definitions
Any technical term, named distribution, named method, or named statistic that an exam candidate must know precisely.
- **Front**: "Define [term]."
- **Back**: A concise, precise definition (1–3 sentences). Include the context (which paper/author) if relevant.

### Card Type 3 — Criteria and Properties
Named criteria, conditions, or properties (e.g., Meyers/Dorweiler criterion, balance property, homogeneity requirement, Panjer (a,b,0) condition).
- **Front**: "State the [name] criterion / condition / property."
- **Back**: What the criterion requires, how to test it, and what it means if satisfied or violated.

### Card Type 4 — Testable Distinctions
Pairs or groups of concepts that are frequently confused or contrasted on exams (e.g., LASSO vs Ridge, Bühlmann vs classical credibility, between-variance vs within-variance, lognormal vs Pareto tail behavior).
- **Front**: "How does [X] differ from [Y] with respect to [dimension]?"
- **Back**: The key differentiator — one sentence each, no more.

### Card Type 5 — Specific Numerical Results
Concrete numbers, thresholds, or quantitative results stated in the text that an exam candidate might need to recall or apply (e.g., approximate credibility values from Bailey & Simon's tables, Panjer recursion starting condition, normal power skewness threshold).
- **Front**: "[Context]: what is [specific quantity]?"
- **Back**: The value, with a brief statement of what it represents.

## Step 3 — What NOT to generate

Do not generate cards for:
- Narrative motivation or historical background ("Why did Bailey & Simon study Canadian data?")
- Content that requires a paragraph-length answer to be useful
- Concepts that are better understood than memorized (high-level intuitions belong in the TL;DR, not flashcards)
- Duplicate cards — if two files cover the same formula or definition, generate the card only once

Aim for **5–15 cards per chapter file**. Prefer precision over volume.

## Step 4 — Write the CSV output

Determine the output filename:
- Single-file reading (e.g., `bailey_&_simon.md`) → `study/flashcards/bailey_&_simon.csv`
- Multi-chapter reading (e.g., `bahnemann/`) → one file per chapter: `study/flashcards/bahnemann_ch1.csv`, `bahnemann_ch2.csv`, etc., named after the source file's chapter number prefix

Create the `study/flashcards/` directory if it does not exist.

Write the CSV with this header row and one data row per card:

```
Front,Back,Tags
```

Formatting rules:
- Enclose every field in double quotes.
- If a field value contains a double quote, escape it as `""`.
- Tags field: space-separated list — always include the paper name (e.g., `bailey_simon`) and the card type (e.g., `formula`, `definition`, `criterion`, `distinction`, `numeric`). Add topic tags from the file's frontmatter where applicable.
- Newlines within a field: use ` | ` as a separator instead of actual newlines (Anki handles this better in CSV imports).
- For formulas: write them in plain text with standard notation (e.g., `Z = n / (n + k)`) rather than LaTeX — Anki's basic card type doesn't render LaTeX by default.

Example rows:
```
"State the Bühlmann credibility formula and define each term.","Z = n / (n + k), where: n = number of observed periods | k = EPV / VHM | EPV = Expected Value of Process Variance (within-class variance) | VHM = Variance of Hypothetical Means (between-class variance)","mahler formula credibility buhlmann_credibility"
"Define the complement of credibility.","The a priori estimate used when Z < 1 in the credibility formula: Modified rate = Z × (observed) + (1 − Z) × (complement). The complement represents the prior belief about the risk's true mean before incorporating experience.","mahler definition credibility complement_of_credibility"
"How does LASSO differ from Ridge with respect to variable selection?","LASSO (L1 penalty) drives some coefficients exactly to zero, performing variable selection. Ridge (L2 penalty) shrinks all coefficients toward zero but never zeros them out.","holmes_casotto distinction lasso penalized_regression"
```

## Constraints

- Never touch any file in `source_pdfs/` or `source_mds/`
- Do not modify any existing content in `study/readings/` — only write new files to `study/flashcards/` 
- If a flashcard CSV for this reading already exists, overwrite it (do not append)

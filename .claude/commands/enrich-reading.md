Enrich the Exam 8 reading "$ARGUMENTS" by adding YAML frontmatter, a TL;DR summary block, and updating the shared concepts index.

## Step 1 — Locate the target files

Resolve "$ARGUMENTS" to files in `modified_mds/` using this logic:

- If `modified_mds/$ARGUMENTS/` is a directory → target all `.md` files inside it
- If `modified_mds/$ARGUMENTS.md` exists → target just that one file
- If neither matches → list valid reading names from `modified_mds/` and stop

From the resolved files, **skip**:
- Any file whose name starts with `00_` (table of contents files)
- Any file whose name contains `_references` or `_bibliography` unless it contains substantive explanatory content beyond a citation list

List the files you will process, then proceed.

## Step 2 — Add frontmatter to each file

For each target file, check whether the file already starts with `---`. If it does, update the existing frontmatter fields in place. If it does not, prepend new frontmatter before the first line of content.

Use this exact schema:

```yaml
---
paper: <snake_case paper name matching the folder/file name, e.g. goldburd_et_al>
chapter: <integer chapter or appendix number; null for single-file readings>
title: <the chapter or section title exactly as it appears in the file's first heading>
topics: [<3–8 key actuarial or technical concepts covered, in snake_case>]
key_formulas: [<names of notable formulas, methods, or estimators covered; empty list [] if none>]
---
```

## Step 3 — Add a TL;DR block immediately after the frontmatter

Insert this block between the closing `---` of the frontmatter and the first line of existing content:

```
> **TL;DR**
> - <most important concept, result, or formula — stated concisely>
> - <second key point>
> - <third key point>
> - <fourth point if warranted>
> - <fifth point if warranted>
```

Keep bullets exam-focused: things a candidate needs to recall or apply, not prose summary. Aim for 3–5 bullets. Do not alter any existing content below the TL;DR.

## Step 4 — Update the concepts index

The shared index lives at `modified_mds/concepts/index.md`. If the file does not exist, create the `concepts/` directory and the file with this header:

```markdown
# Concepts Index

_Cross-reference of key actuarial concepts across all Exam 8 readings._

```

For each topic listed in the frontmatter you just wrote:

1. Find or create a `## <Topic Name>` heading (convert snake_case to Title Case, e.g. `bühlmann_credibility` → `## Bühlmann Credibility`). Keep headings sorted alphabetically.
2. Under that heading, add a link line if it does not already exist:
   ```
   - [<Paper display name> — <Chapter Title>](../path/to/file.md)
   ```
   Use a path relative from `modified_mds/concepts/` to the target file.

Do not duplicate links that are already present.

## Step 5 — Log every change to the changelog

Append one line per modified file to `modified_mds/changelog.md`, using this format:

```
- YYYY-MM-DD | enrich-reading | <path relative to modified_mds/> | added frontmatter + TL;DR
```

Add one additional line for the concepts index update:

```
- YYYY-MM-DD | enrich-reading | concepts/index.md | updated with topics from <paper name>
```

Use today's actual date.

## Constraints

- Never touch any file in `source_pdfs/` or `source_mds/`
- Do not rewrite, reorder, or reformat any existing body content — only prepend or update the frontmatter and TL;DR
- If a file already has frontmatter, update it rather than duplicating it
- If a file already has a TL;DR block, replace it with the newly generated one

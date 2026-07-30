"""Check the conversion without reading 348 files by hand.

The load-bearing checks are conservation ones: every non-empty source cell has
to land in exactly one region, and every formula and every piece of cell text
has to survive into the Markdown.

Run from the repo root:  python scripts/tia_convert/verify.py
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

from classify import EXAMINER, QUESTION, SOLUTION, is_problem_sheet, split_sheet
from emit import OUT, ROOT, SRC, slugify, workbook_id
from render import _BULLET_RE, is_part_label, normalize
from xlsx_reader import load_workbook

_WS = re.compile(r"\s+")


def canon(text: str) -> str:
    """Collapse a string so source cells and rendered Markdown compare equal."""
    t = normalize(text).replace("\\|", "|").replace("<br>", " ")
    return _WS.sub(" ", t).strip()


def main() -> int:
    problems = 0
    cells_read = cells_classified = 0
    formulas_read = formulas_found = 0
    text_missing: list[str] = []
    formula_missing: list[str] = []
    bad_files: list[str] = []
    counts = Counter()
    review: list[str] = []

    for path in sorted(SRC.glob("section-*/*.xlsx")):
        tia, topic = workbook_id(path)
        dest = OUT / path.parent.name / f"{tia}_{topic}"
        wb = load_workbook(str(path))

        order = {}
        idx = wb.by_name("Problem List")
        if idx is not None:
            for row, cs in idx.rows():
                if row >= 2:
                    first = next((c for c in cs if c.col == 1), None)
                    if first and first.text:
                        order[first.text.strip()] = row

        sheets = [s for s in wb.sheets if is_problem_sheet(s)]
        sheets.sort(key=lambda s: order.get(s.name, 10_000 + s.index))

        for n, sheet in enumerate(sheets, start=1):
            problems += 1
            md_path = dest / f"{n:02d}_{slugify(sheet.name)}.md"
            if not md_path.exists():
                bad_files.append(f"MISSING {md_path.relative_to(ROOT)}")
                continue
            md = md_path.read_text(encoding="utf-8")
            md_canon = canon(md)

            split = split_sheet(sheet)
            body = split.question + split.solution + split.examiner

            # -- conservation of cells -------------------------------------
            header = sum(
                1 for c in sheet.cells.values()
                if c.row == 1 or (c.col == 1 and c.row in (2, 3)
                                  and sheet.text_at("A2").strip().lower() == "points")
            )
            cells_read += len(sheet.cells) - header
            cells_classified += len(body)
            if len(set(id(c) for c in body)) != len(body):
                bad_files.append(f"DUPLICATE cell in {md_path.name}")

            # -- conservation of formulas and text -------------------------
            for c in body:
                if c.formula:
                    formulas_read += 1
                    f = c.formula.replace("_xlfn._xlws.", "").replace("_xlfn.", "")
                    if canon(f) in md_canon:
                        formulas_found += 1
                    elif len(formula_missing) < 15:
                        formula_missing.append(
                            f"{path.name}:{sheet.name}:{c.ref} {f[:60]}")
                if c.text and not c.numeric:
                    # Bullets lose their marker and part labels become
                    # headings, so compare against the rendered form.
                    label = is_part_label(c.text)
                    needle = canon(_BULLET_RE.sub("", normalize(c.text)))
                    found = needle in md_canon
                    if label and not found:
                        found = f"### Part {label}" in md
                    if needle and not found and len(text_missing) < 15:
                        text_missing.append(
                            f"{path.name}:{sheet.name}:{c.ref} {needle[:60]!r}")

            # -- structural invariants -------------------------------------
            if not md.startswith("---\n"):
                bad_files.append(f"NO FRONTMATTER {md_path.name}")
            for section in ("## Question", "## Solution"):
                if section not in md:
                    bad_files.append(f"NO {section} in {md_path.name}")
            if "_(no question text)_" in md:
                counts["empty_question"] += 1
            if "_(no solution text)_" in md:
                counts["empty_solution"] += 1

            m = re.search(r"^points: (.+)$", md, re.M)
            a3 = sheet.get("A3")
            want = f"{float(a3.raw):g}" if (a3 and a3.numeric) else "null"
            got = m.group(1).strip() if m else "?"
            if got != "null" and want != "null" and abs(float(got) - float(want)) > 1e-9:
                bad_files.append(f"POINTS MISMATCH {md_path.name} {got}!={want}")
            elif (got == "null") != (want == "null"):
                bad_files.append(f"POINTS MISMATCH {md_path.name} {got}!={want}")

            counts[split.confidence] += 1
            if split.confidence == "review":
                review.append(str(md_path.relative_to(OUT)))

    # -- image manifest ----------------------------------------------------
    manifest = json.loads((OUT / "images_manifest.json").read_text(encoding="utf-8"))
    missing_img = [m["file"] for m in manifest if not (OUT / m["file"]).exists()]
    on_disk = len(list(OUT.rglob("images/*")))
    by_class = Counter(m["class"] for m in manifest)

    md_files = len(list(OUT.rglob("*.md")))
    indexes = len(list(OUT.rglob("index.md")))

    print("=" * 66)
    print(f"problems converted        {problems}")
    print(f"markdown files            {md_files}  ({indexes} indexes + "
          f"{md_files - indexes} problems)")
    print(f"cells read / classified   {cells_read} / {cells_classified}"
          f"   {'OK' if cells_read == cells_classified else 'MISMATCH'}")
    print(f"formulas read / rendered  {formulas_read} / {formulas_found}"
          f"   {'OK' if formulas_read == formulas_found else 'MISMATCH'}")
    print(f"image anchors / on disk   {len(manifest)} / {on_disk}"
          f"   missing={len(missing_img)}")
    print(f"image classes             {dict(by_class)}")
    print(f"split confidence          {counts['clean']} clean, "
          f"{counts['review']} review")
    print(f"empty question / solution {counts['empty_question']} / "
          f"{counts['empty_solution']}")

    problems_found = True
    if text_missing:
        print(f"\nTEXT NOT FOUND IN OUTPUT ({len(text_missing)} shown):")
        for t in text_missing:
            print("  ", t)
    if formula_missing:
        print(f"\nFORMULAS NOT FOUND IN OUTPUT ({len(formula_missing)} shown):")
        for t in formula_missing:
            print("  ", t)
    if bad_files:
        print(f"\nSTRUCTURAL PROBLEMS ({len(bad_files)}):")
        for t in bad_files[:20]:
            print("  ", t)
    if not (text_missing or formula_missing or bad_files or missing_img):
        print("\nAll invariants passed.")
        problems_found = False

    if review:
        print(f"\nFlagged for spot check ({len(review)}):")
        for r in review:
            print("  ", r)
    return 1 if problems_found else 0


if __name__ == "__main__":
    sys.exit(main())

"""Identify problem sheets and split them into question / solution regions.

There is no "Solution" label in these workbooks and blank-row gaps are not a
reliable separator. The boundary is encoded in the cell fill: the question sits
in a shaded box, the solution is white. Measured over all 348 problem sheets,
fill + a per-sheet column band splits 97% of sheets cleanly, against 53% for a
fixed "column >= H" rule and 32% for a single row threshold.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from xlsx_reader import Cell, Image, Shape, Sheet

QUESTION, SOLUTION, EXAMINER = "question", "solution", "examiner"

_EXAMINER_RE = re.compile(r"examiner\s+report", re.I)
_PART_RE = re.compile(r"^\(?([a-z]{1,2}|[ivx]{1,4})[.)]$", re.I)

# "2002 Exam 9 - Q1 revised", "Spring 2013 Exam 5 - Q13", "2014 Exam 8 - Q16a"
_EXAM_RE = re.compile(
    r"^(?:(?P<sitting>Spring|Fall)\s+)?(?P<year>\d{4})\s+Exam\s+(?P<exam>\d+)"
    r"(?:\s*-\s*Q(?P<q>\d+[a-z]?))?",
    re.I,
)
_PRACTICE_RE = re.compile(r"^Practice\s+Problem\s+(\d+)", re.I)


# --------------------------------------------------------------------------

@dataclass(slots=True)
class Meta:
    title: str
    source: str                    # past_exam | practice_problem
    exam_year: int | None = None
    exam_sitting: str | None = None
    exam_number: int | None = None
    question_number: str | None = None
    practice_number: int | None = None
    revised: bool = False
    points: float | None = None
    good_problem: bool = False
    parts: list[str] = field(default_factory=list)


@dataclass(slots=True)
class Split:
    question: list[Cell] = field(default_factory=list)
    solution: list[Cell] = field(default_factory=list)
    examiner: list[Cell] = field(default_factory=list)
    images: dict[str, list[Image]] = field(default_factory=dict)
    shapes: dict[str, list[Shape]] = field(default_factory=dict)
    layout: str = "vertical"       # side_by_side | vertical
    confidence: str = "clean"      # clean | review
    split_col: int = 2
    examiner_row: int | None = None
    examiner_col: int | None = None
    alternations: int = 0


def is_problem_sheet(sheet: Sheet) -> bool:
    """Cell B1 is yellow on exactly 348 of 362 sheets, and on no index sheet."""
    b1 = sheet.get("B1")
    return bool(b1 and b1.is_yellow)


def _is_header(cell: Cell, sheet: Sheet) -> bool:
    """Row 1 banner plus the A2/A3 'Points' block."""
    if cell.row == 1:
        return True
    if cell.col == 1 and cell.row in (2, 3):
        return sheet.text_at("A2").strip().lower() == "points"
    return False


def extract_meta(sheet: Sheet, split: Split) -> Meta:
    name = sheet.name
    title = sheet.text_at("A1") or name

    points = None
    a3 = sheet.get("A3")
    if a3 is not None and a3.numeric:
        points = float(a3.raw)

    good = "good problem" in sheet.text_at("D1").lower()

    m = _EXAM_RE.match(name)
    p = _PRACTICE_RE.match(name)
    if m:
        meta = Meta(
            title=title, source="past_exam",
            exam_year=int(m.group("year")),
            exam_sitting=(m.group("sitting") or "").lower() or None,
            exam_number=int(m.group("exam")),
            question_number=m.group("q"),
            revised="revised" in name.lower(),
            points=points, good_problem=good,
        )
    elif p:
        meta = Meta(title=title, source="practice_problem",
                    practice_number=int(p.group(1)),
                    points=points, good_problem=good)
    else:
        meta = Meta(title=title, source="past_exam",
                    points=points, good_problem=good)

    seen = []
    for c in split.question:
        t = c.text.strip()
        mm = _PART_RE.match(t)
        if mm:
            lbl = mm.group(1).lower()
            if lbl not in seen:
                seen.append(lbl)
    meta.parts = seen
    return meta


def split_sheet(sheet: Sheet) -> Split:
    body = [c for c in sheet.cells.values() if not _is_header(c, sheet)]
    split = Split()
    if not body:
        return split

    # 1. examiner-report marker: appears on 92 sheets, column varies (J, B, K,
    #    I, L, A ...), so search every cell rather than a fixed column.
    #    Usually the block is appended below everything, so a row anchor works.
    #    On one sheet (B_3 '2018 Exam 8 - Q2') the marker heads a far-right
    #    column at row 2; row-anchoring there would swallow the whole sheet, so
    #    a marker near the top is anchored by column instead.
    markers = [c for c in body if _EXAMINER_RE.search(c.text)]
    main = body
    if markers:
        mk = min(markers, key=lambda c: (c.row, c.col))
        max_row = max(c.row for c in body)
        split.examiner_row = mk.row
        if mk.row < 0.25 * max_row:
            split.examiner_col = mk.col
            in_ex = lambda c: c.row >= mk.row and c.col >= mk.col
        else:
            in_ex = lambda c: c.row >= mk.row
        split.examiner = [c for c in body if in_ex(c)]
        main = [c for c in body if not in_ex(c)]

    # 2. per-sheet column band. A constant threshold of H is wrong: the real
    #    boundary is D on 138 sheets, E on 48, B on 46, and >=H on only 19.
    gray_cols = [c.col for c in main if c.is_gray]
    split.split_col = (max(gray_cols) + 1) if gray_cols else 2

    # 3. classify every cell -- classification is total, so nothing is dropped.
    for c in main:
        if c.col >= split.split_col or not c.is_gray:
            split.solution.append(c)
        else:
            split.question.append(c)

    split.layout = ("side_by_side"
                    if any(c.col >= split.split_col for c in split.solution)
                    else "vertical")

    # 4. reading-order sanity. Only the left band can be ambiguous: cells at
    #    col >= split_col are spatially separated and unambiguously solution,
    #    so counting row transitions across the whole sheet would flag every
    #    side-by-side layout. Within the left band the question should end
    #    before the solution begins.
    left = [c for c in main if c.col < split.split_col]
    lq = {c.row for c in left if c.is_gray}
    ls = {c.row for c in left if not c.is_gray}
    mixed = lq & ls
    pure_s = ls - mixed
    out_of_order = bool(lq and ls and max(lq) > min(pure_s or ls))
    split.alternations = len(mixed)
    if mixed or out_of_order:
        split.confidence = "review"

    # 5. images and text boxes follow the region their anchor lands in
    split.images = {QUESTION: [], SOLUTION: [], EXAMINER: []}
    split.shapes = {QUESTION: [], SOLUTION: [], EXAMINER: []}
    qmax_row = max((c.row for c in split.question), default=0)

    def region_of(row: int, col: int) -> str:
        if split.examiner_row is not None and row >= split.examiner_row:
            if split.examiner_col is None or col >= split.examiner_col:
                return EXAMINER
        if row <= qmax_row and col < split.split_col:
            return QUESTION
        return SOLUTION

    for img in sheet.images:
        split.images[region_of(img.row, img.col)].append(img)
    for shp in sheet.shapes:
        split.shapes[region_of(shp.row, shp.col)].append(shp)

    return split


def classify_image(img: Image, region: str) -> str:
    """Bucket an image so the later vision pass can target only what matters."""
    if region == EXAMINER:
        return "examiner_scan"
    if img.size < 5000:
        return "formula_snippet"
    if region == QUESTION:
        return "question_exhibit"
    return "solution_exhibit"

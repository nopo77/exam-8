"""Turn a classified region of cells into Markdown.

Three shapes of content have to survive the trip:

  * prose, which the authors typed one sentence per row and which must be
    rejoined into paragraphs;
  * numeric tables, which become Markdown tables;
  * formulas, which encode the actual solution method and are kept verbatim
    alongside the value they produced.
"""

from __future__ import annotations

import re
from collections import defaultdict

from xlsx_reader import Cell, Image, Shape, num_to_col

_PART_RE = re.compile(r"^\(?([a-z]{1,2}|[ivx]{1,4})[.)]$", re.I)
_BULLET_RE = re.compile(r"^[\u2022\u25cf\u25aa\u25a0\u00b7o]\s+")
_SENT_END = re.compile(r"[.!?:;]$")
# An enumerated line ("i. Using raw class data", "a) Calculate ..."). These are
# separate list items and must not be swallowed into the preceding paragraph.
_ENUM_RE = re.compile(r"^\(?(?:[a-z]{1,2}|[ivx]{1,4}|\d{1,2})[.)]\s+\S", re.I)

# Typographic characters get folded to ASCII; Greek letters and math symbols
# are left alone because they carry meaning in actuarial notation.
_NORMALIZE = {
    "\u2019": "'", "\u2018": "'", "\u201c": '"', "\u201d": '"',
    "\u2212": "-", "\u2217": "*", "\u2013": "-", "\u2014": "--",
    "\u00a0": " ", "\u00b5": "\u03bc", "\u03d5": "\u03c6",
    "\U0001d719": "\u03c6", "\U0001d713": "\u03c8",
}


def normalize(text: str) -> str:
    for bad, good in _NORMALIZE.items():
        text = text.replace(bad, good)
    return text


def clean_formula(formula: str) -> str:
    """Excel stores formulas without the leading '=' and with _xlfn shims."""
    f = formula.replace("_xlfn._xlws.", "").replace("_xlfn.", "")
    return "=" + f


def is_part_label(text: str) -> str | None:
    m = _PART_RE.match(text.strip())
    return m.group(1).lower() if m else None


def _esc(text: str) -> str:
    return normalize(text).replace("|", "\\|").replace("\n", "<br>")


def _cell_inline(cell: Cell) -> str:
    """Value plus, when present, the formula that produced it."""
    text = normalize(cell.text)
    if cell.formula:
        code = clean_formula(cell.formula)
        return f"{text} — `{code}`" if text else f"`{code}`"
    return text


# --------------------------------------------------------------------------

def _render_table(run: list[tuple[int, dict[int, Cell]]]) -> str:
    cols = sorted({c for _, rowmap in run for c in rowmap})

    first = run[0][1]
    rest = run[1:]
    use_header = (
        bool(rest)
        and all(not c.numeric for c in first.values())
        and any(c.numeric for _, rm in rest for c in rm.values())
    )

    if use_header:
        headers = [_esc(first[c].text) if c in first else "" for c in cols]
        body = rest
    else:
        headers = [num_to_col(c) for c in cols]
        body = run

    lines = [
        "| " + " | ".join(h or " " for h in headers) + " |",
        "| " + " | ".join("---" for _ in cols) + " |",
    ]
    formulas: list[str] = []
    if use_header:
        # Header labels are sometimes themselves formulas pulling from the
        # question table; collect those too or they are silently dropped.
        for cell in first.values():
            if cell.formula:
                formulas.append(f"- `{cell.ref}` = `{clean_formula(cell.formula)}`")
    for _, rowmap in body:
        cells = []
        for c in cols:
            cell = rowmap.get(c)
            if cell is None:
                cells.append("")
                continue
            cells.append(_esc(cell.text))
            if cell.formula:
                formulas.append(f"- `{cell.ref}` = `{clean_formula(cell.formula)}`")
        lines.append("| " + " | ".join(cells) + " |")

    out = "\n".join(lines)
    if formulas:
        out += ("\n\n<details><summary>Formulas</summary>\n\n"
                + "\n".join(formulas) + "\n\n</details>")
    return out


def _render_single(rowmap: dict[int, Cell]) -> str:
    """A row holding several cells but not part of a multi-row table."""
    ordered = [c for _, c in sorted(rowmap.items())]
    if (len(ordered) == 2 and not ordered[0].numeric and not ordered[0].formula
            and (ordered[1].numeric or ordered[1].formula)):
        return f"**{normalize(ordered[0].text)}:** {_cell_inline(ordered[1])}"
    parts = [_cell_inline(c) for c in ordered if _cell_inline(c)]
    return " — ".join(parts)


def _column_clusters(cells: list[Cell], max_gap: int = 1) -> list[list[int]]:
    """Group occupied columns into logically separate blocks.

    A side-by-side solution often runs two unrelated grids across the same
    rows (say a MIN() ladder in column J and a labelled block in M:O). Joining
    them row-wise conflates them and also hides the tables, so split wherever
    two or more empty columns sit between occupied ones.
    """
    cols = sorted({c.col for c in cells})
    if not cols:
        return []
    groups, cur = [], [cols[0]]
    for c in cols[1:]:
        if c - cur[-1] - 1 <= max_gap:
            cur.append(c)
        else:
            groups.append(cur)
            cur = [c]
    groups.append(cur)
    return groups


# --------------------------------------------------------------------------

def render_region(cells: list[Cell], images: list[Image] | None = None,
                  shapes: list[Shape] | None = None,
                  image_ref=None) -> str:
    """Render one region (question / solution / examiner) to Markdown.

    Columns are split into logical clusters first, then each cluster is laid
    out top-to-bottom and the clusters are concatenated left-to-right.
    """
    images = list(images or [])
    shapes = list(shapes or [])
    clusters = _column_clusters(cells)

    if not clusters:
        chunks = []
        for img in images:
            ref = image_ref(img) if image_ref else f"`{img.media}`"
            if ref:
                chunks.append(ref)
        for shp in shapes:
            chunks.append("> " + normalize(shp.text).replace("\n", "  \n> "))
        return "\n\n".join(chunks)

    img_buckets = _assign_to_clusters(images, clusters)
    shp_buckets = _assign_to_clusters(shapes, clusters)

    out: list[str] = []
    for gi, group in enumerate(clusters):
        lo, hi = group[0], group[-1]
        sub = [c for c in cells if lo <= c.col <= hi]
        text = _render_cluster(sub, img_buckets[gi], shp_buckets[gi], image_ref)
        if text.strip():
            out.append(text)
    return "\n\n".join(out)


def _assign_to_clusters(items: list, clusters: list[list[int]]) -> list[list]:
    """Place every item in exactly one cluster -- the nearest by column.

    Anything anchored outside all cluster ranges still has to be emitted, so
    distance decides rather than containment.
    """
    buckets: list[list] = [[] for _ in clusters]
    for item in items:
        best, best_d = 0, None
        for gi, group in enumerate(clusters):
            lo, hi = group[0], group[-1]
            d = 0 if lo <= item.col <= hi else min(abs(item.col - lo),
                                                   abs(item.col - hi))
            if best_d is None or d < best_d:
                best, best_d = gi, d
        buckets[best].append(item)
    return buckets


def _render_cluster(cells: list[Cell], images: list[Image],
                    shapes: list[Shape], image_ref) -> str:
    rowmap: dict[int, dict[int, Cell]] = defaultdict(dict)
    for c in cells:
        rowmap[c.row][c.col] = c

    # Split each row into an optional part heading plus its remaining cells.
    entries: list[tuple[int, str, object]] = []
    for row in sorted(rowmap):
        cols = rowmap[row]
        # Several part labels on one row means they head table columns
        # (a., b., c. across the top), not a new section.
        label_cols = [c for c in sorted(cols) if is_part_label(cols[c].text)]
        label_col = label_cols[0] if len(label_cols) == 1 else None
        if label_col is not None:
            label = is_part_label(cols[label_col].text)
            pts = next((cols[c] for c in sorted(cols)
                        if c < label_col and cols[c].numeric), None)
            heading = f"### Part {label}"
            if pts is not None:
                heading += f" ({normalize(pts.text)} pts)"
            entries.append((row, "heading", heading))
            remainder = {c: cell for c, cell in cols.items() if c > label_col}
            if remainder:
                entries.append((row, "row", remainder))
        else:
            entries.append((row, "row", cols))

    blocks: list[tuple[int, str]] = []
    para: list[str] = []
    para_col: int | None = None
    para_row: int | None = None
    bullets: list[str] = []
    bullet_row: int | None = None

    def flush_para():
        nonlocal para, para_col, para_row
        if para:
            blocks.append((para_row, " ".join(para)))
            para, para_col, para_row = [], None, None

    def flush_bullets():
        nonlocal bullets, bullet_row
        if bullets:
            blocks.append((bullet_row, "\n".join(bullets)))
            bullets, bullet_row = [], None

    i = 0
    while i < len(entries):
        row, kind, payload = entries[i]

        if kind == "heading":
            flush_para(); flush_bullets()
            blocks.append((row, payload))
            i += 1
            continue

        cols: dict[int, Cell] = payload

        # --- multi-row table: consecutive rows, each with >= 2 cells ---
        if len(cols) >= 2:
            run = [(row, cols)]
            j = i + 1
            while j < len(entries):
                r2, k2, p2 = entries[j]
                if k2 != "row" or len(p2) < 2 or r2 != run[-1][0] + 1:
                    break
                run.append((r2, p2))
                j += 1
            flush_para(); flush_bullets()
            if len(run) >= 2:
                blocks.append((row, _render_table(run)))
            else:
                blocks.append((row, _render_single(cols)))
            i = j
            continue

        # --- single cell: prose, bullet, or a lone value ---
        cell = next(iter(cols.values()))
        text = normalize(cell.text)

        if _BULLET_RE.match(text):
            flush_para()
            if bullet_row is None:
                bullet_row = row
            bullets.append("- " + _BULLET_RE.sub("", text))
            i += 1
            continue

        flush_bullets()

        if _ENUM_RE.match(text):
            flush_para()
            blocks.append((row, text))
            i += 1
            continue

        if cell.formula or cell.numeric:
            flush_para()
            blocks.append((row, _cell_inline(cell)))
            i += 1
            continue

        # Prose is stored one sentence per row; rejoin runs in the same column
        # into a paragraph, breaking on a blank row, a column change, or a
        # line that ends in a colon (a lead-in to whatever follows).
        contiguous = i > 0 and row == entries[i - 1][0] + 1
        continues = (para
                     and para_col == cell.col
                     and contiguous
                     and not para[-1].rstrip().endswith(":"))
        if continues:
            para.append(text)
        else:
            flush_para()
            para = [text]
            para_col = cell.col
            para_row = row
        i += 1

    flush_para()
    flush_bullets()

    # Interleave images and text boxes at their anchor rows.
    events: list[tuple[int, int, str]] = [(r, 1, t) for r, t in blocks]
    for img in images:
        ref = image_ref(img) if image_ref else f"`{img.media}`"
        if ref:
            events.append((img.row, 0, ref))
    for shp in shapes:
        events.append((shp.row, 0, "> " + normalize(shp.text).replace("\n", "  \n> ")))

    events.sort(key=lambda e: (e[0], e[1]))
    return "\n\n".join(text for _, _, text in events if text.strip())

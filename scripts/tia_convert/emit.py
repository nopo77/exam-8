"""Drive the conversion: 14 workbooks -> ~348 problem files under study/practice_questions/.

Run from the repo root:  python scripts/tia_convert/emit.py
"""

from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

from classify import (EXAMINER, QUESTION, SOLUTION, classify_image,
                      extract_meta, is_problem_sheet, split_sheet)
from render import normalize, render_region
from transcriptions import TRANSCRIPTIONS
from xlsx_reader import load_workbook

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "tia_excel"
OUT = ROOT / "study" / "practice_questions"

# TIA section -> source readings, mirroring study/tia_content_map.md so each
# problem points back at the material it tests.
READINGS = {
    "A2": ["fisher_et_al/02_ch02_risk_sharing_and_loss_sensitive_plans.md"],
    "B2": ["bahnemann/5_ch5_excess_claims.md"],
    "B3": ["bahnemann/6_ch6_limits_and_deductibles.md"],
    "B4": ["fisher_et_al/03_ch03_aggregate_excess_loss_cost_estimation.md",
           "fisher_et_al/04_ch04_concluding_remarks.md"],
    "C1": ["fisher_et_al/01_ch01_experience_rating.md"],
    "C2": [],   # ISO manual is not in this workspace (documented gap)
    "C3": ["mahler/"],
    "C4": ["bailey_&_simon.md"],
    "D1": ["asop_12.md"],
    "D2": ["couret_&_venter/"],
    "D3": ["goldburd_et_al/"],
    "D4": [],   # ASOP 25 itself is not in this workspace (documented gap)
    "D5": ["holmes_&_casotto/"],
    "D6": ["chalk_et_al/"],
}


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "_", normalize(text).lower()).strip("_")
    return re.sub(r"_+", "_", s)


def workbook_id(path: Path) -> tuple[str, str]:
    """'B_3_Pricing_limits_..._practice_solutions.xlsx' -> ('B3', 'pricing_limits_...')."""
    stem = path.stem.replace("_practice_solutions", "")
    m = re.match(r"^([A-D])_(\d)_(.*)$", stem)
    if not m:
        return stem.upper(), slugify(stem)
    return f"{m.group(1)}{m.group(2)}", slugify(m.group(3))


def yaml_value(v) -> str:
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, list):
        return "[" + ", ".join(yaml_value(x) for x in v) + "]"
    s = str(v)
    if s == "" or re.search(r'[:#\[\]{}",\']', s) or s[0] in "-?&*!|>%@`":
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


def frontmatter(fields: dict) -> str:
    lines = ["---"]
    for k, v in fields.items():
        lines.append(f"{k}: {yaml_value(v)}")
    lines.append("---")
    return "\n".join(lines)


def convert_workbook(path: Path, manifest: list) -> dict:
    tia, topic = workbook_id(path)
    section = path.parent.name                      # 'section-a'
    dest = OUT / section / f"{tia}_{topic}"
    img_dir = dest / "images"
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True, exist_ok=True)

    wb = load_workbook(str(path))
    order = _problem_order(wb)
    written: list[dict] = []
    seen_img: dict[str, str] = {}

    problems = [s for s in wb.sheets if is_problem_sheet(s)]
    problems.sort(key=lambda s: order.get(s.name, 10_000 + s.index))

    for n, sheet in enumerate(problems, start=1):
        split = split_sheet(sheet)
        meta = extract_meta(sheet, split)
        fname = f"{n:02d}_{slugify(sheet.name)}.md"
        rel_md = f"{section}/{tia}_{topic}/{fname}"

        def image_ref(img, _sheet=sheet, _split=split):
            if img.sha256 not in seen_img:
                img_dir.mkdir(exist_ok=True)
                name = f"img_{img.sha256[:12]}.{img.ext}"
                (img_dir / name).write_bytes(img.data)
                seen_img[img.sha256] = name
            name = seen_img[img.sha256]
            region = next(r for r, lst in _split.images.items() if img in lst)
            text = TRANSCRIPTIONS.get(img.sha256[:12])
            manifest.append({
                "sha256": img.sha256,
                "file": f"{rel_md.rsplit('/', 1)[0]}/images/{name}",
                "bytes": img.size,
                "workbook": path.name,
                "sheet": _sheet.name,
                "md_path": rel_md,
                "anchor_row": img.row,
                "anchor_col": img.col,
                "region": region,
                "class": classify_image(img, region),
                "transcription": text,
            })
            ref = f"![{region} image](images/{name})"
            # Images carrying content no cell holds get their transcription
            # inlined, so an agent never has to open the PNG.
            return f"{ref}\n\n{text}" if text else ref

        body_q = render_region(split.question, split.images[QUESTION],
                               split.shapes[QUESTION], image_ref)
        body_s = render_region(split.solution, split.images[SOLUTION],
                               split.shapes[SOLUTION], image_ref)
        body_e = render_region(split.examiner, split.images[EXAMINER],
                               split.shapes[EXAMINER], image_ref)

        n_img = sum(len(v) for v in split.images.values())
        fields = {
            "tia_section": tia,
            "tia_topic": topic,
            "title": meta.title,
            "source": meta.source,
            "exam_year": meta.exam_year,
            "exam_sitting": meta.exam_sitting,
            "exam_number": meta.exam_number,
            "question_number": meta.question_number,
            "practice_number": meta.practice_number,
            "revised": meta.revised,
            "points": meta.points,
            "parts": meta.parts,
            "good_problem": meta.good_problem,
            "has_images": n_img > 0,
            "has_examiner_report": bool(split.examiner),
            "layout": split.layout,
            "split_confidence": split.confidence,
            "readings": READINGS.get(tia, []),
            "source_workbook": f"tia_excel/{section}/{path.name}",
            "source_sheet": sheet.name,
        }

        parts_md = [frontmatter(fields), "", f"# {normalize(meta.title)}", ""]
        if meta.points is not None:
            parts_md += [f"**Points:** {meta.points:g}", ""]
        parts_md += ["## Question", "", body_q or "_(no question text)_", ""]
        parts_md += ["## Solution", "", body_s or "_(no solution text)_", ""]
        if body_e:
            parts_md += ["## Examiner Report", "", body_e, ""]

        (dest / fname).write_text("\n".join(parts_md).rstrip() + "\n",
                                  encoding="utf-8")
        written.append({
            "n": n, "file": fname, "title": meta.title, "points": meta.points,
            "good": meta.good_problem, "confidence": split.confidence,
            "source": meta.source,
        })

    _write_index(dest, tia, topic, written)
    return {"tia": tia, "topic": topic, "dir": str(dest.relative_to(ROOT)),
            "count": len(written), "images": len(seen_img)}


def _problem_order(wb) -> dict[str, int]:
    """The 'Problem List' sheet holds the canonical ordering."""
    sheet = wb.by_name("Problem List")
    if sheet is None:
        return {}
    order = {}
    for row, cells in sheet.rows():
        if row < 2:
            continue
        first = next((c for c in cells if c.col == 1), None)
        if first and first.text:
            order[first.text.strip()] = row
    return order


def _write_index(dest: Path, tia: str, topic: str, written: list[dict]) -> None:
    title = topic.replace("_", " ").title()
    lines = [
        frontmatter({
            "tia_section": tia, "tia_topic": topic, "kind": "index",
            "problem_count": len(written),
            "readings": READINGS.get(tia, []),
        }),
        "",
        f"# {tia} — {title}",
        "",
        f"{len(written)} problems converted from "
        f"`tia_excel/.../{tia[0]}_{tia[1]}_..._practice_solutions.xlsx`.",
        "",
        "| # | Problem | Points | Recommended | Split |",
        "|---|---|---|---|---|",
    ]
    for w in written:
        pts = f"{w['points']:g}" if w["points"] is not None else "—"
        flag = "yes" if w["good"] else ""
        conf = "" if w["confidence"] == "clean" else "review"
        lines.append(
            f"| {w['n']} | [{normalize(w['title'])}]({w['file']}) | {pts} | {flag} | {conf} |"
        )
    (dest / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    manifest: list[dict] = []
    summary = []
    for path in sorted(SRC.glob("section-*/*.xlsx")):
        info = convert_workbook(path, manifest)
        summary.append(info)
        print(f"  {info['tia']:3} {info['count']:3} problems  "
              f"{info['images']:3} images  {info['dir']}")

    (OUT / "images_manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8")

    total = sum(s["count"] for s in summary)
    print(f"\n{total} problems across {len(summary)} workbooks")
    print(f"{len(manifest)} image anchors -> {OUT / 'images_manifest.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

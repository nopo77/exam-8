"""Minimal SpreadsheetML reader built on the standard library.

openpyxl is not installed in this workspace, so this module implements the
subset of .xlsx we need for the TIA practice workbooks:

  * shared strings (including rich-text runs)
  * cell fills and italic flags (the question/solution boundary is encoded in
    the fill colour, not in any text marker)
  * cached values with number-format aware display strings
  * formulas, including expansion of ``t="shared"`` followers -- 2,877 of the
    7,178 formulas in this corpus carry no text of their own and would be lost
    by a naive parse
  * image anchors resolved through the drawing rels
"""

from __future__ import annotations

import datetime as _dt
import hashlib
import re
import zipfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field

MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKGREL = "http://schemas.openxmlformats.org/package/2006/relationships"
XDR = "http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing"
DRAW = "http://schemas.openxmlformats.org/drawingml/2006/main"

M = "{%s}" % MAIN
R = "{%s}" % REL
P = "{%s}" % PKGREL
X = "{%s}" % XDR
A = "{%s}" % DRAW


# --------------------------------------------------------------------------
# cell reference helpers
# --------------------------------------------------------------------------

_REF_SPLIT = re.compile(r"([A-Z]+)(\d+)")


def col_to_num(letters: str) -> int:
    """'A' -> 1, 'AA' -> 27."""
    n = 0
    for ch in letters:
        n = n * 26 + (ord(ch) - 64)
    return n


def num_to_col(n: int) -> str:
    out = ""
    while n > 0:
        n, rem = divmod(n - 1, 26)
        out = chr(65 + rem) + out
    return out


def parse_ref(ref: str) -> tuple[int, int]:
    """'B7' -> (7, 2)."""
    m = _REF_SPLIT.match(ref)
    if not m:
        raise ValueError(f"bad cell ref: {ref!r}")
    return int(m.group(2)), col_to_num(m.group(1))


# --------------------------------------------------------------------------
# shared-formula translation
# --------------------------------------------------------------------------

# A cell reference, with the surrounding context needed to avoid matching
# function names (LOG10() ), scientific notation (1E5) and the tail of an
# already-consumed absolute reference.
_CELL_RE = re.compile(
    r"(?<![A-Za-z0-9_$.])(\$?)([A-Z]{1,3})(\$?)(\d{1,7})(?![A-Za-z0-9_(])"
)


def translate_formula(text: str, drow: int, dcol: int) -> str:
    """Shift the relative references in ``text`` by (drow, dcol).

    Used to reconstruct shared-formula followers from their master. String
    literals and quoted sheet names are passed through untouched.
    """
    if not text or (drow == 0 and dcol == 0):
        return text

    out: list[str] = []
    i, n = 0, len(text)
    while i < n:
        ch = text[i]
        if ch == '"':  # string literal, "" escapes a quote
            j = i + 1
            while j < n:
                if text[j] == '"':
                    if j + 1 < n and text[j + 1] == '"':
                        j += 2
                        continue
                    break
                j += 1
            out.append(text[i : j + 1])
            i = j + 1
            continue
        if ch == "'":  # quoted sheet name
            j = i + 1
            while j < n and text[j] != "'":
                j += 1
            out.append(text[i : j + 1])
            i = j + 1
            continue

        m = _CELL_RE.match(text, i)
        if m:
            cdollar, letters, rdollar, digits = m.groups()
            col = col_to_num(letters)
            row = int(digits)
            if not cdollar:
                col += dcol
            if not rdollar:
                row += drow
            if 1 <= col <= 16384 and 1 <= row <= 1048576:
                out.append(f"{cdollar}{num_to_col(col)}{rdollar}{row}")
            else:  # shifted off the sheet -- Excel would show #REF!
                out.append("#REF!")
            i = m.end()
            continue

        out.append(ch)
        i += 1
    return "".join(out)


# --------------------------------------------------------------------------
# number formatting
# --------------------------------------------------------------------------

_BUILTIN_FMT = {
    0: "General", 1: "0", 2: "0.00", 3: "#,##0", 4: "#,##0.00",
    9: "0%", 10: "0.00%", 11: "0.00E+00", 12: "# ?/?", 13: "# ??/??",
    14: "m/d/yyyy", 15: "d-mmm-yy", 16: "d-mmm", 17: "mmm-yy",
    18: "h:mm AM/PM", 19: "h:mm:ss AM/PM", 20: "h:mm", 21: "h:mm:ss",
    22: "m/d/yyyy h:mm", 37: "#,##0 ;(#,##0)", 38: "#,##0 ;[Red](#,##0)",
    39: "#,##0.00;(#,##0.00)", 40: "#,##0.00;[Red](#,##0.00)",
    44: '_("$"* #,##0.00_)', 45: "mm:ss", 46: "[h]:mm:ss", 47: "mmss.0",
    48: "##0.0E+0", 49: "@",
}

_EPOCH = _dt.datetime(1899, 12, 30)
_DATE_CHARS = re.compile(r"(?<!\\)[ymdhs]")
_STRIP_LITERALS = re.compile(r'"[^"]*"|\[[^\]]*\]|\\.')


def _trim(x: float) -> str:
    """Render a float without trailing noise: 3.0 -> '3', 0.15000000002 -> '0.15'."""
    if x == int(x) and abs(x) < 1e15:
        return f"{int(x):,}"
    s = f"{round(x, 6):,.6f}".rstrip("0").rstrip(".")
    return s or "0"


def format_number(raw: float, fmt: str | None) -> str:
    if fmt is None or fmt in ("General", "@"):
        return _trim(raw)

    section = fmt.split(";")[0]
    bare = _STRIP_LITERALS.sub("", section)

    if _DATE_CHARS.search(bare) and "0" not in bare.replace("0%", ""):
        try:
            dt = _EPOCH + _dt.timedelta(days=float(raw))
            if bare.strip().lower() in ("h:mm", "h:mm:ss", "mm:ss"):
                return dt.strftime("%H:%M:%S")
            return dt.strftime("%Y-%m-%d")
        except (OverflowError, ValueError):
            return _trim(raw)

    pct = "%" in bare
    val = raw * 100 if pct else raw

    dec = 0
    if "." in bare:
        tail = bare.split(".", 1)[1]
        dec = len(re.match(r"[0#?]*", tail).group(0))

    grouped = "#,#" in bare
    if grouped:
        body = f"{val:,.{dec}f}"
    elif dec:
        body = f"{val:.{dec}f}"
    else:
        body = _trim(val)

    if pct:
        body += "%"
    if "$" in section:
        body = "$" + body
    return body


# --------------------------------------------------------------------------
# data model
# --------------------------------------------------------------------------

@dataclass(slots=True)
class Cell:
    row: int
    col: int
    text: str = ""
    raw: object = None
    formula: str | None = None
    fill: tuple | None = None
    italic: bool = False
    numeric: bool = False

    @property
    def ref(self) -> str:
        return f"{num_to_col(self.col)}{self.row}"

    @property
    def is_gray(self) -> bool:
        return is_gray(self.fill)

    @property
    def is_yellow(self) -> bool:
        f = self.fill
        return bool(f and f[0] == "rgb" and f[1].endswith("FFFF00"))


@dataclass(slots=True)
class Image:
    row: int            # 1-based anchor row
    col: int            # 1-based anchor col
    media: str          # e.g. 'xl/media/image7.png'
    data: bytes
    sha256: str
    size: int

    @property
    def ext(self) -> str:
        return self.media.rsplit(".", 1)[-1].lower()


@dataclass(slots=True)
class Shape:
    """A drawing text box. Rare (15 corpus-wide, all in D_6) but load-bearing:
    they carry the terms of a matching exercise that exists in no cell."""
    row: int
    col: int
    text: str


@dataclass(slots=True)
class Sheet:
    name: str
    index: int
    cells: dict[tuple[int, int], Cell] = field(default_factory=dict)
    images: list[Image] = field(default_factory=list)
    shapes: list[Shape] = field(default_factory=list)
    merges: list[str] = field(default_factory=list)

    def get(self, ref: str) -> Cell | None:
        return self.cells.get(parse_ref(ref))

    def text_at(self, ref: str) -> str:
        c = self.get(ref)
        return c.text if c else ""

    @property
    def max_row(self) -> int:
        return max((r for r, _ in self.cells), default=0)

    @property
    def max_col(self) -> int:
        return max((c for _, c in self.cells), default=0)

    def rows(self):
        """Yield (row_number, [cells sorted by column]) for non-empty rows."""
        by_row: dict[int, list[Cell]] = {}
        for cell in self.cells.values():
            by_row.setdefault(cell.row, []).append(cell)
        for r in sorted(by_row):
            yield r, sorted(by_row[r], key=lambda c: c.col)


@dataclass(slots=True)
class Workbook:
    path: str
    sheets: list[Sheet]

    def by_name(self, name: str) -> Sheet | None:
        for s in self.sheets:
            if s.name == name:
                return s
        return None


GRAY_RGB = {"FFF2F2F2", "F2F2F2"}


def is_gray(fill: tuple | None) -> bool:
    """The question region is shaded; the solution region is white.

    Two signatures exist corpus-wide: a themed white with a slight darkening
    tint (13 workbooks) and a literal #F2F2F2 (D_6 only, which mixes both).
    """
    if not fill:
        return False
    kind = fill[0]
    if kind == "rgb":
        return fill[1].upper() in GRAY_RGB
    if kind == "theme":
        _, theme, tint = fill
        return theme == 0 and tint is not None and tint < -0.001
    return False


# --------------------------------------------------------------------------
# parsing
# --------------------------------------------------------------------------

def _shared_strings(z: zipfile.ZipFile) -> tuple[list[str], list[bool]]:
    try:
        root = ET.fromstring(z.read("xl/sharedStrings.xml"))
    except KeyError:
        return [], []
    texts, italics = [], []
    for si in root:
        parts, runs, ital_runs = [], 0, 0
        for child in si:
            if child.tag == M + "t":
                parts.append(child.text or "")
            elif child.tag == M + "r":
                runs += 1
                pr = child.find(M + "rPr")
                if pr is not None and pr.find(M + "i") is not None:
                    ital_runs += 1
                t = child.find(M + "t")
                if t is not None:
                    parts.append(t.text or "")
        texts.append("".join(parts))
        italics.append(runs > 0 and ital_runs == runs)
    return texts, italics


def _styles(z: zipfile.ZipFile):
    """Return (fill_by_xf, italic_by_xf, numfmt_by_xf)."""
    root = ET.fromstring(z.read("xl/styles.xml"))

    numfmts = dict(_BUILTIN_FMT)
    node = root.find(M + "numFmts")
    if node is not None:
        for nf in node:
            numfmts[int(nf.get("numFmtId"))] = nf.get("formatCode")

    fills: list[tuple | None] = []
    node = root.find(M + "fills")
    if node is not None:
        for fl in node:
            pat = fl.find(M + "patternFill")
            sig = None
            if pat is not None and pat.get("patternType") == "solid":
                fg = pat.find(M + "fgColor")
                if fg is not None:
                    if fg.get("rgb"):
                        sig = ("rgb", fg.get("rgb").upper())
                    elif fg.get("theme") is not None:
                        tint = fg.get("tint")
                        sig = ("theme", int(fg.get("theme")),
                               float(tint) if tint is not None else None)
            fills.append(sig)

    italics: list[bool] = []
    node = root.find(M + "fonts")
    if node is not None:
        for fo in node:
            italics.append(fo.find(M + "i") is not None)

    xf_fill, xf_ital, xf_fmt = [], [], []
    node = root.find(M + "cellXfs")
    if node is not None:
        for xf in node:
            fid = int(xf.get("fillId", 0))
            fnt = int(xf.get("fontId", 0))
            nfi = int(xf.get("numFmtId", 0))
            xf_fill.append(fills[fid] if fid < len(fills) else None)
            xf_ital.append(italics[fnt] if fnt < len(italics) else False)
            xf_fmt.append(numfmts.get(nfi))
    return xf_fill, xf_ital, xf_fmt


def _rels(z: zipfile.ZipFile, part: str) -> dict[str, str]:
    """Relationship id -> target part path, for the given part."""
    base, _, name = part.rpartition("/")
    rel_path = f"{base}/_rels/{name}.rels"
    try:
        root = ET.fromstring(z.read(rel_path))
    except KeyError:
        return {}
    out = {}
    for rel in root:
        target = rel.get("Target")
        if target.startswith("/"):
            target = target.lstrip("/")
        elif target.startswith("../"):
            target = "xl/" + target[3:]
        elif not target.startswith("xl/"):
            target = f"{base}/{target}"
        out[rel.get("Id")] = target
    return out


def _drawings(z: zipfile.ZipFile, sheet_part: str,
              cache: dict) -> tuple[list[Image], list[Shape]]:
    sheet_rels = _rels(z, sheet_part)
    root = ET.fromstring(z.read(sheet_part))
    node = root.find(M + "drawing")
    if node is None:
        return [], []
    target = sheet_rels.get(node.get(R + "id"))
    if not target:
        return [], []

    draw_rels = _rels(z, target)
    droot = ET.fromstring(z.read(target))
    images: list[Image] = []
    shapes: list[Shape] = []

    for anchor in droot:
        frm = anchor.find(X + "from")
        if frm is None:
            continue
        row = int(frm.find(X + "row").text) + 1
        col = int(frm.find(X + "col").text) + 1

        pic = anchor.find(X + "pic")
        if pic is not None:
            blip = pic.find(f"{X}blipFill/{A}blip")
            media = draw_rels.get(blip.get(R + "embed")) if blip is not None else None
            if not media:
                continue
            if media not in cache:
                data = z.read(media)
                cache[media] = (data, hashlib.sha256(data).hexdigest())
            data, digest = cache[media]
            images.append(Image(row=row, col=col, media=media, data=data,
                                sha256=digest, size=len(data)))
            continue

        sp = anchor.find(X + "sp")
        if sp is not None:
            paras = []
            for para in sp.iter(A + "p"):
                txt = "".join(t.text or "" for t in para.iter(A + "t")).strip()
                if txt:
                    paras.append(txt)
            if paras:
                shapes.append(Shape(row=row, col=col, text="\n".join(paras)))

    return images, shapes


def load_workbook(path: str) -> Workbook:
    z = zipfile.ZipFile(path)
    strings, str_italic = _shared_strings(z)
    xf_fill, xf_ital, xf_fmt = _styles(z)

    wb_rels = _rels(z, "xl/workbook.xml")
    wb_root = ET.fromstring(z.read("xl/workbook.xml"))

    media_cache: dict = {}
    sheets: list[Sheet] = []

    for idx, sheet_el in enumerate(wb_root.find(M + "sheets")):
        part = wb_rels[sheet_el.get(R + "id")]
        sheet = Sheet(name=sheet_el.get("name"), index=idx)
        root = ET.fromstring(z.read(part))

        shared_masters: dict[str, tuple[str, int, int]] = {}

        for row_el in root.iter(M + "row"):
            for c in row_el:
                if c.tag != M + "c":
                    continue
                ref = c.get("r")
                if not ref:
                    continue
                row, col = parse_ref(ref)
                s = int(c.get("s", 0))
                ctype = c.get("t")

                fill = xf_fill[s] if s < len(xf_fill) else None
                italic = xf_ital[s] if s < len(xf_ital) else False
                fmt = xf_fmt[s] if s < len(xf_fmt) else None

                # ---- formula (expanding shared followers) ----
                formula = None
                f_el = c.find(M + "f")
                if f_el is not None:
                    ftype = f_el.get("t")
                    ftext = (f_el.text or "").strip()
                    si = f_el.get("si")
                    if ftype == "shared":
                        if ftext and si is not None:
                            shared_masters[si] = (ftext, row, col)
                            formula = ftext
                        elif si is not None and si in shared_masters:
                            base, brow, bcol = shared_masters[si]
                            formula = translate_formula(base, row - brow, col - bcol)
                    else:
                        formula = ftext or None
                    if formula and ftype == "array":
                        formula = "{" + formula + "}"

                # ---- value ----
                raw, text, numeric = None, "", False
                v_el = c.find(M + "v")
                if ctype == "inlineStr":
                    parts = [t.text or "" for t in c.iter(M + "t")]
                    raw = text = "".join(parts)
                elif v_el is not None and v_el.text is not None:
                    v = v_el.text
                    if ctype == "s":
                        i = int(v)
                        raw = text = strings[i] if i < len(strings) else ""
                        if i < len(str_italic) and str_italic[i]:
                            italic = True
                    elif ctype == "b":
                        raw = v == "1"
                        text = "TRUE" if raw else "FALSE"
                    elif ctype == "e":
                        raw = text = v
                    elif ctype == "str":
                        raw = text = v
                    else:
                        try:
                            raw = float(v)
                            text = format_number(raw, fmt)
                            numeric = True
                        except ValueError:
                            raw = text = v

                if isinstance(text, str):
                    text = text.replace("\r\n", "\n").strip()
                if not text and formula is None:
                    continue

                sheet.cells[(row, col)] = Cell(
                    row=row, col=col, text=text, raw=raw, formula=formula,
                    fill=fill, italic=italic, numeric=numeric,
                )

        node = root.find(M + "mergeCells")
        if node is not None:
            sheet.merges = [mc.get("ref") for mc in node]

        sheet.images, sheet.shapes = _drawings(z, part, media_cache)
        sheet.shapes.sort(key=lambda s: (s.row, s.col))
        sheets.append(sheet)

    z.close()
    return Workbook(path=path, sheets=sheets)


if __name__ == "__main__":  # smoke test
    import sys
    wb = load_workbook(sys.argv[1])
    print(f"{len(wb.sheets)} sheets")
    for s in wb.sheets[:5]:
        nf = sum(1 for c in s.cells.values() if c.formula)
        ng = sum(1 for c in s.cells.values() if c.is_gray)
        print(f"  {s.name[:40]:42} cells={len(s.cells):4} formulas={nf:4} "
              f"gray={ng:4} imgs={len(s.images)}")

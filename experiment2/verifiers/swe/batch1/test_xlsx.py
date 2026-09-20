"""Task-aligned conservative verifier for xlsx."""

import os
import re
from pathlib import Path
import pytest

REPO_DIR = Path(os.environ.get("REPO_DIR", "/workspace/openpyxl"))

def _read(rel):
    p = REPO_DIR / rel
    assert p.is_file(), f"Required file does not exist: {p}"
    return p.read_text(encoding="utf-8", errors="replace")

def _strip_comments(text):
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
    return re.sub(r"//[^\n]*", "", text)

def _interface_body(text, name):
    m = re.search(r"\binterface\s+" + re.escape(name) + r"\b[^{]*\{", text)
    if not m:
        return None
    start = text.find("{", m.start())
    depth = 0
    quote = None
    escaped = False
    i = start
    while i < len(text):
        ch = text[i]
        if quote is not None:
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == quote:
                quote = None
            i += 1
            continue
        if text.startswith("//", i):
            j = text.find("\n", i + 2)
            i = len(text) if j < 0 else j + 1
            continue
        if text.startswith("/*", i):
            j = text.find("*/", i + 2)
            if j < 0:
                return None
            i = j + 2
            continue
        if ch in {"'", '"', "`"}:
            quote = ch
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return text[start+1:i]
        i += 1
    return None

def _field_type(body, field, typ):
    if body is None:
        return False
    body = _strip_comments(body)
    body = re.sub(r"\s+", "", body)
    field = re.escape(re.sub(r"\s+", "", field))
    typ = re.escape(re.sub(r"\s+", "", typ))
    return bool(re.search(r"(^|[;,{])" + field + r"\??:" + typ + r"(?=[;,}]|$)", body))

def _string_literal(text, value):
    text = _strip_comments(text)
    return bool(re.search(r"(['\"])" + re.escape(value) + r"\1", text))

def _identifier(text, value):
    text = _strip_comments(text)
    return bool(re.search(r"\b" + re.escape(value) + r"\b", text))

def test_r1_file_exists():
    # File openpyxl/utils/report_engine.py must exist
    p = REPO_DIR / 'openpyxl/utils/report_engine.py'
    assert p.is_file(), 'Missing required file: openpyxl/utils/report_engine.py'

def test_r2_identifier_in_file():
    # Function generate_sales_report with signature (data: List[Dict], output_path: str) -> None must exist in report_engine.py
    text = _read('openpyxl/utils/report_engine.py')
    assert _identifier(text, 'generate_sales_report'), 'Missing required identifier: generate_sales_report'

def test_r8_identifier_in_file():
    # Module contains BarChart implementation for category comparison
    text = _read('openpyxl/utils/report_engine.py')
    assert _identifier(text, 'BarChart'), 'Missing required identifier: BarChart'

def test_r9_identifier_in_file():
    # Module contains PieChart implementation for distribution
    text = _read('openpyxl/utils/report_engine.py')
    assert _identifier(text, 'PieChart'), 'Missing required identifier: PieChart'

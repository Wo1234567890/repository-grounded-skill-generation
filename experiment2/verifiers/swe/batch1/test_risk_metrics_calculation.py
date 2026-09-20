"""Task-aligned conservative verifier for risk-metrics-calculation."""

import os
import re
from pathlib import Path
import pytest

REPO_DIR = Path(os.environ.get("REPO_DIR", "/workspace/pyfolio"))

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
    # Example script file must exist at examples/risk_metrics_demo.py
    p = REPO_DIR / 'examples/risk_metrics_demo.py'
    assert p.is_file(), 'Missing required file: examples/risk_metrics_demo.py'

def test_r2_file_exists():
    # Unit test file must exist at tests/test_risk_metrics.py
    p = REPO_DIR / 'tests/test_risk_metrics.py'
    assert p.is_file(), 'Missing required file: tests/test_risk_metrics.py'

def test_r3_string_literal_in_file():
    # Example script demonstrates Sharpe Ratio calculation
    text = _read('examples/risk_metrics_demo.py')
    assert _string_literal(text, 'Sharpe Ratio'), 'Missing required string literal: Sharpe Ratio'

def test_r4_string_literal_in_file():
    # Example script demonstrates Maximum Drawdown calculation
    text = _read('examples/risk_metrics_demo.py')
    assert _string_literal(text, 'Maximum Drawdown'), 'Missing required string literal: Maximum Drawdown'

def test_r5_string_literal_in_file():
    # Example script demonstrates Sortino Ratio calculation
    text = _read('examples/risk_metrics_demo.py')
    assert _string_literal(text, 'Sortino Ratio'), 'Missing required string literal: Sortino Ratio'

def test_r6_string_literal_in_file():
    # Example script demonstrates Calmar Ratio calculation
    text = _read('examples/risk_metrics_demo.py')
    assert _string_literal(text, 'Calmar Ratio'), 'Missing required string literal: Calmar Ratio'

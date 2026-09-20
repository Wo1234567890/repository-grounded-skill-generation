"""Task-aligned conservative verifier for dbt-transformation-patterns."""

import os
import re
from pathlib import Path
import pytest

REPO_DIR = Path(os.environ.get("REPO_DIR", "/workspace/dbt-core"))

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
    # Python test file for model compilation must exist at tests/functional/staging/test_stg_orders.py
    p = REPO_DIR / 'tests/functional/staging/test_stg_orders.py'
    assert p.is_file(), 'Missing required file: tests/functional/staging/test_stg_orders.py'

def test_r2_file_exists():
    # Test fixtures file must exist at tests/functional/staging/fixtures.py
    p = REPO_DIR / 'tests/functional/staging/fixtures.py'
    assert p.is_file(), 'Missing required file: tests/functional/staging/fixtures.py'

def test_r3_file_exists():
    # Staging model SQL file must exist at core/dbt/tests/staging/stg_orders.sql
    p = REPO_DIR / 'core/dbt/tests/staging/stg_orders.sql'
    assert p.is_file(), 'Missing required file: core/dbt/tests/staging/stg_orders.sql'

def test_r4_file_exists():
    # Schema documentation file must exist at core/dbt/tests/staging/schema.yml
    p = REPO_DIR / 'core/dbt/tests/staging/schema.yml'
    assert p.is_file(), 'Missing required file: core/dbt/tests/staging/schema.yml'

def test_r5_string_literal_in_file():
    # Staging model must contain source() macro reference
    text = _read('core/dbt/tests/staging/stg_orders.sql')
    assert _string_literal(text, 'source('), 'Missing required string literal: source('

def test_r6_string_literal_in_file():
    # Staging model must contain materialization config block
    text = _read('core/dbt/tests/staging/stg_orders.sql')
    assert _string_literal(text, "config(materialized='view')"), "Missing required string literal: config(materialized='view')"

def test_r8_string_literal_in_file():
    # Schema documentation must contain unique test definition
    text = _read('core/dbt/tests/staging/schema.yml')
    assert _string_literal(text, 'unique'), 'Missing required string literal: unique'

def test_r9_string_literal_in_file():
    # Schema documentation must contain not_null test definition
    text = _read('core/dbt/tests/staging/schema.yml')
    assert _string_literal(text, 'not_null'), 'Missing required string literal: not_null'

def test_r10_string_literal_in_file():
    # Schema documentation must reference custom test assert_positive_amounts
    text = _read('core/dbt/tests/staging/schema.yml')
    assert _string_literal(text, 'assert_positive_amounts'), 'Missing required string literal: assert_positive_amounts'

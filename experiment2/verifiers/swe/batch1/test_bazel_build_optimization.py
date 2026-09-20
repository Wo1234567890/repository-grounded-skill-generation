"""Task-aligned conservative verifier for bazel-build-optimization."""

import os
import re
from pathlib import Path
import pytest

REPO_DIR = Path(os.environ.get("REPO_DIR", "/workspace/bazel"))

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
    # WORKSPACE file must exist at examples/python-bazel/WORKSPACE
    p = REPO_DIR / 'examples/python-bazel/WORKSPACE'
    assert p.is_file(), 'Missing required file: examples/python-bazel/WORKSPACE'

def test_r2_file_exists():
    # Root BUILD.bazel file must exist at examples/python-bazel/BUILD.bazel
    p = REPO_DIR / 'examples/python-bazel/BUILD.bazel'
    assert p.is_file(), 'Missing required file: examples/python-bazel/BUILD.bazel'

def test_r3_file_exists():
    # .bazelrc configuration file must exist at examples/python-bazel/.bazelrc
    p = REPO_DIR / 'examples/python-bazel/.bazelrc'
    assert p.is_file(), 'Missing required file: examples/python-bazel/.bazelrc'

def test_r4_file_exists():
    # Source BUILD.bazel file must exist at examples/python-bazel/src/BUILD.bazel
    p = REPO_DIR / 'examples/python-bazel/src/BUILD.bazel'
    assert p.is_file(), 'Missing required file: examples/python-bazel/src/BUILD.bazel'

def test_r5_file_exists():
    # Sample Python source file must exist at examples/python-bazel/src/main.py
    p = REPO_DIR / 'examples/python-bazel/src/main.py'
    assert p.is_file(), 'Missing required file: examples/python-bazel/src/main.py'

def test_r6_file_exists():
    # Tests BUILD.bazel file must exist at examples/python-bazel/tests/BUILD.bazel
    p = REPO_DIR / 'examples/python-bazel/tests/BUILD.bazel'
    assert p.is_file(), 'Missing required file: examples/python-bazel/tests/BUILD.bazel'

def test_r7_string_literal_in_file():
    # .bazelrc must contain remote cache configuration placeholder
    text = _read('examples/python-bazel/.bazelrc')
    assert _string_literal(text, 'remote_cache'), 'Missing required string literal: remote_cache'

def test_r8_string_literal_in_file():
    # .bazelrc must contain remote execution flags placeholder
    text = _read('examples/python-bazel/.bazelrc')
    assert _string_literal(text, 'remote_executor'), 'Missing required string literal: remote_executor'

def test_r9_string_literal_in_file():
    # .bazelrc must contain spawn_strategy options
    text = _read('examples/python-bazel/.bazelrc')
    assert _string_literal(text, 'spawn_strategy'), 'Missing required string literal: spawn_strategy'

def test_r10_string_literal_in_file():
    # .bazelrc must contain disk_cache for local caching
    text = _read('examples/python-bazel/.bazelrc')
    assert _string_literal(text, 'disk_cache'), 'Missing required string literal: disk_cache'

def test_r11_identifier_in_file():
    # src/BUILD.bazel must define py_binary target //src:main
    text = _read('examples/python-bazel/src/BUILD.bazel')
    assert _identifier(text, 'py_binary'), 'Missing required identifier: py_binary'

def test_r12_identifier_in_file():
    # tests/BUILD.bazel must define py_test targets
    text = _read('examples/python-bazel/tests/BUILD.bazel')
    assert _identifier(text, 'py_test'), 'Missing required identifier: py_test'

"""Task-aligned conservative verifier for v3-performance-optimization."""

import os
import re
from pathlib import Path
import pytest

REPO_DIR = Path(os.environ.get("REPO_DIR", "/workspace/flash-attention"))

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
    # Create benchmarks/benchmark_attention.py file
    p = REPO_DIR / 'benchmarks/benchmark_attention.py'
    assert p.is_file(), 'Missing required file: benchmarks/benchmark_attention.py'

def test_r2_file_exists():
    # Create benchmarks/configs/benchmark_config.yaml file
    p = REPO_DIR / 'benchmarks/configs/benchmark_config.yaml'
    assert p.is_file(), 'Missing required file: benchmarks/configs/benchmark_config.yaml'

def test_r3_file_exists():
    # Create examples/optimization_demo.py file
    p = REPO_DIR / 'examples/optimization_demo.py'
    assert p.is_file(), 'Missing required file: examples/optimization_demo.py'

def test_r4_string_literal_in_file():
    # benchmark_config.yaml contains batch_sizes configuration
    text = _read('benchmarks/configs/benchmark_config.yaml')
    assert _string_literal(text, 'batch_sizes'), 'Missing required string literal: batch_sizes'

def test_r5_string_literal_in_file():
    # benchmark_config.yaml contains seq_lengths configuration
    text = _read('benchmarks/configs/benchmark_config.yaml')
    assert _string_literal(text, 'seq_lengths'), 'Missing required string literal: seq_lengths'

def test_r6_string_literal_in_file():
    # benchmark_config.yaml contains head_dim configuration
    text = _read('benchmarks/configs/benchmark_config.yaml')
    assert _string_literal(text, 'head_dim'), 'Missing required string literal: head_dim'

def test_r7_string_literal_in_file():
    # benchmark_config.yaml contains num_heads configuration
    text = _read('benchmarks/configs/benchmark_config.yaml')
    assert _string_literal(text, 'num_heads'), 'Missing required string literal: num_heads'

def test_r8_string_literal_in_file():
    # benchmark_config.yaml contains dtype configuration
    text = _read('benchmarks/configs/benchmark_config.yaml')
    assert _string_literal(text, 'dtype'), 'Missing required string literal: dtype'

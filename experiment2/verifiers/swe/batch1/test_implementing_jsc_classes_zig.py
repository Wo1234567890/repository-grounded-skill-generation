"""Task-aligned conservative verifier for implementing-jsc-classes-zig."""

import os
import re
from pathlib import Path
import pytest

REPO_DIR = Path(os.environ.get("REPO_DIR", "/workspace/bun"))

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
    # File BunHash.classes.ts must exist at src/bun.js/api/BunHash.classes.ts
    p = REPO_DIR / 'src/bun.js/api/BunHash.classes.ts'
    assert p.is_file(), 'Missing required file: src/bun.js/api/BunHash.classes.ts'

def test_r2_file_exists():
    # File BunHash.zig must exist at src/bun.js/api/BunHash.zig
    p = REPO_DIR / 'src/bun.js/api/BunHash.zig'
    assert p.is_file(), 'Missing required file: src/bun.js/api/BunHash.zig'

def test_r3_file_exists():
    # File hash.test.ts must exist at test/js/bun/hash/hash.test.ts
    p = REPO_DIR / 'test/js/bun/hash/hash.test.ts'
    assert p.is_file(), 'Missing required file: test/js/bun/hash/hash.test.ts'

def test_r4_string_literal_in_file():
    # BunHash.classes.ts must define class with name 'BunHash'
    text = _read('src/bun.js/api/BunHash.classes.ts')
    assert _string_literal(text, 'BunHash'), 'Missing required string literal: BunHash'

def test_r5_string_literal_in_file():
    # BunHash.classes.ts must include constructor: true property
    text = _read('src/bun.js/api/BunHash.classes.ts')
    assert _string_literal(text, 'constructor'), 'Missing required string literal: constructor'

def test_r6_string_literal_in_file():
    # BunHash.classes.ts must include finalize: true property
    text = _read('src/bun.js/api/BunHash.classes.ts')
    assert _string_literal(text, 'finalize'), 'Missing required string literal: finalize'

def test_r7_string_literal_in_file():
    # BunHash.classes.ts must define prototype method 'hash'
    text = _read('src/bun.js/api/BunHash.classes.ts')
    assert _string_literal(text, 'hash'), 'Missing required string literal: hash'

def test_r8_string_literal_in_file():
    # BunHash.classes.ts must define prototype method 'digest'
    text = _read('src/bun.js/api/BunHash.classes.ts')
    assert _string_literal(text, 'digest'), 'Missing required string literal: digest'

def test_r9_string_literal_in_file():
    # BunHash.classes.ts must define prototype getter 'algorithm'
    text = _read('src/bun.js/api/BunHash.classes.ts')
    assert _string_literal(text, 'algorithm'), 'Missing required string literal: algorithm'

def test_r11_string_literal_in_file():
    # BunHash.zig must support 'murmur3' algorithm
    text = _read('src/bun.js/api/BunHash.zig')
    assert _string_literal(text, 'murmur3'), 'Missing required string literal: murmur3'

def test_r12_string_literal_in_file():
    # BunHash.zig must support 'xxhash32' algorithm
    text = _read('src/bun.js/api/BunHash.zig')
    assert _string_literal(text, 'xxhash32'), 'Missing required string literal: xxhash32'

def test_r13_string_literal_in_file():
    # BunHash.zig must support 'xxhash64' algorithm
    text = _read('src/bun.js/api/BunHash.zig')
    assert _string_literal(text, 'xxhash64'), 'Missing required string literal: xxhash64'

def test_r14_string_literal_in_file():
    # BunHash.zig must support 'wyhash' algorithm
    text = _read('src/bun.js/api/BunHash.zig')
    assert _string_literal(text, 'wyhash'), 'Missing required string literal: wyhash'

def test_r20_string_literal_in_file():
    # Test suite must test empty string scenario
    text = _read('test/js/bun/hash/hash.test.ts')
    assert _string_literal(text, 'empty'), 'Missing required string literal: empty'

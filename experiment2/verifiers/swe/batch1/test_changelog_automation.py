"""Task-aligned conservative verifier for changelog-automation."""

import os
import re
from pathlib import Path
import pytest

REPO_DIR = Path(os.environ.get("REPO_DIR", "/workspace/github-changelog-generator"))

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
    # Configuration file must exist at examples/advanced_config/.github_changelog_generator
    p = REPO_DIR / 'examples/advanced_config/.github_changelog_generator'
    assert p.is_file(), 'Missing required file: examples/advanced_config/.github_changelog_generator'

def test_r2_file_exists():
    # Sample output file must exist at examples/advanced_config/CHANGELOG.md
    p = REPO_DIR / 'examples/advanced_config/CHANGELOG.md'
    assert p.is_file(), 'Missing required file: examples/advanced_config/CHANGELOG.md'

def test_r3_file_exists():
    # Documentation file must exist at examples/advanced_config/README.md
    p = REPO_DIR / 'examples/advanced_config/README.md'
    assert p.is_file(), 'Missing required file: examples/advanced_config/README.md'

def test_r4_string_literal_in_file():
    # Configuration file contains enhancement-labels setting with values ["enhancement", "feature"]
    text = _read('examples/advanced_config/.github_changelog_generator')
    assert _string_literal(text, 'enhancement'), 'Missing required string literal: enhancement'

def test_r5_string_literal_in_file():
    # Configuration file contains bug-labels setting with values ["bug", "fix"]
    text = _read('examples/advanced_config/.github_changelog_generator')
    assert _string_literal(text, 'bug'), 'Missing required string literal: bug'

def test_r6_string_literal_in_file():
    # Configuration file contains breaking-labels setting with value ["breaking-change"]
    text = _read('examples/advanced_config/.github_changelog_generator')
    assert _string_literal(text, 'breaking-change'), 'Missing required string literal: breaking-change'

def test_r7_string_literal_in_file():
    # Configuration file contains exclude-labels setting with values ["duplicate", "wontfix"]
    text = _read('examples/advanced_config/.github_changelog_generator')
    assert _string_literal(text, 'duplicate'), 'Missing required string literal: duplicate'

def test_r8_identifier_in_file():
    # Configuration file contains since_tag and due_tag options
    text = _read('examples/advanced_config/.github_changelog_generator')
    assert _identifier(text, 'since_tag'), 'Missing required identifier: since_tag'

def test_r9_identifier_in_file():
    # Configuration file contains unreleased option set to true or false
    text = _read('examples/advanced_config/.github_changelog_generator')
    assert _identifier(text, 'unreleased'), 'Missing required identifier: unreleased'

def test_r10_string_literal_in_file():
    # Configuration file contains breaking_prefix setting with value "**Breaking Changes:**"
    text = _read('examples/advanced_config/.github_changelog_generator')
    assert _string_literal(text, '**Breaking Changes:**'), 'Missing required string literal: **Breaking Changes:**'

def test_r11_identifier_in_file():
    # Configuration file contains header custom header text option
    text = _read('examples/advanced_config/.github_changelog_generator')
    assert _identifier(text, 'header'), 'Missing required identifier: header'

def test_r12_string_literal_in_file():
    # Configuration file contains base option referencing HISTORY.md
    text = _read('examples/advanced_config/.github_changelog_generator')
    assert _string_literal(text, 'HISTORY.md'), 'Missing required string literal: HISTORY.md'

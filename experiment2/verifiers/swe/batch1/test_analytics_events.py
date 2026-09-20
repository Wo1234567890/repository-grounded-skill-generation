"""Task-aligned conservative verifier for analytics-events."""

import os
import re
from pathlib import Path
import pytest

REPO_DIR = Path(os.environ.get("REPO_DIR", "/workspace/metabase"))

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
    # Event definitions file must exist at frontend/src/metabase/lib/analytics.ts
    p = REPO_DIR / 'frontend/src/metabase/lib/analytics.ts'
    assert p.is_file(), 'Missing required file: frontend/src/metabase/lib/analytics.ts'

def test_r2_file_exists():
    # Unit tests file must exist at frontend/test/metabase/lib/analytics.test.ts
    p = REPO_DIR / 'frontend/test/metabase/lib/analytics.test.ts'
    assert p.is_file(), 'Missing required file: frontend/test/metabase/lib/analytics.test.ts'

def test_r3_ts_interface_fields():
    # AnalyticsEvent interface must exist with exact fields: event_name (string), payload (Record<string, unknown>), timestamp (number)
    text = _read('frontend/src/metabase/lib/analytics.ts')
    body = _interface_body(text, 'AnalyticsEvent')
    assert body is not None, 'Missing required interface: AnalyticsEvent'
    assert _field_type(body, 'event_name', 'string'), 'AnalyticsEvent missing exact field/type event_name: string'
    assert _field_type(body, 'payload', 'Record<string, unknown>'), 'AnalyticsEvent missing exact field/type payload: Record<string, unknown>'
    assert _field_type(body, 'timestamp', 'number'), 'AnalyticsEvent missing exact field/type timestamp: number'

def test_r4_string_literal_in_file():
    # Event name 'dashboard_viewed' must be defined in analytics.ts
    text = _read('frontend/src/metabase/lib/analytics.ts')
    assert _string_literal(text, 'dashboard_viewed'), 'Missing required string literal: dashboard_viewed'

def test_r5_string_literal_in_file():
    # Event name 'question_saved' must be defined in analytics.ts
    text = _read('frontend/src/metabase/lib/analytics.ts')
    assert _string_literal(text, 'question_saved'), 'Missing required string literal: question_saved'

def test_r6_string_literal_in_file():
    # Event name 'filter_applied' must be defined in analytics.ts
    text = _read('frontend/src/metabase/lib/analytics.ts')
    assert _string_literal(text, 'filter_applied'), 'Missing required string literal: filter_applied'

def test_r7_string_literal_in_file():
    # dashboard_viewed payload must include field 'dashboard_id'
    text = _read('frontend/src/metabase/lib/analytics.ts')
    assert _string_literal(text, 'dashboard_id'), 'Missing required string literal: dashboard_id'

def test_r8_string_literal_in_file():
    # dashboard_viewed payload must include field 'view_duration_ms'
    text = _read('frontend/src/metabase/lib/analytics.ts')
    assert _string_literal(text, 'view_duration_ms'), 'Missing required string literal: view_duration_ms'

def test_r9_string_literal_in_file():
    # dashboard_viewed payload must include field 'card_count'
    text = _read('frontend/src/metabase/lib/analytics.ts')
    assert _string_literal(text, 'card_count'), 'Missing required string literal: card_count'

def test_r10_string_literal_in_file():
    # question_saved payload must include field 'question_id'
    text = _read('frontend/src/metabase/lib/analytics.ts')
    assert _string_literal(text, 'question_id'), 'Missing required string literal: question_id'

def test_r11_string_literal_in_file():
    # question_saved payload must include field 'question_type'
    text = _read('frontend/src/metabase/lib/analytics.ts')
    assert _string_literal(text, 'question_type'), 'Missing required string literal: question_type'

def test_r12_string_literal_in_file():
    # question_saved payload must include field 'database_id'
    text = _read('frontend/src/metabase/lib/analytics.ts')
    assert _string_literal(text, 'database_id'), 'Missing required string literal: database_id'

def test_r13_string_literal_in_file():
    # question_saved payload must include field 'save_duration_ms'
    text = _read('frontend/src/metabase/lib/analytics.ts')
    assert _string_literal(text, 'save_duration_ms'), 'Missing required string literal: save_duration_ms'

def test_r14_string_literal_in_file():
    # filter_applied payload must include field 'dashboard_id'
    text = _read('frontend/src/metabase/lib/analytics.ts')
    assert _string_literal(text, 'dashboard_id'), 'Missing required string literal: dashboard_id'

def test_r15_string_literal_in_file():
    # filter_applied payload must include field 'filter_type'
    text = _read('frontend/src/metabase/lib/analytics.ts')
    assert _string_literal(text, 'filter_type'), 'Missing required string literal: filter_type'

def test_r16_string_literal_in_file():
    # filter_applied payload must include field 'filter_value_count'
    text = _read('frontend/src/metabase/lib/analytics.ts')
    assert _string_literal(text, 'filter_value_count'), 'Missing required string literal: filter_value_count'

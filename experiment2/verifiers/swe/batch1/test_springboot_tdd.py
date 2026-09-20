"""Task-aligned conservative verifier for springboot-tdd."""

import os
import re
from pathlib import Path
import pytest

REPO_DIR = Path(os.environ.get("REPO_DIR", "/workspace/spring-petclinic"))

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
    # WeightRecord.java entity file must exist
    p = REPO_DIR / 'src/main/java/org/springframework/samples/petclinic/owner/WeightRecord.java'
    assert p.is_file(), 'Missing required file: src/main/java/org/springframework/samples/petclinic/owner/WeightRecord.java'

def test_r2_ts_interface_fields():
    # WeightRecord entity has id field of type Long
    text = _read('src/main/java/org/springframework/samples/petclinic/owner/WeightRecord.java')
    body = _interface_body(text, 'WeightRecord')
    assert body is not None, 'Missing required interface: WeightRecord'
    assert _field_type(body, 'id', 'Long'), 'WeightRecord missing exact field/type id: Long'

def test_r3_ts_interface_fields():
    # WeightRecord entity has petId field of type Long
    text = _read('src/main/java/org/springframework/samples/petclinic/owner/WeightRecord.java')
    body = _interface_body(text, 'WeightRecord')
    assert body is not None, 'Missing required interface: WeightRecord'
    assert _field_type(body, 'petId', 'Long'), 'WeightRecord missing exact field/type petId: Long'

def test_r4_ts_interface_fields():
    # WeightRecord entity has weightKg field of type Double
    text = _read('src/main/java/org/springframework/samples/petclinic/owner/WeightRecord.java')
    body = _interface_body(text, 'WeightRecord')
    assert body is not None, 'Missing required interface: WeightRecord'
    assert _field_type(body, 'weightKg', 'Double'), 'WeightRecord missing exact field/type weightKg: Double'

def test_r5_ts_interface_fields():
    # WeightRecord entity has recordDate field of type LocalDate
    text = _read('src/main/java/org/springframework/samples/petclinic/owner/WeightRecord.java')
    body = _interface_body(text, 'WeightRecord')
    assert body is not None, 'Missing required interface: WeightRecord'
    assert _field_type(body, 'recordDate', 'LocalDate'), 'WeightRecord missing exact field/type recordDate: LocalDate'

def test_r6_file_exists():
    # WeightRecordRepository.java file must exist
    p = REPO_DIR / 'src/main/java/org/springframework/samples/petclinic/owner/WeightRecordRepository.java'
    assert p.is_file(), 'Missing required file: src/main/java/org/springframework/samples/petclinic/owner/WeightRecordRepository.java'

def test_r7_identifier_in_file():
    # WeightRecordRepository extends JpaRepository<WeightRecord, Long>
    text = _read('src/main/java/org/springframework/samples/petclinic/owner/WeightRecordRepository.java')
    assert _identifier(text, 'JpaRepository'), 'Missing required identifier: JpaRepository'

def test_r8_identifier_in_file():
    # WeightRecordRepository has findByPetIdOrderByRecordDateDesc method
    text = _read('src/main/java/org/springframework/samples/petclinic/owner/WeightRecordRepository.java')
    assert _identifier(text, 'findByPetIdOrderByRecordDateDesc'), 'Missing required identifier: findByPetIdOrderByRecordDateDesc'

def test_r9_file_exists():
    # OwnerController.java must exist
    p = REPO_DIR / 'src/main/java/org/springframework/samples/petclinic/owner/OwnerController.java'
    assert p.is_file(), 'Missing required file: src/main/java/org/springframework/samples/petclinic/owner/OwnerController.java'

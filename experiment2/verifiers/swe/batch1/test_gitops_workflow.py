"""Task-aligned conservative verifier for gitops-workflow."""

import os
import re
from pathlib import Path
import pytest

REPO_DIR = Path(os.environ.get("REPO_DIR", "/workspace/flux2"))

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
    # File hack/gitops-demo/clusters/dev/flux-system/gotk-components.yaml must exist
    p = REPO_DIR / 'hack/gitops-demo/clusters/dev/flux-system/gotk-components.yaml'
    assert p.is_file(), 'Missing required file: hack/gitops-demo/clusters/dev/flux-system/gotk-components.yaml'

def test_r2_file_exists():
    # File hack/gitops-demo/clusters/dev/flux-system/kustomization.yaml must exist
    p = REPO_DIR / 'hack/gitops-demo/clusters/dev/flux-system/kustomization.yaml'
    assert p.is_file(), 'Missing required file: hack/gitops-demo/clusters/dev/flux-system/kustomization.yaml'

def test_r3_file_exists():
    # File hack/gitops-demo/apps/base/deployment.yaml must exist
    p = REPO_DIR / 'hack/gitops-demo/apps/base/deployment.yaml'
    assert p.is_file(), 'Missing required file: hack/gitops-demo/apps/base/deployment.yaml'

def test_r4_file_exists():
    # File hack/gitops-demo/apps/base/service.yaml must exist
    p = REPO_DIR / 'hack/gitops-demo/apps/base/service.yaml'
    assert p.is_file(), 'Missing required file: hack/gitops-demo/apps/base/service.yaml'

def test_r5_file_exists():
    # File hack/gitops-demo/apps/base/kustomization.yaml must exist
    p = REPO_DIR / 'hack/gitops-demo/apps/base/kustomization.yaml'
    assert p.is_file(), 'Missing required file: hack/gitops-demo/apps/base/kustomization.yaml'

def test_r6_file_exists():
    # File hack/gitops-demo/apps/overlays/dev/kustomization.yaml must exist
    p = REPO_DIR / 'hack/gitops-demo/apps/overlays/dev/kustomization.yaml'
    assert p.is_file(), 'Missing required file: hack/gitops-demo/apps/overlays/dev/kustomization.yaml'

def test_r7_file_exists():
    # File hack/gitops-demo/apps/overlays/dev/patch-replicas.yaml must exist
    p = REPO_DIR / 'hack/gitops-demo/apps/overlays/dev/patch-replicas.yaml'
    assert p.is_file(), 'Missing required file: hack/gitops-demo/apps/overlays/dev/patch-replicas.yaml'

def test_r8_file_exists():
    # File hack/verify-gitops-demo.sh must exist
    p = REPO_DIR / 'hack/verify-gitops-demo.sh'
    assert p.is_file(), 'Missing required file: hack/verify-gitops-demo.sh'

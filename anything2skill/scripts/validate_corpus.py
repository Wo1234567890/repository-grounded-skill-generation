from pathlib import Path
from html.parser import HTMLParser
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
A2S = ROOT / "anything2skill"

REGISTRY = A2S / "configs" / "corpus_registry.json"
REPORT = A2S / "configs" / "corpus_validation.json"

with REGISTRY.open("r", encoding="utf-8") as f:
    registry = json.load(f)


def sha256_file(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


class VisibleTextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.hidden_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag.lower() in {"script", "style", "noscript", "svg"}:
            self.hidden_depth += 1

    def handle_endtag(self, tag):
        if (
            tag.lower() in {"script", "style", "noscript", "svg"}
            and self.hidden_depth > 0
        ):
            self.hidden_depth -= 1

    def handle_data(self, data):
        if self.hidden_depth == 0:
            self.parts.append(data)

    def text(self):
        return re.sub(r"\s+", " ", " ".join(self.parts)).strip()


BAD_PAGE_MARKERS = [
    "404 not found",
    "page not found",
    "access denied",
    "403 forbidden",
    "captcha",
    "just a moment...",
    "checking your browser",
]


results = []

for source in registry["sources"]:
    sid = source["source_id"]
    local_file = source.get("local_file")

    item = {
        "source_id": sid,
        "title": source.get("title"),
        "local_file": local_file,
        "status": "PASS",
        "checks": [],
        "warnings": [],
    }

    if not local_file:
        item["status"] = "FAIL"
        item["warnings"].append("No local_file recorded.")
        results.append(item)
        continue

    path = ROOT / local_file

    if not path.exists():
        item["status"] = "FAIL"
        item["warnings"].append("File does not exist.")
        results.append(item)
        continue

    size = path.stat().st_size
    item["bytes"] = size

    if size == 0:
        item["status"] = "FAIL"
        item["warnings"].append("File is empty.")
        results.append(item)
        continue

    item["checks"].append("file_exists")
    item["checks"].append("non_empty")

    actual_sha = sha256_file(path)
    item["actual_sha256"] = actual_sha

    expected_sha = source.get("sha256")

    if expected_sha == actual_sha:
        item["checks"].append("sha256_match")
    else:
        item["status"] = "FAIL"
        item["warnings"].append("SHA256 does not match registry.")

    suffix = path.suffix.lower()

    # --------------------------------------------------
    # PDF validation
    # --------------------------------------------------
    if suffix == ".pdf":
        raw = path.read_bytes()

        if raw.startswith(b"%PDF"):
            item["checks"].append("valid_pdf_header")
        else:
            item["status"] = "FAIL"
            item["warnings"].append("Missing PDF header.")

        if size < 10000:
            item["warnings"].append("PDF is unusually small.")

    # --------------------------------------------------
    # HTML validation
    # --------------------------------------------------
    elif suffix in {".html", ".htm"}:
        raw = path.read_text(
            encoding="utf-8",
            errors="replace"
        )

        parser = VisibleTextParser()

        try:
            parser.feed(raw)
            visible = parser.text()
        except Exception:
            visible = re.sub(r"<[^>]+>", " ", raw)
            visible = re.sub(r"\s+", " ", visible).strip()

        item["visible_text_chars"] = len(visible)
        item["preview"] = visible[:300]

        lower = visible.lower()

        bad_hits = [
            marker
            for marker in BAD_PAGE_MARKERS
            if marker in lower[:5000]
        ]

        if bad_hits:
            item["status"] = "FAIL"
            item["warnings"].append(
                "Possible error/block page: " + ", ".join(bad_hits)
            )

        if len(visible) < 500:
            item["status"] = "FAIL"
            item["warnings"].append(
                "HTML contains too little visible text."
            )
        else:
            item["checks"].append("html_has_visible_text")

    # --------------------------------------------------
    # Markdown / text validation
    # --------------------------------------------------
    elif suffix in {".md", ".txt"}:
        text = path.read_text(
            encoding="utf-8",
            errors="replace"
        ).strip()

        item["text_chars"] = len(text)
        item["preview"] = re.sub(r"\s+", " ", text)[:300]

        if len(text) < 200:
            item["status"] = "FAIL"
            item["warnings"].append(
                "Text document is unusually short."
            )
        else:
            item["checks"].append("text_content_present")

    else:
        item["warnings"].append(
            f"Unknown extension: {suffix}"
        )

    results.append(item)


REPORT.write_text(
    json.dumps(
        results,
        indent=2,
        ensure_ascii=False
    ) + "\n",
    encoding="utf-8"
)

passed = [r for r in results if r["status"] == "PASS"]
failed = [r for r in results if r["status"] == "FAIL"]

print("=" * 70)
print("CORPUS VALIDATION")
print("=" * 70)

for r in results:
    print(
        f"{r['status']:4}  "
        f"{r['source_id']:28} "
        f"{r.get('bytes', 0):>10} bytes"
    )

    for warning in r["warnings"]:
        print("      WARNING:", warning)

print()
print("TOTAL :", len(results))
print("PASS  :", len(passed))
print("FAIL  :", len(failed))
print()
print("Report:", REPORT)

if failed:
    print()
    print("FAILED SOURCES:")
    for r in failed:
        print("-", r["source_id"])

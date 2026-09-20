from pathlib import Path
from html.parser import HTMLParser
from datetime import datetime, timezone
import subprocess
import hashlib
import shutil
import json
import re

ROOT = Path(__file__).resolve().parents[2]
A2S = ROOT / "anything2skill"

REGISTRY = A2S / "configs" / "corpus_registry.json"
OUT_DIR = A2S / "corpus_normalized"
MANIFEST = A2S / "configs" / "normalization_manifest.json"

OUT_DIR.mkdir(parents=True, exist_ok=True)


def sha256_file(path):
    h = hashlib.sha256()

    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)

    return h.hexdigest()


class HTMLToMarkdown(HTMLParser):

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.hidden = 0
        self.heading_level = None
        self.in_pre = False

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()

        if tag in {"script", "style", "noscript", "svg"}:
            self.hidden += 1
            return

        if self.hidden:
            return

        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.heading_level = int(tag[1])
            self.parts.append(
                "\n\n" + "#" * self.heading_level + " "
            )

        elif tag == "p":
            self.parts.append("\n\n")

        elif tag == "br":
            self.parts.append("\n")

        elif tag == "li":
            self.parts.append("\n- ")

        elif tag in {"ul", "ol"}:
            self.parts.append("\n")

        elif tag == "pre":
            self.in_pre = True
            self.parts.append("\n\n```\n")

        elif tag == "code" and not self.in_pre:
            self.parts.append("`")

        elif tag in {"section", "article", "main", "div"}:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        tag = tag.lower()

        if tag in {"script", "style", "noscript", "svg"}:
            if self.hidden > 0:
                self.hidden -= 1
            return

        if self.hidden:
            return

        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.heading_level = None
            self.parts.append("\n")

        elif tag == "p":
            self.parts.append("\n")

        elif tag == "pre":
            self.in_pre = False
            self.parts.append("\n```\n")

        elif tag == "code" and not self.in_pre:
            self.parts.append("`")

    def handle_data(self, data):
        if self.hidden:
            return

        if self.in_pre:
            self.parts.append(data)
        else:
            text = re.sub(r"[ \t\r\f\v]+", " ", data)
            self.parts.append(text)

    def markdown(self):
        text = "".join(self.parts)

        # Normalize excessive blank lines
        text = re.sub(r"\n[ \t]+\n", "\n\n", text)
        text = re.sub(r"\n{4,}", "\n\n\n", text)

        return text.strip() + "\n"


with REGISTRY.open("r", encoding="utf-8") as f:
    registry = json.load(f)

records = []

for source in registry["sources"]:

    sid = source["source_id"]
    local_file = source.get("local_file")

    print()
    print("=" * 70)
    print(sid)
    print("=" * 70)

    if not local_file:
        raise RuntimeError(
            f"{sid}: registry has no local_file"
        )

    src = ROOT / local_file

    if not src.exists():
        raise FileNotFoundError(src)

    original_sha = sha256_file(src)

    expected_sha = source.get("sha256")

    if original_sha != expected_sha:
        raise RuntimeError(
            f"{sid}: original SHA256 no longer matches registry"
        )

    suffix = src.suffix.lower()

    # --------------------------------------------------
    # Already-supported textual formats
    # --------------------------------------------------
    if suffix in {".txt", ".md", ".json", ".jsonl"}:

        dest = OUT_DIR / src.name

        shutil.copy2(src, dest)

        method = "identity_copy"

    # --------------------------------------------------
    # HTML -> Markdown-like text
    # --------------------------------------------------
    elif suffix in {".html", ".htm"}:

        raw = src.read_text(
            encoding="utf-8",
            errors="replace"
        )

        parser = HTMLToMarkdown()
        parser.feed(raw)

        text = parser.markdown()

        dest = OUT_DIR / f"{sid}.md"

        dest.write_text(
            text,
            encoding="utf-8"
        )

        method = "html_to_markdown_stdlib"

    # --------------------------------------------------
    # PDF -> text using pdftotext
    # --------------------------------------------------
    elif suffix == ".pdf":

        if shutil.which("pdftotext") is None:
            raise RuntimeError(
                "pdftotext is required for PDF normalization. "
                "Install it with: brew install poppler"
            )

        dest = OUT_DIR / f"{sid}.txt"

        subprocess.run(
            [
                "pdftotext",
                "-layout",
                "-enc",
                "UTF-8",
                str(src),
                str(dest)
            ],
            check=True
        )

        if not dest.exists():
            raise RuntimeError(
                f"{sid}: pdftotext produced no output"
            )

        method = "pdftotext_layout"

    else:
        raise RuntimeError(
            f"{sid}: unsupported source extension {suffix}"
        )

    normalized_sha = sha256_file(dest)

    record = {
        "source_id": sid,
        "title": source.get("title"),
        "source_type": source.get("source_type"),

        "original_file": str(
            src.relative_to(ROOT)
        ),

        "original_sha256": original_sha,

        "normalization_method": method,

        "normalized_file": str(
            dest.relative_to(ROOT)
        ),

        "normalized_sha256": normalized_sha,

        "normalized_bytes": dest.stat().st_size
    }

    records.append(record)

    print("METHOD :", method)
    print("OUTPUT :", dest)
    print("BYTES  :", dest.stat().st_size)
    print("SHA256 :", normalized_sha)


manifest = {
    "created_at_utc":
        datetime.now(timezone.utc).isoformat(),

    "upstream_component":
        "AutoSkill4Doc",

    "upstream_commit":
        "94c47ca488d4ba4117d20272e66d49b9877e68cf",

    "normalization_policy": {
        "txt_md_json_jsonl":
            "copied byte-for-byte",

        "html":
            "converted to Markdown-like visible text; "
            "script/style/noscript/svg content removed",

        "pdf":
            "converted with pdftotext -layout -enc UTF-8",

        "knowledge_selection":
            "no new external sources introduced during normalization"
    },

    "sources": records
}

MANIFEST.write_text(
    json.dumps(
        manifest,
        indent=2,
        ensure_ascii=False
    ) + "\n",
    encoding="utf-8"
)

print()
print("=" * 70)
print("NORMALIZATION SUMMARY")
print("=" * 70)

print("TOTAL:", len(records))
print("OUTPUT DIRECTORY:", OUT_DIR)
print("MANIFEST:", MANIFEST)

from pathlib import Path
from datetime import datetime, timezone
import urllib.request
import urllib.error
import hashlib
import shutil
import json

ROOT = Path(__file__).resolve().parents[2]
A2S = ROOT / "anything2skill"

REGISTRY = A2S / "configs" / "corpus_registry.json"
CORPUS_DIR = A2S / "corpus"
RECORD_DIR = A2S / "source_records"

CORPUS_DIR.mkdir(parents=True, exist_ok=True)
RECORD_DIR.mkdir(parents=True, exist_ok=True)

with REGISTRY.open("r", encoding="utf-8") as f:
    registry = json.load(f)


def sha256_file(path):
    h = hashlib.sha256()

    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)

    return h.hexdigest()


def choose_extension(url, content_type, data):
    lower = url.lower()

    if data.startswith(b"%PDF"):
        return ".pdf"

    if "application/pdf" in content_type:
        return ".pdf"

    if lower.endswith(".pdf"):
        return ".pdf"

    if lower.endswith(".md"):
        return ".md"

    if lower.endswith(".txt"):
        return ".txt"

    if "text/plain" in content_type:
        return ".txt"

    if "markdown" in content_type:
        return ".md"

    return ".html"


for source in registry["sources"]:

    sid = source["source_id"]

    print()
    print("=" * 70)
    print(sid)
    print("=" * 70)

    retrieved_at = datetime.now(timezone.utc).isoformat()

    try:

        # --------------------------------------------------
        # CASE 1: task-supplied local primary source
        # --------------------------------------------------

        preferred_local = source.get("preferred_local_source")

        if preferred_local:

            src = ROOT / preferred_local

            if not src.exists():
                raise FileNotFoundError(
                    f"Local source does not exist: {src}"
                )

            suffix = src.suffix if src.suffix else ".txt"

            dest = CORPUS_DIR / f"{sid}{suffix}"

            shutil.copy2(src, dest)

            digest = sha256_file(dest)

            source["local_file"] = str(
                dest.relative_to(ROOT)
            )

            source["retrieved_at_utc"] = retrieved_at
            source["sha256"] = digest
            source["acquisition_status"] = "success"
            source.pop("acquisition_error", None)

            record = {
                "source_id": sid,
                "title": source["title"],
                "source_type": source["source_type"],
                "acquisition_method": "local_copy",
                "source_path": preferred_local,
                "local_file": source["local_file"],
                "retrieved_at_utc": retrieved_at,
                "sha256": digest,
                "bytes": dest.stat().st_size
            }

            print("LOCAL ->", dest)
            print("SHA256:", digest)

        # --------------------------------------------------
        # CASE 2: web source
        # --------------------------------------------------

        else:

            url = source["url"]

            request = urllib.request.Request(
                url,
                headers={
                    "User-Agent":
                    "Mozilla/5.0 Anything2Skill-Research-Corpus/1.0"
                }
            )

            with urllib.request.urlopen(
                request,
                timeout=90
            ) as response:

                data = response.read()

                final_url = response.geturl()

                content_type = (
                    response.headers.get(
                        "Content-Type",
                        ""
                    )
                    .split(";")[0]
                    .strip()
                    .lower()
                )

            if len(data) == 0:
                raise RuntimeError("Downloaded file is empty.")

            suffix = choose_extension(
                final_url,
                content_type,
                data
            )

            dest = CORPUS_DIR / f"{sid}{suffix}"

            dest.write_bytes(data)

            digest = sha256_file(dest)

            source["local_file"] = str(
                dest.relative_to(ROOT)
            )

            source["retrieved_at_utc"] = retrieved_at
            source["sha256"] = digest
            source["acquisition_status"] = "success"
            source.pop("acquisition_error", None)

            record = {
                "source_id": sid,
                "title": source["title"],
                "source_type": source["source_type"],
                "acquisition_method": "web_download",
                "requested_url": url,
                "final_url": final_url,
                "content_type": content_type,
                "local_file": source["local_file"],
                "retrieved_at_utc": retrieved_at,
                "sha256": digest,
                "bytes": len(data)
            }

            print("WEB ->", dest)
            print("Content-Type:", content_type)
            print("Bytes:", len(data))
            print("SHA256:", digest)

        # Write provenance record
        record_path = RECORD_DIR / f"{sid}.json"

        record_path.write_text(
            json.dumps(
                record,
                indent=2,
                ensure_ascii=False
            )
            + "\n",
            encoding="utf-8"
        )

    except Exception as exc:

        source["acquisition_status"] = "failed"
        source["acquisition_error"] = str(exc)
        source["retrieved_at_utc"] = retrieved_at

        print("FAILED:", exc)


# Save updated registry
with REGISTRY.open("w", encoding="utf-8") as f:
    json.dump(
        registry,
        f,
        indent=2,
        ensure_ascii=False
    )
    f.write("\n")


# Summary
success = [
    s for s in registry["sources"]
    if s.get("acquisition_status") == "success"
]

failed = [
    s for s in registry["sources"]
    if s.get("acquisition_status") == "failed"
]

print()
print("=" * 70)
print("DOWNLOAD SUMMARY")
print("=" * 70)

print("SUCCESS:", len(success))
print("FAILED :", len(failed))

if failed:
    print()
    print("FAILED SOURCES:")

    for s in failed:
        print(
            "-",
            s["source_id"],
            ":",
            s.get("acquisition_error")
        )

print()
print("Corpus directory:")
print(CORPUS_DIR)

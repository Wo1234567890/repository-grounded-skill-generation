from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
A2S = ROOT / "anything2skill"
SB = ROOT / "skillsbench"

tasks = [
    x.strip()
    for x in (A2S / "task_list.txt").read_text().splitlines()
    if x.strip()
]

# Files we allow for identifying technologies / versions.
SAFE_NAMES = {
    "package.json",
    "pom.xml",
    "build.sbt",
    "pyproject.toml",
    "requirements.txt",
    "requirements-dev.txt",
    "environment.yml",
    "config.json",
}

# Never use these task-package areas.
FORBIDDEN_DIRS = {
    "oracle",
    "verifier",
    "skills",
    "dev",
}

result = {}

for task in tasks:
    task_dir = SB / "tasks" / task
    records = []

    for path in task_dir.rglob("*"):
        if not path.is_file():
            continue

        rel = path.relative_to(task_dir)

        # Exclude benchmark-internal / solution-related directories.
        if any(part in FORBIDDEN_DIRS for part in rel.parts):
            continue

        if path.name not in SAFE_NAMES:
            continue

        try:
            text = path.read_text(
                encoding="utf-8",
                errors="replace"
            )
        except Exception:
            continue

        records.append({
            "path": str(rel),
            "content": text[:20000]
        })

    result[task] = records

out = A2S / "configs" / "source_signals.json"

out.write_text(
    json.dumps(result, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

for task, records in result.items():
    print(f"\n===== {task} =====")

    if not records:
        print("No safe manifest/version signal found.")

    for r in records:
        print(" ", r["path"])

print("\nSaved to:", out)

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]

SKILLSBENCH = ROOT / "skillsbench"
A2S = ROOT / "anything2skill"

TASK_LIST = A2S / "task_list.txt"
OUTPUT = A2S / "configs" / "task_inventory.json"

tasks = [
    line.strip()
    for line in TASK_LIST.read_text(encoding="utf-8").splitlines()
    if line.strip()
]

inventory = {}

for task_name in tasks:
    task_dir = SKILLSBENCH / "tasks" / task_name

    if not task_dir.exists():
        print(f"[MISSING] {task_name}")
        continue

    task_md = task_dir / "task.md"

    if task_md.exists():
        task_description = task_md.read_text(
            encoding="utf-8",
            errors="replace"
        )
    else:
        task_description = None

    allowed_files = []
    excluded_files = []

    for path in task_dir.rglob("*"):
        if not path.is_file():
            continue

        rel = path.relative_to(task_dir)
        parts = rel.parts

        # Do NOT expose evaluation/solution information
        forbidden = (
            "oracle" in parts
            or "verifier" in parts
            or (
                len(parts) >= 2
                and parts[0] == "environment"
                and parts[1] == "skills"
            )
        )

        if forbidden:
            excluded_files.append(str(rel))
        else:
            allowed_files.append(str(rel))

    inventory[task_name] = {
        "task_path": str(task_dir),
        "task_description": task_description,
        "allowed_files": sorted(allowed_files),
        "excluded_files": sorted(excluded_files),
    }

    print(
        f"[OK] {task_name}: "
        f"{len(allowed_files)} allowed, "
        f"{len(excluded_files)} excluded"
    )

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

OUTPUT.write_text(
    json.dumps(inventory, indent=2, ensure_ascii=False),
    encoding="utf-8",
)

print()
print(f"Processed {len(inventory)} tasks.")
print(f"Saved to: {OUTPUT}")

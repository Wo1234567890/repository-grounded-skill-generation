from pathlib import Path
import csv
import json
import shutil

from autoskill import AutoSkill

HOME = Path.home()
ROOT = HOME / "Desktop/skill-generation"

STORE = ROOT / "anything2skill/formal_store_swe"
TASK_ROOT = ROOT / "skillsbench/tasks"
CANDIDATE_ROOT = ROOT / "anything2skill/task_skills_swe"
OUTPUT_ROOT = ROOT / "anything2skill/selected_task_skills_swe"

TASKS = [
    "tictoc-unnecessary-abort-detection",
    "debug-trl-grpo",
    "fix-visual-stability",
    "flink-query",
    "react-performance-debugging",
    "simpo-code-reproduction",
    "spring-boot-jakarta-migration",
    "data-to-d3",
    "llm-prefix-cache-replay",
    "fix-build-agentops",
    "fix-build-google-auto",
    "python-scala-translation",
    "parallel-tfidf-search",
    "azure-bgp-oscillation-route-leak",
]

TOP_K = 1
MIN_SCORE = 0.4
DIAGNOSTIC_K = 5

# ------------------------------------------------------------
# Load AutoSkill exactly once
# ------------------------------------------------------------

sdk = AutoSkill.from_config({
    "llm": {
        "provider": "mock",
    },
    "embeddings": {
        "provider": "hashing",
        "dims": 256,
    },
    "store": {
        "provider": "local",
        "path": str(STORE),
    },
    "bm25_weight": 0.1,
})

visible = sdk.list(user_id="docskill")

print("=" * 100)
print("ANYTHING2SKILL TASK-LEVEL RETRIEVAL")
print("=" * 100)
print("Store skills:", len(visible))
print("top_k:", TOP_K)
print("min_score:", MIN_SCORE)
print()

if len(visible) != 392:
    print(f"WARNING: expected 392 store skills, found {len(visible)}")

# Clean only our retrieval output
if OUTPUT_ROOT.exists():
    shutil.rmtree(OUTPUT_ROOT)

OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

summary = []

# ------------------------------------------------------------
# Retrieve for every task
# ------------------------------------------------------------

for task in TASKS:

    task_file = TASK_ROOT / task / "task.md"
    manifest_file = CANDIDATE_ROOT / task / "manifest.tsv"
    task_output = OUTPUT_ROOT / task

    task_output.mkdir(parents=True, exist_ok=True)

    if not task_file.exists():
        raise FileNotFoundError(f"Missing task file: {task_file}")

    if not manifest_file.exists():
        raise FileNotFoundError(f"Missing manifest: {manifest_file}")

    query = task_file.read_text(encoding="utf-8").strip()

    candidate_ids = []
    manifest = {}

    with manifest_file.open(encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")

        for row in reader:
            sid = (row.get("skill_id") or "").strip()

            if not sid:
                continue

            candidate_ids.append(sid)
            manifest[sid] = row

    if not candidate_ids:
        raise RuntimeError(f"No candidate skills for task: {task}")

    # Retrieve top 5 only for diagnostics.
    # Final selection below still uses only top-1.
    hits = sdk.search(
        query,
        user_id="docskill",
        limit=DIAGNOSTIC_K,
        filters={
            "scope": "user",
            "ids": candidate_ids,
        },
    )

    hit_records = []

    for rank, hit in enumerate(hits, 1):
        sid = str(hit.skill.id)
        row = manifest.get(sid, {})

        hit_records.append({
            "rank": rank,
            "score": float(hit.score),
            "skill_id": sid,
            "name": str(hit.skill.name),
            "candidate_path": row.get("path"),
            "sources": row.get("sources"),
        })

    selected = None

    if hits:
        top = hits[0]

        if float(top.score) >= MIN_SCORE:
            selected = top

    result = {
        "task": task,
        "task_file": str(task_file),
        "candidate_count": len(candidate_ids),
        "query_chars": len(query),
        "retrieval": {
            "method": "AutoSkill hybrid retrieval",
            "embeddings_provider": "hashing",
            "embedding_dims": 256,
            "bm25_weight": 0.1,
            "top_k": TOP_K,
            "min_score": MIN_SCORE,
            "diagnostic_k": DIAGNOSTIC_K,
        },
        "hits": hit_records,
        "selected": None,
    }

    if selected is not None:

        sid = str(selected.skill.id)
        row = manifest[sid]

        relative_path = row["path"]
        source_skill = ROOT / "anything2skill" / relative_path

        if not source_skill.exists():
            raise FileNotFoundError(
                f"Selected SKILL.md not found: {source_skill}"
            )

        selected_dir = task_output / "selected_skill"
        selected_dir.mkdir(parents=True, exist_ok=True)

        shutil.copy2(
            source_skill,
            selected_dir / "SKILL.md",
        )

        result["selected"] = {
            "skill_id": sid,
            "name": str(selected.skill.name),
            "score": float(selected.score),
            "sources": row.get("sources"),
            "original_path": relative_path,
            "output_path": str(
                (selected_dir / "SKILL.md").relative_to(ROOT)
            ),
        }

        status = "SELECTED"
        selected_name = str(selected.skill.name)
        selected_score = float(selected.score)

    else:

        status = "NO_SKILL"
        selected_name = "-"
        selected_score = (
            float(hits[0].score)
            if hits
            else 0.0
        )

    # Save query for reproducibility
    (task_output / "query.md").write_text(
        query + "\n",
        encoding="utf-8",
    )

    # Save retrieval details
    (task_output / "retrieval.json").write_text(
        json.dumps(
            result,
            indent=2,
            ensure_ascii=False,
        ) + "\n",
        encoding="utf-8",
    )

    summary.append({
        "task": task,
        "candidates": len(candidate_ids),
        "status": status,
        "score": selected_score,
        "skill": selected_name,
    })

# ------------------------------------------------------------
# Save + print summary
# ------------------------------------------------------------

summary_file = OUTPUT_ROOT / "summary.tsv"

with summary_file.open("w", encoding="utf-8") as f:
    f.write("task\tcandidates\tstatus\tscore\tskill\n")

    for x in summary:
        f.write(
            f'{x["task"]}\t'
            f'{x["candidates"]}\t'
            f'{x["status"]}\t'
            f'{x["score"]:.4f}\t'
            f'{x["skill"]}\n'
        )

print(
    f'{"TASK":40s} '
    f'{"N":>4s} '
    f'{"STATUS":10s} '
    f'{"SCORE":>7s}  '
    f'SKILL'
)

print("-" * 100)

for x in summary:
    print(
        f'{x["task"]:40s} '
        f'{x["candidates"]:4d} '
        f'{x["status"]:10s} '
        f'{x["score"]:7.4f}  '
        f'{x["skill"]}'
    )

print("-" * 100)

selected_count = sum(
    1 for x in summary
    if x["status"] == "SELECTED"
)

print("Tasks:", len(summary))
print("Selected:", selected_count)
print("No skill:", len(summary) - selected_count)
print("Output:", OUTPUT_ROOT)
print("=" * 100)

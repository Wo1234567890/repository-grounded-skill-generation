from pathlib import Path
from collections import defaultdict
import json
import re
import shutil

ROOT = Path.home() / "Desktop/skill-generation/anything2skill"
STORE = ROOT / "formal_store_swe"
REGISTRY = STORE / ".runtime/document_registry"
SKILL_ROOT = STORE / "Users/docskill"

OUTPUT = ROOT / "task_skills_swe"

TASK_SOURCES = {
    "tictoc-unnecessary-abort-detection": [
        "tictoc-paper.txt",
    ],
    "debug-trl-grpo": [
        "trl-grpo-017.md",
    ],
    "fix-visual-stability": [
        "cls-guidance.md",
        "nextjs14-optimization.md",
    ],
    "flink-query": [
        "flink-118-datastream.md",
    ],
    "react-performance-debugging": [
        "nextjs14-optimization.md",
    ],
    "simpo-code-reproduction": [
        "simpo-paper.txt",
        "simpo-repository-docs.md",
    ],
    "spring-boot-jakarta-migration": [
        "spring-boot3-migration.md",
    ],
    "data-to-d3": [
        "d3-docs.md",
    ],
    "llm-prefix-cache-replay": [
        "s3fifo-paper.txt",
        "mooncake-docs.md",
    ],
    "fix-build-agentops": [
        "agentops-docs.txt",
    ],
    "fix-build-google-auto": [
        "google-auto-docs.md",
        "maven-docs.md",
    ],
    "python-scala-translation": [
        "scala-213-docs.md",
        "circe-014-docs.md",
    ],
    "parallel-tfidf-search": [
        "tfidf-reference.txt",
        "python312-parallelism.md",
    ],
    "azure-bgp-oscillation-route-leak": [
        "azure-virtual-wan-docs.md",
        "rfc7908.txt",
    ],
}

# ------------------------------------------------------------------
# 1. Load document registry
# ------------------------------------------------------------------

doc_id_to_title = {}
title_to_doc_id = {}

for f in (REGISTRY / "documents").glob("*.json"):
    d = json.loads(f.read_text(encoding="utf-8"))

    doc_id = d.get("doc_id") or d.get("id")
    if not doc_id:
        continue

    title = (
        d.get("title")
        or Path(d.get("source_file", "")).name
        or doc_id
    )

    doc_id_to_title[doc_id] = title
    title_to_doc_id[title] = doc_id


# ------------------------------------------------------------------
# 2. Build provenance:
#       skill_id -> set(document ids)
# ------------------------------------------------------------------

skill_to_docs = defaultdict(set)

for f in (REGISTRY / "provenance_links").glob("*.json"):
    d = json.loads(f.read_text(encoding="utf-8"))

    if d.get("entity_type") != "skill":
        continue

    skill_id = d.get("entity_id")
    if not skill_id:
        continue

    for doc_id in d.get("doc_ids", []):
        skill_to_docs[skill_id].add(doc_id)


# ------------------------------------------------------------------
# 3. Index final SKILL.md files by their internal skill id
# ------------------------------------------------------------------

skill_files = {}

id_pattern = re.compile(r'^id:\s*["\']?([^"\']+)["\']?\s*$')

for f in SKILL_ROOT.glob("*/SKILL.md"):
    skill_id = None

    try:
        for line in f.read_text(encoding="utf-8").splitlines()[:30]:
            m = id_pattern.match(line.strip())
            if m:
                skill_id = m.group(1).strip()
                break
    except Exception:
        pass

    if skill_id:
        skill_files[skill_id] = f


# ------------------------------------------------------------------
# 4. Rebuild output directory
# ------------------------------------------------------------------

if OUTPUT.exists():
    shutil.rmtree(OUTPUT)

OUTPUT.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------------
# 5. Construct task-specific skill sets
# ------------------------------------------------------------------

summary = []

for task, source_names in TASK_SOURCES.items():

    task_dir = OUTPUT / task
    skills_dir = task_dir / "skills"

    task_dir.mkdir(parents=True, exist_ok=True)
    skills_dir.mkdir(parents=True, exist_ok=True)

    wanted_doc_ids = set()
    missing_sources = []

    for source in source_names:
        doc_id = title_to_doc_id.get(source)

        if doc_id:
            wanted_doc_ids.add(doc_id)
        else:
            missing_sources.append(source)

    selected = []

    for skill_id, doc_ids in skill_to_docs.items():

        matched_docs = doc_ids & wanted_doc_ids

        if not matched_docs:
            continue

        src = skill_files.get(skill_id)

        if src is None:
            continue

        selected.append(
            (
                skill_id,
                src,
                sorted(doc_id_to_title[d] for d in matched_docs),
            )
        )

    selected.sort(key=lambda x: x[1].parent.name)

    manifest_lines = [
        "skill_id\tskill_name\tsources\tpath"
    ]

    for skill_id, src, matched_sources in selected:

        skill_name = src.parent.name

        dest_dir = skills_dir / skill_name
        dest_dir.mkdir(parents=True, exist_ok=True)

        dest = dest_dir / "SKILL.md"
        shutil.copy2(src, dest)

        manifest_lines.append(
            f"{skill_id}\t{skill_name}\t"
            f"{','.join(matched_sources)}\t"
            f"{dest.relative_to(ROOT)}"
        )

    (task_dir / "manifest.tsv").write_text(
        "\n".join(manifest_lines) + "\n",
        encoding="utf-8",
    )

    (task_dir / "sources.txt").write_text(
        "\n".join(source_names) + "\n",
        encoding="utf-8",
    )

    summary.append(
        (
            task,
            len(selected),
            ", ".join(source_names),
            ", ".join(missing_sources) if missing_sources else "-"
        )
    )


# ------------------------------------------------------------------
# 6. Print summary
# ------------------------------------------------------------------

print("=" * 100)
print("ANYTHING2SKILL TASK-SPECIFIC SKILL SETS")
print("=" * 100)

for task, n, sources, missing in summary:
    print(f"{n:3d}  {task}")
    print(f"     sources: {sources}")

    if missing != "-":
        print(f"     MISSING SOURCE: {missing}")

print("-" * 100)

print("TASKS:", len(summary))
print(
    "TOTAL TASK-SKILL ASSIGNMENTS:",
    sum(x[1] for x in summary)
)
print("OUTPUT:", OUTPUT)
print("=" * 100)

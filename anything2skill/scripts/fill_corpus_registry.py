#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
A2S = ROOT / "anything2skill"
REGISTRY = A2S / "configs" / "corpus_registry.json"

URLS = {
    "tictoc-paper": "https://db.cs.cmu.edu/papers/2016/yu-sigmod2016.pdf",
    "trl-grpo-017": "https://huggingface.co/docs/trl/v0.17.0/grpo_trainer",
    "nextjs14-optimization": "https://nextjs.org/docs/14/app/building-your-application/optimizing",
    "cls-guidance": "https://web.dev/articles/optimize-cls",
    "flink-118-datastream": "https://nightlies.apache.org/flink/flink-docs-release-1.18/docs/dev/datastream/overview/",
    "simpo-paper": "https://arxiv.org/pdf/2405.14734",
    "simpo-repository-docs": "https://github.com/princeton-nlp/SimPO",
    "spring-boot3-migration": "https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-3.0-Migration-Guide",
    "d3-docs": "https://d3js.org/api",
    "s3fifo-paper": "https://jasony.me/publication/sosp23-s3fifo.pdf",
    "mooncake-docs": "https://raw.githubusercontent.com/kvcache-ai/Mooncake/main/docs/source/index.md",
    "agentops-docs": "https://raw.githubusercontent.com/AgentOps-AI/agentops/main/llms.txt",
    "google-auto-docs": "https://raw.githubusercontent.com/google/auto/main/README.md",
    "maven-docs": "https://maven.apache.org/guides/index.html",
    "scala-213-docs": "https://www.scala-lang.org/api/2.13.12/",
    "circe-014-docs": "https://circe.github.io/circe/",
    "python312-parallelism": "https://docs.python.org/3.12/library/concurrent.futures.html",
    "tfidf-reference": "https://courses.cs.umbc.edu/graduate/676/umbconly/SaltonBuckleyIPM88.PDF",
    "azure-virtual-wan-docs": "https://learn.microsoft.com/en-us/azure/virtual-wan/about-virtual-hub-routing",
    "rfc7908": "https://www.rfc-editor.org/rfc/rfc7908.txt",
}

# Exact task-supplied primary sources we prefer over re-downloading current copies.
LOCAL_SOURCES = {
    "simpo-paper": "skillsbench/tasks/simpo-code-reproduction/environment/SimPO/paper.pdf",
    "simpo-repository-docs": "skillsbench/tasks/simpo-code-reproduction/environment/SimPO/README.md",
}

with REGISTRY.open("r", encoding="utf-8") as f:
    data = json.load(f)

source_ids = {s["source_id"] for s in data["sources"]}

missing = sorted(source_ids - set(URLS))
extra = sorted(set(URLS) - source_ids)

if missing:
    raise SystemExit(f"ERROR: URLs missing for source IDs: {missing}")
if extra:
    raise SystemExit(f"ERROR: URL mapping has unknown source IDs: {extra}")

for source in data["sources"]:
    sid = source["source_id"]
    source["url"] = URLS[sid]

    if sid in LOCAL_SOURCES:
        source["preferred_local_source"] = LOCAL_SOURCES[sid]
    else:
        source.pop("preferred_local_source", None)

    # These fields will be filled only after acquisition.
    source["local_file"] = None
    source["retrieved_at_utc"] = None
    source["sha256"] = None
    source["acquisition_status"] = "pending"

with REGISTRY.open("w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"Updated: {REGISTRY}")
print(f"Sources with canonical URLs: {len(data['sources'])}")

for s in data["sources"]:
    local = s.get("preferred_local_source")
    if local:
        print(f"[LOCAL-PREFERRED] {s['source_id']}: {local}")
    else:
        print(f"[WEB]             {s['source_id']}")

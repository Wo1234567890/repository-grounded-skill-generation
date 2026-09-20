#!/bin/bash

TASKS=(
  "tictoc-unnecessary-abort-detection"
  "debug-trl-grpo"
  "fix-visual-stability"
  "flink-query"
  "react-performance-debugging"
  "simpo-code-reproduction"
  "spring-boot-jakarta-migration"
  "data-to-d3"
  "llm-prefix-cache-replay"
  "fix-build-agentops"
  "fix-build-google-auto"
  "python-scala-translation"
  "parallel-tfidf-search"
  "azure-bgp-oscillation-route-leak"
)

for RUN in 2 3 4; do
  for TASK in "${TASKS[@]}"; do
    echo
    echo "============================================================"
    echo "START: $TASK | run$RUN"
    echo "============================================================"

    bench eval run \
      --tasks-dir "tasks/$TASK" \
      --agent claude-agent-acp \
      --model claude-haiku-4-5-20251001 \
      --skill-mode no-skill \
      --sandbox docker \
      --concurrency 1 \
      --jobs-dir "jobs/${TASK}_skillx_noskill_run${RUN}"

    STATUS=$?

    echo
    echo "FINISH: $TASK | run$RUN | exit=$STATUS"
    echo "============================================================"
  done
done

echo
echo "ALL RUN2/RUN3/RUN4 JOBS FINISHED"

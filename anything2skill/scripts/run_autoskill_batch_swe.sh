#!/usr/bin/env bash

set -u

ROOT="$HOME/Desktop/skill-generation"

AUTOSKILL="$ROOT/anything2skill/upstream/AutoSkill"
CORPUS="$ROOT/anything2skill/corpus_normalized"

STORE="$ROOT/anything2skill/formal_store_swe"
LOGDIR="$ROOT/anything2skill/logs/formal_swe"
STATE="$ROOT/anything2skill/run_state_swe"

mkdir -p "$STORE" "$LOGDIR" "$STATE"

cd "$AUTOSKILL" || exit 1

FILES=(
  "circe-014-docs.md"
  "google-auto-docs.md"
  "nextjs14-optimization.md"
  "scala-213-docs.md"
  "maven-docs.md"
  "mooncake-docs.md"
  "azure-virtual-wan-docs.md"
  "rfc7908.txt"
  "trl-grpo-017.md"
  "python312-parallelism.md"
  "flink-118-datastream.md"
  "simpo-repository-docs.md"
  "simpo-paper.txt"
  "s3fifo-paper.txt"
  "spring-boot3-migration.md"
  "tictoc-paper.txt"
  "tfidf-reference.txt"
  "cls-guidance.md"
  "d3-docs.md"
  "agentops-docs.txt"
)

TOTAL=${#FILES[@]}
INDEX=0

for FILE in "${FILES[@]}"; do
  INDEX=$((INDEX + 1))

  SRC="$CORPUS/$FILE"
  DONE="$STATE/$FILE.done"
  LOG="$LOGDIR/$FILE.log"

  echo
  echo "======================================================================"
  echo "[$INDEX/$TOTAL] $FILE"
  echo "======================================================================"

  if [[ -f "$DONE" ]]; then
    echo "SKIP: already completed"
    continue
  fi

  if [[ ! -f "$SRC" ]]; then
    echo "ERROR: missing source: $SRC"
    continue
  fi

  START=$(date +%s)

  python3 -m AutoSkill4Doc build \
    --file "$SRC" \
    --store-path "$STORE" \
    --llm-provider anthropic \
    --llm-model claude-haiku-4-5-20251001 \
    --embeddings-provider hashing \
    --extract-strategy strict \
    --section-outline-mode llm \
    --extract-workers 1 \
    2>&1 | tee "$LOG"

  STATUS=${PIPESTATUS[0]}

  END=$(date +%s)
  ELAPSED=$((END - START))

  if [[ $STATUS -eq 0 ]]; then
    {
      echo "completed_at=$(date)"
      echo "elapsed_seconds=$ELAPSED"
      echo "autoskill_commit=$(git rev-parse HEAD)"
    } > "$DONE"

    echo
    echo "SUCCESS: $FILE (${ELAPSED}s)"
  else
    echo
    echo "FAILED: $FILE (exit=$STATUS)"
    echo "LOG: $LOG"
  fi
done

echo
echo "======================================================================"
echo "BATCH FINISHED"
echo "======================================================================"

echo "Completed sources:"
find "$STATE" -name '*.done' -type f | wc -l

echo "Final store:"
echo "$STORE"

echo "AutoSkill commit:"
git rev-parse HEAD

# Trajectory-Generated Skills

This package contains one `SKILL.md` for each of the 14 selected SkillsBench tasks.

Generation basis: only the supplied task specifications, no-skill trajectories, and their run-result metadata were used. No verifier code, gold solution, human skill, or Anything2Skill external corpus was used.

Interpretation rule: successful trajectories were treated as positive procedural evidence; partial/failed trajectories were used mainly to identify pitfalls and to avoid presenting their final claims as verified solutions. The Python-to-Scala task had no executable agent trajectory because all runs failed during environment startup, so its skill is deliberately conservative and task-spec-driven.

## Run evidence

| Task | Trajectories | Rewards / errors |
|---|---:|---|
| `azure-bgp-oscillation-route-leak` | 3 | 0.0, 0.0, 0.0 |
| `data-to-d3` | 4 | 0.0, 0.0, 0.0, 0.0 |
| `debug-trl-grpo` | 4 | 0.25, 0.25, 0.25, 0.25 |
| `fix-build-agentops` | 4 | 0.0, 0.0, 0.0, 0.0 |
| `fix-build-google-auto` | 4 | 0.0, 0.0, 0.0, 0.0 |
| `fix-visual-stability` | 4 | 0.0, 0.0, 0.0, 0.0 |
| `flink-query` | 4 | error:other, 0.0, 0.0, 0.0 |
| `llm-prefix-cache-replay` | 4 | 0.0, 0.0, 0.0, 0.0 |
| `parallel-tfidf-search` | 4 | 0.0, 1.0, 0.0, 0.0 |
| `python-scala-translation` | 4 | error:other, error:other, error:other, error:other |
| `react-performance-debugging` | 5 | 0.0, 0.0, 0.0, error:pipe_closed, 0.0 |
| `simpo-code-reproduction` | 3 | 0.0, 0.0, 0.0 |
| `spring-boot-jakarta-migration` | 4 | 1.0, 1.0, 1.0, 1.0 |
| `tictoc-unnecessary-abort-detection` | 4 | 0.05, 0.45, 0.45, 0.05 |

## Layout

Each task directory contains exactly one `SKILL.md`. `generation_manifest.json` records the trajectory counts and run outcomes used as provenance.

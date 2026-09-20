---
name: flink-event-time-stage-analysis
description: Implement Flink jobs that sessionize task events by event-time inactivity, correlate job lifecycle events, and emit per-job aggregate results without changing protected build configuration.
---

# Flink Event-Time Stage Analysis

## When to Use

Use this skill when a Flink job must infer per-job stages or sessions from timestamped task events and combine them with job lifecycle information.

## Workflow

1. **Read the provided schema before coding.** Inspect the dataset documentation and a small sample of the compressed CSV files. Confirm which numeric event type represents task submission and which job events indicate completion.
2. **Implement the repository's expected data types.** If a shared base class expects `TaskEvent` and `JobEvent`, match its parsing and field conventions rather than bypassing it with an unrelated model.
3. **Use event time for stage boundaries.** For each job, consider only task SUBMIT events, sort/process them by event timestamp, and split stages when the inactivity gap reaches the task-defined threshold. Re-submission after failure or eviction is a new submit event and should be counted again.
4. **Track the longest stage incrementally.** For each job, maintain the current stage count and the maximum seen so far. Closing a stage updates the maximum; job completion must also flush the currently open stage.
5. **Emit after the job lifecycle says the job is finished.** Correlate task-derived state with job events so output reflects a completed job rather than an arbitrary intermediate window.
6. **Honor the output contract exactly.** Emit one tuple per job in the requested textual form and write to the caller-provided local output path. Do not rely on ordering unless required.
7. **Do not change protected build files to make testing easier.** One no-skill run drifted into adding temporary test dependencies and alternative execution setups. Prefer compiling the existing project and validating within its intended Flink environment.

## Validation

Create a tiny hand-checkable sequence for one job containing clustered SUBMIT events, a gap longer than the inactivity threshold, a resubmission, and a completion event. Confirm stage counts and final maximum before running on the full trace.

## Common Failure Modes

- Using processing time instead of the dataset's event timestamps.
- Counting all task events rather than SUBMIT events.
- Treating a resubmitted task as a duplicate to remove.
- Forgetting to flush the last open stage when the job finishes.
- Focusing on JAR launch mechanics while leaving stage semantics unverified.

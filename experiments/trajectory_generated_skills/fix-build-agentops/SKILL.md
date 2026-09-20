---
name: python-ci-build-repair
description: Repair Python CI/build regressions by reproducing the exact failure, checking project-version compatibility and dependencies before source edits, and delivering minimal reproducible patches.
---

# Python CI Build Repair

## When to Use

Use this skill for historical or CI-specific Python build failures where the repository, interpreter version, dependency set, and test/type-check tooling may differ from the current local environment.

## Workflow

1. **Identify the real repository and build command.** Inspect `pyproject.toml`, `tox.ini`, CI configuration, and project metadata before editing source.
2. **Reproduce the failing stage as closely as possible.** A syntax-only compile is not a substitute for the actual build/test/type-check command.
3. **Check version compatibility early.** Compare `requires-python` with syntax used in the diff. For example, PEP 604 `X | Y` type unions require a newer interpreter than code intended to support older Python releases; use compatibility-safe typing forms when the package promises older versions.
4. **Distinguish environment absence from repository defect.** If importing fails because a declared dependency such as `requests` is not installed, install/use the project environment before concluding the source is broken.
5. **Trace failures from the first actionable error.** Inspect imports, type annotations, packaging metadata, and dependency versions before making cosmetic fixes.
6. **Write the analysis before the patch.** Record the observed failure, evidence, root cause, and minimal repair plan in the requested analysis file.
7. **Generate standard diff patches, then apply them.** Keep each patch focused and ensure the patch file matches the actual final edit.
8. **Re-run the original build gate.** Validate on the same interpreter/toolchain target, not only with `py_compile`.

## Trajectory-Derived Caution

No-skill runs found plausible source issues such as a misspelled exported function and newer type-hint syntax in a project declaring older-Python support, yet all runs received zero reward. This shows why a visible code defect is not automatically the build root cause. Reproduce the full build and investigate dependency/interpreter compatibility before stopping.

## Common Failure Modes

- Fixing a typo and declaring the build repaired without reproducing CI.
- Ignoring the package's declared Python-version range.
- Treating a missing installed dependency as proof of a source-code bug.
- Creating diff files that no longer match the final repository state.

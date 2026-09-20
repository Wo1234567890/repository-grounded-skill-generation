---
name: python-to-scala-translation
description: Translate Python data-processing code into idiomatic Scala 2.13 while preserving public behavior, data models, error semantics, and batch APIs.
---

# Python-to-Scala Translation

## When to Use

Use this skill when a Python module must be reimplemented in Scala 2.13 for distributed/data-processing contexts while preserving its externally visible classes, functions, and behavior.

## Translation Workflow

1. **Inventory the Python API before coding.** List every required class, enum-like type, builder, conversion helper, single-item function, and batch function. Preserve the complete public surface.
2. **Extract behavior, not syntax.** For each Python function, write down inputs, outputs, defaults, mutation, exception behavior, null/absence handling, and ordering guarantees.
3. **Choose idiomatic Scala representations.** Use case classes for immutable data records where appropriate, sealed traits/enumerations for closed token categories, `Option` for ordinary absence, and Scala collections instead of mechanically reproducing Python container idioms.
4. **Keep parsing/tokenization rules behaviorally equivalent.** Port edge cases first: empty input, whitespace, numeric formats, temporal strings, metadata attachment, and fallback/universal tokenization.
5. **Design builders in Scala style without changing semantics.** Fluent methods can return a new or updated builder as appropriate, but the constructed tokenizer must match Python behavior.
6. **Keep batch operations deterministic.** `tokenizeBatch` should preserve input ordering and use the same tokenizer selection/conversion rules as the single-item path.
7. **Compile early under Scala 2.13.** Fix type inference, Java/Scala collection boundaries, regex/date APIs, and overload ambiguities as they appear.
8. **Differential-test against Python.** Feed the same representative inputs to both implementations and compare serialized tokens/metadata, not only whether Scala compiles.

## Environment Caution

The available no-skill runs never reached the agent: the Docker build downloaded an x86_64 Coursier binary inside an ARM64 environment and failed before Scala setup. Therefore there is no valid trajectory-derived implementation behavior for this task. Use the task specification conservatively and ensure the toolchain architecture matches the container before evaluating the translation.

## Common Failure Modes

- Word-for-word translation that keeps Python control-flow/data idioms.
- Omitting rarely used public methods because the main path compiles.
- Using `null` broadly instead of explicit absence handling.
- Verifying only compilation rather than behavioral equivalence.

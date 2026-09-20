---
name: maven-multimodule-build-repair
description: Diagnose and repair Maven multi-module build failures involving parent versions, transitive system dependencies, JDK compatibility, and missing annotation APIs with minimal configuration changes.
---

# Maven Multi-Module Build Repair

## When to Use

Use this skill when an older Java/Maven repository fails under a different JDK or CI environment and the failure may be in POM structure or dependency resolution rather than application source.

## Workflow

1. **Run the actual Maven build and preserve the first failure.** Do not start by guessing from source files.
2. **Map the reactor.** Check the root POM, `<modules>`, child `<parent>` coordinates, and inherited versions. Parent-version mismatches can break the build before compilation reaches project code.
3. **Inspect dependency trees for JDK-coupled artifacts.** Older testing/compiler libraries may pull system-scoped `tools.jar` or other artifacts that disappeared after JDK 8. Identify the exact dependency chain before changing versions.
4. **Prefer a targeted compatibility repair.** If a transitive system dependency is obsolete, use the narrowest supported exclusion/replacement that preserves the repository's intended library behavior. Avoid trial-upgrading many versions without evidence.
5. **Handle removed Java EE/JDK annotations explicitly.** When code generation or tests require annotations no longer bundled with the JDK, add the appropriate API dependency at the module(s) that compile that code.
6. **Keep parent/module versions coherent.** Update only the inconsistent coordinates necessary for the reactor to resolve.
7. **Build after each root-cause class.** Dependency-resolution errors, compilation errors, and test errors should be handled sequentially so later failures are not confused with the first one.
8. **Create and apply standard diff patches, then run a clean build again.** The final validation should start from a clean Maven state.

## Trajectory-Derived Caution

A no-skill run eventually reached `BUILD SUCCESS` after changing parent versions, excluding an obsolete `tools.jar` dependency, and adding an annotation API, but the external reward was still zero. Treat local build success as necessary but not sufficient: verify that the chosen changes are minimal, match the intended historical environment, and satisfy the benchmark's exact build command.

## Common Failure Modes

- Guessing dependency versions repeatedly instead of reading the dependency chain.
- Changing source code when Maven cannot resolve the reactor.
- Assuming skipping tests avoids compile-time dependency resolution.
- Applying the same dependency addition to every module without checking which module needs it.

---
id: "7f24b360-0174-5d5c-873a-64fdd478002c"
name: "Modular Dependency Selection for JSON Library"
description: "Select and configure circe subprojects based on parsing, codec derivation, and optics requirements, minimizing core dependencies while allowing alternative implementations."
version: "0.1.0"
tags:
  - "library_setup"
  - "dependency_management"
  - "modular_architecture"
  - "scala"
  - "json"
triggers:
  - "Integrating circe into a Scala project with specific dependency or feature constraints"
  - "Evaluating trade-offs between core simplicity and optional functionality"
  - "Assessing whether to adopt circe subprojects or provide alternative implementations"
---

# Modular Dependency Selection for JSON Library

Select and configure circe subprojects based on parsing, codec derivation, and optics requirements, minimizing core dependencies while allowing alternative implementations.

## Prompt

Evaluate your Scala project's functional needs (JSON parsing, automatic codec generation, lens-based transformations) and dependency constraints. For each capability, decide whether to include the corresponding circe subproject (core, jawn, generic, optics) or provide an alternative implementation. Document your selections and rationale.

## Objective

Select appropriate circe subproject modules to match functional and dependency constraints
## Applicable Signals

- Project has strict dependency footprint requirements
- Need for JSON parsing support (JVM or Scala.js)
- Automatic codec derivation is required
- Lens-based JSON transformation is needed

## Contraindications

- Monolithic library selection is required
- Alternative JSON libraries are preferred
- Dependency footprint is not a concern
- Project cannot tolerate optional subproject dependencies

## Workflow Steps

- {'step': 1, 'action': 'Assess core requirements', 'detail': 'Determine if basic JSON value representation and manual codec support suffice, or if additional capabilities are needed.'}
- {'step': 2, 'action': 'Evaluate parsing needs', 'detail': 'Decide between JVM parsing (via jawn subproject) or Scala.js parsing (via scalajs.js.JSON). Omit if parsing is not required.'}
- {'step': 3, 'action': 'Assess codec derivation', 'detail': 'Determine if automatic codec generation via Shapeless (generic subproject) is needed, or if manual codecs are acceptable.'}
- {'step': 4, 'action': 'Evaluate optics support', 'detail': 'Decide if lens-based transformations are required. If yes, include experimental optics subproject; otherwise omit to avoid Monocle/Scalaz dependency.'}
- {'step': 5, 'action': 'Consider alternative implementations', 'detail': "For each subproject, document whether circe's implementation or an alternative library is chosen, and justify the decision."}
- {'step': 6, 'action': 'Document subproject selection', 'detail': 'Record which subprojects are included, which are excluded, and the rationale for each decision based on project constraints.'}

## Constraints

- Core project has only cats-core as a dependency
- Jawn subproject required for JVM parsing; scalajs.js.JSON for JavaScript parsing
- Shapeless required for generic codec derivation
- Monocle has Scalaz dependency; optics subproject is experimental

## Cautions

- Optics subproject is experimental; evaluate stability before production use.
- Shapeless dependency in generic subproject may impact compile times.
- Scala.js parsing uses browser JSON API; behavior may differ from JVM parsing.
- Omitting core subproject is not recommended; it provides essential JSON value types.

## Output Contract

- Documented subproject selection (core, jawn, generic, optics) with explicit rationale for inclusion or exclusion based on project constraints, dependency footprint, and functional requirements.

## Triggers

- Integrating circe into a Scala project with specific dependency or feature constraints
- Evaluating trade-offs between core simplicity and optional functionality
- Assessing whether to adopt circe subprojects or provide alternative implementations

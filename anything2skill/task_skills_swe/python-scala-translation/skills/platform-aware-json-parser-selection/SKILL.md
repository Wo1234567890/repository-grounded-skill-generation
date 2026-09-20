---
id: "d57ca13a-fbfc-51c7-aa16-3e883557a943"
name: "Platform-Aware JSON Parser Selection"
description: "Route JSON parsing to platform-specific implementations based on runtime environment: JVM via io.circe.jawn or JavaScript via scalajs.js.JSON, with fallback to core parser subproject."
version: "0.1.0"
tags:
  - "json"
  - "parsing"
  - "scala"
  - "cross-platform"
  - "routing"
  - "jvm"
triggers:
  - "Parsing JSON in a Scala.js or JVM context; cross-platform code must handle both targets transparently"
---

# Platform-Aware JSON Parser Selection

Route JSON parsing to platform-specific implementations based on runtime environment: JVM via io.circe.jawn or JavaScript via scalajs.js.JSON, with fallback to core parser subproject.

## Prompt

Detect the runtime platform (JVM or JavaScript/Scala.js). Invoke io.circe.jawn for JVM targets; invoke scalajs.js.JSON for JavaScript targets. Fall back to the core parser subproject if platform detection is ambiguous or if subproject-specific implementations are unavailable.

## Objective

Select and invoke the correct parsing implementation based on runtime platform
## Applicable Signals

- Cross-platform Scala codebase (JVM and Scala.js targets)
- JSON parsing required in shared code
- Runtime platform detection available

## Contraindications

- Single-platform deployment (use platform-specific parser directly)
- Custom parsing logic already in place
- Performance is not a constraint and overhead of routing is unacceptable

## Intervention Moves

- Detect platform: JVM or JavaScript
- Route to io.circe.jawn (JVM) or scalajs.js.JSON (JavaScript)
- Invoke selected parser on input JSON
- Return parsed AST or deserialized object

## Workflow Steps

- Detect runtime platform (JVM or JavaScript)
- Select appropriate parser implementation based on platform
- Invoke selected parser with input JSON
- Return parsed result or propagate parser error

## Constraints

- Platform detection mechanism must be reliable and available at runtime
- Both JVM and JavaScript parser implementations must be available in the build
- Input JSON must be valid; malformed JSON should propagate errors from the selected parser

## Cautions

- Platform detection overhead may impact latency in high-throughput scenarios
- Ensure build configuration includes both jawn and scalajs.js.JSON dependencies for cross-platform targets

## Output Contract

- JSON parsed and deserialized into circe AST or target type without platform-specific errors; caller receives a valid circe JSON value or decoded object, or an error from the selected parser.

## Triggers

- Parsing JSON in a Scala.js or JVM context; cross-platform code must handle both targets transparently

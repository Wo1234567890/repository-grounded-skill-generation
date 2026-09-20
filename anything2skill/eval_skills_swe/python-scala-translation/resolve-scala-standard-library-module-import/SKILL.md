---
id: "d4cdadc0-cd0d-58fc-8c37-b36098dd2e4c"
name: "Resolve Scala Standard Library Module Import"
description: "Locate and import optional Scala standard library modules (reflect, xml, collection.parallel, util.parsing, swing) by their canonical package names and corresponding JAR artifacts."
version: "0.1.0"
tags:
  - "scala"
  - "package_management"
  - "import"
  - "dependency"
  - "standard_library"
triggers:
  - "code needs reflection API, XML handling, parallel collections, parser combinators, or Swing GUI bindings"
---

# Resolve Scala Standard Library Module Import

Locate and import optional Scala standard library modules (reflect, xml, collection.parallel, util.parsing, swing) by their canonical package names and corresponding JAR artifacts.

## Prompt

When your code requires functionality from optional Scala libraries, identify the module by its use case, then declare the correct import statement and ensure the corresponding JAR is available in your build classpath.

## Objective

correctly identify and import the required optional Scala library module
## Applicable Signals

- code needs reflection API
- code needs XML handling
- code needs parallel collections
- code needs parser combinators
- code needs Swing GUI bindings

## Contraindications

- the required functionality is already in core scala package or java.lang
- the JAR is not available in the build classpath

## Workflow Steps

- Identify the functional requirement (reflection, XML, parallel collections, parsing, or GUI).
- Map the requirement to the corresponding optional module: scala.reflect, scala.xml, scala.collection.parallel, scala.util.parsing, or scala.swing.
- Declare the import statement using the canonical package name (e.g., `import scala.reflect._`).
- Ensure the corresponding JAR (e.g., scala-reflect.jar, scala-xml.jar) is declared in build configuration.

## Output Contract

- correct import statement and JAR dependency declared in build configuration
- downstream code can reference the imported module without resolution errors

## Triggers

- code needs reflection API, XML handling, parallel collections, parser combinators, or Swing GUI bindings

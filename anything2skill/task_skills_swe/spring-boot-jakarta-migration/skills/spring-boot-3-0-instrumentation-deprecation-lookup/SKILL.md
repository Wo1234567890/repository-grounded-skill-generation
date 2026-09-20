---
id: "f05ceea9-3c01-50d3-97c1-374c9b16251a"
name: "Spring Boot 3.0 Instrumentation Deprecation Lookup"
description: "Reference guide for mapping deprecated Spring Boot 2.x instrumentation classes to their Spring Boot 3.0 Observation-based replacements. Enables developers to quickly identify equivalent classes and understand the functional shift from direct instrumentation to Observation conventions during migration."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "metrics"
  - "observation"
  - "deprecation"
  - "instrumentation"
  - "reference"
triggers:
  - "Identifying which instrumentation classes need replacement"
  - "Planning migration scope for metrics and observation"
  - "Searching for equivalent functionality in Spring Boot 3.0"
examples:
  - input: "Found WebMvcMetricsFilter in codebase"
    output: "Replace with Spring Framework's ServerHttpObservationFilter; update to use ServerRequestObservationConvention for custom behavior"
  - input: "Found MetricsRestTemplateCustomizer in RestTemplateBuilder configuration"
    output: "Replace with ObservationRestTemplateCustomizer; apply to RestTemplateBuilder bean"
  - input: "Have custom TagProvider or TagContributor implementations"
    output: "Extend DefaultServerRequestObservationConvention and override getLowCardinalityKeyValues() to add custom KeyValues"
---

# Spring Boot 3.0 Instrumentation Deprecation Lookup

Reference guide for mapping deprecated Spring Boot 2.x instrumentation classes to their Spring Boot 3.0 Observation-based replacements. Enables developers to quickly identify equivalent classes and understand the functional shift from direct instrumentation to Observation conventions during migration.

## Prompt

Use this reference to identify which deprecated instrumentation classes in your Spring Boot 2.x codebase need replacement in Spring Boot 3.0. Look up the old class name to find its equivalent and understand the functional shift from direct instrumentation to Observation-based conventions.

## Objective

Provide lookup reference for deprecated-to-replacement class mappings during Spring Boot 3.0 migration
## Applicable Signals

- Codebase contains WebMvcMetricsFilter
- Codebase contains MetricsRestTemplateCustomizer
- Codebase contains *TagProvider, *TagContributor, or *Tags classes
- Migration from Spring Boot 2.x to 3.0 is in progress

## Contraindications

- Migration already completed
- No deprecated instrumentation classes present in codebase
- Using Spring Boot 2.x (reference is for 3.0 migration only)

## Constraints

- This is a static reference; does not execute migration logic
- Functional equivalence requires understanding Observation conventions
- Custom TagProvider or TagContributor implementations require extension of DefaultServerRequestObservationConvention

## Output Contract

- Developer can quickly identify the replacement class for each deprecated instrumentation class and understand the functional shift from direct instrumentation to Observation-based conventions.

## Example Executions

### Example 1

- Input: Found WebMvcMetricsFilter in codebase
- Output: Replace with Spring Framework's ServerHttpObservationFilter; update to use ServerRequestObservationConvention for custom behavior

### Example 2

- Input: Found MetricsRestTemplateCustomizer in RestTemplateBuilder configuration
- Output: Replace with ObservationRestTemplateCustomizer; apply to RestTemplateBuilder bean

### Example 3

- Input: Have custom TagProvider or TagContributor implementations
- Output: Extend DefaultServerRequestObservationConvention and override getLowCardinalityKeyValues() to add custom KeyValues

## Triggers

- Identifying which instrumentation classes need replacement
- Planning migration scope for metrics and observation
- Searching for equivalent functionality in Spring Boot 3.0

## Examples

### Example 1

Input:

  Found WebMvcMetricsFilter in codebase

Output:

  Replace with Spring Framework's ServerHttpObservationFilter; update to use ServerRequestObservationConvention for custom behavior

### Example 2

Input:

  Found MetricsRestTemplateCustomizer in RestTemplateBuilder configuration

Output:

  Replace with ObservationRestTemplateCustomizer; apply to RestTemplateBuilder bean

### Example 3

Input:

  Have custom TagProvider or TagContributor implementations

Output:

  Extend DefaultServerRequestObservationConvention and override getLowCardinalityKeyValues() to add custom KeyValues

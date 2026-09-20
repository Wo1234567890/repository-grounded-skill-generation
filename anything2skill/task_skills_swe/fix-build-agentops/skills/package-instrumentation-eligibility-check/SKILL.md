---
id: "e63667bd-2d54-5e5c-afa1-a566d7cccf56"
name: "Package Instrumentation Eligibility Check"
description: "Determine whether a package should be instrumented by AgentOps by verifying it is not already instrumented and is in the target allowlist (AGENTIC_LIBRARIES or PROVIDERS). Prevents duplicate instrumentation and filters non-target packages."
version: "0.1.0"
tags:
  - "instrumentation"
  - "package_discovery"
  - "conditional_gate"
  - "agentops"
  - "integration_filtering"
triggers:
  - "Package discovery or initialization phase begins"
  - "A new package is encountered during dependency scanning"
  - "Instrumentation decision is required before applying AgentOps hooks"
---

# Package Instrumentation Eligibility Check

Determine whether a package should be instrumented by AgentOps by verifying it is not already instrumented and is in the target allowlist (AGENTIC_LIBRARIES or PROVIDERS). Prevents duplicate instrumentation and filters non-target packages.

## Prompt

Check if a package is eligible for AgentOps instrumentation by verifying: (1) the package is not already instrumented via _is_package_instrumented(), (2) the package is in the AGENTIC_LIBRARIES or PROVIDERS allowlist. Return False (skip) if the package is already instrumented or not in either allowlist; return True (proceed) only if the package is not yet instrumented AND is in at least one allowlist.

## Objective

decide_instrumentation_eligibility
## Applicable Signals

- package_name available
- AGENTIC_LIBRARIES and PROVIDERS lists populated
- instrumentation state queryable via _is_package_instrumented()

## Contraindications

- Package is already fully instrumented by AgentOps
- Package is not in AGENTIC_LIBRARIES or PROVIDERS allowlists
- Instrumentation is disabled globally
- Package name is null or empty

## Workflow Steps

- {'step': 1, 'action': 'Check if package is already instrumented', 'condition': '_is_package_instrumented(package_name) returns True', 'outcome': 'Log debug message and return False (skip instrumentation)'}
- {'step': 2, 'action': 'Check if package is in target agentic libraries', 'condition': 'package_name in AGENTIC_LIBRARIES', 'outcome': 'Set is_target_agentic = True'}
- {'step': 3, 'action': 'Check if package is in target providers', 'condition': 'package_name in PROVIDERS', 'outcome': 'Set is_target_provider = True'}
- {'step': 4, 'action': 'Evaluate membership', 'condition': 'is_target_agentic OR is_target_provider', 'outcome': 'Return True (proceed with instrumentation)'}
- {'step': 5, 'action': 'Default decision', 'condition': 'Neither agentic nor provider check passed', 'outcome': 'Log debug message and return False (skip instrumentation)'}

## Constraints

- Must check prior instrumentation state before evaluating target membership
- Must reference AGENTIC_LIBRARIES and PROVIDERS as authoritative allowlists
- Decision must be logged with rationale for debugging

## Cautions

- Duplicate instrumentation can cause performance degradation or conflicts; verify _is_package_instrumented() is reliable
- Allowlist membership must be kept in sync with supported integrations

## Output Contract

- Boolean decision (True to instrument, False to skip) with debug log entry confirming the decision rationale. Caller receives clear signal for downstream instrumentation routing.

## Triggers

- Package discovery or initialization phase begins
- A new package is encountered during dependency scanning
- Instrumentation decision is required before applying AgentOps hooks

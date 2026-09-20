---
id: "cd0bfed4-59ec-5259-90fd-1903beb88f0e"
name: "Version-Specific OpenAI Instrumentor Initialization"
description: "Detect OpenAI library version at runtime and apply the appropriate instrumentation strategy: delegate to legacy instrumentor for v0, or proceed with standard v1 initialization. Ensures instrumentation compatibility across library versions by routing initialization logic based on version detection."
version: "0.1.0"
tags:
  - "openai"
  - "instrumentation"
  - "version_detection"
  - "initialization"
  - "conditional_routing"
  - "compatibility"
triggers:
  - "OpenAI library version is unknown or mixed (v0 and v1 coexist)"
  - "Initialization phase begins and library version must be detected"
  - "Runtime environment requires adaptive instrumentation strategy"
examples:
  - input: "is_openai_v1() returns False; kwargs={'tracer': <tracer_instance>}"
    output: "OpenAIV0Instrumentor().instrument(tracer=<tracer_instance>) is called; self.config.wrapped_methods = []"
    notes: "Legacy v0 path: delegate to v0-specific instrumentor and suppress v1 wrapping"
  - input: "is_openai_v1() returns True; kwargs={'tracer': <tracer_instance>}"
    output: "Normal initialization continues; wrapped_methods list is populated by parent class; no legacy instrumentor invoked"
    notes: "Current v1 path: proceed with standard instrumentation flow"
---

# Version-Specific OpenAI Instrumentor Initialization

Detect OpenAI library version at runtime and apply the appropriate instrumentation strategy: delegate to legacy instrumentor for v0, or proceed with standard v1 initialization. Ensures instrumentation compatibility across library versions by routing initialization logic based on version detection.

## Prompt

Check the OpenAI library version using is_openai_v1(). If v0 is detected, instantiate and invoke OpenAIV0Instrumentor().instrument() with the provided kwargs, then clear the wrapped_methods list to prevent double instrumentation. If v1 is detected, proceed with normal initialization. This micro-step runs during the _initialize phase before custom wrapping is applied.

## Objective

Route instrumentation logic based on OpenAI library version to ensure compatibility across v0 and v1
## Applicable Signals

- is_openai_v1() returns False (legacy v0 detected)
- is_openai_v1() returns True (current v1 detected)
- InstrumentorConfig is instantiated and ready for version-specific adjustment

## Contraindications

- Library version is guaranteed to be v1 only; version detection is unnecessary
- Legacy v0 support is not required or deprecated
- Instrumentation must not branch on version; single-version setup is enforced

## Workflow Steps

- {'step': 1, 'action': 'Check OpenAI library version', 'detail': 'Call is_openai_v1() to determine if the library is v0 or v1'}
- {'step': 2, 'action': 'Route to legacy instrumentor if v0', 'detail': 'If is_openai_v1() returns False, instantiate OpenAIV0Instrumentor() and call .instrument(**kwargs)'}
- {'step': 3, 'action': 'Clear wrapped methods for v0 path', 'detail': 'Set self.config.wrapped_methods = [] to skip normal v1 wrapping after legacy instrumentation'}
- {'step': 4, 'action': 'Proceed with v1 initialization if v1 detected', 'detail': 'If is_openai_v1() returns True, continue with normal initialization flow'}

## Constraints

- is_openai_v1() function must be available and reliable
- OpenAIV0Instrumentor class must be importable and functional if v0 is detected
- wrapped_methods list must be cleared after legacy instrumentor invocation to prevent duplicate wrapping
- kwargs passed to _initialize must be forwarded to legacy instrumentor without modification

## Cautions

- If legacy instrumentor fails, the entire initialization may fail; ensure v0 support is tested
- Clearing wrapped_methods after v0 instrumentation prevents normal v1 wrapping; confirm this is the intended behavior
- Version detection must occur before custom wrapping (_custom_wrap) to avoid conflicts

## Output Contract

- Correct instrumentor selected and initialized; wrapped_methods list populated or cleared based on version; no instrumentation errors on legacy or current versions; initialization state is consistent with detected library version

## Example Executions

### Example 1

- Input: is_openai_v1() returns False; kwargs={'tracer': <tracer_instance>}
- Output: OpenAIV0Instrumentor().instrument(tracer=<tracer_instance>) is called; self.config.wrapped_methods = []
- Notes: Legacy v0 path: delegate to v0-specific instrumentor and suppress v1 wrapping

### Example 2

- Input: is_openai_v1() returns True; kwargs={'tracer': <tracer_instance>}
- Output: Normal initialization continues; wrapped_methods list is populated by parent class; no legacy instrumentor invoked
- Notes: Current v1 path: proceed with standard instrumentation flow

## Triggers

- OpenAI library version is unknown or mixed (v0 and v1 coexist)
- Initialization phase begins and library version must be detected
- Runtime environment requires adaptive instrumentation strategy

## Examples

### Example 1

Input:

  is_openai_v1() returns False; kwargs={'tracer': <tracer_instance>}

Output:

  OpenAIV0Instrumentor().instrument(tracer=<tracer_instance>) is called; self.config.wrapped_methods = []

Notes:

  Legacy v0 path: delegate to v0-specific instrumentor and suppress v1 wrapping

### Example 2

Input:

  is_openai_v1() returns True; kwargs={'tracer': <tracer_instance>}

Output:

  Normal initialization continues; wrapped_methods list is populated by parent class; no legacy instrumentor invoked

Notes:

  Current v1 path: proceed with standard instrumentation flow

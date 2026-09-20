---
id: "f51af5de-39df-59d7-a895-20bfd95920c7"
name: "OpenAI Library Instrumentation Setup"
description: "Configure and initialize OpenTelemetry instrumentation for OpenAI client library with version-specific handling and streaming wrapper registration. Establishes comprehensive observability for OpenAI API calls including chat completions, beta endpoints, and responses APIs."
version: "0.1.0"
tags:
  - "observability"
  - "instrumentation"
  - "opentelemetry"
  - "openai"
  - "telemetry"
  - "tracing"
triggers:
  - "OpenAI client library is added as a project dependency"
  - "Agent or application requires telemetry collection and distributed tracing"
  - "Integration with observability platform (e.g., AgentOps) is initiated"
examples:
  - input: "OpenAI library v1.0+ installed; agent requires distributed tracing"
    output: "OpenaiInstrumentor instance with v1 streaming wrappers registered for Completions.create, AsyncCompletions.create, beta Completions.parse, AsyncCompletions.parse, and Responses.create; metrics enabled"
    notes: "Standard path for modern OpenAI library"
  - input: "OpenAI library v0.x installed; legacy support required"
    output: "OpenaiInstrumentor delegates to OpenAIV0Instrumentor; wrapped_methods cleared to prevent double-wrapping"
    notes: "Fallback path for older OpenAI versions"
---

# OpenAI Library Instrumentation Setup

Configure and initialize OpenTelemetry instrumentation for OpenAI client library with version-specific handling and streaming wrapper registration. Establishes comprehensive observability for OpenAI API calls including chat completions, beta endpoints, and responses APIs.

## Prompt

Initialize an OpenaiInstrumentor instance by: (1) creating an InstrumentorConfig with library metadata, wrapped methods, and metrics enabled; (2) detecting OpenAI library version and applying version-specific initialization (legacy v0 fallback or v1 standard); (3) registering custom streaming wrappers for chat completion, async chat completion, beta chat completion parse, and responses APIs using wrap_function_wrapper. Ensure all wrapped methods are configured before instrumentation completes.

## Objective

Set up comprehensive observability instrumentation for OpenAI API calls with version compatibility and streaming support
## Applicable Signals

- openai library version >= 0.27.0 detected
- instrumentation framework initialized
- metrics collection enabled in configuration

## Contraindications

- OpenAI library is not a project dependency
- Instrumentation is already active for OpenAI
- Telemetry collection is explicitly disabled
- Application does not require distributed tracing

## Workflow Steps

- {'step': 1, 'action': 'Create InstrumentorConfig', 'details': 'Instantiate InstrumentorConfig with library_name, library_version, wrapped_methods from _get_wrapped_methods(), metrics_enabled=True, and dependencies=["openai >= 0.27.0"]'}
- {'step': 2, 'action': 'Call parent __init__', 'details': 'Pass config to super().__init__(config) to initialize CommonInstrumentor base'}
- {'step': 3, 'action': 'Detect OpenAI version', 'details': 'In _initialize(), call is_openai_v1() to determine library version'}
- {'step': 4, 'action': 'Apply version-specific initialization', 'details': 'If not v1 (legacy v0): instantiate OpenAIV0Instrumentor, call instrument(**kwargs), and clear wrapped_methods list. Otherwise, proceed to custom wrapping.'}
- {'step': 5, 'action': 'Register streaming wrappers', 'details': 'In _custom_wrap(), if is_openai_v1() and self._tracer exists, use wrap_function_wrapper to register wrappers for: (a) openai.resources.chat.completions.Completions.create (sync), (b) openai.resources.chat.completions.AsyncCompletions.create (async), (c) openai.resources.beta.chat.completions.Completions.parse (beta sync), (d) openai.resources.beta.chat.completions.AsyncCompletions.parse (beta async), (e) openai.resources.responses.Responses.create (responses API)'}
- {'step': 6, 'action': 'Verify instrumentation complete', 'details': 'Confirm all wrapped methods are registered and tracer is active'}

## Constraints

- OpenAI library version must be >= 0.27.0
- CommonInstrumentor base class must be available
- wrapt library must be available for function wrapping
- Tracer instance must be initialized before custom wrapping

## Cautions

- Version detection (is_openai_v1) must execute before initialization to avoid wrapping legacy endpoints incorrectly
- For OpenAI v0, skip normal instrumentation and delegate to OpenAIV0Instrumentor to prevent double-wrapping
- Streaming wrappers require tracer to be non-null; check self._tracer before attempting custom wraps

## Output Contract

- Instrumentor instance fully configured with: (1) InstrumentorConfig containing library metadata and wrapped method list; (2) version-specific initialization applied (legacy fallback or v1 standard); (3) all streaming wrappers registered for chat completions, beta endpoints, and responses APIs; (4) metrics collection enabled; (5) ready for downstream telemetry collection and tracing of OpenAI API calls

## Example Executions

### Example 1

- Input: OpenAI library v1.0+ installed; agent requires distributed tracing
- Output: OpenaiInstrumentor instance with v1 streaming wrappers registered for Completions.create, AsyncCompletions.create, beta Completions.parse, AsyncCompletions.parse, and Responses.create; metrics enabled
- Notes: Standard path for modern OpenAI library

### Example 2

- Input: OpenAI library v0.x installed; legacy support required
- Output: OpenaiInstrumentor delegates to OpenAIV0Instrumentor; wrapped_methods cleared to prevent double-wrapping
- Notes: Fallback path for older OpenAI versions

## Triggers

- OpenAI client library is added as a project dependency
- Agent or application requires telemetry collection and distributed tracing
- Integration with observability platform (e.g., AgentOps) is initiated

## Examples

### Example 1

Input:

  OpenAI library v1.0+ installed; agent requires distributed tracing

Output:

  OpenaiInstrumentor instance with v1 streaming wrappers registered for Completions.create, AsyncCompletions.create, beta Completions.parse, AsyncCompletions.parse, and Responses.create; metrics enabled

Notes:

  Standard path for modern OpenAI library

### Example 2

Input:

  OpenAI library v0.x installed; legacy support required

Output:

  OpenaiInstrumentor delegates to OpenAIV0Instrumentor; wrapped_methods cleared to prevent double-wrapping

Notes:

  Fallback path for older OpenAI versions

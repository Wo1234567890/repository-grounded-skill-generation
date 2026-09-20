---
id: "632f9b0e-d20b-5fa0-b0a2-df6b66a333cd"
name: "Streaming API Wrapper Registration"
description: "Register function wrappers for OpenAI v1 streaming endpoints to capture telemetry for sync and async calls. Attaches tracing wrappers to chat completions, beta completions, and responses API entry points."
version: "0.1.0"
tags:
  - "openai"
  - "instrumentation"
  - "streaming"
  - "telemetry"
  - "wrapper"
  - "tracing"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "OpenAI v1 is detected"
  - "Streaming telemetry is required"
  - "Tracer instance is available and initialized"
---

# Streaming API Wrapper Registration

Register function wrappers for OpenAI v1 streaming endpoints to capture telemetry for sync and async calls. Attaches tracing wrappers to chat completions, beta completions, and responses API entry points.

## Prompt

Use wrap_function_wrapper to attach stream wrapper functions to OpenAI v1 streaming method entry points. Register wrappers for: (1) openai.resources.chat.completions.Completions.create and AsyncCompletions.create, (2) openai.resources.beta.chat.completions.Completions.parse and AsyncCompletions.parse, (3) openai.resources.responses.Responses.create. Each wrapper call passes the tracer instance to enable telemetry capture.

## Objective

Attach tracing wrappers to streaming method entry points for OpenAI v1 to enable telemetry capture
## Applicable Signals

- is_openai_v1() returns True
- self._tracer is not None
- Custom wrapping phase is entered

## Contraindications

- Streaming is not used in the application
- Tracer is None or uninitialized
- OpenAI v0 is active (use legacy instrumentor instead)
- wrap_function_wrapper is not available

## Workflow Steps

- {'step': 1, 'action': 'Check tracer availability', 'detail': 'Verify self._tracer is not None before proceeding'}
- {'step': 2, 'action': 'Register chat completions sync wrapper', 'detail': "wrap_function_wrapper('openai.resources.chat.completions', 'Completions.create', chat_completion_stream_wrapper(self._tracer))"}
- {'step': 3, 'action': 'Register chat completions async wrapper', 'detail': "wrap_function_wrapper('openai.resources.chat.completions', 'AsyncCompletions.create', async_chat_completion_stream_wrapper(self._tracer))"}
- {'step': 4, 'action': 'Register beta completions sync wrapper', 'detail': "wrap_function_wrapper('openai.resources.beta.chat.completions', 'Completions.parse', chat_completion_stream_wrapper(self._tracer))"}
- {'step': 5, 'action': 'Register beta completions async wrapper', 'detail': "wrap_function_wrapper('openai.resources.beta.chat.completions', 'AsyncCompletions.parse', async_chat_completion_stream_wrapper(self._tracer))"}
- {'step': 6, 'action': 'Register responses API wrapper', 'detail': "wrap_function_wrapper('openai.resources.responses', 'Responses.create', responses_stream_wrapper(self._tracer))"}

## Constraints

- Must execute after version detection confirms OpenAI v1
- Tracer instance must be initialized before wrapper registration
- All four endpoint paths must be wrapped in sequence to ensure complete coverage

## Cautions

- Wrapping errors should be caught and logged; do not silently fail
- Ensure wrapper functions (chat_completion_stream_wrapper, async_chat_completion_stream_wrapper, responses_stream_wrapper) are defined before registration

## Output Contract

- All four streaming endpoints wrapped with corresponding stream wrapper functions; no import or wrapping errors; tracer is passed to each wrapper for telemetry capture.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- OpenAI v1 is detected
- Streaming telemetry is required
- Tracer instance is available and initialized

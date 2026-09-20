---
id: "1ee9b37e-ec9b-5576-80e8-6df9e2f57d51"
name: "LLM API Call Tracking"
description: "Automatically capture and log LLM API interactions from supported providers, extracting model, provider, token counts, cost, and message content for observability and debugging."
version: "0.1.0"
tags:
  - "llm_observability"
  - "instrumentation"
  - "api_tracking"
  - "monitoring"
  - "agentops"
triggers:
  - "LLM agent initialization with supported provider (OpenAI, Anthropic, etc.)"
  - "Need to monitor API usage, costs, and performance metrics"
  - "Debugging or observability requirement for LLM interactions"
examples:
  - input: "Agent makes API call to OpenAI GPT-4 with prompt 'Analyze this data'"
    output: "Log entry: {model: 'gpt-4', provider: 'OpenAI', prompt_tokens: 5, completion_tokens: 42, cost: 0.00156, messages: {prompt: 'Analyze this data', completion: '...'}}"
---

# LLM API Call Tracking

Automatically capture and log LLM API interactions from supported providers, extracting model, provider, token counts, cost, and message content for observability and debugging.

## Prompt

Initialize AgentOps instrumentation to intercept and track LLM API calls. Collect model name, provider identifier, prompt token count, completion token count, estimated interaction cost, and full message content. Log structured entries for each API interaction.

## Objective

Collect comprehensive LLM interaction metadata for monitoring and analysis
## Applicable Signals

- LLM provider integration event
- API call initiation from supported provider
- Agent execution with LLM backend

## Contraindications

- Unsupported LLM provider
- API call logging disabled by policy
- No instrumentation framework available

## Intervention Moves

- Initialize AgentOps tracking module
- Intercept provider API calls
- Extract and structure metadata fields
- Log interaction record

## Workflow Steps

- {'step': 1, 'action': 'Import and initialize AgentOps', 'detail': 'Load agentops module and configure for target provider'}
- {'step': 2, 'action': 'Establish provider connection', 'detail': 'Connect to supported LLM provider (OpenAI, Anthropic, etc.)'}
- {'step': 3, 'action': 'Intercept API calls', 'detail': 'Enable automatic tracking of outbound API requests'}
- {'step': 4, 'action': 'Extract metadata', 'detail': 'Capture model name, provider, prompt tokens, completion tokens, cost, messages'}
- {'step': 5, 'action': 'Log structured entry', 'detail': 'Record complete interaction metadata for observability'}

## Constraints

- Provider must be in supported list (OpenAI, Anthropic, etc.)
- AgentOps library must be installed and initialized
- API credentials must be valid and accessible

## Cautions

- Ensure sensitive prompt content is handled according to data retention policy
- Monitor cost tracking accuracy against actual provider billing
- Verify token count calculations match provider specifications

## Output Contract

- Structured log entries containing: model identifier, provider name, prompt token count, completion token count, estimated cost, and full prompt and completion message content. Each entry is timestamped and linked to the originating agent execution.

## Example Executions

### Example 1

- Input: Agent makes API call to OpenAI GPT-4 with prompt 'Analyze this data'
- Output: Log entry: {model: 'gpt-4', provider: 'OpenAI', prompt_tokens: 5, completion_tokens: 42, cost: 0.00156, messages: {prompt: 'Analyze this data', completion: '...'}}

## Triggers

- LLM agent initialization with supported provider (OpenAI, Anthropic, etc.)
- Need to monitor API usage, costs, and performance metrics
- Debugging or observability requirement for LLM interactions

## Examples

### Example 1

Input:

  Agent makes API call to OpenAI GPT-4 with prompt 'Analyze this data'

Output:

  Log entry: {model: 'gpt-4', provider: 'OpenAI', prompt_tokens: 5, completion_tokens: 42, cost: 0.00156, messages: {prompt: 'Analyze this data', completion: '...'}}

---
id: "44161230-0147-5338-8218-7c5c95ef22d1"
name: "Anthropic Streaming Message Handler"
description: "Consume streamed message tokens from Anthropic Claude API within an AgentOps session. Handles incremental token delivery for real-time agent response processing."
version: "0.1.0"
tags:
  - "anthropic"
  - "streaming"
  - "agentops"
  - "integration"
  - "real-time"
  - "token-consumption"
triggers:
  - "Anthropic integration requires low-latency token streaming"
  - "Agent needs to process partial responses in real-time"
  - "AgentOps session is active and initialized"
---

# Anthropic Streaming Message Handler

Consume streamed message tokens from Anthropic Claude API within an AgentOps session. Handles incremental token delivery for real-time agent response processing.

## Prompt

Initialize Anthropic client with AgentOps context. Create a streaming message request. Iterate through the stream, capturing each content block delta. Log token consumption to AgentOps. Finalize the session with completion status.

## Objective

Consume streamed message tokens from Anthropic API with AgentOps tracking
## Applicable Signals

- streaming=true in request configuration
- Anthropic client instantiated
- AgentOps session context available

## Contraindications

- Full message buffering is acceptable; use non-streaming variant instead
- Non-streaming Anthropic calls only
- AgentOps not initialized or session not started

## Workflow Steps

- Verify AgentOps session is active
- Instantiate Anthropic client
- Create streaming message request with max_tokens and model parameters
- Iterate through stream response, capturing each content block
- Log token deltas to AgentOps tracking
- Accumulate final message state from stream completion
- End AgentOps session with completion status

## Constraints

- AgentOps session must be initialized before streaming begins
- Anthropic client must be configured with valid credentials
- Stream must be consumed within active session context

## Cautions

- Incomplete stream consumption may result in lost tokens or incomplete logging
- Network interruption during streaming requires error handling and session recovery

## Output Contract

- Stream consumed completely; all tokens captured and logged; final message state available for downstream processing; AgentOps session closed with success or error status

## Triggers

- Anthropic integration requires low-latency token streaming
- Agent needs to process partial responses in real-time
- AgentOps session is active and initialized

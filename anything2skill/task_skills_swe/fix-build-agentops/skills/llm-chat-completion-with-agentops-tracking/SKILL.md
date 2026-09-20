---
id: "4862f3b3-8d5d-5992-8f28-f11b25465da9"
name: "LLM Chat Completion with AgentOps Tracking"
description: "Execute a chat completion request to an LLM endpoint with AgentOps session tracking enabled. Captures the API call, model selection, and response for observability and debugging."
version: "0.1.0"
tags:
  - "llm"
  - "chat_completion"
  - "agentops"
  - "observability"
  - "api_integration"
triggers:
  - "LLM response needed for agent task"
  - "User query requires LLM inference"
  - "AgentOps session is active and initialized"
examples:
  - input: "User message: 'Tell me a cool fact about AgentOps', model: 'open-mistral-nemo'"
    output: "LLM response content printed; interaction recorded in AgentOps session"
    notes: "Assumes AgentOps session already initialized and LLM client configured"
---

# LLM Chat Completion with AgentOps Tracking

Execute a chat completion request to an LLM endpoint with AgentOps session tracking enabled. Captures the API call, model selection, and response for observability and debugging.

## Prompt

Invoke the LLM client's chat.complete method with a user message and model identifier. Extract the response content from the message choices and print or return it. The AgentOps session must be active before this call.

## Objective

invoke_llm_with_tracking
## Applicable Signals

- AgentOps session started
- LLM client configured with valid endpoint
- User message or prompt ready

## Contraindications

- AgentOps session not initialized
- LLM endpoint unavailable or misconfigured
- No observability or tracking requirement

## Workflow Steps

- Verify AgentOps session is active
- Prepare user message with role and content
- Call client.chat.complete with messages list and model parameter
- Extract response from message.choices[0].message.content
- Return or print the response content

## Constraints

- AgentOps session must be active before invocation
- LLM client must be instantiated with valid credentials
- Model identifier must be supported by the endpoint

## Cautions

- Ensure session is ended after all LLM calls complete
- Handle API errors and timeouts gracefully
- Validate response structure before accessing message content

## Output Contract

- LLM response message content extracted and returned; interaction logged in AgentOps session for observability

## Example Executions

### Example 1

- Input: User message: 'Tell me a cool fact about AgentOps', model: 'open-mistral-nemo'
- Output: LLM response content printed; interaction recorded in AgentOps session
- Notes: Assumes AgentOps session already initialized and LLM client configured

## Triggers

- LLM response needed for agent task
- User query requires LLM inference
- AgentOps session is active and initialized

## Examples

### Example 1

Input:

  User message: 'Tell me a cool fact about AgentOps', model: 'open-mistral-nemo'

Output:

  LLM response content printed; interaction recorded in AgentOps session

Notes:

  Assumes AgentOps session already initialized and LLM client configured

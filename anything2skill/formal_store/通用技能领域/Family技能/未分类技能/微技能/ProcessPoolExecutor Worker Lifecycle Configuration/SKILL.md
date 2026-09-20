---
id: "a57f0399-4bb1-5b74-ac1f-a7080f6b3f1f"
name: "ProcessPoolExecutor Worker Lifecycle Configuration"
description: "Initialize AgentOps client with API key loaded from environment variables and configure session lifecycle management for decorator-based tracing."
version: "0.1.1"
tags:
  - "agent_instrumentation"
  - "session_management"
  - "initialization"
  - "environment_configuration"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Need to specify fork vs spawn start method for cross-platform compatibility"
  - "Require custom worker initialization before task execution"
  - "Need to limit worker task count to control memory or resource accumulation"
  - "Multiprocessing context must be explicitly controlled"
---

# ProcessPoolExecutor Worker Lifecycle Configuration

Initialize AgentOps client with API key loaded from environment variables and configure session lifecycle management for decorator-based tracing.

## Prompt

Load AGENTOPS_API_KEY from environment variables using load_dotenv(). Call agentops.init() with the API key, set auto_start_session=False to allow external decorators (@trace) to manage session lifecycle, and optionally include tags for session identification.

## Objective

configure_agent_instrumentation
## Applicable Signals

- Application startup phase
- Decorator-based session management pattern detected

## Contraindications

- Session lifecycle is already managed by a parent framework
- auto_start_session=True is required by downstream code

## Workflow Steps

- Call load_dotenv() to load environment variables from .env file
- Retrieve AGENTOPS_API_KEY using os.getenv()
- Call agentops.init() with API key, auto_start_session=False, and optional tags
- Verify client initialization completes without error

## Constraints

- AGENTOPS_API_KEY must be available in environment variables
- load_dotenv() must be called before accessing environment variables
- auto_start_session must be set to False when using external session decorators

## Output Contract

- AgentOps client initialized with API key loaded from environment; session ready for decorator-managed tracing; client instance available for downstream instrumentation.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need to specify fork vs spawn start method for cross-platform compatibility
- Require custom worker initialization before task execution
- Need to limit worker task count to control memory or resource accumulation
- Multiprocessing context must be explicitly controlled

---
id: "0d3b8c73-bb09-5ca7-be2b-c651fe62185f"
name: "Initialize AgentOps Client with API Keys"
description: "Load environment variables for API authentication and initialize the AgentOps client with session configuration, trace naming, and metadata tags. This skill sets up an authenticated AgentOps session for agent tracing and monitoring before any agent execution begins."
version: "0.1.0"
tags:
  - "initialization"
  - "authentication"
  - "agentops"
  - "openai"
  - "session_setup"
  - "configuration"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Starting a new agent application that requires OpenAI and AgentOps integration"
  - "Before any agent execution or tracing begins"
  - "When environment variables are available and session is not yet initialized"
examples:
  - input: "Environment variables OPENAI_API_KEY and AGENTOPS_API_KEY are set in .env file"
    output: "client (OpenAI instance) and tracer (AgentOps tracer) are ready; session is active with trace_name and tags recorded"
    notes: "Typical startup scenario for a new agent application"
---

# Initialize AgentOps Client with API Keys

Load environment variables for API authentication and initialize the AgentOps client with session configuration, trace naming, and metadata tags. This skill sets up an authenticated AgentOps session for agent tracing and monitoring before any agent execution begins.

## Prompt

1. Load environment variables using dotenv or equivalent mechanism.
2. Set OPENAI_API_KEY and AGENTOPS_API_KEY in os.environ from loaded variables or defaults.
3. Call agentops.init() with auto_start_session=True, providing a trace_name and tags for session metadata.
4. Create a tracer object using agentops.start_trace() with matching trace_name and tags.
5. Instantiate OpenAI client.
6. Verify that client and tracer are ready for downstream agent operations.

## Objective

Set up authenticated AgentOps session for agent tracing and monitoring
## Applicable Signals

- Application startup phase
- Agent framework initialization requested
- API credentials available in environment or configuration

## Contraindications

- API keys are already loaded in memory
- AgentOps session is already initialized
- Running in a context where environment variables cannot be safely modified
- Credentials are not available or invalid

## Workflow Steps

- {'step': 1, 'action': 'Load environment variables', 'detail': 'Call load_dotenv() to load variables from .env file or equivalent'}
- {'step': 2, 'action': 'Set OPENAI_API_KEY', 'detail': 'os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")'}
- {'step': 3, 'action': 'Set AGENTOPS_API_KEY', 'detail': 'os.environ["AGENTOPS_API_KEY"] = os.getenv("AGENTOPS_API_KEY", "your_api_key_here")'}
- {'step': 4, 'action': 'Initialize AgentOps client', 'detail': 'agentops.init(auto_start_session=True, trace_name="<descriptive_name>", tags=[<relevant_tags>])'}
- {'step': 5, 'action': 'Create tracer object', 'detail': 'tracer = agentops.start_trace(trace_name="<descriptive_name>", tags=[<relevant_tags>])'}
- {'step': 6, 'action': 'Instantiate OpenAI client', 'detail': 'client = OpenAI()'}

## Constraints

- OPENAI_API_KEY and AGENTOPS_API_KEY must be accessible via environment or dotenv
- dotenv or equivalent environment loading mechanism must be available
- agentops and openai packages must be installed and importable
- Session initialization must complete before any tracing or agent execution

## Cautions

- Do not hardcode API keys in source code; use environment variables or secure vaults
- Ensure trace_name and tags are descriptive for debugging and monitoring
- Verify that auto_start_session=True is appropriate for your use case; disable if manual session control is needed

## Output Contract

- AgentOps client initialized with active session, tracer object created and ready for use, and OpenAI client instantiated. Downstream caller receives (client, tracer) tuple or equivalent objects ready for agent execution and tracing.

## Example Executions

### Example 1

- Input: Environment variables OPENAI_API_KEY and AGENTOPS_API_KEY are set in .env file
- Output: client (OpenAI instance) and tracer (AgentOps tracer) are ready; session is active with trace_name and tags recorded
- Notes: Typical startup scenario for a new agent application

## 子技能目录
- [Initialize AgentOps for Camel AI Observability](通用技能领域/Family技能/未分类技能/微技能/Initialize AgentOps for Camel AI Observability/SKILL.md) ｜ 适用：Set up AgentOps environment variable and initialize the observability client to track and analyze Camel AI agents with full observability.
- [Load and Inject Environment Variables Safely](通用技能领域/Family技能/未分类技能/微技能/Load and Inject Environment Variables Safely/SKILL.md) ｜ 适用：Retrieve API keys from environment or configuration source and inject them into os.environ with fallback defaults, ensuring secure credential handling without hardcoding secrets.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Initialize AgentOps for Camel AI Observability` 时，优先调用它。 线索：Starting a new Camel AI agent project and need to enable tracking and debugging capabilities, observability, camel-ai, agentops, initialization
- 当目标、阶段或方法更接近 `Load and Inject Environment Variables Safely` 时，优先调用它。 线索：Application requires external API keys (OpenAI, AgentOps, etc.), Credentials are stored in .env files or system environment, Before client initialization that depends on environment variables, credential_management, environment_setup

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Starting a new agent application that requires OpenAI and AgentOps integration
- Before any agent execution or tracing begins
- When environment variables are available and session is not yet initialized

## Examples

### Example 1

Input:

  Environment variables OPENAI_API_KEY and AGENTOPS_API_KEY are set in .env file

Output:

  client (OpenAI instance) and tracer (AgentOps tracer) are ready; session is active with trace_name and tags recorded

Notes:

  Typical startup scenario for a new agent application

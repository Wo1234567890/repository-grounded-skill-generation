---
id: "9abe764e-fbfb-5b76-876e-59bdd1b73d66"
name: "AgentOps Session Initialization"
description: "Initialize AgentOps with API key and session configuration, setting auto_start_session=False when session lifecycle is managed externally via decorators."
version: "0.1.0"
tags:
  - "agentops"
  - "initialization"
  - "session_management"
  - "api_integration"
  - "agent_setup"
  - "agent-observability"
  - "tracing"
  - "session-setup"
  - "debugging"
  - "crewai"
triggers:
  - "Starting a new agent application or session that requires operation tracking"
  - "Need to integrate AgentOps API for monitoring and session management"
  - "Session lifecycle will be managed externally via decorators"
  - "Starting a new CrewAI or multi-agent workflow"
  - "Need to enable session tracing and debugging"
  - "Require observability for agent actions and execution traces"
examples:
  - input: "Environment contains AGENTOPS_API_KEY=valid_key_string"
    output: "agentops.init() called with auto_start_session=False and tags set; monitoring active"
    notes: "Typical setup for decorator-managed session lifecycle"
  - input: "auto_start_session=False, trace_name='CrewAI Job Posting', tags=['crewai', 'job-posting']"
    output: "AgentOps session initialized with deferred start; trace_name and tags registered for later session activation"
    notes: "Deferred start allows manual control over when tracing begins"
---

# AgentOps Session Initialization

Initialize AgentOps with API key and session configuration, setting auto_start_session=False when session lifecycle is managed externally via decorators.

## Prompt

Load the AGENTOPS_API_KEY from environment variables using load_dotenv(). Call agentops.init() with the API key, set auto_start_session=False to allow external session management via decorators, and pass tags for session identification.

## Objective

Configure and activate AgentOps monitoring for an agent application
## Applicable Signals

- Application startup phase
- Agent framework initialization
- Decorator-based session management pattern detected
- Workflow initialization phase
- Agent framework instantiation
- Debugging or monitoring requirement

## Contraindications

- AgentOps is already initialized in the same process
- Session lifecycle is managed by a parent framework
- AGENTOPS_API_KEY environment variable is not set
- Running agents without observability requirements
- Offline or local-only execution without telemetry
- Environments where external tracing is prohibited

## Workflow Steps

- {'step': 1, 'action': 'Load environment variables', 'detail': 'Call load_dotenv() to load variables from .env file'}
- {'step': 2, 'action': 'Retrieve API key', 'detail': 'Extract AGENTOPS_API_KEY from environment using os.getenv()'}
- {'step': 3, 'action': 'Initialize AgentOps', 'detail': 'Call agentops.init(api_key, auto_start_session=False, tags=[...])'}
- Import agentops module
- Load environment configuration (dotenv.load_dotenv)
- Call agentops.init() with trace_name, tags, and auto_start_session parameters
- Verify client is ready to capture traces

## Constraints

- auto_start_session must be set to False when using external session management decorators
- API key must be valid and loaded from environment before initialization
- Initialization must occur before any traced operations
- AgentOps package must be installed and imported
- Environment variables (e.g., API keys) must be loaded before init()
- auto_start_session parameter controls whether session starts immediately or on explicit call

## Cautions

- Do not call agentops.init() multiple times in the same process
- Ensure environment variables are loaded before accessing AGENTOPS_API_KEY
- Tags should be meaningful for session identification and filtering

## Output Contract

- AgentOps instance initialized with valid API key, auto_start_session flag set to False, and tags applied for session identification. Monitoring is active and ready for decorator-managed session lifecycle.
- AgentOps client initialized with active session context, ready to capture agent actions and traces. Session metadata (trace_name, tags) is registered and available for downstream observability.

## Example Executions

### Example 1

- Input: Environment contains AGENTOPS_API_KEY=valid_key_string
- Output: agentops.init() called with auto_start_session=False and tags set; monitoring active
- Notes: Typical setup for decorator-managed session lifecycle

### Example 2

- Input: auto_start_session=False, trace_name='CrewAI Job Posting', tags=['crewai', 'job-posting']
- Output: AgentOps session initialized with deferred start; trace_name and tags registered for later session activation
- Notes: Deferred start allows manual control over when tracing begins

## Triggers

- Starting a new agent application or session that requires operation tracking
- Need to integrate AgentOps API for monitoring and session management
- Session lifecycle will be managed externally via decorators
- Starting a new CrewAI or multi-agent workflow
- Need to enable session tracing and debugging
- Require observability for agent actions and execution traces

## Examples

### Example 1

Input:

  Environment contains AGENTOPS_API_KEY=valid_key_string

Output:

  agentops.init() called with auto_start_session=False and tags set; monitoring active

Notes:

  Typical setup for decorator-managed session lifecycle

### Example 2

Input:

  auto_start_session=False, trace_name='CrewAI Job Posting', tags=['crewai', 'job-posting']

Output:

  AgentOps session initialized with deferred start; trace_name and tags registered for later session activation

Notes:

  Deferred start allows manual control over when tracing begins

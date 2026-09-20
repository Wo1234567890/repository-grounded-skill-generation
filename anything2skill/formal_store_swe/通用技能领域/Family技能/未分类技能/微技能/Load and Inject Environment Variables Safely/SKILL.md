---
id: "ba427050-7f6d-5312-9015-b85cded85fd1"
name: "Load and Inject Environment Variables Safely"
description: "Retrieve API keys from environment or configuration source and inject them into os.environ with fallback defaults, ensuring secure credential handling without hardcoding secrets."
version: "0.1.0"
tags:
  - "credential_management"
  - "environment_setup"
  - "api_key_injection"
  - "dotenv"
  - "security"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Application requires external API keys (OpenAI, AgentOps, etc.)"
  - "Credentials are stored in .env files or system environment"
  - "Before client initialization that depends on environment variables"
examples:
  - input: ".env file contains OPENAI_API_KEY=sk-... and AGENTOPS_API_KEY=..."
    output: "os.environ[\"OPENAI_API_KEY\"] and os.environ[\"AGENTOPS_API_KEY\"] are set with loaded values"
    notes: "Standard case: credentials loaded from .env file"
  - input: ".env file missing; system environment has OPENAI_API_KEY set"
    output: "os.environ[\"OPENAI_API_KEY\"] is set from system environment; AGENTOPS_API_KEY uses fallback default"
    notes: "Partial environment case: one key from system, one from fallback"
---

# Load and Inject Environment Variables Safely

Retrieve API keys from environment or configuration source and inject them into os.environ with fallback defaults, ensuring secure credential handling without hardcoding secrets.

## Prompt

Load environment variables from a .env file or system environment using dotenv. Retrieve API keys (e.g., OPENAI_API_KEY, AGENTOPS_API_KEY) and inject them into os.environ with fallback defaults. Ensure the keys are available in the environment before downstream client initialization.

## Objective

Safely load and set API credentials without hardcoding secrets
## Applicable Signals

- dotenv library available
- .env file present in project root or parent directory
- System environment variables set

## Contraindications

- Credentials are already in memory
- Running in a restricted environment where os.environ modification is forbidden
- Using a secrets manager that handles injection automatically

## Workflow Steps

- {'step': 1, 'action': 'Import required modules', 'detail': 'Import dotenv.load_dotenv and os'}
- {'step': 2, 'action': 'Load .env file', 'detail': 'Call load_dotenv() to read environment variables from .env file'}
- {'step': 3, 'action': 'Retrieve and inject OPENAI_API_KEY', 'detail': 'Use os.getenv() to retrieve OPENAI_API_KEY from environment; set os.environ["OPENAI_API_KEY"] with fallback default'}
- {'step': 4, 'action': 'Retrieve and inject AGENTOPS_API_KEY', 'detail': 'Use os.getenv() to retrieve AGENTOPS_API_KEY from environment; set os.environ["AGENTOPS_API_KEY"] with fallback default'}
- {'step': 5, 'action': 'Verify injection', 'detail': 'Confirm that os.environ contains both keys with non-empty values'}

## Constraints

- dotenv must be imported and load_dotenv() callable
- os module must be available
- Fallback defaults should never contain real secrets; use placeholder strings only

## Cautions

- Do not log or print actual API key values
- Ensure .env file is in .gitignore to prevent accidental secret commits
- Verify that os.environ modifications persist for the entire application session

## Output Contract

- os.environ contains OPENAI_API_KEY and AGENTOPS_API_KEY with valid values ready for downstream client initialization

## Example Executions

### Example 1

- Input: .env file contains OPENAI_API_KEY=sk-... and AGENTOPS_API_KEY=...
- Output: os.environ["OPENAI_API_KEY"] and os.environ["AGENTOPS_API_KEY"] are set with loaded values
- Notes: Standard case: credentials loaded from .env file

### Example 2

- Input: .env file missing; system environment has OPENAI_API_KEY set
- Output: os.environ["OPENAI_API_KEY"] is set from system environment; AGENTOPS_API_KEY uses fallback default
- Notes: Partial environment case: one key from system, one from fallback

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Application requires external API keys (OpenAI, AgentOps, etc.)
- Credentials are stored in .env files or system environment
- Before client initialization that depends on environment variables

## Examples

### Example 1

Input:

  .env file contains OPENAI_API_KEY=sk-... and AGENTOPS_API_KEY=...

Output:

  os.environ["OPENAI_API_KEY"] and os.environ["AGENTOPS_API_KEY"] are set with loaded values

Notes:

  Standard case: credentials loaded from .env file

### Example 2

Input:

  .env file missing; system environment has OPENAI_API_KEY set

Output:

  os.environ["OPENAI_API_KEY"] is set from system environment; AGENTOPS_API_KEY uses fallback default

Notes:

  Partial environment case: one key from system, one from fallback

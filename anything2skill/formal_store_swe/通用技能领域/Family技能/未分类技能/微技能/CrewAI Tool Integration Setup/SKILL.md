---
id: "c9c9bfdb-dee1-55da-a3f8-30840db7d2bd"
name: "CrewAI Tool Integration Setup"
description: "Import and instantiate CrewAI tools (WebsiteSearchTool, SerperDevTool, FileReadTool) with required configuration parameters. Prepares a multi-tool agent environment for task execution."
version: "0.1.0"
tags:
  - "crewai"
  - "tool-setup"
  - "agent-initialization"
  - "multi-tool"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Building a CrewAI agent that requires web search, file I/O, or external API access"
  - "Tools need explicit initialization before agent task assignment"
examples:
  - input: "Need to set up web search and file reading for a job posting analysis agent"
    output: "web_search_tool = WebsiteSearchTool(); file_read_tool = FileReadTool(file_path='job_description.md', description='Tool to read job description')"
    notes: "Tools are now ready to be passed to agent task definitions"
---

# CrewAI Tool Integration Setup

Import and instantiate CrewAI tools (WebsiteSearchTool, SerperDevTool, FileReadTool) with required configuration parameters. Prepares a multi-tool agent environment for task execution.

## Prompt

Import the required CrewAI tool classes from crewai_tools.tools. Instantiate each tool with its configuration: WebsiteSearchTool() requires no parameters; SerperDevTool() requires no parameters; FileReadTool() requires file_path and description parameters. Ensure all tool instances are created before passing them to agent task definitions.

## Objective

Configure and instantiate external tools for agent use
## Applicable Signals

- Agent definition requires external tool dependencies
- Multi-tool orchestration is planned

## Contraindications

- Agents use only built-in capabilities with no external tool dependencies
- Tool initialization is handled by framework defaults

## Workflow Steps

- Import tool classes from crewai_tools.tools
- Instantiate WebsiteSearchTool with no required parameters
- Instantiate SerperDevTool with no required parameters
- Instantiate FileReadTool with file_path and description parameters
- Verify all tool instances are ready for agent assignment

## Constraints

- FileReadTool requires valid file_path parameter pointing to an accessible file
- Tool imports must precede instantiation
- All tool instances must be created before agent binding

## Cautions

- Ensure file_path points to an existing, readable file before FileReadTool instantiation
- Tool configuration must match agent task requirements

## Output Contract

- Tool instances created and ready for agent task assignment; tool references available for agent binding.

## Example Executions

### Example 1

- Input: Need to set up web search and file reading for a job posting analysis agent
- Output: web_search_tool = WebsiteSearchTool(); file_read_tool = FileReadTool(file_path='job_description.md', description='Tool to read job description')
- Notes: Tools are now ready to be passed to agent task definitions

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Building a CrewAI agent that requires web search, file I/O, or external API access
- Tools need explicit initialization before agent task assignment

## Examples

### Example 1

Input:

  Need to set up web search and file reading for a job posting analysis agent

Output:

  web_search_tool = WebsiteSearchTool(); file_read_tool = FileReadTool(file_path='job_description.md', description='Tool to read job description')

Notes:

  Tools are now ready to be passed to agent task definitions

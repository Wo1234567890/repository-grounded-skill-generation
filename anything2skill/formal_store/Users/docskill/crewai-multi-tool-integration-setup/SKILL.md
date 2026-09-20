---
id: "da683d52-5269-5aad-8c4d-e2c74527351a"
name: "CrewAI Multi-Tool Integration Setup"
description: "Configure and instantiate multiple specialized tools (WebsiteSearchTool, SerperDevTool, FileReadTool) for use within a CrewAI agent workflow. Each tool is initialized with specific parameters and descriptions to enable web search, external API queries, and file I/O capabilities."
version: "0.1.0"
tags:
  - "crewai"
  - "tool-setup"
  - "agent-orchestration"
  - "configuration"
triggers:
  - "Assembling a CrewAI agent that requires web search capabilities"
  - "Need for external API queries via SerperDev"
  - "Agent workflow requires file I/O operations"
---

# CrewAI Multi-Tool Integration Setup

Configure and instantiate multiple specialized tools (WebsiteSearchTool, SerperDevTool, FileReadTool) for use within a CrewAI agent workflow. Each tool is initialized with specific parameters and descriptions to enable web search, external API queries, and file I/O capabilities.

## Prompt

Initialize three tool instances for CrewAI agents:
1. WebsiteSearchTool: for searching and extracting content from websites
2. SerperDevTool: for external API-based search queries
3. FileReadTool: for reading local files with a specified file path and description

Each tool should be instantiated with appropriate parameters before assignment to agents.

## Objective

prepare_agent_toolset
## Applicable Signals

- Agent definition phase initiated
- Multiple tool types needed for single workflow
- Tool credentials and file paths available

## Contraindications

- Agent requires only built-in reasoning without external tools
- Tool credentials or API keys are not configured
- Required file paths do not exist or are inaccessible
- Network access or external APIs are unavailable

## Workflow Steps

- {'step': 1, 'action': 'Import required tool classes from crewai_tools.tools', 'detail': 'from crewai_tools.tools import WebsiteSearchTool, SerperDevTool, FileReadTool'}
- {'step': 2, 'action': 'Instantiate WebsiteSearchTool', 'detail': 'web_search_tool = WebsiteSearchTool()'}
- {'step': 3, 'action': 'Instantiate SerperDevTool', 'detail': 'serper_dev_tool = SerperDevTool()'}
- {'step': 4, 'action': 'Instantiate FileReadTool with file path and description', 'detail': 'file_read_tool = FileReadTool(file_path="job_description_example.md", description="A tool to read the job description example file.")'}
- {'step': 5, 'action': 'Verify all three tool instances are ready', 'detail': 'Confirm tools are instantiated and accessible for agent assignment'}

## Constraints

- FileReadTool requires valid file_path parameter pointing to an accessible file
- SerperDevTool and WebsiteSearchTool require appropriate API credentials
- Tool instantiation must occur before agent assignment

## Cautions

- Verify all external API credentials are loaded before tool initialization
- Ensure file paths are correct and files exist before FileReadTool instantiation
- Tool initialization failures should be caught and logged for debugging

## Output Contract

- Three tool instances (web_search_tool, serper_dev_tool, file_read_tool) instantiated and ready to be assigned to CrewAI agents. Each tool is configured with appropriate parameters and can be passed to agent definitions.

## Triggers

- Assembling a CrewAI agent that requires web search capabilities
- Need for external API queries via SerperDev
- Agent workflow requires file I/O operations

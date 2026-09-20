---
id: "52ede92c-2b1d-599f-a1c6-67b86b86d311"
name: "Qualify and Resolve XML Namespaces"
description: "Set up AgentOps monitoring for LLM and agent framework calls by importing the library and calling init() with an API key. Use this as the entry point to enable observability in Python agent scripts."
version: "0.1.1"
tags:
  - "initialization"
  - "monitoring"
  - "observability"
  - "agent"
  - "llm"
  - "bootstrap"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Setting or reading SVG/XML attributes with namespace prefixes"
  - "Need to look up standard namespace URIs (e.g., xlink, svg, xmlns)"
  - "Qualifying element or attribute names for DOM or SVG operations"
examples:
  - input: "d3.namespace('xlink:href')"
    output: "{space: 'http://www.w3.org/1999/xlink', local: 'href'}"
    notes: "Resolves the xlink prefix to its standard namespace URI"
  - input: "d3.namespaces"
    output: "Object containing built-in namespace mappings (xlink, svg, xmlns, etc.)"
    notes: "Provides reference for available standard namespaces"
---

# Qualify and Resolve XML Namespaces

Set up AgentOps monitoring for LLM and agent framework calls by importing the library and calling init() with an API key. Use this as the entry point to enable observability in Python agent scripts.

## Prompt

Import the agentops library and call agentops.init() with your API key to activate monitoring. This must be done before any agent or LLM calls are made.

## Objective

Initialize monitoring infrastructure
## Applicable Signals

- Script entry point reached
- Agent framework instantiation planned
- LLM integration required

## Contraindications

- Monitoring is already active
- API key is unavailable or invalid
- Script does not use supported LLM or agent frameworks

## Workflow Steps

- {'step': 1, 'action': 'Import agentops library', 'detail': 'Add `import agentops` to your script'}
- {'step': 2, 'action': 'Call initialization function', 'detail': 'Call `agentops.init()` with your API key'}

## Constraints

- API key must be valid and available
- agentops library must be installed
- Initialization must occur before any monitored calls

## Output Contract

- AgentOps library imported and init() executed successfully; monitoring is active and ready to capture agent and LLM calls.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Setting or reading SVG/XML attributes with namespace prefixes
- Need to look up standard namespace URIs (e.g., xlink, svg, xmlns)
- Qualifying element or attribute names for DOM or SVG operations

## Examples

### Example 1

Input:

  d3.namespace('xlink:href')

Output:

  {space: 'http://www.w3.org/1999/xlink', local: 'href'}

Notes:

  Resolves the xlink prefix to its standard namespace URI

### Example 2

Input:

  d3.namespaces

Output:

  Object containing built-in namespace mappings (xlink, svg, xmlns, etc.)

Notes:

  Provides reference for available standard namespaces

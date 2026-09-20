---
id: "a15c94c4-b528-54d1-ba34-fce25d8b9141"
name: "Session Drawer Navigation"
description: "Locate and retrieve a previously recorded session from the Session Drawer by browsing session history and metadata such as execution time and SDK versions."
version: "0.1.0"
tags:
  - "session-management"
  - "debugging"
  - "navigation"
  - "retrieval"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "User knows approximate session timestamp or wants to browse available sessions"
  - "User needs to select a past session for inspection or analysis"
---

# Session Drawer Navigation

Locate and retrieve a previously recorded session from the Session Drawer by browsing session history and metadata such as execution time and SDK versions.

## Prompt

Open the Session Drawer and browse the list of previously recorded sessions. Use session metadata (execution time, SDK versions, framework type) to identify and select the target session. Click or select the session to load it for further inspection.

## Objective

Find and open a specific past session
## Applicable Signals

- Session history is available in the Session Drawer
- User has completed at least one recorded session

## Contraindications

- A session is already open and active
- Real-time monitoring of current execution is in progress

## Workflow Steps

- Access the Session Drawer from the main interface
- Review the list of previously recorded sessions with metadata
- Identify the target session using execution time, SDK version, or framework type
- Select or click the session to load it

## Constraints

- Session Drawer must be accessible from the current view
- Session metadata (execution time, SDK versions) must be populated

## Cautions

- Ensure the correct session is selected before proceeding to detailed analysis
- Session metadata may vary depending on the agent framework used (e.g., Crew, AutoGen)

## Output Contract

- Selected session is loaded and ready for drilldown analysis (waterfall view, LLM call details, event breakdown) or overview inspection (meta-analysis across sessions).

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- User knows approximate session timestamp or wants to browse available sessions
- User needs to select a past session for inspection or analysis

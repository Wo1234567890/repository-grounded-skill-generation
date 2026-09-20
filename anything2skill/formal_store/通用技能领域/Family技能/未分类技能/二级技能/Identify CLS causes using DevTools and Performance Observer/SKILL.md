---
id: "c7dbc50b-9b25-5f54-9f06-fd56a3a45afe"
name: "Identify CLS causes using DevTools and Performance Observer"
description: "Systematic workflow for selecting and navigating dashboard views to inspect agent execution, span relationships, and LLM interactions. Enables review of session performance across Timeline, Tree, Message, and Analytics modes."
version: "0.1.0"
tags:
  - "agent_debugging"
  - "dashboard_navigation"
  - "performance_analysis"
  - "session_review"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "CLS regression suspected in production or staging"
  - "Baseline CLS score needs investigation"
  - "User reports visual instability during page interaction"
  - "Performance audit reveals elevated CLS metric"
---

# Identify CLS causes using DevTools and Performance Observer

Systematic workflow for selecting and navigating dashboard views to inspect agent execution, span relationships, and LLM interactions. Enables review of session performance across Timeline, Tree, Message, and Analytics modes.

## Prompt

When debugging agent behavior or reviewing session performance, identify your debugging intent (e.g., trace execution flow, inspect LLM prompts, compare metrics). Select the corresponding dashboard view: Timeline View for chronological span display, Tree View for parent-child relationships, Message View for LLM interaction details, or Analytics for aggregated metrics. Navigate to the selected view and extract the required insight.

## Objective

Enable practitioner to systematically inspect agent performance across multiple visualization modes
## Applicable Signals

- Session performance review initiated
- Debugging intent identified (execution flow, latency, prompt content, or metrics comparison)

## Contraindications

- Real-time agent control or intervention is required
- This is inspection-only; not suitable for execution control or live intervention

## Workflow Steps

- {'step': 1, 'action': 'Identify debugging intent', 'detail': 'Determine what aspect of agent performance requires inspection (execution flow, span duration, LLM interaction, or cross-session metrics)'}
- {'step': 2, 'action': 'Select appropriate view', 'detail': 'Route to Timeline View (chronological spans), Tree View (hierarchical relationships), Message View (LLM details), or Analytics (aggregated metrics)'}
- {'step': 3, 'action': 'Navigate and inspect', 'detail': 'Access the selected dashboard view and locate the relevant performance data'}
- {'step': 4, 'action': 'Extract insight', 'detail': 'Identify the required performance insight (e.g., slow span, prompt content, session comparison)'}

## Constraints

- Dashboard views are read-only inspection tools
- View selection must align with debugging intent

## Cautions

- Dashboard views provide inspection only; they do not control agent execution
- Ensure view selection matches the debugging question being asked

## Output Contract

- Practitioner has navigated to the appropriate dashboard view and extracted the required performance insight (e.g., identified slow span, reviewed prompt content, or compared session metrics)

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- CLS regression suspected in production or staging
- Baseline CLS score needs investigation
- User reports visual instability during page interaction
- Performance audit reveals elevated CLS metric

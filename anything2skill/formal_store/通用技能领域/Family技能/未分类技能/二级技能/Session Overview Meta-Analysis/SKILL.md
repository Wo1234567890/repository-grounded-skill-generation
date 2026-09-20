---
id: "9fbec445-9be1-57ea-823e-bc232cb5bbd6"
name: "Session Overview Meta-Analysis"
description: "Aggregate and display summary statistics and trends across all recorded sessions in a single consolidated view for high-level performance and behavior pattern analysis."
version: "0.1.0"
tags:
  - "debugging"
  - "session_analysis"
  - "aggregation"
  - "reporting"
  - "cross_session"
  - "performance_review"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "User requests trend analysis across multiple agent runs"
  - "User wants to compare performance metrics between sessions"
  - "User seeks high-level overview of overall agent behavior patterns"
---

# Session Overview Meta-Analysis

Aggregate and display summary statistics and trends across all recorded sessions in a single consolidated view for high-level performance and behavior pattern analysis.

## Prompt

Retrieve all recorded sessions and compute cross-session metrics including execution time distributions, event type frequencies, error rates, and performance trends. Present aggregated data in a unified dashboard that enables comparison of agent behavior patterns across multiple runs without requiring drill-down into individual session details.

## Objective

analyze_cross_session_patterns
## Applicable Signals

- user_intent: identify_trends
- user_intent: compare_performance
- user_intent: assess_overall_patterns
- context: multiple_sessions_available

## Contraindications

- User is investigating a specific session incident
- User needs granular event-level or prompt-completion details
- User requires drill-down into individual LLM calls or tool execution

## Workflow Steps

- Retrieve metadata and summary statistics for all recorded sessions
- Compute cross-session metrics: total execution time, event type distribution, error frequency, success rates
- Identify trends and patterns in agent behavior across runs
- Render aggregated metrics and comparative visualizations in a single consolidated dashboard

## Constraints

- Requires at least two recorded sessions to generate meaningful comparative statistics
- Aggregation must preserve session isolation; do not merge event sequences across sessions

## Output Contract

- Meta-analysis dashboard displaying aggregated metrics, trends, and comparative statistics across all sessions
- User can identify performance patterns and behavioral trends without navigating individual session details

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- User requests trend analysis across multiple agent runs
- User wants to compare performance metrics between sessions
- User seeks high-level overview of overall agent behavior patterns

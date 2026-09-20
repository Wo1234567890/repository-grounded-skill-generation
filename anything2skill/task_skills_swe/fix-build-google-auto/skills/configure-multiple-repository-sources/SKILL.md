---
id: "1abf2070-8099-5772-97e2-faec712dfda8"
name: "Configure Multiple Repository Sources"
description: "Workflow for selecting and navigating multiple dashboard views to analyze agent execution and performance metrics. Enables inspection of session behavior, execution flow tracing, and LLM interaction review across single or multiple sessions."
version: "0.1.1"
tags:
  - "agent_monitoring"
  - "dashboard"
  - "performance_analysis"
  - "session_inspection"
  - "execution_tracing"
triggers:
  - "Multiple artifact sources required"
  - "Repository failover or load distribution needed"
  - "Mirror or proxy configuration required"
  - "Project dependencies span multiple remote repositories"
examples:
  - input: "Inspect execution flow of a single agent session"
    output: "Timeline View displays chronological spans with duration and parent-child relationships"
    notes: "Use Timeline View when tracing sequential execution order is primary goal"
  - input: "Review LLM prompts and completions for a session"
    output: "Message View displays detailed LLM interactions with prompt and completion content"
    notes: "Use Message View for debugging LLM behavior or understanding model interactions"
  - input: "Compare performance metrics across multiple sessions"
    output: "Analytics view displays aggregated metrics across sessions and operations"
    notes: "Use Analytics for trend analysis and cross-session performance comparison"
---

# Configure Multiple Repository Sources

Workflow for selecting and navigating multiple dashboard views to analyze agent execution and performance metrics. Enables inspection of session behavior, execution flow tracing, and LLM interaction review across single or multiple sessions.

## Prompt

Select the appropriate dashboard view based on analysis goal: use Session List for session overview and filtering, Timeline View for chronological span display, Tree View for hierarchical parent-child relationships, Message View for detailed LLM prompt and completion content, or Analytics for aggregated cross-session metrics. Navigate to the selected view and display relevant performance data.

## Objective

Navigate agent performance dashboards to analyze execution and performance metrics
## Applicable Signals

- Agent execution completed
- Session data available
- Performance analysis requested
- Debugging or optimization phase initiated

## Contraindications

- Real-time agent control required
- Agent configuration modification needed
- Write operations on agent state required

## Workflow Steps

- {'step': 1, 'action': 'Determine analysis objective', 'detail': 'Identify what aspect of agent performance needs inspection: overview, chronology, hierarchy, message details, or aggregated metrics.'}
- {'step': 2, 'action': 'Select appropriate dashboard view', 'detail': 'Route to Session List (overview and filtering), Timeline View (chronological spans), Tree View (hierarchical relationships), Message View (LLM interactions), or Analytics (aggregated metrics).'}
- {'step': 3, 'action': 'Apply filters or navigation parameters', 'detail': 'Configure view-specific filters, time ranges, or session selections as needed.'}
- {'step': 4, 'action': 'Display and interpret performance data', 'detail': 'Render the selected view and present relevant execution traces, metrics, or interaction details to the caller.'}

## Constraints

- Read-only analysis workflow
- Requires completed or in-progress session data
- Dashboard views must be available in the AgentOps platform

## Cautions

- This skill provides visualization and analysis only; it does not modify agent behavior or configuration.
- Large session datasets may require filtering or pagination in Session List view.

## Output Contract

- Caller receives the selected dashboard view with relevant performance data, execution traces, or metrics displayed. Output includes session overview, chronological or hierarchical span relationships, LLM interaction details, or aggregated performance metrics depending on view selection.

## Example Executions

### Example 1

- Input: Inspect execution flow of a single agent session
- Output: Timeline View displays chronological spans with duration and parent-child relationships
- Notes: Use Timeline View when tracing sequential execution order is primary goal

### Example 2

- Input: Review LLM prompts and completions for a session
- Output: Message View displays detailed LLM interactions with prompt and completion content
- Notes: Use Message View for debugging LLM behavior or understanding model interactions

### Example 3

- Input: Compare performance metrics across multiple sessions
- Output: Analytics view displays aggregated metrics across sessions and operations
- Notes: Use Analytics for trend analysis and cross-session performance comparison

## Triggers

- Multiple artifact sources required
- Repository failover or load distribution needed
- Mirror or proxy configuration required
- Project dependencies span multiple remote repositories

## Examples

### Example 1

Input:

  Inspect execution flow of a single agent session

Output:

  Timeline View displays chronological spans with duration and parent-child relationships

Notes:

  Use Timeline View when tracing sequential execution order is primary goal

### Example 2

Input:

  Review LLM prompts and completions for a session

Output:

  Message View displays detailed LLM interactions with prompt and completion content

Notes:

  Use Message View for debugging LLM behavior or understanding model interactions

### Example 3

Input:

  Compare performance metrics across multiple sessions

Output:

  Analytics view displays aggregated metrics across sessions and operations

Notes:

  Use Analytics for trend analysis and cross-session performance comparison

---
id: "fb8ebdf4-e71c-5087-8a57-7bcf85d7244c"
name: "Stream Event Processing for Agent Output"
description: "Iterate over agent event streams, filter by event type, and output text-generation events in real-time. Use when consuming streaming responses from agent frameworks that emit structured event objects."
version: "0.1.0"
tags:
  - "streaming"
  - "event-processing"
  - "agent-output"
  - "real-time"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Agent framework returns streaming event objects"
  - "Real-time output display is required"
  - "Event objects have event_type and text attributes"
examples:
  - input: "stream object from agent framework with events: [Event(event_type='text-generation', text='Hello'), Event(event_type='metadata', text='...'), Event(event_type='text-generation', text=' World')]"
    output: "Hello World (printed to stdout without newlines between segments)"
    notes: "Non-text-generation events are filtered out; text segments are concatenated in real-time"
---

# Stream Event Processing for Agent Output

Iterate over agent event streams, filter by event type, and output text-generation events in real-time. Use when consuming streaming responses from agent frameworks that emit structured event objects.

## Prompt

Iterate over the event stream. For each event, check if event.event_type equals 'text-generation'. If true, extract and output event.text without adding newlines (use end='' or equivalent). Continue until stream is exhausted.

## Objective

Process and display streamed text-generation events from agent execution
## Applicable Signals

- stream object available from agent execution
- event.event_type attribute present
- event.text attribute present

## Contraindications

- Batch processing is preferred over streaming
- Event stream is not available or is None
- Output buffering or aggregation is required before display

## Workflow Steps

- Receive or obtain the event stream from agent framework
- Iterate over stream using for-loop or equivalent
- Check event.event_type == 'text-generation' for each event
- Extract event.text when condition is true
- Output text without line termination (end='' or equivalent)
- Continue until stream is exhausted

## Constraints

- Event stream must be iterable
- Each event must have event_type and text attributes
- Output must not block stream consumption

## Cautions

- Ensure stream is properly closed or exhausted to avoid resource leaks
- Handle empty or malformed event.text gracefully

## Output Contract

- Text content from text-generation events is printed or collected in real-time without blocking stream consumption. Non-text-generation events are silently skipped.

## Example Executions

### Example 1

- Input: stream object from agent framework with events: [Event(event_type='text-generation', text='Hello'), Event(event_type='metadata', text='...'), Event(event_type='text-generation', text=' World')]
- Output: Hello World (printed to stdout without newlines between segments)
- Notes: Non-text-generation events are filtered out; text segments are concatenated in real-time

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Agent framework returns streaming event objects
- Real-time output display is required
- Event objects have event_type and text attributes

## Examples

### Example 1

Input:

  stream object from agent framework with events: [Event(event_type='text-generation', text='Hello'), Event(event_type='metadata', text='...'), Event(event_type='text-generation', text=' World')]

Output:

  Hello World (printed to stdout without newlines between segments)

Notes:

  Non-text-generation events are filtered out; text segments are concatenated in real-time

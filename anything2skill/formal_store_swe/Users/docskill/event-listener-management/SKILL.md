---
id: "8ab7d9c6-0610-506d-b327-c9d8908c0519"
name: "Event listener management"
description: "Collect and buffer streamed event data from an LLM response, checking for completion signals and concatenating text chunks until the stream terminates."
version: "0.1.1"
tags:
  - "streaming"
  - "llm_integration"
  - "response_handling"
  - "event_processing"
  - "buffer_aggregation"
triggers:
  - "Interactive element requires event response"
  - "User interaction must trigger a callback"
---

# Event listener management

Collect and buffer streamed event data from an LLM response, checking for completion signals and concatenating text chunks until the stream terminates.

## Prompt

Iterate over incoming stream events. For each event, check if finish_reason equals 'stop'. If stop signal is detected, print the aggregated response and exit the loop. Otherwise, append the event text to the response buffer. Continue until stream is exhausted.

## Objective

Aggregate streamed LLM output into a complete response
## Applicable Signals

- event.data.choices[0].finish_reason available in stream
- event.text contains partial response content
- Stream iteration protocol supported by caller

## Contraindications

- Using non-streaming or batch API responses
- Response data already fully buffered in memory
- Synchronous single-response APIs without event iteration

## Workflow Steps

- Initialize empty response buffer
- Begin iteration over message stream
- For each event, check event.data.choices[0].finish_reason
- If finish_reason == 'stop', print response and break
- Otherwise, concatenate event.text to response buffer
- Continue until stream exhausted

## Constraints

- finish_reason must be accessible at event.data.choices[0].finish_reason
- event.text must contain the text chunk to append
- Stream must be iterable and terminate cleanly

## Cautions

- Ensure event structure matches expected schema before accessing nested fields
- Handle potential None or missing finish_reason gracefully
- Verify stream iteration does not raise exceptions on termination

## Output Contract

- Complete aggregated response string printed to output; stream fully consumed and finish_reason == 'stop' confirmed.

## Triggers

- Interactive element requires event response
- User interaction must trigger a callback

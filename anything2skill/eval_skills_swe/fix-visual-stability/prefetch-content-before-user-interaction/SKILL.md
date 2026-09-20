---
id: "97f51c7d-46d0-51ce-aae0-119942df443e"
name: "Prefetch Content Before User Interaction"
description: "Load new content in the background before the user initiates a load action, so it displays immediately when requested without perceived delay or layout shift penalty."
version: "0.1.0"
tags:
  - "performance"
  - "layout_shift"
  - "CLS"
  - "prefetch"
  - "content_loading"
  - "user_experience"
triggers:
  - "User-initiated load button or refresh action is present in the interface"
  - "Content to be loaded can be predicted or anticipated"
  - "Load action is expected within a predictable timeframe"
examples:
  - input: "User hovers over or focuses on a 'Load more' button; next page of products is predictable"
    output: "Next batch of product data is prefetched and cached; when user clicks 'Load more', products appear immediately without network latency"
    notes: "Prefetch triggered on hover or focus to maximize time before click"
  - input: "Live feed with 'Refresh' button; new feed items can be anticipated"
    output: "New feed content is fetched in background before user clicks 'Refresh'; clicking 'Refresh' displays cached content instantly"
    notes: "Similar to Twitter live feed pattern; layout shifts within 500ms of user input do not count toward CLS"
---

# Prefetch Content Before User Interaction

Load new content in the background before the user initiates a load action, so it displays immediately when requested without perceived delay or layout shift penalty.

## Prompt

When a user-initiated load action (such as clicking 'Load more' or 'Refresh') is anticipated, prefetch the content in the background before the user interaction occurs. This ensures the content is available in memory or cache and can be displayed instantaneously upon user request. Layout shifts occurring within 500 milliseconds of user input are not counted toward CLS, but prefetching eliminates the shift entirely by having content ready.

## Objective

Reduce perceived latency and eliminate layout shifts by preloading content before user-triggered load events
## Applicable Signals

- Presence of 'Load more' or 'Refresh' button
- Predictable content patterns (e.g., pagination, feed updates)
- User interaction event listeners are registered

## Contraindications

- Content is unpredictable or cannot be anticipated
- Bandwidth is severely constrained or metered
- User has disabled prefetch or background loading in browser settings
- Network conditions are poor or unreliable

## Workflow Steps

- {'step': 1, 'action': 'Identify user-initiated load trigger points', 'detail': "Detect buttons, links, or controls that initiate content loading (e.g., 'Load more', 'Refresh')"}
- {'step': 2, 'action': 'Initiate background prefetch before user interaction', 'detail': 'Fetch and cache the next batch of content in the background using fetch, XMLHttpRequest, or service worker'}
- {'step': 3, 'action': 'Store prefetched content in accessible cache', 'detail': 'Place content in memory, IndexedDB, or service worker cache for immediate retrieval'}
- {'step': 4, 'action': 'Display content immediately upon user interaction', 'detail': 'When user clicks the load button, retrieve cached content and render without network delay'}
- {'step': 5, 'action': 'Verify no layout shift occurs', 'detail': 'Confirm that content insertion does not cause unexpected layout shifts; use fixed containers or carousels if needed'}

## Constraints

- Prefetch must complete before user interaction to provide instantaneous display
- Content must be stored in memory or cache accessible to the rendering engine
- Prefetch should not block or delay other critical page operations

## Cautions

- Prefetching unused content wastes bandwidth; only prefetch when user interaction is highly likely
- Monitor cache size to avoid memory exhaustion on resource-constrained devices
- Ensure prefetched content remains valid and does not become stale before user interaction

## Output Contract

- Content is available in memory or cache before user interaction
- Load appears instantaneous with no perceived delay
- Layout shifts within 500 milliseconds of user input are not counted toward CLS
- User experiences seamless content update without visual jank

## Example Executions

### Example 1

- Input: User hovers over or focuses on a 'Load more' button; next page of products is predictable
- Output: Next batch of product data is prefetched and cached; when user clicks 'Load more', products appear immediately without network latency
- Notes: Prefetch triggered on hover or focus to maximize time before click

### Example 2

- Input: Live feed with 'Refresh' button; new feed items can be anticipated
- Output: New feed content is fetched in background before user clicks 'Refresh'; clicking 'Refresh' displays cached content instantly
- Notes: Similar to Twitter live feed pattern; layout shifts within 500ms of user input do not count toward CLS

## Triggers

- User-initiated load button or refresh action is present in the interface
- Content to be loaded can be predicted or anticipated
- Load action is expected within a predictable timeframe

## Examples

### Example 1

Input:

  User hovers over or focuses on a 'Load more' button; next page of products is predictable

Output:

  Next batch of product data is prefetched and cached; when user clicks 'Load more', products appear immediately without network latency

Notes:

  Prefetch triggered on hover or focus to maximize time before click

### Example 2

Input:

  Live feed with 'Refresh' button; new feed items can be anticipated

Output:

  New feed content is fetched in background before user clicks 'Refresh'; clicking 'Refresh' displays cached content instantly

Notes:

  Similar to Twitter live feed pattern; layout shifts within 500ms of user input do not count toward CLS

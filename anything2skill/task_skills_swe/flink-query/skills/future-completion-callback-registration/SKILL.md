---
id: "e0543d5d-48b2-54e9-bd99-13af454968ef"
name: "Future Completion Callback Registration"
description: "Prevent cumulative layout shift by pre-allocating container space for dynamically loaded elements such as ads, embeds, or forms using min-height or explicit dimensions."
version: "0.1.2"
tags:
  - "layout_stability"
  - "cumulative_layout_shift"
  - "space_reservation"
  - "performance"
  - "web_vitals"
triggers:
  - "A parallel task is submitted and the caller needs to perform an action (e.g., log, update state, trigger next task) as soon as it completes, without waiting synchronously"
examples:
  - input: "Ad container that loads asynchronously after page render"
    output: "Container with min-height set to expected ad height; placeholder shown if ad fails to load; CLS reduced for that region"
    notes: "Prevents shift when ad loads or fails to load"
  - input: "Embed placeholder for third-party content"
    output: "Container with explicit width and height matching embed dimensions; placeholder visible until embed loads"
    notes: "Maintains space allocation throughout load lifecycle"
---

# Future Completion Callback Registration

Prevent cumulative layout shift by pre-allocating container space for dynamically loaded elements such as ads, embeds, or forms using min-height or explicit dimensions.

## Prompt

Set the initial container size to the smallest dimension that will be used, or use min-height to allow the parent element to grow as necessary. Show a placeholder if no content is returned, to avoid collapsing the reserved space. This reduces layout shift impact compared to leaving the container at 0px default size.

## Objective

Reduce layout shift impact from late-loaded content
## Applicable Signals

- Ad container or embed placeholder element is being added to the page
- Content will load dynamically after initial page render
- Container dimensions can be estimated or bounded

## Contraindications

- Content dimensions are truly unknown and cannot be estimated
- User interaction is required before content appears
- Space reservation would create excessive empty whitespace

## Intervention Moves

- Set min-height or explicit width/height on the container element
- Display a placeholder when no content is returned
- Avoid collapsing reserved space by removing the container

## Workflow Steps

- {'step': 1, 'action': 'Identify the container element for late-loading content', 'detail': 'Determine which element will hold ads, embeds, or dynamic forms'}
- {'step': 2, 'action': 'Set initial container size using min-height or explicit dimensions', 'detail': 'Use the smallest size that will accommodate the expected content, or set min-height to allow growth'}
- {'step': 3, 'action': 'Display a placeholder when content is unavailable', 'detail': 'Show a placeholder element to maintain reserved space if no ad or content is returned'}
- {'step': 4, 'action': 'Verify layout shift reduction', 'detail': 'Measure CLS for the container element to confirm the shift impact is reduced'}

## Constraints

- Container must have a measurable or estimable minimum dimension
- Placeholder must be shown to prevent space collapse
- Reserved space should not exceed reasonable viewport bounds

## Cautions

- Removing reserved space causes as much layout shift as inserting content
- Collapsing the container when content is unavailable negates the benefit

## Output Contract

- Container element with min-height or explicit width/height set; placeholder displayed when content is unavailable; measured reduction in cumulative layout shift for that element.

## Example Executions

### Example 1

- Input: Ad container that loads asynchronously after page render
- Output: Container with min-height set to expected ad height; placeholder shown if ad fails to load; CLS reduced for that region
- Notes: Prevents shift when ad loads or fails to load

### Example 2

- Input: Embed placeholder for third-party content
- Output: Container with explicit width and height matching embed dimensions; placeholder visible until embed loads
- Notes: Maintains space allocation throughout load lifecycle

## Triggers

- A parallel task is submitted and the caller needs to perform an action (e.g., log, update state, trigger next task) as soon as it completes, without waiting synchronously

## Examples

### Example 1

Input:

  Ad container that loads asynchronously after page render

Output:

  Container with min-height set to expected ad height; placeholder shown if ad fails to load; CLS reduced for that region

Notes:

  Prevents shift when ad loads or fails to load

### Example 2

Input:

  Embed placeholder for third-party content

Output:

  Container with explicit width and height matching embed dimensions; placeholder visible until embed loads

Notes:

  Maintains space allocation throughout load lifecycle

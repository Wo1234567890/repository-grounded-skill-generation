---
id: "fc39f0fb-79d3-5b44-97d4-583266e72630"
name: "Preemptive Abort Decision"
description: "Keep reserved container space visible with a placeholder element when late-loaded content is unavailable, preventing the reserved space from collapsing and causing secondary layout shifts."
version: "0.1.1"
tags:
  - "layout_stability"
  - "cumulative_layout_shift"
  - "placeholder_management"
  - "content_loading"
  - "web_performance"
triggers:
  - "Transaction enters validation phase"
  - "Transaction has non-empty read set"
  - "Write-set locking is about to occur"
examples:
  - input: "Transaction T with read set {tuple_x, tuple_y}; tuple_x.rts=100, tuple_y.rts=95; tuple_x.wts=100 (matches TS_word), tuple_y.wts=90 (does not match TS_word); approximate_timestamp=100"
    output: "Abort decision: true. Reason: tuple_y.rts (95) < approximate_timestamp (100) AND tuple_y.wts (90) ≠ latest_wts. No write-set locks acquired."
    notes: "Early abort prevents unnecessary lock acquisition and contention."
  - input: "Transaction T with read set {tuple_a}; tuple_a.rts=50; tuple_a.wts=50 (matches TS_word); approximate_timestamp=50"
    output: "Abort decision: false. Reason: validation condition not met (wts matches). Proceed to write-set locking and full validation."
    notes: "Transaction may succeed; full validation required."
---

# Preemptive Abort Decision

Keep reserved container space visible with a placeholder element when late-loaded content is unavailable, preventing the reserved space from collapsing and causing secondary layout shifts.

## Prompt

When a reserved space for late-loaded content (ads, embeds, dynamic elements) may remain empty, display a placeholder element (skeleton, loading indicator, or fallback) that maintains the container's dimensions. This prevents the reserved space from collapsing, which can trigger layout shifts equal in magnitude to inserting new content. Ensure the placeholder occupies the same space as the expected content.

## Objective

Prevent layout shift from reserved space collapse
## Applicable Signals

- Reserved container space is defined (via min-height, fixed height, or aspect-ratio)
- Content load may result in empty or null response
- Space collapse risk is identified during layout stability audit

## Contraindications

- Space reservation is not used or not applicable
- Content is guaranteed to always load successfully
- User experience requires immediate space reclamation when content unavailable
- Placeholder would obscure critical page content

## Intervention Moves

- Display placeholder element matching reserved container dimensions
- Replace placeholder with primary content upon successful load
- Retain placeholder if content load fails or times out

## Workflow Steps

- {'step': 1, 'action': 'Define reserved container with explicit dimensions (min-height, fixed height, or aspect-ratio CSS)', 'rationale': 'Establishes baseline space allocation independent of content availability'}
- {'step': 2, 'action': 'Create placeholder element with matching dimensions', 'rationale': 'Ensures space does not collapse when primary content is unavailable'}
- {'step': 3, 'action': 'Display placeholder on page load or when content fetch begins', 'rationale': 'Maintains visual stability during content loading phase'}
- {'step': 4, 'action': 'Replace placeholder with primary content when load completes, or keep placeholder visible if load fails', 'rationale': 'Prevents secondary layout shift from space collapse'}

## Constraints

- Placeholder must occupy identical dimensions as reserved space
- Placeholder must remain visible until primary content loads or timeout occurs
- Placeholder styling must not introduce additional layout shifts

## Cautions

- Placeholder visibility duration should be monitored; prolonged empty states may degrade user experience
- Ensure placeholder is semantically appropriate (e.g., skeleton screen for images, loading spinner for dynamic content)

## Output Contract

- Placeholder element (skeleton, loading indicator, or fallback) maintains container dimensions when primary content is unavailable; no secondary cumulative layout shift (CLS) occurs from space collapse; reserved space remains visually stable throughout content lifecycle.

## Triggers

- Transaction enters validation phase
- Transaction has non-empty read set
- Write-set locking is about to occur

## Examples

### Example 1

Input:

  Transaction T with read set {tuple_x, tuple_y}; tuple_x.rts=100, tuple_y.rts=95; tuple_x.wts=100 (matches TS_word), tuple_y.wts=90 (does not match TS_word); approximate_timestamp=100

Output:

  Abort decision: true. Reason: tuple_y.rts (95) < approximate_timestamp (100) AND tuple_y.wts (90) ≠ latest_wts. No write-set locks acquired.

Notes:

  Early abort prevents unnecessary lock acquisition and contention.

### Example 2

Input:

  Transaction T with read set {tuple_a}; tuple_a.rts=50; tuple_a.wts=50 (matches TS_word); approximate_timestamp=50

Output:

  Abort decision: false. Reason: validation condition not met (wts matches). Proceed to write-set locking and full validation.

Notes:

  Transaction may succeed; full validation required.

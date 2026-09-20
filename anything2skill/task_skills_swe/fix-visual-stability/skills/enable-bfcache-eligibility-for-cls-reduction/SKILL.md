---
id: "9c6166af-7cdc-5ca7-aee4-7abf58704f08"
name: "Enable bfcache eligibility for CLS reduction"
description: "Validate and configure web pages to be eligible for browser back/forward cache (bfcache) to prevent layout shifts during navigation restoration and keep Cumulative Layout Shift scores low."
version: "0.1.0"
tags:
  - "web_performance"
  - "layout_shift"
  - "browser_cache"
  - "bfcache"
  - "CLS_optimization"
triggers:
  - "Optimizing Cumulative Layout Shift (CLS) scores"
  - "Preparing pages for back/forward navigation performance"
  - "Targeting instant page restoration without reflow"
---

# Enable bfcache eligibility for CLS reduction

Validate and configure web pages to be eligible for browser back/forward cache (bfcache) to prevent layout shifts during navigation restoration and keep Cumulative Layout Shift scores low.

## Prompt

To enable bfcache eligibility: (1) Audit your page for bfcache-blocking features such as unresolved promises, open connections, or certain API usage patterns. (2) Remove or refactor blocking code. (3) Verify that the page state is preserved in memory without requiring dynamic refresh on back/forward navigation. (4) Test navigation cycles to confirm instant restoration without reflow or layout shifts.

## Objective

Ensure pages are bfcache-eligible to eliminate layout shifts on back/forward navigation
## Applicable Signals

- CLS metric is a performance optimization target
- Navigation patterns include back/forward user actions
- Page load involves potential layout reflow

## Contraindications

- Pages require dynamic state refresh on navigation
- bfcache is explicitly disabled by application requirements
- CLS is not a performance metric of concern

## Intervention Moves

- Audit page for bfcache-blocking features
- Refactor or remove blocking code patterns
- Preserve page state in memory across navigation
- Test back/forward navigation cycles

## Workflow Steps

- {'step': 1, 'action': 'Audit page for bfcache-blocking features', 'details': 'Check for unresolved promises, open connections, or API usage patterns that prevent bfcache eligibility'}
- {'step': 2, 'action': 'Refactor blocking code', 'details': 'Remove or refactor code that blocks bfcache eligibility'}
- {'step': 3, 'action': 'Verify state preservation', 'details': 'Confirm that page state is preserved in memory without requiring dynamic refresh on back/forward navigation'}
- {'step': 4, 'action': 'Test navigation cycles', 'details': 'Perform back/forward navigation tests to confirm instant restoration without reflow or layout shifts'}

## Constraints

- Page must not use APIs or patterns that block bfcache eligibility
- State preservation must not depend on server-side refresh
- Navigation restoration must occur without triggering layout recalculation

## Cautions

- Verify bfcache eligibility across target browsers before deployment
- Monitor CLS scores across multiple navigation cycles to confirm stability

## Output Contract

- Page is bfcache-eligible; back/forward navigation restores page state instantly without layout shifts; CLS score remains stable across navigation cycles.

## Triggers

- Optimizing Cumulative Layout Shift (CLS) scores
- Preparing pages for back/forward navigation performance
- Targeting instant page restoration without reflow

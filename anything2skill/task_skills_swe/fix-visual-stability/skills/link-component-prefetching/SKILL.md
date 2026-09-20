---
id: "0a3e55ab-5645-5ce1-bea7-ad5c4fbf07a9"
name: "Link Component Prefetching"
description: "Use Next.js Link component to prefetch linked pages in the background for faster page transitions. Apply when navigating between internal pages to improve perceived performance and user experience."
version: "0.1.0"
tags:
  - "next.js"
  - "navigation"
  - "performance"
  - "prefetching"
  - "ui-optimization"
triggers:
  - "implementing internal page navigation"
  - "want smoother page transitions"
  - "need to reduce perceived latency between routes"
---

# Link Component Prefetching

Use Next.js Link component to prefetch linked pages in the background for faster page transitions. Apply when navigating between internal pages to improve perceived performance and user experience.

## Prompt

Invoke the Link component for internal page navigation. The component automatically prefetches the target page in the background, reducing perceived latency on transition. Ensure the href points to an internal route; external links should use standard <a> tags instead.

## Objective

accelerate page navigation through background prefetching
## Applicable Signals

- internal route navigation required
- user experience latency concerns
- multi-page application structure

## Contraindications

- linking to external domains
- prefetching would consume unnecessary bandwidth
- user is on slow or metered connection

## Intervention Moves

- replace native <a> tags with Next.js Link component for internal routes
- configure href attribute to target internal page path
- allow component to handle prefetching automatically

## Constraints

- Link component must wrap internal routes only
- href must point to valid internal page path
- prefetching occurs automatically; no manual configuration required

## Cautions

- External links should use standard <a> tags to avoid prefetch overhead
- Consider user bandwidth constraints before enabling prefetching at scale

## Output Contract

- Linked pages prefetch in background; page transitions appear instantaneous or near-instantaneous to user

## Triggers

- implementing internal page navigation
- want smoother page transitions
- need to reduce perceived latency between routes

---
id: "0206e659-bf77-5deb-8fb3-c028f46014de"
name: "Link Prefetching Strategy"
description: "Prefetch linked pages in the background to enable faster and smoother page transitions. Use when implementing internal page links to reduce perceived latency during navigation."
version: "0.1.0"
tags:
  - "navigation"
  - "performance"
  - "prefetching"
  - "ui_optimization"
  - "component_abstraction"
triggers:
  - "User implements internal page links in single-page or multi-page application"
  - "Goal is to reduce perceived latency on page transitions"
  - "Navigation between application pages is frequent"
---

# Link Prefetching Strategy

Prefetch linked pages in the background to enable faster and smoother page transitions. Use when implementing internal page links to reduce perceived latency during navigation.

## Prompt

When a user hovers over or focuses on an internal link, prefetch the target page's resources in the background. This allows the page transition to complete without visible loading delay when the user clicks. Do not prefetch external links or heavy resources in bandwidth-constrained environments.

## Objective

accelerate_navigation
## Applicable Signals

- Internal link element detected
- Page transition latency is a performance concern
- User interaction with link is imminent

## Contraindications

- External links to third-party domains
- Links to heavy resources that should not be preloaded
- Bandwidth-constrained or metered network environments
- User has disabled prefetching preferences

## Intervention Moves

- Configure Link component to prefetch target page resources
- Trigger prefetch on user hover or focus event

## Workflow Steps

- Identify internal navigation links in the application
- Configure Link component to prefetch target page resources
- Trigger prefetch on user hover or focus event
- Complete page transition on user click without additional loading

## Constraints

- Only prefetch internal links within the application
- Respect user network conditions and data-saver preferences
- Do not prefetch resources that are not necessary for immediate page load

## Cautions

- Excessive prefetching may consume unnecessary bandwidth
- Monitor prefetch success rate to avoid wasted resources

## Output Contract

- Target page resources are prefetched before user click; page transition completes without visible loading delay.

## Triggers

- User implements internal page links in single-page or multi-page application
- Goal is to reduce perceived latency on page transitions
- Navigation between application pages is frequent

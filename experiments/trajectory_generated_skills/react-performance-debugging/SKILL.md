---
name: nextjs-performance-debugging
description: Diagnose and optimize React/Next.js performance across server data fetching, API routes, bundle size, and component rerendering without breaking functional selectors.
---

# React and Next.js Performance Debugging

## When to Use

Use this skill when a Next.js application is functionally correct but slow during page load, cart/interaction updates, expensive comparison views, or API requests.

## Workflow

1. **Establish a before measurement.** Use the browser, server logs, build output, or timing instrumentation to identify which user path is slow. Do not optimize only from visual inspection of source.
2. **Separate server/API latency from client rendering cost.** Trace slow paths through page data fetches, route handlers, component render trees, and imported bundles.
3. **Parallelize independent I/O.** If server-side or route-handler requests do not depend on one another, issue them concurrently and await them together. Preserve error handling and required ordering for dependent calls.
4. **Reduce repeated render-time scans.** If each rendered card filters the same reviews or metadata array, precompute a lookup map once and reuse O(1) lookups.
5. **Memoize at stable boundaries.** Use component memoization only when props can remain stable; combine it with memoized derived data/callbacks where needed. Memoization is not a substitute for removing expensive work.
6. **Delay heavy optional code.** Advanced-analysis libraries or components should be dynamically imported when the user actually opens that feature, rather than inflating the initial route bundle.
7. **Keep non-critical work off the response critical path.** Logging or analytics that does not affect the response should not serially block a latency-sensitive API path.
8. **Preserve observable behavior.** Keep required `data-testid` values, required components, and existing `performance.mark()` instrumentation. Verify homepage data, cart behavior, and advanced compare content after every optimization batch.

## Verification

Rebuild the app, compare route/bundle output, and exercise the exact slow scenarios. A no-skill trajectory identified plausible code-level bottlenecks but still received no task credit, so source-level plausibility alone is insufficient; verify actual rendered behavior and timing.

## Common Failure Modes

- Optimizing many files at once without a measured bottleneck.
- Lazy-loading code but accidentally removing the tested advanced content.
- Adding `React.memo` while passing freshly created props every render.
- Parallelizing calls that actually have data dependencies.
- Claiming performance improvement from code patterns without measuring the target scenario.

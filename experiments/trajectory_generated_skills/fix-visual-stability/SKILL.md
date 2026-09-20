---
name: nextjs-visual-stability
description: Diagnose and repair layout shifts, flicker, hydration flashes, and unstable loading states in React and Next.js interfaces while preserving tested DOM contracts.
---

# Next.js Visual Stability Repair

## When to Use

Use this skill for React/Next.js pages with visible layout shifts or flicker during hydration, asynchronous data loading, image loading, pagination, or conditional rendering.

## Workflow

1. **Preserve the DOM contract first.** Record class names, ids, and `data-testid` attributes that tests may depend on. Do not rename or remove them while optimizing layout.
2. **Observe the unstable states.** Run the app with its backing API, inspect the page before and after data arrives, and use browser automation or screenshots when available. Do not rely only on static source inspection.
3. **Reserve space for asynchronous content.** If a banner, side panel, results bar, or similar component returns `null` before data arrives, keep a stable container or placeholder with dimensions close to the final content.
4. **Make loading geometry resemble final geometry.** Skeletons should match the eventual grid/card dimensions instead of replacing a large region with one short "loading" line.
5. **Stabilize media dimensions.** Give product/media regions a predictable aspect ratio or dimensions and use an appropriate fitting rule so image decode does not resize surrounding layout.
6. **Handle hydration-sensitive state deliberately.** Theme or client-storage state can cause first-render flashes. Separate server-safe initial markup from client initialization and use hydration suppression only where the mismatch is intentional and understood.
7. **Prevent viewport-width jumps.** When content length changes whether a scrollbar appears, reserve scrollbar space when appropriate.
8. **Validate interactions after visual fixes.** Re-check theme switching, pagination, data loading, and any conditional controls. A stable placeholder is not acceptable if it blocks the real interaction.

## Verification

Verify both source-level invariants and rendered behavior. Check that required selectors remain unchanged, layout-reservation classes reach the built CSS, images have stable geometry, and the page still loads actual products and interactive controls.

## Common Failure Modes

- Declaring success because stability-related CSS exists without measuring the rendered page.
- Removing conditionally rendered components instead of reserving their space.
- Adding placeholders whose size does not match the final content.
- Masking hydration problems broadly rather than isolating the state causing the flash.

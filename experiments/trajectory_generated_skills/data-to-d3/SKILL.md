---
name: d3-interactive-stock-visualization
description: Build a self-contained D3 v6 single-page visualization with force-clustered bubbles, a linked data table, robust CSV parsing, and offline-friendly assets.
---

# D3 Interactive Bubble Chart and Linked Table

## When to Use

Use this skill when converting tabular entity data into a browser-openable D3 page that combines a force-layout chart with a synchronized table.

## Workflow

1. **Inspect the data before designing scales.** Count rows, identify missing fields, and confirm CSV quoting. Long text fields may contain embedded newlines, so never parse CSV by simply splitting on newline and comma.
2. **Create the required self-contained file layout.** Keep HTML, CSS, JavaScript, the requested D3 v6 asset, and copied input data under the output directory using relative paths that work from a local HTTP server.
3. **Normalize entities once.** Parse market capitalization into a numeric value, preserve ticker/name/sector strings, and explicitly mark rows such as ETFs that lack fields used by stock-specific encodings.
4. **Build a force simulation for the bubbles.** Map each sector to a nearby cluster center, pull nodes toward that center with `forceX`/`forceY`, and use collision force to prevent overlap. Keep cluster centers compact enough that the chart reads as one visualization.
5. **Encode size and color consistently.** Scale radius by market capitalization for ordinary stocks; use a stable fallback size for entities without market-cap data. Use one sector color mapping for bubbles and the legend.
6. **Label and tooltip carefully.** Put ticker text inside bubbles. Show tooltips only when the required descriptive fields are available.
7. **Render the table from the same normalized data.** Format large market-cap numbers compactly and keep all requested columns.
8. **Use one shared selection state.** Clicking either a bubble or a table row should update both visual representations, including row highlight and bubble selection state.
9. **Verify in a real browser.** Serve the output directory, check that D3 and data files load, inspect the DOM, and exercise both directions of the linked interaction.

## Trajectory-Derived Caution

The no-skill runs repeatedly encountered CSV parsing issues from quoted multi-line descriptions. Use a standards-compliant CSV parser (including D3's CSV facilities) or an equivalent parser that preserves quoted newlines. A file-layout check alone is not enough to prove the visualization renders correctly.

## Common Failure Modes

- Hand-parsing CSV line-by-line.
- Using separate selection logic for chart and table so they drift out of sync.
- Letting missing market-cap values produce `NaN` radii.
- Loading D3 from a network URL when evaluation expects the local asset.

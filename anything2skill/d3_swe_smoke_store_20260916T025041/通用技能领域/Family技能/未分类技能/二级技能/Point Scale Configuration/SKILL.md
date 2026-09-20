---
id: "2a9692d5-e0f3-5cc4-bc50-d8604c23fd8f"
name: "Point Scale Configuration"
description: "Configure and apply ordinal point scales for mapping categorical or ordinal domain values to evenly-spaced visual positions with optional padding, rounding, and alignment control."
version: "0.1.0"
tags:
  - "d3"
  - "scale"
  - "ordinal"
  - "point-scale"
  - "visualization"
  - "axis"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Need to map categorical or ordinal data to evenly-spaced visual positions"
  - "Creating axis labels or discrete point layouts"
---

# Point Scale Configuration

Configure and apply ordinal point scales for mapping categorical or ordinal domain values to evenly-spaced visual positions with optional padding, rounding, and alignment control.

## Prompt

Create a point scale by: (1) instantiate d3.scalePoint(), (2) set domain with categorical values, (3) set output range [min, max], (4) optionally enable rounding via rangeRound() or round(), (5) optionally set padding outside first and last point, (6) optionally set alignment for extra space, (7) query step distance between adjacent points if needed, (8) copy scale if reuse required.

## Objective

Set up a point scale with domain, range, and layout parameters for discrete ordinal positioning
## Applicable Signals

- Need to map categorical or ordinal data to evenly-spaced visual positions
- Creating axis labels or discrete point layouts
- Positioning marks at uniform intervals along an axis

## Contraindications

- Continuous numeric scales required
- Non-uniform spacing needed
- Data is already pre-positioned
- Bandwidth or area allocation required (use band scale instead)

## Workflow Steps

- {'step': 1, 'action': 'Instantiate scale', 'detail': 'Create a new point scale using d3.scalePoint()'}
- {'step': 2, 'action': 'Set domain', 'detail': 'Call point.domain([values]) with array of categorical or ordinal values'}
- {'step': 3, 'action': 'Set output range', 'detail': 'Call point.range([min, max]) or point.rangeRound([min, max]) to define pixel or coordinate bounds'}
- {'step': 4, 'action': 'Configure padding (optional)', 'detail': 'Call point.padding(value) to set space outside first and last point; value in [0, 1]'}
- {'step': 5, 'action': 'Configure alignment (optional)', 'detail': 'Call point.align(value) to control point alignment when extra space exists; value in [0, 1]'}
- {'step': 6, 'action': 'Enable rounding (optional)', 'detail': 'Call point.round(true) or use point.rangeRound() to snap positions to integer pixels'}
- {'step': 7, 'action': 'Query scale properties (optional)', 'detail': 'Call point.step() to get distance between adjacent point starts; point.bandwidth() returns 0'}
- {'step': 8, 'action': 'Reuse scale (optional)', 'detail': 'Call point.copy() to create independent copy for parallel use'}

## Constraints

- Domain must be an array of distinct categorical or ordinal values
- Range must be a two-element array [min, max]
- Padding value must be in range [0, 1]
- Alignment value must be in range [0, 1]
- Point scale always returns bandwidth of zero (no area allocation)

## Cautions

- Changing domain or range after scale creation invalidates cached step distance
- Padding and alignment interact; test visual output with expected data cardinality
- Round mode affects pixel-perfect positioning; verify rendering on target display

## Output Contract

- Returns a configured scale function that accepts a domain value and returns its corresponding point position (number). Scale object exposes methods: domain(), range(), rangeRound(), round(), padding(), align(), bandwidth(), step(), copy().

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need to map categorical or ordinal data to evenly-spaced visual positions
- Creating axis labels or discrete point layouts

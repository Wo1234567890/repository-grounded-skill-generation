---
id: "4b4f8703-5d47-55ac-b24e-68ee06c335cd"
name: "ColorBrewer Diverging Palette Selection"
description: "Select and apply ColorBrewer diverging color schemes for visualizations encoding data with two opposing extremes and a meaningful midpoint. Diverging palettes (BrBG, PiYG, PRGn, PuOr, RdBu, RdGy, RdYlBu, RdYlGn, Spectral) are semantically distinct from sequential and categorical schemes."
version: "0.1.0"
tags:
  - "color_scheme"
  - "d3_interpolate"
  - "colorbrewer"
  - "diverging_palette"
  - "visualization_design"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Encoding data with a meaningful neutral midpoint"
  - "Visualizing opposing or contrasting data extremes"
  - "Selecting color scheme for diverging phenomena (anomalies, deviations, political/economic spectra)"
examples:
  - input: "Temperature anomaly data ranging from -5°C to +5°C with 0°C as neutral"
    output: "d3.interpolateRdBu or d3.schemeRdBu applied; red for positive anomalies, blue for negative, white/neutral at center"
    notes: "RdBu (Red-Blue) is semantically appropriate for temperature divergence"
  - input: "Political voting data with left/right spectrum and center as balanced"
    output: "d3.interpolatePRGn or d3.schemePRGn applied; purple for left, green for right, neutral center"
    notes: "PRGn (Purple-Green) provides clear visual separation for opposing political positions"
---

# ColorBrewer Diverging Palette Selection

Select and apply ColorBrewer diverging color schemes for visualizations encoding data with two opposing extremes and a meaningful midpoint. Diverging palettes (BrBG, PiYG, PRGn, PuOr, RdBu, RdGy, RdYlBu, RdYlGn, Spectral) are semantically distinct from sequential and categorical schemes.

## Prompt

When visualizing data with a meaningful center point and contrasting high/low values (e.g., temperature anomalies, political spectrum, profit/loss), select the appropriate ColorBrewer diverging palette. Use d3.interpolate* functions for continuous scales or d3.scheme* for discrete color arrays. Verify the palette name matches the semantic intent of your data.

## Objective

Provide reusable reference to diverging color interpolators and schemes for two-sided data encoding
## Applicable Signals

- Data has natural center or zero point
- High and low values require visual distinction
- Semantic meaning depends on midpoint interpretation

## Contraindications

- Sequential data without meaningful center
- Categorical data without inherent ordering
- Single-hue emphasis required
- Accessibility constraints prohibit specific color pairs

## Constraints

- Palette must be one of the nine ColorBrewer diverging schemes: BrBG, PiYG, PRGn, PuOr, RdBu, RdGy, RdYlBu, RdYlGn, Spectral
- Use d3.interpolate* for continuous scales; d3.scheme* for discrete arrays
- Midpoint color should visually represent neutral state

## Cautions

- Diverging palettes are not interchangeable with sequential or categorical schemes
- Color perception varies; test with target audience when accessibility is critical

## Output Contract

- Correct ColorBrewer diverging palette name (e.g., d3.interpolateRdBu or d3.schemeRdBu) selected and applied to visualization scale
- Palette semantically matches data structure with clear visual distinction between opposing extremes and neutral midpoint

## Example Therapist Responses

### Example 1

- Client/Input: Temperature anomaly data ranging from -5°C to +5°C with 0°C as neutral
- Therapist/Output: d3.interpolateRdBu or d3.schemeRdBu applied; red for positive anomalies, blue for negative, white/neutral at center
- Notes: RdBu (Red-Blue) is semantically appropriate for temperature divergence

### Example 2

- Client/Input: Political voting data with left/right spectrum and center as balanced
- Therapist/Output: d3.interpolatePRGn or d3.schemePRGn applied; purple for left, green for right, neutral center
- Notes: PRGn (Purple-Green) provides clear visual separation for opposing political positions

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Encoding data with a meaningful neutral midpoint
- Visualizing opposing or contrasting data extremes
- Selecting color scheme for diverging phenomena (anomalies, deviations, political/economic spectra)

## Examples

### Example 1

Input:

  Temperature anomaly data ranging from -5°C to +5°C with 0°C as neutral

Output:

  d3.interpolateRdBu or d3.schemeRdBu applied; red for positive anomalies, blue for negative, white/neutral at center

Notes:

  RdBu (Red-Blue) is semantically appropriate for temperature divergence

### Example 2

Input:

  Political voting data with left/right spectrum and center as balanced

Output:

  d3.interpolatePRGn or d3.schemePRGn applied; purple for left, green for right, neutral center

Notes:

  PRGn (Purple-Green) provides clear visual separation for opposing political positions

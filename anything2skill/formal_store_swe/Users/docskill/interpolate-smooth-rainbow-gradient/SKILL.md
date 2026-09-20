---
id: "1f7ca898-7081-55cc-b581-8680192a237e"
name: "Interpolate smooth rainbow gradient"
description: "Generate a continuous smooth rainbow color interpolation function for sequential or cyclical data visualization. Maps normalized input values [0, 1] to perceptually smooth rainbow color strings suitable for ordered or circular data."
version: "0.1.0"
tags:
  - "color"
  - "interpolation"
  - "visualization"
  - "d3"
  - "gradient"
  - "rainbow"
triggers:
  - "continuous or cyclical data requires smooth color transition"
  - "rainbow color effect is acceptable for the visualization"
  - "perceptual uniformity is secondary to visual appeal"
examples:
  - input: "t = 0.0"
    output: "red (start of rainbow)"
    notes: "Beginning of the color spectrum"
  - input: "t = 0.5"
    output: "cyan/green (middle of rainbow)"
    notes: "Midpoint of the smooth gradient"
  - input: "t = 1.0"
    output: "magenta/purple (end of rainbow)"
    notes: "End of the color spectrum"
---

# Interpolate smooth rainbow gradient

Generate a continuous smooth rainbow color interpolation function for sequential or cyclical data visualization. Maps normalized input values [0, 1] to perceptually smooth rainbow color strings suitable for ordered or circular data.

## Prompt

Call this skill when you need to map continuous or cyclical numeric data to a smooth rainbow color ramp. The skill returns an interpolation function that accepts a normalized value between 0 and 1 and returns a color string. Use d3.interpolateRainbow for a standard less-angry rainbow, or d3.interpolateSinebow for a smoother perceptually-uniform variant.

## Objective

generate smooth rainbow color interpolation function
## Applicable Signals

- data is ordered or circular in nature
- caller needs a function, not a fixed palette
- smooth gradient across the full spectrum is desired

## Contraindications

- categorical data (use categorical color schemes instead)
- accessibility-critical contexts (rainbow is not colorblind-safe)
- diverging or sequential single-hue scales are required
- discrete color categories are needed

## Workflow Steps

- Select interpolation variant: d3.interpolateRainbow (standard) or d3.interpolateSinebow (smoother)
- Call the selected function with a normalized value t in [0, 1]
- Receive color string output
- Apply color string to visualization element

## Constraints

- input must be normalized to [0, 1] range
- output is a color string (hex or CSS format)
- function is deterministic and stateless

## Cautions

- Rainbow colors are not colorblind-accessible; avoid in accessibility-critical applications
- Perceptual uniformity is lower than dedicated sequential or diverging scales

## Output Contract

- Returns an interpolation function that accepts a single numeric argument in [0, 1] and returns a color string (e.g., 'rgb(255, 0, 0)' or hex equivalent). The function is reusable across multiple data points.

## Example Executions

### Example 1

- Input: t = 0.0
- Output: red (start of rainbow)
- Notes: Beginning of the color spectrum

### Example 2

- Input: t = 0.5
- Output: cyan/green (middle of rainbow)
- Notes: Midpoint of the smooth gradient

### Example 3

- Input: t = 1.0
- Output: magenta/purple (end of rainbow)
- Notes: End of the color spectrum

## Triggers

- continuous or cyclical data requires smooth color transition
- rainbow color effect is acceptable for the visualization
- perceptual uniformity is secondary to visual appeal

## Examples

### Example 1

Input:

  t = 0.0

Output:

  red (start of rainbow)

Notes:

  Beginning of the color spectrum

### Example 2

Input:

  t = 0.5

Output:

  cyan/green (middle of rainbow)

Notes:

  Midpoint of the smooth gradient

### Example 3

Input:

  t = 1.0

Output:

  magenta/purple (end of rainbow)

Notes:

  End of the color spectrum

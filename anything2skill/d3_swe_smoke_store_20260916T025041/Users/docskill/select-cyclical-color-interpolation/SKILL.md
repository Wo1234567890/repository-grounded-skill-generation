---
id: "9566fcc1-43c4-5755-9511-c3669e5ff821"
name: "Select cyclical color interpolation"
description: "Apply a smooth, continuous color interpolation function for encoding cyclic or periodic data dimensions. Returns either the rainbow or sinebow interpolator based on visual preference and perceptual smoothness requirements."
version: "0.1.0"
tags:
  - "color"
  - "interpolation"
  - "cyclic"
  - "periodic"
  - "d3-color"
  - "data_encoding"
triggers:
  - "encoding periodic or cyclic data (angles, time-of-day, hue cycles)"
  - "need smooth, continuous color transition across a wrapped dimension"
  - "data naturally wraps around (0–360°, 0–24h, 0–1 normalized)"
examples:
  - input: "Encoding time-of-day (0–24h) as hue; normalized to [0, 1]."
    output: "d3.interpolateRainbow(0.5) → color string at midday (e.g., cyan/green region of rainbow)."
    notes: "Smooth transition across 24-hour cycle."
  - input: "Encoding angle (0–360°) as hue; normalized to [0, 1]."
    output: "d3.interpolateSinebow(0.25) → color string at 90° (e.g., yellow region)."
    notes: "Sinebow provides perceptually uniform transitions."
---

# Select cyclical color interpolation

Apply a smooth, continuous color interpolation function for encoding cyclic or periodic data dimensions. Returns either the rainbow or sinebow interpolator based on visual preference and perceptual smoothness requirements.

## Prompt

To encode periodic or cyclic data (angles, time-of-day, hue cycles), retrieve and apply a cyclical color interpolator. Call d3.interpolateRainbow or d3.interpolateSinebow with a normalized input value in [0, 1]. The interpolator returns a color string for that position in the cycle.

## Objective

retrieve and apply cyclical color interpolator
## Applicable Signals

- cyclic data dimension detected
- smooth color gradient required
- data wraps or repeats

## Contraindications

- categorical or discrete data
- diverging data requiring a midpoint
- linear sequential encoding
- colorblind accessibility is a hard requirement

## Workflow Steps

- Determine whether data is truly cyclic (wraps around).
- Normalize data values to [0, 1].
- Select interpolator: d3.interpolateRainbow (traditional) or d3.interpolateSinebow (perceptually smoother).
- Call interpolator with normalized value to retrieve color string.
- Apply color to visual element.

## Constraints

- input must be normalized to [0, 1]
- output is a color string (hex or rgb)
- sinebow is smoother perceptually; rainbow is more traditional

## Cautions

- rainbow and sinebow are not colorblind-friendly; use categorical or diverging schemes if accessibility is critical
- ensure input normalization before calling interpolator

## Output Contract

- Returns a callable interpolation function (d3.interpolateRainbow or d3.interpolateSinebow) that accepts a normalized input in [0, 1] and returns a color string suitable for direct use in SVG or canvas rendering.

## Example Therapist Responses

### Example 1

- Client/Input: Encoding time-of-day (0–24h) as hue; normalized to [0, 1].
- Therapist/Output: d3.interpolateRainbow(0.5) → color string at midday (e.g., cyan/green region of rainbow).
- Notes: Smooth transition across 24-hour cycle.

### Example 2

- Client/Input: Encoding angle (0–360°) as hue; normalized to [0, 1].
- Therapist/Output: d3.interpolateSinebow(0.25) → color string at 90° (e.g., yellow region).
- Notes: Sinebow provides perceptually uniform transitions.

## Triggers

- encoding periodic or cyclic data (angles, time-of-day, hue cycles)
- need smooth, continuous color transition across a wrapped dimension
- data naturally wraps around (0–360°, 0–24h, 0–1 normalized)

## Examples

### Example 1

Input:

  Encoding time-of-day (0–24h) as hue; normalized to [0, 1].

Output:

  d3.interpolateRainbow(0.5) → color string at midday (e.g., cyan/green region of rainbow).

Notes:

  Smooth transition across 24-hour cycle.

### Example 2

Input:

  Encoding angle (0–360°) as hue; normalized to [0, 1].

Output:

  d3.interpolateSinebow(0.25) → color string at 90° (e.g., yellow region).

Notes:

  Sinebow provides perceptually uniform transitions.

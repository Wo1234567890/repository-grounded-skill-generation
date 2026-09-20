---
id: "a68ef8fc-ec1c-541a-a723-4a28825dcc8f"
name: "Identify and audit images lacking dimension metadata"
description: "Scan page markup and CSS to detect images without width/height attributes or aspect-ratio declarations, flagging them as CLS risk factors. This diagnostic micro-skill precedes remediation and helps prioritize layout stability fixes."
version: "0.1.0"
tags:
  - "CLS"
  - "layout_shift"
  - "performance"
  - "audit"
  - "image_optimization"
  - "responsive_design"
triggers:
  - "Running CLS audit or performance review"
  - "Lighthouse reports image-related layout shifts"
  - "Need to prioritize layout stability fixes"
  - "Performance baseline assessment"
examples:
  - input: "HTML: <img src=\"puppy.jpg\" alt=\"Puppy with balloons\">"
    output: "Missing: width, height, aspect-ratio. Viewport: above-fold. Severity: high."
    notes: "No dimension metadata; will cause layout shift when image loads."
  - input: "HTML: <img src=\"puppy.jpg\" width=\"640\" height=\"360\" alt=\"Puppy with balloons\">"
    output: "Present: width=640, height=360. Severity: none."
    notes: "Dimensions specified; space pre-allocated."
  - input: "CSS: img { width: 100%; height: auto; } HTML: <img src=\"puppy.jpg\" alt=\"Puppy\">"
    output: "Missing: height attribute, aspect-ratio. CSS width only. Severity: high."
    notes: "Responsive width without aspect-ratio; height unknown until load."
---

# Identify and audit images lacking dimension metadata

Scan page markup and CSS to detect images without width/height attributes or aspect-ratio declarations, flagging them as CLS risk factors. This diagnostic micro-skill precedes remediation and helps prioritize layout stability fixes.

## Prompt

Inspect all <img> and <video> elements in the document. Check for presence of width and height attributes (with or without units) or CSS aspect-ratio declarations. Flag any image or video element that lacks both explicit dimensions and aspect-ratio reservation. Categorize findings by viewport position (above-fold vs. below-fold) to assess user-facing impact.

## Objective

detect_missing_dimensions
## Applicable Signals

- CLS metric elevated or flagged
- Visual regression reports mentioning image loading
- Responsive design audit in progress

## Contraindications

- Images are dynamically generated with no static markup
- Audit scope is limited to non-image content
- Page uses only vector or inline SVG without raster images

## Workflow Steps

- {'step': 1, 'action': 'Enumerate all img and video elements in the document', 'detail': 'Parse DOM or static markup to collect all media elements'}
- {'step': 2, 'action': 'Check for width and height attributes', 'detail': 'Verify presence of width and height on each element (with or without units)'}
- {'step': 3, 'action': 'Check for CSS aspect-ratio or equivalent dimension rules', 'detail': 'Inspect computed styles for aspect-ratio, width, height, max-width, or similar constraints'}
- {'step': 4, 'action': 'Classify missing dimensions', 'detail': 'Flag elements lacking both attributes and CSS dimension rules'}
- {'step': 5, 'action': 'Rank by viewport position', 'detail': 'Categorize findings as above-fold (high priority) or below-fold (lower priority)'}

## Constraints

- Requires access to page source markup and computed CSS styles
- Must inspect both HTML attributes and CSS rules (width, height, aspect-ratio, max-width, etc.)
- Should distinguish between responsive images (srcset) and single-source images

## Cautions

- CSS-only dimension rules may be overridden by inline styles; check computed styles
- Aspect-ratio alone does not guarantee space reservation in older browsers; verify fallback dimensions
- Above-fold images have higher user-impact priority than below-fold

## Output Contract

- Structured list or report of image/video elements missing width, height, or aspect-ratio declarations. Each entry includes element selector, current attributes, viewport position, and severity level. Report enables downstream remediation skill to prioritize fixes.

## Example Executions

### Example 1

- Input: HTML: <img src="puppy.jpg" alt="Puppy with balloons">
- Output: Missing: width, height, aspect-ratio. Viewport: above-fold. Severity: high.
- Notes: No dimension metadata; will cause layout shift when image loads.

### Example 2

- Input: HTML: <img src="puppy.jpg" width="640" height="360" alt="Puppy with balloons">
- Output: Present: width=640, height=360. Severity: none.
- Notes: Dimensions specified; space pre-allocated.

### Example 3

- Input: CSS: img { width: 100%; height: auto; } HTML: <img src="puppy.jpg" alt="Puppy">
- Output: Missing: height attribute, aspect-ratio. CSS width only. Severity: high.
- Notes: Responsive width without aspect-ratio; height unknown until load.

## Triggers

- Running CLS audit or performance review
- Lighthouse reports image-related layout shifts
- Need to prioritize layout stability fixes
- Performance baseline assessment

## Examples

### Example 1

Input:

  HTML: <img src="puppy.jpg" alt="Puppy with balloons">

Output:

  Missing: width, height, aspect-ratio. Viewport: above-fold. Severity: high.

Notes:

  No dimension metadata; will cause layout shift when image loads.

### Example 2

Input:

  HTML: <img src="puppy.jpg" width="640" height="360" alt="Puppy with balloons">

Output:

  Present: width=640, height=360. Severity: none.

Notes:

  Dimensions specified; space pre-allocated.

### Example 3

Input:

  CSS: img { width: 100%; height: auto; } HTML: <img src="puppy.jpg" alt="Puppy">

Output:

  Missing: height attribute, aspect-ratio. CSS width only. Severity: high.

Notes:

  Responsive width without aspect-ratio; height unknown until load.

---
id: "30d72c77-fba4-5b7c-b89a-1ff0a77a8cc1"
name: "Inverse Document Frequency (IDF) Lookup"
description: "Calculate a missing image dimension using the aspect ratio formula to enable layout space reservation before the image loads. Given one known dimension (height) and an aspect ratio (e.g., 16:9), compute the other dimension (width) to prevent cumulative layout shift."
version: "0.1.1"
tags:
  - "layout_shift_prevention"
  - "responsive_images"
  - "aspect_ratio"
  - "dimension_calculation"
  - "space_reservation"
triggers:
  - "Building tf-idf weights"
  - "Analyzing term rarity or discriminative power across document collection"
examples:
  - input: "{'height': 360, 'aspect_ratio': '16:9'}"
    output: "{'width': 640}"
    notes: "16:9 aspect ratio with 360px height yields 640px width"
  - input: "{'height': 300, 'aspect_ratio': '4:3'}"
    output: "{'width': 400}"
    notes: "4:3 aspect ratio with 300px height yields 400px width"
---

# Inverse Document Frequency (IDF) Lookup

Calculate a missing image dimension using the aspect ratio formula to enable layout space reservation before the image loads. Given one known dimension (height) and an aspect ratio (e.g., 16:9), compute the other dimension (width) to prevent cumulative layout shift.

## Prompt

Use the aspect ratio formula: width = height × (aspect_width / aspect_height). Substitute the known height value and the aspect ratio components to derive the missing width. Return the calculated dimension in the same units as the input.

## Objective

derive_missing_dimension
## Applicable Signals

- Image element with height specified but width missing
- CSS aspect-ratio property or intrinsic aspect ratio available
- Responsive design context where one dimension is constrained

## Contraindications

- Aspect ratio is unknown or variable
- Image is truly fluid with no intrinsic dimensions or aspect ratio
- Dimension is already explicitly specified in markup or CSS

## Workflow Steps

- {'step': 1, 'action': 'Identify the known dimension (height) and the aspect ratio (width:height)', 'input': 'height value, aspect_width, aspect_height'}
- {'step': 2, 'action': 'Apply the formula: width = height × (aspect_width / aspect_height)', 'input': 'height, aspect_width, aspect_height'}
- {'step': 3, 'action': 'Return the calculated width value', 'output': 'width in same units as input height'}

## Constraints

- Aspect ratio must be expressed as two positive numbers (width:height)
- Known dimension must be a valid numeric value in consistent units
- Calculated dimension should be rounded or truncated to match browser layout precision

## Cautions

- Ensure aspect ratio matches the actual image; mismatched ratios will distort the image or reserve incorrect space
- Use consistent units (pixels, percentages, or relative units) for input and output

## Output Contract

- Calculated dimension value (in pixels or relative units) that matches or approximates the actual image size; layout space correctly reserved before image load

## Example Executions

### Example 1

- Input: {'height': 360, 'aspect_ratio': '16:9'}
- Output: {'width': 640}
- Notes: 16:9 aspect ratio with 360px height yields 640px width

### Example 2

- Input: {'height': 300, 'aspect_ratio': '4:3'}
- Output: {'width': 400}
- Notes: 4:3 aspect ratio with 300px height yields 400px width

## Triggers

- Building tf-idf weights
- Analyzing term rarity or discriminative power across document collection

## Examples

### Example 1

Input:

  {'height': 360, 'aspect_ratio': '16:9'}

Output:

  {'width': 640}

Notes:

  16:9 aspect ratio with 360px height yields 640px width

### Example 2

Input:

  {'height': 300, 'aspect_ratio': '4:3'}

Output:

  {'width': 400}

Notes:

  4:3 aspect ratio with 300px height yields 400px width

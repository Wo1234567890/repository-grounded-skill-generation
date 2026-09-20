---
id: "ee115434-2950-5f2b-aa99-144a723eba29"
name: "Image Component Optimization"
description: "Prevent layout shifts by calculating and reserving space for images before they load, using aspect ratio derived from width and height attributes. When image dimensions are known or can be derived from aspect ratio, set width and height attributes to allow the browser to pre-allocate space and avoid text reflow."
version: "0.1.1"
tags:
  - "layout_shift"
  - "image_optimization"
  - "web_performance"
  - "aspect_ratio"
  - "cls_prevention"
triggers:
  - "displaying images in responsive web layouts"
  - "need to reduce initial page load time"
examples:
  - input: "Image with 640px width and known 16:9 aspect ratio"
    output: "<img src=\"puppy.jpg\" width=\"640\" height=\"360\" alt=\"Puppy with balloons\">"
    notes: "Height calculated as 640 × (9/16) = 360px"
  - input: "Image with 360px height and known 16:9 aspect ratio"
    output: "<img src=\"puppy.jpg\" width=\"640\" height=\"360\" alt=\"Puppy with balloons\">"
    notes: "Width calculated as 360 × (16/9) = 640px"
---

# Image Component Optimization

Prevent layout shifts by calculating and reserving space for images before they load, using aspect ratio derived from width and height attributes. When image dimensions are known or can be derived from aspect ratio, set width and height attributes to allow the browser to pre-allocate space and avoid text reflow.

## Prompt

1. Identify the image's aspect ratio (e.g., 16:9, 4:3).
2. If one dimension is known, calculate the other using the aspect ratio formula: for x:y ratio, if width is known, height = width × (y/x); if height is known, width = height × (x/y).
3. Set both width and height attributes on the <img> element (e.g., <img src="image.jpg" width="640" height="360" alt="description">).
4. Include CSS to ensure the aspect ratio is preserved across responsive layouts.
5. Verify that space is reserved before the image begins downloading.

## Objective

prevent_layout_shift
## Applicable Signals

- Image source is specified but dimensions are missing
- Aspect ratio of image is known or documented
- Text or other content is positioned below the image

## Contraindications

- Image dimensions are truly unknown and cannot be inferred
- Responsive images with multiple sources (srcset) require different handling
- Image is dynamically sized based on container without fixed aspect ratio

## Workflow Steps

- {'step': 1, 'action': 'Determine aspect ratio', 'detail': 'Identify or calculate the aspect ratio of the image (e.g., 16:9, 4:3, 1:1)'}
- {'step': 2, 'action': 'Calculate missing dimension', 'detail': 'If one dimension is known, use the formula: missing_dimension = known_dimension × (ratio_component / other_ratio_component)'}
- {'step': 3, 'action': 'Set width and height attributes', 'detail': 'Add width and height attributes to the <img> tag with calculated values'}
- {'step': 4, 'action': 'Verify space reservation', 'detail': 'Confirm that the browser reserves space before image download begins'}

## Constraints

- Both width and height attributes must be set on the img element
- Aspect ratio must be accurately known or calculated
- CSS must preserve the aspect ratio for responsive layouts

## Cautions

- Incorrect aspect ratio calculation will result in distorted or improperly sized images
- Setting only one dimension without aspect ratio CSS may not prevent layout shifts
- Responsive images with srcset may require additional techniques beyond this micro-skill

## Output Contract

- Browser reserves sufficient vertical and horizontal space for the image before download
- Text and other content do not shift when the image loads
- Layout remains stable throughout image load lifecycle

## Example Therapist Responses

### Example 1

- Client/Input: Image with 640px width and known 16:9 aspect ratio
- Therapist/Output: <img src="puppy.jpg" width="640" height="360" alt="Puppy with balloons">
- Notes: Height calculated as 640 × (9/16) = 360px

### Example 2

- Client/Input: Image with 360px height and known 16:9 aspect ratio
- Therapist/Output: <img src="puppy.jpg" width="640" height="360" alt="Puppy with balloons">
- Notes: Width calculated as 360 × (16/9) = 640px

## Triggers

- displaying images in responsive web layouts
- need to reduce initial page load time

## Examples

### Example 1

Input:

  Image with 640px width and known 16:9 aspect ratio

Output:

  <img src="puppy.jpg" width="640" height="360" alt="Puppy with balloons">

Notes:

  Height calculated as 640 × (9/16) = 360px

### Example 2

Input:

  Image with 360px height and known 16:9 aspect ratio

Output:

  <img src="puppy.jpg" width="640" height="360" alt="Puppy with balloons">

Notes:

  Width calculated as 360 × (16/9) = 640px

---
id: "88e2cd8b-cded-5050-9820-9ed10a2b232a"
name: "Reserve space for images using dimensions or aspect ratio"
description: "Prevent Cumulative Layout Shift by declaring image dimensions via width/height attributes or CSS aspect-ratio before the image loads, ensuring the browser allocates correct layout space upfront."
version: "0.1.0"
tags:
  - "layout_shift"
  - "cls_mitigation"
  - "image_optimization"
  - "responsive_design"
  - "web_performance"
triggers:
  - "Adding images or video elements to a page"
  - "Implementing responsive design with flexible sizing"
  - "Lighthouse or CLS audit flags image-related layout shifts"
examples:
  - input: "Fixed-size image with known dimensions 640×360"
    output: "<img src=\"puppy.jpg\" width=\"640\" height=\"360\" alt=\"Puppy with balloons\">"
    notes: "Browser reserves 640×360 pixel area before fetch; image stretches to fit space"
  - input: "Responsive image with 16:9 aspect ratio"
    output: "img { width: 100%; aspect-ratio: 16 / 9; }"
    notes: "CSS aspect-ratio maintains proportions; height is calculated from width"
  - input: "Image with known aspect ratio but flexible width"
    output: "<img src=\"image.jpg\" width=\"640\" height=\"360\" style=\"width: 100%; height: auto;\" alt=\"...\">"
    notes: "Attributes provide aspect ratio hint; CSS allows responsive sizing without layout shift"
---

# Reserve space for images using dimensions or aspect ratio

Prevent Cumulative Layout Shift by declaring image dimensions via width/height attributes or CSS aspect-ratio before the image loads, ensuring the browser allocates correct layout space upfront.

## Prompt

When adding images or video elements to a page, always include width and height size attributes on the element, or reserve the required space with CSS aspect-ratio or similar. This ensures the browser can allocate the correct amount of space in the document while the image is loading, preventing text and other content from shifting when the image arrives.

For traditional fixed-size images, use width and height attributes without units (pixel dimensions). For responsive images, use CSS aspect-ratio to maintain proportions while allowing flexible width. If you know the aspect ratio (e.g., 16:9 or 4:3), you can calculate one dimension from the other.

## Objective

allocate_layout_space_before_image_load
## Applicable Signals

- Image element without width/height attributes detected
- CSS-only image sizing without aspect-ratio fallback
- CLS metric spike correlated with image load timing

## Contraindications

- Image dimensions are truly unknown at build time and cannot be inferred
- Dynamic content with no aspect ratio information available
- Image is decorative and layout space is intentionally flexible

## Intervention Moves

- Add width and height attributes to img or video elements
- Apply CSS aspect-ratio rule to image selectors
- Convert responsive images to use aspect-ratio with flexible width

## Workflow Steps

- {'step': 1, 'action': 'Determine image dimensions or aspect ratio', 'detail': 'Identify the true width and height of the image, or calculate the aspect ratio (width:height ratio, e.g., 16:9)'}
- {'step': 2, 'action': 'Choose declaration method', 'detail': 'For fixed-size images, use width and height attributes. For responsive images, use CSS aspect-ratio or width/height attributes with responsive CSS.'}
- {'step': 3, 'action': 'Apply dimensions to image element', 'detail': 'Add width and height attributes to <img> or <video> tag, or add CSS aspect-ratio rule to the image class/selector'}
- {'step': 4, 'action': 'Verify layout space allocation', 'detail': 'Confirm that the browser reserves the correct space before the image loads; test with slow network to observe no text reflow'}

## Constraints

- Width and height attributes must be specified before the image fetch begins
- Aspect ratio must be accurate to prevent over- or under-allocation of space
- CSS aspect-ratio property requires browser support (modern browsers only)

## Cautions

- Incorrect aspect ratio will cause the image to stretch or compress, degrading visual quality
- Omitting dimensions entirely will cause layout shift when the image loads

## Output Contract

- Image element includes width and height attributes (or CSS aspect-ratio rule)
- Browser reserves layout space before image fetch
- No visible text reflow or layout shift when image loads
- CLS contribution from this image is zero or negligible

## Example Executions

### Example 1

- Input: Fixed-size image with known dimensions 640×360
- Output: <img src="puppy.jpg" width="640" height="360" alt="Puppy with balloons">
- Notes: Browser reserves 640×360 pixel area before fetch; image stretches to fit space

### Example 2

- Input: Responsive image with 16:9 aspect ratio
- Output: img { width: 100%; aspect-ratio: 16 / 9; }
- Notes: CSS aspect-ratio maintains proportions; height is calculated from width

### Example 3

- Input: Image with known aspect ratio but flexible width
- Output: <img src="image.jpg" width="640" height="360" style="width: 100%; height: auto;" alt="...">
- Notes: Attributes provide aspect ratio hint; CSS allows responsive sizing without layout shift

## Triggers

- Adding images or video elements to a page
- Implementing responsive design with flexible sizing
- Lighthouse or CLS audit flags image-related layout shifts

## Examples

### Example 1

Input:

  Fixed-size image with known dimensions 640×360

Output:

  <img src="puppy.jpg" width="640" height="360" alt="Puppy with balloons">

Notes:

  Browser reserves 640×360 pixel area before fetch; image stretches to fit space

### Example 2

Input:

  Responsive image with 16:9 aspect ratio

Output:

  img { width: 100%; aspect-ratio: 16 / 9; }

Notes:

  CSS aspect-ratio maintains proportions; height is calculated from width

### Example 3

Input:

  Image with known aspect ratio but flexible width

Output:

  <img src="image.jpg" width="640" height="360" style="width: 100%; height: auto;" alt="...">

Notes:

  Attributes provide aspect ratio hint; CSS allows responsive sizing without layout shift

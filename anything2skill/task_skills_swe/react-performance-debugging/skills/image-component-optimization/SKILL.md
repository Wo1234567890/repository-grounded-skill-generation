---
id: "6d8fa45a-b5a5-5a9a-9e04-504a7636bdcb"
name: "Image Component Optimization"
description: "Declare width and height attributes on img and picture source elements to establish aspect ratio and prevent layout shifts when images load."
version: "0.1.1"
tags:
  - "layout_shift"
  - "CLS"
  - "responsive_images"
  - "html_attributes"
  - "performance"
  - "web_vitals"
triggers:
  - "displaying images in Next.js pages or components"
  - "need responsive image sizing across device types"
  - "want to reduce initial page load time"
examples:
  - input: "Responsive image with srcset"
    output: "<img width=\"1000\" height=\"1000\" src=\"puppy-1000.jpg\" srcset=\"puppy-1000.jpg 1000w, puppy-2000.jpg 2000w, puppy-3000.jpg 3000w\" alt=\"Puppy with balloons\" />"
    notes: "Width and height establish aspect ratio; browser reserves space before any srcset variant loads"
  - input: "Art-directed image with picture and multiple sources"
    output: "<picture>\n  <source media=\"(max-width: 799px)\" srcset=\"puppy-480w-cropped.jpg\" width=\"480\" height=\"400\" />\n  <source media=\"(min-width: 800px)\" srcset=\"puppy-800w.jpg\" width=\"800\" height=\"400\" />\n  <img src=\"puppy-800w.jpg\" alt=\"Puppy with balloons\" width=\"800\" height=\"400\" />\n</picture>"
    notes: "Each source and fallback img have width and height; dimensions may differ per source if aspect ratio changes with art direction"
---

# Image Component Optimization

Declare width and height attributes on img and picture source elements to establish aspect ratio and prevent layout shifts when images load.

## Prompt

When defining img or picture elements with known or calculable aspect ratios, add width and height attributes to all img tags and source elements within picture tags. For responsive images using srcset, include dimensions on the img element. For art-directed images using picture with multiple sources, set width and height on each source element and the fallback img element. This reserves layout space before the image asset loads, preventing cumulative layout shift (CLS).

## Objective

Prevent layout shift by reserving image space before image asset loads
## Applicable Signals

- Defining img or picture elements
- Images have known or calculable aspect ratios
- Responsive image sets (srcset) or art direction (picture with sources) are used
- Layout shift observed during image load

## Contraindications

- Image dimensions are truly unknown at build time
- Aspect ratio varies per viewport without media query control
- Intrinsic sizing is required and dimensions cannot be predetermined

## Workflow Steps

- {'step': 1, 'action': 'Identify the image aspect ratio (width:height ratio)', 'detail': 'Calculate or obtain the intrinsic dimensions of the image asset'}
- {'step': 2, 'action': 'Add width and height attributes to img element', 'detail': 'Set width and height in pixels or as a ratio that matches the image aspect ratio'}
- {'step': 3, 'action': 'For responsive images with srcset, declare dimensions on img', 'detail': 'Include width and height attributes alongside srcset attribute'}
- {'step': 4, 'action': 'For art-directed images using picture, add dimensions to each source', 'detail': 'Set width and height on each source element and the fallback img element; dimensions may differ per source if aspect ratio changes'}
- {'step': 5, 'action': 'Verify layout space is reserved before image load', 'detail': 'Test in browser to confirm no content shift occurs when image loads'}

## Constraints

- Width and height must match the actual aspect ratio of the image
- For responsive images, dimensions should reflect the largest or reference size
- All source elements within a picture tag should have matching width and height declarations

## Cautions

- Mismatched width and height values will distort the image or cause unexpected layout
- Dimensions must be consistent across all breakpoints unless using media-query-specific source elements

## Output Contract

- Browser reserves layout space matching declared dimensions; image loads without shifting surrounding content; aspect ratio preserved across responsive breakpoints.

## Example Executions

### Example 1

- Input: Responsive image with srcset
- Output: <img width="1000" height="1000" src="puppy-1000.jpg" srcset="puppy-1000.jpg 1000w, puppy-2000.jpg 2000w, puppy-3000.jpg 3000w" alt="Puppy with balloons" />
- Notes: Width and height establish aspect ratio; browser reserves space before any srcset variant loads

### Example 2

- Input: Art-directed image with picture and multiple sources
- Output: <picture>
  <source media="(max-width: 799px)" srcset="puppy-480w-cropped.jpg" width="480" height="400" />
  <source media="(min-width: 800px)" srcset="puppy-800w.jpg" width="800" height="400" />
  <img src="puppy-800w.jpg" alt="Puppy with balloons" width="800" height="400" />
</picture>
- Notes: Each source and fallback img have width and height; dimensions may differ per source if aspect ratio changes with art direction

## Triggers

- displaying images in Next.js pages or components
- need responsive image sizing across device types
- want to reduce initial page load time

## Examples

### Example 1

Input:

  Responsive image with srcset

Output:

  <img width="1000" height="1000" src="puppy-1000.jpg" srcset="puppy-1000.jpg 1000w, puppy-2000.jpg 2000w, puppy-3000.jpg 3000w" alt="Puppy with balloons" />

Notes:

  Width and height establish aspect ratio; browser reserves space before any srcset variant loads

### Example 2

Input:

  Art-directed image with picture and multiple sources

Output:

  <picture>
    <source media="(max-width: 799px)" srcset="puppy-480w-cropped.jpg" width="480" height="400" />
    <source media="(min-width: 800px)" srcset="puppy-800w.jpg" width="800" height="400" />
    <img src="puppy-800w.jpg" alt="Puppy with balloons" width="800" height="400" />
  </picture>

Notes:

  Each source and fallback img have width and height; dimensions may differ per source if aspect ratio changes with art direction

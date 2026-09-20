---
id: "2ba77d5e-554c-592b-8196-b40f9b51dd59"
name: "Dynamic Open Graph Image Generation"
description: "Generate dynamic Open Graph images using JSX and CSS with the imageResponse constructor to create customized social media preview cards for each route or content variant."
version: "0.1.0"
tags:
  - "metadata"
  - "social_media"
  - "open_graph"
  - "image_generation"
  - "nextjs"
  - "seo"
triggers:
  - "Page requires custom social media preview images"
  - "Content is dynamic or varies per route"
  - "Social media sharing optimization needed"
---

# Dynamic Open Graph Image Generation

Generate dynamic Open Graph images using JSX and CSS with the imageResponse constructor to create customized social media preview cards for each route or content variant.

## Prompt

Use the imageResponse constructor to generate dynamic OG images. Pass JSX and CSS to render custom preview cards. Serve the generated image as the og:image meta tag. Verify output in social media preview tools (LinkedIn, Twitter, Facebook).

## Objective

Generate dynamic OG images for social sharing
## Applicable Signals

- Dynamic content per page or route segment
- Need for customized social media cards
- og:image meta tag not pre-generated

## Contraindications

- Static pre-generated OG images already exist and are sufficient
- imageResponse constructor not available in deployment environment
- Performance constraints prohibit runtime image generation

## Workflow Steps

- Define JSX template for OG image layout
- Add CSS styling for visual appearance
- Invoke imageResponse constructor with JSX and CSS
- Return generated image as og:image meta tag
- Test preview in social media sharing tools

## Constraints

- imageResponse constructor must be available in the runtime
- JSX and CSS rendering must complete within acceptable latency
- Generated image must be served as valid og:image meta tag

## Cautions

- Runtime image generation may increase response latency; consider caching strategies
- Verify output in multiple social media platforms (LinkedIn, Twitter, Facebook) as rendering varies
- Ensure JSX/CSS complexity does not exceed rendering timeout

## Output Contract

- Generated image served as og:image meta tag; verified in social media preview tools; image renders correctly across major platforms

## Triggers

- Page requires custom social media preview images
- Content is dynamic or varies per route
- Social media sharing optimization needed

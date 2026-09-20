---
id: "074c7e0f-5b37-5e78-b0a2-ac32cae09625"
name: "Configure Next.js Page Metadata"
description: "Set up page metadata using static metadata objects or dynamic generateMetadata functions in layout.js or page.js files to optimize SEO and social media presentation."
version: "0.1.0"
tags:
  - "nextjs"
  - "metadata"
  - "seo"
  - "social_media"
  - "configuration"
triggers:
  - "Building or updating a Next.js page that needs SEO optimization or custom social media preview"
---

# Configure Next.js Page Metadata

Set up page metadata using static metadata objects or dynamic generateMetadata functions in layout.js or page.js files to optimize SEO and social media presentation.

## Prompt

Export a static `metadata` object or a dynamic `generateMetadata` function from your layout.js or page.js file. Use config-based metadata to modify the <head> element and customize how your content appears in search results and on social media platforms.

## Objective

Set up metadata for SEO and social sharing
## Applicable Signals

- Building or updating a Next.js page that needs SEO optimization
- Customizing social media preview for a page
- Requiring dynamic metadata based on page content or route parameters

## Contraindications

- Static pre-rendered pages with no dynamic content requirements
- Metadata already hardcoded in HTML
- Pages where metadata is managed by external services

## Workflow Steps

- {'step': 1, 'action': 'Choose configuration approach', 'detail': 'Decide between static metadata object (for fixed metadata) or dynamic generateMetadata function (for content-dependent metadata)'}
- {'step': 2, 'action': 'Export metadata from layout.js or page.js', 'detail': 'Add the metadata export to the appropriate file in your route segment'}
- {'step': 3, 'action': 'Verify metadata in page head', 'detail': 'Inspect the rendered <head> element to confirm metadata is correctly applied'}

## Constraints

- Metadata must be exported from layout.js or page.js files
- Dynamic generateMetadata function receives route parameters and search parameters as arguments
- Static metadata object is suitable only when metadata does not depend on dynamic content

## Output Contract

- Metadata object or generateMetadata function successfully exported from layout.js or page.js
- Verified presence of metadata tags in the page <head> element
- Social media platforms and search engines can read the configured metadata

## Triggers

- Building or updating a Next.js page that needs SEO optimization or custom social media preview

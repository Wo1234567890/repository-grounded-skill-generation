---
id: "1e423471-bdb1-5e62-97ab-d86fcb0899f5"
name: "Static Asset Serving via Public Folder"
description: "Configure and serve static assets (images, fonts, files) through Next.js `/public` folder with CDN caching for efficient delivery."
version: "0.1.0"
tags:
  - "static_assets"
  - "cdn_caching"
  - "performance"
  - "deployment"
  - "nextjs"
triggers:
  - "Project requires serving images, fonts, or other static files that should be cached and delivered efficiently across CDN"
---

# Static Asset Serving via Public Folder

Configure and serve static assets (images, fonts, files) through Next.js `/public` folder with CDN caching for efficient delivery.

## Prompt

Place static assets (images, fonts, other files) in the `/public` folder at the project root. Files in `/public` are served at root-relative URLs (e.g., `/image.png` for `/public/image.png`) and can be cached by CDN providers for efficient delivery. Use this approach for assets that do not require dynamic generation or per-request customization.

## Objective

Enable efficient static asset delivery with CDN caching
## Applicable Signals

- Project requires serving images, fonts, or other static files
- Assets should be cached and delivered efficiently across CDN
- Static files are not expected to change per request

## Contraindications

- Assets require dynamic generation or server-side processing
- Content must be customized per request or user
- Files need to be generated at runtime

## Workflow Steps

- Create or use existing `/public` folder at project root
- Place static asset files (images, fonts, etc.) in `/public`
- Reference assets in code using root-relative URLs (e.g., `/filename.ext`)
- Verify CDN provider caching headers are applied to `/public` assets
- Test asset delivery and caching behavior in production

## Constraints

- Assets must be static and not require per-request modification
- File paths are exposed in URLs; do not place sensitive files in `/public`

## Output Contract

- Static assets placed in `/public` folder are accessible via root-relative URLs and cached by CDN providers for efficient delivery

## Triggers

- Project requires serving images, fonts, or other static files that should be cached and delivered efficiently across CDN

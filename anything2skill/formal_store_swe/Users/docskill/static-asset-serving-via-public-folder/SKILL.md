---
id: "457c51d4-6891-5bfb-9b16-0ed1ab424bfa"
name: "Static Asset Serving via Public Folder"
description: "Configure and serve static assets (images, fonts, files) from Next.js `/public` folder with CDN caching integration. Use when deploying static content that requires efficient delivery and cache optimization."
version: "0.1.0"
tags:
  - "next.js"
  - "static_assets"
  - "cdn_caching"
  - "performance"
  - "deployment"
triggers:
  - "Deploying static assets (images, fonts, CSS, JS bundles) that need CDN caching and fast delivery"
---

# Static Asset Serving via Public Folder

Configure and serve static assets (images, fonts, files) from Next.js `/public` folder with CDN caching integration. Use when deploying static content that requires efficient delivery and cache optimization.

## Prompt

Place static assets (images, fonts, CSS, JS bundles) in the `/public` folder. Next.js automatically serves these files at the root path. Configure CDN providers to cache files from `/public` for efficient delivery. Verify that assets are accessible via their public URLs and that cache headers are properly applied.

## Objective

Enable efficient static asset delivery through public folder configuration and CDN caching
## Applicable Signals

- Deploying static assets (images, fonts, CSS, JS bundles)
- Need for CDN caching and fast delivery
- Optimization of asset delivery performance
- Public-facing static content without authentication requirements

## Contraindications

- Serving dynamic content
- User-generated files requiring runtime processing
- Sensitive data requiring authentication or authorization
- Content that changes frequently and requires cache invalidation

## Workflow Steps

- {'step': 1, 'action': 'Place static assets in `/public` folder', 'detail': 'Organize images, fonts, and other static files in the `/public` directory at project root'}
- {'step': 2, 'action': 'Configure CDN provider', 'detail': 'Set up CDN to cache files from `/public` folder for efficient global delivery'}
- {'step': 3, 'action': 'Verify asset accessibility', 'detail': 'Test that assets are accessible via their public URLs (e.g., `/image.png`)'}
- {'step': 4, 'action': 'Validate cache headers', 'detail': 'Confirm that CDN cache headers are properly applied and cache is functioning'}

## Constraints

- Assets must be placed in `/public` folder at project root
- Files are served at root path (e.g., `/public/image.png` → `/image.png`)
- CDN provider must be configured to cache from `/public` endpoint

## Cautions

- Do not store sensitive or authenticated content in `/public`
- Ensure CDN cache invalidation strategy is in place for updated assets
- Monitor cache hit rates to verify CDN integration is working

## Output Contract

- Static assets served from `/public` folder with CDN cache headers applied and verified delivery performance. Assets are accessible at root-relative paths and cached by CDN provider.

## Triggers

- Deploying static assets (images, fonts, CSS, JS bundles) that need CDN caching and fast delivery

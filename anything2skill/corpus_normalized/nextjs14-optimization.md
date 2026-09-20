---
title: Optimizations
description: Optimize your Next.js application for best performance and user experience.
url: "https://nextjs.org/docs/14/app/building-your-application/optimizing"
docs_index: /docs/14/llms.txt
version: 14.2.35
lastUpdated: 2023-10-26
prerequisites:
  - "Building Your Application: /docs/14/app/building-your-application"
---


> For an index of all Next.js documentation, see [/docs/14/llms.txt](/docs/14/llms.txt).
Next.js comes with a variety of built-in optimizations designed to improve your application's speed and [Core Web Vitals](https://web.dev/vitals/). This guide will cover the optimizations you can leverage to enhance your user experience.

## Built-in Components

Built-in components abstract away the complexity of implementing common UI optimizations. These components are:

* **Images**: Built on the native `<img>` element. The Image Component optimizes images for performance by lazy loading and automatically resizing images based on device size.
* **Link**: Built on the native `<a>` tags. The Link Component prefetches pages in the background, for faster and smoother page transitions.
* **Scripts**: Built on the native `<script>` tags. The Script Component gives you control over loading and execution of third-party scripts.

## Metadata

Metadata helps search engines understand your content better (which can result in better SEO), and allows you to customize how your content is presented on social media, helping you create a more engaging and consistent user experience across various platforms.

The Metadata API in Next.js allows you to modify the `<head>` element of a page. You can configure metadata in two ways:

* **Config-based Metadata**: Export a [static `metadata` object](/docs/app/api-reference/functions/generate-metadata#metadata-object) or a dynamic [`generateMetadata` function](/docs/app/api-reference/functions/generate-metadata#generatemetadata-function) in a `layout.js` or `page.js` file.
* **File-based Metadata**: Add static or dynamically generated special files to route segments.

Additionally, you can create dynamic Open Graph Images using JSX and CSS with [imageResponse](/docs/app/api-reference/functions/image-response) constructor.

## Static Assets

Next.js `/public` folder can be used to serve static assets like images, fonts, and other files. Files inside `/public` can also be cached by CDN providers so that they are delivered efficiently.

## Analytics and Monitoring

For large applications, Next.js integrates with popular analytics and monitoring tools to help you understand how your application is performing. Learn more in the  [OpenTelemetry](/docs/pages/building-your-application/optimizing/open-telemetry) and [Instrumentation](/docs/pages/building-your-application/optimizing/instrumentation) guides.

- [Images](/docs/14/app/building-your-application/optimizing/images)
  - Optimize your images with the built-in `next/image` component.
- [Fonts](/docs/14/app/building-your-application/optimizing/fonts)
  - Optimize your application's web fonts with the built-in `next/font` loaders.
- [Scripts](/docs/14/app/building-your-application/optimizing/scripts)
  - Optimize 3rd party scripts with the built-in Script component.
- [Metadata](/docs/14/app/building-your-application/optimizing/metadata)
  - Use the Metadata API to define metadata in any layout or page.
- [Static Assets](/docs/14/app/building-your-application/optimizing/static-assets)
  - Next.js allows you to serve static files, like images, in the public directory. You can learn how it works here.
- [Bundle Analyzer](/docs/14/app/building-your-application/optimizing/bundle-analyzer)
  - Analyze the size of your JavaScript bundles using the @next/bundle-analyzer plugin.
- [Lazy Loading](/docs/14/app/building-your-application/optimizing/lazy-loading)
  - Lazy load imported libraries and React Components to improve your application's loading performance.
- [Analytics](/docs/14/app/building-your-application/optimizing/analytics)
  - Measure and track page performance using Next.js Speed Insights
- [Instrumentation](/docs/14/app/building-your-application/optimizing/instrumentation)
  - Learn how to use instrumentation to run code at server startup in your Next.js app
- [OpenTelemetry](/docs/14/app/building-your-application/optimizing/open-telemetry)
  - Learn how to instrument your Next.js app with OpenTelemetry.
- [Third Party Libraries](/docs/14/app/building-your-application/optimizing/third-party-libraries)
  - Optimize the performance of third-party libraries in your application with the `@next/third-parties` package.

---

For an index of all available documentation, see [/docs/14/llms.txt](/docs/14/llms.txt)
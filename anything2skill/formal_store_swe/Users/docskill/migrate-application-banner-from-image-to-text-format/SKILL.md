---
id: "62e04fb9-e4e6-5a6e-a547-d7587f52306e"
name: "Migrate Application Banner from Image to Text Format"
description: "Replace image-based application banners (banner.gif, banner.jpg, banner.png) with a text-based banner.txt file during Spring Boot 3.0 upgrade. Image banner files are no longer supported in Spring Boot 3.0 and must be migrated to text format to maintain startup banner customization."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "resource-migration"
  - "banner-configuration"
  - "pre-upgrade"
triggers:
  - "Spring Boot 3.0 upgrade initiated"
  - "Application resources contain banner.gif, banner.jpg, or banner.png files"
  - "Application startup banner customization is required"
---

# Migrate Application Banner from Image to Text Format

Replace image-based application banners (banner.gif, banner.jpg, banner.png) with a text-based banner.txt file during Spring Boot 3.0 upgrade. Image banner files are no longer supported in Spring Boot 3.0 and must be migrated to text format to maintain startup banner customization.

## Prompt

Locate and remove or archive image banner files (banner.gif, banner.jpg, banner.png) from src/main/resources/. Create a banner.txt file with equivalent text-based banner content. Verify application starts without banner-related warnings or errors.

## Objective

Migrate application startup banner from image format to text format
## Applicable Signals

- Image banner files present in src/main/resources/
- Spring Boot version upgrade from 2.x to 3.0
- Custom banner display expected at application startup

## Contraindications

- Application does not use custom banners
- Only text-based banner.txt is already present
- Banner display is disabled via configuration

## Workflow Steps

- {'step': 1, 'action': 'Identify image banner files', 'detail': 'Scan src/main/resources/ for banner.gif, banner.jpg, banner.png'}
- {'step': 2, 'action': 'Archive or remove image files', 'detail': 'Back up image banner files or delete them from resources'}
- {'step': 3, 'action': 'Create text-based banner', 'detail': 'Create banner.txt with equivalent ASCII art or text content'}
- {'step': 4, 'action': 'Verify migration', 'detail': 'Start application and confirm banner displays without errors'}

## Constraints

- Image banner files must be removed or archived before upgrade
- banner.txt must be created in src/main/resources/ directory
- Text banner content should preserve original visual intent

## Cautions

- Ensure banner.txt is properly formatted as plain text
- Verify file encoding is UTF-8 to avoid character display issues
- Test application startup to confirm banner displays correctly

## Output Contract

- Image banner files removed or archived; banner.txt file created with equivalent text-based banner content; application starts without banner-related warnings or errors

## Triggers

- Spring Boot 3.0 upgrade initiated
- Application resources contain banner.gif, banner.jpg, or banner.png files
- Application startup banner customization is required

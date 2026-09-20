---
id: "4e69e2c1-4c56-5dc5-ab94-5f6cba669a7c"
name: "Select categorical color scheme"
description: "Choose and retrieve a predefined categorical color palette from D3's scheme library based on the number of distinct categories and visual design requirements. Returns an array of hex color strings suitable for encoding nominal variables in visualizations."
version: "0.1.0"
tags:
  - "color"
  - "palette"
  - "categorical"
  - "d3"
  - "visualization"
  - "encoding"
triggers:
  - "encoding categorical data with distinct colors"
  - "need 8–12 distinct hues"
  - "designing charts or visualizations with nominal variables"
---

# Select categorical color scheme

Choose and retrieve a predefined categorical color palette from D3's scheme library based on the number of distinct categories and visual design requirements. Returns an array of hex color strings suitable for encoding nominal variables in visualizations.

## Prompt

Identify the number of distinct categories in your data. Select the appropriate D3 categorical scheme based on palette size (8, 9, 10, or 12 colors) and visual design intent. Retrieve the scheme array and apply it to your categorical encoding.

## Objective

retrieve categorical color palette
## Applicable Signals

- encoding categorical data with distinct colors
- need 8–12 distinct hues
- designing charts or visualizations with nominal variables

## Contraindications

- continuous or sequential data
- diverging data requiring perceptual ordering
- accessibility constraints requiring colorblind-safe palettes

## Workflow Steps

- Count the number of distinct categories in the dataset
- Match category count to available scheme sizes: 8 (Accent, Dark2, Pastel2, Set2), 9 (Pastel1, Set1), 10 (Category10, Observable10, Tableau10), or 12 (Paired, Set3)
- Select scheme based on visual design intent and contrast requirements
- Retrieve the scheme array using d3.scheme<Name>
- Apply the color array to categorical encoding in visualization

## Constraints

- Scheme size must match or exceed the number of distinct categories
- Schemes are fixed arrays; custom color interpolation requires separate skill

## Output Contract

- Array of hex color strings matching the selected scheme (e.g., d3.schemeCategory10 returns 10-color array). Caller receives a ready-to-use color palette for categorical data encoding.

## Triggers

- encoding categorical data with distinct colors
- need 8–12 distinct hues
- designing charts or visualizations with nominal variables

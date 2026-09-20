---
id: "f9073280-7a61-55d8-83fa-b6946f8b5268"
name: "Select categorical color scheme"
description: "Choose and retrieve a predefined categorical color palette from D3's scheme library based on the number of categories and visual design intent. Use when mapping discrete data values to distinct colors."
version: "0.1.0"
tags:
  - "color"
  - "categorical"
  - "palette"
  - "d3"
  - "visualization"
triggers:
  - "rendering categorical data with 8–12 distinct categories; need perceptually distinct colors"
---

# Select categorical color scheme

Choose and retrieve a predefined categorical color palette from D3's scheme library based on the number of categories and visual design intent. Use when mapping discrete data values to distinct colors.

## Prompt

Identify the number of distinct categories in your data. Select the appropriate D3 categorical scheme (schemeCategory10, schemeAccent, schemeDark2, schemeObservable10, schemePaired, schemePastel1, schemePastel2, schemeSet1, schemeSet2, schemeSet3, or schemeTableau10) that matches your category count and visual design requirements. Retrieve the color array from the selected scheme.

## Objective

retrieve categorical color palette
## Applicable Signals

- rendering categorical data with 8–12 distinct categories
- need perceptually distinct colors for discrete values
- mapping nominal or ordinal data to visual channels

## Contraindications

- continuous or diverging data requiring smooth gradients
- sequential color encoding needed
- accessibility constraints demand colorblind-safe palettes
- fewer than 3 or more than 12 categories (use alternative schemes)

## Workflow Steps

- {'step': 1, 'action': 'Count the number of distinct categories in the dataset.'}
- {'step': 2, 'action': 'Match category count to available scheme sizes: 8 (Accent, Dark2, Pastel2, Set2), 9 (Pastel1, Set1), 10 (Category10, Observable10, Tableau10), or 12 (Paired, Set3).'}
- {'step': 3, 'action': 'Select scheme based on visual intent (e.g., Pastel for soft appearance, Dark2 for high contrast).'}
- {'step': 4, 'action': 'Retrieve the color array from d3.scheme[SelectedName].'}
- {'step': 5, 'action': 'Return array to caller for encoding or legend use.'}

## Constraints

- scheme selection must match or slightly exceed the number of categories
- output is a fixed array; no dynamic interpolation
- schemes are predefined; custom color mixing not supported by this skill

## Cautions

- Verify that the selected scheme has sufficient colors for your category count.
- Consider perceptual uniformity and accessibility when choosing between similar schemes.

## Output Contract

- Array of hex color strings matching the selected scheme (e.g., d3.schemeCategory10 returns 10 colors). Caller receives a direct reference to the color array for immediate use in encoding or legend generation.

## Triggers

- rendering categorical data with 8–12 distinct categories; need perceptually distinct colors

---
id: "97383e49-571c-52c0-b2d6-94994add9342"
name: "Logarithmic Scale Configuration"
description: "Create and configure quantitative logarithmic scales with base, tick computation, formatting, and domain normalization. Use when mapping data ranges to logarithmic visual encodings in charts or plots."
version: "0.1.0"
tags:
  - "logarithmic_scale"
  - "d3_scale"
  - "quantitative_encoding"
  - "tick_formatting"
  - "domain_normalization"
triggers:
  - "Data spans multiple orders of magnitude"
  - "Logarithmic visual encoding is required"
  - "Tick labels and domain bounds need standardization"
---

# Logarithmic Scale Configuration

Create and configure quantitative logarithmic scales with base, tick computation, formatting, and domain normalization. Use when mapping data ranges to logarithmic visual encodings in charts or plots.

## Prompt

To configure a logarithmic scale: (1) Create the scale using d3.scaleLog(). (2) Set the logarithm base if non-default using log.base(). (3) Compute representative tick values from the domain using log.ticks(). (4) Format tick labels for readability using log.tickFormat(). (5) Extend the domain to nice round numbers using log.nice(). Return the configured scale object ready for encoding data.

## Objective

Configure a logarithmic scale with ticks and formatting
## Applicable Signals

- Data spans multiple orders of magnitude
- Logarithmic visual encoding is required
- Tick labels and domain bounds need standardization
- Scale base customization is needed

## Contraindications

- Data is linear or categorical
- Negative or zero values dominate the domain
- Linear scale is more interpretable for the use case

## Workflow Steps

- {'step': 1, 'action': 'Create logarithmic scale', 'detail': 'Instantiate d3.scaleLog() to create a new logarithmic scale object'}
- {'step': 2, 'action': 'Set logarithm base', 'detail': 'Call log.base(value) to set the base of the logarithm (default is 10); use 2 for binary, e for natural logarithm, etc.'}
- {'step': 3, 'action': 'Compute representative ticks', 'detail': 'Call log.ticks() to generate an array of tick values from the domain suitable for axis labels'}
- {'step': 4, 'action': 'Format tick labels', 'detail': 'Call log.tickFormat() to obtain a formatter function for converting tick values to human-readable strings'}
- {'step': 5, 'action': 'Normalize domain bounds', 'detail': 'Call log.nice() to extend the domain to nice round numbers for cleaner visualization'}

## Constraints

- Domain values must be positive (logarithm is undefined for zero and negative numbers)
- Base must be a positive number greater than 1
- Scale must be applied to positive data ranges only

## Cautions

- Ensure domain does not contain zero or negative values before applying logarithmic scale
- Verify that logarithmic encoding is appropriate for the data distribution and audience interpretation
- Test tick formatting output to confirm readability at target resolution

## Output Contract

- Returns a configured logarithmic scale object with methods for domain setting, range setting, and value encoding. The scale is ready to encode positive numeric data and produce formatted tick labels for axis rendering.

## Triggers

- Data spans multiple orders of magnitude
- Logarithmic visual encoding is required
- Tick labels and domain bounds need standardization

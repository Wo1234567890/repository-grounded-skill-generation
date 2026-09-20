---
id: "89619032-1a42-5a12-9130-bac41f56be66"
name: "Symmetric Logarithmic Scale Setup"
description: "Create a symmetric logarithmic scale that handles both positive and negative values with a configurable constant parameter. Use when data includes negative ranges and logarithmic symmetry around zero is needed."
version: "0.1.0"
tags:
  - "scale"
  - "quantitative"
  - "logarithmic"
  - "symmetric"
  - "d3"
  - "encoding"
triggers:
  - "Data contains both positive and negative values"
  - "Logarithmic behavior is desired near zero and at extremes"
  - "Symmetric visual encoding around zero is required"
---

# Symmetric Logarithmic Scale Setup

Create a symmetric logarithmic scale that handles both positive and negative values with a configurable constant parameter. Use when data includes negative ranges and logarithmic symmetry around zero is needed.

## Prompt

Initialize a symlog scale using d3.scaleSymlog(). Set the constant parameter via symlog.constant() to control the transition behavior between linear and logarithmic regions. The constant determines the slope at zero and affects how smoothly the scale transitions from linear near zero to logarithmic at extremes.

## Objective

Set up a symlog scale with constant parameter configured
## Applicable Signals

- Domain spans negative to positive range
- Need for logarithmic compression at extremes
- Requirement for smooth transition through zero

## Contraindications

- Data is strictly positive (use d3.scaleLog instead)
- Linear scale is sufficient for the use case
- Domain does not cross zero

## Workflow Steps

- {'step': 1, 'action': 'Create symlog scale instance', 'detail': 'Call d3.scaleSymlog() to instantiate the scale'}
- {'step': 2, 'action': 'Configure constant parameter', 'detail': 'Call symlog.constant(value) to set the transition constant; typical range 1–10 depending on data'}
- {'step': 3, 'action': 'Bind domain and range', 'detail': 'Set .domain([min, max]) and .range([start, end]) to complete scale configuration'}

## Constraints

- Constant parameter must be a positive number
- Scale requires explicit domain and range binding after creation
- Symlog is asymptotically logarithmic; behavior near zero depends on constant value

## Cautions

- Constant value significantly affects scale behavior; test with domain-specific values
- Very small constant values may cause numerical instability near zero

## Output Contract

- Symlog scale object with constant parameter set, ready for domain/range binding and value mapping

## Triggers

- Data contains both positive and negative values
- Logarithmic behavior is desired near zero and at extremes
- Symmetric visual encoding around zero is required

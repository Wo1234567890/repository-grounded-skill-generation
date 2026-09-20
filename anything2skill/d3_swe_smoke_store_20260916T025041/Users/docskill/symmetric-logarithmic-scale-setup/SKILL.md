---
id: "20214464-3316-56b9-a291-cc015dc44474"
name: "Symmetric Logarithmic Scale Setup"
description: "Create a symmetric logarithmic scale that handles both positive and negative values with a configurable constant parameter. Use when data includes negative ranges and logarithmic symmetry around zero is needed."
version: "0.1.0"
tags:
  - "scale"
  - "quantitative"
  - "logarithmic"
  - "symmetric"
  - "d3"
triggers:
  - "Data spans negative and positive values"
  - "Logarithmic behavior is desired near zero and at extremes"
  - "Symmetric visual encoding around zero is required"
examples:
  - input: "Data range: [-1000, 1000]; constant: 1"
    output: "Symlog scale with symmetric compression; values near zero map linearly, extreme values compress logarithmically"
    notes: "Constant of 1 provides moderate transition; adjust higher for gentler transition, lower for sharper"
---

# Symmetric Logarithmic Scale Setup

Create a symmetric logarithmic scale that handles both positive and negative values with a configurable constant parameter. Use when data includes negative ranges and logarithmic symmetry around zero is needed.

## Prompt

Initialize a symlog scale using d3.scaleSymlog(). Set the constant parameter via symlog.constant() to control the transition behavior between linear and logarithmic regions. Bind domain and range after configuration.

## Objective

Set up a symlog scale with constant parameter
## Applicable Signals

- Dataset contains both negative and positive numeric values
- Visualization requires logarithmic compression at extremes
- Domain crosses zero

## Contraindications

- Data is strictly positive (use d3.scaleLog instead)
- Linear scale is sufficient for the use case
- Domain does not cross zero

## Intervention Moves

- Call d3.scaleSymlog() to instantiate the scale
- Invoke symlog.constant(value) to set the constant parameter
- Bind domain via .domain([min, max])
- Bind range via .range([output_min, output_max])

## Workflow Steps

- {'step': 1, 'action': 'Instantiate symlog scale', 'detail': 'const scale = d3.scaleSymlog();'}
- {'step': 2, 'action': 'Configure constant parameter', 'detail': 'scale.constant(1); // Adjust value based on data range and desired transition behavior'}
- {'step': 3, 'action': 'Set domain', 'detail': 'scale.domain([-max_value, max_value]); // Symmetric domain around zero'}
- {'step': 4, 'action': 'Set range', 'detail': 'scale.range([0, width]); // Or other output range'}

## Constraints

- Constant parameter must be a positive number
- Domain must include both negative and positive values for symmetric behavior to be meaningful

## Cautions

- Symlog scales are more complex than linear or standard log scales; verify constant tuning produces expected visual output
- Tick generation and formatting may require custom handling for clarity across the symmetric range

## Output Contract

- Symlog scale object with constant parameter set and ready for domain/range binding. Caller receives a configured scale function that maps input values to output range with symmetric logarithmic behavior.

## Example Therapist Responses

### Example 1

- Client/Input: Data range: [-1000, 1000]; constant: 1
- Therapist/Output: Symlog scale with symmetric compression; values near zero map linearly, extreme values compress logarithmically
- Notes: Constant of 1 provides moderate transition; adjust higher for gentler transition, lower for sharper

## Triggers

- Data spans negative and positive values
- Logarithmic behavior is desired near zero and at extremes
- Symmetric visual encoding around zero is required

## Examples

### Example 1

Input:

  Data range: [-1000, 1000]; constant: 1

Output:

  Symlog scale with symmetric compression; values near zero map linearly, extreme values compress logarithmically

Notes:

  Constant of 1 provides moderate transition; adjust higher for gentler transition, lower for sharper

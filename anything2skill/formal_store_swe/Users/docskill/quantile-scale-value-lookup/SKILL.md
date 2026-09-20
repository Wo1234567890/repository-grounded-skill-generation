---
id: "a286b247-ce61-5ac7-8e36-e3cd81f305ad"
name: "Quantile Scale Value Lookup"
description: "Query a configured quantile scale to retrieve the output range value for a given input domain value, or invert to find domain values for a given range value. Use for encoding individual data points or decoding range selections in visualization or interaction contexts."
version: "0.1.0"
tags:
  - "scale"
  - "quantile"
  - "lookup"
  - "encoding"
  - "decoding"
  - "value_transformation"
triggers:
  - "A quantile scale is already configured with domain and range"
  - "Need to encode a single data point using the scale"
  - "Need to decode a range selection back to domain values"
examples:
  - input: "quantile scale configured with domain [0, 100] and range ['red', 'yellow', 'green']; query domainValue = 45"
    output: "rangeValue = 'yellow'"
    notes: "Forward lookup maps the domain value to its corresponding quantile bin's range value"
  - input: "quantile scale configured with domain [0, 100] and range ['red', 'yellow', 'green']; query rangeValue = 'yellow'"
    output: "domainExtent = [33.33, 66.67]"
    notes: "Inverse lookup returns the domain range that maps to the given range value"
---

# Quantile Scale Value Lookup

Query a configured quantile scale to retrieve the output range value for a given input domain value, or invert to find domain values for a given range value. Use for encoding individual data points or decoding range selections in visualization or interaction contexts.

## Prompt

Given a quantile scale that is already configured with domain and range, use the scale's quantile() method to map a domain value to its corresponding range value. Alternatively, use quantile.invertExtent() to map a range value back to the domain extent [min, max]. Ensure the input value is within the scale's configured bounds before querying.

## Objective

Transform a domain value to range value or invert a range value to domain extent
## Applicable Signals

- scale.quantile(value) invocation required
- scale.invertExtent(value) invocation required
- Single-value lookup (not batch transformation)

## Contraindications

- Scale is not yet configured or domain/range not set
- Batch transformation needed (use map or forEach instead)
- Domain value is outside the scale's configured domain
- Range value is outside the scale's configured range

## Workflow Steps

- {'step': 1, 'action': 'Verify the quantile scale is configured', 'detail': 'Confirm scale.domain() and scale.range() have been set'}
- {'step': 2, 'action': 'Choose lookup direction', 'detail': 'Determine whether to map domain→range (forward) or range→domain (inverse)'}
- {'step': 3, 'action': 'Execute forward lookup', 'detail': 'Call scale.quantile(domainValue) to get the corresponding range value'}
- {'step': 4, 'action': 'Execute inverse lookup', 'detail': 'Call scale.invertExtent(rangeValue) to get the domain extent [min, max]'}
- {'step': 5, 'action': 'Return result', 'detail': 'Provide the range value (forward) or domain extent array (inverse) to the caller'}

## Constraints

- Input value must be within the scale's configured bounds
- Scale must have been initialized with domain() and range() before querying
- Forward query returns a single range value; inverse query returns a domain extent array

## Cautions

- Quantile scales divide the domain into equal-probability bins; edge values may map to the same range value
- invertExtent() returns the domain extent for a given range value, not a single point

## Output Contract

- Forward query returns a single output range value ready for visualization binding. Inverse query returns a domain extent array [min, max] representing the domain values that map to the given range value. Both outputs are immediately usable for downstream visualization or interaction logic.

## Example Executions

### Example 1

- Input: quantile scale configured with domain [0, 100] and range ['red', 'yellow', 'green']; query domainValue = 45
- Output: rangeValue = 'yellow'
- Notes: Forward lookup maps the domain value to its corresponding quantile bin's range value

### Example 2

- Input: quantile scale configured with domain [0, 100] and range ['red', 'yellow', 'green']; query rangeValue = 'yellow'
- Output: domainExtent = [33.33, 66.67]
- Notes: Inverse lookup returns the domain range that maps to the given range value

## Triggers

- A quantile scale is already configured with domain and range
- Need to encode a single data point using the scale
- Need to decode a range selection back to domain values

## Examples

### Example 1

Input:

  quantile scale configured with domain [0, 100] and range ['red', 'yellow', 'green']; query domainValue = 45

Output:

  rangeValue = 'yellow'

Notes:

  Forward lookup maps the domain value to its corresponding quantile bin's range value

### Example 2

Input:

  quantile scale configured with domain [0, 100] and range ['red', 'yellow', 'green']; query rangeValue = 'yellow'

Output:

  domainExtent = [33.33, 66.67]

Notes:

  Inverse lookup returns the domain range that maps to the given range value

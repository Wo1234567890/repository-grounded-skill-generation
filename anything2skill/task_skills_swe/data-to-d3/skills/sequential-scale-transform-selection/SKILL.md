---
id: "1c288611-d13b-5081-b35c-178add510064"
name: "Sequential Scale Transform Selection"
description: "Select and apply the appropriate mathematical transform (linear, logarithmic, power, symmetric logarithmic, or quantile) when creating a sequential scale to match data distribution characteristics."
version: "0.1.0"
tags:
  - "d3"
  - "scale"
  - "sequential"
  - "transform"
  - "data-encoding"
  - "initialization"
triggers:
  - "Initializing a sequential scale"
  - "Need to match scale type to data characteristics"
  - "Data exhibits exponential, polynomial, symmetric, or percentile-based patterns"
---

# Sequential Scale Transform Selection

Select and apply the appropriate mathematical transform (linear, logarithmic, power, symmetric logarithmic, or quantile) when creating a sequential scale to match data distribution characteristics.

## Prompt

When initializing a sequential scale, choose the correct scale constructor based on your data distribution:
- Use d3.scaleSequentialLog for exponential or multiplicative data.
- Use d3.scaleSequentialPow for polynomial relationships; d3.scaleSequentialSqrt for square-root relationships.
- Use d3.scaleSequentialSymlog for data spanning zero with mixed magnitudes.
- Use d3.scaleSequentialQuantile for percentile-based or rank-ordered encoding.
Invoke the selected constructor and pass your domain and interpolator to complete the scale.

## Objective

Choose the correct sequential scale constructor based on data distribution
## Applicable Signals

- Exponential or multiplicative data distribution → logarithmic transform
- Polynomial or power-law relationships → power or sqrt transform
- Data spanning zero with mixed magnitudes → symmetric logarithmic transform
- Percentile-based or rank-ordered encoding → quantile transform

## Contraindications

- Data is categorical
- Using non-sequential scale types (ordinal, band, point)
- Transform is already baked into data preprocessing
- Scale type is fixed by external specification

## Workflow Steps

- {'step': 1, 'action': 'Analyze data distribution characteristics', 'detail': 'Determine if data is exponential, polynomial, symmetric around zero, or percentile-based'}
- {'step': 2, 'action': 'Select appropriate scale constructor', 'detail': 'Match data pattern to constructor: Log, Pow, Sqrt, Symlog, or Quantile'}
- {'step': 3, 'action': 'Invoke selected constructor', 'detail': 'Call d3.scaleSequential[Transform]() to create scale instance'}
- {'step': 4, 'action': 'Configure domain and interpolator', 'detail': 'Set scale domain and interpolator via chained methods'}

## Constraints

- Must select exactly one transform type per scale instance
- Transform selection must occur before domain and interpolator assignment
- Selected constructor must be compatible with continuous quantitative domain

## Cautions

- Incorrect transform selection can distort data representation and mislead visualization consumers
- Symmetric logarithmic transform requires careful handling of zero-crossing data
- Quantile transform requires pre-computed quantile array

## Output Contract

- Correct scale constructor invoked (d3.scaleSequentialLog, d3.scaleSequentialPow, d3.scaleSequentialSqrt, d3.scaleSequentialSymlog, or d3.scaleSequentialQuantile) matching data distribution; scale instance ready for domain and interpolator configuration.

## Triggers

- Initializing a sequential scale
- Need to match scale type to data characteristics
- Data exhibits exponential, polynomial, symmetric, or percentile-based patterns

---
id: "14cd600d-122b-5a58-b13a-625c8cd0a23e"
name: "Statistical Distribution Random Variate Generation"
description: "Generate pseudorandom numbers from 16 named statistical distributions (uniform, normal, exponential, Poisson, binomial, beta, gamma, Weibull, Cauchy, logistic, geometric, Bernoulli, Bates, Irwin–Hall, log-normal, Pareto) with optional reproducible seeding via LCG. Use when sim..."
version: "0.1.0"
tags:
  - "random_sampling"
  - "statistical_distribution"
  - "Monte_Carlo"
  - "simulation"
  - "pseudorandom"
  - "d3_random"
triggers:
  - "Need to sample from a named distribution (normal, exponential, Poisson, binomial, beta, gamma, Weibull, Cauchy, logistic, geometric, Bernoulli, Bates, Irwin–Hall, log-normal, Pareto)"
  - "Require reproducible randomness via seed control"
---

# Statistical Distribution Random Variate Generation

Generate pseudorandom numbers from 16 named statistical distributions (uniform, normal, exponential, Poisson, binomial, beta, gamma, Weibull, Cauchy, logistic, geometric, Bernoulli, Bates, Irwin–Hall, log-normal, Pareto) with optional reproducible seeding via LCG. Use when sim...

## Prompt

Invoke the appropriate d3.random* function for your target distribution. Pass distribution parameters (e.g., mean and standard deviation for normal; shape and scale for Weibull). Optionally set random.source to a seeded LCG (d3.randomLcg) for reproducibility. Call the returned generator function repeatedly to obtain variates.

## Objective

Provide callable random variate generators for 16 common probability distributions with optional seed control
## Applicable Signals

- Need to sample from a named distribution (uniform, normal, exponential, Poisson, binomial, beta, gamma, Weibull, Cauchy, logistic, geometric, Bernoulli, Bates, Irwin–Hall, log-normal, Pareto)
- Require reproducible randomness via seed control
- Simulation or Monte Carlo sampling workflow initiated

## Contraindications

- Cryptographic randomness required
- Deterministic sequences needed instead of stochastic sampling
- Distribution not in the supported list (16 named distributions only)

## Workflow Steps

- Select target distribution from supported list
- Gather required parameters for chosen distribution
- Optionally initialize d3.randomLcg with seed for reproducibility
- Invoke corresponding d3.random* function with parameters
- Call returned generator function repeatedly to obtain variates

## Constraints

- LCG seeding is optional; without it, randomness is non-reproducible
- Each distribution function has specific parameter requirements; incorrect parameters will produce invalid or unexpected results

## Cautions

- Seeding via d3.randomLcg is not cryptographically secure; do not use for security-sensitive applications
- Distribution parameters must be valid for the chosen distribution (e.g., shape > 0 for gamma, 0 < p < 1 for Bernoulli)

## Output Contract

- Array or stream of random variates matching the specified distribution parameters and seeded state; each call to the generator function returns one variate

## Triggers

- Need to sample from a named distribution (normal, exponential, Poisson, binomial, beta, gamma, Weibull, Cauchy, logistic, geometric, Bernoulli, Bates, Irwin–Hall, log-normal, Pareto)
- Require reproducible randomness via seed control

---
id: "b0753993-afce-5508-a1a7-2fd97d825dbe"
name: "Generate random variates from statistical distributions"
description: "Generate pseudorandom numbers from 15+ named statistical distributions (uniform, normal, exponential, Poisson, binomial, beta, gamma, Weibull, Cauchy, logistic, geometric, Bernoulli, Bates, Irwin–Hall, log-normal, Pareto) with optional seeding via LCG source. Use when simulation, Monte Carlo sampling, or stochastic modeling requires reproducible random variates."
version: "0.1.0"
tags:
  - "random_sampling"
  - "statistical_distribution"
  - "Monte_Carlo"
  - "simulation"
  - "pseudorandom"
  - "reproducible_randomness"
triggers:
  - "Need to sample from a named distribution (normal, exponential, Poisson, binomial, beta, gamma, Weibull, Cauchy, logistic, geometric, Bernoulli, Bates, Irwin–Hall, log-normal, Pareto); require reproducible randomness via seed control"
---

# Generate random variates from statistical distributions

Generate pseudorandom numbers from 15+ named statistical distributions (uniform, normal, exponential, Poisson, binomial, beta, gamma, Weibull, Cauchy, logistic, geometric, Bernoulli, Bates, Irwin–Hall, log-normal, Pareto) with optional seeding via LCG source. Use when simulation, Monte Carlo sampling, or stochastic modeling requires reproducible random variates.

## Prompt

Invoke the appropriate d3.random* function for your target distribution. Pass distribution parameters (e.g., mean, standard deviation for normal; shape and scale for Weibull). Optionally set random.source to a seeded LCG (d3.randomLcg) for reproducibility. Call the returned generator function repeatedly to obtain variates.

## Objective

Provide callable random variate generators for common probability distributions
## Applicable Signals

- Need to sample from a named distribution (normal, exponential, Poisson, binomial, beta, gamma, Weibull, Cauchy, logistic, geometric, Bernoulli, Bates, Irwin–Hall, log-normal, Pareto)
- Require reproducible randomness via seed control
- Simulation or Monte Carlo sampling task initiated

## Contraindications

- Cryptographic randomness required
- Deterministic sequences needed instead of stochastic sampling
- Distribution not in the supported list (uniform, int, normal, log-normal, Bates, Irwin–Hall, exponential, Pareto, Bernoulli, geometric, binomial, gamma, beta, Weibull, Cauchy, logistic, Poisson)

## Constraints

- LCG seeding is optional; if reproducibility is critical, seed before generating variates
- Each distribution function returns a generator; call the generator repeatedly to obtain multiple variates

## Cautions

- Unseeded generators use Math.random() and are not reproducible across runs
- Parameter ranges and semantics vary by distribution; consult distribution documentation for valid inputs

## Output Contract

- Array or stream of random variates matching the specified distribution parameters and seeded state; each call to the generator function returns one variate

## Triggers

- Need to sample from a named distribution (normal, exponential, Poisson, binomial, beta, gamma, Weibull, Cauchy, logistic, geometric, Bernoulli, Bates, Irwin–Hall, log-normal, Pareto); require reproducible randomness via seed control

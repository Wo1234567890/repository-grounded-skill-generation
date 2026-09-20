---
id: "53d0fca2-5bbc-5b9c-8b0e-503ea09b80ba"
name: "Virtual Hub Routing Concepts Reference"
description: "Reference taxonomy for classifying route leak incidents into Types 1–4 based on the policy violation context between source AS and destination AS roles. Enables standardized incident categorization and pattern analysis across documented route leak events."
version: "0.1.1"
tags:
  - "route_leak"
  - "classification"
  - "BGP"
  - "policy_violation"
  - "incident_analysis"
triggers:
  - "Designing virtual hub routing topology"
  - "Troubleshooting routing behavior"
  - "Onboarding team members to Virtual WAN routing model"
---

# Virtual Hub Routing Concepts Reference

Reference taxonomy for classifying route leak incidents into Types 1–4 based on the policy violation context between source AS and destination AS roles. Enables standardized incident categorization and pattern analysis across documented route leak events.

## Prompt

When analyzing a route leak incident, identify the source AS and destination AS roles involved. Determine which of Types 1–4 best describes the policy violation context. Types 1–4 all involve route leaks in violation of policy, but differ in the roles and relationships of the source and destination ASes. Document the assigned type and the AS role context to enable consistent incident tracking and pattern analysis.

## Objective

Provide a reference taxonomy for route leak classification based on policy violation context
## Applicable Signals

- Route leak incident detected and requires type assignment
- Multiple leak events need to be compared for pattern analysis
- Incident documentation requires standardized type classification

## Contraindications

- Do not use for real-time BGP filtering or route validation
- Do not use for implementing automated leak prevention mechanisms
- Not suitable for operational routing decisions; use only for post-incident analysis and categorization

## Workflow Steps

- Identify source AS and destination AS roles in the leak incident
- Determine policy violation context
- Map incident to Types 1–4 framework
- Document assigned type with AS role context

## Constraints

- Classification requires clear identification of source AS and destination AS roles
- Types 1–4 framework assumes policy violation context is known or can be determined

## Output Contract

- Route leak incident assigned to one of Types 1–4 with documented source and destination AS roles and policy violation context

## Triggers

- Designing virtual hub routing topology
- Troubleshooting routing behavior
- Onboarding team members to Virtual WAN routing model

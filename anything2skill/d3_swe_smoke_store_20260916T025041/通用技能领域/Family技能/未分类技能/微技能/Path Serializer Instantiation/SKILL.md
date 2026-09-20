---
id: "c69dcb33-41ce-5497-9369-d6d806584ef3"
name: "Path Serializer Instantiation"
description: "Create a new path serializer object to begin a path drawing session. Choose standard precision with d3.path() or fixed decimal precision with d3.pathRound() based on output requirements."
version: "0.1.0"
tags:
  - "d3"
  - "path"
  - "serialization"
  - "graphics"
  - "initialization"
  - "svg"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "starting a new path drawing session"
  - "need a fresh path object"
  - "require precision control for serialized output"
examples:
  - input: "Start drawing with standard precision"
    output: "path = d3.path(); path ready for commands"
    notes: "Use for typical SVG rendering"
  - input: "Start drawing with fixed decimal precision"
    output: "path = d3.pathRound(); path ready for commands with rounded output"
    notes: "Use when output precision must be controlled"
---

# Path Serializer Instantiation

Create a new path serializer object to begin a path drawing session. Choose standard precision with d3.path() or fixed decimal precision with d3.pathRound() based on output requirements.

## Prompt

Instantiate a path serializer before executing any drawing commands. Select d3.path() for standard SVG path precision or d3.pathRound() when fixed decimal output precision is required. The returned object is ready to accept moveTo, lineTo, arc, and other drawing commands.

## Objective

instantiate path serializer
## Applicable Signals

- session begins
- prior path finalized or closed
- precision requirement specified

## Contraindications

- reusing an existing path object
- path is already closed and finalized
- drawing commands already queued on active path

## Workflow Steps

- {'step': 1, 'action': 'Determine precision requirement', 'detail': 'Decide whether standard SVG precision or fixed decimal rounding is needed'}
- {'step': 2, 'action': 'Invoke serializer constructor', 'detail': 'Call d3.path() for standard precision or d3.pathRound() for fixed decimal precision'}
- {'step': 3, 'action': 'Receive path object', 'detail': 'Capture returned serializer object ready for drawing commands'}

## Constraints

- Instantiation must occur before any drawing command (moveTo, lineTo, arc, etc.)
- Choose precision variant (standard or rounded) before instantiation; cannot change mid-session

## Cautions

- d3.pathRound() applies fixed decimal rounding; verify precision meets output requirements
- Path object is stateful; reusing across multiple independent drawings may cause command accumulation

## Output Contract

- Path serializer object ready to accept drawing commands (moveTo, lineTo, arc, quadraticCurveTo, bezierCurveTo, arcTo, rect, closePath). Object maintains internal command queue and can serialize to SVG path data string via toString().

## Example Therapist Responses

### Example 1

- Client/Input: Start drawing with standard precision
- Therapist/Output: path = d3.path(); path ready for commands
- Notes: Use for typical SVG rendering

### Example 2

- Client/Input: Start drawing with fixed decimal precision
- Therapist/Output: path = d3.pathRound(); path ready for commands with rounded output
- Notes: Use when output precision must be controlled

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- starting a new path drawing session
- need a fresh path object
- require precision control for serialized output

## Examples

### Example 1

Input:

  Start drawing with standard precision

Output:

  path = d3.path(); path ready for commands

Notes:

  Use for typical SVG rendering

### Example 2

Input:

  Start drawing with fixed decimal precision

Output:

  path = d3.pathRound(); path ready for commands with rounded output

Notes:

  Use when output precision must be controlled

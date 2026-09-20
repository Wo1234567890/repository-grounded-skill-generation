---
id: "7046d4d5-e184-57df-b145-fcc4dacd4ee0"
name: "Identify Third-Party Content Control Constraints"
description: "Assess the degree of control over late-loaded content (ads, embeds, iframes) to determine which CLS mitigation techniques are feasible, accounting for unknown dimensions and embedded layout shifts."
version: "0.1.0"
tags:
  - "layout_shift"
  - "cls"
  - "third_party_content"
  - "constraint_analysis"
  - "web_performance"
triggers:
  - "Evaluating CLS caused by third-party content (ad partners, external embeds)"
  - "Determining which prevention or mitigation strategies can be applied to late-loaded content"
  - "Assessing control over dynamically injected ads, iframes, or embeds"
---

# Identify Third-Party Content Control Constraints

Assess the degree of control over late-loaded content (ads, embeds, iframes) to determine which CLS mitigation techniques are feasible, accounting for unknown dimensions and embedded layout shifts.

## Prompt

When evaluating CLS caused by third-party content, determine: (1) whether content dimensions are known or unknown, (2) whether layout shifts occur within the embed or affect surrounding content, (3) which mitigation strategies are applicable given your control level. If you have no control over the content (e.g., ad partner), you cannot prevent internal shifts but can still reserve space or adjust placement. Document these constraints before selecting a mitigation technique.

## Objective

assess_mitigation_feasibility
## Applicable Signals

- Third-party content insertion detected
- Unknown content dimensions
- Layout shifts in content following embeds
- Ad partner or external embed integration

## Contraindications

- Content is first-party and fully controllable
- No third-party dependencies exist
- CLS is caused by user interactions or animations
- Content dimensions and behavior are fully known and controlled

## Workflow Steps

- {'step': 1, 'action': 'Identify the source of late-loaded content', 'detail': 'Determine whether content is inserted by a third-party (ad partner, external service) or first-party'}
- {'step': 2, 'action': 'Assess dimension knowledge', 'detail': 'Document whether the final dimensions of the content are known, partially known, or unknown'}
- {'step': 3, 'action': 'Map shift locations', 'detail': 'Identify whether layout shifts occur within the embed itself or affect surrounding content'}
- {'step': 4, 'action': 'Determine control level', 'detail': "Assess your ability to control the content's size, timing, and internal layout"}
- {'step': 5, 'action': 'Match applicable techniques', 'detail': 'Based on control level, identify which mitigation strategies are feasible (space reservation, placement adjustment, or acceptance of limited control)'}

## Constraints

- Third-party content may have unknown final dimensions
- Internal layout shifts within embeds may be uncontrollable
- Control level determines which mitigation techniques are feasible

## Cautions

- Do not assume you can control layout shifts within third-party embeds
- Distinguish between shifts you can prevent (space reservation, placement) and shifts you cannot (internal embed behavior)

## Output Contract

- Clear mapping of which content dimensions are known vs. unknown; identification of which layout shifts occur within vs. outside the embed; decision on applicable mitigation technique (space reservation, placement, or acceptance of limited control).

## Triggers

- Evaluating CLS caused by third-party content (ad partners, external embeds)
- Determining which prevention or mitigation strategies can be applied to late-loaded content
- Assessing control over dynamically injected ads, iframes, or embeds

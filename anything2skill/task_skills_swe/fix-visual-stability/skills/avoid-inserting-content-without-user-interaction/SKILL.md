---
id: "2b4b1a7a-f586-51b3-9394-8759f4b9cb94"
name: "Avoid inserting content without user interaction"
description: "Prevent unexpected layout shifts by gating dynamic content insertion behind explicit user actions. This safety rule ensures that ads, notifications, modals, and other late-loaded content only appear in response to user interaction, maintaining stable layout and predictable CLS."
version: "0.1.0"
tags:
  - "layout_shift"
  - "CLS"
  - "content_insertion"
  - "user_interaction"
  - "safety"
  - "web_performance"
triggers:
  - "Designing content insertion patterns; evaluating ad placement, notification, or modal strategies; reviewing auto-play or auto-load behaviors"
---

# Avoid inserting content without user interaction

Prevent unexpected layout shifts by gating dynamic content insertion behind explicit user actions. This safety rule ensures that ads, notifications, modals, and other late-loaded content only appear in response to user interaction, maintaining stable layout and predictable CLS.

## Prompt

When designing or reviewing content insertion patterns, enforce that all dynamic content (ads, embeds, notifications, modals) appears only after explicit user action such as click, scroll-to, or expand. Do not auto-inject content into the viewport during passive browsing or page load. Verify that any auto-play or auto-load behavior is either disabled or gated behind user interaction.

## Objective

Eliminate layout shifts caused by unsolicited content insertion
## Applicable Signals

- Designing content insertion patterns for ads, notifications, or modals
- Evaluating auto-play or auto-load behavior in page design
- Reviewing dynamic content injection strategies
- Assessing CLS impact of late-loaded content

## Contraindications

- Content is part of initial page load or critical to page function
- User has explicitly requested content (e.g., clicked expand button)
- Content must load immediately for accessibility or usability reasons

## Intervention Moves

- Gate ad insertion behind user click or expand action
- Disable auto-play for embedded media unless user explicitly enables it
- Require user interaction before showing modals, notifications, or overlays

## Constraints

- All dynamic insertions must be user-triggered
- Auto-play and auto-load behaviors must be disabled or gated
- Content insertion must not occur during passive browsing

## Cautions

- Distinguish between initial page load (exempt) and subsequent dynamic insertions (gated)
- Ensure user interaction is explicit and intentional, not accidental hover or scroll
- Test across form factors and interaction patterns to confirm no unsolicited content appears

## Output Contract

- No unsolicited content appears in viewport during passive browsing
- All dynamic insertions are user-triggered
- CLS remains stable and predictable
- Layout does not shift due to unannounced content injection

## Triggers

- Designing content insertion patterns; evaluating ad placement, notification, or modal strategies; reviewing auto-play or auto-load behaviors

---
id: "261678cc-7a60-52bd-a859-8c97684cc8a8"
name: "Apply Custom Property Tweens During Transition"
description: "Define and execute custom interpolation logic for individual attributes, styles, or text content during an active transition using tween functions. Enables frame-by-frame control over property animation when default interpolators are insufficient."
version: "0.1.0"
tags:
  - "d3"
  - "transition"
  - "animation"
  - "tween"
  - "interpolation"
  - "custom_easing"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Default interpolator is insufficient; need frame-by-frame control over property animation; animating non-standard properties or computed values"
---

# Apply Custom Property Tweens During Transition

Define and execute custom interpolation logic for individual attributes, styles, or text content during an active transition using tween functions. Enables frame-by-frame control over property animation when default interpolators are insufficient.

## Prompt

To apply a custom tween during a transition:
1. Call transition.attrTween(name, function) to tween an attribute with a custom interpolator.
2. Call transition.styleTween(name, function) to tween a style property with a custom interpolator.
3. Call transition.textTween(function) to tween text content with a custom interpolator.
4. Call transition.tween(name, function) to run custom code during the transition.
5. The tween function receives the current datum and index, and must return an interpolator function.
6. The interpolator function receives a time value (0 to 1) and returns the interpolated value for that frame.
7. Return the interpolated value from the interpolator to update the property on each animation frame.

## Objective

Interpolate a single property or text value using a custom tween function during an active transition
## Applicable Signals

- Default interpolator is insufficient for the target property
- Need frame-by-frame control over property animation
- Animating non-standard properties or computed values
- Custom easing or value transformation required during animation

## Contraindications

- Simple linear or standard easing of standard CSS properties suffices
- No custom interpolation logic required
- Default d3 interpolators handle the property adequately

## Intervention Moves

- Define tween function that accepts datum and index
- Return interpolator function from tween
- Interpolator receives normalized time (0–1) and returns interpolated value
- Attach tween to transition via attrTween, styleTween, textTween, or tween

## Constraints

- Tween function must return a valid interpolator function
- Interpolator must accept a time parameter (0 to 1)
- Interpolator must return a value compatible with the target property
- Tween executes within the active transition lifecycle

## Cautions

- Performance: complex tween logic runs on every animation frame; optimize for frame rate
- Ensure interpolator handles edge cases (t=0 and t=1) correctly
- Custom tweens do not inherit default easing; apply easing logic inside the interpolator if needed

## Output Contract

- Tween function executes on each animation frame, returning interpolated value; property updates smoothly from start to end state over the transition duration.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Default interpolator is insufficient; need frame-by-frame control over property animation; animating non-standard properties or computed values

---
type: patch
title: "Pres-Link Tone Sweep — dark-to-bright in one knob"
device: Chase Bliss Brothers AM
date: 2026-06-15
description: 'Chase Bliss''s demonstrated PRES LINK trick — link TONE and PRESENCE so they move together, turning the TONE knob into a single, dramatic control that sweeps from very dark to very bright. Joel Korte demos it in DISTORTION with the gain way up (CB Technical Demo): the same TONE knob takes you across the whole tonal range. A performance/expression-friendly voicing where one knob (or one expression sweep) does big tonal moves.'
tags: [pres-link, distortion, tone-sweep, expression, performance, designed]
dips:
  PRES LINK (the channel): "ON (links TONE + PRESENCE so they move together)"
  CONTROL bank (right side, optional): "assign EXP (or 0–5V CV) → TONE for a foot-swept dark→bright move"
controls:
  - { name: "CHANNEL MODE", type: switch, value: "DISTORTION (Joel's demo) for the most dramatic sweep; any mode works", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN", type: knob, value: "up — the higher the gain, the more dramatic the dark→bright sweep; dial from recipe, no published clock" }
  - { name: "TONE", type: knob, value: "the single dark→bright control (now sweeping TONE + PRESENCE together via PRES LINK); dial from recipe" }
  - { name: "VOL", type: knob, value: "dial from recipe" }
  - { name: "PRESENCE", type: knob, value: "follows TONE while PRES LINK is ON — no separate setting" }
  - { name: "PRES LINK", type: switch, value: "ON (the dip that links TONE + PRESENCE for the dramatic single-knob sweep)" }
  - { name: "EXP/CV", type: button, value: "optional — assign to TONE via the CONTROL (right-side) dips so your foot sweeps dark→bright" }
---

# Pres-Link Tone Sweep — dark-to-bright in one knob

## Concept
Chase Bliss's demonstrated PRES LINK trick: turn the PRES LINK dip on so TONE and PRESENCE move together, collapsing two tone controls into one dramatic knob that sweeps from very dark to very bright. Joel Korte demos it in DISTORTION with the gain way up (CB Technical Demo) — the same TONE knob takes you across the whole tonal range in a single move. It's a performance-minded voicing: one knob (or one expression sweep) does the big tonal moves on a hard-clipped voice. Related to, but distinct from, the full-range/synth PRES LINK patch — this one chases the dramatic single-knob tone sweep as a performance tool.

## How to play it
1. Turn the PRES LINK dip ON for your channel — TONE and PRESENCE now move together.
2. Set the channel to DISTORTION with the gain up (Joel's demo) for the most dramatic effect.
3. Sweep the TONE knob: it now goes from very dark to very bright in one move.
4. For a performance move, assign an expression pedal to TONE on the CONTROL (right-side) dip bank so your foot does the dark→bright sweep — a filter-sweep-like effect on a hard-clipped voice.

## Notes
- CB-quoted: the PRES LINK behavior and the dark→bright demo (DISTORTION, gain up) are quoted; no exact knob numbers are published — dial GAIN/TONE/VOL from the recipe.
- Related to but distinct from the full-range/synth PRES LINK patch: this one chases the dramatic single-knob tone sweep as a performance tool, not the full tonal range for synth-like voicing.
- Pairs well with expression-over-TONE for a filter-sweep-like effect on a hard-clipped voice; on a Morningstar/MIDI controller, set expression rules at the BANK level, not the preset level (documented gotcha).

## Sources
- research/transcripts/cb-technical-demo.md (PRES LINK "makes for a more dramatic tone control," demoed in DISTORTION gain up: "very dark… can get very bright as well")
- research/links/cb-technical-demo-settings.md (PRES LINK use)
- Ref: Brothers AM manual, "Customize" (PRES LINK)

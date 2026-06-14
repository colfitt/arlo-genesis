---
type: patch
title: Two-Personality Patch (rig signature)
device: Chase Bliss Onward
date: 2026-06-14
description: A hands-free Freeze sub-drone underneath + a Playback-error Glitch tracking your playing on top — a pad + tracking glitch nothing else in the rig does.
tags: [two-channel, routing, freeze, glitch, sub-drone, tracking, centerpiece, designed, signature]
hidden:
  BALANCE (on MIX): split the two voices' relative loudness
  ROUTING (per-section): route ERROR/Effects to one channel so each voice stays distinct
controls:
  - { name: "FREEZE channel", type: switch, value: "locked sub-drone (OCTAVE down, SUSTAIN max, hold-to-lock)" }
  - { name: "GLITCH channel", type: switch, value: "live, TYPE = PLAYBACK errors, ERROR up" }
  - { name: "OCTAVE (Freeze)", type: knob, value: "down" }
  - { name: "SUSTAIN (Freeze)", type: knob, value: "max" }
  - { name: "TYPE (Glitch)", type: switch, value: "PLAYBACK", options: ["Timing", "Condition", "Playback"] }
  - { name: "ERROR (Glitch)", type: knob, value: "up" }
  - { name: "Slot/Bank", type: knob, value: "Onboard L or R — the rig's centerpiece Onward preset" }
---

# Two-Personality Patch (rig signature)

## Concept
A hands-free Freeze sub-drone underneath + a Playback-error Glitch tracking your playing on top — a pad + tracking glitch nothing else in the rig does. Think of it as Complex Couple tuned to drone + tracking glitch for the banjo/baritone. Use hidden BALANCE (on MIX) + per-section ROUTING to split the two voices so each stays distinct.

## How to play it
1. Set **FREEZE = locked sub-drone**: OCTAVE down, SUSTAIN max, hold-to-lock.
2. Set **GLITCH = live**: TYPE = PLAYBACK errors, ERROR up.
3. Use hidden **BALANCE (on MIX)** to set the relative loudness of the two channels.
4. Route ERROR/Effects to one channel via the hidden per-section ROUTING toggles so each voice stays distinct.

## Notes
- The rig recipe, but the underlying example (sub-octave Freeze + playback-error Glitch via per-section routing) is **verbatim from Doug Hanson's demo**; the BALANCE/ROUTING mechanics are manual-verified.
- Think of it as Complex Couple (complex-couple) tuned to drone + tracking glitch for the banjo/baritone.

## Sources
- designed from UsageGuide §5 + `research/transcripts/doug-hanson-onward-demo-feature-rundown.md` + `aaron-rusch-onward-hidden-options.md` + `research/links/delaydude-onward-review-usage.md`
- Transformed from Pedalxly Onward-Patches.md (designed)

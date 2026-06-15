---
type: patch
title: "Prism Shift — Arpeggiated Shimmer Cloud (freeze + solo)"
device: Eventide H90
date: 2026-06-15
description: "Polyphonic pitch shifter that arpeggiates multiple shifted voices into a rising/falling cloud of glassy notes — FREEZE it for a sustained sparkling pad to play over. A manual-sourced arp recipe distinct from the existing prismshift-self-generating-stereo-arp-bed and the factory 'Sequential Chimes' seeds. Arp types, step length, the six shift ratios, per-voice controls and FREEZE/SHIFT behavior are from the Eventide manual; exact knob values are not published — dial from recipe."
tags: [prism-shift, pitch, arpeggio, shimmer, freeze, pad, ambient]
dips:
  STEP_LENGTH: "set to 1/8 or 1/16 (tempo-sync) for a steady cloud"
  SHIFT_RATIO: "pick a wide ratio (e.g. +P4/+P11) for sparkle"
  SLEW: "smooth = glided pitch transitions; stepped = discrete jumps"
controls:
  - { name: "Algorithm", type: switch, value: "Prism Shift (pitch)" }
  - { name: "Arpeggio Type", type: switch, value: "Rising (for the climbing cloud)", options: ["Rising", "Falling", "Falling/Rising", "Rising/Falling"] }
  - { name: "Step Length", type: knob, value: "tempo-synced 1/8 or 1/16 — dial to taste" }
  - { name: "Shift Ratio", type: switch, value: "bright/wide, e.g. +P4/+P11 for sparkle", options: ["-1oct/+1oct", "(four mid options)", "+P4/+P11"] }
  - { name: "Arpeggio Order", type: switch, value: "by ear (sets the voice sequence)" }
  - { name: "Slew", type: knob, value: "lower = smooth glided pitch; higher = stepped jumps — dial to taste" }
  - { name: "Auto EQ", type: switch, value: "on to tame harshness in the cloud — by ear" }
  - { name: "Gain (per voice)", type: knob, value: "balance the voices in the cloud — by ear" }
  - { name: "Feedback (per voice)", type: knob, value: "raise for a denser regenerating cloud — by ear" }
  - { name: "Spread (per voice)", type: knob, value: "widen for stereo cloud — by ear" }
  - { name: "FREEZE", type: switch, value: "footswitch — latching; holds the cloud as a sustained pad" }
  - { name: "SHIFT", type: switch, value: "footswitch — momentary; rotates the shift values" }
---

# Prism Shift — Arpeggiated Shimmer Cloud (freeze + solo)

## Concept
Prism Shift is the H90's polyphonic pitch shifter, and here it arpeggiates several shifted voices into a rising (or falling) cloud of glassy notes. Choose a tempo-synced Step Length and a bright, wide shift ratio so the voices stagger upward into a shimmer, then hit FREEZE to lock the cloud into a sustained sparkling pad and solo over the top. The momentary SHIFT footswitch rotates the shift values for movement. This is a manual-sourced arp recipe, distinct from the existing prismshift-self-generating-stereo-arp-bed and the factory "Sequential Chimes" seed — both of those lean on factory starting points; this one builds the arp cloud straight from the published Prism Shift controls.

## How to play it
1. Load **Prism Shift** on Preset A; choose a **Rising** Arpeggio Type and a tempo-synced **Step Length** (1/8 or 1/16).
2. Pick a bright, wide **Shift Ratio** — e.g. **+P4/+P11** — for sparkle (the six ratios run from -1oct/+1oct up to +P4/+P11).
3. Set **Slew** for smooth (glided) vs stepped pitch transitions, and balance the per-voice **Gain / Feedback / Spread** by ear; use **Auto EQ** to tame harshness.
4. Hold a chord, then trigger **FREEZE** (latching) to sustain the cloud and solo over it.
5. Tap **SHIFT** (momentary) to rotate the voicing for movement.

## Notes
- Arpeggio types (Rising, Falling, Falling/Rising, Rising/Falling), tempo-synced Step Length, the six shift ratios (-1oct/+1oct up to +P4/+P11), Arpeggio Order, Slew, Auto EQ, the per-voice Gain/Feedback/Spread controls, and FREEZE (latching) / SHIFT (momentary) behavior are **from the Eventide manual**. Exact knob values are **not published** — treat the values above as a dialable recipe, not sourced settings.
- Prism Shift is in the SIFT (Spectral Instantaneous Frequency Tracking) family, so it tracks chords cleanly — good for polyphonic arp clouds.
- Distinct from the existing prismshift-self-generating-stereo-arp-bed and prismshift-polyphony-freeze-pad seeds, and from the factory "Sequential Chimes" recipe.

## Sources
- https://cdn.eventideaudio.com/manuals/h90/1.1.2/content/algorithms/pitch.html (Prism Shift: arpeggio types, step length, six shift ratios, per-voice controls, FREEZE latching + SHIFT momentary)
- provenance: manufacturer manual — controls/ratios published, no exact values (dial from recipe)

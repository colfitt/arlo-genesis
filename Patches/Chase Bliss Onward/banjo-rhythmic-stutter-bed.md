---
type: patch
title: Banjo Rhythmic Stutter Bed
device: Chase Bliss Onward
date: 2026-06-14
description: Turn banjo rolls into a tight rhythmic stutter bed by catching only the percussive attack.
tags: [glitch, stutter, rhythmic, banjo, percussive, designed, signature]
hidden:
  SENSITIVITY (on SIZE): toward LESS (so the hot GK-5 per-string transients don't over-trigger)
controls:
  - { name: "Channel", type: switch, value: "GLITCH", options: ["FREEZE", "GLITCH"] }
  - { name: "SIZE", type: knob, value: "down/left (catches only the front transient)" }
  - { name: "MIX", type: knob, value: "up (to audition)" }
  - { name: "SUSTAIN", type: knob, value: "max (to audition)" }
  - { name: "Slot/Bank", type: knob, value: "live, or build a banjo-stutter preset" }
---

# Banjo Rhythmic Stutter Bed

## Concept
Turn banjo rolls into a tight rhythmic stutter bed by catching only the percussive attack. On the GLITCH channel, SIZE = how much of the front of the grabbed ~1s chunk plays — so a small SIZE catches only the front transient, meaning the banjo's hard percussive attack survives (a swell would lose its quiet front).

## How to play it
1. Set the channel to **GLITCH**.
2. Turn **SIZE down/left** so it catches only the front transient — the banjo's hard percussive attack survives a small SIZE.
3. Bring **MIX up + SUSTAIN max** to audition.
4. In the hidden menu, set **SENSITIVITY (on SIZE) toward LESS** so the hot GK-5 per-string transients don't over-trigger.

## Notes
- The mechanic (small SIZE keeps a hard pick transient) is verified Aaron Rusch behavior; SENSITIVITY-toward-LESS for the GK-5 is the rig-specific tuning.
- Maps to ALPFV's "glitchy drums & textures" target.

## Sources
- designed from UsageGuide §5 + `research/transcripts/aaron-rusch-onward-glitch-channel.md` + `aaron-rusch-onward-hidden-options.md`
- Transformed from Pedalxly Onward-Patches.md (designed)

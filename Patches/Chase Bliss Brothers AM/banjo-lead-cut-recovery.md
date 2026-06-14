---
type: patch
title: Banjo-Lead Cut Recovery
device: Chase Bliss Brothers AM
date: 2026-06-14
description: Claw the Gold Tone banjo's articulation and cut back AFTER the Hizumitas has darkened it, so the banjo-as-lead survives into the Longsword and the End Board's granular/reverb stages — lead with booster and Presence, not gain.
tags: [treble-booster, rangemaster, banjo, lead, cut-recovery, designed, signature]
dips:
  PRES LINK 1: on (optional — TONE 1 sweeps tone+presence together for a more dramatic, open control)
hidden:
  Input-Impedance trim: back CCW (buffers upstream)
  Treble/Presence trim: "adjusted in conjunction with the top tone knob makes a big difference" for banjo cut
controls:
  - { name: "TREBLE BOOSTER", type: switch, value: "DOWN (classic Rangemaster, upper-mid emphasis)", options: ["UP (bright)", "MIDDLE (off)", "DOWN (Rangemaster)"] }
  - { name: "CHANNEL 1 MODE", type: switch, value: "OVERDRIVE (or BOOST for cleaner)", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN 1", type: knob, value: "10–11 o'clock (low — articulation not crunch)" }
  - { name: "VOL 1", type: knob, value: "noon" }
  - { name: "TONE 1", type: knob, value: "1 o'clock" }
  - { name: "CHANNEL 2 MODE", type: switch, value: "off (or low-OD Tightener under it)", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "PRESENCE 1", type: knob, value: "brought UP noticeably (hold Ch1 footswitch + TONE 1) — the documented 'opens it out' move" }
---

# Banjo-Lead Cut Recovery

## Concept
The single most rig-specific patch: claw the Gold Tone banjo's articulation and cut back AFTER the Hizumitas has darkened it, so the banjo-as-lead survives into the Longsword and the End Board's granular/reverb stages. The banjo needs articulation and level here, NOT more saturation — a treble booster into an already-overdriven signal (the Muff) is exactly where it gives a "vocal" lead (Mick Taylor / TPS).

## How to play it
1. Set the TREBLE BOOSTER DOWN (classic Rangemaster, upper-mid emphasis) into Channel 1 in OVERDRIVE (or BOOST for cleaner), GAIN 1 low at ~10–11 for articulation not crunch.
2. Bring PRESENCE 1 UP noticeably (hold Ch1 footswitch + TONE 1) — the documented "opens it out" move; or engage PRES LINK 1 so TONE 1 sweeps tone+presence together for a more dramatic, open control.
3. Internal trims: back Input-Impedance CCW (buffers upstream); adjust the treble/presence trim in conjunction with the top tone knob for banjo cut.
4. Optionally run a low-OD Tightener on Channel 2 underneath, or leave Ch2 off.

## Notes
- Designed starting points, not found settings.
- Lead with the booster and Presence, not gain — the banjo is already loud and bright pre-Muff; the job is restoring what the Muff rolled off so the lead reads through the downstream walls.
- Slot: intended as a MIDI preset (suggested).

## Sources
- designed from Brothers-AM-DeepResearch.md §6 (banjo)
- research/links/tps-demo-settings.md (treble booster into overdriven = vocal lead; presence-up)
- research/links/guitar-com-big-review-tips.md (treble/presence trim with top tone)
- Transformed from Pedalxly Brothers-AM-Patches.md (designed)

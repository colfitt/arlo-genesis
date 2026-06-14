---
type: patch
title: VG-800 Pad Rotor Wash
device: Boss BF-3
date: 2026-06-14
description: Slow flange on a continuous VG-800 synth/string pad — a pad gives the comb filter unlimited material, yielding an evolving, rotor-like wash; one of the best drone tricks in this slot. Rig-specific designed patch.
tags: [flanger, drone, pad, rotor, wash, evolving, indie-folk, art-rock, designed, signature]
controls:
  - { name: "MODE", type: switch, value: "Standard (or Ultra for a thicker scoop)", options: ["Standard", "Ultra", "Gate/Pan", "Momentary"] }
  - { name: "MANUAL", type: knob, value: "~11:00" }
  - { name: "RES", type: knob, value: "~10:00–12:00" }
  - { name: "DEPTH", type: knob, value: "~11:00–12:00 (moderate)" }
  - { name: "RATE", type: knob, value: "~7–8:00 (very slow)" }
  - { name: "Input", type: switch, value: "GUITAR IN (VG-800 summed output)", options: ["GUITAR IN", "BASS IN"] }
  - { name: "Output", type: switch, value: "OUTPUT A (mono)", options: ["OUTPUT A (mono)", "OUTPUT A+B (stereo)"] }
---

# VG-800 Pad Rotor Wash

## Concept
Slow flange on a continuous VG-800 synth/string pad. Because a pad sustains indefinitely, the comb filter gets unlimited material to chew on, producing an evolving, rotor-like wash — one of the best drone tricks available in this slot. Banjo/baritone via GK-5 → VG-800 pad models feed the BF-3, and the sustained pad carries the motion under the lead.

## How to play it
1. Set MODE to Standard (or Ultra for a thicker scoop), RATE very slow (~7–8:00), DEPTH moderate (~11:00–12:00), RES ~10:00–12:00, MANUAL ~11:00.
2. Run the VG-800 summed output into GUITAR IN with a sustained pad model.
3. Hold the pad and let the slow flange evolve into a rotor wash; play the banjo/baritone lead over it.

## Notes
- Rig-specific (designed). Indie-folk/art-rock drone fit; banjo-as-lead-friendly when the VG-800 carries a sustained pad under the lead.
- Keep RES moderate so polyphonic patches don't artifact harshly — unless that's wanted (on this aesthetic, the artifact is a feature).

## Sources
- Designed from `research/BF-3-DeepResearch.md` §6 "Modeled VG-800 signal" + `research/BF-3-UsageGuide.md` §6 "VG-800 pad patches"
- Transformed from Pedalxly BF-3-Patches.md (designed)

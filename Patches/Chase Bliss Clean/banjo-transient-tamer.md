---
type: patch
title: Banjo Transient Tamer
device: Chase Bliss Clean
date: 2026-06-14
description: The rig's banjo-as-lead voice — fixes the GK-5 divided-pickup banjo's violent-attack / no-sustain problem so notes behave like guitar before the fuzz wall.
tags: [compression, banjo, transient-control, sustain, lead, designed, signature]
dips:
  Dusty: off
  Swell Aux: off
  Motion: off
  Noise Gate: off
  Sidechain: off
  Latch: off
  Spread: off
  MISO: off
hidden:
  Envelope Balance (EQ knob): "high (EQ knob toward MORE) — comp tracks the bright register, ignores phantom lows"
controls:
  - { name: "Sensitivity", type: knob, value: "HIGHER (banjo is bright but quiet in the control band — set by left LED)" }
  - { name: "Dynamics", type: knob, value: "noon (into limiting, to extend)" }
  - { name: "Attack", type: knob, value: "1:00 (slow, ~50-100 ms — let the pluck spike through THEN clamp)" }
  - { name: "Wet", type: knob, value: "1:00" }
  - { name: "Dry", type: knob, value: "10:00 (light parallel, keep pick detail)" }
  - { name: "EQ", type: knob, value: "noon (off, main page) — repurposed as Envelope Balance on hidden page" }
  - { name: "Release", type: switch, value: "R (Slow 1.5s, extend decay into guitar-like sustain)", options: ["L Fast 50ms", "Mid User 650ms", "R Slow 1.5s"] }
  - { name: "Mode", type: switch, value: "Mid (Manual)", options: ["L Shifty", "Mid Manual", "R Modulated"] }
  - { name: "Physics", type: switch, value: "Mid (stable)", options: ["L subtle wobble", "Mid stable", "R twitchy"] }
  - { name: "Slot/Bank", type: knob, value: "Candidate onboard preset (banjo set), MIDI-recallable with a banjo-lead board scene" }
---

# Banjo Transient Tamer

## Concept
Designed for the Gold Tone EBM-5 banjo via the GK-5 divided pickup — the rig's banjo-as-lead voice. It fixes the violent-attack / no-sustain problem so notes behave like a guitar before the fuzz wall: a slow attack lets the pluck spike escape, then limiting clamps and a slow release extends the decay into guitar-like sustain. The hidden Envelope Balance is set high so the compressor tracks the bright register and ignores the phantom lows — "the banjo tool."

## How to play it
1. **Set Sensitivity by ear to the left LED FIRST** — run it HIGHER (banjo is bright but quiet in the control band). GK-5 per-string level differs from a passive pickup, so this will NOT match guitar settings — always re-LED.
2. Dynamics ~noon (into limiting, to extend).
3. Attack ~1:00 (slow, ~50–100 ms) so the pluck spikes through, then clamps.
4. Release toggle RIGHT (Slow 1.5 s) to extend decay into sustain.
5. Wet ~1:00; Dry ~10:00 (light parallel to keep pick detail).
6. **Hidden option:** hold both footswitches, set the EQ knob toward MORE = Envelope Balance high (comp tracks the bright register, ignores phantom lows). Audio is unaffected — only the control signal is high-passed.

## Notes
- The single best argument for Clean's first slot.
- If you add the Noise Gate dip for quiet fingerpicking, keep its threshold (Sensitivity, in gate mode) LOW or it eats soft notes.
- Approximate/designed values — dial Sensitivity by feel per the GK-5's per-string output. All CUSTOMIZE dips OFF (Noise Gate optional, as noted).

## Sources
- Designed from Clean manual Recipe 1 (slow attack/release) + Envelope Balance (Hidden Options pp.18–19)
- `research/transcripts/bachelormachines-compressor-science-deep-dive.md` (transient-designer: push Dry to engage stage-2 limiter for body, stage-1 shapes; slow attack lets the transient escape)
- `research/transcripts/chase-bliss-clean-official-video-manual.md` (Envelope Balance = HPF on control signal)
- `research/Clean-DeepResearch.md` §6 (banjo all-attack/no-sustain; Envelope Balance = "the banjo tool")
- Transformed from Pedalxly Clean-Patches.md (designed)

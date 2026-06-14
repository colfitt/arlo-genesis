---
type: patch
title: Hizumitas Fuzz Wall
device: Chase Bliss Big Time
date: 2026-06-14
description: EQD Hizumitas (or any sustaining fuzz) → Big Time minimal chain — hold one note for an endless ambient/drone wall, with COLOR kept modest so the limiter doesn't clamp to porridge.
tags: [fuzz, shoegaze, doom, drone, minimal-chain, designed, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot via CC27" }
  - { name: "Chain / Input", type: switch, value: "Hizumitas (mono) → IN-L (auto MISO mono-in/stereo-out)", options: ["mono → IN-L (MISO)", "stereo in"] }
  - { name: "MODE", type: switch, value: "Long", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Compressed (holds a sustaining fuzz together, prevents runaway)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "Focus (shaves highs+lows → keeps the muff wall defined)", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Sine subtle", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "LOW ~25–35% (fuzz already supplies saturation — bring up only until repeats just begin to compress)" }
  - { name: "TIME", type: knob, value: "long" }
  - { name: "CLUSTER", type: knob, value: "~40%" }
  - { name: "TILT EQ", type: knob, value: "pushed UP (cut low mud from the muff wall)" }
  - { name: "FEEDBACK", type: knob, value: "~60%" }
  - { name: "WET", type: knob, value: "~45%" }
  - { name: "TEXTURE", type: knob, value: "~45% (alt — comp amount)" }
  - { name: "DIFFUSE", type: knob, value: "mid (alt under FEEDBACK)" }
  - { name: "SPREAD", type: switch, value: "widen", options: ["off", "widen", "ping-pong"] }
---

# Hizumitas Fuzz Wall

## Concept
EQD Hizumitas (or any sustaining fuzz) → Big Time minimal chain: hold one note for an endless ambient/drone wall. Compressed STATE holds the sustaining fuzz together and prevents runaway; Focus voicing shaves highs and lows to keep the muff wall defined. Because the fuzz already supplies saturation, COLOR stays low — too much COLOR plus a hot fuzz makes the limiter clamp to porridge.

## How to play it
1. Run Hizumitas (mono) → **IN-L**, which auto-engages **MISO** (mono-in/stereo-out).
2. Pre-shape the muff with the Hizumitas Filter knob (scooped ↔ thick) before the delay.
3. Hold one note and let the wall build endlessly.
4. Bring COLOR up only until the repeats just begin to compress — no further.

## Notes
- Keep COLOR modest — too much COLOR + hot fuzz = limiter clamps to porridge. Compressed is the safe state under sustain.
- **MXR 108 fuzz variant:** use Saturated + CLUSTER higher for spitty rhythmic stabs the multi-taps echo.

## Sources
- 🟣 designed from `research/links/centerpiece-minimal-chains-and-sampler-integration.md` §A (fuzz→Big Time gain-staging, COLOR modest, STATE Compressed under sustaining fuzz, TILT up + Focus to tame mud, MISO auto-engage) + Hizumitas GearProfile.
- Transformed from Pedalxly Big-Time-Patches.md (designed)

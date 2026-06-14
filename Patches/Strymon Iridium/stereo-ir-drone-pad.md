---
type: patch
title: Stereo IR Drone Pad (dark-L / bright-R)
device: Strymon Iridium
date: 2026-06-14
description: A wide sustained drone bed where one chord blooms into a stereo pad — built on the Impulse Manager stereo-IR widening trick (darker IR left, brighter IR right) for the Swans/post-rock wall.
tags: [drone, ambient, wall, post-rock, stereo, designed, signature]
hidden:
  Impulse Manager — Match left channel: unchecked
  Impulse Manager — LEFT IR: darker same-vendor IR (24-bit/96 kHz WAV ≤500 ms)
  Impulse Manager — RIGHT IR: brighter same-vendor IR (24-bit/96 kHz WAV ≤500 ms)
  Impulse Manager — per-side trim: use LEVEL/TREBLE/BASS to re-center the brighter side
  Impulse Manager — SYNC CHANGES: click before unplugging USB
controls:
  - { name: "Amp", type: switch, value: "round (clean bloom) or punch (saturated wall)", options: ["round", "chime", "punch"] }
  - { name: "Cab", type: switch, value: "the dual-IR slot", options: ["a", "b", "c"] }
  - { name: "Drive", type: knob, value: "round ~noon / punch ~1:00–2:00" }
  - { name: "Bass", type: knob, value: "10:00" }
  - { name: "Middle", type: knob, value: "round 11:00 / punch 9:00" }
  - { name: "Treble", type: knob, value: "noon" }
  - { name: "Level", type: knob, value: "to taste" }
  - { name: "Room", type: knob, value: "1:00 (SIZE LARGE)" }
  - { name: "Input Level", type: switch, value: "Instrument", options: ["Instrument", "Line"] }
  - { name: "Output Mode", type: switch, value: "Normal (ON LED red)", options: ["Normal", "Amp Bypass", "Cab Bypass"] }
  - { name: "Rear Input Selector", type: switch, value: "STEREO (true stereo out, both jacks)", options: ["MONO", "STEREO", "SUM"] }
  - { name: "Slot/Bank", type: knob, value: "FAV (the wide drone bed) — dual-IR Collection saved at ~/Documents/Strymon/collections" }
---

# Stereo IR Drone Pad (dark-L / bright-R)

## Concept
A wide sustained drone bed for the Swans/post-rock wall — one chord blooms into a wide stereo pad using the Impulse Manager stereo-IR widening trick on a single cab slot. A darker IR loaded into the LEFT channel and a brighter same-vendor IR into the RIGHT, so the L/R difference itself creates the width. Hybrid stereo room + dual-IR width = a finished wall with zero extra pedals, giving the downstream H90/Dark Star a pristine wide stereo bloom to smear.

## How to play it
1. PREP (USB, pedal powered): pick one cab slot, uncheck "Match left channel," drag a DARKER same-vendor IR into LEFT and a BRIGHTER same-vendor IR into RIGHT (both 24-bit/96 kHz WAV ≤500 ms, same vendor to avoid phase cancellation). Use per-side LEVEL/TREBLE/BASS trim to re-center the brighter side. Click SYNC CHANGES before unplugging.
2. PLAY: AMP round (clean bloom) or punch (saturated wall); CAB = the dual-IR slot; DRIVE round ~noon / punch ~1–2:00; BASS 10:00; MIDDLE round 11 / punch 9; TREBLE noon.
3. ROOM 1:00, SIZE LARGE.
4. INPUT LEVEL = Instrument, OUTPUT MODE = Normal (red), rear = STEREO (true stereo out, both jacks).
5. Do NOT sum to mono — the L/R difference IS the width.

## Notes
- DESIGNED patch — requires Impulse Manager prep, not knob-only.
- Same vendor on both sides avoids phase cancellation.
- Useless if the path is summed to mono.

## Sources
- designed from documented stereo-IR widening — research/links/tips-hidden-behaviors.md; research/links/tips-soundonsound-poweruser.md; research/transcripts/westbrook-impulse-manager-tips.md (Iridium-UsageGuide.md §3). No artist attribution.
- Transformed from Pedalxly Iridium-Patches.md (designed)

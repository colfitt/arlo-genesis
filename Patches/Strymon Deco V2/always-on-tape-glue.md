---
type: patch
title: Always-On Tape Glue
device: Strymon Deco V2
date: 2026-06-14
description: The everyday front-of-chain tape warmer — set a high saturation level and ride guitar/VG-800 volume for the drive amount, fattening the banjo/baritone source so you feel it more than hear it (Pete Celi / Strymon in-depth demo).
tags: [tape-warmth, always-on, glue, front-of-chain, factory, signature]
hidden:
  Low Trim: 9-10:00 (slightly up, keeps bottom tight; 15-150 Hz range)
controls:
  - { name: "Tape Saturation", type: switch, value: "ON", options: ["ON","OFF"] }
  - { name: "Doubletracker", type: switch, value: "OFF (or Blend full CCW)", options: ["ON","OFF"] }
  - { name: "Saturation", type: knob, value: "~12-1:00 (set fairly high)" }
  - { name: "Voice", type: switch, value: "classic", options: ["classic","cassette"] }
  - { name: "Tone", type: knob, value: "12:00" }
  - { name: "Volume", type: knob, value: "to unity (match bypassed level on engage)" }
  - { name: "Slot/Bank", type: knob, value: "PC10 (Favorite candidate)" }
---

# Always-On Tape Glue

## Concept
The cornerstone front-of-chain warmer. Set a fairly high saturation level and let your guitar/VG-800 volume set the actual drive amount — rolled back is clean/transparent, dug in adds harmonics, compression and dynamic band-limiting. The maker's own headline move: "a level where you don't really hear the saturation but it's fattening everything." Single coils warm audibly around 10:00.

## How to play it
1. Engage Tape Saturation only; leave the Doubletracker off (or Blend full CCW).
2. Set Saturation fairly high (~12–1:00), Voice classic, Tone at noon.
3. Match Volume to your bypassed level on engage — the Deco is a gain device and jumps in volume.
4. Hold the Tape Saturation footswitch ON until both LEDs flash, then turn TONE to set Low Trim up to ~9–10:00 (keeps the bottom tight).
5. Ride guitar volume / VG-800 level live for the drive: rolled back = clean, dug in = harmonics + compression.

## Notes
- The cornerstone voice. Pairs with CB Clean (always-on).
- Keep front-panel Tone dark and Low Trim up so it does NOT re-brighten an already-tamed banjo.
- It's a gain device — be on firmware v1.22+ (ideally v1.33) to avoid the saturation-sweep volume burst.

## Sources
- transcripts/strymon-pete-celi-in-depth-demo.md ("set a fairly high distortion level and let your guitar volume set the drive… a level where you don't really hear the saturation but it's fattening everything")
- UsageGuide §1/§2; manual Rev D for Low Trim (15–150 Hz)
- Ref: Pete Celi / Strymon in-depth demo (ST8pp4HN554)
- Transformed from Pedalxly Deco-V2-Patches.md (factory/artist)

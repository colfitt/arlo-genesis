---
type: patch
title: Sag Swell / Slapback Designer
device: Chase Bliss Clean
date: 2026-06-14
description: Uses deep Sag to turn sustained drones/held chords into swelling pads, or to add a transient-boost + slapback tail to plucked/drum sources before the texture boards.
tags: [sag, swell, slapback, pad, texture, community, signature]
dips:
  Dusty: off
  Swell Aux: off
  Motion: off
  Noise Gate: off
  Sidechain: off
  Latch: off
  Spread: off
  MISO: off
controls:
  - { name: "Dynamics", type: knob, value: "PAST 3:00 (deep Sag)" }
  - { name: "Sensitivity", type: knob, value: "10:00 (low enough that quiet noodling passes through untouched)" }
  - { name: "Attack", type: knob, value: "slow-ish (CW) to lengthen the escaping transient + create the swell" }
  - { name: "Wet", type: knob, value: "up" }
  - { name: "Dry", type: knob, value: "blend to taste for body" }
  - { name: "EQ", type: knob, value: "to taste" }
  - { name: "Release", type: switch, value: "L (Fast) for the slapback-return character", options: ["L Fast 50ms", "Mid User 650ms", "R Slow 1.5s"] }
  - { name: "Mode", type: switch, value: "Mid (Manual)", options: ["L Shifty", "Mid Manual", "R Modulated"] }
  - { name: "Physics", type: switch, value: "Mid (or L for organic wobble)", options: ["L subtle wobble", "Mid stable", "R twitchy"] }
  - { name: "Bypass FS (hold)", type: button, value: "max the Sag momentarily as a 'fall apart' gesture" }
---

# Sag Swell / Slapback Designer

## Concept
Deep Sag (Dynamics past 3:00) inverts the compressor's dynamics — loud becomes soft, soft becomes loud — and favors higher frequencies. With a slow attack and fast release it boosts the transient AND adds a slapback return; on sustained sources it becomes a swelling pad. Turn Sensitivity down in Sag and the pedal behaves almost like a volume swell. On-brand sleeper for feeding pre-swelled material into the downstream Microcosm/Blooper/MOOD so they sound intentional — one part can sound like three instruments.

## How to play it
1. Push Dynamics PAST 3:00 into deep Sag.
2. Set Sensitivity ~10:00 — low enough that quiet noodling passes through untouched.
3. Attack slow-ish (CW) to lengthen the escaping transient and create the swell.
4. Release toggle LEFT (Fast) for the slapback-return character.
5. Wet up; Dry blend to taste for body; Mode MID; Physics MID (or LEFT for organic wobble).
6. **Bypass-FS HOLD = max the Sag momentarily** as a "fall apart" gesture.

## Notes
- Sag inverts dynamics and favors higher frequencies — use on banjo/guitar/VG-800, **AVOID on the boomy baritone lows** (it reacts poorly to bass).
- Add reverb over it (downstream) for the swelling-pad effect.

## Sources
- `research/transcripts/bachelormachines-compressor-science-deep-dive.md` (slow-attack/fast-release Sag boosts the transient AND adds a slapback return; on sustained sources = swelling pad)
- `research/transcripts/geardead-fun-creative-compression-guitar.md` (turn Sensitivity down in Sag and it behaves almost like a swell — add reverb over it)
- Transformed from Pedalxly Clean-Patches.md (community)

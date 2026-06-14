---
type: patch
title: Aleatoric Arp Wall (Recipe D, per-Part arps)
device: Novation 61SL MkIII
date: 2026-06-14
description: DOUG-designed Session — a slowly mutating, self-sustaining arpeggio wall from one held chord; hands-free generative density you tweak live.
tags: [generative, arp, aleatoric, latch, drone, designed, signature]
controls:
  - { name: "Part 1 Latch", type: button, value: "Hold a chord and LATCH it (works whether Arp on/off)" }
  - { name: "Part 1 Arp Type", type: switch, value: "Random", options: ["Up", "Down", "Played", "Random"] }
  - { name: "Part 1 Arp Octaves", type: knob, value: "3–6" }
  - { name: "Part 1 Arp Chance (per-arp, fw 1.4)", type: knob, value: "~60–80%" }
  - { name: "Part 1 Arp Gate", type: knob, value: "100% (overlapping)" }
  - { name: "Part 1 Arp Sync Rate", type: knob, value: "1/16" }
  - { name: "Part 2 Arp Type", type: switch, value: "Played", options: ["Up", "Down", "Played", "Random"] }
  - { name: "Part 2 Arp Sync Rate", type: knob, value: "1/8T" }
  - { name: "Part 2 Arp Octaves", type: knob, value: "2 (a second, slower aleatoric line)" }
  - { name: "Scales", type: switch, value: "On + Snap (random octave-spanning notes stay in key)", options: ["Off", "On"] }
  - { name: "Session Slot", type: knob, value: "Session slot 8" }
hidden:
  Drone trick: "Arp LATCH with Arp OFF = a continuous sustained note (drone generator) into VG-800 or a soft synth, hands-free"
---

# Aleatoric Arp Wall (Recipe D, per-Part arps)

## Concept
A slowly mutating, self-sustaining arpeggio wall from one held chord — hands-free generative density you tweak live. Drives a sustained synth/VG voice. Per-Part arp + per-arp probability are firmware 1.4 features — the heart of the "generative & constantly evolving instrument" framing — and all 8 Parts can run independent arps at once.

## How to play it
1. PART1: hold a chord and LATCH it (Latch button — works whether Arp on/off). Arp = Random, Octaves = 3–6, Chance ~60–80% (per-arp probability, firmware 1.4), Gate 100% (overlapping), Sync Rate 1/16.
2. PART2 (same held chord): Arp Type = Played, Sync Rate = 1/8T, Octaves = 2 → a second, slower aleatoric line (per-Part independent arps, firmware 1.4).
3. SCALES: On + Snap → random octave-spanning notes stay in key.
4. Latch self-sustains hands-free; tweak Chance/Octaves live for the mutation.
5. Route Part1/Part2 to chosen voices (e.g. VG synth + soft synth).
6. BONUS DRONE TRICK: Arp LATCH with Arp OFF = a continuous sustained note (a drone generator) into the VG-800 or a soft synth, hands-free.

## Notes
- DESIGNED.
- Per-Part arp + per-arp probability are firmware 1.4 — the heart of the "generative & constantly evolving instrument" framing.
- Latch-with-Arp-OFF is the documented hidden drone trick.

## Sources
- designed from research/links/seq-generative-recipes.md Recipe D + seq-manual-arpeggiator.md (Random/Played, Oct 1–6, Chance 0–100%, latch) + forum-hidden-features-power-user-tips.md (latch=drone) + novation-firmware-1.4-generative-instrument.md; taste-profile sustained-walls.
- Ref: Taste — post-punk/experimental sustained crescendo; indie-folk washes (Sufjan electronic layers).
- Transformed from Pedalxly 61SL-MkIII-Patches.md (designed)

---
type: patch
title: Go-To-Sleep Random Stutter
device: Chase Bliss Blooper
date: 2026-06-14
description: Jonny Greenwood's randomized stutter/glitch (Go To Sleep, There There) — Scrambler as the near-1:1 hardware equivalent of his Max/MSP random-generator patch (Radiohead/Jonny Greenwood).
tags: [glitch, scrambler, stutter, radiohead, taste-profile, designed, signature]
dips:
  DRY KILL: "ON = the Feral's kill-dry toggle (glitch-only output); leave OFF to blend dry + stutter like the LS-2 in/out"
controls:
  - { name: "MOD B", type: knob, value: "CCW of noon = random (Jonny's random generator); deeper CCW = more chopping; CW = repeating sequence (fixed Feral Glitch mode)" }
  - { name: "MOD B slot", type: switch, value: "B5 Scrambler", options: ["B4", "B5", "B6"] }
  - { name: "MOD B engage", type: button, value: "engage to chop; toggle on/off to regenerate a new random arrangement" }
  - { name: "REPEATS", type: knob, value: "up" }
  - { name: "VOLUME", type: knob, value: "12 o'clock" }
  - { name: "Slot/Bank", type: knob, value: "MOD B5 default bank · MIDI PC 11 (shares Scrambler family) or its own slot" }
---

# Go-To-Sleep Random Stutter

## Concept

Jonny Greenwood's randomized stutter/glitch from "Go To Sleep" and "There There." His Max/MSP patch ran a random generator that looped chunks of audio for an "x" amount of time, decided randomly. Blooper's Scrambler is the near-1:1 hardware equivalent — a 16-slice grid, random or fixed. Designed to emulate; Radiohead's actual method is a Max/MSP patch, not a Blooper.

## How to play it

1. Record a dense source first — play a lot of notes (banjo/VG arp), exactly as Jonny "plays a lot of notes so the patch always has something to loop."
2. Set MOD B to Scrambler (B5), knob CCW of noon = random (Jonny's random generator); deeper CCW = more chopping.
3. Engage to chop into the pattern; toggle on/off to regenerate a new random arrangement (the patch's re-roll).
4. For the fixed mode of the Feral Glitch, set Scrambler CW = repeating sequence instead.
5. REPEATS up, VOLUME 12. Jump points lock to the 16-slice grid so they support the rhythm.
6. DRY KILL dip ON = the Feral's kill-dry toggle (glitch-only output); leave it off to blend dry + stutter like the LS-2 in/out.

## Notes

- Sync the grid to the Digitakt clock (see Clock-synced blooping) so the random stutter feels intentional, like the patch's tempo-aware chunks.
- For "occasional disturbance" rather than constant chop, use Skip Protection — same Scrambler, lowest random setting.

## Sources

- 🟣 designed from `Research/Taste-Profile/sources/musicradar-feral-glitch-greenwood-stutter.md` (random generator loops audio for x time; LS-2 in/out routing; random vs fixed; kill-dry toggle) + Scrambler behavior in Drone Pattern / Skip Protection.
- Ref: Radiohead / Jonny Greenwood — "Go To Sleep," "There There" randomized stutter Max/MSP patch (the Feral Glitch pedal recreates it).
- Transformed from Pedalxly Blooper-Patches.md (designed)

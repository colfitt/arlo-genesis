---
type: patch
title: Spectral Mill (Resynth into Microcosm)
device: Chase Bliss Lost & Found
date: 2026-06-14
description: DOUG-designed — feeds the Microcosm a constantly-moving resynthesized signal (Spectral Modulator + Gen Lite) instead of dry guitar; glacial spectral filter sweeps + digital-distortion grit for the art-rock studio-as-instrument glitch-texture move (Radiohead glitch/granular).
tags: [glitch, spectral, granular, art-rock, texture, designed, signature]
dips:
  SPREAD: on
  UNSYNC: off
hidden:
  GLUE: "10:00"
  EQ: "to taste"
controls:
  - { name: "ROUTING", type: switch, value: "L+R parallel", options: ["L>R", "L+R", "L<R"] }
  - { name: "L slot mode", type: switch, value: "3B Spectral Modulator" }
  - { name: "R slot mode", type: switch, value: "6B Gen Lite (needs L SWAP on, or run Spectral solo)" }
  - { name: "L SWAP", type: switch, value: "on (to host Gen Lite in the right slot; both modes live on left channel natively)", options: ["on", "off"] }
  - { name: "MODIFY (L notch depth)", type: knob, value: "1:00" }
  - { name: "TIME (L sawtooth-LFO rate)", type: knob, value: "9:00–10:00 (SLOW — glacial sweep)" }
  - { name: "ALT (L resonance/clipping)", type: knob, value: "2:00 (digital-distortion grit; normalizes upper partials)" }
  - { name: "Gen Lite (R, if paired)", type: knob, value: "full wet, TIME toward wow, ALT crinkles ~10:00" }
  - { name: "BLEND", type: knob, value: "11:00 (toward Spectral)" }
  - { name: "MIX (RAMP)", type: knob, value: "1:00–2:00" }
  - { name: "Slot/Bank", type: knob, value: "Preset bank 2 (BANK dip)" }
---

# Spectral Mill (Resynth into Microcosm)

## Concept
Instead of feeding the Microcosm dry guitar, this gives its grain engine far richer raw material — a constantly-moving resynthesized signal. The Spectral Modulator (3B) does glacial filter sweeps (slow sawtooth LFO) with a resonance/clipping edge for digital-distortion grit, optionally paired with Gen Lite (6B) for extra ruin. This is the art-rock studio-as-instrument glitch-texture move (Radiohead glitch/granular).

## How to play it
1. Set ROUTING `L+R` parallel. To pair Gen Lite, enable **L SWAP** so the left slot can host a right-channel mode (or run Spectral Modulator solo and skip the swap).
2. Set TIME(L) ~9–10:00 for a glacial sawtooth-LFO sweep.
3. Push ALT(L) ~2:00 for the resonance/clipping grit (normalizes upper partials → digital distortion).
4. If pairing Gen Lite: full wet, TIME toward wow, ALT crinkles ~10:00.
5. Follow with the downstream reverbs to make it shine.

## Notes
- **DESIGNED, not found.** Spectral Modulator is the standout "resynthesis" texture for this rig.
- SPREAD on puts the L/R spectral processing on opposed LFOs.
- UNSYNC off → LFO syncs to clock (~3:00 ≈ one cycle/beat, noon ≈ once/bar/side).
- Pair with Gen Lite for extra ruin, or run solo.

## Sources
- Spectral Modulator map (MODIFY = depth, TIME = sawtooth LFO rate, ALT = resonance + clipping/digital distortion, SPREAD = opposed LFOs, syncs to clock, "best followed by delay/reverb to shine") from BachelorMachinesTV Pt1 — `research/transcripts/bachelormachinestv-science-part1.md`
- Johnston "3B from lo-fi low-pass to glacial filter sweeps" — `research/transcripts/secret-weapons-mark-johnston-walkthrough.md`
- Dossier §5 "feed Microcosm a Spectral-Modulator shimmer" — `research/Lost-and-Found-DeepResearch.md`
- Taste lens art-rock cluster — `Research/Taste-Profile/taste-profile.md`
- Ref: Taste cluster — art-rock / studio-as-instrument (Radiohead glitch/granular textures)
- Transformed from Pedalxly Lost-and-Found-Patches.md (designed)

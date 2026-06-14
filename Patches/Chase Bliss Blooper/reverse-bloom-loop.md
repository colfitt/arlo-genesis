---
type: patch
title: Reverse-Bloom Loop
device: Chase Bliss Blooper
date: 2026-06-14
description: Daydreaming's reversed glockenspiel that fades in (plus Jonny's reversed guitar) — a captured-then-reversed loop via Stepped Speed CCW (Radiohead, A Moon Shaped Pool / Backdrifts).
tags: [pitch, reverse, ambient, radiohead, taste-profile, designed, signature]
controls:
  - { name: "Mode", type: switch, value: "ADD (to print a clean reversed layer back into the wall)", options: ["NORM", "ADD", "SAMP"] }
  - { name: "MOD B", type: knob, value: "CCW = reverse (loop runs in reverse; decaying tail now swells in)" }
  - { name: "MOD B slot", type: switch, value: "B4 Stepped Speed", options: ["B4", "B5", "B6"] }
  - { name: "REPEATS", type: knob, value: "max (FADE none)" }
  - { name: "Slot/Bank", type: knob, value: "MOD B4 default bank, knob CCW · MIDI PC 3 (Stepped-Speed family)" }
---

# Reverse-Bloom Loop

## Concept

The other Daydreaming move — Thom samples ringing glockenspiel notes and reverses them so each note that rang out now gently fades IN. Also covers Jonny's reversed guitar (Backdrifts) and A Moon Shaped Pool's "sample-something-then-reverse-it" approach. Radiohead's reverse is a captured-then-reversed sample, not a swelling reverse-delay pedal — Blooper's reversed loop is the honest hardware match.

## How to play it

1. Capture a ringing pluck/swell (banjo, VG pad, or a reverb tail grabbed in SAMP from upstream).
2. Play the loop backwards: set MOD B to Stepped Speed (B4), knob CCW (= reverse) so the loop runs in reverse — the decaying tail now swells in.
3. For a clean reversed layer printed back into the wall, do it in ADD and overdub the reversed pass on top of the forward loop (the "sample-then-reverse-and-layer" method).
4. Pair with FADE (none) / REPEATS max.

## Notes

- Radiohead's reverse is a captured-then-reversed sample, not a swelling reverse-delay pedal — capture → reverse → layer is the honest hardware match.
- For the swelling-in attack on a single note, also see the MOOD Slip reverse.
- Feed into the H90 hall so the reversed blooms diffuse.

## Sources

- 🟣 designed from `Research/Taste-Profile/sources/kingofgear-thom-looping-daydreaming.md` + `Research/Taste-Profile/sources/kingofgear-jonny-reverse-delay-backdrifts.md` (reverse = captured sample reversed, not a pedal swell) + Stepped-Speed CCW reverse in Rainbow Machine shimmer.
- Ref: Radiohead — "Daydreaming" (reversed glockenspiel that fades in) + "Backdrifts" (reversed guitar, Max/MSP); AMSP "sample-then-reverse" technique.
- Transformed from Pedalxly Blooper-Patches.md (designed)

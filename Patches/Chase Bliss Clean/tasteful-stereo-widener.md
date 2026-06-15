---
type: patch
title: Tasteful Stereo Widener (MISO + SPREAD)
device: Chase Bliss Clean
date: 2026-06-15
description: "Turns a mono source into a wide, mono-safe stereo image — MISO splits mono to stereo, SPREAD adds independent per-channel processing, then the default 'wild' width is tamed by spread-routing to EQ only, keeping Physics centered and Dry blended up the middle for a mono core. Devin Belanger's 'beautiful natural stereo movement that doesn't phase out' — pure analog, no DSP, sums to mono cleanly (demo + Tape Op/ReviewRevival + manual)."
tags: [stereo, spread, miso, widener, ambient, mono-to-stereo, community]
dips:
  MISO: on
  Spread: "on (Spread Routing -> EQ via Hidden Options)"
  Dusty: off
  Swell Aux: off
  Motion: off
  Noise Gate: off
  Sidechain: off
  Latch: off
controls:
  - { name: "MISO (dip)", type: switch, value: "ON — TS in / TRS out, splits a mono input to a stereo output", options: ["off", "on"] }
  - { name: "SPREAD (dip)", type: switch, value: "ON — independent L/R per-channel processing for stereo motion", options: ["off", "on"] }
  - { name: "Spread Routing (Hidden Option — Physics toggle)", type: switch, value: "EQ only — keep comp identical both sides so only the EQ moves in stereo", options: ["EQ only", "EQ + Comp", "Comp only"] }
  - { name: "Physics", type: switch, value: "Mid (centered/stable) — keeps the width tasteful, not twitchy", options: ["L subtle wobble", "Mid stable", "R twitchy"] }
  - { name: "EQ", type: knob, value: "dial to taste — the EQ is what moves in stereo (Manual = flickering pan, Modulated = auto-pan, Shifty = smooth dynamic pan)" }
  - { name: "Dry", type: knob, value: "blend UP for a mono core down the middle when SPREAD gets too intense" }
  - { name: "Wet", type: knob, value: "to taste" }
  - { name: "Mode", type: switch, value: "to taste (sets the stereo motion character — see EQ)", options: ["L Shifty", "Mid Manual", "R Modulated"] }
---

# Tasteful Stereo Widener (MISO + SPREAD)

## Concept
Clean can split a single mono input into a wide, mono-safe stereo image with zero DSP. Flip MISO to split mono to stereo (TS in / TRS out), flip SPREAD for independent per-channel processing, then tame SPREAD's default "wild" width: in Hidden Options set Spread Routing to EQ only (identical comp both sides), keep the Physics toggle centered for stability, and blend Dry up the middle for a mono core. The result is Devin Belanger's "beautiful natural stereo movement that doesn't phase out" — pure analog, summing cleanly to mono.

## How to play it
1. Wire mono in / stereo out (TS in, TRS out) and flip the MISO dip.
2. Flip the SPREAD dip for independent per-channel stereo motion.
3. In Hidden Options, set Spread Routing (Physics toggle) to EQ only so the comp is identical both sides and only the EQ moves in stereo.
4. Keep the Physics toggle centered (stable) so the width stays tasteful, not twitchy.
5. Blend Dry up for a mono core down the middle when SPREAD gets too intense. Run into two amps spread apart for a trippy image.

## Notes
- **No published clock-face values** — this is a dialable routing recipe (a config of dips + Hidden Options), not a sourced knob settings dump. Dial the EQ/Dry/Wet by ear.
- SPREAD's DEFAULT character is wild/aggressive widening, NOT subtle (Tape Op / ReviewRevival) — the spread-route-to-EQ + Dry-center moves are what make it tasteful (Devin Belanger).
- Each EQ mode has its own stereo motion: Manual = flickering panning, Modulated = auto-pan, Shifty = smooth dynamic pan.
- Mono-safe: pure analog, no DSP, no phase cancellation when summed to mono.
- In THIS rig it only pays off if Clean is redeployed END-of-chain — the front slot is mono.

## Sources
- `research/links/daily-clean-stereo-spread-miso-and-chain-placement.md` (MISO/SPREAD wiring; SPREAD default = wild widening; spread-route to EQ only + Physics centered + Dry up the middle = tasteful; mono-safe)
- `research/transcripts/devin-belanger-clean-most-useful-pedal.md` ("beautiful natural stereo movement that doesn't phase out... fully mono-compatible, no digital DSP"; dry-center technique)
- `research/transcripts/chase-bliss-clean-official-video-manual.md` (MISO = TS in/TRS out + dip; SPREAD per-effect stereo; Spread Routing hidden option)
- Chase Bliss Clean official manual (Customize MISO/SPREAD p.34-35, Spread Routing p.19, EQ p.29)
- `reviewrevival.ca/reviews/chase-bliss-clean-definitive-review-2025` (trippy through dual amps; wild default)
- Transformed from community sources (demo:Devin Belanger + review:Tape Op/ReviewRevival + manual)

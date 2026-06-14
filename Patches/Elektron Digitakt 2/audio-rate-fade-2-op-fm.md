---
type: patch
title: Audio-Rate FADE = 2-OP FM (blooming metallic tone)
device: Elektron Digitakt 2
date: 2026-06-14
description: Metallic FM drones / clangorous lead from a single sample or single-cycle — push an LFO to audio rate as the FM modulator and bloom it in via negative FADE.
tags: [fm, metallic, drone, lfo, factory, signature]
controls:
  - { name: "LFO1 DEST", type: switch, value: "Pitch" }
  - { name: "LFO1 WAVE", type: switch, value: "Sine" }
  - { name: "LFO1 MULT", type: knob, value: "512 / 1k / 2k (pushes LFO to audio rate = the FM modulator)" }
  - { name: "LFO1 FADE", type: knob, value: "negative (fade-in; range −64…63) so the FM blooms in over time" }
  - { name: "LFO1 SPD", type: knob, value: "bipolar — negative runs backward; sets frequency ratio vs note pitch" }
  - { name: "Carrier", type: switch, value: "the sample / single-cycle" }
---

# Audio-Rate FADE = 2-OP FM (blooming metallic tone)

## Concept
Two-operator FM on the DT2 without an FM engine: push an LFO to audio rate (high MULT) so it becomes the FM modulator, with the sample/single-cycle as the carrier. A negative FADE makes the FM bloom in over time for a metallic drone or clangorous lead. The harmonic-vs-clangorous character is set by note pitch against `MULT/SPD`.

## How to play it
1. LFO: `DEST = Pitch`; `WAVE = Sine`; `MULT = 512 / 1k / 2k` (pushes the LFO to audio rate = the FM modulator; the sample/single-cycle = carrier).
2. Set `FADE =` negative (fade-in, range −64…63) so the FM blooms in over time.
3. Frequency ratio is set by note pitch vs `MULT/SPD` — dial harmonic vs clangorous.
4. `SPD` is bipolar (negative runs backward).

## Notes
- `FADE −64…63` is the one hard manual range; the ratio is ear-dialed.
- Save as preset "FM Bloom."

## Sources
- `research/links/dt2-manual-lfo-mode-fade-fm.md` (Manual OS1.15A §11.9)
- elektronauts LFO threads
- Transformed from Pedalxly Digitakt-2-Patches.md (factory)

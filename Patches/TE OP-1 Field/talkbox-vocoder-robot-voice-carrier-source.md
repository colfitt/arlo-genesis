---
type: patch
title: Talkbox/Vocoder Robot-Voice (carrier source)
device: TE OP-1 Field
date: 2026-06-14
description: INDEX-ONLY / APPROXIMATE — the Daft Punk talkbox/vocoder robot vocal. The OP-1 has no vocoder/talkbox, so this only mimics the result via a filtered carrier or chromatic voice sample.
tags: [vocal, electronic, daft-punk, vocoder, approximate, taste-profile, designed, signature]
controls:
  - { name: "Engine (carrier option A)", type: switch, value: "Cluster/Dr Wave — sustained saw note", options: ["Dr Wave","Cluster","Phase","Digital","Voltage","FM","String","Face","iter","Synth Sampler","Sampler"] }
  - { name: "Filter modulation", type: switch, value: "value-LFO or hand-ride, rhythmic, in time with a spoken/sung phrase" }
  - { name: "Engine (option B)", type: switch, value: "Synth Sampler — one-note-sample a voice, play chromatically for robotic-choir flavor" }
  - { name: "Slot/Bank", type: knob, value: "Synth Sampler sampler/ folder — robot-carrier (OP1-E3)" }
---

# Talkbox/Vocoder Robot-Voice (carrier source)

## Concept

INDEX-ONLY / APPROXIMATE: the Daft Punk talkbox/vocoder robot vocal. The OP-1 has no vocoder or talkbox, so this only mimics the **result** (a moving, formant-ish robot tone) — not the method. There is no tube, no mouth-formant, no bank-of-bandpass vocoder. Filter-fake only. Flagged.

## How to play it

1. **Option A (carrier):** Use the OP-1 as the carrier — a sustained **Cluster/Dr Wave** saw note, and modulate its filter rhythmically (value-LFO or hand-ride) in time with a spoken/sung phrase.
2. **Option B (chromatic voice):** Use the **Synth Sampler** to one-note-sample a voice and play it chromatically for a robotic-choir flavor.

## Notes

- INDEX-ONLY, APPROXIMATE — reproduces the result, not the talkbox/vocoder method. Flagged as such in the source.
- Save as `robot-carrier` in the `sampler/` folder (OP1-E3).

## Sources

- Ref: Daft Punk talkbox/vocoder vocals ("Around the World" talkbox; SVC-350/DigiTech Talker vocoders)
- Research/Taste-Profile/sources/daft-punk-talkbox-vocoder-per-song-bjango.md
- Transformed from Pedalxly OP-1-Field-Patches.md (DOUG-designed)

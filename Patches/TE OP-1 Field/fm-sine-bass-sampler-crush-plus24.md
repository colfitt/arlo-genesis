---
type: patch
title: "FM sine bass → +24 sampler crush"
device: TE OP-1 Field
date: 2026-06-15
description: "Pure sine bass built on the FM engine (FM amount fully down), layered detuned/vibrato takes to tape, then resampled into the Synth Sampler and gained to +24 for crunchy digital distortion with a very pleasant character — a value-exact crush trick from a published op1tips forum recipe."
tags: [bass, fm, sampler, distortion, resample]
dips:
  RESAMPLE: "Detune the layered sine takes slightly + add vibrato before resampling for the best crush."
controls:
  - { name: "Engine", type: switch, value: "FM", options: ["Dr Wave","Cluster","Phase","Digital","Voltage","FM","String","Face","iter","Synth Sampler","Sampler"] }
  - { name: "FM amount (BLUE)", type: knob, value: "0 (fully down) — pure sine carrier" }
  - { name: "Synth Sampler volume ([Shift]+Red)", type: knob, value: "+24 — crunchy digital distortion" }
  - { name: "FX", type: switch, value: "delay (or other) after the crush, to taste" }
  - { name: "Tape", type: switch, value: "layer several takes, each slightly detuned + with vibrato" }
---

# FM sine bass → +24 sampler crush

## Concept

Build a pure sine bass on the **FM** engine with the FM amount (BLUE) all the way down, so the carrier rings as a clean sine. Layer several detuned, vibrato'd takes to tape to give the sound some harmonic content, then lift/drop that layered tape into the **Synth Sampler** and crank the sampler volume to **+24**. The overdriven sampler gain produces crunchy digital distortion "with a very pleasant character" — a documented, value-exact OP-1 crush trick.

## How to play it

1. Select **FM**, turn **BLUE** (FM amount) fully down for a clean sine carrier.
2. Record several takes to tape, each slightly **detuned** and with **vibrato**.
3. Lift/drop the layered tape into the **Synth Sampler**.
4. Raise the **Synth Sampler volume to +24** (`[Shift]+Red`) for crunchy digital distortion.
5. Add **delay** or other FX to finish.

## Notes

- The +24 sampler crush is a documented OP-1 trick for "crunchy digital distortion with a very pleasant character."
- Stacking detuned sine layers first gives the crush more harmonic content to bite on.
- Provenance: forum recipe (op1tips). **FM amount = 0 (min)** and **sampler gain = +24** are published values; all other knob positions (FX/delay amount, exact detune/vibrato depth) are dial-to-taste and not sourced.

## Sources

- github.com/ratbag98/op1tips (FM sine bass + layer detune/vibrato → sampler at +24 for crunchy digital distortion)

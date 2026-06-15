---
type: patch
title: "Ambient drone — tape + tempo slowdown bed"
device: TE OP-1 Field
date: 2026-06-15
description: "A deep ambient drone built by slowing both tempo and tape speed to a crawl, running a long-attack/long-release poly synth with portamento, drawing pitches into the Sketch sequencer set to Hold, and drowning the whole thing in CWO + Spring/Mother. The slowdown gestures and the Poly / Portamento / Sketch-Hold key combos are published; envelope and FX amounts are to-taste (forum recipe, op1tips)."
tags: [drone, ambient, tape, sketch-sequencer, pad, community, signature]
dips:
  TAPE_AFTER_RECORD: "record at normal/fast tempo THEN slow the tape afterward for a mellower, smeared atmosphere"
controls:
  - { name: "Tempo (metronome screen, Blue)", type: knob, value: "slow way down" }
  - { name: "Tape speed (metronome screen, white)", type: knob, value: "slow way down" }
  - { name: "Engine", type: switch, value: "any pad/poly synth with long attack + long release", options: ["Dr Wave","Cluster","Phase","Digital","Voltage","FM","String","Face","iter","Synth Sampler","Sampler"] }
  - { name: "T2 Attack", type: knob, value: "long — to-taste" }
  - { name: "T2 Release", type: knob, value: "long — to-taste" }
  - { name: "Poly ([Shift]+Blue)", type: switch, value: "on" }
  - { name: "Portamento ([Shift]+Green)", type: knob, value: "up — to-taste" }
  - { name: "Sequencer", type: switch, value: "Sketch (draw pitches), then Hold ([Shift]+Orange)", options: ["Pattern","Tombola","Endless","Finger","Sketch","Arpeggio","Hold"] }
  - { name: "Synth FX", type: switch, value: "CWO or delay — amount to-taste" }
  - { name: "Master FX", type: switch, value: "Spring (or Mother) — amount to-taste" }
---

# Ambient drone — tape + tempo slowdown bed

## Concept

A deep ambient drone made by dragging both **tempo and tape speed** down to a crawl on the metronome screen, then sustaining it. Use a pad/poly engine with a **long attack + long release**, turn **Poly** on and raise **Portamento** so notes glide into each other, then **draw a chord in the Sketch sequencer and latch it with Hold** so the drone keeps sounding hands-free. Wash it all out with **CWO (or delay) on the Synth FX** and **Spring (or Mother) on the Master FX**. The result is a slow, smeared, evolving bed. Distinct from the existing `slow-ambient-drone-setup` patch by its specific Sketch-draw → Hold construction and the record-then-slow-the-tape trick.

## How to play it

1. On the **metronome screen**, slow **tempo** (Blue) and **tape speed** (white) right down.
2. Pick a pad/poly engine with a **long attack + long release**; enable **Poly** (`[Shift]+Blue`) and raise **Portamento** (`[Shift]+Green`).
3. **Draw a chord** in the **Sketch** sequencer and set it to **Hold** (`[Shift]+Orange`) so it sustains hands-free.
4. Add **CWO** (or delay) on the **Synth FX** and **Spring** (or **Mother**) on the **Master FX**.
5. Let it sustain; record a long pass to tape.

## Notes

- **Values are a dialable recipe, not sourced settings.** The slowdown gestures (Blue tempo / white tape on the metronome) and the Poly / Portamento / Sketch-Hold key combos are published in the op1tips set, but the exact envelope and FX amounts are not — treat Attack/Release, Portamento depth, and the CWO/Spring/Mother mix as starting points and dial to taste.
- **Record at normal/fast tempo, then slow the tape afterward** — the documented trick for a mellower, smeared atmosphere rather than tracking everything at crawl speed.
- **Sketch Hold** keeps the drone sounding hands-free while you ride the tape and FX.
- Distinct from `slow-ambient-drone-setup` (which latches a single low note via the Hold sequencer) by its Sketch-draw → Hold chord construction and the tape-after-record gesture.

## Sources

- github.com/ratbag98/op1tips — Ambient drone recipe: slow tempo (Blue) / tape speed (white) on the metronome, long A/R, Poly (`[Shift]+Blue`), Portamento (`[Shift]+Green`), Sketch Hold (`[Shift]+Orange`), CWO/delay + Spring (community)
- Provenance: forum recipe (op1tips) — gesture/combo set published, amounts to-taste

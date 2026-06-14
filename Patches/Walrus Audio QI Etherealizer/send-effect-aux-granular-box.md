---
type: patch
title: Send-Effect / Aux Granular Box (synth/drum-machine)
device: Walrus Audio QI Etherealizer
date: 2026-06-14
description: Use the Qi as a stereo send/aux granular-reverb effect for a synth or drum machine (true stereo in/out), not strictly inline.
tags: [granular, reverb, send, aux, synth, drum-machine, rig-integration, community, signature]
controls:
  - { name: "Flow", type: switch, value: "Parallel (recommended — keeps engines discrete)", options: ["Series", "Parallel"] }
  - { name: "Grain Mix", type: knob, value: "lean on Grain for the ambient bloom" }
  - { name: "Space", type: knob, value: "lean on Space for the ambient bloom" }
  - { name: "Mix/Dry", type: knob, value: "blend the return" }
  - { name: "Slot/Bank", type: knob, value: "Routing config (use over a grain/space patch)" }
---

# Send-Effect / Aux Granular Box (synth/drum-machine)

## Concept
Use the Qi as a stereo send/aux granular-reverb effect for a synth or drum machine (true stereo in/out), rather than strictly inline. Lean on Grain + Space for the ambient bloom and blend the return. Community ran it with SH-101, Prophet Rev2, Nymphes, OP-XY, and TB-303.

## How to play it
1. Patch the Qi on a stereo aux/send (DAW or mixer).
2. Set Flow to **Parallel** (recommended — keeps engines discrete).
3. Lean on **Grain + Space** for the ambient bloom.
4. Blend the return.

## Notes
- ⚠️ RIG-RELEVANT: confirms hot-source clipping — NO line/instrument level switch; pad/reamp the input.
- Community (Elektronauts: Claid, jayhosking).

## Sources
- research/links/elektronauts-synth-community-thread.md; transcripts/synth-anatomy-with-synths.md
- Transformed from Pedalxly QI-Etherealizer-Patches.md (community)

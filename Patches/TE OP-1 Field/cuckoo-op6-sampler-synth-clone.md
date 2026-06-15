---
type: patch
title: "Cuckoo — sampler-as-synth-cloner (OP-6 method)"
device: TE OP-1 Field
date: 2026-06-15
description: "Cuckoo's signature: sample another synth into the OP-1's sampler engine to 'clone' it — his 'OP-6' pack is 40 patches sampled off a Sequential OB-6. Rig translation: sample a single sustained note from the VG-800, Prophet, Juno, or DX7 and play it polyphonically as a 'broken synth' voice. Artist method (Cuckoo OP-6 pack) — method-level, no published values."
tags: [sampler, polyphonic, clone, keys, artist, signature]
controls:
  - { name: "Engine", type: switch, value: "Synth Sampler", options: ["Dr Wave","Cluster","Phase","Digital","Voltage","FM","String","Face","iter","Synth Sampler","Sampler"] }
  - { name: "Sample source", type: button, value: "one sustained note from the source synth (OB-6 / Prophet / Juno / DX7 / VG-800); play the matching key while sampling so tuning is correct" }
  - { name: "Loop start/end", type: knob, value: "set loop points for seamless polyphonic sustain" }
  - { name: "[Shift]+GRAY (crossfade)", type: knob, value: "crossfade loop for infinite sustain" }
  - { name: "Tape degrade", type: switch, value: "Vintage / Porta tape for the 'broken synth choir'", options: ["Vintage","Porta"] }
  - { name: "Slot/Bank", type: knob, value: "sampler/ folder — op6-clone (e.g. ob6-clone / juno-clone)" }
---

# Cuckoo — sampler-as-synth-cloner (OP-6 method)

## Concept

Cuckoo's signature trick: sample another synth straight into the OP-1's sampler engine to "clone" its voice. His "OP-6" pack is 40 patches sampled off a Sequential OB-6 — the name is the joke (OP-1 + OB-6). The rig translation is the same move on whatever's in the room: sample a single sustained note from the VG-800, Prophet, Juno, or DX7, set the loop, and play that captured voice polyphonically as a "broken synth" version of the source. Overlaps the Andreas Roman one-note-poly patch in mechanism, but this is the distinct Cuckoo *synth-cloning* concept — capturing a whole synth's voice, not just a found sustained note.

## How to play it

1. Play one long sustained note on the source synth (OB-6 / Prophet / Juno / DX7 / VG-800).
2. In the **Synth Sampler**, sample it — play the matching key while sampling so the tuning lands correctly.
3. Set **loop start/end** points + **`[Shift]+GRAY` crossfade** for seamless polyphonic sustain.
4. Play chords across the keys — you're now playing a sampled "clone" of that synth.
5. Degrade on **Vintage / Porta** tape for the "broken synth choir."

## Notes

- REAL cited Cuckoo method (OP-6 = OB-6 sampled in). Method-level — **no published knob values**. The control block is a dialable recipe, not sourced settings.
- Overlaps the Andreas Roman one-note-poly patch in mechanism, but this is the distinct Cuckoo synth-cloning concept (sample a whole synth's voice).
- Remember: no time-stretch — pitching up shortens the captured note. Save as `op6-clone` (e.g. `ob6-clone` / `juno-clone`) in the `sampler/` folder.

## Sources

- Gear/TE OP-1 Field/research/links/op1-demo-educators-hainbach-cuckoo-rmr.md (§Cuckoo — "OP-6" sampler-as-synth-cloner)
- Gear/TE OP-1 Field/research/transcripts/sonwu-op1-field-sampler-engine-tutorial.md (§SYNTH SAMPLER)
- Transformed from Pedalxly OP-1-Field-Patches.md (artist)

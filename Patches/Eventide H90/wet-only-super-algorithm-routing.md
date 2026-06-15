---
type: patch
title: "Wet-Only Super-Algorithm — 100% Wet A into B under dry"
device: Eventide H90
date: 2026-06-15
description: "Leon Todd's core H90 routing trick: set Preset A's Mix to 100% so only its wet feeds Preset B, build a combined A->B wet block (e.g. SP2016 reverb into chorus, or Blackhole/Crystals into MangledVerb), then blend the whole wet 'super-algorithm' under a fully dry signal with the Program Mix. Dry stays uncolored while a modulated/degraded wall rings behind it — the End-board's signature technique. Demoed by Leon Todd (YouTube), concept + example chains published, no full knob table."
tags: [routing, technique, ambient, sustained-wall, leon-todd, signature]
controls:
  - { name: "Routing", type: switch, value: "Series (Preset A -> Preset B)" }
  - { name: "Preset A Mix", type: knob, value: "100% (fully wet — only A's wet enters B)" }
  - { name: "A->B Wet Block", type: switch, value: "any wet chain; Todd demos: SP2016 Reverb 100% -> Chorus / Vintage Delay 100% -> Tremolo (panner) / Crystals -> distortion", options: ["SP2016 Reverb -> Chorus", "Vintage Delay -> Tremolo", "Crystals -> MangledVerb", "Blackhole -> MangledVerb"] }
  - { name: "Program Mix", type: knob, value: "~50% (blends the wet block under dry); drive from exp pedal / HotKnob P to swell" }
  - { name: "Kill Dry", type: switch, value: "OFF (essential — the dry path is what stays clean)", options: ["OFF", "ON"] }
---

# Wet-Only Super-Algorithm — 100% Wet A into B under dry

## Concept
Leon Todd's core H90 routing trick: set Preset A's Mix to 100% so only its wet signal feeds Preset B, build a combined A->B wet block (e.g. SP2016 reverb into chorus, or Blackhole/Crystals into MangledVerb), then blend the whole wet "super-algorithm" under a fully dry signal with the Program Mix. Dry stays uncolored while a modulated/degraded wall rings behind it — the End-board's signature technique.

## How to play it
1. Route Preset A -> Preset B in Series.
2. Set Preset A Mix to 100% so only its wet signal enters B.
3. Build the wet effect across A->B (e.g. reverb into chorus, Crystals into MangledVerb).
4. Set Kill Dry OFF and use Program Mix (~50%) to sit the wet wall under the dry note.
5. Optional: drive Program Mix from an exp pedal / HotKnob P to swell the wall in and out.

## Notes
- This is a technique/template, **not** fixed knob values — only the routing/Mix/Kill-Dry choices are sourced. The published examples (SP2016 -> Chorus, Vintage Delay -> Tremolo, Crystals -> distortion) are concrete, but the actual A->B contents are yours to dial.
- Kill Dry MUST be OFF — the dry path is exactly what stays clean under the wet wall.
- Program Mix is the blend control. Map it to an exp pedal or HotKnob P to swell the wall in and out.
- Don't run two fully-wet effects in series in a true W/D/W rig — use parallel routing or the Program-Mix blend instead.
- Rig-core variant: run Blackhole/Shimmer/Wormhole/Crystals at 100% into MangledVerb, blend under dry, then print to the tape stage.
- Demoed on the H9 editor; algorithm/routing is identical on the H90.

## Sources
- research/transcripts/leon-todd-h90-routing-trick-wet-only-superalgorithm.md (youtube jxWh3LG-MY8, 7:07)
- research/H90-UsageGuide.md §1 (wet-only super-algorithm trick)
- Provenance: technique — Leon Todd (demo:Leon Todd), concept + example chains published, no full knob table

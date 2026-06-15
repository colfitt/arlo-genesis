---
type: patch
title: "MangledVerb — Doom Reverb-into-Drive (bow-scrape to mayhem)"
device: Eventide H90
date: 2026-06-15
description: "Reverb-into-distortion super-algorithm (Pre-Delay -> Reverb -> EQ -> Distortion) with a Wobble detune control — bow-scraping a cello string out to a roaring, detuned, apocalyptic doom wash. The native partner for the rig's degradation thesis and the wet-only super-algorithm's B slot. Signal flow, the softclip(1-100)/overdrive split, output -18 to +6 dB, Wobble, band EQ, low-Size/Decay reverse behavior, and the Size~15 distortion value are sourced (manual + Algorithm Guide + Leon Todd); remaining knobs dial from recipe."
tags: [mangledverb, reverb, distortion, doom, degraded, wobble, sustained-wall, signature]
controls:
  - { name: "Preset A Algorithm", type: switch, value: "MangledVerb" }
  - { name: "Signal Flow", type: switch, value: "Pre-Delay -> Reverb -> EQ -> Distortion (fixed internal order)" }
  - { name: "Distortion", type: knob, value: "first half (1-100) = soft-clip; second half switches to overdrive" }
  - { name: "Distortion Output Level", type: knob, value: "-18 to +6 dB (set to taste)" }
  - { name: "Wobble", type: knob, value: "detuning-modulation rate (dial for seasick detune)" }
  - { name: "Low Band Level", type: knob, value: "pre-distortion EQ (recipe — cut to de-mud)" }
  - { name: "Mid Band Level", type: knob, value: "pre-distortion EQ (recipe)" }
  - { name: "High Band Level", type: knob, value: "pre-distortion EQ (recipe)" }
  - { name: "Size", type: knob, value: "~15 for distortion-flavored use (sourced); larger for a cavernous mangled space; low = reverse-reverb swell" }
  - { name: "Decay", type: knob, value: "low for reverse-reverb attack; long for doom wash (recipe)" }
  - { name: "Preset B Algorithm", type: switch, value: "100%-wet Blackhole or Shimmer feeding A (End-board core move)" }
---

# MangledVerb — Doom Reverb-into-Drive (bow-scrape to mayhem)

## Concept
The H90's MangledVerb runs reverb straight into distortion — Pre-Delay -> Reverb -> EQ -> Distortion — so the dirt eats the tail, not the dry note. Add the Wobble detune and the whole thing slides from a bow scraping a single cello string up to a roaring, detuned, apocalyptic doom wash. It's the native partner for the rig's degradation thesis, and it shines as Preset B catching a 100%-wet Blackhole/Shimmer (the End-board core move). Factory presets in this neighborhood: **DoomDrive, Oblivion, ScreamWarp**.

## How to play it
1. Load MangledVerb on Preset A; set a big Size/Decay for a cavernous space, or Size ~15 for the distortion-flavored use.
2. Push the Distortion knob into the **overdrive** (upper) half; set Output Level (-18 to +6 dB) to taste.
3. Add Wobble for detuned movement, then shape the Low/Mid/High band EQ (pre-distortion) to keep it from turning to mud.
4. For swells, drop Size/Decay low — MangledVerb gives a reverse-reverb attack into the dirt.
5. Use it as Preset B catching a 100%-wet Blackhole or Shimmer (End-board core move) for a layered, mangled wall.

## Notes
- **Sourced:** the signal flow, the soft-clip (1-100) -> overdrive split on the Distortion knob, the -18 to +6 dB output range, the Wobble detune control, the pre-distortion band EQ, low Size/Decay = reverse-reverb attack, and **Size ~15 for distortion mode** all come from the Eventide manual + Algorithm Guide (corroborated by Leon Todd's wet-only super-algorithm trick).
- **Recipe, not sourced:** no published numeric values exist for Distortion amount, Output Level, Wobble rate, the three band levels, or Decay — dial those by ear. Treat them as a starting recipe, not factory settings.
- Factory presets in this family: DoomDrive, Oblivion, ScreamWarp.
- Pairs natively with the rig's degradation/tape thesis; the wet-only Blackhole/Shimmer -> MangledVerb routing is the End-board signature.

## Sources
- https://cdn.eventideaudio.com/manuals/h90/1.11.4/content/algorithms/reverb.html (MangledVerb: softclip 1-100 then overdrive, Wobble, band EQ, output -18 to +6 dB, low Size/Decay = reverse; presets DoomDrive, Oblivion, ScreamWarp)
- research/H90-DeepResearch.md §3 (MangledVerb — Algorithm Guide §10, manuals/EventideH90.pdf; Size~15 for distortion mode)
- research/transcripts/leon-todd-h90-routing-trick-wet-only-superalgorithm.md (MangledVerb as B slot)

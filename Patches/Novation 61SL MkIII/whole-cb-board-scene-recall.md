---
type: patch
title: Whole-CB-Board Scene Recall (one PC = the stack)
device: Novation 61SL MkIII
date: 2026-06-14
description: Recall a whole-pedalboard state across the CB stack with a single Program Change, so a Session = whole-board song recall — Verse/Chorus/Bridge scenes for live play.
tags: [cb-stack, scene-recall, program-change, live, community, signature]
controls:
  - { name: "Buttons (scene PCs)", type: button, value: "8 buttons → 8 scene PCs (toggle/momentary)" }
  - { name: "Button (LIVE)", type: button, value: "Reserve one for PC0 = LIVE/follow-knobs" }
  - { name: "Scene strategy", type: switch, value: "A (lean): shared channel + matched preset #s", options: ["A (shared ch + matched preset)", "B (distinct channels per pedal)"] }
  - { name: "Channel (Strategy A)", type: knob, value: "Same MIDI channel across scene pedals (default ch.2)" }
  - { name: "Part Destination", type: switch, value: "The CB DIN chain", options: ["USB", "DIN1", "DIN2", "CV"] }
  - { name: "Session Slot", type: knob, value: "Session slot 3 (Save-Lock)" }
hidden:
  PC convention: "PC# = recall slot; PC0 = LIVE/follow-knobs; empty slot = nothing"
  Slot counts: "MOOD/L+F/Onward/Blooper = 122 slots; Big Time = 127 (10 factory); Gen Loss = 2 onboard + PC recall"
  Save over MIDI: "PC# while holding both footswitches, or CC111 (MOOD/L+F, value=slot) / CC27+CC28 (Big Time)"
---

# Whole-CB-Board Scene Recall (one PC = the stack)

## Concept
Recall a whole-pedalboard state across the CB stack (Brothers AM, Clean, MOOD MkII, Blooper, Big Time, Generation Loss, Onward + Hologram/H90 if desired) with a single Program Change, so a Session = whole-board song recall. Build Verse/Chorus/Bridge scenes you can jump between live with one button each.

## How to play it
1. SCENE STRATEGY A (lean): set the CB pedals you want in a scene to the SAME MIDI channel (default ch.2), and SAVE THE SAME PRESET NUMBER on every pedal for a song part — e.g. "Verse" = preset 10 on Blooper+MOOD+L+F+Onward+Big Time+Gen Loss+Clean.
2. A template BUTTON then sends ONE PC 10 on that channel → every pedal jumps to its own preset 10 at once.
3. CB CONVENTION: PC# = recall slot (PC0 = LIVE/follow-knobs; empty slot = nothing); MOOD/L+F/Onward/Blooper = 122 slots, Big Time = 127 (10 factory), Gen Loss = 2 onboard + PC recall.
4. SAVE over MIDI = PC# while holding both footswitches, or CC111 (MOOD/L+F, value=slot) / CC27+CC28 (Big Time).
5. TEMPLATE: map 8 buttons to 8 scene PCs (toggle/momentary), reserve a button for PC0 = LIVE.
6. PHYSICAL: SL DIN Out → CB MIDIBox (needs its OWN 9V!) → ring-active TRS to ≤4 TRS pedals per box (two boxes for the stack); Big Time takes 5-pin DIN directly.
7. Build one template in Components, then CLONE & re-channel per pedal (libslmkiii) for Strategy B. PART Destination = the CB DIN chain.

## Notes
- Verified CB PC/save convention.
- Strategy A (shared channel + matched preset #s) = whole-board recall in one message; use Strategy B (distinct channels) only when you need per-pedal CC automation simultaneously.
- CB Clean = always-on cornerstone — its clock-sync feature is feature-listed but CC-UNCONFIRMED, so don't rely on clocking it from a scene.

## Sources
- REUSED Gear/Chase Bliss Blooper/research/links/cb-stack-preset-scene-recall.md (§2,§3 Strategy A) + cb-stack-midi-trs-and-midibox.md (MIDIBox/channels) + int-recipe-cb-stack-pedals.md.
- Ref: Rig — CB stack; CB Clean always-on, Big Time centerpiece.
- Transformed from Pedalxly 61SL-MkIII-Patches.md (community)

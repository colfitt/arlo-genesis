---
type: patch
title: Scene-Crossfade Performance (equal-power dry ↔ crushed)
device: Elektron Octatrack MkII
date: 2026-06-14
description: A whole performance played with one hand on the crossfader — a dry loop morphs to a filter-swept, crushed, freeze-fed wash via two contrasting scenes.
tags: [crossfader, scenes, performance, drone, designed, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Any Part · Scene A = clean slot, Scene B = changes slot" }
  - { name: "Scene A", type: button, value: "dry loop, filter open, no FX ([SCENE A]+[TRIG n])" }
  - { name: "Scene B", type: button, value: "filter swept low, Lo-Fi crushed, freeze-delay feedback high ([SCENE B]+[TRIG m])" }
  - { name: "XLV (crossfader level)", type: knob, value: "lock for equal-power level (post-FX, MIN = mute / MAX = pass at set LEVEL)" }
  - { name: "XVOL", type: knob, value: "AMP MAIN (pre-FX)" }
  - { name: "XDIR AB/CD", type: knob, value: "MIXER for DIR-monitored inputs" }
  - { name: "Scene lock", type: button, value: "hold [SCENE]+turn DATA ENTRY (inverted graphics = locked)" }
  - { name: "Scene mute", type: button, value: "[FUNC]+[SCENE A/B] (snap to base)" }
  - { name: "Slice-morph STRT", type: knob, value: "slice loop 16/SLIC = ON, lock STRT = SL1 to Scene A and STRT = SL16 to Scene B (fader sweeps which slices play)" }
---

# Scene-Crossfade Performance (equal-power dry ↔ crushed)

## Concept
A whole performance played with one hand on the crossfader: a dry loop morphs to a filter-swept, crushed, freeze-fed wash. Two contrasting scenes in one Part, with XLV/XVOL locked for equal-power level so there's no center dip during the fade. Scene locks override p-locks during a fade for smooth transitions.

## How to play it
1. Build one Part with two contrasting scenes. **Scene A** = dry loop, filter open, no FX. **Scene B** = filter swept low, Lo-Fi crushed, freeze-delay feedback high.
2. Lock **XLV/XVOL** for equal-power level (no center dip): XLV overlays every track LEVEL (post-FX, MIN = mute / MAX = pass at set LEVEL); XVOL in AMP MAIN (pre-FX); XDIR AB/CD in MIXER for DIR-monitored inputs.
3. Assign: [SCENE A]+[TRIG n], [SCENE B]+[TRIG m]; lock by holding [SCENE]+turning DATA ENTRY (inverted graphics = locked).
4. Scene mute = [FUNC]+[SCENE A/B] (snap to base). Scenes-as-keyboard: hold [SCENE B]+tap scene slots like keys.
5. **Named moves:**
   - *Drone swell* — A: LEVEL/XLV low, FX dry; B: XLV up, Dark Reverb mix up, freeze-delay feedback up.
   - *Filter sweep* — A: cutoff open; B: cutoff low + resonance high.
   - *Stutter/collapse* — A: clean Thru; B: Lo-Fi crush on, bit/SR low, freeze-delay capturing a fragment, fast LFO depth up.
   - *Slice-morph* — slice loop 16/SLIC = ON, lock **STRT = SL1** to Scene A and **STRT = SL16** to Scene B → fader sweeps which slices play.

## Notes
- Scene locks override p-locks during a fade (smooth transitions).
- The slice-morph STRT SL1↔SL16 trick is the most concrete single recipe here (manual §17.2.2).
- Scene contents are **designed** starting points — dial to taste.

## Sources
- designed from links/rig-crossfader-scenes-performance.md + DeepResearch §13(c) (Manual §10.3 p53-54, §17.2.2 p108, §16.4 p100-101)
- Transformed from Pedalxly Octatrack-MkII-Patches.md (DOUG-designed)

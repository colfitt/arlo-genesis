---
type: patch
title: Live-Mangle-the-Pedalboard
device: Elektron Octatrack MkII
date: 2026-06-14
description: The rig-defining patch — the pedalboard's stereo fuzz wall flows live through the OT and the crossfader morphs a clean wall into a destroyed/frozen smear.
tags: [drone, fuzz-wall, live-fx, thru-machine, crossfader, designed, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Bank A / Part 1 / Pattern 1 · Track 1 Thru" }
  - { name: "Track 1 machine", type: switch, value: "Thru", options: ["Static", "Flex", "Thru", "Neighbor", "Pickup"] }
  - { name: "Track 1 SRC MAIN INAB", type: switch, value: "A B (A hard-L / B hard-R)", options: ["A", "B", "A B", "-"] }
  - { name: "Track 1 SRC MAIN INCD", type: switch, value: "-", options: ["C", "D", "C D", "-"] }
  - { name: "MIXER DIR AB", type: knob, value: "0 (kill dry passthrough)" }
  - { name: "MIXER AB GAIN", type: knob, value: "set so <REC> LEDs flicker healthy (range -64..+63)" }
  - { name: "MIXER MAIN OUT", type: knob, value: "0 (unity)" }
  - { name: "FX1", type: switch, value: "Multimode resonant filter (or Lo-Fi Collection)", options: ["Filter", "Lo-Fi", "..."] }
  - { name: "FX2", type: switch, value: "Echo Freeze Delay (tempo-synced)", options: ["Delay", "Echo Freeze Delay", "..."] }
  - { name: "LFO1 dest", type: switch, value: "FX1 cutoff" }
  - { name: "LFO1 wave", type: switch, value: "slow triangle" }
  - { name: "Scene A (fader left)", type: button, value: "[SCENE A]+[TRIG 1] = clean wall: FX mild, filter open, freeze-delay feedback low" }
  - { name: "Scene B (fader right)", type: button, value: "[SCENE B]+[TRIG 2] = ruined wall: filter cutoff swept down + resonance high, Lo-Fi crush on, freeze-delay feedback near max, LFO depth up" }
---

# Live-Mangle-the-Pedalboard

## Concept
The pedalboard's stereo fuzz/drone wall (Longsword / MXR 108 / Brothers AM stacks) flows live through the OT via a Thru machine, and one throw of the crossfader morphs the clean wall into a destroyed, frozen smear. This is THE centerpiece patch — the OT becomes the rig's live destruction stage for sustained fuzz/drone walls.

## How to play it
1. Print the pedalboard stereo (Board 3 424 / PORTA424 L/R) into OT inputs **A/B** (impedance-balanced TRS).
2. MIXER: set **DIR AB = 0** (DIR bypasses the FX blocks, so killing it forces all audio through the Thru chain), set **AB GAIN** so the `<REC>` LEDs flicker healthy not clipping, **MAIN OUT = 0** unity.
3. Track 1 = **Thru**, **SRC MAIN INAB = A B**, INCD = −. Thru passes NO audio until triggered, so place **ONE sample trig on step 1** (or hold **[TRACK 1]+[PLAY]**).
4. Set **FX1** = multimode resonant filter (or Lo-Fi Collection), **FX2** = Echo Freeze Delay (tempo-synced). Route **LFO 1 → FX1 cutoff** as a slow triangle so the wall breathes.
5. Assign **Scene A** ([SCENE A]+[TRIG 1]) = clean wall: FX mild, filter open, freeze-delay feedback low.
6. Assign **Scene B** ([SCENE B]+[TRIG 2]) = ruined wall: hold [SCENE B] + turn knobs to lock → filter cutoff swept down + resonance high, Lo-Fi crush on, freeze-delay feedback near max, LFO depth up.
7. Throw the crossfader between A and B to perform the morph.

## Notes
- **Optional capture layer:** Track 2 = Flex on recorder buffer 1; a recorder trig grabs ~16 s of wall, auto-slice; equal-power fade = Track 1 XLV MAX@A/MIN@B, Track 2 XLV MIN@A/MAX@B.
- **Stutter variant:** short Thru track length (1/16 scale) + conditional/probability trigs + micro-timing; fast LFO→cutoff = tremolo/glitch.
- Don't run DIR-dry + Thru together → comb-filter phasing; keep DIR = 0, pick one monitor path.
- Latency ~1.5 ms / 64 samples (effectively real-time).
- All scene/FX values are **designed** starting points — dial to taste.

## Sources
- designed from links/rig-recipe-mangle-fuzz-wall.md + thru-machine-live-fx-setup.md + DeepResearch §13(a) (Manual §16.1.2 p97, §17.5 p111, §10.3 p53-54, §9.2 p47)
- Transformed from Pedalxly Octatrack-MkII-Patches.md (DOUG-designed)

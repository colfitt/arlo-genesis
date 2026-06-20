---
type: patch
title: MOD Compressed Chorus / Vibrato
device: Chase Bliss Big Time
date: 2026-06-19
description: "MOD-mode chorus that flips to true vibrato — MODE Mod (3–46 ms), SCALE Off, MOTION Sine so the wet beats against the dry for a dreamy, compressed chorus (factory #1 COMPRESSED CHORUS territory). Pull DRY to zero (alt under WET) and it becomes a true pitch-wobble vibrato — the 'kill dry for vibrato/lo-fi' move Snyder calls out at Superbooth. STATE Compressed for the smooth, dreamy factory #1 character. The control routing (MODE/SCALE/MOTION/STATE) is first-party-sourced; the clock-face fader numbers are a dialable DOUG recipe, not published."
tags: [mod, chorus, vibrato, modulation, dry-kill, compressed, designed]
dips:
  DRY KILL: "OFF for chorus (dry + wet beat together); ON (or pull DRY to zero, alt under WET) for true vibrato"
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot (10 internal / 127 via MIDI); recall flies the faders to saved positions" }
  - { name: "MODE", type: switch, value: "Mod (3–46 ms — the chorus/flanger/warble zone, NOT a delay; this IS the patch)", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Compressed (the dreamy, smooth factory #1 COMPRESSED CHORUS character)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "HiFi (flat — Snyder: 'useful for modulation'; keeps the chorus clean) or Warm for a vintage-rack tint", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off (manual: 'When SCALE is off you will get classic, bendy pitch modulation, useful for creating chorusing, flanging, and tape-style warble' — this is what makes it a chorus/vibrato, not a pitch-quantized voice)", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Sine (smooth LFO drift — the chorus/vibrato wobble)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "low–moderate ~30% (clean chorus; the patch is built on modulation, not clipping)" }
  - { name: "TIME", type: knob, value: "short–mid of the MOD range (sets the chorus voice; very short = tight, toward 46 ms = wider, more flange-adjacent)" }
  - { name: "CLUSTER", type: knob, value: "low ~20% (thicken/widen the wet field without washing it out)" }
  - { name: "TILT EQ", type: knob, value: "at/just above noon (keep the chorus out of the low-mid mud)" }
  - { name: "FEEDBACK", type: knob, value: "low ~20% (a touch of resonance richens the chorus; keep it well clear of flange/runaway)" }
  - { name: "WET", type: knob, value: "~40% for chorus (dry retained so the wet beats against it); pull DRY to zero (alt under WET) for vibrato" }
  - { name: "RATE", type: knob, value: "alt under TIME — slow–moderate (the chorus/vibrato wobble speed)" }
  - { name: "DEPTH", type: knob, value: "alt under CLUSTER — moderate (the pitch-modulation depth; deeper = more obvious vibrato)" }
  - { name: "SPREAD", type: switch, value: "widen (open the chorus across the stereo field)", options: ["off", "widen", "ping-pong"] }
  - { name: "DRY KILL", type: switch, value: "OFF for chorus; flip ON (Options) or pull DRY to zero for true vibrato", options: ["off", "on"] }
  - { name: "MODE button (hold 2s)", type: button, value: "Panic reset → clean simple delay" }
---

# MOD Compressed Chorus / Vibrato

## Concept
The MOD range (3–46 ms) is Big Time's chorus/flanger/warble zone, not a delay. With **SCALE Off** the manual promises "classic, bendy pitch modulation, useful for creating chorusing, flanging, and tape-style warble" — so dry + wet beating together with a slow **MOTION Sine** gives a dreamy, compressed chorus (factory #1 COMPRESSED CHORUS territory). The single move that turns it into a **true vibrato**: pull DRY to zero (DRY KILL, or the alt-under-WET dry level) so only the pitch-wobbling wet remains — the "kill dry for vibrato/lo-fi" trick Snyder demos at Superbooth. **STATE Compressed** supplies the smooth, dreamy factory-#1 glue. Distinct from `mod-slap-comb-flange-double` (which uses MOD as a slap → comb → flange double with FEEDBACK pushed into a flanger); this one is a clean chorus that flips to vibrato, with FEEDBACK kept low.

## How to play it
1. Set **MODE Mod**, **SCALE Off**, **MOTION Sine**, **STATE Compressed**.
2. Confirm you hear a chorus/warble, not a slap or a delay — **TIME** in the short–mid of the MOD range.
3. For **chorus**: keep **DRY KILL OFF** so dry and wet beat together; set **WET ~40%**, **RATE slow–moderate**, **DEPTH moderate** (alt menu, under TIME / CLUSTER).
4. For **vibrato**: flip **DRY KILL ON** (Options) or pull the dry to zero (alt under WET) so only the pitch-wobbling wet is heard — soft = subtle, deeper DEPTH = seasick.
5. Keep **COLOR low (~30%)** and **FEEDBACK low (~20%)** — this is a modulation patch, not a clipping or flange patch; too much FEEDBACK climbs toward the flanger and out of chorus.
6. Push **TILT EQ at/just above noon** to keep the chorus clear of low-mid mud; **SPREAD widen** to open it across the field.
7. Hold the **MODE button** (2 s) to panic-reset to a clean delay.

## Notes
- **STEP is non-functional in MOD mode** (verified): there is no footswitch sequence-stepping here — in MOD the TAP LEFT footswitch instead toggles MOTION on/off. So treat the footswitches as MOTION-toggle / bypass, not a step sequencer.
- The chorus↔vibrato flip is the dry-level move: chorus = dry + wet beating; vibrato = wet only (DRY KILL or dry pulled to zero). Same engine, one knob.
- **VOICING HiFi is "useful for modulation"** (Snyder, Superbooth) — flat, keeps the chorus clean; switch to Warm for a vintage-digital-rack tint if you want the chorus a touch darker.
- ⚠️ HONEST: only the control *routing* (MODE Mod, SCALE Off, MOTION Sine, STATE Compressed, the DRY-KILL=vibrato move) is first-party-sourced. The specific clock-face positions (COLOR / TIME / CLUSTER / TILT / FEEDBACK / WET / RATE / DEPTH) are a dialable DOUG recipe set by ear, not published Chase Bliss numerics. On recall the motorized faders fly to the saved positions and override these starting points.

## Sources
- 🟣 DOUG-designed patch. Control routing is first-party-sourced; numeric fader positions are a dialable recipe (designed starting points), flagged as such — the motorized faders override on recall.
- `research/bloops/2026-06-19-chase-bliss-big-time.md` (Lens: patches — MOD-mode recipes): MODE Mod, SCALE Off, MOTION Sine; manual quote "When SCALE is off you will get classic, bendy pitch modulation, useful for creating chorusing, flanging, and tape-style warble"; dry+wet beating = chorus, pull DRY to zero = true vibrato ("kill dry for vibrato/lo-fi" — Snyder, Superbooth); STATE Compressed for factory #1 COMPRESSED CHORUS character.
- Factory #1 COMPRESSED CHORUS ("smooth modulation… dreamy… compressed") + MOD = chorus/flanger zone, not a delay: `gear/Chase Bliss Big Time/research/links/cb-big-time-factory-presets-recipes.md`.
- VOICING HiFi "useful for modulation" + STATE Compressed mechanics: `gear/Chase Bliss Big Time/research/transcripts/sonicstate-superbooth-john-snyder-eae-interview.md`; `gear/Chase Bliss Big Time/manuals/Big+Time_Manual_Chase+Bliss.pdf`.
- STEP non-functional in MOD (TAP LEFT toggles MOTION instead): `research/bloops/2026-06-19-chase-bliss-big-time.md` (candidate index chunks).
- Distinctness checked against `Patches/Chase Bliss Big Time/mod-slap-comb-flange-double.md` (MOD slap → comb → flange, FEEDBACK-into-flanger; this patch is clean chorus↔vibrato with low FEEDBACK).

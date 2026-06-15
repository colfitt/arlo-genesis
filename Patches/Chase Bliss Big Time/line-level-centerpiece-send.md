---
type: patch
title: Line-Level Centerpiece Send
device: Chase Bliss Big Time
date: 2026-06-15
description: "A wet-only aux/centerpiece configuration of Big Time for a LINE-LEVEL synth/sampler source (OP-1 Field, Digitakt 2, MPC) — one saturating stereo delay unifies a whole part, DRY KILL returns 100% wet into a parallel/aux path, COLOR stays low because line sources are already hot, and song sections recall by Program Change so the delay re-voices itself hands-free. Designed from the centerpiece minimal-chains + sampler-integration source; method-level controls (DRY KILL, STATE, COLOR-low rule, MIDI CCs) are sourced, numeric fader values are a dialable recipe."
tags: [centerpiece, line-level, aux-send, dry-kill, saturated, clock-locked, synth, sampler, designed, signature]
controls:
  - { name: "Source / Input", type: switch, value: "Line-level source (OP-1 Field via EHX Effects Interface; Digitakt 2 / MPC direct) → IN-L/IN-R stereo", options: ["OP-1 → EHX Interface → stereo in", "DT2/MPC direct stereo in"] }
  - { name: "DRY KILL", type: switch, value: "ON (Options) — Big Time returns 100% wet into a parallel/aux path; this is what makes it a SEND, not an insert", options: ["off (insert)", "on (wet-only / aux)"] }
  - { name: "+12dB input", type: switch, value: "OFF (alt — only engage if the OP-1/source is quiet)", options: ["off", "+12dB"] }
  - { name: "MODE", type: switch, value: "Long (tighter sections → Short)", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Saturated (the one saturating character the part inherits; Compressed to hold dense sections together)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "Warm (Analog for more vintage haze)", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Off (slow Sine for drift)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "low ~25-30% [DIALABLE — line sources are already hot; too much COLOR slams the analog limiter to porridge; bring it up only if the source is quiet]" }
  - { name: "TIME", type: knob, value: "tapped / MIDI clock (CC54 subdivision)" }
  - { name: "CLUSTER", type: knob, value: "~25% for body (raise for multi-tap)" }
  - { name: "TILT EQ", type: knob, value: "noon → slightly up" }
  - { name: "FEEDBACK", type: knob, value: "~45% [DIALABLE]" }
  - { name: "WET", type: knob, value: "~50% or to taste at the aux return [DIALABLE]" }
  - { name: "SPREAD", type: switch, value: "widen", options: ["off", "widen", "ping-pong"] }
  - { name: "MIDI clock", type: knob, value: "CC111 = 0 (follow shared clock); CC54 = subdivision" }
  - { name: "Preset save / recall", type: knob, value: "CC27 = save to slot; PC# = recall slot per song section; PC 0 = LIVE (follow faders)" }
  - { name: "MODE button (hold)", type: button, value: "Panic reset → clean delay if a section runs away" }
---

# Line-Level Centerpiece Send

## Concept
A wet-only aux/centerpiece configuration of Big Time for a LINE-LEVEL synth/sampler source (OP-1 Field, Digitakt 2, MPC). One saturating stereo delay character unifies a whole part; DRY KILL returns 100% wet into a parallel/aux path; COLOR stays low because line sources are already hot; MIDI clock shared and song sections recalled by Program Change so the delay re-voices itself hands-free. This is the minimal, no-fuzz, line-level sibling of the fuzz-wall centerpiece patches — built around DRY KILL + COLOR-low + PC scenes rather than a guitar / Gen-Loss end-board echo. Big Time is marketed as "the perfect centerpiece for a synth setup" precisely because of its balanced/unbalanced line-level stereo I/O, which is what this patch leans on.

## How to play it
1. Feed the line-level source through its level bridge first (OP-1 → EHX Effects Interface), then into Big Time **IN-L / IN-R** (stereo). Digitakt 2 / MPC put out healthy line level and can go in direct.
2. Turn **ON DRY KILL** (Options) so Big Time returns 100% wet — route its output to a parallel/aux return, leaving the dry in the desk.
3. Set **STATE Saturated** and keep **COLOR low (~25-30%)** so the hot line source doesn't clamp the analog limiter; bring COLOR up only if it sounds thin.
4. Slave to shared MIDI clock: **CC111 = 0** (follow). Set subdivision via **CC54** if you want rhythmic taps. Pick ONE clock master — never loop clock.
5. Save a preset per song section via **CC27**, then fire **Program Changes (PC#)** on section changes so the delay re-voices verse→chorus→outro hands-free; **PC 0 = LIVE**.
6. Ride **WET** (or the aux fader) to swell the delay in; hold the **RIGHT footswitch** to FREEZE a phrase into a held bed; hold **MODE** to panic-reset to a clean delay.

## Notes
- **DRY KILL is what makes this an aux SEND** rather than an insert — the delay becomes its own printed voice on a fader, ideal for sketch-to-finish reuse.
- **COLOR-low is effectively mandatory for line-level sources** (they're already hot) — this is the opposite gain-staging from a quiet guitar.
- All numeric fader values here are a **dialable RECIPE, not sourced settings** — Chase Bliss publishes character/intent, not numbers, and Big Time's motorized flying faders override any written values on recall. The method-level choices (DRY KILL, STATE, the COLOR-low rule, the MIDI CCs) ARE sourced.
- Big Time takes MIDI on a **native 5-pin DIN** — no MIDIBox needed (unlike the other CB pedals). Put it on the shared CB channel (ch.2) if you want one PC to jump a whole CB stack at once.
- ⚠️ **MPC Sample distorts kicks/bass when slaved on fw 1.2.1** — if an MPC is the source, run it as clock master (Big Time follows via CC111) or verify the 1.3.x fix before relying on it.

## Sources
- 🟣 designed from `gear/Chase Bliss Big Time/research/links/centerpiece-minimal-chains-and-sampler-integration.md` §C [V/R] (line-level sources, OP-1 → EHX Effects Interface path, COLOR-low for hot line sources, DRY KILL = wet-only aux return, native-DIN clock CC111/CC54, preset save CC27 / recall PC# / PC 0 = LIVE, "+12 dB" alt for quiet sources, MPC fw clock caveat, "the perfect centerpiece for a synth setup" balanced I/O).
- `gear/Chase Bliss Big Time/research/Big-Time-DeepResearch.md` / `Big-Time-UsageGuide.md` (DRY KILL, line-level/balanced I/O, +12dB input).
- `gear/Chase Bliss Big Time/research/transcripts/mark-johnston-secret-weapons-big-time-deep-dive.md` (STATE Saturated character, hold-MODE panic reset, FREEZE; preamp "sounds good on synths/drum machines").

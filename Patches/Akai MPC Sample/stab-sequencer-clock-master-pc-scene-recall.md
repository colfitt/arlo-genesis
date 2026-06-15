---
type: patch
title: Stab Sequencer — Clock Master + PC Scene Recall
device: Akai MPC Sample
date: 2026-06-15
description: "MPC as MIDI clock MASTER playing sparse synth-stab/drum-machine seed events into a clock-locked multitap delay, with Program Change recalling verse/chorus/breakdown scenes hands-free. Designed craft on AC50-confirmed controls + Big Time centerpiece sampler-integration research; not a documented artist patch."
tags: [taste-profile, clock-master, program-change, stabs, sequencer, designed, signature]
controls:
  - { name: "Sync (Preferences → Sync)", type: switch, value: "MASTER (MIDI Clock Out ON, USB / TRS MIDI out to Big Time)", options: ["Master", "Slave"] }
  - { name: "Stab pattern", type: knob, value: "sparse half-bar / dotted-8th grid (leave gaps for the delay taps)" }
  - { name: "Stab voice", type: knob, value: "short synth/drum-machine one-shot, tight Amp decay = clean transient" }
  - { name: "Tune", type: knob, value: "to song key (kick/root if drum-machine)" }
  - { name: "Filter (as EQ)", type: knob, value: "HPF the stab to leave low end for the crushed delay" }
  - { name: "Pan", type: knob, value: "center for mono→MISO, or hard-panned pair for stereo" }
  - { name: "Program Change", type: switch, value: "on section boundaries → MPC scene (stab voice + pattern) flips on the downbeat" }
  - { name: "Output", type: switch, value: "stereo out → Big Time stereo ins (or one mono stab → IN-L auto-MISO)" }
  - { name: "Slot/Bank", type: knob, value: "one pad bank per scene; PC selects the scene" }
---

# Stab Sequencer — Clock Master + PC Scene Recall

## Concept
The MPC playing sparse synth-stab / drum-machine voices as the rhythmic SOURCE for a downstream multitap delay, running as MIDI clock MASTER (its fw 1.2.1 slave-distortion bug means it must never be slaved) and using Program Change messages to recall verse/chorus/breakdown scenes hands-free. Deliberately sparse on purpose — the stabs are meant to be multiplied into a groove by the Big Time's CLUSTER taps, so this patch supplies the seed events + the clock + the arrangement, not a finished beat.

## How to play it
1. Set the MPC as MIDI clock MASTER (Preferences → Sync, Clock Out ON) — do NOT slave it (fw 1.2.1 distorts audio when slaved; verify any 1.3.x fix before trusting the other direction).
2. Sequence a SPARSE stab pattern on a half-bar / dotted-8th grid — leave gaps, because the Big Time's CLUSTER taps will fill them.
3. Pick a short stab voice (tight Amp decay) so each hit is a clean transient; Tune to song key; HPF a touch so the crushed delay owns the lows.
4. Set the audio out (stereo, or one mono stab into Big Time IN-L for auto-MISO) and send MIDI clock so the Big Time locks (its CC111=0).
5. Program Change on section boundaries to recall verse/chorus/breakdown scenes hands-free; optionally mirror the PC to recall a matching Big Time slot so both flip on the same downbeat.

## Notes
- ⚠️ MPC Sample (AC50) distorts audio when MIDI-SLAVED on fw 1.2.1 — it must run as clock MASTER here. Verify the 1.3.x fix before ever slaving it.
- Sparse-by-design: the part you hear is mostly the Big Time's CLUSTER taps; this patch is the seed, not the finished groove.
- ⚠️ Knob/scene specifics are a dialable recipe (designed craft on AC50-confirmed controls), not a sourced artist patch.
- Source Recall does NOT work on the built-in mic (works on Resample) — capture stabs via Resample if grabbing a jam.

## Sources
- 🟣 designed — clock-master mandate + CC/PC sampler-integration from `Gear/Chase Bliss Big Time/research/links/centerpiece-minimal-chains-and-sampler-integration.md` §C and the Big Time `lo-fi-rhythmic-groove.md` MPC-slave-distortion warning.
- Ref: LCD / filter-house / lo-fi groove-first stab source — `Research/Taste-Profile/electronic.md`.
- AC50 controls (Tune/Filter/Pan/Resample/Sync) from `Patches/Akai MPC Sample/4-on-the-floor-909-808-kit-cowbell.md` + `cohesive-tuned-kit-whole-kit-build.md` + `resample-to-bake-fx-sequence-length-loop-bounce.md`.
</content>
</invoke>

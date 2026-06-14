---
type: patch
title: Snappy One-Shot — Transient + Tight Decay
device: Akai MPC Sample
date: 2026-06-14
description: Tighten any sampled drum hit into a punchy one-shot — the single biggest "snap" move, using the Transient Knob FX plus a clipped decay tail.
tags: [drum-craft, one-shot, transient, punch, factory, designed, signature]
controls:
  - { name: "Polyphony", type: switch, value: "Mono (One Shot, Note On off)", options: ["Mono", "Poly"] }
  - { name: "Amp Env Attack", type: knob, value: "0" }
  - { name: "Amp Env Decay", type: knob, value: "25–45 (of 127)" }
  - { name: "Decay From (Shift+K2)", type: switch, value: "Start", options: ["Start", "End"] }
  - { name: "Vel Sens", type: knob, value: "90–110 (of 127)" }
  - { name: "Transient Knob FX K1 Attack", type: knob, value: "+30…+60%" }
  - { name: "Transient Knob FX K2 Shape", type: knob, value: "~40%" }
  - { name: "Transient Knob FX K3 Sustain", type: knob, value: "−20…−50%" }
  - { name: "Normalize (Shift in Trim/Mix/Amp)", type: button, value: "Normalize to 0 dB before baking" }
  - { name: "Resample (Pad 11)", type: button, value: "Bake to make permanent" }
  - { name: "Slot/Bank", type: knob, value: "Per-pad (Sample > Amp Env + Knob FX = Transient)" }
---

# Snappy One-Shot — Transient + Tight Decay

## Concept
The single biggest "snap" move on the AC50 — turning any sampled drum hit (kick/snare/perc) into a tight, punchy one-shot. The Amp Env clips the tail for punch and space, and the Transient Knob FX exaggerates the attack while cutting the ring. This corrects the old "no transient shaper" claim: the Transient Knob FX is the confirmed designer (manual p.54).

## How to play it
1. On the Play page, set Polyphony = Mono so the pad behaves as a One Shot (Note On off).
2. Amp Env: Attack = 0; Decay ≈ 25–45 (of 127). `Shift+K2` set Decay From = Start so the tail is clipped (punch + space).
3. Set Vel Sens ≈ 90–110 for dynamics.
4. Add the Transient Knob FX on that pad: K1 Attack +30…+60%, K2 Shape ~40%, K3 Sustain −20…−50% (cuts ring, exaggerates the hit).
5. Normalize first (`Shift` in Trim/Mix/Amp).
6. Bake it permanent with Resample (Pad 11).

## Notes
- The Transient FX is the confirmed designer (manual p.54) — corrects the older "no transient shaper" claim.
- The Decay=0 / Decay-From-Start variant doubles as the fix for "my samples fade out unexpectedly."

## Sources
- 🟢 manual ranges `research/links/manual-fx-parameter-reference-knob-fx-color-vintage.md` (Amp Env + Transient, UG v1.3 pp.25,54)
- 🟣 punch shaping designed from `research/links/craft-punchy-drum-samples-on-the-ac50.md` + `research/links/mpcforums-ac50-amp-envelope-fade-and-note-on-sustain.md`
- Transformed from Pedalxly MPC-Sample-Patches.md (factory + designed)

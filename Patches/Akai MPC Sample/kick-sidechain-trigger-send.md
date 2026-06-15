---
type: patch
title: Kick Sidechain Trigger Send
device: Akai MPC Sample
date: 2026-06-15
description: "A tight, transient-forward kick one-shot assigned to its OWN MPC output so a 1/8\" cable can key an external pedal's sidechain (Chase Bliss Clean) without ever being summed into the wet path. AC50 control ranges (Mono polyphony, Amp Env, Transient Knob FX p.54) are manual-confirmed; using the pad as a dedicated outboard sidechain trigger send is a DESIGNED routing, not a documented artist patch."
tags: [sidechain, trigger, kick, one-shot, drum-craft, routing, designed]
controls:
  - { name: "Polyphony", type: switch, value: "Mono (One Shot)", options: ["Mono", "Poly"] }
  - { name: "Amp Env Attack", type: knob, value: "0" }
  - { name: "Amp Env Decay", type: knob, value: "short (~25–45 of 127)" }
  - { name: "Decay From (Shift+K2)", type: switch, value: "Start (clipped tail = punch + clean trigger edge)", options: ["Start", "End"] }
  - { name: "Vel Sens", type: knob, value: "~90–110 (of 127)" }
  - { name: "Transient Knob FX K1 Attack", type: knob, value: "+30…+60%" }
  - { name: "Transient Knob FX K2 Shape", type: knob, value: "~40%" }
  - { name: "Transient Knob FX K3 Sustain", type: knob, value: "−20…−50% (cut ring → snappy trigger)" }
  - { name: "Tune", type: knob, value: "to taste (pitch irrelevant to the trigger — set for feel/headroom)" }
  - { name: "Output routing", type: switch, value: "dedicated MPC output (NOT the main mix bus) → 1/8\" TS to Clean's sidechain jack" }
  - { name: "Pattern", type: knob, value: "program at the subdivision the gate should pulse (four-on-the-floor = steady chop; syncopated = stuttering bloom)" }
---

# Kick Sidechain Trigger Send

## Concept
A dedicated kick send whose only job is to drive an outboard sidechain. The kick is built as a tight, transient-forward one-shot and assigned to its OWN output so a 1/8" cable can carry it into Clean's sidechain jack while the wet effect chain never sums it. Program the kick at whatever subdivision you want the downstream gate to pulse — four-on-the-floor for a steady chop, syncopation for a stuttering bloom. It's the metronome that drives the swelling reverb gate; you hear the beat (if at all) only through the MPC's separate main outs.

## How to play it
1. Build a tight kick one-shot: Polyphony Mono, Amp Attack 0, short Decay, `Shift+K2` Decay From = Start.
2. Add Transient Knob FX (K1 Attack +30…+60%, K3 Sustain −20…−50%) so the hit is snappy with little ring — a clean trigger edge.
3. Assign the kick pad to a DEDICATED MPC output (not the main mix); run a 1/8" TS from that out to Clean's sidechain jack.
4. Keep the MPC's main outs going to the mixer separately if you want to hear the beat — the trigger send is audio-key only.
5. Program the kick at the subdivision you want the reverb gate to pulse (four-on-the-floor = steady chop; syncopated = stuttering bloom).
6. Tune to taste — pitch is irrelevant to the trigger, set it for feel/headroom into the sidechain.

## Notes
- The kick is a TRIGGER, not part of the wet path — it keys Clean's swell and is never summed into the reverb wash.
- Mono / short-decay / transient-forward = a clean, reliable trigger edge so the downstream sidechain fires once per hit, no double-triggers.
- ⚠️ AC50 control RANGES (Mono polyphony, Amp Env, Transient Knob FX p.54) are manual-confirmed; using the pad as a dedicated outboard sidechain trigger send is a DESIGNED routing, not a documented artist patch. Exact Decay/Transient values are a dialable recipe.
- Swap the pattern to change the rhythm of the downstream gate without touching the pedal.

## Sources
- 🟢 manual ranges `research/links/manual-fx-parameter-reference-knob-fx-color-vintage.md` (Amp Env + Transient Knob FX, UG v1.3 pp.25,54; Mono/One-Shot polyphony p.25)
- 🟣 designed trigger-send routing (kick to a dedicated output to key an outboard sidechain) from `research/links/craft-punchy-drum-samples-on-the-ac50.md` + the Clean sidechain move
- Ref: `Patches/Akai MPC Sample/snappy-one-shot-transient-tight-decay.md` (kick snap recipe basis)

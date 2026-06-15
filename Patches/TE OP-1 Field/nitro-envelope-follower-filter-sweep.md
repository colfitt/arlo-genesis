---
type: patch
title: "Nitro — envelope-follower auto-wah sweep"
device: TE OP-1 Field
date: 2026-06-15
description: "A dialable recipe (no published values) for an auto-wah / breathing dynamic-sweep using the Nitro FX — a dual self-oscillating filter with an envelope follower on cutoff. Drive a synth or sampled loop through it and let the follower open the filter on transients. Effect description synthesized from the magazinmehatronika Field review (Nitro = dual filter, envelope follower on cutoff, self-oscillating) + an op1tips forum tip (Element LFO in envelope mode for a manual sweep)."
tags: [effect, nitro, filter, envelope-follower, auto-wah]
dips:
  Safety: "both filters can self-oscillate — back off resonance if it howls"
controls:
  - { name: "FX", type: switch, value: "Nitro (load on Synth FX slot or Master FX)" }
  - { name: "Filter band", type: knob, value: "set where you want the focus — dial by ear" }
  - { name: "Resonance", type: knob, value: "raise for character; push toward self-oscillation for a whistle (back off if it howls)" }
  - { name: "Envelope follower", type: knob, value: "let it track input dynamics so cutoff opens on transients (auto-wah motion)" }
  - { name: "LFO", type: switch, value: "element (envelope mode) → filter cutoff for a manual sweep — optional alternative", options: ["value","tremolo","random","element","t_scale"] }
---

# Nitro — envelope-follower auto-wah sweep

## Concept

Nitro is a dual self-oscillating filter with an envelope follower on cutoff. Drive a synth or a sampled loop through it and let the follower open the filter dynamically — the cutoff tracks input transients for auto-wah / breathing dynamic-sweep movement. It is especially good on drum loops, where the per-hit dynamics give the filter something to chew on. On the OP-1 Field, Field describes Nitro as a dual self-oscillating filter with envelope follower (it was a band-pass-style filter on the original OP-1). For a hands-on alternative to the follower, an Element LFO in envelope mode can be assigned to filter cutoff for a manual sweep.

## How to play it

1. Load **Nitro** on the Synth FX slot or as a Master FX.
2. Set the **filter band** where you want the focus.
3. Raise **resonance** for character — push toward self-oscillation for a whistle.
4. Let the **envelope follower** open cutoff on transients for auto-wah motion (great on a drum loop).
5. Alternatively, assign an **Element LFO (envelope mode) → filter cutoff** for a manual sweep instead of the follower.

## Notes

- **No published numeric values** — this is a dialable recipe, not sourced knob positions. The effect is described qualitatively in the review/forum tip; tune band, resonance, and follower amount by ear.
- HONESTY FLAG: both filters can self-oscillate — back off resonance if it howls.
- Field describes Nitro as a dual self-oscillating filter with an envelope follower on cutoff (it was a band-pass-style filter on the OG OP-1).
- Great on drum loops for breathing dynamic movement.

## Sources

- magazinmehatronika.com/en/op-1-field-review/ (Nitro = dual filter, envelope follower on cutoff, self-oscillating)
- github.com/ratbag98/op1tips (Element LFO in envelope mode → filter cutoff for sweep)
- dialable recipe (no published values) — effect description from review + forum tip

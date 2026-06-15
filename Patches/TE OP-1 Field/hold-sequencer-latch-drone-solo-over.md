---
type: patch
title: "Hold sequencer — latch a drone, solo above"
device: TE OP-1 Field
date: 2026-06-15
description: "The Field's Hold sequencer as a one-person drone rig — set a break point, latch low notes below it as a sustained drone, and play freely above while GRAY transposes the held chord in key. The banjo/baritone drone-bed-with-lead-on-top performance, hands-free. Documented in the new-sequencer walkthroughs (ADG, digiphex, loopop) — method-level, no published values."
tags: [drone, performance-setup, hold-sequencer, sustained, designed, signature]
dips:
  Polyphony cap: "~10 voices — you can't latch every key"
controls:
  - { name: "Sequencer", type: switch, value: "Hold", options: ["Pattern","Tombola","Endless","Finger","Sketch","Arpeggio","Hold"] }
  - { name: "Hold BLUE (break point)", type: knob, value: "set so notes below = held, notes above = free" }
  - { name: "Hold GRAY (transpose in key)", type: knob, value: "transpose held note(s)/chord in key" }
  - { name: "Hold GOLD (poly/mono)", type: switch, value: "poly or mono — in mono, same note toggles off", options: ["poly","mono"] }
  - { name: "ORANGE (press = clear / rotate = toggle Hold)", type: knob, value: "press to clear held notes; rotate to toggle Hold on/off" }
---

# Hold sequencer — latch a drone, solo above

## Concept

The Field's **Hold** sequencer turned into a one-person drone rig. You set a **break point** (BLUE): everything you play **below** it gets latched and held, everything **above** it plays freely. Hold a low note or chord under the break point and it sustains as a drone while both hands are free to solo a lead on top — the classic banjo/baritone "drone bed with the melody over it" performance, hands-free. **GRAY** transposes the held chord in key as you go, so the drone can move under the lead. This is the Hold-sequencer *technique* itself, distinct from the slow-ambient drone setup patch (which is the tempo/tape/envelope staging it lives inside).

## How to play it

1. `[Shift]+[Sequencer]` → **Hold**.
2. Set the **break point** (BLUE) so low notes hold and high notes don't.
3. Latch a low note or chord **below** the break point — it sustains as a drone.
4. Play a lead freely **above** the break point.
5. Use **GRAY** to transpose the held drone/chord in key; press **ORANGE** to clear.

## Notes

- Documented new-sequencer behavior (ADG, loopop, digiphex). Method-level — **no published knob values**; controls above are a dialable recipe, not sourced settings.
- **GOLD** sets poly vs. mono; in mono, pressing the same held note again toggles it off.
- Honesty flag: there's a **~10-voice polyphony cap**, so you can't latch every key — budget your held drone voices against whatever the lead needs.
- Pairs with the slow-ambient drone setup; that patch is the staging, this is the performance technique that runs inside it.

## Sources

- Gear/TE OP-1 Field/research/transcripts/adg-op1-field-full-walkthrough-for-owners.md (§Hold sequencer)
- Gear/TE OP-1 Field/research/transcripts/digiphex-op1-field-sequencers-tutorial.md (§HOLD)
- Gear/TE OP-1 Field/research/OP-1-Field-UsageGuide.md §1 (Hold — drone + solo), §5
- Method technique (ADG, digiphex, loopop) — method-level, no published values

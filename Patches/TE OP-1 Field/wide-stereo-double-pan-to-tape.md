---
type: patch
title: "Wide stereo double — [Shift]+Orange pan-to-tape"
device: TE OP-1 Field
date: 2026-06-15
description: "Turn a mono banjo or baritone into a wide stereo part with no FX — [Shift]+Orange sets the record PAN to the tape track, so you record one mono pass hard-left and a second pass hard-right, and two mono takes become a wide stereo double. Rig-native width, no master FX slot consumed. The [Shift]+Orange pan-to-tape trick is documented (op-forums abyssody/Heyes, ratbag98); pan is hard-L/hard-R, method-level otherwise."
tags: [width, stereo, tape-trick, designed, signature]
controls:
  - { name: "[Shift]+Orange (set record pan)", type: switch, value: "set the record PAN to the tape track" }
  - { name: "Pass 1 pan", type: knob, value: "hard LEFT (record the mono part)" }
  - { name: "Pass 2 pan", type: knob, value: "hard RIGHT (re-record the same part)" }
  - { name: "[Shift]+Tempo (optional detune)", type: knob, value: "detune one pass +/-20 cents for a tuned chorus — see the chorus-pad patch" }
  - { name: "Slot/Bank", type: knob, value: "tape recipe (pairs with banjo / baritone mono sources)" }
---

# Wide stereo double — [Shift]+Orange pan-to-tape

## Concept

Turn a mono banjo or baritone into a **wide stereo part with no FX**. `[Shift]+Orange` sets the record PAN to the tape track, so you record one mono pass hard-left and a second pass hard-right. Two mono takes become a wide stereo double — rig-native width, no master FX slot consumed. This is the plain dry double; the tuned +/-20-cent variant is already the chorus-pad patch.

## How to play it

1. `[Shift]+Orange` to set the record pan to tape.
2. Record the mono part (banjo / baritone) panned **hard LEFT**.
3. Re-record the same part panned **hard RIGHT**.
4. Playback = a wide stereo double from two mono takes.
5. For a tuned chorus instead, detune one pass +/-20 cents (`[Shift]+Tempo`).

## Notes

- Documented community trick (op-forums abyssody/Heyes, ratbag98). Pan = hard-L / hard-R; method-level otherwise — no further published knob values, so treat the rest as a dialable recipe.
- Consumes no FX slot. The +/-20-cent variant is already the chorus-pad patch; this is the plain dry double.

## Sources

- Gear/TE OP-1 Field/research/links/op-forums-op1-field-workflows-tips.md (§Shift+Orange pan for recording)
- Gear/TE OP-1 Field/research/links/github-ratbag98-op1tips-distilled.md
- Gear/TE OP-1 Field/research/OP-1-Field-UsageGuide.md §1 ([Shift]+Orange pan to tape)

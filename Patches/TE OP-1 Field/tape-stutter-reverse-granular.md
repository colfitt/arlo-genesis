---
type: patch
title: "Tape stutter — reverse-granular glitch fills"
device: TE OP-1 Field
date: 2026-06-15
description: "On-box tape performance — tap the stutter/chop button on the beat and press it repeatedly to creep BACKWARDS through the tape, generating reverse-granular stutters and glitch fills directly on recorded material. No plugins, all hardware gesture, tempo-synced (forum recipe, op1tips — performance gestures documented, no published knob values)."
tags: [tape, stutter, glitch, reverse, performance, granular]
dips:
  TAPE_STOP_QUALITY: "Blue knob alongside the tape-stop button changes the quality of the slowdown."
controls:
  - { name: "Mode", type: switch, value: "Tape", options: ["Synth","Drum","Tape","Mixer"] }
  - { name: "Stutter/chop button (6)", type: switch, value: "tap on the beat; press repeatedly to creep BACKWARDS for reverse-granular stutters (tempo-synced)" }
  - { name: "Stutter quality (white knob)", type: knob, value: "twist while stuttering to change the stutter character (dial to taste — no published value)" }
  - { name: "Brake button (4)", type: switch, value: "tape slowdown; hit tape-stop + reverse together for an instant no-slowdown hard stop" }
  - { name: "Slowdown quality (blue knob)", type: knob, value: "alongside tape-stop, changes the quality of the slowdown (dial to taste — no published value)" }
---

# Tape stutter — reverse-granular glitch fills

## Concept

Use the tape stutter/chop button to creep backwards through the tape, generating reverse-granular stutters and glitch fills directly on recorded material — no plugins, all hardware gesture, tempo-synced. The stutter button scrubs playback in sync with tempo; pressing it repeatedly creeps the playhead BACKWARDS, which is the documented way to wring reverse-granular textures out of any audio already on tape. The white knob alongside the stutter changes the stutter quality, and the brake button gives you a tape slowdown — or hit tape-stop + reverse simultaneously for an instant, no-slowdown hard stop.

## How to play it

1. Play the tape and tap the stutter/chop button (6) on the beat.
2. Press it repeatedly to creep backwards for reverse-granular stutters.
3. Twist the white knob while stuttering to change the stutter character.
4. Use Brake (4) for a slowdown, or tape-stop + reverse together for an instant hard stop.
5. Record the performance pass as the take.

## Notes

- These are tempo-synced performance gestures, not menu settings.
- Repeated stutter creeping is the documented way to get reverse-granular textures from any tape audio.
- Method-level recipe — no published knob values. The white (stutter quality) and blue (slowdown quality) knobs above are dialable to taste, not sourced settings; the button gestures are the documented part.

## Sources

- github.com/ratbag98/op1tips (stutter button creeps backwards = reverse granular; white knob changes quality; tape-stop + reverse = instant stop)

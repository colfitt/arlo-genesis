---
type: patch
title: STRT-LFO Generative Scrub (endless-variation drone engine)
device: Elektron Octatrack MkII
date: 2026-06-14
description: Endless-variation drone/texture from a single captured wall — generative scrubbing via an LFO on STRT, no resequencing needed (Elektronauts "OT special tricks").
tags: [drone, generative, lfo, slicing, tape-feel, community, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Bank B / Part 1 · LFO → STRT on any Flex/Static track" }
  - { name: "LFO → STRT", type: switch, value: "scrubs through a sample/chain for endless variation; on a sliced sample rolls through different slices" }
  - { name: "HOLD-triggered LFO on slice start", type: switch, value: "auditions a whole sample chain" }
  - { name: "Slide trigs on RATE", type: switch, value: "tape-inertia PIPO (ping-pong) / pitch glides (tape-stop/start feel)" }
  - { name: "Sample-lock + slice-lock", type: switch, value: "CAN combine with p-locks on the same step (different sample AND filter/pitch per step)" }
  - { name: "The dice", type: button, value: "[TRACK PARAM]+[YES] randomizes the current param page (+[NO] reloads saved); pair with PART RELOAD [FUNC]+[CUE]" }
---

# STRT-LFO Generative Scrub (endless-variation drone engine)

## Concept
Endless-variation drone/texture from a single captured wall — generative scrubbing, no resequencing needed. An LFO on STRT (Playback page) scrubs through a sample or chain for endless variation; on a sliced sample/chain it rolls through different slices ("different drum kits" from one chain). The STRT-LFO scrub, slide-trig RATE tape-feel, and the dice are the most on-aesthetic moves for evolving degraded textures.

## How to play it
1. Put an **LFO on STRT** (Playback page) — scrubs through a sample/chain for endless variation; on a sliced sample/chain it rolls through different slices.
2. Audition a whole sample chain via a **HOLD-triggered LFO** on slice start.
3. **Slide trigs on RATE** = tape-inertia PIPO (ping-pong) / pitch glides (tape-stop/start feel — on-aesthetic for degraded tape).
4. Sample-lock + slice-lock **CAN combine with p-locks** on the same step (different sample AND filter/pitch per step).
5. **The dice:** [TRACK PARAM]+[YES] randomizes the current param page (+[NO] reloads saved) — pair with PART RELOAD ([FUNC]+[CUE]) to tweak destructively then snap back.
6. Remove a lock surgically: hold [NO]+the PARAM knob while the sequencer plays over the step.

## Notes
- Technique grab-bag — the STRT-LFO scrub + slide-trig RATE tape-feel + the dice are the most on-aesthetic for evolving degraded textures.
- ⚠️ MIDI-track CC p-lock gotcha: OT filters out unchanged CCs, so a p-lock equal to the track default WON'T send.

## Sources
- Ref: Elektronauts "OT special tricks" community thread
- research/links/elektronauts-hidden-features-tricks.md (/7416, /14486)
- Transformed from Pedalxly Octatrack-MkII-Patches.md (community)

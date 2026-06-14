---
type: patch
title: Reverse-over-Modulated-Granular-Bed
device: Hologram Microcosm
date: 2026-06-14
description: Organic, modulated granular bed driven by Digitakt MIDI tracks + LFOs, then flipped to Reverse for the payoff — a mono source comes out wide.
tags: [granular-bed, reverse, digitakt, cc-modulation, organic, performance, community, signature]
hidden:
  MIDI channel: Microcosm listens on Ch 1
  CC targets: "Activity=CC 6, Repeats=CC 11, Time=CC 10, Filter=CC 8, Space=CC 12"
  Clock-vs-CC trap: to hand-modulate Time via CC 10 you must turn OFF Digitakt Clock Send (clock overrides CC 10)
controls:
  - { name: "Engine", type: switch, value: "a granular engine (organic, modulated bed)" }
  - { name: "Activity (CC 6)", type: knob, value: "Digitakt LFO destination (randomize for organic granulation; slow triangle/sine for gentle sway)" }
  - { name: "Reverse (press selector in)", type: button, value: "flip over the modulated bed (CC 47)" }
  - { name: "Slot/Bank", type: knob, value: "YELLOW #51 alt (PC 51)" }
---

# Reverse-over-Modulated-Granular-Bed

## Concept
Organic, modulated granular bed driven by Digitakt MIDI tracks + LFOs, flipped to Reverse for the payoff. The Digitakt's track LFO modulates a Microcosm CC destination (randomize for organic granulation; slow triangle/sine for a gentle sway), then you flip Reverse over the modulated bed. "I love the Microcosm in reverse setting — sounds beautiful." A mono source comes out wide (the engines generate genuine stereo).

## How to play it
1. Set the Digitakt MIDI track to Ch 1 (Microcosm listens on Ch 1).
2. Target a CC: Activity=CC 6, Repeats=CC 11, Time=CC 10 (also Filter=CC 8, Space=CC 12).
3. Assign the track LFO to that CC destination (randomize for organic granulation; slow triangle/sine for a gentle sway).
4. After arming, stop/start transport to begin the CC stream.
5. Flip REVERSE (press selector / CC 47) over the modulated bed.

## Notes
- Cited workflow — the exact Digitakt-drives-Microcosm pairing in this rig.
- CLOCK-vs-CC trap: to hand-modulate Time via CC 10 you must turn OFF Digitakt Clock Send (clock overrides CC 10) — choose clock-sync OR CC-Time, not both.
- A mono source comes out wide (engines generate genuine stereo).

## Sources
- `research/transcripts/youtube-microcosm-digitakt-cc-modulation-workflow.md`
- Transformed from Pedalxly Microcosm-Patches.md (community)

---
type: patch
title: OT-as-Live-Mixer (Cavagnaro dual Thru-per-input)
device: Elektron Octatrack MkII
date: 2026-06-14
description: The simplest OT-as-live-mixer/FX-unit setup — two external sources, each through its own Thru track with filter + delay, mutable from the front panel (Ron Cavagnaro method).
tags: [live-fx, mixer, thru-machine, community, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Bank A / Part 1 · Track 1 Thru (input A), Track 2 Thru (input B)" }
  - { name: "Track 1 machine", type: switch, value: "Thru, input = A", options: ["Static", "Flex", "Thru", "Neighbor", "Pickup"] }
  - { name: "Track 2 machine", type: switch, value: "Thru, input = B", options: ["Static", "Flex", "Thru", "Neighbor", "Pickup"] }
  - { name: "Track 1 trig", type: button, value: "ONE trig on the track (opens the channel continuously)" }
  - { name: "FX1 default", type: switch, value: "Filter (tweak cutoff + WIDTH live)" }
  - { name: "FX2 default", type: switch, value: "Delay (raise SEND per track to feed it)" }
  - { name: "PROJECT > MIDI > SYNC", type: switch, value: "enable transport + clock send/receive as needed" }
  - { name: "Mute", type: button, value: "[FUNC]+track key (yellow = muted, red = active)" }
---

# OT-as-Live-Mixer (Cavagnaro dual Thru-per-input)

## Concept
The on-ramp to using the OT as the rig's live mixer/FX unit: two external sources, each routed through its own Thru track with a filter and a delay, mutable from the front panel. This is the simplest version before scenes and resampling are layered on. The pedalboard stereo print can feed A/B (a Thru per pair, or one Thru INAB = A B for the stereo pair).

## How to play it
1. PROJECT > MIDI > SYNC: enable transport + clock send/receive as needed.
2. **Track 1 = Thru, input = A**; place **ONE trig** on the track — Thru passes audio only across a triggered step, so one trig opens the channel continuously.
3. **Track 2 = Thru, input = B**.
4. FX1 default = filter (tweak cutoff + WIDTH live); FX2 default = delay (raise SEND per track to feed it).
5. Mute a channel by holding **[FUNC]+track key** (yellow = muted, red = active).

## Notes
- The on-ramp before scenes/resampling are layered on.
- Rig map: pedalboard stereo print → A/B → a Thru per pair (or one Thru INAB = A B for the stereo pair).
- MkI tutorial, identical engine to MkII. yt-dlp verified.

## Sources
- Ref: Ron Cavagnaro "OT As A Mixer: Thru Machine Basics" (MkI, identical engine)
- research/transcripts/cavagnaro-ot-as-mixer-thru-machine-basics.md (youtube V0QMTiJicVA)
- Transformed from Pedalxly Octatrack-MkII-Patches.md (community)

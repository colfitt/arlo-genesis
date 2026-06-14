---
type: patch
title: Dual-Rhythm Multi-Tap (MIDI)
device: UAFX Del-Verb
date: 2026-06-14
description: A MIDI-only rhythmic-echo patch — a dual-rhythm delay subdivision (CC25=4 or 5) reachable only via app or CC, with a hi-cut ping-pong delay into a Cascade 224 Hall. Requires a USB-host MIDI controller. Not signature-fit; technique/utility.
tags: [midi, utility, multi-tap, rhythmic, electronic, technique, designed]
hidden:
  Delay Division (CC25): "4 = Dual 1/4 + dotted-1/8, OR 5 = Dual 1/4 + 1/8 — multi-tap patterns NOT settable from hardware tap"
controls:
  - { name: "Delay Model", type: switch, value: "Precision (CC14=2)", options: ["Tape EP-III", "Analog DMM", "Precision"] }
  - { name: "Delay voicing (app-assigned)", type: switch, value: "Stereo Ping Pong Hi-Cut" }
  - { name: "Reverb Model", type: switch, value: "Hall 224", options: ["Spring '65", "Plate 140", "Hall 224"] }
  - { name: "Reverb voicing (app-assigned)", type: switch, value: "Cascade 224" }
  - { name: "Reverb", type: knob, value: "noon" }
  - { name: "Delay Division", type: switch, value: "CC25=4 (Dual 1/4 + dotted-1/8) or CC25=5 (Dual 1/4 + 1/8)", options: ["CC25=4", "CC25=5"] }
  - { name: "Feedback (CC24)", type: knob, value: "≈70" }
  - { name: "Mix (CC22)", type: knob, value: "≈64" }
  - { name: "Mod (CC27)", type: knob, value: "0 (off)" }
  - { name: "Reverb level (CC28)", type: knob, value: "≈80" }
  - { name: "Trails", type: switch, value: "ON", options: ["ON", "OFF"] }
---

# Dual-Rhythm Multi-Tap (MIDI)

## Concept
The single most useful "hidden" delay feature: dual-rhythm subdivisions that cannot be set from the hardware tap — only via the app or CC-25. A hi-cut stereo ping-pong delay running a dual-rhythm pattern (Dual 1/4 + dotted-1/8, or Dual 1/4 + 1/8) feeds a bright "Cascade 224" hall for rhythmic ambient/dub echoes over a locked pulse. Requires a USB-host MIDI controller (Morningstar MC6/MC8 Pro or CME H2MIDI Pro).

## How to play it
1. **Set voicings over Bluetooth first** (Delay "Stereo Ping Pong Hi-Cut," Reverb "Cascade 224"), THEN plug into the MIDI host — the single USB-C port means the host and the UAFX Control app cannot run simultaneously.
2. Park physical knobs at a sane neutral baseline (engine-select snaps every knob to its PHYSICAL position — WYSIWYG).
3. Send messages in the **MANDATORY order**, ~50 ms apart:
   - (1) bypass/unbypass →
   - (2) CC14=2 (Precision Select) + CC15 (Reverb Select) →
   - (3) all param CCs: CC25=4 or 5 (Division), CC24≈70 (Feedback), CC22≈64 (Mix), CC27=0 (Mod off), CC28≈80 (Reverb).
4. Sync the delay to MIDI Beat Clock.
5. Use CC-20 (Reverb Bypass) to toggle reverb independently even in a footswitch mode that can't.

## Notes
- Not signature-fit — technique/utility.
- **GOTCHAS:** (1) sending Delay/Reverb Select mid-stack **WIPES every param CC already sent** — engine-select must come FIRST, params AFTER; (2) **~50 ms minimum** between messages or the pedal ignores changes; (3) the single USB-C port means the MIDI host and the UAFX Control app cannot run at the same time — set voicings over Bluetooth first.

## Sources
- designed from manual MIDI-CC chart (CC-25 dual-rhythm modes 4/5, send-order rule, WYSIWYG knob-snap) + host-device notes — `research/links/midi-official-manual-cc-chart.md`, `research/links/midi-morningstar-forum-delverb-implementation.md`, `research/links/midi-ua-unlock-usb-midi.md`
- Ref: Electronic/groove-first cluster (rhythmic multi-tap echoes over a locked pulse)
- Transformed from Pedalxly Del-Verb-Patches.md (DOUG-designed)

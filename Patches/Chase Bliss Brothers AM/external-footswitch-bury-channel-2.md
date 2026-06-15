---
type: patch
title: "Bury Channel 2 — remote TS footswitch toggle"
device: Chase Bliss Brothers AM
date: 2026-06-15
description: A wiring/utility patch that exploits a documented Brothers AM feature — the MIDI jack doubles as a TS external-footswitch input that bypasses Channel 2. Plug any normally-open momentary footswitch in with a TS (mono) cable and it automatically takes control of Channel 2's on/off, so you can bury the AM elsewhere on the board and still toggle its second channel from a remote switch without running MIDI. As quoted on That Pedal Show's Brothers AM demo and the usage guide; tone is your choice — dial the knobs from the recipe.
tags: [external-footswitch, routing, footswitch-push, utility, designed]
dips:
  MASTER: on
controls:
  - { name: "CHANNEL 1 MODE", type: switch, value: "your always-on voice (e.g. BOOST or OVERDRIVE)", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN 1", type: knob, value: "dial from recipe — no published value" }
  - { name: "VOL 1", type: knob, value: "dial from recipe — no published value" }
  - { name: "TONE 1", type: knob, value: "to taste" }
  - { name: "CHANNEL 2 MODE", type: switch, value: "your kick-on voice (BOOST lift or OVERDRIVE), toggled by the remote footswitch", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN 2", type: knob, value: "dial from recipe — no published value" }
  - { name: "VOL 2", type: knob, value: "dial from recipe — no published value" }
  - { name: "TONE 2", type: knob, value: "to taste" }
  - { name: "PRESENCE", type: knob, value: "to taste" }
  - { name: "MIDI JACK", type: switch, value: "used as TS external-footswitch input — normally-open momentary footswitch via a TS (mono) cable takes control of Channel 2's bypass automatically", options: ["MIDI (TRS cable)", "external footswitch (TS cable, controls Channel 2)"] }
---

# Bury Channel 2 — remote TS footswitch toggle

## Concept
The Brothers AM's MIDI jack does double duty: with a TS (tip-sleeve, mono) cable it becomes an external-footswitch input that bypasses Channel 2. Plug any normally-open momentary footswitch in and it automatically takes control of Channel 2's on/off — no MIDI rig required. That lets you bury the AM somewhere awkward on a crowded board (or off to the side) while keeping its second channel footswitchable from anywhere. Set Channel 1 as your always-on voice and Channel 2 as the kick-on (a BOOST lift or an OVERDRIVE), and the remote stomp becomes your lead/rhythm toggle.

## How to play it
1. Set Channel 1 as your always-on voice and Channel 2 as the kick-on (boost/OD) you want to toggle remotely.
2. Plug a normally-open momentary footswitch into the MIDI jack using a TS (tip-sleeve, mono) cable — it automatically takes control of Channel 2's bypass.
3. Stomp the remote switch to toggle Channel 2 on/off from anywhere on the board.
4. Turn the MASTER dip on so the remote toggle is a controlled level change rather than a jump.

## Notes
- Documented feature: the MIDI jack's TS external-footswitch function (bypasses Channel 2, normally-open momentary, TS cable) is quoted from the source material; the tone is your choice — dial the knobs from the recipe, no published values.
- Useful for burying the AM in a crowded board while keeping its lift footswitchable, with no MIDI rig required.
- Don't use a TRS cable here — the TS (mono) cable is what selects the footswitch function (a TRS cable is for actual MIDI).
- MASTER dip on recommended so the remote Channel 2 toggle doesn't throw stage level.

## Sources
- research/transcripts/tps-vs-prince-duke-of-tone.md ("MIDI jack can also be used to bypass channel two… normally-open momentary foot switch using a TS mono cable… takes control automatically")
- research/links/tps-demo-settings.md (MIDI jack doubles as external footswitch)
- Brothers-AM-UsageGuide.md §3 (MIDI jack doubles as TS external-footswitch input)
- Ref: That Pedal Show — Brothers AM (2025-04-25)

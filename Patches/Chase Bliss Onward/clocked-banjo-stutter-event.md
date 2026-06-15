---
type: patch
title: Clocked Banjo/Loop Stutter Event
device: Chase Bliss Onward
date: 2026-06-15
description: "DOUG-designed glitch-event source at the head of the Onward → Big Time chain: fuses small-SIZE front-transient stutter with clock-locked subdivision so the Glitch channel throws discrete, rhythmic, clock-quantized grains from guitar/loops for Big Time to multitap."
tags: [glitch, stutter, clock-sync, rhythmic, midi, banjo, loops, designed, centerpiece]
hidden:
  SENSITIVITY (on SIZE): toward LESS (so hot per-note transients don't over-trigger)
controls:
  - { name: "Channel", type: switch, value: "GLITCH", options: ["FREEZE", "GLITCH"] }
  - { name: "SIZE", type: knob, value: "small/down-left (catches only the front transient; with MIDI clock present, SIZE = the subdivision)" }
  - { name: "MIX", type: knob, value: "up to taste (audition full)" }
  - { name: "SUSTAIN", type: knob, value: "high (audition max)" }
  - { name: "Glitch retrigger", type: button, value: "CC108 (clock-quantized)" }
  - { name: "SIZE (MIDI)", type: knob, value: "CC14 (ch.2)" }
  - { name: "Tap tempo (no MIDI)", type: button, value: "double-tap BOTH footswitches (left taps tempo, right exits)" }
  - { name: "Slot/Bank", type: knob, value: "recall via PC in the one-PC whole-stack scene" }
---

# Clocked Banjo/Loop Stutter Event

## Concept
The glitch-event source for the 'one direction per song' Onward → Big Time centerpiece. Fuses two existing Onward mechanics into one purpose-built patch: the GLITCH channel with SIZE small (grabs only the front transient, so the percussive pick/loop attack survives as a clean, articulate stutter grain) AND the stutter repeats locked to MIDI clock (with clock present, SIZE = subdivision). The result is discrete, rhythmic, clock-quantized glitch fragments that track the live signal — short events that decay rather than a runaway texture — built specifically to feed Big Time's CLUSTER multitap for stutter-on-stutter rhythmic glitch-delay on a shared grid.

## How to play it
1. Set the channel to **GLITCH**.
2. Turn **SIZE down/left** so it catches only the front transient — the percussive pick or loop attack survives as a clean stutter grain.
3. Send **MIDI clock** (Digitakt 2 master via the CB MIDIbox/TRS) so **SIZE = the subdivision** and the Glitch repeats lock to tempo. With no MIDI, **double-tap BOTH footswitches** to tap tempo (left taps, right exits).
4. Bring **MIX up** and **SUSTAIN high** to audition the stutter density.
5. In the hidden menu, set **SENSITIVITY (on SIZE) toward LESS** so hot transients don't over-trigger.
6. Fire **CC108** to retrigger the Glitch clock-quantized for rhythmic punch-ins; p-lock **SIZE via CC14 (ch.2)** for subdivision changes.
7. Feed the stereo out straight into **Big Time's stereo ins** — one direction, no feedback loop back into Onward.

## Notes
- Purpose-built for the 'Onward → Big Time — Glitch Event Into Space' chain: the event source that Big Time's CLUSTER multitap + DIFFUSE turns into rhythmic→ambient tails.
- Small-SIZE-keeps-the-attack is verified Aaron Rusch behavior; SIZE=subdivision under clock + CC108 retrigger + CC14 SIZE are verified manual/Doug Hanson behavior. Fusing them into one named preset is the designed contribution — **treat the combined recipe as dialable, not a published factory number.**
- One direction per song: Onward feeds Big Time, never the reverse — discrete decaying events plus Big Time's Compressed STATE are what keep the stutter-delay from runaway.
- 🟣 DOUG-designed patch: built by fusing the 'Banjo Rhythmic Stutter Bed' and 'Clock-Synced Glitch Subdivision' patches. Component behaviors are sourced; the combined single-preset numerics are a designed interpretation, flagged as dialable rather than a published factory value.

## Sources
- `research/transcripts/aaron-rusch-onward-glitch-channel.md` (small SIZE keeps the front transient on GLITCH channel)
- `research/transcripts/doug-hanson-onward-demo-feature-rundown.md` + Onward manual pp.8–9, 45 (SIZE=subdivision under MIDI clock; tap-tempo gesture)
- `research/links/cb-stack-clock-sync-per-pedal.md` (CC108 Glitch retrigger clock-quantized, CC14 SIZE on ch.2)
- `research/transcripts/aaron-rusch-onward-hidden-options.md` (SENSITIVITY on SIZE)
</content>
</invoke>

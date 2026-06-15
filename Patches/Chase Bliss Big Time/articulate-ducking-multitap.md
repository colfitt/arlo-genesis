---
type: patch
title: Articulate Ducking Multitap
device: Chase Bliss Big Time
date: 2026-06-15
description: "The centerpiece delay of a clock-locked chain — an articulate, clean multi-tap delay whose Compressed-STATE 'snappy ducking' keeps the repeats out from under the player's attack and blooms them back in the gaps. The articulate, non-lo-fi cousin of the Lo-Fi Rhythmic Groove patch: same MODE Short + CLUSTER multi-tap + clock-lock recipe, but 0.5X crush OFF and tuned for punchy dotted-8th ping-pong repeats. Fed by a gently-leveled source so COLOR stays low and the limiter does musical ducking, not clamping."
tags: [rhythmic, clock-locked, multi-tap, ducking, compressed, articulate, ping-pong, designed, signature]
hidden:
  CC54 subdivision: "dotted-8th (CC54 range 0–12 = 1/16…whole — pick the dotted-8th value)"
  CC111 clock ignore: "0 (clock ignore OFF → follow / slave to the DT2 master)"
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot via CC27; recall by PC on DT2 pattern change" }
  - { name: "Chain / Input", type: switch, value: "Mono source → IN-L (auto-engages MISO mono-in/stereo-out); stereo synth feeds both ins directly", options: ["mono → IN-L (MISO)", "stereo in"] }
  - { name: "MODE", type: switch, value: "Short", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Compressed (snappy ducking — the engine of the patch; holds repeats out from under your fresh attack)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "Focus (keeps the multi-taps articulate and defined)", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off (clock snaps TIME to the quarter note — bend TIME without losing tempo)", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Off", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "0.5X", type: switch, value: "off (crush OFF — this is the CLEAN articulate cousin of Lo-Fi Rhythmic Groove)", options: ["off", "on"] }
  - { name: "COLOR", type: knob, value: "low ~25–30% (bring up only until repeats just begin to compress)" }
  - { name: "TIME", type: knob, value: "MIDI clock (slave) — subdivision dotted-8th via CC54" }
  - { name: "CLUSTER", type: knob, value: "~50% (the multi-tap rhythmic pattern)" }
  - { name: "TILT EQ", type: knob, value: "slightly up" }
  - { name: "FEEDBACK", type: knob, value: "~40% (articulate — decays musically, not a wall)" }
  - { name: "WET", type: knob, value: "~40%" }
  - { name: "SPREAD", type: switch, value: "ping-pong (taps scatter L↔R)", options: ["off", "widen", "ping-pong"] }
  - { name: "MODE button (hold)", type: button, value: "Panic reset → clean simple delay" }
---

# Articulate Ducking Multitap

## Concept
A clock-locked, clean multi-tap delay built around Big Time's Compressed STATE used as "snappy ducking" (ambienttrash 6:46) so the repeats stay out from under your fresh attack and bloom back in the gaps. The articulate, non-lo-fi cousin of the Lo-Fi Rhythmic Groove patch: same MODE Short + CLUSTER multi-tap + clock-lock recipe, but 0.5X crush OFF and tuned for punchy, even, dotted-8th ping-pong repeats that breathe around a groove instead of washing over the line. Fed by a gently-leveled source (Clean), not a hot fuzz — so COLOR stays low and the limiter does musical ducking, not clamping.

## How to play it
1. Slave to MIDI clock: set **CC111 = 0** (clock ignore off, so the pedal follows the DT2 master).
2. Set the subdivision via **CC54** to the dotted-8th value (CC54 range 0–12 = 1/16…whole).
3. MODE **Short**, STATE **Compressed** — this is the "snappy ducking" voice that holds repeats out from under your attack.
4. Dial CLUSTER to **~50%** for the multi-tap rhythmic pattern; SPREAD **ping-pong** to fan the added taps L↔R.
5. Start COLOR **low (~25–30%)** and bring it up only until the repeats just begin to compress — too much COLOR + a hot input clamps the limiter to porridge.
6. Keep FEEDBACK **~40%** so repeats sing and decay musically rather than washing into a wall; ride CLUSTER/WET to swell the delay in for a chorus.
7. Feed it a gently-leveled source (Clean "Home Base") — do NOT double-compress hard, or the Compressed limiter has nothing left to duck.
8. Mono in → **IN-L** auto-engages MISO for stereo ping-pong; a stereo synth feeds both ins directly. Hold **MODE** = panic-reset to a clean simple delay.

## Notes
- Compressed STATE = "snappy ducking" is the documented term that backs this patch (ambienttrash demo 6:46).
- This is the CLEAN articulate version: 0.5X crush is **OFF**, distinguishing it from the Lo-Fi Rhythmic Groove patch (crush ON, COLOR ~40%) and from the Clean Stereo Delay patch (Digital STATE = no limiter, no ducking).
- Big Time takes MIDI natively on a 5-pin DIN — no MIDIBox needed; DT2 DIN MIDI OUT → Big Time MIDI IN directly.
- With SCALE Off, the clock snaps delay TIME to the incoming quarter note so you can bend TIME without losing tempo.
- ⚠ HONEST: only the STATE/MODE/VOICING behavior and the CC54/CC111 clock CCs are verified/sourced; the specific knob clock-face positions (COLOR/CLUSTER/FEEDBACK/WET/TILT) are a dialable recipe set by ear, not published Chase Bliss numerics. Flying faders override on recall — re-trim by ear.

## Sources
- 🟣 designed from `Gear/Chase Bliss Big Time/research/links/centerpiece-minimal-chains-and-sampler-integration.md` §"Rhythmic delay locked to the groove" [V/R] (MODE Short + CLUSTER multi-tap + STATE Compressed locked to clock) and §"Clock-sync" [V] (CC111 = MIDI CLOCK IGNORE FOLLOW=0, CC54 = subdivision 0–12, native 5-pin DIN, COLOR-low gain-staging so the limiter ducks rather than clamps).
- `Gear/Chase Bliss Big Time/research/transcripts/ambienttrash-big-time-full-demo-stereo-NOTES.md` (6:46 "Compressed state — snappy ducking"; reference chain EAE Halberd → Chase Bliss Clean comp → Big Time → Mercury7).
- Big Time MIDI Manual (CC54 subdivision, CC111 clock ignore, CC14–19 knob CCs, PC recall) — chasebliss.com.

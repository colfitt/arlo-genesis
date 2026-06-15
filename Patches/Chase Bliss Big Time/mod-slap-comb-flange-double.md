---
type: patch
title: MOD Slap → Comb/Flange Double
device: Chase Bliss Big Time
date: 2026-06-15
description: "The end-of-chain modulation/slap engine for the 'Deco → Big Time Double-Track Slap Wall' chain — Big Time's most underused voice, MODE Mod (3–46 ms), used as a slapback/chorus/flange engine rather than a delay. It takes Deco's doubled, wobbling source and stacks the 3–46 ms MOD taps on top: a tight slap/double at the short end, then COLOR + FEEDBACK drive the taps into a comb filter and then a flanger for a wide, tape-thickened lead that gets gluier the harder you push it. Maps to factory presets #1 COMPRESSED CHORUS / #2 SLAP/DOUBLE / #5 BROKEN DYNAFLANGE territory. Chase Bliss publishes character, not numbers — all clock-face values are a dialable recipe, and the flying faders override them on recall."
tags: [mod, slapback, chorus, flange, comb-filter, double, modulation, designed, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot (10 internal / 127 via MIDI); recall flies the faders to saved positions" }
  - { name: "Chain / Input", type: switch, value: "Deco doubletracker (doubled + wobbling) → Big Time IN; mono → IN-L auto-engages MISO mono-in/stereo-out, stereo source feeds both ins", options: ["mono → IN-L (MISO)", "stereo in"] }
  - { name: "MODE", type: switch, value: "Mod (3–46 ms — this IS the patch; the slapback/chorus/flange range, NOT a delay)", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Compressed (SLAP/DOUBLE-style burly expander; snappy ducking holds the double together and articulate, not a disintegrating mass)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "Warm (primitive-digital rack-delay filtering — the 'signature elliptical ripple')", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Sine, slow (chorus/flange drift on the short MOD taps)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "low–moderate ~30% (clean slap; push up WITH feedback to drive the taps into comb/flange)" }
  - { name: "TIME", type: knob, value: "short end of MOD for slap → roll toward 46 ms for chorus" }
  - { name: "CLUSTER", type: knob, value: "low ~20% (thickens the double without washing it out)" }
  - { name: "TILT EQ", type: knob, value: "above noon (cut the doubled low-mid mud so the comb/flange peaks read)" }
  - { name: "FEEDBACK", type: knob, value: "~35% (clean slap) → 55–65% (climbs the comb filter into flange — the main 'thicken' control)" }
  - { name: "WET", type: knob, value: "~40%" }
  - { name: "SPREAD", type: switch, value: "widen (open the doubled field; ping-pong if you want the slap to fan L↔R)", options: ["off", "widen", "ping-pong"] }
  - { name: "DRY KILL", type: switch, value: "optional ON (Options menu) for a pure wet MOD field; OFF keeps the doubled dry in front", options: ["off", "on"] }
  - { name: "MODE button (hold 2s)", type: button, value: "Panic reset → clean simple delay if the flange runs away" }
---

# MOD Slap → Comb/Flange Double

## Concept
Big Time's most underused voice: MODE Mod (3–46 ms) used as a slapback/chorus/flange engine, not a delay. At the short end it's a tight slap/double; push COLOR + FEEDBACK and the 3–46 ms taps beat against the dry into a comb filter and then a flanger. Built to sit at the end of a doubled, wobbling source (Deco doubletracker in front) so the MOD taps stack on an already-doubled signal = a wide, tape-thickened lead that gets gluier the harder you push it. Maps to factory presets #1 COMPRESSED CHORUS / #2 SLAP/DOUBLE / #5 BROKEN DYNAFLANGE territory.

## How to play it
1. Set MODE to **Mod** and confirm you hear a slap/double, not a delay — TIME at the short end of the 3–46 ms range.
2. Start with **COLOR low (~30%)** and **FEEDBACK ~35%** for a clean, tight slapback double.
3. Ride **FEEDBACK up toward 55–65%** (and nudge COLOR) — the 3–46 ms taps start beating against the dry into a comb filter, then a flanger. This is the "thickens the more you push it" axis.
4. Roll **TIME** from the short end toward 46 ms to move slap → chorus; **MOTION Sine** adds the drift.
5. Push **TILT EQ above noon** to cut the doubled low-mid mud so the comb/flange peaks read clearly.
6. Use **STATE Compressed** (not Saturated) — the source is a clean doubled lead, so you want the snappy expander/ducking that keeps the slap articulate. Flip **DRY KILL ON** (Options) for a pure wet MOD field.
7. Hold the **MODE button** (2 s) to panic-reset to a clean delay if the flange runs away.

## Notes
- The MOD range (3–46 ms) is Big Time's slapback/chorus/flange voice and is underused in this rig — no other Big Time patch here uses Mod as its core voice. This patch fills that gap.
- Designed to live downstream of a doubled, wobbling source (e.g. Deco "Watery Tape Chorus"): the MOD taps multiply an already-doubled signal for a wide, tape-thickened lead.
- Gain-staging: keep COLOR modest so the analog preamp doesn't slam the limiter and clamp the slap flat. COLOR + FEEDBACK together are the clean-slap ↔ comb ↔ flange dial.
- STATE Compressed is deliberate vs. Saturated — clean doubled lead, not a fuzz wall; want articulate, snappy taps, not a disintegrating mass.
- ⚠️ HONEST: only the MODE/STATE/VOICING/TILT behavior and the factory-preset character are sourced; the specific clock-face positions (COLOR/TIME/CLUSTER/TILT/FEEDBACK/WET) are a dialable recipe set by ear, not published Chase Bliss numerics. On recall the motorized faders fly to the saved positions and override these starting points.

## Sources
- 🟣 DOUG-designed patch. Built on first-party Big Time MODE spec + factory-preset character descriptions (#1/#2/#5) and manual gain-structure/STATE/VOICING mechanics. No numeric fader positions are published by Chase Bliss — all knob values are a dialable recipe (designed starting points), flagged as such; the motorized faders override on recall.
- `gear/Chase Bliss Big Time/research/Big-Time-DeepResearch.md` §spec — MODE "Mod (3–46 ms)" range; COLOR/FEEDBACK gain-structure (manual pp.24–25); VOICING Warm "signature elliptical ripple" (pp.38–39).
- `gear/Chase Bliss Big Time/research/links/cb-big-time-factory-presets-recipes.md` — factory presets #1 COMPRESSED CHORUS ("smooth modulation… dreamy… compressed"), #2 SLAP/DOUBLE ("big, burly expander with two stages of clipping and room-like ambience… doubling and almost-real-time textures"), #5 BROKEN DYNAFLANGE ("a starved flanger… dynamic oscillations that react to your instrument's loudness"); STATE Compressed mechanics (manual pp.34–35); TILT-EQ-up to cut mud (manual pp.38–39).
- `gear/Chase Bliss Big Time/research/Big-Time-UsageGuide.md` — MODES list (MOD ~3–46 ms) and factory-preset names.
- Chain: `Chains/big-time-deco-double-track-slap.md` (DOUG-designed integration).
</content>
</invoke>

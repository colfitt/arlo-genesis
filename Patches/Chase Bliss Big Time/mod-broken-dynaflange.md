---
type: patch
title: MOD Broken Dynaflange
device: Chase Bliss Big Time
date: 2026-06-19
description: "Factory #5 BROKEN DYNAFLANGE territory — a starved flanger whose sweep tracks your playing dynamics. MODE Mod (3–46 ms), STATE #!&% misbias (the 'starved' flanger character) with Saturated as the gentler alternative, MOTION Env so the flange fills the gaps between notes and reacts to loudness. COLOR kept low so soft playing stays clean and only digging in starves the flanger. Distinct from `mod-slap-comb-flange-double` (Compressed, MOTION Sine, clean slap) and from both existing Env patches (which live in Short/Long, not MOD). Control routing is first-party-sourced; the clock-face numbers are a dialable DOUG recipe."
tags: [mod, flange, dynaflange, misbias, envelope-follower, dynamics-reactive, starved, designed]
hidden:
  TEXTURE: "alt under COLOR — misbias sensitivity; how violently hard attacks starve the flanger"
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot (10 internal / 127 via MIDI); recall flies the faders to saved positions" }
  - { name: "MODE", type: switch, value: "Mod (3–46 ms — the flanger zone, NOT a delay; this IS the patch)", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "#!&% (misbias) — the 'starved' flanger character; flip to Saturated for a gentler, less broken sweep", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "Warm (vintage-rack tint that suits the broken sweep) or HiFi for a more defined flange", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off (bendy pitch modulation / flange sweep — not a quantized pitch voice)", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Env (envelope follower drives the flange sweep — it fills the gaps between your notes and reacts to loudness)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "LOW ~25% (load-bearing — soft playing stays clean; only digging in starves the flanger)" }
  - { name: "TIME", type: knob, value: "short–mid of the MOD range (sets the flange comb spacing/voice)" }
  - { name: "CLUSTER", type: knob, value: "low–moderate ~25% (thicken/widen the swept field)" }
  - { name: "TILT EQ", type: knob, value: "at/just above noon (keep the starved sweep out of the mud)" }
  - { name: "FEEDBACK", type: knob, value: "moderate ~40–55% (resonant enough to flange; not so high it runs away on a hard attack)" }
  - { name: "WET", type: knob, value: "~45% (dry retained so the dynamic flange reads against the dry note)" }
  - { name: "RATE", type: knob, value: "alt under TIME — moderate (sweep speed when the envelope releases)" }
  - { name: "DEPTH", type: knob, value: "alt under CLUSTER — moderate–high (how far the envelope sweeps the flanger)" }
  - { name: "TEXTURE", type: knob, value: "alt under COLOR — moderate (misbias sensitivity; how violently hard attacks starve/break the flanger)" }
  - { name: "SPREAD", type: switch, value: "widen (open the swept field across the stereo image)", options: ["off", "widen", "ping-pong"] }
  - { name: "MODE button (hold 2s)", type: button, value: "Panic reset → clean simple delay if the starved sweep runs away" }
---

# MOD Broken Dynaflange

## Concept
Factory **#5 BROKEN DYNAFLANGE** rebuilt as a performance: a starved flanger whose sweep is driven by your playing dynamics. **MODE Mod** puts Big Time in its flanger zone; **STATE #!&% (misbias)** supplies the starved, broken character (Saturated is the gentler alternative); **MOTION Env** points the envelope follower at the flange so it "fills the gaps between your notes… reacts to loudness." The load-bearing move is **COLOR LOW** — soft playing stays clean, and only digging in starves the flanger into its broken, dynamic oscillation. Distinct from `mod-slap-comb-flange-double` (which is MOD as a Compressed, MOTION-Sine clean slap → comb → flange double) and from both existing Env patches (`env-divebomb-lead`, `dynamics-crumble-long-echo`) which live in Short/Long, not MOD.

## How to play it
1. Set **MODE Mod**, **STATE #!&% (misbias)**, **MOTION Env**, **SCALE Off**.
2. Keep **COLOR LOW (~25%)** and **TEXTURE moderate** (alt under COLOR) — this is what keeps soft playing clean and only lets hard attacks starve the flanger.
3. Set **FEEDBACK moderate (~40–55%)** so it's resonant enough to flange but doesn't run away on a loud transient.
4. In the Alt menu: set **DEPTH moderate–high** (under CLUSTER — how far the envelope sweeps the flanger) and **RATE moderate** (under TIME — sweep speed on release).
5. Play softly and it stays clean; **dig in and the flanger starves/breaks**, then the sweep fills the gap between notes as the envelope releases.
6. If the broken sweep feels too tame, flip **STATE to #!&% misbias** (vs Saturated) for the more starved character, or push **TEXTURE**; if it runs away, drop **FEEDBACK** or **DEPTH** first.
7. Hold the **MODE button** (2 s) to panic-reset to a clean delay.

## Notes
- **STEP is non-functional in MOD mode** (verified): no footswitch sequence-stepping in MOD — TAP LEFT instead toggles MOTION on/off. Treat the footswitches as MOTION-toggle / bypass.
- **COLOR LOW is the patch.** It is what preserves the clean-when-gentle / breaks-when-you-dig-in response. Raising COLOR makes the flanger starve constantly and kills the dynamic move (same lesson as `dynamics-crumble-long-echo`).
- **#!&% misbias vs Saturated:** misbias = the broken/starved character (factory #5); Saturated = a gentler, less-broken dynamic sweep. Both are dynamics-reactive via MOTION Env; pick by how broken you want it.
- ⚠️ PROVISIONAL on envelope polarity: the manual fixes **no** attack-vs-release direction. It describes ENV functionally — as **transient-triggered step/sequence advancing**, with pitch/sweep direction set by **DEPTH above vs below TIME** (and by SCALE on/off) — and never states a fixed "harder = down / harder = up" polarity. So "dig in → dive-bomb / starve" is **one achievable DEPTH/SCALE-off character** (cf. Snyder's failing-PSU inspiration anecdote, which is flavor, not a firmware spec), **not a universal polarity.** The "fills the gaps between notes / breathing" behavior is the intended character, but the precise attack-vs-release feel is user-configurable and must be confirmed by ear on hardware.
- ⚠️ HONEST: only the control *routing* (MODE Mod, STATE misbias/Saturated, MOTION Env, low COLOR) is first-party-sourced. The specific clock-face positions (COLOR / TIME / CLUSTER / TILT / FEEDBACK / WET / RATE / DEPTH / TEXTURE) are a dialable DOUG recipe, not published Chase Bliss numerics. On recall the motorized faders fly to saved positions and override these starting points.

## Sources
- 🟣 DOUG-designed patch. Control routing is first-party-sourced; numeric fader positions are a dialable recipe (designed starting points), flagged as such — the motorized faders override on recall.
- `research/bloops/2026-06-19-chase-bliss-big-time.md` (Lens: patches — MOD-mode recipes): MODE Mod, STATE #!&% misbias (the "starved" flanger character) or Saturated, MOTION Env so the flange sweep tracks playing dynamics ("fills the gaps between your notes… react to loudness"); low COLOR so soft playing stays clean and only digging in starves the flanger; explicitly distinct from `mod-slap-comb-flange-double` (Compressed, Sine, clean slap) and from both existing Env patches (Short/Long, not MOD).
- Factory #5 BROKEN DYNAFLANGE ("a starved flanger… dynamic oscillations that react to your instrument's loudness"): `gear/Chase Bliss Big Time/research/links/cb-big-time-factory-presets-recipes.md`.
- STATE #!&% misbias behavior + Snyder misbias-as-instrument: `gear/Chase Bliss Big Time/research/transcripts/sonicstate-superbooth-john-snyder-eae-interview.md`.
- MOTION Env + TEXTURE (misbias sensitivity, alt under COLOR) mechanics: `Patches/Chase Bliss Big Time/dynamics-crumble-long-echo.md`, `Patches/Chase Bliss Big Time/crushed-analog.md`.
- STEP non-functional in MOD (TAP LEFT toggles MOTION instead): `research/bloops/2026-06-19-chase-bliss-big-time.md` (candidate index chunks).
- Env-polarity caveat (manual fixes no attack-vs-release direction; ENV is transient-triggered with direction set by DEPTH above/below TIME — "dig in = dive-bomb" is one achievable character, not a universal polarity; confirm by ear on hardware): `research/bloops/2026-06-19-chase-bliss-big-time-l2.md` (Flagged / uncertain; Suggested corpus edits).

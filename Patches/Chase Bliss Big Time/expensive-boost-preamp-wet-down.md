---
type: patch
title: Expensive-Boost Preamp (WET Down)
device: Chase Bliss Big Time
date: 2026-06-15
description: "Big Time used as nothing but a delay — WET pulled fully down turns it into a standalone stereo analog preamp (manual p.24), so the delay engine is silent and only the matched analog dry path passes. COLOR becomes the drive/saturation control, +12dB is the boost, STATE picks the saturation character. A warm, gently-driven, stereo-split 'expensive clean boost' that colors the tone BEFORE the part — a studio-saturator front end with zero time-based effect, built to feed a downstream ambient/granular box (here MOOD). Designed (DOUG); WET-down-preamp behavior is published/sourced, knob positions are a dialable recipe set by ear."
tags: [preamp, boost, wet-down, saturation, clean-boost, stereo, analog-preamp, no-delay, designed]
dips:
  DRY CLEAN: "OFF (Options) — dry MUST hit the preamp or the patch is defeated"
  DRY KILL: "OFF (Options) — there's no wet signal; DRY KILL would mute everything"
controls:
  - { name: "WET", type: knob, value: "fully down (= standalone stereo analog preamp; delay engine muted — manual p.24)" }
  - { name: "+12dB", type: switch, value: "ON (the boost — alt under STATE)", options: ["off", "on"] }
  - { name: "COLOR", type: knob, value: "to taste — this is now your DRIVE/saturation amount, NOT delay feedback; ~9:00 clean-warm, toward noon-and-up for audible grit (RECIPE — set by ear)" }
  - { name: "STATE", type: switch, value: "Saturated (soft-clip console warmth) [alt = Compressed = leveled/glued boost; #!&% misbias = preamp sags & grinds]", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "Warm or Analog (most preamp-like; Analog = EAE Sending V2 callback)", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "FEEDBACK", type: knob, value: "irrelevant / down (no wet path with WET=0)" }
  - { name: "DRY CLEAN", type: switch, value: "OFF in Options (dry MUST hit the preamp — ON would route dry around the preamp and defeat the patch)", options: ["off", "on"] }
  - { name: "DRY KILL", type: switch, value: "OFF in Options (no wet signal exists — ON would mute the only signal passing)", options: ["off", "on"] }
  - { name: "SPREAD", type: switch, value: "widen (alt under MOTION)", options: ["off", "widen", "ping-pong"] }
  - { name: "Input routing", type: switch, value: "IN-L only → auto MISO (mono-in / stereo-out): a mono instrument exits as a colored stereo pair", options: ["mono → IN-L (MISO)", "stereo in"] }
---

# Expensive-Boost Preamp (WET Down)

## Concept
Big Time used as nothing but a delay — WET pulled fully down turns it into a standalone stereo analog preamp (manual p.24), so the delay engine is silent and only the matched analog dry path passes. COLOR becomes the drive/saturation control (it sets how hot you hit the input preamp), +12dB is the boost, and STATE picks the saturation character. The result is a warm, gently-driven, stereo-split "expensive clean boost" that colors the tone BEFORE the part — a studio-saturator front end with zero time-based effect. Built to feed an ambient/granular box (here MOOD) a harmonically richer, already-saturated source than a clean DI.

## How to play it
1. Pull **WET** all the way down — Big Time is now a standalone stereo analog preamp (manual p.24); the delay is silent.
2. Turn **+12dB ON** (the boost) and set **STATE = Saturated** (or Compressed / misbias for other characters).
3. Set **VOICING** to **Warm or Analog** for the most preamp-like, EAE-Sending-style tone.
4. In the **Options** menu confirm **DRY CLEAN is OFF** (dry must hit the preamp) and **DRY KILL is OFF** (or you'll mute everything).
5. Dial **COLOR** by ear against your input: back off for clean-warm, push up until the note just starts to grit — this is your drive amount.
6. Patch **IN-L only** so **MISO** auto-engages and a mono instrument exits as a colored stereo pair; **SPREAD widen** for the spread.

## Notes
- The WET-fully-down = standalone stereo analog preamp behavior is **published** (manual p.24); the specific COLOR / +12dB / STATE knob values are a **dialable RECIPE, NOT a saved factory preset** — set by ear.
- **COLOR here is a DRIVE control, not delay feedback** — it sets how hot you hit the input preamp.
- There is no feedback path with WET=0, so this is a "safe" loud — but +12dB plus hot COLOR still spikes output (manual warns twice). Set level before printing to tape.
- **DRY CLEAN OFF is mandatory** — DRY CLEAN routes the dry around the preamp and would defeat the entire patch. **DRY KILL OFF is mandatory** — there is no wet signal, so DRY KILL would mute the patch.
- To go transparent, kill **+12dB** and roll **COLOR** back — the analog preamp stays in circuit, just clean.

## Sources
- 🟣 designed (DOUG) from `gear/Chase Bliss Big Time/research/Big-Time-DeepResearch.md` (manual p.24: "Pull WET all the way down to turn Big Time into a standalone stereo analog preamp"; analog dry-thru; DRY CLEAN = dry bypasses preamp; DRY KILL Options behavior).
- `gear/Chase Bliss Big Time/research/Big-Time-UsageGuide.md` §1 (COLOR = how hot you hit the input preamp + limiter; +12dB = "second most important button", built to add gain; STATE saturation characters; Warm/Analog = EAE Sending V2 voicing).
- `gear/Chase Bliss Big Time/research/transcripts/mark-johnston-secret-weapons-big-time-deep-dive.md` (WET pulled fully down + COLOR alone = "expensive boost"/preamp; DRY CLEAN removes COLOR from dry path; DRY KILL removes dry from output).
- manual `Big+Time_Manual_Chase+Bliss.pdf` p.24 (WET-down preamp), p.10 (loudness faders COLOR / FEEDBACK / WET).

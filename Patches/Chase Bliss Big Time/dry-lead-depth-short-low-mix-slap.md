---
type: patch
title: Dry-Lead Depth (Short, Low-Mix Slap)
device: Chase Bliss Big Time
date: 2026-06-15
description: "Purpose-built final stage for the Clean → MOOD → Big Time dry-lead-over-soaked-loop chain — a short, low-mix, low-feedback delay that adds dimension to ONLY the live dry lead, leaving MOOD's reverb-soaked micro-loop bed untouched so the dry-vs-soaked contrast survives. Digital (limiter off) keeps it clean and pitch-stable; clock-face numbers are a dialable recipe, not a sourced preset."
tags: [clean, short, low-mix, lead, depth, slapback, designed]
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot; or hold MODE for the live panic-reset (≈ Factory #0) and trim WET/FEEDBACK down" }
  - { name: "MODE", type: switch, value: "Short", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Digital (limiter off — clean, pitch-stable, no smear/sat of the lead)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "HiFi (keep the lead present and articulate)", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Off (or Sine very slow + shallow for the faintest tape drift)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "low ~20%" }
  - { name: "TIME", type: knob, value: "short slap-to-eighth (lands inside the lead's phrasing)" }
  - { name: "CLUSTER", type: knob, value: "0 (single clean repeats, no multi-tap)" }
  - { name: "TILT EQ", type: knob, value: "noon → slightly up (keep the lead above the bed)" }
  - { name: "FEEDBACK", type: knob, value: "low ~25% (one or two repeats, no build)" }
  - { name: "WET", type: knob, value: "low ~25–30% (depth, NOT a wash)" }
  - { name: "SPREAD", type: switch, value: "widen (subtle) if running stereo, else off", options: ["off", "widen", "ping-pong"] }
  - { name: "MODE button (hold)", type: button, value: "Panic reset → clean simple delay (≈ Factory #0); trim WET/FEEDBACK down after" }
---

# Dry-Lead Depth (Short, Low-Mix Slap)

## Concept
A short, low-mix, low-feedback delay whose only job is to add dimension to a live DRY lead floating over a fully-soaked bed (e.g. MOOD's micro-loop-only reverb loop). Limiter off (Digital) keeps it clean and pitch-stable so it never smears or saturates the lead; short TIME, low WET and near-zero FEEDBACK/CLUSTER mean it reads as 'depth on the dry transients,' not a second wash. Built specifically because no existing Big Time patch fills the 'Short + light + depth-only-on-the-lead' role — clean-stereo-delay is a utility reset (WET ~40%), let-down is a dense multi-tap jangle wall, and the lead/drone patches are Long. The whole discipline is restraint: if it starts washing, it has gone too far and will muddy the soaked bed it is supposed to sit in front of.

## How to play it
1. Set MODE Short, STATE Digital, VOICING HiFi, CLUSTER 0.
2. Start WET ~25–30% and FEEDBACK ~25% — you want one short repeat of depth, not a tail.
3. Tap TIME to a short slap or eighth that lands inside the phrasing of the lead.
4. Play your dry lead over the soaked bed; the delay should add dimension you only notice when you bypass it.
5. If the lead starts to wash or fight the bed, drop WET first — never push it up to compete.
6. Hold the **MODE button** to panic-reset to a clean simple delay if the patch ever drifts.

## Notes
- Purpose-built for the 'Clean → MOOD → Big Time' dry-lead-over-soaked-loop chain — Big Time deepens ONLY the dry live lead, never the MOOD reverb bed.
- Digital STATE = no limiter, so the lead stays clean and pitch-stable (won't smear like Compressed/misbias states).
- Short + low-WET + low-FEEDBACK + CLUSTER 0 is the non-negotiable recipe; a long/high-feedback setting here would smear the soaked loop into mud and erase the dry-vs-soaked contrast the chain exists to preserve.
- Numeric fader positions are designed starting points; on recall the flying faders override them.
- ⚠️ No published knob numbers exist — Chase Bliss publishes character, not numbers; all clock-face values are presented as a dialable recipe set by ear (honesty flag), not a sourced preset.

## Sources
- 🟣 designed (DOUG) for this chain from the Big Time gear profile (Short mode, Digital/limiter-off, stereo I/O) + the "Clean Stereo Delay" patch (Digital STATE = no limiter, low COLOR/CLUSTER for transparent stable repeats, hold-MODE panic reset) + `research/transcripts/mark-johnston-secret-weapons-big-time-deep-dive.md` (Digital = no limiter; hold-MODE = instant clean simple delay).
- Role contrast verified against existing Big Time patches: clean-stereo-delay (utility reset, WET ~40%), let-down-cascading-jangle-delay (dense multi-tap wall), ondes-martenot-lead-delay & oceanic-drone-bed (Long) — none fill the Short/light/lead-depth-only slot.
- Honesty flag: Chase Bliss publishes character not numbers; all clock-face values are dialable starting points, not a sourced preset.

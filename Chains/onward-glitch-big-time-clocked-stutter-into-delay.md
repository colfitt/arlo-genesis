---
type: chain
title: Onward Glitch → Big Time — Clocked Stutter-into-Delay
date: 2026-06-14
artists: [Radiohead]
instrument: banjo
gear:
  - Roland VG-800
  - Chase Bliss Clean
  - MXR M173 Classic 108 Fuzz
  - Chase Bliss Onward
  - Chase Bliss Big Time
  - Chase Bliss MOOD MkII
  - Hologram Chroma Console
  - Eventide H90
  - Elektron Digitakt 2
  - Novation 61SL MkIII
---

# Onward Glitch → Big Time — Clocked Stutter-into-Delay ⭐

A minimal two-box centerpiece where one glitch pedal supplies the *event* and Big Time supplies the *space* — angular stutters smeared into rhythmic multi-tap tails, all on one grid. Banjo plucks shatter into angular repeating fragments that the delay fans into a rhythmic, slightly-crushed cloud sitting over a frozen sub-octave pad.

🟣 DOUG-designed integration. No artist used this exact chain — the per-unit patch refs carry their own provenance, and the Taste-ref names the sound it chases.

## Signal path

Banjo (GK-5) → VG-800 → Clean (#1 Home Base) → MXR 108 (spitty fuzz, optional) → **CB Onward #17 Two-Personality Patch** (Board 2 placement / pre-Big-Time send) → **Big Time #1 Crushed Analog** (clocked) → MOOD → Chroma → H90 → tape.

## Per-unit

- **Onward #17 Two-Personality Patch** — a hands-free locked **FREEZE sub-drone** underneath + a live **PLAYBACK-error GLITCH** tracking your banjo on top. The glitch side is what Big Time multi-taps; the freeze side is the pad under it.
- **Big Time #1 Crushed Analog (Factory #7)** — but lock TIME to clock and lean on CLUSTER: MODE Short, STATE Compressed (keeps the stuttered taps articulate in a dense mix — borrow from #2 Lo-Fi Rhythmic Groove), CLUSTER ~⅓–½ (the multi-tap pattern echoing the glitches), 0.5X ON (12-bit crush), COLOR ~40%, FEEDBACK ~45%, WET ~40%, SPREAD ping-pong (the added taps fan L/R).

## Routing

**Clock them together** so glitch timing and delay subdivision lock to one grid — Onward syncs its GLITCH timing to MIDI clock; Big Time locks TIME via **CC54** subdivision (dotted-8th or 16th). Set Big Time SCALE Off/Chromatic so clock snaps delay to the quarter. Run the **DT2 (or 61SL) as clock master** driving both (DT2 #29 MIDI/Clock-Master template; 61SL #3 per-pedal CC template can also retrigger Onward's Glitch via **CC108** clock-quantized). Pick ONE master — never loop clock. Stereo from Onward into Big Time's stereo ins.

## Sound

Banjo plucks shatter into angular repeating fragments that the delay fans into a rhythmic, slightly-crushed cloud sitting over a frozen sub-octave pad.

**Taste-ref:** art-rock / studio-as-instrument (Radiohead "Ful Stop" glitch-rhythm; reverse/glitch delays as the hook).

## Play

Lock the Onward freeze sub-drone hands-free, then play banjo so the live glitch tracks it; **CC108 from the 61SL retriggers the Glitch in time** for punch-ins. Big Time's CLUSTER fader is the live "more/less taps" control.

## Sources

- **Basis:** designed integration; chains **Onward #17**, **Big Time #1 Crushed Analog** (+ #2's Compressed/CLUSTER clock-lock), **DT2 #29 / 61SL #3**. Glitch-before-delay logic + "clock them together" from the centerpiece source file §B [R/V] ("glitch supplies the event, Big Time the space"; Onward syncs GLITCH to MIDI clock, Big Time locks TIME via CC54).
- `Gear/Chase Bliss Big Time/research/links/centerpiece-minimal-chains-and-sampler-integration.md`
- `Research/Chains/centerpiece-live.md` (C2)
- `Research/Taste-Profile/taste-profile.md`

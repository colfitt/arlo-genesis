---
type: chain
title: "OP-1 → Big Time Bouncy Thermae Synth Pluck"
date: 2026-06-15
artists: []
instrument: "OP-1 Field synth pluck"
gear:
  - TE OP-1 Field
  - EHX Interface
  - Chase Bliss Clean
  - Chase Bliss Big Time
---

# OP-1 → Big Time Bouncy Thermae Synth Pluck

One key on the OP-1 explodes into a self-playing melodic sequence. A bare, dry synth pluck feeds the centerpiece delay running the Thermae cascade trick — SCALE on **Oct+4+5**, MOTION **Square**, STEP engaged — so each repeat jumps to a new octave/5th/4th and the whole ladder ping-pongs across the stereo field. The instrument is doing almost nothing; the Big Time is the arranger.

🟣 DOUG-designed integration. No artist played this exact chain — the per-unit patch refs carry their own provenance, and the Sound section names the taste it chases. The headline move is routing the proven banjo "bouncy Thermae" cascade onto a non-guitar source (OP-1 synth pluck) for instrument variety while keeping Big Time the spine.

## Signal path

**OP-1 Field** (synth pluck, FX off — **TE OP-1 — "Bare Synth Pluck (Thermae Fuel)"**) → 1/4" line out → **EHX Interface** (line/instrument front-end into the board) → **CB Clean — "DI Fattener — Hotter Into the Interface"** → **CB Big Time — "Bouncy Thermae Oct+4+5 Ping-Pong Pluck"** (IN-L only → auto-**MISO** mono→stereo; SCALE Oct+4+5, MOTION Square, STEP MODE on, SPREAD ping-pong) → stereo out → board/tape.

The OP-1 is purely the source — no internal delay/reverb on the voice, because the Big Time *is* the delay and any baked-in echo would smear the cascade. Clean sits between the interface and the Big Time as an evener/fattener so every pluck hits the delay at the same hot level (the STEP/MOTION cascade fires cleanest off consistent transients).

## Per-unit

- **TE OP-1 — "Bare Synth Pluck (Thermae Fuel)"** (new) — a dry, percussive synth pluck with a fast-ish decay and **FX OFF**. Engine to taste (Dr Wave or Digital for a clean pitched pluck; FM for a glassier bell-pluck), Octave **0 or +1**, short envelope so each note is a clean discrete event. The point is a bare, mono, transient-rich note with no onboard delay/reverb — pure fuel for the Big Time's pitch stepper. *Engine/octave are op1.fun-granularity; per-knob envelope values dial by ear — recipe, not a published patch.*
- **CB Clean — "DI Fattener — Hotter Into the Interface"** (reuse) — gentle compression (Dynamics modest, Sensitivity by the left LED) plus Wet up past noon for make-up gain into the next stage; Dry blended for body. Originally a guitar-into-DI trick, it does the same job here: levels and fattens the OP-1 pluck so it slams the Big Time evenly. Keep it subtle — even transients, not audible squash. *Dialable recipe — no published clock-face values; set by ear to the stated targets.*
- **CB Big Time — "Bouncy Thermae Oct+4+5 Ping-Pong Pluck"** (new) — MODE **Short**, STATE **Compressed** (holds the stepped repeats together without runaway, keeps the pitch artifacts clean), VOICING **HiFi** or **Focus**, **SCALE = Oct+4+5** (each repeat steps octave / +5th / +4th — the wider cascade vs. plain octaves), **MOTION = Square** (the Thermae pitch-jump shape), **STEP MODE = ON** (Options page — maps the LEFT footswitch to walk pitch through the scale), **SPREAD = ping-pong** (repeats alternate hard L↔R as they climb), COLOR ~40%, TILT EQ noon→up (keep the pluck transients defined so steps fire cleanly), FEEDBACK ~50–60% (cascade length — long enough to hear the ladder build), WET ~45%, TIME mid (step speed). *Knob values are a dialable recipe — Big Time presets fly the faders on recall, and these numerics are designed starting points interpreting factory-#4 "Bouncy Thermae" intent, not published settings.*

## Routing

Mono synth pluck the whole way to the Big Time IN-L; **IN-L only auto-engages MISO** (mono-in/stereo-out), so stereo begins at the Big Time and the ping-pong SPREAD has a real stereo field to throw repeats across. **Gain-staging is the game:** Clean evens and fattens so every pluck hits the delay at one consistent hot level — the STEP/MOTION cascade fires most musically off uniform transients, and an inconsistent OP-1 velocity would make some steps fire and others not. Keep STATE **Compressed** (not Saturated/misbias) so the Oct+4+5 transposition stays pitched and clean rather than smearing into noise; drive defeats the "musical ladder" goal. Set WET below the dry pluck at first — a cascade climbing in 5ths/octaves stacks a lot of energy fast. No clock strictly required (this is a gestural cascade, not a grid part), but FOLLOW the rig clock if you want the step speed to land on the bar.

Two load-bearing details:
- **SCALE Oct+4+5 vs. Octave:** Octave gives clean octave-only jumps; **Oct+4+5 adds the 4th and 5th** so the ladder is a richer, more chordal cascade — that's the chosen flavor here. (Oct+4+5 also maps to traditional tap subdivisions if you want it rhythmic.)
- **STEP MODE** turns the LEFT footswitch into a manual pitch-stepper through the SCALE — tap to walk the cascade up by hand for a composed run, or leave it self-stepping off MOTION for hands-free.

## Sound

A plucky synth note that detonates into a bouncing octave/5th/4th cascade panning across the stereo field — a self-playing melodic sequence from a single OP-1 key. Composed and glassy, not chaotic: the repeats *are* the melody, climbing a scale-quantized ladder while ping-pong throws each step to the opposite side. Taste-ref: CB Thermae lineage / factory-#4 "Bouncy Thermae" ("an upbeat echo sequencer reminiscent of an old friend") routed to a synth source — the "more mature Thermae" idea (Emily Hopkins, Big Time as instrument) played as a melodic gesture from one note.

## Play

Play *less* than you think — one bare OP-1 pluck, let go, listen. The Big Time's STEP/MOTION + Oct+4+5 SCALE does the density and the melody. For a composed run, tap the Big Time LEFT footswitch (STEP MODE) to walk the cascade up the scale by hand; for hands-free, leave it self-stepping off the Square MOTION. Space your plucks — let one ladder finish bouncing before launching the next so the ping-pong field stays legible. Press-and-hold MODE on the Big Time is the panic-reset back to a plain delay if a cascade runs away.

## Sources

- **Basis:** designed integration; chains **TE OP-1 — "Bare Synth Pluck (Thermae Fuel)"** (new) + **CB Clean — "DI Fattener — Hotter Into the Interface"** (reuse) + **CB Big Time — "Bouncy Thermae Oct+4+5 Ping-Pong Pluck"** (new). The cascade mechanic — *SCALE quantizes the pitch movement of MOTION (Square pitch-jumps stepped through Oct+4+5), STEP MODE walks pitch through the scale from the LEFT footswitch, and SPREAD ping-pong pans the repeats* — follows `Patches/Chase Bliss Big Time/bouncy-thermae.md` (factory #4 intent) and `Patches/Chase Bliss Big Time/banjo-thermae-cascade-lead.md` (SCALE/MOTION/STEP/MISO method), both sourced from `gear/Chase Bliss Big Time/research/transcripts/mark-johnston-secret-weapons-big-time-deep-dive.md` (MOTION/SCALE/STEP/SCALE-IGNORE) + `centerpiece-harp-lady-emily-hopkins-big-time-as-instrument.md` ("more mature Thermae").
- Clean role (level/fatten into the interface): `Patches/Chase Bliss Clean/di-fattener-hotter-into-interface.md`.
- OP-1 source (bare dry pluck, FX off): dialable recipe per `gear/TE OP-1 Field/research/OP-1-Field-DeepResearch.md` (engine voices) — no published per-knob values.
- Honesty: all Big Time / Clean / OP-1 numerics here are dialable recipes (interpreted from factory intent + engine descriptions), not published knob values.

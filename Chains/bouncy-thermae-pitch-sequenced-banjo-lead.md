---
type: chain
title: "\"Bouncy Thermae\" Pitch-Sequenced Banjo Lead (clock-locked)"
date: 2026-06-14
artists: [Radiohead]
instrument: banjo
gear:
  - Roland VG-800
  - Chase Bliss Clean
  - Chase Bliss Big Time
  - Hologram Chroma Console
  - Eventide H90
  - MXNHLT PORTA424
---

# "Bouncy Thermae" Pitch-Sequenced Banjo Lead (clock-locked)

A melodic hook where the *repeats are the melody* — single banjo notes stepped through a scale by the centerpiece, locked to the rig clock so it sits in a sequenced arrangement. ⭐ signature-fit.

This is a 🟣 designed integration of owned-gear patches; no artist ever played *this* chain. The Taste-ref names the sound it chases, and the per-unit patch sheets carry their own provenance.

## Signal path

EBM-5 banjo (GK-5) → **VG-800 (#3 GR-300 Thick-Synth Lead)** → Clean (#2 Transparent Enhancer) → [Board 2 thru] → **Big Time (#7 Bouncy Thermae, Factory #4)** → Chroma → **H90 (#25 PrismShift Self-Generating Stereo Arp Bed, Mix low)** → PORTA424 → tape. *(Big Time sits 2nd on Board 3; H90 is later on Board 3 — order preserved.)*

## Per-unit

- VG-800 **#3 GR-300 Thick-Synth Lead** — `PITCH A = +12` (or +7/+5), `COMP SW ON` extends the hexa-VCO decay (the banjo fast-decay fix), `ENV MOD` for pick-triggered wah. Recall GK **#1 EBM5 BANJO**.
- Clean **#2 Transparent Enhancer** — slow Attack keeps the pluck attack uncompressed so the GR-300 transient triggers the Thermae steps cleanly; the cleanest banjo-as-lead base.
- Big Time **#7 Bouncy Thermae (Factory #4)** — MODE Short, STATE Compressed, SCALE Octave (or Oct+4+5 = maps to tap subdivisions), MOTION Square; **SCALE IGNORE optional ON** for cleaner sine + scaled steps. Feed single notes; repeats arpeggiate into octave ladders.
- H90 **#25 PrismShift Self-Generating Stereo Arp Bed** — from factory "Sequential Chimes"; **Spread = FULL** so arps pan L↔R, slow Step Length for an ambient bed under the Big Time sequence; Mid voice stays live/playable. Mix low (the bed, not the lead).

## Routing

Mono banjo front; Big Time MISO to stereo. **DT2 (or 61SL) is clock master.** Big Time slaved: subdivision via CC54, p-lock COLOR/TIME via CC14–19 from the DT2 for grid-quantized moves (Big Time #2 method). H90 tempo-sync its delay components to the same MIDI clock. 61SL #5 (Big Time Centerpiece Performance Template) can ride TIME/WET live without diving into the pedal. Keep TILT EQ above noon — defined banjo transients are what the Thermae steps fire on.

## Sound

A self-arpeggiating banjo melody that climbs scale-quantized octave ladders in time, with a slow stereo PrismShift chime bed cascading underneath — a sequenced, glassy, banjo-driven hook.

Taste-ref: art-rock-studio-as-instrument (sequenced/stepped pitched delay; CB Thermae lineage) + the electronic-groove-first lean of letting a locked figure generate melody.

## Play

Play *less* than you think — sparse single plucks. The Big Time SCALE stepping and the H90 self-generating arp do the density. Use Big Time STEP MODE (tap LEFT) to manually walk the pitch for a composed run, or leave it on the clock for hands-free.

## Sources

- Basis: designed integration; chains VG-800 #3 + #1(GK) → Clean #2 → Big Time #7 → H90 #25. Clock-lock/CC54/p-lock-CC14–19 from Big Time sheet #2 + DT2 #29 (MIDI/Clock-Master template); 61SL #5 for live centerpiece control.
- `Research/Chains/banjo-baritone-leads.md` (C2)

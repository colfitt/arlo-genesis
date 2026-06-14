---
type: chain
title: Sampler Resample Loop — Big Time Texture → Samplers → Back Through Big Time
date: 2026-06-14
artists: [Car Seat Headrest, Radiohead]
instrument: drums/sampler
gear:
  - Chase Bliss Big Time
  - TE OP-1 Field
  - Elektron Digitakt 2
  - Akai MPC Sample
  - EHX Effects Interface
  - Eventide H90
---

# Sampler Resample Loop — Big Time Texture → Samplers → Back Through Big Time ⭐

The "recorded-wrong" generation-loss loop with Big Time at both ends: print a Big Time texture into a sampler, mangle it, then stream it back through Big Time so one delay is the song's glue — the OP-1-sketch → MPC-beat → Digitakt-sequence → all-through-Big-Time workflow. A frozen Big Time wall, sampled and crushed, played back as a chromatic/poly choir, then re-delayed by the same pedal — degradation stacked until it sounds captured on the wrong machine.

🟣 DOUG-designed integration. No artist used this exact chain — the per-unit patch refs carry their own provenance, and the Taste-ref names the sound it chases.

## Signal path

(capture) Big Time wet out → **OP-1 / DT2 / MPC sampler in**; (mangle in the box) → (return) sampler out → EHX Effects Interface (line→instrument, for the OP-1) → **Big Time** as a stereo aux/insert → CB stack → H90 → tape.

## Per-unit

- **Big Time #4 Oceanic Drone Bed (freeze-and-solo)** — build a wall, **hold RIGHT FS to FREEZE** a non-degrading infinite pad; *this frozen bed is the thing you sample.* MODE Long, STATE #!&%/Saturated, COLOR ~25–30%, FEEDBACK ~80%, DIFFUSE high. Keep WET conservative (it's loud).
- **OP-1 #21 Andreas Roman one-note polyphonic sampler** — sample the frozen Big Time bed as ONE note, then play it polyphonically across the keys (the "broken synth choir" engine). Re-print to Porta tape for stacked degrade. (~20 s cap; bounce-volume +8 to match.)
- **DT2 #17 Optoproductions Resample-the-Master Mangle Loop** — alt path: record Big Time's output (`INPUT = MAIN INPUT`) → Grid-slice → Comb → bit-crush → resample again. ⚠️ disable `TO MAIN` while resampling re-amped audio or it feeds back.
- **MPC #13 Resample to Bake FX** + **#14 Bake-the-Grit (SP1200)** — capture Big Time off the rear inputs → Chop→Transients → bake vintage-emulator/LoFi via Resample (⚠️ silent first try — do it twice). DJ-Shadow logic: a Big Time sample bank nobody else has.

## Routing

**OP-1 needs the EHX Effects Interface** (its line out goes farty/muddy straight into instrument-level gear) — route OP-1 → Effects Interface → Big Time. DT2/MPC put out healthy line level → feed straight in; set Big Time **COLOR low** for line sources (already hot) and use **DRY KILL** so Big Time returns wet-only into the aux path. On the return pass keep one clock master (whoever's driving the song).

## Sound

A frozen Big Time wall, sampled and crushed, played back as a chromatic/poly choir, then re-delayed by the same pedal — degradation stacked until it sounds captured on the wrong machine.

**Taste-ref:** lo-fi / prolific (Car Seat Headrest cassette-degrade) crossed with art-rock studio-as-instrument (the looped-and-layered build); banjo-as-lead can play the resampled choir.

## Play

FREEZE a Big Time bed → sample it on the OP-1/DT2/MPC → mangle → drop the sampler line back through Big Time. One delay, the whole song's glue.

## Sources

- **Basis:** designed integration; chains **Big Time #4 Oceanic Drone Bed**, **OP-1 #21**, **DT2 #17**, **MPC #13 + #14**. Resample-back-into-the-samplers paths (OP-1 line-matching via EHX Interface, DT2 `TO MAIN` feedback caveat, MPC silent-first-resample, DRY KILL wet-only return, "one delay the whole song's glue") all from the centerpiece source file §C [V] resampling + handoff sections.
- `Gear/Chase Bliss Big Time/research/links/centerpiece-minimal-chains-and-sampler-integration.md`
- `Research/Chains/centerpiece-live.md` (C5)
- `Research/Taste-Profile/taste-profile.md`

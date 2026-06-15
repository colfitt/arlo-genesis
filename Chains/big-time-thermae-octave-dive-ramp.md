---
type: chain
title: Big Time Thermae Octave-Dive Ramp
date: 2026-06-15
artists: []
instrument: synth / guitar-synth (Novation 61SL MkIII)
gear:
  - Novation 61SL MkIII
  - Chase Bliss Big Time
---

# Big Time Thermae Octave-Dive Ramp

Drag one fader and the whole delay transposes. This is the centerpiece used as a *playable pitch instrument*: a held synth note feeds the Big Time, SCALE is set to **Octave**, and dragging the TIME control sweeps the entire delay up and down in scale-quantized octave steps — musical ramps, no portamento mush. The trick that keeps it from going feral is **SCALE IGNORE**, which frees the MOTION matrix from the TIME clock so a clean sine LFO keeps wobbling underneath while TIME does nothing but transpose. Played hands-on from the 61SL's CC faders.

🟣 DOUG-designed integration. No artist played this exact chain — the per-unit patch refs carry their own provenance, and the Sound section names the taste it chases.

## Signal path

**61SL MkIII** (synth voice out → audio in to Big Time; SL DIN Out → Big Time MIDI IN) → **CB Big Time — "Thermae Octave-Dive Ramp"** (SCALE Octave, SCALE IGNORE ON, MOTION Sine, TIME swept live via 61SL CC15) → stereo out → tape/board.

The 61SL is both the instrument *and* the controller: its synth/soft-synth voice is the source feeding Big Time's input, and its DIN out plus encoder/fader CCs drive the pedal hands-free per **Novation 61SL — "Big Time Centerpiece Performance Template"**.

## Per-unit

- **CB Big Time — "Thermae Octave-Dive Ramp"** (new) — MODE **Short** (or Long for a slower wash), STATE **Digital** or **Compressed** (keep the pitch artifacts clean — no Saturated/misbias chaos here), VOICING **HiFi**, **SCALE = Octave** (octave jumps only), **MOTION = Sine** (the smooth wobble underneath), **SCALE IGNORE = ON** (Options/"E" page — frees the sine from the TIME clock), TILT EQ ~noon, COLOR low-mid, FEEDBACK ~45–55% (so each transposed tail rings long enough to hear the step). The whole move lives in the **TIME** fader: with SCALE = Octave, dragging TIME re-pitches the entire delay in clean octave steps. *Knob values are a dialable recipe — Big Time presets fly the faders on recall, and these numerics are designed starting points, not published settings.*
- **Novation 61SL — "Big Time Centerpiece Performance Template"** — **enc1 = CC15 TIME** is the star here (this is the transposition fader); enc2 = CC19 WET, enc3 = CC14 COLOR; **Fader Pickup ON** so jumps don't snap. Big Time set to **FOLLOW** (CC111 = 0) if you want the sine wobble loosely clock-aware, or leave it free-running — this is a gestural ramp, not a rhythmic part, so a clock isn't required.

## Routing

Mono synth voice into Big Time IN; Big Time outputs stereo (SPREAD widen for a little width on the transposed tails). **Gain-staging:** keep COLOR low-mid and STATE Digital/Compressed so the octave transposition stays clean and pitched — drive (Saturated/misbias) smears the steps into noise, which defeats the "musical ramp" goal. Set WET below dry at first; a fully transposed delay an octave down is a *lot* of low-end energy, so dial WET against the synth body rather than burying it.

Two CC subtleties worth knowing:
- **SCALE dependency on the clock:** with SCALE on OFF/CHROMATIC the delay snaps to the quarter; on **OCTAVE/Oct+4+5 the subdivision tracks musically** (per the centerpiece template's verified note). Octave is exactly what we want.
- **SCALE IGNORE is the load-bearing option** — without it, dragging TIME also drags the modulation rate (because TIME is the modulation clock) and the sine speeds up/slows down as you transpose. With SCALE IGNORE ON, the sine stays put and TIME becomes a pure pitch fader. That separation is the whole patch.

## Sound

Smooth, scale-quantized octave ramps — drag the fader and the echo glides the whole delay up or down in clean octave leaps while a slow sine keeps the tails breathing underneath. Composed, not chaotic: the stereo-Thermae character (pitched, ambient) without the square-wave arpeggiation. Taste-ref: CB Thermae lineage / "more mature Thermae" (Emily Hopkins, Big Time as instrument) — pitched delay played as a melodic gesture rather than a per-note cascade.

## Play

Hold or sustain one synth note (long envelope/legato suits this). With the right hand free, **ride 61SL enc1 (CC15 TIME)**: push it up for an octave-rising ramp, pull it down for the dive. Because SCALE = Octave, you can't land off-key — the steps are quantized. For a recallable home base, tap the Big Time LEFT footswitch once: it snaps TIME to the center of the fader throw so you can bend an octave up/down *around* that pivot and return cleanly (the documented "useful with SCALE = octaves" hack). Leave the sine slow and low under it all. Press-and-hold MODE is the panic-reset back to a plain delay if a ramp runs away.

## Sources

- **Basis:** designed integration; chains **CB Big Time — "Thermae Octave-Dive Ramp"** (new) + **Novation 61SL — "Big Time Centerpiece Performance Template"**. Core mechanic — *SCALE quantizes the pitch movement of both TIME and MOTION* (so dragging TIME transposes the delay in octave steps) and *SCALE IGNORE lets the MOTION matrix ignore TIME (smooth sine while TIME transposes)* — verified in `gear/Chase Bliss Big Time/research/transcripts/mark-johnston-secret-weapons-big-time-deep-dive.md` (MOTION/SCALE §; SCALE IGNORE in the OPTIONS/"E" page §; the LEFT-tap "snaps TIME to center… useful with SCALE = octaves" hack).
- CC15 = TIME, Fader Pickup, CC111 follow, SCALE-on-OCTAVE subdivision tracking: verified Big Time CC map in `Patches/Novation 61SL MkIII/big-time-centerpiece-performance-template.md`.
- Taste-ref ("more mature Thermae"): `gear/Chase Bliss Big Time/research/transcripts/centerpiece-harp-lady-emily-hopkins-big-time-as-instrument.md`.

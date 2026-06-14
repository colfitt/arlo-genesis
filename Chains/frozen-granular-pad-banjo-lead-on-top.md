---
type: chain
title: Frozen Granular Pad, Banjo Lead On Top
date: 2026-06-14
artists: [Yvette Young, Bon Iver, Sufjan Stevens]
instrument: banjo
gear:
  - Roland VG-800
  - Chase Bliss Clean
  - Walrus Audio QI Etherealizer
  - OBNE Dark Star V3
  - Chase Bliss Big Time
  - Hologram Chroma Console
  - Eventide H90
  - MXNHLT PORTA424
---

# Frozen Granular Pad, Banjo Lead On Top

The Yvette-Young workflow translated to banjo-as-lead — capture a chord into a frozen granular pad on Board 2, then play a banjo lead over the self-sustaining bed. The cleanest "lead over a held wall" chain. ⭐ signature-fit.

This is a 🟣 designed integration of owned-gear patches; no artist ever played *this* chain. The Taste-ref names the sound it chases, and the per-unit patch sheets carry their own provenance.

## Signal path

EBM-5 banjo (GK-5) → **VG-800 (#6 CRYSTAL Shimmer Pad** for the bed *or* **#4 SOLO Lead** for the live lead — see Play) → Clean (#12 Dynamic Volume Swell) → [Board 1 → Board 2] → **QI Etherealizer (#4 Frozen Banjo/Baritone Pad → Dark Star)** → **Dark Star V3 (#24 Frozen banjo bed)** → [Board 3] → **Big Time (#4 Oceanic Drone Bed, WET low)** → Chroma → **H90 (#28 PrismShift/Polyphony Freeze Pad)** → PORTA424 → tape.

## Per-unit

- VG-800 **#6 CRYSTAL Shimmer Pad** — `SUSTAIN 90–100` glassy bell drone as the bed source; `NORMAL MIX OFF` (let the model own it). Switch to **#4 SOLO Lead** (or just dry banjo through a less-saturated model) for the line you play *over* the freeze.
- Clean **#12 Dynamic Volume Swell** — AUX swell (LATCH for toggle); Wet = Swell In ~noon, Dry = Swell Out ~noon. The banjo pluck *bows in* like a bowed note, feeding the granular pad pre-swelled material.
- QI **#4 Frozen Banjo/Baritone Pad** — Grain Cloud, short-press **Freeze** to loop the grain buffer; **Space modest (10–11:00)** so the Dark Star owns the space; **Tone LPF** to tame the banjo 2–4 kHz spike. ⚠️ RIG-CRITICAL: pad/reamp the VG-800 line level before the Qi (no level switch — it clips hot; use the bench EHX Effects Interface).
- Dark Star V3 **#24 Frozen banjo bed** — Mix mostly wet, **Aux = Hold**, short Lag so the fast banjo transient speaks before the wash blooms; LPF side if octave content ice-picks. Stereo, trails on (Board-2 terminus, #28 global config).
- Big Time **#4 Oceanic Drone Bed** — MODE Long, low COLOR / high FEEDBACK climb, **WET set low** (the manual warns twice about runaway); this thickens the held bed, doesn't front it.
- H90 **#28 PrismShift/Polyphony Freeze Pad** — freeze the bed; the **PrismShift Mid voice stays live/playable** so the lead still rings through the frozen pitched pad.

## Routing

Mono banjo (Board 1) → stereo from CE-2W onward into Board 2; QI runs **Parallel** by default. ⚠️ **Dark Star Aux=Hold passes new notes BONE-DRY** — that is *good* here: the dry banjo lead sits in front of the frozen wash. Lean on the dry path + the H90/Chroma for the lead's own ambience. No clock needed (this is a held/ambient chain) — but the 61SL #4 (Whole-CB-Board Scene Recall) can recall the whole Board-3 state for the song part in one PC.

## Sound

A static, glassy, granular cathedral bed that never decays, with a clear bowed-in banjo melody floating on top — the lead present and dry-forward, the wall infinite behind it.

Taste-ref: indie-folk-confessional (the freeze-pad-and-jam, halo-around-one-voice intimacy) + post-punk-texture-dynamics (the sustained wall). Approximation: the QI grain cloud is a *fixed* pitched cloud, not a played MIDI harmony — it chases the result, not the Prismizer method.

## Play

Strum/roll one banjo chord → Clean swells it in → short-press QI **Freeze** to capture the grain pad → engage Dark Star **Aux Hold** to lock the wash → switch the VG-800 to the lead voice and solo over the frozen bed. To release, tap Freeze/Hold off; trails keep the wash ringing.

## Sources

- Basis: designed integration; chains VG-800 #6/#4 → Clean #12 → QI #4 → Dark Star #24 (+#28 global) → Big Time #4 → H90 #28. Freeze-then-solo workflow from QI #19 (Yvette) + Dark Star #13/#24 Aux-Hold; the bone-dry-Hold caveat is from the Dark Star sheet #13.
- `Research/Chains/banjo-baritone-leads.md` (C3)

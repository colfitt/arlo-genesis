---
type: chain
title: Banjo Thermae Cascade Over a Tape-Aged Bed
date: 2026-06-14
artists: [Radiohead]
instrument: banjo
gear:
  - Roland VG-800
  - Chase Bliss Clean
  - Chase Bliss Generation Loss
  - Chase Bliss Big Time
  - Chase Bliss Blooper
  - Hologram Chroma Console
  - Eventide H90
  - MXNHLT PORTA424
---

# Banjo Thermae Cascade Over a Tape-Aged Bed

The signature banjo-as-lead move — feed single banjo plucks and let the centerpiece arpeggiate them into clean octave ladders, sitting over a self-aging loop bed. One player, one melodic hook, a whole wall behind it. ⭐ signature-fit.

This is a 🟣 designed integration of owned-gear patches; no artist ever played *this* chain. The Taste-ref names the sound it chases, and the per-unit patch sheets carry their own provenance.

## Signal path

EBM-5 banjo (GK-5) → **VG-800 (#4 SOLO Lead Synth)** → Clean (#5 Banjo Transient Tamer) → [Board 2 thru] → **Generation Loss (#1 Subtle Tape Age)** → **Big Time (#8 Banjo Thermae Cascade Lead)** → **Blooper (#5 Banjo layer-builder)** → Chroma (re-stereo) → **H90 (#1 Cavernous Blackhole Drone, Mix back)** → PORTA424 → tape.

## Per-unit

- VG-800 **#4 SOLO Lead Synth** — long `SUSTAIN 80–100` defeats the banjo's fast decay so each pluck rings long enough to feed the cascade; recall GK profile **#1 EBM5 BANJO** first, 5th string excluded.
- Clean **#5 Banjo Transient Tamer** — slow Attack (~1:00) lets the pluck spike through then clamps; Envelope Balance high (tracks the bright register). Re-LED Sensitivity for the GK banjo.
- Gen Loss **#1 Subtle Tape Age** — Model 4 (Portamax-RT), Wow ~10:00, the "nice and wistful" patina so the cascade arrives already tape-warm. Hidden Input Gain = Line.
- Big Time **#8 Banjo Thermae Cascade Lead** — MODE Short, STATE Digital/Compressed (keep pitch clean), SCALE Octave, MOTION Square, **SCALE IGNORE ON** (musical ramps, no feral chaos), FEEDBACK ~45–55%.
- Blooper **#5 Banjo layer-builder** — capture one banjo phrase, overdub a Stepped-Speed (B4) octave-down layer for sub-thickness, then solo fresh banjo over the self-running bed.
- H90 **#1 Cavernous Blackhole Drone** — pull Blackhole Mix *back* so the wall sits behind the line; HotSwitch 1 → Feedback-to-Freeze if you want to lock the tail.

## Routing

Mono banjo → VG-800 → Clean (mono, Board 1). Big Time auto-engages **MISO** (mono-in/stereo-out) off IN-L; Blooper is **mono in/out** (degrade here, let **Chroma re-expand to stereo** before the H90). Clock: run DT2/MPC as master and slave Big Time via **CC54** (subdivision) so the cascade steps land on the grid; Blooper armed to the same clock (Blooper #27, CV CLOCK or MIDIBox). Keep Big Time **COLOR modest** — the source is already tape-degraded (Gen Loss upstream), over-saturating a pre-degraded source sounds awful.

## Sound

A bright banjo line that blooms into stepped octave cascades, each repeat tape-warmed, riding a slowly-aging sub-octave loop — melodic and clear up top, deep and worn underneath.

Taste-ref: art-rock-studio-as-instrument — the "Let Down" cascading-arpeggio-as-wall idea (Radiohead), rebuilt on the banjo voice rather than doubled Telecasters.

## Play

Pick sparse single notes — let the Big Time cascade do the arpeggio work. Print the Blooper bed once (one-shot overdub for the octave-down layer), drop to playback, then play the live lead on top. Optionally tap LEFT on Big Time in STEP MODE to walk the pitch up by hand.

## Sources

- Basis: designed integration; chains VG-800 #4 + #1(GK) → Clean #5 → Gen Loss #1 → Big Time #8 → Blooper #5 → H90 #1. Cascade-over-wall concept mirrors the art-rock cluster index "Let Down wall (one player)" recipe (`Research/Taste-Profile/art-rock.md` § Chain recipes). Big Time COLOR-modest-after-Gen-Loss gain-staging from Big Time sheet Rig placement note.
- `Research/Chains/banjo-baritone-leads.md` (C1)

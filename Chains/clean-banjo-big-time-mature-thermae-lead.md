---
type: chain
title: "Clean → Big Time Mature Thermae Banjo Lead"
date: 2026-06-15
artists: [Chase Bliss, Emily Hopkins]
instrument: banjo (GK-5) / guitar-synth pluck
gear:
  - Roland VG-800
  - Chase Bliss Clean
  - Chase Bliss Big Time
---

# Clean → Big Time Mature Thermae Banjo Lead

A melodic sequencer you play one note at a time. Single plucked banjo notes cascade into arpeggiated octave / 4th / 5th ladders that ping-pong across the stereo field, with a clean sine wobble breathing underneath. You don't play phrases — you play *seeds*, and the Big Time's repeats do the melodic work. This is the Thermae-successor trick: Big Time is the "more mature Thermae," and the whole rig exists to feed it clean, even, evenly-tracked single notes.

This is a 🟣 designed integration of owned-gear patches; no artist played *this* chain. The Taste-ref names the sound it chases, and the per-unit patch sheets carry their own provenance.

## Signal path

EBM-5 banjo (GK-5) → **VG-800 — "Sufjan Fingerpicked Banjo Lead"** (recall **VG-800 — "GK SETTING — EBM5 BANJO"** first) → **CB Clean — "Banjo Transient Tamer"** (even the attacks) → **CB Big Time — "Mature Thermae Oct+4+5 Ladder Lead"** (Short/Mod · SCALE Oct+4+5 · MOTION Square + STEP · SCALE IGNORE · SPREAD ping-pong) → stereo out → board.

## Per-unit

- VG-800 **"Sufjan Fingerpicked Banjo Lead"** — banjo played as a clean 4-string guitar (5th string excluded; `NORMAL MIX ~20–40%` keeps the real pluck/finger noise). Dirt OFF, onboard REV/DLY off. We want *bright, discrete, clean plucks* — not a sustained synth pad — because the Big Time's SCALE engine steps cleanest off a clearly-articulated transient. Recall **"GK SETTING — EBM5 BANJO"** first; it is the enabler nothing else tracks without.
- Clean **"Banjo Transient Tamer"** — the load-bearing unit. The GK banjo's attack is violent and decay near-zero; the SCALE steps will misfire on ragged transients. Slow Attack (~1:00) lets each pluck spike escape, then limiting clamps and the slow Release (R, 1.5 s) extends decay so each seed note rings long enough to feed a full ladder. Hidden Envelope Balance high so the comp tracks the bright register and ignores phantom lows. **Re-LED Sensitivity for the GK banjo** — it will not match guitar settings.
- Big Time **"Mature Thermae Oct+4+5 Ladder Lead"** — MODE **Short** (or **Mod** for tighter ramps), STATE **Digital/Compressed** (keep the pitch artifacts clean), SCALE **Oct+4+5** (octave + perfect 4th + 5th ladders), MOTION **Square + STEP**, **SCALE IGNORE ON** (smooth sine modulation under the scaled transposition — the clean wobble, none of the feral chaos), SPREAD **ping-pong** (ladders bounce L↔R across the field), FEEDBACK ~50–60% (ladder length), CLUSTER low-mid (let the core ladder read), TILT EQ noon → up (keep the bright banjo transients defined so the steps fire). Values are a **dialable recipe** (see patch — the Big Time has motorized flying faders; numerics are designed starting points, not published settings).

## Routing

Mono front (banjo → VG-800 → Clean, Board 1). Big Time auto-engages **MISO** (mono-in/stereo-out) off IN-L, so the ping-pong ladders open up to stereo from the Big Time onward — no need to run a stereo source. **Gain-staging is the whole game and it runs in this order for a reason:** the VG-800 gives a clean discrete pluck → Clean *evens* it (slow-attack limiting + extended decay) so every seed note arrives at the same level with the same envelope → the Big Time's SCALE steps then track cleanly off a predictable transient. Skip the Clean and the ladders stutter and drop notes on hard picks. Keep TILT EQ above noon — defined transients are what the SCALE engine listens for. No clock strictly required (STEP is hand-played), but slave Big Time via CC54 if you want the ladders to land on a grid.

## Sound

A glassy, self-arpeggiating banjo lead: each plucked note blooms into an octave/4th/5th ladder that walks up and ping-pongs across the stereo field, a slow clean sine wobble breathing underneath the whole thing. Melodic and clear — you hear a sequencer, but it's one player feeding it one note at a time.

Taste-ref: the CB Thermae lineage as "more mature Thermae" (Emily Hopkins / harp-as-instrument, rebuilt on the banjo voice) + the art-rock "Let Down" cascading-arpeggio-as-melody idea, sequenced rather than strummed.

## Play

Play *far* less than you think — sparse single plucks, let each ring. The cascade does the arpeggio. The defining performance move is **STEP MODE**: tap the Big Time LEFT footswitch to walk the pitch up through the SCALE by hand — that's how you "play the melody" through the repeats, one composed step at a time, rather than just letting it free-run. Leave SCALE IGNORE on so the sine wobble stays musical under your steps. For a hands-free version, drop STEP and let MOTION Square free-run the ladders on the clock.

## Sources

- Basis: designed integration; chains VG-800 "Sufjan Fingerpicked Banjo Lead" + "GK SETTING — EBM5 BANJO" → Clean "Banjo Transient Tamer" → Big Time "Mature Thermae Oct+4+5 Ladder Lead". "More mature Thermae" framing + SCALE/MOTION/STEP/SCALE IGNORE behavior from `research/transcripts/mark-johnston-secret-weapons-big-time-deep-dive.md` + `centerpiece-harp-lady-emily-hopkins-big-time-as-instrument.md`. Banjo transients = ideal SCALE/MOTION fuel per DeepResearch §6; Clean transient-evening (slow attack → escape → clamp, extend decay) from the Clean "Banjo Transient Tamer" sheet.
- Big Time knob values are a dialable recipe (unpublished; motorized flying faders override on recall), not sourced manufacturer settings.
- `Research/Chains/banjo-baritone-leads.md` (designed)

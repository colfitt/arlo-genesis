---
type: chain
title: Big Time Banjo Step Arpeggiator
date: 2026-06-15
artists: [Radiohead]
instrument: banjo (GK-5 → VG-800)
gear:
  - Roland VG-800
  - Chase Bliss Clean
  - Chase Bliss Big Time
---

# Big Time Banjo Step Arpeggiator

The played version of the Thermae cascade. Where the auto-cascade lead (see `banjo-thermae-cascade-over-a-tape-aged-bed.md`) lets the repeats arpeggiate themselves, this one hands the sequencer to your foot: with Big Time in **STEP mode**, the LEFT footswitch becomes a step button. Each tap walks the whole cascade one rung up a quantized Oct+4+5 ladder, so single banjo plucks turn into a *performed* arpeggio sequence — you decide when the pitch climbs. 🟣 designed integration of owned-gear patches; no artist ever played this exact chain. The Taste-ref names the sound it chases.

## Signal path

EBM-5 banjo (GK-5) → **VG-800 — "SOLO Lead Synth (sustained banjo line)"** (recall GK profile **VG-800 — "GK SETTING — EBM5 BANJO"** first) → **CB Clean — "Banjo Transient Tamer"** → [Board 2 thru] → **CB Big Time — "Step Arpeggiator (tap LEFT to walk the scale)"** (IN-L auto-**MISO**, mono→stereo) → stereo out.

## Per-unit

- **VG-800 — "GK SETTING — EBM5 BANJO":** recall this GK calibration slot first — it is the banjo-as-lead enabler nothing else works without. 4 main strings track for the lead; 5th string muted or `STRING LEVEL 5 = 0`, real 5th drone kept via `NORMAL MIX ~20–40%`.
- **VG-800 — "SOLO Lead Synth (sustained banjo line)":** `SYNTH TYPE = SOLO`, `SUSTAIN 80–100` — the banjo-decay fix. Each pluck has to ring long enough to survive one or two foot-taps without dying before the step lands, so push SUSTAIN higher here than you would for the auto-cascade. `TOUCH SENS ~50` keeps the pick attack alive — that transient is what the next stage and the stepper read.
- **CB Clean — "Banjo Transient Tamer":** slow Attack (~1:00) lets the pluck spike escape, then limiting clamps and the slow Release (R, 1.5 s) extends decay into guitar-like sustain. Hidden Envelope Balance high so the comp tracks the bright register and ignores phantom lows. Re-LED Sensitivity for the GK banjo — it will not match guitar settings. The point: a clean, defined attack on every note so the Big Time has a clear transient to step from.
- **CB Big Time — "Step Arpeggiator (tap LEFT to walk the scale)":** MODE **Short**, STATE **Compressed** (keeps stepped repeats articulate, no runaway), VOICING **HiFi/Focus** (clean pitch), SCALE **Oct+4+5**, MOTION **Square**, **STEP MODE ON** (Options). FEEDBACK ~45–55% sets how long each rung sustains before you tap the next; TILT EQ at noon → up keeps the bright banjo transients defined. **Tap LEFT** to advance one step up the Oct+4+5 ladder; the cascade transposes on each tap. This is the dialable recipe — Big Time fader/knob numerics here are designed starting points (flying faders override on recall), not published artist values.

## Routing

Mono banjo front (VG-800 → Clean, Board 1). Big Time IN-L auto-engages **MISO** (mono-in/stereo-out); stereo from Big Time onward. **No clock needed** — this is a performed sequence, not a grid-locked one, so the LEFT footswitch drives the steps by hand instead of CC54 subdivision off the DT2. (If you *do* want it grid-quantized and hands-free, that is the sibling `bouncy-thermae-pitch-sequenced-banjo-lead.md` — slave to clock and let the cascade auto-step. The whole distinction of this chain is keeping the step on your foot.) **Gain-staging:** Clean limits and slow-attacks so each note presents the Big Time a single clean transient; keep Big Time COLOR modest (~40%) so the source stays clear and the stepped pitches read cleanly rather than smearing into mud. The high VG-800 SUSTAIN is the load-bearing setting — too short and the note dies before the next step, breaking the arpeggio.

## Sound

A performed, played arpeggio: single banjo plucks that you walk up a quantized octave/4th/5th ladder by tapping your foot in time with the part. Glassy and articulate up top, climbing on cue — a hand-driven cousin of the self-running Thermae cascade, with the phrasing and rhythm decided live instead of by a clock.

Taste-ref: art-rock-studio-as-instrument — the "Let Down" stepped/cascading-pitch-as-melody idea (Radiohead / CB Thermae lineage), but performed step-by-step on the footswitch rather than auto-generated.

## Play

Play *less* than you think — sparse single plucks, let each ring. Tap the LEFT footswitch to walk the pitch up the Oct+4+5 ladder: one tap per intended pitch jump, in time with the phrase, so the climb is composed rather than random. Let FEEDBACK carry the previous rung underneath while you step to the next for a building stack. To reset to the bottom of the ladder, stop tapping and let the cascade settle (or recall the slot). For a hands-free auto-cascade version of the same voice, switch STEP MODE off and clock-lock it (see `bouncy-thermae-pitch-sequenced-banjo-lead.md`).

## Sources

- Basis: designed integration; chains VG-800 "GK SETTING — EBM5 BANJO" + "SOLO Lead Synth" → Clean "Banjo Transient Tamer" → Big Time "Step Arpeggiator". STEP MODE behavior (Options → STEP MODE ON → tap LEFT footswitch steps pitch through SCALE), SCALE Oct+4+5, MOTION Square, SCALE IGNORE, and MISO from `research/transcripts/mark-johnston-secret-weapons-big-time-deep-dive.md` + harp-lady transcript ("more mature Thermae"). Big Time numeric knob/fader values are designed dialable starting points, not published artist settings. Banjo-transient-as-step-fuel and high-SUSTAIN banjo-decay fix from the patch sheets' own provenance.
- 🟣 designed (DOUG); sibling of `banjo-thermae-cascade-over-a-tape-aged-bed.md` and `bouncy-thermae-pitch-sequenced-banjo-lead.md`.

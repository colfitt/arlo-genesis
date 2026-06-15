---
type: chain
title: "Hizumitas → Lost & Found Sympathetic Banjo Drone"
date: 2026-06-15
artists: [Boris, Stars of the Lid]
instrument: banjo (GK-5 → VG-800) / baritone
gear:
  - Roland VG-800
  - Chase Bliss Clean
  - EarthQuaker Devices Hizumitas
  - Chase Bliss Lost & Found
---

# Hizumitas → Lost & Found Sympathetic Banjo Drone

Banjo plinks become a sustaining, glassy vibraphone-pipe drone wall that resonates forever — a bowed-pipe tone from a self-selecting resonator. The trick is feeding the resonator a *long, pitched* note instead of a banjo's 1.5-second plink: the Hizumitas turns that decay into infinite fuzz-sustain so Lost & Found's Sympathetic Resonator has something to lock onto, and the resonator's pipes self-select pitch and forgive messy banjo input. This is an L&F-spotlight chain — no Big Time, no second wall. 🟣 DOUG-designed integration; no artist played this exact chain.

## Signal path

Banjo (GK-5 → VG-800, dark E.GUITAR model) → **CB Clean — "Banjo Transient Tamer"** (tames the GK-5 attack, slow release extends decay) → **EQD Hizumitas — "Banjo Infinite-Sustain Drone Feeder"** (1.5s plink → infinite pitched fuzz note, bass-side Tone) → **CB Lost & Found — "Banjo Bowed-Pipe Doom Drone"** (5B Sympathetic Resonator, MODIFY feedback MAXED = resonates forever; HOLD R footswitch = PITCH FREEZE; L<R into Useful Ambience halo) → out.

## Per-unit

- **CB Clean — "Banjo Transient Tamer":** the rig's banjo-as-lead conditioner. Sensitivity HIGHER (set by the left LED — GK-5 per-string output won't match guitar), Dynamics ~noon into limiting, Attack ~1:00 (the pluck spike escapes, *then* the limiter clamps), Release toggle RIGHT (Slow 1.5s) to extend decay, Wet ~1:00 / Dry ~10:00 light parallel for pick detail. Hidden Envelope Balance set high so the comp tracks the bright banjo register and ignores phantom lows. This is the clean stage — it makes the banjo behave like a sustaining guitar note *before* it hits the fuzz, which is what gives Hizumitas an even, predictable note to feed forward.
- **EQD Hizumitas — "Banjo Infinite-Sustain Drone Feeder":** the engine of the whole chain. **Volume hot · Sustain MAXED (CW) · Tone ~1:00–2:00 (bass-side CW, rolls off banjo's piercing 2–4 kHz via the 3n3 HPF cap).** Max Sustain converts the ~1.5s banjo decay into an effectively infinite, pitched fuzz tone; the bass-side Tone keeps it dark and droney (not a cutting lead) so the resonator locks a clean fundamental rather than a shrieking partial. The compression character keeps the long tail predictable, not runaway. ⚠️ Sustain-max + bass-side is a dialable recipe (DOUG's interpretation for this resonator-feeder role) — the only *published* Hizumitas sustain-max seed (Premier Guitar) sets Tone 8–10 for a *cutting* lead; here we deliberately go the other way (bass-side) for a drone.
- **CB Lost & Found — "Banjo Bowed-Pipe Doom Drone":** the spotlight. R slot = **5B Sympathetic Resonator**, **MODIFY (R feedback) MAXED (4:00–5:00) = resonates forever**, TIME (R onset) ~noon (onset is barely audible on shipping units — leave it). ROUTING **L<R** (Right feeds Left) into L slot **1B Useful Ambience** as an internal reverb halo (MODIFY L ~1:00, TIME L ~2:00 large). BLEND ~2:00 toward the halo, MIX/RAMP 2:00–3:00. TRAILS on (frozen pad survives bypass), LATCH on (the FREEZE hold latches). **HOLD the R footswitch = PITCH FREEZE** to lock the drone into a sustained wall, then sweep the hidden ALT octave (start −1) *during the ring* for expression.

## Routing

Four boxes, simple mono-or-stereo series, no clock (this is a drone, not a rhythmic grid). **The whole game is the hand-off from one sustain mechanism to the next:**

1. **Clean conditions, then Hizumitas sustains.** A raw GK-5 banjo plink is all-attack / no-sustain — feed that straight into the resonator and it gets a transient with nothing to lock onto. Clean's slow-attack / slow-release limiting turns the pluck into a guitar-like note, and Hizumitas at max Sustain then stretches it into an *infinite* pitched fuzz note. By the time the signal reaches L&F, it's a long, steady, dark drone tone — exactly what the Sympathetic Resonator wants.
2. **Hizumitas voiced dark on purpose.** Bass-side Tone matters because the resonator self-selects which pitch to ring; a bright, piercing fuzz makes it lock onto squealing upper partials. Rolling off the banjo's 2–4 kHz spike via the CW Tone sweep gives the resonator a clean fundamental to grab, so you get a glassy *vibraphone-pipe* tone instead of a shriek. The resonator forgives messy banjo input — but a dark, even input forgives it more.
3. **L&F is the only wall.** No Big Time, no Microcosm, no Dark Star downstream — the reverb halo is kept *internal* to the L&F (L<R into Useful Ambience) precisely so nothing double-stacks the resonator's ring. This is an L&F-spotlight chain by design. PITCH FREEZE (HOLD R) locks the wall; play fresh banjo over the frozen drone or let it hang.

If it gets shrill, pull the Hizumitas Tone further bass-side (CW) first, then nudge the L&F hidden EQ CCW — the shrillness lives in the fuzz feed, not the resonator.

## Sound

A banjo plink that blooms into a sustaining, glassy vibraphone pipe-drone that resonates forever — bowed-pipe tones from a self-selecting resonator, haloed by a soft internal reverb. Dark, glassy, and endless rather than aggressive. Taste-ref: Boris/Wata's Hizumitas sustain feeding a Stars of the Lid / drone-ambient pipe-organ bed — a banjo lead that dissolves into a church-organ wall.

## Play

Pick a single sustained banjo note or a slow chord and let Clean + Hizumitas stretch it into a long, dark, fuzzed tone. As it rings, the Sympathetic Resonator catches a pitch and starts to glow into a glassy pipe-drone. When you hear a pitch you like, **HOLD the L&F R footswitch to PITCH FREEZE** and lock the wall — then sweep the hidden ALT octave *during* the ring for movement, or play a fresh banjo line over the top of the frozen drone. Slow, sustained chordal input tracks cleanest; fast banjo rolls will artifact (on-aesthetic). For a longer build, swell in with the instrument volume so the fuzz attack never bites.

## Sources

- **Basis:** 🟣 designed integration; chains **CB Clean — "Banjo Transient Tamer"** (reused) + **EQD Hizumitas — "Banjo Infinite-Sustain Drone Feeder"** (created) + **CB Lost & Found — "Banjo Bowed-Pipe Doom Drone"** (reused). The hand-off logic — Clean conditions the GK-5 transient, Hizumitas converts 1.5s decay into infinite pitched sustain, L&F's Sympathetic Resonator self-selects and forgives messy banjo — is the rig's banjo-as-lead-into-drone signature move.
- Sympathetic Resonator mechanics (MODIFY feedback max = "resonates forever", PITCH FREEZE on R-footswitch HOLD, onset subtle, ALT octave only audible when swept during the ring) from `research/transcripts/bachelormachinestv-science-part2.md` + Knobs walkthrough ("12 pipes / forgiving note-gated drone source"). L<R into Useful Ambience halo from `research/Lost-and-Found-DeepResearch.md` §13(b).
- Hizumitas banjo voicing (bass-side Tone rolls off 2–4 kHz via the 3n3 HPF cap; compression evens banjo attack/decay) from `gear/.../Hizumitas-DeepResearch.md` §6 + UsageGuide §6. Sustain-max published seed (Tone 8–10 for a *cutting* lead) from the Premier Guitar review — this chain deliberately voices the opposite (bass-side) for a drone.
- Clean banjo conditioning (slow attack lets the pluck spike escape, slow release extends decay, Envelope Balance = "the banjo tool") from `research/Clean-DeepResearch.md` §6 + Clean manual Recipe 1 / Hidden Options pp.18–19.
- Note: the Hizumitas Sustain-max + bass-side Tone positions for the resonator-feeder role are a dialable recipe (DOUG's interpretation), not factory-published numbers; the L&F resonator/freeze knob positions are likewise a dialable recipe from the shipping map, not published presets.

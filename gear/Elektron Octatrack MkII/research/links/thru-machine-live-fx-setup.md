Manual: Octatrack MkII User Manual, §16.1.2 (p.97), §16.3 (p.99), §16.5/17.5 (p.111), §8.8 MIXER (p.42), Appendix A.1 (p.117)
Elektron manual + Elektronauts (octatrack-input-latency #160569)

# THRU MACHINE — OT as a live stereo FX processor on the pedalboard (the centerpiece)

## What a Thru machine is
A Thru machine is a **utility machine that listens to the physical inputs** (INAB / INCD) and routes that audio through the track's two FX blocks, the AMP/filter, and the three LFOs (Appendix A.1). It is NOT a sound — it's a "pass external audio through this track" machine. It **must be trigged** (one sample trig on the sequencer) before it passes any audio. Stop it with [TRACK] + [STOP].

## Two ways the OT hears the inputs — pick the Thru method
- **DIR method** (MIXER menu, DIR AB/CD = 127): routes inputs straight to the main outs as a basic mixer. **DIR audio is NOT affected by the two FX blocks** (only by a master-track effect if track 8 is a master). Costs no track. Use only for clean monitoring/passthrough.
- **THRU method** (DIR AB/CD = 0 + a Thru machine on a track): the input only exists *through* that track, so it gets the track's FX, filter, LFOs, scenes, mutes. **This is the goal** — it turns the OT into a live effects unit for the pedalboard. Costs one track per stereo input pair.

## Concrete setup — process the pedalboard's stereo print
1. **Patch:** pedalboard stereo print (Board 3 out: 424 / PORTA424 stage L/R) → OT **inputs A and B** (impedance-balanced TRS). Confirm the `<REC>` LEDs flicker with the signal. If LEDs are dark but you hear it, raise **AB GAIN** in MIXER (−64 mute … 0 unity … +63 = +12 dB).
2. **MIXER menu** ([MIX]): set **DIR AB = 0** (kills the dry passthrough so only the Thru track carries it). Leave **MAIN OUT** at 0 (unity).
3. **Track 1 = Thru machine** (double-tap [TRACK 1] → QUICK ASSIGN → Thru). In **SRC MAIN**, set **INAB = A B** (stereo, A hard-L / B hard-R). Set INCD = − (ignore C/D). VOL controls the input level into the track (max = +12 dB, min = mute).
4. **Place ONE sample trig** on step 1 of track 1. Without a trig the Thru machine passes nothing. Press [PLAY].
5. **FX1 / FX2** on the Thru track: this is where the wall gets mangled. For this rig:
   - FX1 = **multimode resonant filter** (sweepable cutoff — assign an LFO to it) or **Lo-Fi Collection** (bit/SR crush + distortion) to degrade the fuzz further.
   - FX2 = **Echo Freeze Delay** (tempo-synced; can freeze/sustain a fragment infinitely) or a **reverb** (Dark / Spring / Gatebox Plate) for the wash.
   - Comb filter / flanger / phaser are all on tap for metallic drone color.
6. **Assign an LFO** (one of 3 per track) to FX1 cutoff for a slow filter drift, or to the freeze-delay feedback. Slow triangle/sine = drone motion; fast = stutter/glitch.

## Latency reality
OT input→output latency is **~1.5 ms (64 samples)** per the Elektronauts input-latency thread — **not noticeable when playing an instrument through it**. Reported "OT latency" problems almost always trace to a DAW/soundcard buffer in a round-trip loop, not the OT itself. For a hardware-only signal path (pedalboard → OT → monitors/FOH), treat the OT as effectively real-time. (Contrast: round-tripping through Ableton-into-OT-and-back DOES add latency — don't do that for live processing.)

## Why the Thru track is better than DIR for this rig
- Mutable: mute track 1 to cut the whole wall instantly ([FUNC]+[TRACK 1]).
- Scene-able: the crossfader can morph FX params on the live wall (see rig-recipe-mangle-fuzz-wall.md).
- Sampleable: the same wall feeding the Thru track can be captured by the track recorder at any moment (see resample-the-rig-master-track.md).
- Chainable: feed the Thru track into Neighbor machines (tracks 2/3/4) for an up-to-8-FX serial rack (see int-ot-effects-processor-neighbor-chain.md).

## Gotcha
- If you ALSO want the dry wall in the mains alongside the processed Thru track, you'd set DIR AB up — but then you get the dry signal phasing against the (1.5 ms later) Thru track. For the live FOH case the manual's §16.3 trick is cleaner: keep DIR = 0 and only the processed audio returns.

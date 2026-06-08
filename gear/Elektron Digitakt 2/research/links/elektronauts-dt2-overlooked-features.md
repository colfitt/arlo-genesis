https://www.elektronauts.com/t/overlooked-new-features-of-digitakt-ii/213177
elektronauts.com · community thread (OP warpigs330) · started 2024

# Digitakt II — Overlooked New Features

Companion to the Tips & Tricks thread: features people miss, mostly DT2-only vs the OG Digitakt. Author attributions as surfaced.

## Mixer / dynamics
- **Pattern Volume** (warpigs330). A separate per-pattern volume control in the mixer/compressor section — useful for balancing loudness between patterns in a set. [Flagged: a commenter (Kraus) notes this also exists on the OG DT1, so NOT strictly DT2-only.]
- **Compressor routing + real sidechain** (warpigs330). You can choose *which tracks feed the master compressor* and *which tracks (or the input) are analyzed as the sidechain key*. This is genuine sidechain compression — e.g. duck a drone bed against a kick. [DT2-only: the OG had a far simpler master comp.] Access is via the SETUP/FX menu (community elsewhere cites FUNC+FLTR into the compressor setup).

## Modulation
- **Velocity in the mod matrix** (warpigs330). Route mod sources to velocity-style destinations — e.g. "envelope decay for velocity… for hi-hat variation." Adds humanization without p-locking every step.
- **Random LFO with Slew** (triandgle). The LFO has a RANDOM waveform plus a SLEW parameter — slow slew = smooth drifting randomness. This is THE drone/ambient modulation primitive (see the DROWNED drone-pack creator's note that all their drone motion is "slow LFOs on Filter/Pitch, or Random LFOs with slow Slews").
- **3 LFOs per audio track** (LyingDalai). DT2-only (OG had 1). Stack: LFO1 slow filter sweep, LFO2 slow pitch drift, LFO3 random→sample-slot for variation.
- **Portamento / Legato / Glissando** settings (Humanprogram) for expressive monophonic synth/lead lines.

## Trig conditions
- **LAST and NOT-LAST conditions** (Python). "Allows for easily programming drum fills when a new pattern is cued" — fires (or suppresses) a trig on the last pass before a pattern change, leaving the FILL condition free for other uses. Especially powerful with multi-page patterns.

## Sample management
- **Auto-preview + random name generator** (djadonis206). Samples auto-audition as you scroll; there's a random-name utility for quick captures.
- **Page Loop** (LyingDalai) — loop a single page of a pattern.

## FX / filters
- **Comb filter with key-tracking + filter envelope** (LyingDalai). The Comb filter key-tracks so it plays in tune alongside the sample, and its envelope shapes metallic transients. Said to behave better in the bass than the Octatrack's comb. On-aesthetic for detuned-resonator banjo/baritone textures.
- **Improved Bit Reduction (BR) and Sample Rate Reduction (SRR)** (LyingDalai) vs prior Elektron implementations.

## MIDI / routing
- **MIDI presets** (LyingDalai). Save complete MIDI-track configs as presets.
- **Selective USB audio output** (Python). Send only specific track(s) (a stereo pair or two mono) out over USB audio for external processing/resampling. Python's example: "resampling tracks through… guitar pedals" with an OP-1 Field in the chain. Directly relevant to this rig's re-amp/resample-through-the-board workflow.

NOTE: forum did not spell out every menu path; combos above are from this thread plus cross-referenced community posts. Sidechain/comp routing path quoted from the wider community as FUNC+FLTR in SETUP.

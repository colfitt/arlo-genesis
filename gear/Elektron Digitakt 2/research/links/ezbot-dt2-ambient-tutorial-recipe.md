https://www.youtube.com/watch?v=4xBD3wQRR3I
youtube.com · EZBOT (Matthew Piecora, Seattle hardware artist/educator) · 2025-03-05

# EZBOT — "Digitakt II Ambient Music Tutorial // Tips and Tricks"

~2-hour live build of a full ambient track from scratch on the DT2 using only factory sounds. The single best concrete-recipe source found. Full transcript: transcripts/ezbot-dt2-ambient-music-tutorial.md. DT2-specific throughout. Real values below.

## Setup
- FUNC → set **track scaling reset to INFINITY** (no auto-reset) so tracks run polymetric / never line up — the backbone of generative ambient. He warns that changing the project SCALE late can duplicate pages and lose you, so set scale FIRST.
- Set a **musical scale + keyboard fold ON** (two octaves on the trig keys). He lands on **harmonic minor**. Hold a trig + turn note → snaps to scale.

## Sound source: turn the DT2 into a wavetable synth
- Load a factory **wavetable** sample, SRC machine = **Grid**, set **GRID = 64** for fine "scan" resolution, LOOP on. The DT2 has no "scan" param, so you **move sample START with an LFO** (or velocity → LFO → start) to scan the wavetable. Shape AMP to a **pluck**.

## Generative sequencing
- Lay ~**7 trigs** (7-step seq against infinite scaling = constant phase drift). Set **track-level PROBABILITY low (~20%)** so notes fire sparsely and randomly — instant ambient. (Per-step probability p-locks also work.)
- **Duplicate the track** (hold track→COPY, paste preset to track 2; copy/paste the sequence), then **offset** track 2 by a step and move its notes up; pan track 1 slightly left, track 2 slightly right. Two detuned, offset copies = width + motion.

## LFOs (real values)
- LFO on track 1: **MULT = 1** (so it's NOT a tempo multiple → very slow), **SPEED = 16**, **shape = TRIANGLE**, **mode = FREE (free-running)**, **destination = Multi-mode filter frequency**. Opens the sound slowly.
- **Copy the LFO to track 2** (hold MOD→copy / paste) but **change its SPEED** so the two drift independently → more depth.
- Add **key tracking** so higher notes open the filter more.
- A small LFO on **BIT REDUCTION** adds moving "weirdness/grit."

## Send FX (real values, set in FUNC+FX page)
- **Delay:** PING-PONG ON, width up high (hard L/R), **delay send ~88**, feed a little into reverb, top filtered.
- **Reverb:** send **~90**, filtered in a "nice spot" by default. (Reverb has an INF/freeze available.)
- Tempo slow: he drops to **80 BPM**. "Ambient tunes are all about low-pass filters."
- TIP: hold FUNC + press an encoder to see exact numeric values in the secondary FX menus.

## Resample → tape-loop (Steve Reich phasing) workflow
- RECORDER: source = **MAIN OUTS** (captures the delay/reverb/bit-reduction you dialed). Use **PLAY-RECORD** (recording starts on PLAY = perfectly quantized from bar 1, unlike threshold recording which clips the transient — he calls this "as good at sampling as the Octatrack" for phrases). Record **4 bars**.
- Save as "loop1," place on a lower track (he uses **track 9** as a "resample track," keeps 1–8 as sound sources). Trig length = **4 bars = 64 steps**.
- **Repitch** the resample (SRC = Repitch) — "tasty every time"; try **reverse**; drop an octave for a swelling bed.
- **Steve Reich tape loops:** make **two copies** of the loop, both SRC = **Oneshot**, both **64 steps, LOOP on**, started together. Because the DT2 captures TRUE STEREO (L/R waveforms differ), and you offset one copy slightly, the two slowly **phase** against each other → classic generative shimmer.

## Degradation note (on-aesthetic for this rig)
- He frames **Sample Rate Reduction + Bit Reduction** as adding "jagged edges → more harmonics" = 8-bit crunch / sharper, "recorded-wrong" sounds. Exactly the resample-then-crush move for fuzz-wall prints.

NOTE: values are EZBOT's live choices, transcribed from auto-subs; correct in spirit, fine-tune by ear. He calls the DT2 "my favorite sampler of all time."

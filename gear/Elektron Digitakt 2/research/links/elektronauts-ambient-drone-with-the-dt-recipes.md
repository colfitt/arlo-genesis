https://www.elektronauts.com/t/ambient-drone-with-the-dt/41776
elektronauts.com · community thread (long-running) · multi-year

# "Ambient/Drone with the DT?" — community recipes

The big community thread on coaxing drones/ambient out of a Digitakt. CAVEAT: much of this thread predates the DT2 and refers to the **OG Digitakt** (64-step patterns, ONE LFO, mono). The techniques transfer to DT2 and get BETTER there (128 steps, 3 LFOs, stereo, Comb filters). Flagged inline.

## LFO recipes (real values quoted)
- **Random sample-start:** assign an LFO to **sample START** with a **RANDOM** waveform → "instant random loveliness" (each trig grabs a different point of a long sample). DT2: do this with one of the 3 LFOs and keep the others on filter/pitch.
- **Ultra-slow evolution:** LFO **SPEED = 0.1** with the project at **1 BPM** → extremely slow modulation for generative beds. (On DT2 you can instead use SPD low + MULT low and a slow Slew without crawling the whole project tempo.)
- **OG-only workaround:** people chained extra LFOs via **MIDI loopback** (route MIDI out→in to gain more LFOs) — reported MIDI-stability issues. NOT needed on DT2, which already has 3 LFOs/track.

## Envelope / AMP
- **Infinite sustain bed:** set **AMP DECAY = INF**, drop a trig, then play **chromatic notes** while you tweak filter / LFO / sends live — turns the box into a drone organ.
- Envelope cycle tops out around **~20 s**; for longer motion than that, use a **one-shot LFO** (slow, trig-mode ONE) as a super-slow envelope.

## Sequencer / timing
- **Track scaling 1/2 or slower** stretches a pattern into a long, slow drone evolution. (DT2's 128-step patterns + per-track scale give even longer runs.)
- **Conditional trigs + probability** across the pattern so the bed never repeats identically — the generative core for this rig.
- **Smooth transitions:** duplicate a pattern, retune tracks or shift delay time slightly between copies.

## Samples
- **Single-cycle waveforms** loaded as samples → "mental drone possibilities" (play them chromatically across the trig keys as an oscillator).
- **Long samples** (e.g. a recorded harp/guitar line) work well triggered with **multi-trigs / retrigs**.

## FX
- Reverb is "lush" and has an **INFINITE** setting — hold a tail forever for a bed.
- Delay time is adjustable but historically **not p-lockable** on OG; workarounds via pattern duplication. (Verify per OS on DT2.)

## DT2 upgrade notes (why this is easier on the II)
- 3 LFOs → put one on filter, one on pitch, one on sample-start simultaneously.
- Stereo + Panoramic Chorus + Supervoid Reverb → real width on the bed.
- Comb+/Comb− filter machines → metallic, detuned-resonator drone color the OG never had.

NOTE: values above are quoted from forum posts; treat as starting points, not gospel. Most predate DT2 — re-test on current OS.

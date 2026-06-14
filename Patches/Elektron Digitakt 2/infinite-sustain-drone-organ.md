---
type: patch
title: Infinite-Sustain Drone Organ
device: Elektron Digitakt 2
date: 2026-06-14
description: Turn the box into a hand-played drone organ from a held sample — INF amp decay plus a slow one-shot LFO as a super-slow envelope and random sample-start.
tags: [drone, organ, ambient, hands-on, community, signature]
controls:
  - { name: "AMP DECAY", type: knob, value: "INF" }
  - { name: "Play", type: button, value: "Drop a trig, then play chromatic notes while tweaking filter / LFO / sends live" }
  - { name: "LFO1 MODE (slow envelope)", type: switch, value: "ONE (one-shot, slow) — envelope cycle tops out ≈ 20 s", options: ["FREE","TRIG","HOLD","ONE","HALF"] }
  - { name: "LFO (random sample-start)", type: switch, value: "DEST = sample START, WAVE = RANDOM (each trig grabs a different point)" }
  - { name: "Ultra-slow evolution (OG values)", type: knob, value: "LFO SPEED = 0.1 at 1 BPM — on DT2 use low SPD + low MULT + slow SLEW instead" }
  - { name: "Track scaling", type: knob, value: "1/2 or slower (stretches a pattern into a long drone)" }
---

# Infinite-Sustain Drone Organ

## Concept
Turns the DT2 into a hand-played drone organ from a single held sample. With `AMP DECAY = INF` you drop a trig and then play chromatic notes by hand, sweeping filter, LFO and sends live. Because the envelope cycle tops out around 20 s, a slow ONE-SHOT LFO doubles as a super-slow envelope, and a RANDOM LFO on sample START grabs a fresh point of a long sample on every trig.

## How to play it
1. Set `AMP DECAY = INF`, drop a trig, then play chromatic notes while tweaking filter / LFO / sends live.
2. The envelope cycle tops out ≈ 20 s; for slower motion use a ONE-SHOT LFO (slow, `MODE = ONE`) as a super-slow envelope.
3. Random sample-start: assign an LFO to sample `START` with RANDOM waveform → each trig grabs a different point of a long sample ("instant random loveliness").
4. Ultra-slow evolution (OG values): `LFO SPEED = 0.1` at 1 BPM — on the DT2 instead use low `SPD` + low `MULT` + slow `SLEW` without crawling the whole tempo.
5. Track scaling 1/2 or slower stretches a pattern into a long drone.

## Notes
- Mostly OG-era values (64-step, 1 LFO, mono), flagged in-source as transferring-but-improving; re-test the `SPEED 0.1 / 1 BPM` figures on current OS.
- Use one pattern; one held-sample track.

## Sources
- `research/links/elektronauts-ambient-drone-with-the-dt-recipes.md` (t/41776)
- Transformed from Pedalxly Digitakt-2-Patches.md (community)

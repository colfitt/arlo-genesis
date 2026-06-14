---
type: patch
title: Cuckoo on-box kit — synthesize-then-sample
device: TE OP-1 Field
date: 2026-06-14
description: Build a whole kit from the OP-1's own engines, record the row to tape, sample it into the Drum Sampler — extends to sampling the banjo/fuzz-wall instead of stock drums.
tags: [drum-kit, synthesize-then-sample, build-method, designed, signature]
controls:
  - { name: "KICK", type: switch, value: "Phase engine, very short snap + Nitro filter pulled to bass + Unison (fat)" }
  - { name: "SNARE", type: switch, value: "Phase/noise snap, Nitro filter shifted UP ([Shift]+turn = fine)" }
  - { name: "HAT/SHAKER", type: switch, value: "Digital noise channel, 4th octave (kills tonality), short" }
  - { name: "TUNED PERC", type: switch, value: "Face engine (conga-ish)" }
  - { name: "METALLIC/GONG", type: switch, value: "Face engine NOT in unison, a couple tuned tones" }
  - { name: "BASS", type: switch, value: "Cluster" }
  - { name: "EXTRA SNARE/SHAKER", type: switch, value: "String engine in Unison, tightened/tuned up" }
  - { name: "Record source", type: switch, value: "EAR icon (not mic → avoids feedback)", options: ["mic","ear/tape"] }
  - { name: "FADE", type: switch, value: "OFF" }
  - { name: "Slice trim", type: knob, value: "trim slices to zero crossings" }
  - { name: "Slot/Bank", type: knob, value: "drum/ folder — cuckoo-kit (24-slice)" }
---

# Cuckoo on-box kit — synthesize-then-sample

## Concept

Build a whole drum kit from the OP-1's own synth engines, record the row to tape, then sample it back into the Drum Sampler. This extends naturally to sampling the banjo or fuzz-wall instead of stock drums. A REAL cited Cuckoo method (built on the OG OP-1; identical on the Field bar 20 s vs 12 s sampling time).

## How to play it

1. **KICK** = Phase engine, very short snap + Nitro filter pulled to bass + Unison (fat).
2. **SNARE** = same Phase/noise snap, Nitro filter shifted UP (`[Shift]`+turn = fine).
3. **HAT/SHAKER** = Digital noise channel, 4th octave (kills tonality), short.
4. **TUNED PERC** = Face engine (conga-ish). **METALLIC/GONG** = Face NOT in unison, a couple tuned tones.
5. **BASS** = Cluster. **EXTRA SNARE/SHAKER** = String engine in Unison, tightened/tuned up.
6. Record the row to tape: **FADE OFF**, record source = **EAR icon** (not mic, to avoid feedback).
7. Hold the sample button + play the tape row to capture it into the Drum Sampler.
8. Trim slices to **zero crossings**. Watch for double-compression.

## Notes

- REAL cited Cuckoo method. Engine choices are concrete; knob positions are qualitative as he described them.
- Tagged designed = build-method, not a downloadable patch. Save as `cuckoo-kit` (24-slice).

## Sources

- Ref: Cuckoo "OP-1 drumkit tutorial"
- Gear/TE OP-1 Field/research/transcripts/cuckoo-op1-drumkit-build-and-sample-tutorial.md (YouTube vJwU8utM7iE) + UsageGuide §1
- Transformed from Pedalxly OP-1-Field-Patches.md (DOUG-designed)

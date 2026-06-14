---
type: patch
title: Scene-Locked Random/Square LFOs (controlled-randomness wall)
device: Elektron Octatrack MkII
date: 2026-06-14
description: Making a static drone PERFORM — the crossfader turns on stacked random/square LFO modulation you trigger but can't fully predict (VoltageCtrl "Crossfader Demystified").
tags: [crossfader, scenes, lfo, generative, drone, community, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Bank B / Part 2 · Master track (T8) enabled; LFO-depth locks into Scene A" }
  - { name: "Pattern", type: knob, value: "[BANK] new pattern; [FUNC]+[PAGE] → 64 steps; ~92 BPM foundation" }
  - { name: "Master track", type: switch, value: "enable (PROJECT>CONTROL>AUDIO)" }
  - { name: "Approach 1 LFO1", type: switch, value: "→ FX1 low-pass cutoff, waveshape = RANDOM; ZERO depth by default; lock LFO depth into Scene A (B→A turns the random filter mod on)" }
  - { name: "Approach 1 LFO3", type: switch, value: "→ filter WIDTH, square wave (hard off/on), locked into Scene A; + T8 master comb filter freq locked into Scene A; ~4-5 retrigs locked into Scene A" }
  - { name: "Approach 2 LFO1", type: switch, value: "→ sample PITCH, square wave (time-stretched so it stays in time), zero depth, locked into a scene on track 4" }
  - { name: "Approach 2 LFO2", type: switch, value: "→ DJ EQ frequency, zero depth, locked into a scene" }
  - { name: "Approach 3 (beat-repeat)", type: switch, value: "T8 FX2 = delay, LOCK ON, TAPE OFF; SEND to 0 (freezes buffer); lock SEND = 0 + raise FEEDBACK (127 = loop indefinitely = beat repeat) into Scene A" }
  - { name: "Approach 4 (tape delay)", type: switch, value: "delay LOCK OFF, TAPE ON, FEEDBACK down for echo, ride TIME; lock params into Scene A, then DELAY CONTROL keyboard mode rides time live" }
---

# Scene-Locked Random/Square LFOs (controlled-randomness wall)

## Concept
Making a static drone PERFORM: the crossfader turns on stacked random/square LFO modulation you trigger but can't fully predict — a degraded/recorded-wrong evolving texture. LFO depths are zeroed by default and locked into a scene, so throwing the fader toward that scene switches the modulation on. The most musically-interesting crossfader source, directly on-aesthetic for evolving degraded walls.

## How to play it
1. [BANK] new pattern; [FUNC]+[PAGE] → **64 steps; ~92 BPM** foundation. Enable master track (PROJECT>CONTROL>AUDIO).
2. **Approach 1 (random):** LFO1 → FX1 low-pass filter, **waveshape = RANDOM**, adjust speed; ZERO LFO depth by default; hold [SCENE A]+lock LFO depth into Scene A → crossfader B→A turns the random filter mod on. Stack: Track 8 master FX → comb filter (lock freq into Scene A); LFO3 → filter WIDTH, **square wave** (hard off/on), lock into Scene A; SRC page → lock ~4-5 retrigs into Scene A (chance-based).
3. **Approach 2 (pitch+EQ):** LFO1 → sample PITCH **square wave** (time-stretched so it stays in time); LFO2 → DJ EQ frequency; zero depths, lock into a scene on track 4.
4. **Approach 3 (beat-repeat via delay LOCK):** Track 8 FX2 = delay, **LOCK ON, TAPE OFF**; bring SEND to 0 (freezes buffer); hold [SCENE A]+lock SEND = 0 + raise **FEEDBACK (127 = loop indefinitely = beat repeat)**.
5. **Approach 4 (tape delay):** delay LOCK OFF, **TAPE ON**, FEEDBACK down for echo, ride TIME; lock params into Scene A, then DELAY CONTROL keyboard mode rides time live.

## Notes
- The most musically-interesting crossfader source; directly on-aesthetic for evolving degraded walls. Verified tutorial.

## Sources
- Ref: VoltageCtrlRtv "Crossfader Demystified + Performance Effects"
- research/transcripts/voltagectrl-ot-crossfader-demystified.md (youtube 2VHovBWC3hs)
- Transformed from Pedalxly Octatrack-MkII-Patches.md (community)

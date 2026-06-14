---
type: patch
title: Fast Resampling Capture-and-Destroy ([REC3] master vs CUE)
device: Elektron Octatrack MkII
date: 2026-06-14
description: The core capture-and-destroy loop — print the whole mangled pedalboard mix (or a selective stem) to a buffer with one button, slice-grid it, re-sequence. No special tracks (EZBOT method).
tags: [resample, capture, slicing, master, cue, community, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Bank A / Part 1 · Track 8 = Master; capture buffer assigned to a spare track at LEVEL 127" }
  - { name: "Track 8 machine", type: switch, value: "Master (PROJECT>CONTROL>AUDIO)" }
  - { name: "Method 1 (whole mix) REC SETUP 1", type: switch, value: "SOURCE 3 = TRACK 8 (summed mix), RECORDING LENGTH = 4 bars, DESELECT inputs A B C D, TRIG = 1 2" }
  - { name: "Method 1 REC SETUP 2", type: switch, value: "QUANTIZE RECORD = PATTERN LENGTH (starts at top of pattern); keep fades for overlapping/melodic captures" }
  - { name: "Method 2 (selective stem) REC SETUP 1", type: switch, value: "SOURCE = CUE, then CUE up only the tracks you want (bounce contains only cued tracks)" }
  - { name: "Method 3 (resample on master)", type: switch, value: "SOURCE = T8, LENGTH = 16, QUANTIZE = PATTERN LENGTH (uses buffer 8 when 1-7 are full; no preview on master)" }
  - { name: "Capture button", type: button, value: "[REC3] (+ confirms recording)" }
  - { name: "Captured track LEVEL", type: knob, value: "127 (anti-generation-loss; so re-sampled layers don't lose level)" }
  - { name: "Mangle", type: knob, value: "QUICK CREATE SLICE GRID → SLIC on → keyboard = slices → scatter trigs / CREATE RANDOM LOCKS" }
---

# Fast Resampling Capture-and-Destroy ([REC3] master vs CUE)

## Concept
The core capture-and-destroy loop: print the whole mangled pedalboard mix (or a selective stem via CUE) to a buffer with one button, slice-grid it, and re-sequence. No special tracks required. The fastest no-setup resampling workflow — and LEVEL = 127 on captures is the key anti-generation-loss rule.

## How to play it
1. **Track 8 = MASTER** (PROJECT>CONTROL>AUDIO).
2. **Method 1 (whole mix):** on a spare track, [FUNC]+[REC] → REC SETUP 1: **SOURCE 3 = TRACK 8** (summed mix at real vol/pan), RECORDING LENGTH = 4 bars, **DESELECT inputs A B C D** (no incoming noise), TRIG = 1 2. REC SETUP 2: **QUANTIZE RECORD = PATTERN LENGTH** (starts at top of pattern); keep fades for overlapping/melodic captures. Start the pattern, hit **[REC3]** ("+" confirms recording).
3. **Method 2 (selective stem via CUE):** REC SETUP 1 SOURCE = **CUE**, then CUE up only the tracks you want; play, [REC3] — bounce contains only cued tracks (isolate "just the banjo" or "just the wall").
4. **Method 3 (resample on master):** REC SETUP 1 SOURCE = T8, LENGTH = 16, QUANTIZE = PATTERN LENGTH — uses buffer 8 when 1-7 are full (no preview on master track).
5. **Audition/save:** [FUNC]+[REC3] → EDIT THIS RECORDING; **SET captured track LEVEL = 127** (so re-sampled layers don't lose level each generation); [REC3] → SAVE THIS RECORDING (timestamped).
6. **Mangle:** QUICK CREATE SLICE GRID → SLIC on → keyboard = slices → scatter trigs / CREATE RANDOM LOCKS.
7. **BPM-sync imported loops:** audio editor ATTRIBUTES [FX1] ORIGINAL TEMPO = true BPM, TIMESTRETCH = NORMAL/BEATS, then SRC SETUP TSTR = AUTO.

## Notes
- The fastest no-setup resampling workflow. **LEVEL = 127 on captures is the key anti-generation-loss rule.** yt-dlp verified + manual-grounded.
- ⚠️ **Master-comp trap:** resampling thru Track 8 re-compresses (level jump) → resample via CUE OR scene-lock master Comp **MIX = 0**.

## Sources
- Ref: EZBOT "Best Resampling Method" (community, verified)
- transcripts/ezbot-ot-fastest-resampling.md + links/resample-the-rig-master-track.md + links/elektronauts-resampling-master-track.md (youtube qcfjc2w_L60; Manual §9.1-9.2 p44-48, §17.1-17.3 p104-109)
- Transformed from Pedalxly Octatrack-MkII-Patches.md (community)

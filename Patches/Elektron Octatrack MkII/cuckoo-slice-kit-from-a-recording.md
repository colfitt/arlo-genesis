---
type: patch
title: Cuckoo Slice-Kit-from-a-Recording (record → slice → keyboard)
device: Elektron Octatrack MkII
date: 2026-06-14
description: The foundational record-slice-sequence workflow — record any source into a buffer, slice it, play slices off the trig row, build a kick from a filter, freeze a fragment (Cuckoo Tutorial #1).
tags: [slicing, resample, flex, master-delay-freeze, community, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Bank A / Part 1 · All tracks Flex; track n → recording buffer n; Track 8 Master for delay-freeze" }
  - { name: "All tracks machine", type: switch, value: "Static → Flex (Flex = RAM, malleable)", options: ["Static", "Flex"] }
  - { name: "MIXER DIR", type: knob, value: "~127 (monitors record level; [FUNC]+encoder snaps full/zero/full-neg)" }
  - { name: "PLAYBACK SLICES", type: switch, value: "ON, then [FUNC]+up/down keyboard mode = SLICE", options: ["ON", "OFF"] }
  - { name: "Kick-from-filter FX1", type: switch, value: "Filter — crank RESONANCE, hunt low-cut (lands near 31) for a sub thump" }
  - { name: "Kick-from-filter grit", type: switch, value: "FX1 → Lo-Fi (distortion + bit reduction); FX2 → Dark Reverb as SEND not mix" }
  - { name: "Scene assign", type: button, value: "[SCENE A]/[SCENE B]+trig; hold scene + tweak to lock (max PITCH, negative RATE = reverse, whole-pattern pitch shift, LFO1→pitch depth = vibrato)" }
  - { name: "Master delay (T8)", type: switch, value: "double-tap; TAPE mode, LOCK on + SEND = 0 (freezes buffer + mutes live input)" }
  - { name: "Master delay FEEDBACK", type: knob, value: "max (sustain); DELAY CONTROL keyboard mode rides TIME live" }
---

# Cuckoo Slice-Kit-from-a-Recording (record → slice → keyboard)

## Concept
The canonical on-ramp: record any source (a kick, a voice, the pedalboard wall) into a buffer, slice it, play the slices off the trig row, build a kick from a resonant filter, and freeze a fragment with the master delay. The master delay-freeze (TAPE/LOCK/SEND=0/FEEDBACK max) is the "capture a fragment and sustain forever" move for drone beds.

## How to play it
1. Change all tracks Static→**Flex** (Flex = RAM, malleable). Assign track n → recording n.
2. MIXER: turn up DIR (~127 monitors record level); hold [FUNC]+encoder snaps full/zero/full-neg.
3. **Record:** [REC] on the target track (icon "+" = recording). Audition: track+play.
4. Edit: track → [BANK] → audio editor (3 encoders = start/end/loop; 4th = visual gain only; [FUNC]+YES = preview). Trim front silence to a zero-crossing (white square = snapped).
5. **SLICE:** edit → SLICE mode → position playhead with LEVEL knob → YES to drop a slice.
6. **Play slices:** PLAYBACK → SLICES ON, then [FUNC]+up/down to keyboard mode = SLICE.
7. **Kick-from-filter:** pitch sample down in PLAYBACK; FX1 = filter, crank RESONANCE, hunt the low-cut (**lands near 31**) for a sub thump; grit: FX1 → Lo-Fi (distortion + bit reduction), FX2 → Dark Reverb as SEND not mix.
8. **Scenes:** [SCENE A]/[SCENE B]+trig to assign; hold scene + tweak to lock (max PITCH, negative RATE = reverse, whole-pattern pitch shift, LFO1→pitch depth = vibrato).
9. **Leapfrog:** while on Scene B, reassign Scene A to a new slot, fade, reassign B — walk many states fast.
10. **Master delay freeze:** Track 8 = MASTER; master delay double-tap, **TAPE mode, LOCK on + SEND = 0** (freezes buffer + mutes live input), crank **FEEDBACK max** to sustain; DELAY CONTROL keyboard mode rides TIME live.
11. **SAVE:** edit → FILE → SAVE AND ASSIGN SAMPLE → name → ASSIGN TO FREE FLEX (recording slots wiped on every project load).

## Notes
- The canonical on-ramp.
- Filter-kick low-cut "~31" is the one explicit numeric value. yt-dlp verified.

## Sources
- Ref: Cuckoo "Octatrack Tutorial #1" (community, verified)
- research/transcripts/cuckoo-ot-tutorial-01-basics.md (youtube NrhPOGzn7LI)
- Transformed from Pedalxly Octatrack-MkII-Patches.md (community)

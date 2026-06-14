---
type: patch
title: Resample-the-Banjo-Loop (banjo-as-glitch-lead)
device: Elektron Octatrack MkII
date: 2026-06-14
description: Turning a Gold Tone EBM-5 banjo phrase into a sliced, re-triggered, re-pitched sequence the banjo never physically played — banjo-as-lead.
tags: [resample, slicing, flex, banjo, glitch-lead, crossfader, designed, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Bank A / Part 4 · Track 1 Flex on recorder buffer 1, 16/16 track length" }
  - { name: "Track 1 machine", type: switch, value: "Flex on recorder buffer 1", options: ["Flex", "Static", "Pickup"] }
  - { name: "REC SETUP 1 INAB", type: switch, value: "A (or A B if stereo)", options: ["A", "B", "A B", "-"] }
  - { name: "REC SETUP 1 RLEN", type: knob, value: "16 or MAX" }
  - { name: "REC SETUP 1 TRIG", type: switch, value: "ONE2", options: ["ONE", "ONE2", "HOLD"] }
  - { name: "REC SETUP 1 QREC", type: switch, value: "PLEN (capture starts at next pattern wrap, bar-aligned)" }
  - { name: "Slice grid", type: knob, value: "CREATE SLICE GRID → 16 SLICES" }
  - { name: "TSNS", type: knob, value: "high (BEAT timestretch — each slice = one note on picks)" }
  - { name: "SRC SETUP SLIC", type: switch, value: "ON (STRT selects slices)", options: ["ON", "OFF"] }
  - { name: "SRC SETUP TSTR", type: switch, value: "AUTO" }
  - { name: "STRT (Start)", type: knob, value: "CREATE RANDOM LOCKS or hand-lock per step (CC17)" }
  - { name: "PITCH (PTCH)", type: knob, value: "per-step p-locks for runs (CC16)" }
  - { name: "RTRG / RTIM (Retrig)", type: knob, value: "retrig on a couple steps for rolls (CC20/CC21)" }
  - { name: "RATE", type: knob, value: "negative on others for reversed picks (CC19)" }
  - { name: "Trig condition", type: switch, value: "conditional/probability (60-80% or 1:2/1:4)" }
  - { name: "FX1", type: switch, value: "light Lo-Fi" }
  - { name: "FX2", type: switch, value: "Spring Reverb" }
  - { name: "Scene A", type: button, value: "sliced line dry/open" }
  - { name: "Scene B", type: button, value: "filter swept + Lo-Fi crushed + freeze-delay catching fragments" }
---

# Resample-the-Banjo-Loop (banjo-as-glitch-lead)

## Concept
Turning a Gold Tone EBM-5 banjo phrase (GK-5 → VG-800 → board → OT) into a sliced, re-triggered, re-pitched sequence the banjo never physically played. The captured loop is sliced to 16, then re-sequenced with random/hand-locked slice starts, per-step pitch, retrigs, and reverse — banjo-as-lead.

## How to play it
1. **Capture:** banjo → OT input A (mono GK-5/VG-800) or A/B if stereo. Track 1 = Flex on recorder buffer 1.
2. RECORDING SETUP 1: **INAB = A** (or A B), **RLEN = 16 or MAX, TRIG = ONE2, QREC = PLEN** (capture starts at next pattern wrap, bar-aligned). Play the roll; [TRACK 1]+[REC1] (or a one-shot recorder trig FUNC+TRIG in GRID).
3. **Slice:** audio editor [TRACK 1]+[BANK], TRIM to phrase, SLICE [AMP] → CREATE SLICE GRID → **16 SLICES**. For transient-accurate slicing on picks, set **TSNS high** (BEAT timestretch) so each slice = one note.
4. SRC SETUP: **SLIC = ON** (STRT selects slices), **TSTR = AUTO**.
5. **Re-sequence:** GRID RECORDING, clear trigs [FUNC]+[PLAY], one sample trig per step. **CREATE RANDOM LOCKS** to scatter slices OR hand-lock STRT per step; **per-step PITCH p-locks** for runs; RTRG/RTIM retrig on a couple steps for rolls; **negative RATE** on others for reversed picks; **conditional/probability trigs** (60-80% or 1:2/1:4) so the line mutates each loop.
6. FX: light Lo-Fi + Spring Reverb.
7. **Perform:** Scene A = sliced line dry/open; Scene B = filter swept + Lo-Fi crushed + freeze-delay catching fragments.

## Notes
- TSNS tuned to the picking attack is the key per-source param.
- Alt: skip slicing, use a Pickup + re-pitch/reverse live.
- Re-sequence values are **designed** starting points — dial to taste.

## Sources
- designed from links/rig-recipe-loop-resequence-banjo.md + DeepResearch §13(b) (Manual §17.1.4 p105, §17.2.1 p107, §13 slice/attributes, Appendix A.2 p118)
- Transformed from Pedalxly Octatrack-MkII-Patches.md (DOUG-designed)

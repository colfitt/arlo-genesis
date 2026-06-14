---
type: patch
title: Source Recall Capture — Jam Safety Net
device: Akai MPC Sample
date: 2026-06-14
description: Grabbing a jam you forgot to record — a one-take fuzz/banjo performance — from the continuous background audio buffer.
tags: [sampling, capture, source-recall, workflow, factory, signature]
controls:
  - { name: "Source Recall (Shift + Sample Recall)", type: button, value: "drops ~20–25 s buffer onto next available pad" }
  - { name: "Alt access", type: button, value: "Shift + Input Configuration → Source Recall" }
  - { name: "Trim (Pad 13)", type: button, value: "truncate; zoom to refine start; Shift+Pad 13 to confirm" }
  - { name: "Then Chop", type: button, value: "re-sequence the captured buffer" }
  - { name: "Slot/Bank", type: knob, value: "Next free pad" }
---

# Source Recall Capture — Jam Safety Net

## Concept
Grabbing a jam you forgot to record — a one-take fuzz/banjo performance. The AC50 keeps a continuous ~20–25 s background audio buffer plus the last-played MIDI loop, so you can drop it onto a pad even if you never hit record. A real gotcha: Source Recall does NOT work on the built-in mic — it DOES work on Resample.

## How to play it
1. `Shift + Sample Recall` (or `Shift + Input Configuration` → Source Recall) drops the buffer onto the next available pad even if you never hit record.
2. Then Trim (Pad 13 to truncate, zoom to refine start, `Shift+Pad 13` to confirm).
3. Then Chop.

## Notes
- ⚠️ Source Recall does NOT work on the built-in mic — it DOES work on Resample.
- The "no mic, yes Resample" caveat is a real gotcha.

## Sources
- 🟢 `research/transcripts/akaipro-mpc-sample-resampling.md` + `research/transcripts/youtube-mpc-sample-ten-tips-and-tricks-10min.md`
- Transformed from Pedalxly MPC-Sample-Patches.md (factory)

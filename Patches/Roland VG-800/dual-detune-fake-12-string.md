---
type: patch
title: "DUAL Detune Fake 12-String — STR DELAY doubling"
device: Roland VG-800
date: 2026-06-15
description: "A fake 12-string built from DUAL GUITAR with per-string STR DELAY offsets — delaying one model's string sound a few ms behind the other simulates the 12-string sub-string shimmer without the 12STR block. The manual's own \"simulate a 12-string\" mechanism, distinct from the existing DUAL fake-chorus."
tags: [dual-guitar, 12-string, chorus, width, community, textural]
dips:
  ALT TUNE SW: "ON (required for STR DELAY to apply)"
  DIV MODE: "DUAL"
  AB BALANCE: "centered"
controls:
  - { name: "INST TYPE", type: switch, value: "DUAL GUITAR" }
  - { name: "ALT TUNE SW", type: switch, value: "ON (required for STR DELAY to take effect)", options: ["ON", "OFF"] }
  - { name: "A: STR DELAY (per string)", type: knob, value: "a few ms behind B — dial from recipe (0–100 ms range, no published values)" }
  - { name: "B: STR DELAY (per string)", type: knob, value: "a few ms apart from A — dial from recipe (0–100 ms range, no published values)" }
  - { name: "A: PITCH / FINE (per string)", type: knob, value: "small offset vs B for doubled chorus depth — dial from recipe (no published values)" }
  - { name: "B: PITCH / FINE (per string)", type: knob, value: "small offset vs A for doubled chorus depth — dial from recipe (no published values)" }
  - { name: "AB BALANCE", type: knob, value: "centered" }
  - { name: "Pan / stereo split", type: knob, value: "A left / B right for a wide doubled 12-string" }
  - { name: "Slot/Bank", type: knob, value: "User Memory (guitar mode)" }
---

# DUAL Detune Fake 12-String — STR DELAY doubling

## Concept

A fake 12-string built from `DUAL GUITAR` with per-string `STR DELAY` offsets — delaying one model's string sound a few ms behind the other simulates the 12-string sub-string shimmer without the `12STR` block. This is the manual's own "simulate a 12-string" mechanism (`A:`/`B: STR DELAY` "delay the string sound of one of them to simulate a 12-string guitar"), distinct from the existing DUAL Fake Chorus — that one leans on per-string tuning offsets; this one adds the per-string `STR DELAY` for the jangle/doubling.

## How to play it

1. Set `INST TYPE = DUAL GUITAR`; `ALT TUNE SW = ON` (required for `STR DELAY` to take effect).
2. Set `A: STR DELAY` vs `B: STR DELAY` a few ms apart per string to fake the 12-string sub-string shimmer.
3. Add small per-string `PITCH`/`FINE` offsets between A and B for the doubled chorus depth (the Gear Sounds fake-chorus mechanism).
4. Spread A↔B across the stereo split for a wide doubled 12-string.

## Notes

- Manual-verified mechanism: `A:`/`B: STR DELAY` 0–100 ms "delay the string sound of one of them to simulate a 12-string guitar" — NOT applied when `ALT TUNE SW` is OFF.
- Complements the existing DUAL Fake Chorus (per-string tuning offsets) — this one adds the per-string `STR DELAY` for the jangle/doubling.
- ⚠ Exact per-string delay values are not published — dial from the manual-verified ranges. Treat the knob values above as a dialable recipe, not sourced settings.

## Sources

- 🟢 `research/links/parameter-guide-alt-tuning-values.md` (`A:`/`B: STR DELAY` 0–100 ms = fake 12-string; only when `ALT TUNE SW` ON)
- 🔵 `research/transcripts/gear-sounds-how-to-create-patch.md` (DUAL GUITAR + per-string offsets = fake chorus)
- manual-verified mechanism (no published values) — dialable recipe

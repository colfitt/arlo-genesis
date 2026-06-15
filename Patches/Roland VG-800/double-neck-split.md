---
type: patch
title: Double Neck — two instruments, one performance
device: Roland VG-800
date: 2026-06-15
description: The factory "Double Neck" preset Juca Nery tours — a DUAL split presenting two distinct modeled instruments (e.g. a 12-string up top and a 6-string/bass below) as if playing a doubleneck, switched or split by string group with CTL-1 changing the rig.
tags: [dual-guitar, string-split, factory, performance]
dips:
  DIV MODE: DUAL
  AB BALANCE: "~50 (centered)"
  CTL-1: "rig/instrument change (factory convention)"
controls:
  - { name: "INST TYPE", type: switch, value: "DUAL GUITAR" }
  - { name: "DIV MODE", type: switch, value: "DUAL", options: ["SINGLE", "DUAL"] }
  - { name: "Channel A model", type: switch, value: "one instrument model (e.g. 12-string up top) — dial from recipe, no published value" }
  - { name: "Channel B model", type: switch, value: "a second instrument model (e.g. 6-string / bass below) — dial from recipe, no published value" }
  - { name: "AB BALANCE", type: knob, value: "~50 (centered)" }
  - { name: "CTL-1", type: switch, value: "rig/instrument change (toggle between the two necks)" }
  - { name: "Slot/Bank", type: knob, value: "Factory bank (\"Double Neck\" memory)" }
---

# Double Neck — two instruments, one performance

## Concept

The factory "Double Neck" preset Juca Nery tours — a DUAL split presenting two distinct modeled instruments (e.g. a 12-string up top and a 6-string/bass below) as if playing a doubleneck, switched or split by string group with CTL-1 changing the rig. It reframes the Dual Guitar two-path architecture as a single-performer doubleneck: two voices on one neck, addressed by where you play (or which footswitch you hit).

## How to play it

1. Recall the factory "Double Neck" memory.
2. Confirm `INST TYPE = DUAL GUITAR` with two different models on A/B; split by fretboard or toggle with CTL-1.
3. Play the low strings for one neck's voice, the high strings for the other (or footswitch between them via CTL-1).
4. Spread A↔B across the stereo split (CE-2W → Deco V2) for a wide two-instrument image.

## Notes

- Named factory preset (Juca Nery: "Double Neck"). `DUAL GUITAR` A/B is confirmed real (VGuitarForums: like the VG-99 CHAIN A/B, with a restricted model set in DUAL mode).
- Distinct from the existing Ultimate / Jazz / Acoustic splits in framing (doubleneck pairing rather than a clean/dirty or bass/guitar split).
- ⚠ Exact model pairing and split point are not published — dial the A/B models and the fretboard/CTL-1 split from the memory. Treat the values here as a dialable recipe, not captured settings.

## Sources

- 🟢 `research/transcripts/juca-nery-creative-tool-patch-tour.md` ("Double Neck")
- 🟢 `research/links/vguitarforums-vg800-main-thread.md` (DUAL GUITAR = VG-99 CHAIN A/B; restricted models in dual mode)
- Transformed from Pedalxly VG-800-Patches.md (factory — no published values)

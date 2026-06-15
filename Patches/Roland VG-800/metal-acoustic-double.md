---
type: patch
title: "Metal Acoustic — acoustic model doubling a heavy electric"
device: Roland VG-800
date: 2026-06-15
description: "The factory \"Metal Acoustic\" preset both Marcus Curtis and Juca Nery flag — a surprisingly heavy tone built on an ACOUSTIC model blended/split with a distorted metal electric, so the acoustic doubles the electric for rhythm. The literal \"recorded-wrong\"/unexpected-source move the rig is built on."
tags: [dual-guitar, acoustic, overdrive, factory, string-split, signature]
dips:
  DIV MODE: "DUAL if splitting low/high"
  AB BALANCE: "centered (~50)"
  OUTPUT SELECT: "LINE/PHONES"
controls:
  - { name: "INST TYPE", type: switch, value: "DUAL GUITAR (or ACOUSTIC + dirty AMP)" }
  - { name: "Voice A", type: switch, value: "ACOUSTIC model" }
  - { name: "Voice B", type: switch, value: "E.GUITAR into a high-gain AMP" }
  - { name: "Blend", type: switch, value: "blended (AB BALANCE) or split by string group" }
  - { name: "DIV MODE", type: switch, value: "DUAL if splitting low/high", options: ["SINGLE", "DUAL"] }
  - { name: "AB BALANCE", type: knob, value: "centered (~50)" }
  - { name: "OUTPUT SELECT", type: switch, value: "LINE/PHONES", options: ["LINE/PHONES", "GUITAR AMP"] }
  - { name: "AMP model / gain", type: knob, value: "high-gain — dial from recipe (no published values)" }
  - { name: "Split point", type: knob, value: "to taste — dial from recipe (no published values)" }
---

# Metal Acoustic — acoustic model doubling a heavy electric

## Concept

The factory "Metal Acoustic" preset both Marcus Curtis and Juca Nery flag — a surprisingly heavy tone built on an ACOUSTIC model blended (or string-split) with a distorted metal electric, so the acoustic *doubles* the electric for rhythm. The literal "recorded-wrong"/unexpected-source move the rig is built on: one voice = `ACOUSTIC` model, the other = `E.GUITAR` into a high-gain `AMP`. Distinct from the Acoustic-Top/Dirty-Rock-Bottom Split — that one is high=acoustic / low=overdrive; this one is the acoustic *doubling* a metal electric.

## How to play it

1. Recall the factory "Metal Acoustic" memory, or build with `INST TYPE = DUAL GUITAR`: one chain = `ACOUSTIC` model, the other = `E.GUITAR` into a high-gain `AMP`.
2. Blend the two (`AB BALANCE`) or split by string group for acoustic-doubled rhythm.
3. Keep the acoustic bright so it cuts through the distorted layer.
4. Into MXR 108 → Hizumitas the dual layer fuzzes as one thick wall.

## Notes

- Named factory preset (Marcus Curtis: "metal tone built on an ACOUSTIC guitar model — surprisingly heavy"; Juca Nery: "Metal Acoustic — blend of an acoustic guitar and a metal electric, good for rhythm where the acoustic doubles the electric").
- Distinct from the existing Acoustic-Top/Dirty-Rock-Bottom Split (that's high=acoustic / low=overdrive); this one is acoustic DOUBLING a metal electric.
- ⚠ Exact amp model, gain, and split point are not published — dial from the factory memory. Treat the knob values above as a dialable recipe, not sourced settings.

## Sources

- 🟢 `research/transcripts/marcus-curtis-setup-and-demo.md` ("metal tone built on an ACOUSTIC guitar model — surprisingly heavy")
- 🟢 `research/transcripts/juca-nery-creative-tool-patch-tour.md` ("Metal Acoustic — blend of an acoustic guitar and a metal electric")
- factory preset (named, no published values) — dialable recipe

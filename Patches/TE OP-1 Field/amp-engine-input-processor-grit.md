---
type: patch
title: "Amp engine — input processor + on-box grit"
device: TE OP-1 Field
date: 2026-06-15
description: "The firmware-1.6 Amp synth engine turns the Field into a pocket guitar-amp + multi-FX: amp/compression/tone/distortion plus a tuner that processes ANY input (guitar, synth, USB audio, even the internal mic). It's the first stage of grit applied on-box before the signal ever leaves the unit — the front half of the rig's two-stage 'recorded-wrong' wall (amp engine → board fuzz). The engine and its four encoder roles are documented (Ollie Loops + synthanatomy); exact knob positions are not published, so per-knob values are a dialable recipe."
tags: [amp, drive, grit, utility, input-processor, firmware-1.6, signature]
dips:
  FIRMWARE: "requires 1.6+"
  ROUTING: "external/USB source runs through the Field's downstream FX (Nitro/CWO/Mother) before tape"
controls:
  - { name: "Engine", type: switch, value: "Amp (synth engine, firmware 1.6+)" }
  - { name: "Input source", type: switch, value: "3.5mm line-in OR USB audio", options: ["3.5mm line-in","USB audio"] }
  - { name: "Input mode (OCHRE on [Input] page)", type: switch, value: "MONO", options: ["mono","stereo"] }
  - { name: "Input gain", type: knob, value: "set so the meter peaks ~60-70% (published guidance)" }
  - { name: "Enc1 — Volume", type: knob, value: "to taste (no published value)" }
  - { name: "Enc2 — Compression", type: knob, value: "to taste (no published value)" }
  - { name: "Enc3 — Tone", type: knob, value: "to taste — CCW rolls off highs / boosts lows, CW boosts highs (no published value)" }
  - { name: "Enc4 — Distortion", type: knob, value: "to taste — CW goes subtle → heavy (no published value)" }
  - { name: "T2 — Tuner", type: switch, value: "tune the source / acoustic instruments via the mic" }
  - { name: "T3 — Effect", type: switch, value: "reverb / phaser" }
  - { name: "T4 — LFO", type: switch, value: "to taste" }
---

# Amp engine — input processor + on-box grit

## Concept

Firmware 1.6 added an **Amp** synth engine that turns the Field into a pocket guitar-amp and multi-FX. It applies amp modeling, compression, tone shaping and distortion — plus a tuner — to ANY input: a guitar, an external synth, USB audio from a computer, even the unit's internal mic. That makes it the first stage of grit applied *on-box*, before the signal ever leaves the OP-1. In the rig's two-stage "recorded-wrong" wall, this is the front half: the Amp engine dirties the source, then a board fuzz takes it the rest of the way. Crucially, it lets you commit a PROCESSED external sound to tape rather than recording dry and fixing later.

## How to play it

1. Update to **firmware 1.6+**; open the **Amp** engine in synth mode with the source plugged into the **3.5mm** input or routed over **USB audio**.
2. Press **[Input]**, rotate **OCHRE** to set the input to **MONO**; set the input gain so the meter peaks around **60-70%**.
3. Set **Enc1** (volume), **Enc2** (compression), **Enc3** (tone — CCW rolls off highs/boosts lows, CW boosts highs) and **Enc4** (distortion — CW = subtle → heavy) to taste; use **T2** to tune the source.
4. Chain the Field's downstream FX (**Nitro / CWO / Mother**) after the Amp engine and record to tape **WET**.
5. For two grit stages, stack a board fuzz (MXR M108 / EAE Longsword) after the OP-1.

## Notes

- HONESTY FLAG: the Amp engine and all four encoder roles (volume / compression / tone / distortion) are documented, and the ~60-70% input-gain guidance is published — but **no exact knob values are published**. Treat Enc1-Enc4 above as a dialable recipe, not sourced numbers.
- Works on the internal mic too — tune acoustic instruments via the **T2** tuner (wear headphones to avoid feedback).
- The point of the patch is committing PROCESSED external sound to tape instead of recording dry: this is the on-box half of the dossier's two-stage grit trick.
- Provenance: factory feature (firmware 1.6) + documented encoder map (Ollie Loops) — parameter names published, knob values to-taste.

## Sources

- Gear/TE OP-1 Field/research/transcripts/ollieloops-op1-field-improved-tape-workflow.md (§The 'amp' synth engine)
- Gear/TE OP-1 Field/research/OP-1-Field-UsageGuide.md §3 (new 'amp' engine), §5
- Gear/TE OP-1 Field/research/OP-1-Field-DeepResearch.md §3 (Amp firmware addition)
- synthanatomy.com/2025/12/teenage-engineering-op-1-field-1-6-amp-synth-engine-multi-channel-usb-audio-and-more.html (Amp: volume/compression/tone/drive + tuner; USB through Field FX)
- blog.imseankim.com/teenage-engineering-op-1-field-firmware-1-6-amp-synth-engine-update/ (firmware 1.6 Amp engine)

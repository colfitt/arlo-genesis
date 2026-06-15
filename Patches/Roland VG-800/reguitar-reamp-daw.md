---
type: patch
title: "Re-Guitar Reprocessing — change the whole instrument after the take"
device: Roland VG-800
date: 2026-06-15
description: "Record the raw, unprocessed GK divided-pickup string signal to your DAW, then reprocess it later through any VG-800 model — Boss's \"Re-Guitar / Re-Bass.\" Like re-amping, except you can change the instrument, tuning and amp after the performance — commit an acoustic take or a synth take from one banjo/baritone pass. Manufacturer-stated workflow (feature sourced; the not-class-compliant caveat is repo-verified) — no published knob values."
tags: [re-guitar, reamp, daw, usb, workflow, midi]
dips:
  USB: "USB-C audio + MIDI. Full multichannel \"Re-Guitar\" mode needs the Boss Mac/Win driver and is NOT class-compliant; iOS/Android must use USB GENERIC mode, which disables the highest-CPU Re-Guitar setting (FW 1.02, Elantric)."
  PITCH TO MIDI: "Also outputs pitch-to-MIDI for triggering software instruments (distinct from the audio reprocessing below)."
controls:
  - { name: "USB audio mode", type: switch, value: "Re-Guitar multichannel (Boss Mac/Win driver) for full quality; USB GENERIC (class-compliant) for iOS/Android — generic disables the multichannel Re-Guitar setting", options: ["Re-Guitar multichannel", "USB GENERIC"] }
  - { name: "Record source", type: switch, value: "Dry, unprocessed GK divided-pickup string signal (the re-render source)" }
  - { name: "INST TYPE", type: switch, value: "Chosen at mix — any guitar / bass / synth model; dial from the part, no published values" }
  - { name: "ALT TUNE TYPE", type: switch, value: "Chosen at mix — re-tune the re-rendered take independently of the performance" }
  - { name: "FX / amp", type: switch, value: "Chosen at mix — re-render through any VG-800 FX and amp; dial from the part" }
  - { name: "Slot/Bank", type: knob, value: "Pick the re-render Memory at mix; commit multiple versions (acoustic take vs synth take) from one performance" }
---

# Re-Guitar Reprocessing — change the whole instrument after the take

## Concept

Record the raw, unprocessed GK divided-pickup string signal to your DAW, then reprocess it later through any VG-800 model — Boss markets this as "Re-Guitar / Re-Bass." It's like re-amping, except you can change the instrument, tuning and amp *after* the performance: lay down one banjo or baritone pass and later commit it as an acoustic take, a synth take, or a re-tuned take, all from the same dry string data. The take stops being a tone decision and becomes raw material. (Distinct from the pitch-to-MIDI patches — that's MIDI note-out to drive synths; this is dry-string *audio* reprocessing.)

## How to play it

1. Connect the VG-800 over USB-C to your DAW with the Boss driver (Mac/Win) for full multichannel.
2. Record the unprocessed GK string signal alongside your monitored tone.
3. Later, play the dry string data back into the VG-800.
4. Choose any instrument model, tuning and FX, and re-render the part.
5. Commit different versions (acoustic take vs synth take) from one banjo/baritone performance.

## Notes

- Boss markets this as "Re-Guitar / Re-Bass" — like re-amping but you can change the whole instrument; it also does pitch-to-MIDI for triggering software instruments. The feature itself is manufacturer-sourced.
- Honesty caveat (repo firmware lore): the highest-quality Re-Guitar multichannel USB mode is NOT class-compliant; iOS/Android get a reduced USB GENERIC mode (FW 1.02 enables generic at the cost of the multichannel mode). Frees you from committing to a tone at tracking time.
- ⚠ Recipe, not capture: the models/tunings/FX are chosen at mix from the part. No knob values are published — dial from the performance.
- Distinct from the pitch-to-MIDI patches (that's MIDI note-out to drive synths; this is dry-string audio reprocessing).

## Sources

- 🟢 https://www.boss.info/global/products/vg-800/ (Re-Guitar / Re-Bass feature)
- 🟢 https://sonicstate.com/news/2025/01/16/boss-announces-vg-800-v-guitar-processor/ (Re-Guitar / Re-Bass announced)
- `research/links/vguitarforums-firmware-lore.md` (FW 1.02 generic mode disables multichannel Re-Guitar)
- `research/links/vguitarforums-usb-audio-software-instruments.md` (Re-Guitar not class-compliant; iOS reduced)
- Provenance: manufacturer-stated workflow (feature sourced; not-class-compliant caveat repo-verified) — no published knob values

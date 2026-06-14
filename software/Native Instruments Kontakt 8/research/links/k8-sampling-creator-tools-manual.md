https://www.native-instruments.com/ni-tech-manuals/creator-tools-manual/en/overview-of-creator-tools
Native Instruments · Creator Tools Manual — Overview / Instrument Editor / Lua scripting · current (ships with Kontakt 8)

# Creator Tools — the standalone instrument-building companion app

Creator Tools is a free standalone app that **ships with Kontakt 8** (separate
launcher, not inside the plug-in). It is the "developer bench" for batch /
programmatic instrument building. Three components:

1. **Debugger** — for finding and fixing problems in Kontakt KSP script
   (steps, breakpoints, watch variables). Engine-side; not the sampling angle.
2. **Instrument Editor** — the workhorse for sampling. It **connects live to a
   running Kontakt instance** (Kontakt open in your DAW or standalone) and
   shows the instrument's structure as a nested tree (instrument → groups →
   zones). A **Lua Script** panel runs Lua scripts you've written/saved to disk
   to **programmatically modify** that live instrument.
3. **GUI Designer** — visual layout of the Komplete UI (engine/UI side).

## What the Instrument Editor + Lua can do (the batch-building payoff)

- **Automap samples directly from disk** — create a new instrument's zones from
  a folder of samples without dragging by hand. Limited file-system access lets
  it build instruments from samples on disk.
- **Duplicate and batch-rename groups and zones** — e.g. spin up 5 round-robin
  groups or rename a whole velocity tree in one pass.
- **Copy settings from one part of an instrument to another** — copy a group's
  envelope / FX / tuning to every other group at once.
- **Edit zone properties** — tune, volume, mapping, names — in bulk via script.
- **Rearrange / add / remove groups and zones** programmatically.

## MIR functions (Music Information Retrieval) — the auto-detection magic

These analyze the audio so you don't tune/map by ear:

- **Pitch detection** — detects the fundamental of a *monophonic / single-note*
  sample, on the MIDI scale (69 = 440 Hz), range semitone 15 (~20 Hz) to 120
  (~8.4 kHz). Use it to auto-set root keys. (Note: unreliable on vibrato-heavy
  or inharmonic sources — see Hilowitz's violin caveat.)
- **RMS / Loudness detection** — calculated over small audio blocks; the block
  length = "frame size" (seconds), repeated at a "hop size" interval to the end
  of the sample. Useful for auto-sorting samples into velocity layers by level.
- **Single vs batch functions** — single functions take an absolute filename;
  **batch functions take an absolute folder name** and process the whole folder.

## Getting started

Example + tutorial Lua scripts ship **in the application folder**. Copy the
`scripts/` folder contents to `user/Documents/Native Instruments/Creator Tools`
so your own scripts and the examples live together. The 2020-era community
workflow (Hilowitz) uses Creator Tools' export Lua scripts to convert a finished
Kontakt instrument out to **Decent Sampler** and **SFZ** formats (paste console
output, strip absolute paths → relative). The Kontakt 8 era adds the
**Komplete Instrument Building Toolkit (KIBT) 1.0** with the new Komplete Script
language + Komplete UI framework for high-DPI reactive interfaces.

## Rig relevance
For this rig the killer use is **folder-to-instrument batch building**: dump a
labelled folder of OP-1 / Digitakt / VG-800 one-shots (or banjo notes) on disk,
run an automap Lua script, let pitch-detection set root keys, and skip the
manual drag-and-map entirely — then export to NKI (and optionally Decent
Sampler/SFZ for portability to the iPad / Ableton Lite rig).

> Source: NI Creator Tools Manual (overview-of-creator-tools, the Instrument
> Editor / Lua Script / MIR pages). Page 403's on direct fetch; content
> distilled from the manual text surfaced in search. Cross-ref the PDF:
> native-instruments.com → KONTAKT_602_Creator_Tools_Manual.pdf.

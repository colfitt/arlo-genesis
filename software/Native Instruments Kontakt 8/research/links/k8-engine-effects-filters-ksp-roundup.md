Multiple sources (KVR, HISE forum, NI manual structure, magneticmag/musicradar reviews)
Built-in effects, filters, convolution + KSP scope · roundup

## Built-in effects & filters (verified across sources)
- Kontakt ships with a large built-in FX suite — the marketing/spec figure cited
  widely is **~92 effect modules** total: reverbs, delays, dynamics, distortions,
  guitar amps + cabinets, modulation FX, EQs, bitcrushers, filters, plus a
  convolution effect and a surround panner.
- Premium DSP carried in: **RAUM** (reverb), **Replika** (delay), **Reaktor
  filters**, tape saturation, and **convolution reverb** are built directly into
  Kontakt — "eliminating the need for third-party plugins" (NI build-instrument
  video).
- Effect types include: delay, reverb, distortion/overdrive, chorus, flanger,
  phaser, stereo modeller, inverter, lo-fi, compressor, surround panner,
  convolution.
- Filters: multi-mode filter set; **8.3 (Mar 2025)** added **Moog-style passband
  filters** and **Japanese Sallen-Key** filters.

## Convolution / IR (from KVR + NI forum)
- Kontakt has a built-in **Convolution** instrument effect usable as **insert OR
  send**. You can **drag any audio file into it as an impulse response** — so it
  doubles as a creative convolution box (load a noisy/degraded IR, not just a
  hall).
- It splits the IR into **early vs late reflections**, each separately filterable
  and sizable; has **pre-delay** and reverb controls.
- Ships with factory IR samples (cathedrals, halls, etc.).
- Community verdict: a perfectly usable convolution reverb, especially for
  built-in/library use; the dedicated **RAUM** algo reverb is the go-to for
  big modulated/cosmic tails.

## Insert vs send vs bus (architecture)
- Kontakt's effect rows mirror a mixer: **Group Insert FX → Amplifier →
  Instrument Insert FX → Send FX → Main/Instrument FX → output**. Plus **Aux
  send buses** at the instrument level.
- CRITICAL for modulation: only **Source / Amplifier / Group Insert FX** params
  can be internally modulated. Instrument Insert, Send, and Main FX cannot (use
  host automation or move the FX to a Group Insert slot).

## KSP scope (verified, honest)
- **KSP = Kontakt Script Processor.** It sits between incoming MIDI and the
  Source module, **at the instrument level** (same level as Instrument Insert/
  Send FX). NOT a plain MIDI processor — it can read/write Kontakt-specific
  params (group names, zone tuning, engine params) and build **custom GUIs**.
- A "script" is plain text in the **Kontakt Script Language**; loaded as a module
  in the Script Editor tab, saved as a **.nkp** preset. Apply to compile.
- What it can do: arpeggiators/harmonizers, sequencers (incl. Euclidean),
  exotic tunings, intelligent articulation switching, round-robin/humanization
  logic, custom performance GUIs with graphics. Every pro Kontakt library uses it.
- Learning curve (honest): the engine is approachable for SMALL scripts (you can
  load + tweak factory script presets like Harmonize with zero coding), but
  WRITING non-trivial KSP is real programming — callbacks (on note / on release /
  on controller / on init), variables, UI widgets. The canonical free learning
  resource is **Nils Liberg's KSP tutorial**; the official **KSP Reference
  Manual** (Kontakt 8 PDF, ~ Sept 2024) catalogues every command.
- **Creator Tools** (separate NI app) handles the developer side: GUI design via
  the Creator Tools editor, debugging, instrument packaging/encoding — easier
  than hand-coding the GUI in raw KSP.

---
name: Pure LoFi
brand: Arturia
category: software
subcategory: instrument
formats: [vst3, au, standalone]
host_in: [logic, ableton]
installed: true
install_path: /Library/Audio/Plug-Ins/Components/Pure LoFi.component
version: latest
status: owned
tags: []
related: []
---

# Arturia Pure LoFi

**Summary** — Arturia lo-fi **synth/sampler** (April 2025). Bakes degradation **at
the source**: 2 engines + a noise engine → per-engine Hardware modes (CMI, Emulator
II, SK-1, SP-1200, S900, MPC60) → filters → a tape **LoFi Processor** → 4 FX.

> ⚠️ **Repo note:** this was previously mis-filed under "Cableguys" by a
> `scan_plugins.py` brand-heuristic bug. It is Arturia (`com.arturia.component.Pure-LoFi`,
> `/Applications/Arturia/`). Scanner now keys brand off the bundle-id manufacturer.

## Why I have it
A **pre-degraded instrument/texture source** to sit *alongside* the banjo — a fast
nostalgic pad/keys/noise generator. **NOT** another degrade effect: RC-20 +
SketchCassette + Decapitator + Lossy + the hardware tape pedals already own the
"degrade existing audio" job. Pure LoFi's non-overlapping value is *generating*
lo-fi sound, then (optionally) running it through that effect chain.

## Signature uses
- **Drone/texture-bed render:** turn OFF both oscillators so only the **Noise
  engine** sounds, hold a note → continuous wash → **bounce to audio** to layer
  into the wall.
- **LoFi-Amount-as-envelope:** drag the amp ADSR onto **LoFi Amount** so the lo-fi
  hits on the transient then clears (or backs off after attack).
- **Creative Sampler random-trigger** pads (taped-piano samples, vibrato + filter on
  vinyl-rotation-derived LFOs) for non-static evolving pads.
- Per-engine **Hardware modes** + the master **LoFi Processor** tape modes (Golden
  Age / Dim Memories / Cathodic Tube…) for source-baked grit.

## Notes
- **It's an INSTRUMENT, not an effect** — no insert/bus/stem use. The **LoFi
  Processor is NOT available as a standalone effect** (a reviewer's specific wish) —
  you can't put it on the banjo the way you'd use RC-20.
- **2025 release → thin community**; **launch QC drift** (in-app tutorial demos
  features that misbehave; Advanced-FX modules can read greyed-out even when on).
  External tutorials beat the official docs.
- Deep usage research → `research/Pure-LoFi-UsageGuide.md` (5 transcripts + 5 links).

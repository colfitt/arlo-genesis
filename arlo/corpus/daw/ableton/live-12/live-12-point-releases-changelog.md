# Live 12 Point Releases — What Each Version Added

**Scope:** daw
**Source:** Deep-research synthesis (2026-05) — Ableton Live 12.x — verify before treating as authoritative
**Canonical references:** [Ableton Live 12 Release Notes](https://www.ableton.com/en/release-notes/live-12/); [All new features in Live 12](https://www.ableton.com/en/live/all-new-features/); [Live 12 — coming March 5](https://www.ableton.com/en/blog/ableton-live-12-coming-march-5/); [Live 12.1 is Out Now](https://www.ableton.com/en/blog/live-121-is-out-now/); [Live 12.2 release blog](https://www.ableton.com/en/blog/ableton-live-12-2-is-coming-on-june-11/); [Live 12.3 is Out Now](https://www.ableton.com/en/blog/live-12-3-is-here/); [Push with Live 12 Release Notes](https://www.ableton.com/en/release-notes/push-12/)
**Tags:** `daw-ableton`, `live-12`, `live-12-feature`, `changelog`, `reference-fact`, `version-history`

---

## Why this file exists

Older online tutorials confidently describe features as "Live 12" without specifying which point release introduced them. The result is users searching "how to do stem separation in Live 12" and being told it's been there since launch, when in fact it arrived in Live 12.3, twenty months after 12.0. This file is the version-stamping reference: every feature added in every shipped 12.x point release, sourced from Ableton's official [Live 12 Release Notes](https://www.ableton.com/en/release-notes/live-12/) and supporting launch blog posts. **Rules used in this file**: only verified shipped additions are listed; "expected in 12.x" or "rumored" features are omitted; minor bug fixes are omitted; release-date-by-release-date organization.

## Live 12.0 — March 5, 2024 (launch)

The headline release. Per the [Ableton launch announcement](https://www.ableton.com/en/blog/ableton-live-12-coming-march-5/) and [Live 12.0 launch coverage](https://cdm.link/ableton-live-12-everything-new/), the 12.0 launch shipped:

**New instruments and effects:**
- **Meld** — bi-timbral, MPE-enabled synthesizer with two macro oscillators per voice, 18+ engine types, dual multimode filters, modulation matrix
- **Granulator III** — granular instrument with MPE, on-the-fly audio grabbing, stereo LFO, three playback modes (replaces older Granulator)
- **Roar** — three-stage saturation/coloring effect, supports series/parallel/mid-side/feedback/multiband configurations, built-in compressor, 12+ shaper modes

**MIDI composition tools:**
- **MIDI Generators** (Stacks, Rhythm, Seed, Shape, Euclidean) — generate notes from scratch into a clip
- **MIDI Transformations** (Arpeggiate, Connect, Ornament, Quantize, Recombine, Span, Strum, Time Warp, Velocity Shaper, Chop) — modify existing notes
- **Scale awareness** — project-wide and per-clip Scale settings, scale-aware MIDI editor highlighting

**Modulation:**
- **Modulators promoted to core** — Shaper, LFO, Envelope Follower, Shaper MIDI, Envelope MIDI, Expression Control, MPE Control
- **New modulation behavior** — destinations no longer locked when modulated; Modulation vs. Remote Control toggle

**Tuning systems:**
- **.scl/.ascl scale-file import** — 152 included tunings (EDO 5–72, European historical, Just Intonation, world traditions)
- **All built-in instruments tuning-aware** — Operator, Analog, Wavetable, Drift, Meld, Sampler, Simpler, Electric, Tension, Collision

**Workflow and UI:**
- **Stacked detail views** — clip editor, device, automation visible simultaneously
- **Mixer in Arrangement view** — previously Session-only
- **Browser auto-tagging, sound similarity search**
- **Refined UI with reduced visual clutter**
- **Expanded keyboard accessibility**

Note: **Drift** is often listed as a "Live 12 new" synth but actually shipped in Live 11.3 (October 2023). It is bundled with all Live 12 editions and is widely associated with the 12.0 launch — but the device itself predates 12.0.

## Live 12.1 — October 8, 2024

Per the [Live 12.1 is Out Now blog post](https://www.ableton.com/en/blog/live-121-is-out-now/) and [Synthtopia coverage](https://www.synthtopia.com/content/2024/10/08/ableton-live-12-1-now-available-heres-whats-new/):

**New instruments and effects:**
- **Auto Shift** — real-time pitch correction and harmonization device, monophonic pitch tracking, formant shifting, MIDI sidechain for harmony generation
- **Drum Sampler** — compact sampling device for Drum Rack with 8-bit, time stretch, ring modulation, FM, pitch envelope, punch effects
- **Limiter overhaul** — smoother release curve, updated metering, Mid/Side routing, True Peak, Soft Clip, Maximize modes
- **Saturator** — Bass Shaper curve added, improved UI

**MIDI tools:**
- **Find and Select MIDI Notes** — filter and select notes by time, pitch, velocity, chance, duration via new MIDI editor toolbar
- **Chop MIDI tool** — note chopping operations
- **Two new MPE-specific MIDI Transformations** — **Glissando** (pitch bend curve between notes) and **LFO** (LFO on MPE parameters per note)
- **Apply Grooves Instantly**

**Workflow:**
- **Scale Awareness for Audio Clips** — audio clips can now carry scale information
- **Auto-tagging** — automatic tag assignment for samples under 60 seconds and VST3/AU plugins
- **Full-Height Browser** option
- **Undo History**
- **CC Control** MIDI assignment workarounds
- **Device icons** across instrument/effect presets
- **Macro Variations on Push 2/3**

## Live 12.2 — June 11, 2025

Per the [Live 12.2 release blog](https://www.ableton.com/en/blog/ableton-live-12-2-is-coming-on-june-11/), [MusicTech coverage](https://musictech.com/news/gear/ableton-live-12-2-release-date-features/), and the [Live 12 Release Notes](https://www.ableton.com/en/release-notes/live-12/):

**Devices:**
- **Auto Filter redesign** — new filter types (DJ, Comb, Vowel, Morph, Resampling, Notch + LP), new circuits (SVF, DFM, MS2, PRD), reduced algorithmic latency (~2 ms, down from ~5 ms)
- **Expressive Chords** — new MPE-enabled Max for Live device for intuitive chord progression playing, free for all Live editions and Push
- **Meld additions** — Chord oscillator, Scrambler LFO FX
- **Roar updates** — Delay routing mode, Dispersion filter, external/MIDI sidechain, Envelope Hold
- **Resonators and Spectral Resonator** — gained scale awareness and tuning system support
- **Operator** — maximum voice count increased to 32

**Workflow:**
- **Bounce to New Track / Bounce Track in Place** — bounce clips or time selections including processing to a new audio track
- **Browser Filter View redesign** — toggle system, content columns customization, sorting
- **Quick Tags Panel** — manage tags without opening full Tag Editor
- **Custom browser icons** for library labels and user folders
- **Device header improvements** — separate sidechain toggle, dedicated context menu button, breakout view arrow
- **Take Lanes** improvements in Arrangement view
- **Scene Follow Actions** — Unlinked and Longest modes
- **Automation/Modulation keyboard workflow** — breakpoint selection, navigation, editing via keyboard
- **GPU renderer** option (Windows; not applicable on macOS)
- **Push** — Follow Actions on Push, structure and perform Sets

**Auto Pan-Tremolo redesign** is sometimes attributed to 12.2 but actually shipped in Live 12.3 per the [Live 12 Release Notes](https://www.ableton.com/en/release-notes/live-12/). Confirm before claiming.

## Live 12.2.1 through 12.2.7 (bug-fix and control-surface point releases)

Per the [Live 12 Release Notes](https://www.ableton.com/en/release-notes/live-12/):

- **12.2.1 (June 19, 2025)** — Novation Launch Control XL 3 control surface support; Move control surface fixes
- **12.2.2 (August 13, 2025)** — Komplete Kontrol S MK3 updates (track meters, encoder fine-tuning, tempo control, device navigation)
- **12.2.5 (August 27, 2025)** — Akai MPK Mini Plus support; additional Komplete Kontrol S MK3 enhancements
- **12.2.6 (October 14, 2025)** — Akai MPK mini IV support
- **12.2.7 (November 12, 2025)** — Push 2/3 connection fixes (macOS); Max 9.0.8 update

## Live 12.3 — November 25, 2025

The stem-separation release. Per the [Live 12.3 is Out Now blog](https://www.ableton.com/en/blog/live-12-3-is-here/) and [MusicTech coverage](https://musictech.com/news/music/ableton-live-12-3/):

**Major features:**
- **Stem Separation** — built-in local audio separation into Vocals, Drums, Bass, Others (Suite only); High Speed and High Quality modes; browser-context and clip-context workflows; auto-tempo-detection in empty Sets
- **Splice Integration** — browser-integrated sample library, key detection, Sound search, preview sync
- **Auto Pan-Tremolo** — redesigned device with Panning/Tremolo modes, LFO enhancements, Modulation Attack parameter

**Workflow:**
- **Bounce Group Tracks** — Bounce Group to New Track, Bounce Group in Place
- **Paste Bounced Audio** — paste copied material as bounced audio directly
- **Device A/B Comparison** — toggle between two device states; copy settings between states
- **Arrangement View** — MIDI note filtering, empty clip insertion without time selection, Shift-click clip creation
- **Browser sidebar icon updates**
- **Multiple MIDI clip warp marker support** via "Set 1.1.1 Here"
- **Splice/Cloud/Push label hiding** via context menu

**Core Library additions:**
- New drum racks, vocal/guitar recording templates, Auto Pan-Tremolo presets

**Control surfaces:**
- Akai MPK Mini Plus, Komplete Kontrol S Mk3 updates

**Max 9.0.9 bundled** with insert_device, insert_chain, DrumChain.in_note API additions; Edit in Max option.

## Live 12.3.1 through 12.3.8 (bug fixes and incremental features)

Per the [Live 12 Release Notes](https://www.ableton.com/en/release-notes/live-12/):

- **12.3.1 (December 9, 2025)** — Soundtoys plugin crash fixes
- **12.3.2 (December 17, 2025)** — Max for Live API performance fix
- **12.3.5 (January 26, 2026)** — Bounce to New Track unique track numbering; crash folder auto-cleanup
- **12.3.6 (March 3, 2026)** — Novation Launch Control 3 control surface support; Macro mapping Simpler filter type fixes
- **12.3.7 (April 13, 2026)** — **GPU stem separation for macOS 26.4+** (major speed improvement for stem separation on Apple Silicon)
- **12.3.8 (April 29, 2026)** — Expressive E Osmose control surface support

## Live 12.4 — May 5, 2026 (current at time of writing)

The most recent major point release. Per the [Live 12 Release Notes](https://www.ableton.com/en/release-notes/live-12/) and [SynthAnatomy Live 12.4 coverage](https://synthanatomy.com/2026/04/ableton-live-12-stay-creative-and-in-focus-an-overview-of-the-new-features.html):

**Major features:**
- **Link Audio** — real-time peer-to-peer audio streaming between Link-connected devices, with latency controls and peer management; major addition for collaboration and live performance
- **Erosion device update** — Noise Blend control, Stereo Width morphing, reduced latency (2ms)
- **Chorus-Ensemble refinement** — Classic mode renamed to "Chorus" with Time and Taps parameters
- **Delay device LFO expansion** — Hertz/milliseconds/tempo-synced modes, seven waveforms, Morph parameter
- **Stem Separation refinements** — Separate Stems for Time Selection, Merge Selected Stems to Single Track, audible-portion processing
- **Learn View** — replaces Help View with structured learning modules, video content, progress tracking
- **Quick Tags improvements** — create tags, parent tags, tag groups directly from Quick Tags panel
- **Wavetable maximum voice count increased to 16**
- **Device renaming when folded** capability
- **Arrangement View** — Cmd-click grid toggle (macOS), Esc focus behavior, Copy Time command
- **Move Control Surface** — audio clip support in Note Mode

**Max for Live 9.1.4** with new parameter visibility modes ("Visible," "Visible (Not Stored)").

**Core Library** — Vocal Strip Complete, Guitar Amp Stack racks, updated Chorus-Ensemble/Delay presets, KUČKA drum racks.

## Features commonly misattributed to wrong versions

A short list of version-attribution errors that show up in online tutorials:

- **Stem Separation** — Live 12.3 (not 12.1 as occasionally claimed)
- **Drift synthesizer** — Live 11.3 (not 12.0; ships with Live 12 but predates it)
- **Hybrid Reverb** — Live 11.0 (not 12.x)
- **Unified Delay device** — Live 11.0 (not 12.x)
- **Spectral Resonator and Spectral Time** — Live 11.0 (not 12.x)
- **Auto Shift** — Live 12.1 (not 12.0)
- **Drum Sampler** — Live 12.1 (not 12.0)
- **Auto Filter redesign** — Live 12.2 (not 12.0)
- **Note Modulator** — does not exist as a shipped Live 12 device as of 12.4. If a future point release adds one, this file will need updating.

## How to verify a feature's version when in doubt

The single canonical source is [Ableton's Live 12 Release Notes](https://www.ableton.com/en/release-notes/live-12/) — every shipped point release is listed with its full changelog. The launch blog posts ([12.0](https://www.ableton.com/en/blog/ableton-live-12-coming-march-5/), [12.1](https://www.ableton.com/en/blog/live-121-is-out-now/), [12.2 announcement](https://www.ableton.com/en/blog/ableton-live-12-2-is-coming-on-june-11/), [12.3](https://www.ableton.com/en/blog/live-12-3-is-here/)) cover the headline features in user-friendly language. The Push-firmware-matching release notes at [Push with Live 12 Release Notes](https://www.ableton.com/en/release-notes/push-12/) track which Live features have been brought to Push standalone firmware. When a tutorial cites a "Live 12" feature, check the published date and the release notes to confirm the feature actually exists in the version it claims.

## What's NOT in Live 12 as of 12.4

Things commonly assumed or requested but not shipped as of Live 12.4 (May 2026):

- A dedicated "Note Modulator" device (the MIDI-triggered modulation family is Envelope MIDI, Shaper MIDI, Expression Control, MPE Control)
- Folder-based project organization in the Arrangement view
- Multi-monitor view-splitting beyond the existing primary/secondary support
- A native LUFS meter device (third-party Youlean is the common solution)
- DDP album export for mastering
- Native MTS-ESP client support (Microtuner is the bridge)
- Audio-rate modulation on the standard Modulators

These are the most commonly asked-about features that don't yet ship. If a future 12.x release adds any, this file needs updating.

## Cited Retrieval Topics

- "what version of ableton live has stem separation"
- "when did ableton release live 12"
- "what came in live 12.1"
- "what came in live 12.2"
- "what came in live 12.3"
- "what came in live 12.4"
- "what version of live introduced auto shift"
- "is drift a live 12 synth"
- "when was the auto filter redesigned in live 12"
- "what's the latest version of ableton live 12"

## Sources

- [Ableton — Live 12 Release Notes](https://www.ableton.com/en/release-notes/live-12/)
- [Ableton — All new features in Live 12](https://www.ableton.com/en/live/all-new-features/)
- [Ableton Blog — Live 12 coming March 5](https://www.ableton.com/en/blog/ableton-live-12-coming-march-5/)
- [Ableton Blog — Live 12.1 is Out Now](https://www.ableton.com/en/blog/live-121-is-out-now/)
- [Ableton Blog — Live 12.2 is Coming on June 11](https://www.ableton.com/en/blog/ableton-live-12-2-is-coming-on-june-11/)
- [Ableton Blog — Live 12.3 is out now](https://www.ableton.com/en/blog/live-12-3-is-here/)
- [Ableton — Push with Live 12 Release Notes](https://www.ableton.com/en/release-notes/push-12/)
- [CDM — Ableton Live 12: a guide to everything that's new](https://cdm.link/ableton-live-12-everything-new/)
- [Synthtopia — Ableton Live 12.1 Now Available](https://www.synthtopia.com/content/2024/10/08/ableton-live-12-1-now-available-heres-whats-new/)
- [MusicTech — Live 12.2 release details](https://musictech.com/news/gear/ableton-live-12-2-release-date-features/)
- [MusicTech — Ableton Live 12.3 has arrived](https://musictech.com/news/music/ableton-live-12-3/)
- [SynthAnatomy — Ableton Live 12.4 overview](https://synthanatomy.com/2026/04/ableton-live-12-stay-creative-and-in-focus-an-overview-of-the-new-features.html)

## See also

- `corpus/daw/ableton/live-12/modulators-shaper-lfo-envelope-follower-note-modulator.md` (C1 — modulators detail)
- `corpus/daw/ableton/live-12/scale-aware-midi-and-global-scale.md` (C2 — scale awareness detail)
- `corpus/daw/ableton/live-12/midi-generators-and-transformations.md` (C3 — MIDI Tools detail)
- `corpus/daw/ableton/live-12/tuning-systems-and-microtonal-support.md` (C4 — tuning systems detail)
- `corpus/daw/ableton/live-12/stem-separation.md` (C5 — stem separation detail)
- `corpus/daw/ableton/live-12/push-3-standalone-workflow.md` (C6 — Push standalone detail)

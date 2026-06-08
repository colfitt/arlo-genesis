# Tuning Systems and Microtonal Support (Live 12)

**Scope:** daw
**Source:** Deep-research synthesis (2026-05) — Ableton Live 12.x — verify before treating as authoritative
**Canonical references:** [Live 12 Reference Manual — Using Tuning Systems](https://www.ableton.com/en/live-manual/12/using-tuning-systems/); [All new features in Live 12](https://www.ableton.com/en/live/all-new-features/); [Sound on Sound — Live 12 Tuning Systems](https://www.soundonsound.com/techniques/ableton-live-12-tuning-systems); [Live 12 Release Notes](https://www.ableton.com/en/release-notes/live-12/); [Ableton — Microtuner pack](https://www.ableton.com/en/packs/microtuner/)
**Tags:** `daw-ableton`, `live-12`, `live-12-feature`, `tuning`, `microtonal`, `xenharmonic`, `ascl`

---

## What "tuning systems" means in Live 12

Pre-Live-12, alternate tunings in Ableton meant either retuning a sampler one note at a time, using the free Microtuner Max for Live device (released 2022), or running MTS-ESP. Live 12 made tuning a first-class project-level property. The [Live 12 Reference Manual on Tuning Systems](https://www.ableton.com/en/live-manual/12/using-tuning-systems/) describes it as "a Scala file loaded into a Live Set to use a custom tuning for notes" — when active, the loaded tuning replaces the default 12-tone equal temperament across all built-in instruments and any MPE-capable third-party plugins. This is one of the single most-requested features in Ableton history, and Live 12's implementation made microtonal composition genuinely accessible without specialist plugins.

## The .scl and .ascl file formats

Live 12 reads two file formats. **.scl** is the Scala format developed by Manuel Op de Coul in 1991 — a plain-text definition of a scale as a sequence of pitch ratios or cents values. The Scala archive at huygens-fokker.org contains over 5,000 historical and theoretical scales, all directly loadable into Live 12. **.ascl** is Ableton's superset of .scl that adds metadata fields (display name, scale degree names, reference pitch) without breaking .scl compatibility. An .ascl file is a .scl file with extra optional headers — .scl files load fine and .ascl files load with richer metadata. Drag either format into the Tuning section of the browser, or drop directly into a Live Set, and the tuning becomes available for selection.

## Loading and activating a tuning

The workflow is: open the Browser, click the **Tunings** label in the sidebar. Live ships with 152 included tunings spanning Equal Divisions of the Octave (EDO) from 5-EDO to 72-EDO, European historical tunings (Pythagorean, meantone, well-tempered systems), Just Intonation variants, and world traditions (Arabic Maqam, Persian Radif, Turkish Makam, Gamelan slendro and pelog), per the [Sound on Sound Live 12 Tuning Systems coverage](https://www.soundonsound.com/techniques/ableton-live-12-tuning-systems). Double-click a tuning file or press Enter to load it — it appears in the Tuning section of the project. Custom user .scl/.ascl files added to a Places folder show under the "User" tag. Once a tuning is loaded, set its **Reference Pitch** (the frequency anchor, typically 440 Hz on A) and the **Reference Note** (which MIDI note maps to the reference pitch). For 12-EDO replacement, that's it.

## Per-project, not per-device

This is the most-misunderstood part of Live 12 tuning. The [Live 12 Reference Manual](https://www.ableton.com/en/live-manual/12/using-tuning-systems/) confirms: tuning systems operate **per-project (Live Set)**, not per-instrument. Loading a tuning applies it globally — every instrument that respects tuning systems retunes simultaneously. There's no per-track tuning override built into Live 12's native tuning system. If you need different tunings on different tracks within one project, the workarounds are: place the Microtuner Max for Live device on each track with different per-device tuning settings (Microtuner has Lead/Follow modes for syncing or independence), or freeze tracks at one tuning before loading another. For most users, project-level tuning is the right abstraction — alternate-tuning compositions usually live entirely in one tuning.

## Which built-in instruments are tuning-aware

The [Live 12 Reference Manual on Tuning Systems](https://www.ableton.com/en/live-manual/12/using-tuning-systems/) states: "All of Live's built-in instruments are supported for use with tuning systems." The complete list of built-in tuning-aware instruments as of Live 12.2:

- **Wavetable, Drift, Meld** — the modern synth family (all MPE-capable, all fully tuning-aware)
- **Operator** — the FM workhorse
- **Analog** — the subtractive synth
- **Sampler, Simpler** — both samplers respect tuning
- **Electric, Tension, Collision** — the physical-modeling family
- **Resonators, Spectral Resonator** — added in Live 12.2 per the [release notes](https://www.ableton.com/en/release-notes/live-12/)
- **External Instrument** — passes tuning through to external MIDI hardware as pitch-bend information (with caveats — see the limits section)

Bundled Max for Live instruments inherit tuning support if they're MPE-capable. The Drum Sampler (Live 12.1+) is tuning-aware for its pitched playback. Tunings apply directly to the instrument's pitch generation — when the project tuning changes, every existing note immediately plays at the new pitch without re-recording.

## Common alternate tunings and what they sound like

A short tour of the most-reached-for tunings:

- **Just Intonation (5-limit)** — uses small-integer-ratio intervals. Major thirds are perfectly consonant (5:4 ratio), the tonic-fifth (3:2) is pure. Drone music, La Monte Young, Indian classical. Sounds "in tune" in a way 12-EDO never quite does — but transposing reveals wolf intervals.
- **19-EDO** — divides the octave into 19 equal parts. Has better major thirds than 12-EDO and approximates meantone temperament well. Sounds slightly "off" at first; rewards repeated listening.
- **31-EDO** — divides into 31. Approximates Just Intonation extremely well and supports diatonic music that sounds nearly identical to 12-EDO with subtler color.
- **Bohlen-Pierce** — based on the 3:1 tritave rather than the 2:1 octave, divided into 13 equal steps. Sounds genuinely alien — no octaves, no familiar tonic-dominant relationships.
- **Pythagorean** — historical, pure 3:2 fifths stacked, slightly sharp major thirds. Medieval and Renaissance music.
- **Gamelan slendro/pelog** — non-Western scales with 5 or 7 notes per octave at non-equal spacings.

Sound on Sound's Live 12 Tuning Systems article recommends "pick one and simply start playing the keyboard" as the exploration method — alternate tunings reveal their character through play, not theory.

## Microtonal MIDI composition workflow

The full microtonal workflow in Live 12 looks like this: (1) load a tuning system from the Browser into the Tuning section. (2) optionally, set the Control Bar Scale to a microtonal scale .ascl file that matches the tuning's note layout (so the MIDI editor highlights in-scale notes — see C2). (3) compose in the MIDI editor as normal — notes are MIDI note numbers, but their realized pitches follow the loaded tuning. (4) for non-standard pitches that don't map cleanly to MIDI's 128 notes, use Microtuner or the per-instrument detune controls. (5) bounce or freeze at the desired tuning to lock in the realized pitches before exporting. The MIDI file format does NOT carry tuning system data — exporting MIDI to another software loses the tuning. For audio-out distribution, bounce-to-audio is the only reliable handoff.

## Third-party plugin compatibility

This is the practical hard edge. The [Live 12 Reference Manual on Tuning Systems](https://www.ableton.com/en/live-manual/12/using-tuning-systems/) is explicit: "instruments that are not MPE-enabled or use different pitch bend ranges are likely to play out of tune." Live 12 passes tuning information to third-party VST2, VST3, and AU instruments only if they are MPE-capable AND have their pitch bend range set to **48 semitones**. Most popular synths (Serum 2, Vital, Pigments, Phase Plant, U-he Diva/Repro/Hive, Arturia V Collection) support MPE and tunings if configured correctly. Plugins without MPE support (older instruments, many sample libraries, anything that ignores per-note pitch bend) will play in standard 12-EDO regardless of Live's project tuning. The [Sound on Sound Live 12 Tuning Systems article](https://www.soundonsound.com/techniques/ableton-live-12-tuning-systems) recommends testing each third-party instrument with a long tonic note and checking the pitch on a tuner before committing to a project.

## The Microtuner Max for Live device — when to reach for it

The [Microtuner pack](https://www.ableton.com/en/packs/microtuner/) is a free Ableton-published MIDI device that predates Live 12's native tuning system support. It still ships and is worth understanding because it complements the project-level system. Microtuner is a MIDI effect placed before an instrument — it intercepts incoming MIDI notes and translates them into pitch-bend-modified output that the downstream instrument plays. Microtuner offers per-device tuning (one Microtuner per track lets you have different tunings on different tracks within a project), Lead/Follow modes for syncing tunings across multiple instances, polyphonic and MPE modes, and MTS-ESP integration. Use cases where Microtuner beats the project-level tuning system: multiple tunings in one project, real-time tuning changes during performance, syncing with MTS-ESP clients, working with non-MPE third-party plugins (Microtuner sends pitch-bend that even non-MPE plugins respond to).

## Limits and gotchas

Several practical limits to name. First, the project-level tuning system requires Live 12.0+ — older Sets won't load with tuning information when opened in Live 11. Second, recording MIDI from a controller produces MIDI note numbers, and those numbers are interpreted through the active tuning at playback — so a tonic recorded under one tuning will play at a different pitch if the tuning is later changed (which is usually the point, but can surprise the user). Third, MIDI export strips tuning information. Fourth, drum racks where the pads play non-pitched samples are unaffected by tuning (this is the intended behavior — kick drums don't get retuned to 19-EDO). Fifth, latency may be slightly higher with tuning active on some third-party plugins as the host translates MIDI notes into pitch-bend-adjusted output. Sixth, alternate tunings with more than 12 notes per octave still use the standard MIDI note grid in the piano roll — composing in 19-EDO means thinking about which MIDI note number corresponds to which step in the tuning, which is non-obvious until the user maps it.

## Cited Retrieval Topics

- "how do i use a microtonal tuning in ableton live 12"
- "what's the difference between .scl and .ascl files"
- "can i use just intonation in ableton live 12"
- "do third party plugins work with live 12 tuning systems"
- "how do i load a scala scale into ableton live 12"
- "which built-in instruments support tuning systems in live 12"
- "can i have different tunings on different tracks in live 12"
- "how do i compose in 19-edo in ableton"
- "what's the difference between scale and tuning in live 12"
- "do drum racks get retuned by tuning systems in live 12"

## Sources

- [Ableton Live 12 Reference Manual — Using Tuning Systems](https://www.ableton.com/en/live-manual/12/using-tuning-systems/)
- [Ableton — All new features in Live 12](https://www.ableton.com/en/live/all-new-features/)
- [Ableton — Live 12 Release Notes](https://www.ableton.com/en/release-notes/live-12/)
- [Ableton — Microtuner pack](https://www.ableton.com/en/packs/microtuner/)
- [Sound on Sound — Ableton Live 12 Tuning Systems](https://www.soundonsound.com/techniques/ableton-live-12-tuning-systems)
- [CDM — Ableton Live 12: a guide to everything that's new](https://cdm.link/ableton-live-12-everything-new/)

## See also

- `corpus/daw/ableton/live-12/scale-aware-midi-and-global-scale.md` (C2 — scale awareness, the layer above tuning)
- `corpus/daw/ableton/devices/wavetable-drift-meld-synths.md` (B10 — the most tuning-aware Live synths)
- `corpus/daw/ableton/devices/operator-analog-synths.md` (B9 — Operator and Analog tuning behavior)
- `corpus/harmony/voice-leading-for-songwriters.md` (general harmony context)

# corpus/daw/ — DAW-Specific Knowledge

This directory holds **DAW-specific** corpus files. Files here describe how a particular DAW does a thing, not the DAW-agnostic principle behind it. The general corpus (`corpus/{recording,mixing,mastering,synthesis,sampling,rhythm,structure,harmony,melody,lyrics,workflow}/`) covers the principles; this directory covers the implementations.

The split exists because ARLO needs to advise differently depending on what the user has open. A question like *"how do I sidechain a kick to bass"* gets a DAW-agnostic recipe from the general corpus AND a DAW-specific implementation file from here.

## Streams

| Stream | Folder | Target | Status |
|---|---|---|---|
| Ableton Live 12 (macOS) | `corpus/daw/ableton/` | Live 12.x current | 📋 Planned — see `DAW-ABLETON-RESEARCH-PLAN.md` at repo root |
| Logic Pro 11 (macOS) | `corpus/daw/logic/` | Logic Pro 11.x | Future — seeded by the Logic parity map in `corpus/daw/ableton/reference/ableton-to-logic-parity-map.md` |
| FL Studio | `corpus/daw/fl/` | Future | Not yet planned |
| Pro Tools | `corpus/daw/pro-tools/` | Future | Not yet planned |
| Bitwig | `corpus/daw/bitwig/` | Future | Not yet planned |

## Per-stream structure

Each DAW stream is organized by area. The Ableton stream uses:

```
corpus/daw/ableton/
├── workflows/    ← Fundamental Live workflows (Session/Arrangement, racks, recording, routing)
├── devices/      ← Stock device families (EQ Eight, Compressors, Reverbs, synths, samplers)
├── live-12/      ← Live-12-only features (modulators, scale-aware MIDI, MIDI Generators, etc.)
├── patterns/     ← Production patterns (vocal chains, drum bus, parallel comp, sidechain)
├── editing/      ← Comping, warping, slicing
├── friction/     ← Diagnostic flows (silent track, monitoring loop, CPU, latency, crash recovery)
├── reference/    ← Keyboard shortcuts, Logic parity map
└── timeless/     ← Pre-Live-12 producer wisdom verified to still work in Live 12
```

Logic and other future DAW streams should mirror this convention with the equivalent area folders.

## Provenance and version-stamping

Every file in this directory is tagged with the DAW version at the time of research:
- Front-matter `Source:` line includes the version (e.g., `Deep-research synthesis (2026-05) — Ableton Live 12.x`)
- Inline claims about features/devices name the version they shipped in (e.g., "Hybrid Reverb (Live 11+)", "the Envelope Follower modulator (Live 12+)")

This discipline matters because DAWs ship breaking changes. When Live 13 arrives, a regex search across this directory identifies every Live-12-only claim that needs re-verification.

## Cross-references to the general corpus

Files in this directory cross-link to the general-corpus DAW-agnostic foundation via a `See also:` footer. Examples:

- `corpus/daw/ableton/patterns/vocal-chains-in-live.md` → `See also: corpus/mixing/vocal-mixing.md`
- `corpus/daw/ableton/timeless/resampling-discipline.md` → `See also: corpus/sampling/chopping-resampling-and-warping.md`
- `corpus/daw/ableton/devices/operator-analog-synths.md` → `See also: corpus/synthesis/fm-and-wavetable-synthesis.md`

The pattern: DAW-agnostic concept lives in the general corpus; DAW-specific implementation lives here. ARLO retrieval gets both layers.

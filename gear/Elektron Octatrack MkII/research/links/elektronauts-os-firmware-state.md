https://www.elektronauts.com/t/octatrack-os-1-40-bug-reports/143259
elektron.se · OS 1.40B readme (2024-09) + "Octatrack OS 1.40C" thread /217914 + "came with 1.40B" /186239 + CDM 1.4 writeup

# Firmware / OS state — mature and effectively frozen

The Octatrack is a fully mature, slow-cadence platform. **OS 1.40 (Dec 2020) was the last MAJOR feature update**; everything since is maintenance.

## Version timeline (as of 2026)
- **1.40** (Dec 2020) — the big one (features below).
- **1.40A** (Dec 17 2020) — quick bugfix; LAUNCH builds had real issues (see below).
- **1.40B** (readme dated 2024-09) — maintenance/production-process release; widely regarded as the **mature stable build**; many units shipped with it.
- **1.40C** — newest; ships on current units; "support for updated production process," essentially no user-facing changes. No feature additions.
- Across this whole arc there are **no MkII-exclusive features** — all OS capabilities run on MkI too.

## What OS 1.40 ADDED (the last creative update — worth knowing)
- **MIDI Trig Modes** — an external MIDI keyboard/pads can now PLAY slices and sample slots live and record them into the sequencer (huge for the 61SL MkIII driving the OT chromatically).
- **Tempo per Pattern** — independent BPM per pattern within an arrangement.
- **Parameter Randomization (the "dice")** — `[TRACK PARAM page] + [YES]` randomizes that page's params; `[TRACK PARAM] + [NO]` reloads saved values. Fast happy-accident generator.
- **P-lock multiple trigs at once** — hold several trigs, lock once; also multi-trig copy/paste/clear, microtiming, sample locks.
- **Trig Preview** — in grid record, `[TRIG] + [YES]` previews a step (with its p-locks) to main, `[TRIG] + [CUE]` to cue. Audition before you commit.
- **MkII display brightness** in PERSONALIZE.

## Stability / known bugs (mostly the 1.40/1.40A launch window — largely settled by 1.40B)
- Reported at launch: rare **project corruption / encoder freeze** (all encoders locked, pattern loss); **random lockups** (notably on the LFO page) needing a power cycle; a **scene-display bug** (A2 shown as A10); intermittent **LFO-not-modulating-CC**, knob value not refreshing until reload, occasional unresponsive trig buttons, sound cutting out on a track until edited; the persistent **"DUB ABORTED"** pickup error.
- Consensus by 2026: **1.40B/C are solid.** Standard precautions still apply: **back up the CF card before any OS update, never update right before a gig**, and Save Project before pulling the card.

https://midi.guide/d/hologram/microcosm/
midi.guide (community MIDI reference) · cross-verified against pencilresearch/midi GitHub CSV and Hologram MIDI docs · accessed 2026-06

# Microcosm full MIDI CC + Program Change map (verified)

Cross-checked between midi.guide and the pencilresearch/midi GitHub CSV — the two agree. The Microcosm **listens on Ch 1 by default** and **echoes its MIDI IN to its MIDI OUT** (so one cable can clock + control a daisy chain).

## Control-Change (CC) map — the eight knobs + secondaries
| CC | Function | Notes |
|---|---|---|
| 5 | Subdivision | 0–31 = 1/4, 32–63 = 1/2, 64–95 = TAP, 96–111 = 2x, 112–127 = 4x |
| 6 | **Activity** | density/complexity |
| 7 | **Shape** | envelope contour |
| 8 | **Cutoff** | low-pass filter (knob = FILTER) |
| 9 | **Mix** | dry/effect balance |
| 10 | **Time** | subdivision or global tempo |
| 11 | **Repeats** | effect duration/frequency |
| 12 | **Space** | reverb/delay wet mix |
| 13 | **Loop Level** | looper playback volume |
| 14 | Frequency | pitch-mod RATE (Shape secondary) |
| 15 | Resonance | filter resonance (Filter secondary) |
| 16 | Volume | effect MASTER VOLUME (Mix secondary — the "effect volume" hidden control) |
| 17 | Looper playback speed (continuous) | vari-speed |
| 18 | Looper playback (stepped) | |
| 19 | Depth | pitch-mod DEPTH (Repeats secondary) |
| 20 | Reverb mode | 0–31 Bright Room, 32–63 Dark Medium, 64–95 Large Hall, 96–127 Ambient (Space secondary) |
| 21 | Loop fade time | (Loop Level secondary) |

## Looper CCs
| CC | Function |
|---|---|
| 22 | Looper On/Off (0–63 off, 64–127 on) |
| 23 | Playback direction (0–63 fwd, 64–127 reverse) |
| 24 | Routing (0–63 Post-FX, 64–127 Pre-FX) |
| 25 | Looper Only mode |
| 26 | Burst mode |
| 27 | Quantize |
| 28 | Record |
| 29 | Play |
| 30 | Overdub |
| 31 | Stop |
| 34 | Erase |
| 35 | Undo |

## System / footswitch CCs
| CC | Function |
|---|---|
| 45 | Preset Copy |
| 46 | Preset Save |
| 47 | Reverse effect |
| 48 | **Hold Sampler / Freeze** (0–63 off, 64–127 on) — you can MIDI-trigger the freeze! |
| 93 | Tap Tempo |
| 102 | Bypass (0–63 bypass, 64–127 engage) |

## Program Change (preset/engine recall)
- **PC #1–44** = the 44 effect variations (11 engines × A–D).
- **PC #45–60** = the 16 user presets (4 color banks × 4).
- **No CC for preset increment/decrement** — to scroll presets you must drive PC numbers from a counter on the controller (see Morningstar thread capture).

## Rig-relevant takeaways
- **CC 48 = remote Freeze.** The Digitakt (or a Morningstar) can trigger/release the Hold Sampler in time with a song — freeze a drone on a downbeat without a footswitch.
- **CC 16 = effect master volume** is the level-match knob for taming a hot fuzz wall feeding in; it's a hidden secondary (Shift+Mix) on the hardware.
- **CC 5/CC 20 are stepped value-zones**, not smooth — send the band center (e.g. 96 for Large Hall reverb), not edge values.

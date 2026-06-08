https://patchstorage.com/wayward/
Patchstorage · son_wu (Empress ZOIA / Euroburo) · accessed 2026-06-03

# WAYWARD — ZOIA recreation of the Onward Glitch section
Companion control patch: https://patchstorage.com/cba-lab-a-laboratory-for-controlling-chase-bliss-audio-pedals/

Not a preset recipe, but the most useful **community control map** for the Onward's Glitch engine — included because it documents the exact parameter set and CC layout someone reverse-engineered from the manual, which doubles as a cheat-sheet for what to tweak.

## What it is
- **Platform:** Empress **ZOIA / Euroburo**. Creator **son_wu**. ~1,547 downloads (WIP state).
- A recreation of **the Glitch section of the Onward**, *"made as close to the original, so it's easy to understand by reading ONWARD's manual."* All controls reachable on page 1; per-channel error types via output switches at the bottom.

## The control map (its MIDI CC assignments — the useful part)
| CC | Param |
|---|---|
| 70 | Fade |
| 71 | Size |
| 72 | Mix |
| 73 | Octave |
| 74 | Error type |
| 75 | Error strength |
| 76 | Sustain |
| 77 | Sample-rate reduction |

⚠️ These are **son_wu's own ZOIA CC choices for the clone**, NOT the real Onward's MIDI CC map. For the actual Onward MIDI CCs (SIZE = CC14, the CC102–109 footswitch/retrigger map, dip-switch CCs, etc.) use the verified table in `Gear/Chase Bliss Blooper/research/links/cb-stack-preset-scene-recall.md` §4.

## Why it's here
The list above is a concise inventory of the Glitch side's *sound-shaping parameters* (Fade, Size, Mix, Octave, Error type/strength, Sustain, sample-rate reduction) — a quick reference for which knobs actually move the glitch character, confirmed by someone who rebuilt it from the manual. Also a free way to audition Onward-style glitch on a ZOIA before committing the bench pedal to a board.

**CBA lab** (same Patchstorage author space) is a generic ZOIA patch for MIDI-automating all six knobs of any CBA pedal via configurable modulation sources — relevant if you want grid-aligned modulation of the Onward beyond its onboard ramping.

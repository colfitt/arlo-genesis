https://www.manualslib.com/guide/4257002/hologram-chroma-console-multi-effect-pedal-user-manual.html
manualslib.com (Chroma Console manual mirror) · Hologram Electronics manual · accessed 2026-06-03

# Chroma Console — MIDI implementation + button-combo map (from manual)

## MIDI CC numbers (secondary controls), confirmed from manual
- **SENSITIVITY** — CC# 72 (0–127)
- **EFFECT VOL (Character)** — CC# 73
- **DRIFT (Movement)** — CC# 74
- **EFFECT VOL (Movement)** — CC# 75
- **DRIFT (Diffusion)** — CC# 76
- **EFFECT VOL (Diffusion)** — CC# 77
- **OUTPUT LEVEL** — CC# 78
- **EFFECT VOL (Texture)** — CC# 79

(Primary-knob CC numbers — TILT/RATE/TIME/AMOUNT×4/MIX — exist in the full MIDI chart but were not captured in this excerpt; consult the on-disk manual's MIDI table for the complete map. v1.04 firmware ALSO added per-module **bypass/engage** CCs — see firmware-page capture.)

## MIDI clock
- Syncs time-based effects (Vibrato, Phaser, Tremolo, Cascade, Reels, Collage, Reverse) to external MIDI clock.
- Clock source modes: **Auto (default, prioritizes USB)**, **USB-only**, or **DIN-only**.
- Returns to **internal clock** when it receives a MIDI **Stop** message or loses the external clock signal. (Relevant for the rig: the Digitakt 2 is clock master — if the Digitakt stops, the Chroma falls back to its own tap/internal tempo, so gestures/delays will keep running but unsynced.)

## Button-combo map (the "hidden" control deck — easy to forget)
- **A + D** (the two outer buttons) → **FX SETUP** (reorder the 4 modules; FILTER style; capture PRE/POST routing; dual-bypass assignment).
- **A + B** (first two) → **SECONDARY CONTROLS** (SENSITIVITY, DRIFT ×2, OUTPUT LEVEL, EFFECT VOL ×4).
- **B + C** (middle two) → **COPY / SAVE** (save preset; copy gesture/capture).
- **C + D** (last two) → **GESTURE** record mode.
- **All four buttons** → **GLOBAL SETTINGS** (bypass mode, preset-browser audition, clock source, calibration, etc.).

## Honesty flag
- The manual excerpt did NOT list explicit **Program Change** numbers for the 80 presets; PC recall is supported (presets are PC-recallable) but the exact PC→preset mapping should be confirmed against the on-disk manual's MIDI section. (Treat "PC n = preset n" as unverified until checked.)

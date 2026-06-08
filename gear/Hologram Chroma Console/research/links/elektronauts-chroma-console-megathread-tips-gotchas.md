https://www.elektronauts.com/t/chroma-console-hologram-electronics/202802
elektronauts.com · Hologram Chroma Console mega-thread (33+ pages) · 2024–2025 (page 29 sampled)

# Elektronauts Chroma Console mega-thread — community tips & gotchas

The single richest community thread (Elektron/synth-leaning user base — directly relevant to a Digitakt-clocked rig). Highlights distilled:

## Confirmed gotchas / bugs
- **REVERSE "DRIFT" appears inert.** User `funktree` (Oct 1, 2024): the DRIFT secondary on REVERSE (Diffusion) — "cannot hear the difference." Confirmed by `sicijk` (Oct 3): "Even for me drifting the Reverse doesn't produce anything noticeable." → Don't rely on DRIFT to animate a REVERSE patch; use a recorded GESTURE on TIME instead.
- **Secondary-knob positions are NOT remembered per-effect (early firmware).** `funktree`: adjusting DRIFT for one effect carries the value over to other effects in the same module/row — you must re-set it via the secondary menu when you switch effects in that module. (Plan around this when scene-switching; it may be improved in later firmware — unverified.)
- **One effect per module, hard limit.** `sicijk` (Oct 3): you cannot chain two effects from the same module — e.g. COLLAGE and SPACE/CASCADE/REELS/REVERSE all live in DIFFUSION, so you can't run COLLAGE *and* SPACE at once. This caps some "ethereal" stacked-time designs. Workaround: use the H90/Big Sky downstream for the second time-voice.

## Tempo / clock notes
- `funktree`: "slight flashes indicate internal tempo," and "most of the effects from row 2 and 3 [Movement + Diffusion] are sensitive to tap tempo" — i.e. modulation + delay effects are the clock-syncable ones (matches the manual's clock list).

## Community tool surfaced here
- **Max-for-Live editor** posted by `chapelierfou` (Oct 4, 2024) with randomizers, parameter visualization, and program recall; `infiniteposse` called it "beautiful" for managing presets visually. (See separate maxforlive capture.)

## Support
- Official support: support@hologramelectronics.com (shared by `Tajnost`). Hologram is responsive to bug reports in this thread.

## Why follow this thread
Elektron-forum audience = lots of MIDI-clock / Digitakt integration talk, preset-editor development, and firmware-bug reporting. Best place to track future firmware behavior and undocumented quirks.

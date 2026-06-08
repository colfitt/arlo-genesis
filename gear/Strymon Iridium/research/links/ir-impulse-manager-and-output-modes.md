# Iridium IR system & AMP DISABLE — authoritative workflow (Settings+Demos facet)

> Output-mode placement/stacking lives in `stack-placement-output-modes.md` (integration facet). The brief output-mode recap below is kept only for self-containment; that file is the authority for rig wiring.

Sources (Strymon official):
- Impulse Manager + Iridium: https://www.strymon.net/faq/using-strymon-impulse-manager-with-iridium/
- Disable amp/cab on Iridium: https://www.strymon.net/faq/how-can-i-disable-the-amp-or-cab-on-iridium/
- Impulse Manager support hub: https://www.strymon.net/support/impulse-manager/
- Video: Strymon "Impulse Manager for Iridium" (official, 2020) https://www.youtube.com/watch?v=B_G9kV3fwOo
- Video: Westbrook "Impulse Manager Tips & Tricks" (deep) https://www.youtube.com/watch?v=SpsO9cB6EOI  (transcript: ../transcripts/westbrook-impulse-manager-tips.md)

## Loading custom IRs (Impulse Manager)
- IR file spec: 24-bit / 96 kHz WAV, up to 500 ms. Per cab slot you can load 2 mono files (one LEFT, one RIGHT) OR 1 stereo file.
- Connect Iridium via the included USB-mini cable (pedal must be powered); launch Strymon Impulse Manager; it auto-detects the pedal.
- Left column = browse your drive for compatible IRs. Drag-and-drop into the LEFT, RIGHT, or MONO (center) section of any of the 9 cab slots.
- Per-side INFO ("i") gives LEVEL + general TREBLE/BASS trim to balance mismatched IRs.
- Hit SYNC CHANGES to write to the pedal. Save Collections → stored at /Users/<user>/Documents/Strymon/collections (Mac & Win).
- "Load ANY 24/96 WAV up to 500 ms" trick: bass cabs, acoustic body resonance, even short samples — turns Iridium into a general convolution loader (combine with AMP DISABLE below).

## Output Modes (global; set by HOLD ON footswitch at power-up, then turn DRIVE to choose)
Per Strymon's current FAQ, the ON LED takes the color of the active mode:
- RED  = Amp + Cab BOTH ON (default / "Normal"). Full amp + IR cab + room.
- GREEN = AMP BYPASS — amp modeling OFF; CAB + ROOM stay on. Use to run an EXTERNAL preamp/drive pedal (or a load-box'd amp FX send) INTO the Iridium's IR engine. (= "load an external preamp into the IR cabs.")
- AMBER = CAB BYPASS — IR cab OFF; AMP + ROOM stay on. Use to feed a REAL power amp / FX return / cab (the amp model with no speaker sim).

NOTE on naming vs. the dossier: the dossier §2/§13 used "Cab Bypass = amp+room, no cab" and "Amp Bypass = cab+room only" — those FUNCTIONAL descriptions are correct, but Strymon's FAQ labels them the OTHER way around relative to which block is bypassed (GREEN "Amp Bypass" = amp removed → cab+room; AMBER "Cab Bypass" = cab removed → amp+room). The LED colors above are the authoritative reference. Net behavior matches the dossier; only the GREEN/AMBER label-to-color mapping is the precise bit to trust here.

## AMP DISABLE (firmware 1.32+, Oct 2023) — distinct from output modes
- A Live Edit function that runs CAB + ROOM on a NON-guitar source with the amp model disabled (e.g. a synth, drum bus, or a bass DI) — i.e. pure IR convolution + room on any input.
- Combined with custom-IR loading, this is the "Iridium as a stereo convolution box" use case. For this rig: load a bass-cab 24/96 IR + AMP DISABLE = clean Jazz Bass DI with a real cab IR and room.
- 1.32 also made LEVEL TRIM persist across power cycles. Latest firmware: Rev 1.33 (Nov 2024).

## Stereo IR craft (from the Westbrook tutorial)
- Each slot can hold a DIFFERENT mono IR L vs R → build a custom 2x12 (two speakers, or one speaker / two mics, e.g. SM57 + Royer 121). Wider, fuller stereo image.
- Balance brighter side back to center with the per-side level/treble/bass trim.
- Mix IRs from the SAME vendor to avoid phase issues; cross-vendor blends often phase-cancel.
- Mono/centered = drop one IR in the CENTER slot (safe for FOH summing).
- Solo wide trick: in a DAW, delay a mono IR 9 ms, consolidate to 500 ms, load delayed-vs-original L/R (do NOT use if summed to mono).

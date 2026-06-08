Manual: SL MkIII V2 pp.19–22, 28, 32–35 (CV/Gate, Host ports, InControl)
Novation manual

# RECIPE — MIDI-to-CV bridge (modular) + soft-synth master keyboard

## A) MIDI-to-CV bridge for analog/modular gear
1. **Calibrate first** (Global → CV Calibration): per port, CV Low = 220 Hz (A2), CV High = 880 Hz (A4), tune to a VCO, **Apply**. (See `cv-gate-mod-calibration.md`.)
2. **Patch:** CV1 → VCO 1V/oct in; Gate1 → envelope/gate in; Mod1 → filter cutoff / VCA CV; Clock Out → modular clock-in.
3. **Route a Part to CV/Gate 1** (Shift+Sessions → CV/Gate = 1). Keybed or sequencer plays the **mono last-note** voice; Gate is high while held.
4. **Mod1:** Global set **Mod 1 CC** = the CC you'll send + **Mod 1 Range** = −5/+5V or 0/+5V. Map a **fader/encoder/aftertouch** to that CC in the Template → real-time filter/VCA voltage. Sequencer automation on that CC also drives Mod1.
5. **Pitch Bend to CV:** Global, set ±2 semis for playable bends out the CV pitch port.
6. **Clock Out PPQN:** match the modular (commonly 1 PPQN; up to 24).
7. **From the DAW:** the host "To CV/Gate" port plays the modular too — **MIDI ch.1 → CV/Gate 1, ch.2 → CV/Gate 2**, CC-matching-ModCC → Mod port. So Logic/Ableton can sequence the modular through the SL.
- **Limit:** each CV voice is **monophonic, last-note** — two voices max (CV1+CV2). Plan mono lines/drones, not chords.

## B) Soft-synth master keyboard (the daily driver — Logic / Ableton)
- **Standard MIDI mode** (not InControl): USB to Mac, **Part 1 → USB, Ch1**, play **Kontakt/Komplete 15 / Arturia V Collection 11** on the armed DAW track.
- **Velocity curve** Normal/Normal+ (Global); **aftertouch → CC1 (mod)** or a filter CC for expression.
- **Zones** to split: e.g. low octave → a bass Part/synth, upper → pad (each Zone = own Dest Part, key range, octave/transpose, and per-zone enable of pitch/mod wheel, aftertouch, pedals). Overlapping zones = layered sounds.
- For **hands-on device control + transport + mixer**, switch to **InControl** (Ableton = clip launch + device banking; Logic = device + Smart Controls). See `incontrol-ableton-setup.md` / `incontrol-logic-reason-setup.md`. Remember: standalone-sequencer ↔ InControl is a **hard mode toggle** — pick one transport per session.
- **No Automap** → deep per-plugin auto-mapping is gone; use the DAW script's device banking, or a standard-MIDI Template + the plugin's own MIDI-learn.

## Combining A + B
One Session can have Part 1 → USB soft-synth (play in Logic/Ableton), Part 2 → CV/Gate 1 (modular mono voice), Part 3 → DIN (a pedal/Elektron), all clocked by the SL as master. The SL genuinely plays + sequences + clocks + CV-bridges the rig from one keybed — its whole reason for being off-board.

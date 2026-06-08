Manual: SL MkIII User Guide V2, pp.19–21 (CV Mod Range/CC, Pitch Bend to CV, CV Calibration, CV/Gate)  +  https://userguides.novationmusic.com/hc/en-gb/articles/25626767118994-Using-the-SL-MkIII-s-CV-and-Gate-connections
Novation manual + Novation CV/Gate user guide (article 403s to auto-fetch; verified against manual)

# CV / Gate / Mod — the rig's only MIDI-to-CV bridge

## The ports (7× 3.5 mm TS jacks)
**Clock Out, CV1, Gate1, Mod1, CV2, Gate2, Mod2.** Two complete CV-pitch + Gate + Mod voices.

## Pitch CV (the note voltage)
- **MIDI notes 24–108 → 0–7 V** linear pitch range. Notes outside 24–108 **clamp** to min/max.
- **MONOPHONIC, last-note priority** — the poly stream from keybed/sequencer/MIDI collapses to the most-recently-played note. Plan mono basslines/leads/drones, not chords, per CV voice.

## Gate
- Goes **high (open)** while any note is active on that voice, falls **low (closed)** when all notes released. = gate-while-held. Pair with the CV pitch for a standard 1V/oct-style mono voice (after calibration).

## Mod outputs (CC → voltage)
Each Mod port is a **CC-to-voltage** converter, configured in **Global**:
- **CV Mod 1 CC / CV Mod 2 CC** — set the **CC number** each Mod port listens to (per port, via rotary).
- **CV Mod 1 Range / CV Mod 2 Range** — output voltage range: **"−5 to 5 V"** or **"0 to 5 V"**.
- When a Part routed to that CV/Gate voice outputs that CC (from a surface control, sequencer automation, or incoming MIDI), it appears as voltage on the Mod port. (Note: manual's CV/Gate page says 0 to +5V for Mod; the Global range setting offers the −5/+5V option — set per use.)
- Use Mod for filter cutoff, VCA, or any modular CV destination; map it to a fader/encoder/aftertouch in the Template for hands-on control.

## Pitch Bend to CV
- **Global** setting: both CV outputs can react to the **Pitch Wheel**, range selectable **±1 semitone to ±12 semitones (±1 octave)**. Set ±2 for natural playable bends.

## CV Pitch Calibration (do this first, per port)
Global → page down to **CV Calibration** → soft button **Calibrate**:
1. Press **CV 1 Low** (or CV 2 Low) — sets the port to ~**220 Hz (A2)**. Connect the port to your VCO/sound source; tune by ear, by tuner, or read on an oscilloscope.
2. Turn the **Tune** knob until the output is **exactly 220 Hz**.
3. Press **CV 1 High** (or CV 2 High) — repeat for **880 Hz (A4)**.
4. Press orange **Apply** to save. (**Reset** = restore factory cal; **Exit** = back to Global.)
The full pitch range then calibrates from those two anchor points. Recalibrate per destination VCO if tracking drifts.

## Routing a Part to CV/Gate
- **Shift + Sessions** (Part Settings) → set that Part's **CV/Gate** destination to **1**, **2**, or **Both**. Notes on the Part now drive the chosen voice; the Part's CC (matching the Mod CC) drives Mod.
- From the **host/USB "To CV/Gate" port**: MIDI **ch.1 → CV/Gate 1, ch.2 → CV/Gate 2**; CC matching a Mod-CC → that Mod port (lets the DAW play the modular through the SL).

## Clock Out PPQN (analog sync to modular)
- Global **Clock Out PPQN**: **1 / 2(default) / 4 / 8 / 24**. Match the modular's clock-in expectation (commonly 1 PPQN = quarter-notes for Eurorack; some want higher). Pulses send while transport runs.

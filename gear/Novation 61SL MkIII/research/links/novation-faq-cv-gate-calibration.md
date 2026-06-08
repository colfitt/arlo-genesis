https://support.novationmusic.com/hc/en-gb/articles/360002860659-How-to-Calibrate-the-Pitch-and-Mod-Wheels-on-SL-MkIII
support.novationmusic.com + userguides.novationmusic.com (CV & Gate guide) · official KB · current
(KB pages 403 WebFetch — distilled from search snippets quoting the official text)

Concrete CV/Gate/Mod setup + the calibration procedure. This is the MIDI-to-CV bridge the rest of the rig has no other source for.

## CV pitch
- **MIDI notes 24–108 → 0–7 V** pitch CV (1 V/oct). Notes outside the range clamp.
- **CV/Gate is MONOPHONIC.** The poly note stream (keys + sequencer + incoming MIDI) collapses to a **last-note-priority** mono voice per CV pair. Two CV/Gate/Mod pairs = two independent mono voices.

## Calibrate the pitch CV (do this before trusting tracking)
1. **Global** button → Up/Down arrows to the **CV** options.
2. Press the soft button for **CV1 Low** (or CV2 Low). Set the **low reference = 220 Hz (A2)** — fine-tune with the **Tune** knob.
3. Repeat for the **high** point and match **880 Hz (A4)**.
4. Verify by ear/tuner, or connect the CV out to an **oscilloscope / measuring device** for accuracy. (You must connect the port to a sound source or meter to calibrate.)

## Mod outputs
- Two Mod outputs, each set to **mirror one CC number** (Global: "CV mod 1 CC" / "CV mod 2 CC"). Controllable + sequenceable from any Part.
- Each Mod output independently switchable **bi-polar (−5/+5 V)** or **uni-polar (0/+5 V)**.

## Pitch-bend → CV
- Pitch-bend can drive CV (added in firmware 1.4); range configurable in semitones (dossier cites ±1 to ±12).

## Gate
- Gate goes high while a note is held (mono, follows the last-note voice).

## Rig use
- This is the ONLY MIDI-to-CV path in the rig. Calibrate both pitch ports once (A2/A4) and they hold. Use a Mod output (set bipolar for through-zero / filter FM-ish moves, unipolar for VCA/filter) assigned to an expressive CC; sequence it from a Part for evolving drone modulation. Clock Out for analog sync — but see the clock-drift file: keep Clock Out at 1 or 2 PPQN.

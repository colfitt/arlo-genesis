# GK-5 Calibration Profile — Gold Tone EBM-5 banjo

**Save as: GK SET SELECT slot 1, NAME "EBM5 BANJO"** (System → GK SETTING; GK SETTINGS persist through power-off, recall instantly when you switch instruments). This is the hard one — banjo on a divided pickup is off-label, so treat the numbers below as a *calibrated starting point*, not gospel. Grounded in the VG-800 GK SETTING parameter page (DISTANCE 10.0–30.0 mm, SENS 1–7 per string 0–100, SCALE presets, PU DIRECTION/POSITION); banjo-specific values are inference + the real-world "banjo tracks fine on a GK" corroboration.

## Mounting reality first (before any menu)
- EBM-5 is a **solidbody electric banjo** — flat top, so a GK-5 can mount like on a guitar. Use the included **shim spacers** to get the element close and *parallel* under all strings. Tracking quality is set in the physical install as much as in the menu.
- The **5th string** starts at the 5th fret with its own side peg. Mount the GK-5 in the bridge-area string run where all five strings pass over the element. The 5th still crosses the pickup zone down there — verify it physically sits over an element lane before trusting the menu.

## GK SETTING values (starting point)
| Parameter | Value | Why |
|---|---|---|
| GK TYPE | **GK-5** (or GK5KIT-6 if you used a 6-element kit and left one lane unused) | Match the physical pickup |
| SCALE | **ST (648 mm)** as a baseline | Banjo scale (~26–27") is close-ish to a long guitar scale; ST is the safe start. If high strings track sharp/wobbly, this is the knob — there's no banjo preset, so audition ST vs LP (628) and pick whichever tracks the open strings cleanest. *Inference — verify by ear.* |
| PU DIRECTION | **NORMAL** (cable exits 6th-string side) or REVERSE — match your physical mount | Wrong direction maps strings to the wrong lanes |
| DISTANCE 1–6 | **start ~12–14 mm**, raise per string if a string distorts/double-triggers | Banjo strings are bright and high-output; closer = hotter = more false triggers on fast transients. Back DISTANCE off (larger number) on any string that splats. |
| SENS (per string 1–6) | **start ~70–80**, then tune each string individually (see below) | Default sens wobbles even on a normal guitar (MusicRadar); banjo's fast bright attack makes this worse |
| GAIN | **2** (lower if strong picking distorts) | Banjo transients are spiky; lower global gain tames false-triggers |

## Per-string SENS method (do this with TUNER open, picking at performance strength)
1. Set all SENS to ~75. Pick each open string hard and watch the tuner/INST response.
2. **Too sensitive** (note doubles, octave-jumps, or "wobbles" on the attack) → **lower** that string's SENS in steps of 5.
3. **Too weak** (note drops out, takes two picks to trigger) → **raise** SENS.
4. Banjo's **bright, fast attack** is the wobble culprit. The fix order: (a) lower that string's SENS, (b) raise its DISTANCE a touch, (c) lower global GAIN, (d) if it still glitches on tremolo/roll picking, accept it as character into the fuzz wall rather than chasing perfection.

## The 5th-string drone problem (the signature headache)
- It's a **short, high-tension, high-pitched (G) string** that decays fast and may sit slightly off the element's ideal lane due to its 5th-fret origin.
- Symptoms to expect: octave errors, dropouts, or it tracking the wrong lane.
- **Workarounds, in order:**
  1. **Physical:** confirm the 5th physically crosses an element; nudge the GK-5 angle so it does.
  2. **SENS:** give string 5 its **own** value — usually **lower** than the others (it's hot and bright), often 55–65.
  3. **STRING MUTE 5** (in GUITAR-TO-MIDI) or **STRING LEVEL 5 = 0** (INST common, STRING/OTHERS page) to **mute the 5th from the model entirely** when it won't behave — you keep the real 5th-string drone via NORMAL MIX while the model ignores it. This is the pragmatic doom move: let the model voice the 4 melody strings, let the *actual banjo* 5th drone ring underneath.
  4. **POSITION LIMIT** won't help (it's fret-range, not per-string) — ignore.
- **Realistic expectation:** the 4 main strings will track well enough for leads/chords; the 5th is the one you'll most often *exclude from the model* and keep as a real drone. That's not a failure — it's arguably the better musical result for this rig.

## What tracks well vs poorly on the banjo (set expectations)
- **Well:** single-note melody/lead on the 4 main strings, sustained-model patches where you mask the attack glitches (VIO, ORGAN, SLOW GEAR), and anything feeding a fuzz/granular chain that *wants* artifacts.
- **Poorly:** fast rolls into clean polyphonic SYNTH (GR-300 chords), big bends, and the bare 5th string into sustain patches. Don't fight these — route them to texture, or mute the offending string from the model.

## Companion settings (not in GK SET, but pair with this profile)
- INST common: **NORMAL MIX ON, ~20–40%** to keep the real banjo attack/5th-string drone under the model.
- GUITAR-TO-MIDI (if MIDI'ing out): PLAY FEEL **FEEL3–4** or **NO DYNA**, LOW VELO CUT **2–4**, HOLD **HOLD1** — see calibration-baritone for the shared MIDI logic.

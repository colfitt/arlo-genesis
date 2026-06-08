https://www.youtube.com/watch?v=9bJpBYmoUMw
youtube.com · "A Guide To Generative Sample Chains On Digitakt 2" · EZBOT (Matthew) · May 9 2024

# Generative Sample Chains on the Digitakt II — EZBOT (transcript, distilled to prose)

A complete, button-by-button DT2 walkthrough of building a sample chain from scratch and turning it into a generative slicer. All DT2. Cleaned from auto-captions; the concrete steps and shortcuts are reliable, light music passages omitted.

## Concept
A sample chain = several short samples evenly spaced along one longer sample (e.g. sample on trig 1, next on 5, 9, 13). Each sample's tail must end before the next begins so slices don't bleed. Slice the chain across a quantized grid (the GRID machine, formerly "Slice"), then *modulate the slice/sample position* so each sequencer step lands on a different slice — that's the generative engine.

## Step-by-step (button combos verbatim where given)

1. **Set track length.** FUNCTION + page to reach track scaling; FUNCTION + YES toggles **per-track scaling** (independent length per all 16 tracks — DT2 feature). Hold FUNCTION while turning an encoder to move in quantized groups of 16; or FUNCTION + up/down. He matches master and track to 64/64. Longer track scale + slower track SPEED = room for longer samples (DT2 can load much longer samples than the OG — OG max one-shot was 30 s).

2. **Collect sounds into the Preset Pool.** Hit the sound/preset (music-icon) browser → MANAGE → YES. Auto-audition sounds; check-box several short, *dry* sounds (he intentionally avoids ones drenched in delay so tails don't bleed into the next slice). Left-arrow → "Add to preset pool." Now they're recallable any time (hold the encoder to bring up the pool).

3. **Preset Keyboard mode** (DT2-only, "very similar to slots mode on the Octatrack, but playing presets"). FUNCTION + down → select PRESET POOL. Trig keys now play the pooled presets; left/right arrows page through them.

4. **Step-record jump** to lay the chain. RECORD, STOP, STOP enters step-record jump mode. It jumps across the keyboard by your **trig length** — with trig length at 1/4 it advances 4 steps per note, landing on 1, 5, 9, 13. Hold FUNCTION in step-edit mode and run across the pooled presets to place one per slice.

5. **Resample the track into one sample.** Set up sampling with SOURCE = the track you built (he's on track 11, so source = track 11). Arm with the **threshold = H encoder**, hit play/record, capture, SAVE (he names it "chain 1"), assign to a track (track 1), mute the source track.

6. **Load into GRID machine + de-click.** On the new sample track: trim the AMP envelope to basically HOLD/sustain so the sample cuts off cleanly at the end; a touch of OVERDRIVE to taste. FUNCTION + SRC → change machine to **GRID**. Set the grid divisions to match the number of samples in the chain (he uses 16). Now each step's slice position maps exactly to where each sample sat in the chain.

7. **Make it generative.** Put down steps; p-lock/modulate the **slice (sample-slice select) position** per step — or use the MODIFIER → "sample slice select" with **trigger condition RANDOM** so the slice chosen is random each pass. Lengthen trigs to taste, add more triggers, raise tempo, drop a drum beat behind it.

8. **Make it melodic in a scale.** FUNCTION + keyboard, change CHROMATIC → e.g. **Dorian**, set root (he uses G minor). In keyboard scale mode, **push the trig + push the encoder** to constrain note selection to scale notes only — assign each slice a random in-scale note for a generative melody.

9. **Finish.** Resample again if desired; he suggests throwing a **Comb filter** on the result for a metallic character.

## Why this matters for the rig
This is the canonical DT2 recipe for turning a pile of banjo/baritone one-shots (or fuzz-wall fragments) into a self-varying melodic/percussive generator — random slice + random in-scale note + conditional trigs = evolving, never-identical lines that suit drone/shoegaze beds. The "dry short samples, tails ended before next slice" rule is the practical key.

NOTE: button-combo names (RECORD/STOP/STOP, FUNCTION+SRC, threshold=H encoder, FUNCTION+keyboard) are as spoken in the video. "Slice" machine = "GRID" on current DT2 OS.

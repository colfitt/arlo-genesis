https://www.youtube.com/watch?v=pvR1gMepME0
Optoproductions (Melvin) · Digitakt 2 Creative Resampling · 2024-09-26

> Source captions: YouTube auto-generated, cleaned to prose. ~18m. DIGITAKT II specific. The core resampling/sound-design workflow: the DT2 sampling *itself* (the internal master bus) repeatedly to grow new sounds.

## Concept
The DT2 can sample its own output, not just external gear. Resampling = record the master (or a track) back into a new sample, then mangle, then resample again — a sound-design loop.

## Step 1 — make a source to resample
- Start with a basic project (drums + a bass patch sampled from the modular).
- Three level controls exist: AMP page level, SRC page level, and the track LEVEL encoder.
- Add a trig; on AMP set the envelope to **Attack/Hold/Decay**, turn HOLD all the way to **NOTE**, set note length to 16; add overdrive/distortion; pull DECAY down.

## Step 2 — resample the master bus
- SAMPLE page → **FUNC + (clear buffer)**. On the INPUT setting scroll all the way left past "left/right" to **MAIN INPUT** = the DT2's own master (everything you hear on PLAY).
- Raise level with the **Master Overdrive** (a touch), add **master compression**.
- Record e.g. 16 steps; arm the track; set record-on-play; press PLAY to capture the master.
- Save; name it (suffix "resample" so it's findable); FUNC + COPY copies the name to reuse. Assign to a track (e.g. 9).

## Step 3 — re-use and record the performance
- Go to a new pattern; reuse the same kit (Save Kit first, then Load Kit) and **note/match the BPM**.
- Turn off the compressor and master overdrive here (so you don't stack compression on compression).
- Enter notes; AHD envelope, decay down, note length 16.
- Play with **LENGTH + LOOP ON** to turn it into a granular/glitch sample; move the **loop point**.
- **Record the whole performance**: on SAMPLE page keep INPUT = MAIN INPUT, set sample LENGTH to Max, arm the track; press PLAY then go to the sample settings and twist controls live to capture all the movement. Stop, store as "resample 2" to another track (e.g. 9).

## Step 4 — slice & mangle the resample
- On the new track, switch SRC machine to **Grid**, set slices to 16, add an **LFO to slice-select** (SCE SELECT), increase depth, waveform = **random**, play with the LFO speed/multiplier and the grid LENGTH (4, 2) and grid size.
- Add a **high-pass filter**, raise resonance, add a second **random LFO → filter frequency**. Try **Comb filter** (hold FUNC + press machine) with high feedback for a powerful metallic tone; play with tempo.
- Add per-channel **overdrive / bit crushing** for "recorded-wrong" character.
- Resample again: SAMPLE → clear buffer → length 64 → arm → PLAY. Save. Can resample more variations (clear buffer, increase length, play again).

## Step 5 — slice the new resample into a playable instrument
- Switch SRC machine to **Grid**, set the trig mode to **Note**, add slices (16), enter keyboard mode to play the slices. FUNC + KEYBOARD → set keyboard mode to **Fold** for more notes. Raise level; add more overdrive.
- Lengthen the pattern *per track*: **FUNC + YES** for per-track length; change this track's LENGTH and RESET to 32 (then later 64), and fine-tune nudging notes left/right.

## Master glue / side-chain (closing)
- Master compression with **side-chain to the kick**: set compressor side-chain SOURCE = Track 1, then **exclude the kick from the compressor** via FUNC + setup → compressor routing → turn off Track 1 (so the kick triggers but bypasses).
- **Hold TRACK + turn a knob** applies the same change to all tracks at once (e.g. a master filter sweep or pitch/"beach" shift). Then change the pitch globally for effect.

Takeaway: "a really simple technique but very effective" — keep resampling the master, slicing, and re-mangling to spawn entirely new sounds.

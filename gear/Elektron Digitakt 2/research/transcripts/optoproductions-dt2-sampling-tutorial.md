https://www.youtube.com/watch?v=wi-DCA-uyO8
Optoproductions (Melvin) · Digitakt 2 Sampling Tutorial · 2024-07-18

> Source captions: YouTube auto-generated, cleaned to prose. ~30m. DIGITAKT II specific. Covers stereo sampling, the SRC playback machines (Oneshot/Werp/Stretch/Repitch/Grid), MIDI-machine sampling, and a full build. Note: recorded on early firmware — flags a mono-sampling bug since fixed (see Dave Mech OS 1.10 transcript).

## Early-firmware caveat (now resolved)
At time of recording the DT2 **could not sample in mono** — stereo-only. Workaround was a cable splitter or mixer to dual-mono a mono source. (Mono sampling was added in OS 1.10 — see davemech-dt2-os110-deep-dive.md.)

## Sampling setup
- Press SAMPLE. Two monitor options: listen to input **pre-** or **post-mix**. If post-mix, FUNC + MOD → mixer page 5 has an **input level** control. NB: the mixer "input" is a **monitor level only, not input gain** — set real levels at your preamp/synth.
- **Set the tempo first** (e.g. 125) — it determines how loops behave under the tempo-synced machines.
- Set record length (e.g. 64 steps ≈ 8 s).
- Two record modes: **Threshold** (gate — set threshold above the noise floor, arm, recording starts when signal exceeds it — best for one-shots/free playing) and **Play** (records on transport, with the metronome/pre-roll count-in; hold RECORD + PLAY for the count-in).
- Audition the buffer: **hold FUNC + YES**. Delete take: FUNC + NO. Click track + 2-bar pre-roll on the TEMPO page.
- Trim START/END, preview-loop with encoder D, zoom (FUNC = vertical zoom). YES saves + names; FUNC + COPY copies the name to reuse. Assign to a track. Sample stays in buffer until **FUNC + (clear/"now")**.

## SRC playback machines (auditioned on a recorded loop)
- **Oneshot** (default): plays from start; good for drum hits. To play a long loop you must lengthen the track (FUNC + PAGE for whole pattern, or FUNC + YES for this track only; set track length 64 and pattern RESET 64). Set AMP release/length so it doesn't cut.
- **Werp** (warp): lets you change tempo, but "really clicky" on sustained material — better for drum loops than tonal pads.
- **Stretch**: time-stretches the whole pattern length; some artifacts on tonal content.
- **Repitch**: turntable behaviour — lower tempo lowers pitch, **no artifacts**, but you can't change note independently. Good when artifact-free pitch-down matters.
- **Grid**: chops the sample into slices set by the LENGTH + GRID parameters (8/16/32/64 parts). LENGTH = how many slices play. Set trig mode to **Note** → keyboard plays slices. FUNC + KEYBOARD → **Fold** mode (starts in the middle); hold KEYBOARD-mode + down arrow to drop octaves (e.g. −4). Live-record slices: hold RECORD + PLAY (twice = quantized). Add release/attack, LOOP, adjust grid; add Overdrive.

## Sampling an external MIDI'd synth (Nord)
- Set a track to **MIDI machine** (FUNC + SRC → MIDI), pick a MIDI channel (hold FUNC + push encoder, change channel). Keyboard mode spreads the synth's drums across notes; black keys change settings.
- Make a MIDI pattern, then on SAMPLE set record mode to **Play** so it plays the MIDI notes *and* records them simultaneously; arm and record.
- Trim individual hits out of the recording (kick/snare/hat), saving each to its own track (1, 2, 3) — reuse the copied name. Clear the leftover MIDI pattern: in record mode, FUNC + CLEAR (NB: only the track's sequence if in record; whole pattern if not).
- Recover from a mistake: **FUNC + NO** reloads the pattern to last stored state; **FUNC + YES** stores a temporary state to return to.

## Build details worth keeping
- Conditional trig: hold a trig → set condition (e.g. **1:2** plays one of every two bars) for variation.
- Loop a pad sample (start/end/loop points); add reverb; **p-lock the start position** with a **random** value per step.
- **Bass via a loop + transpose**: record a one-note loop; set pattern length 64 with one trig and track length 16 → it repeats per bar; p-lock only the pitch of that single note per bar (much faster than locking every note). Switch machine Oneshot→Werp, set segment length, tweak.
- Per-track LFOs to sample-rate-reduction, etc. Add delay to hats; shorten kick with AHD envelope; add an LFO → pitch (saw/exponential, trig mode = trigger) for extra click.
- Snare reverb; AMP envelope as a transient designer (ADSR mode: cut tail, highlight attack).
- Master: master overdrive + compression; **side-chain compression** to the kick, excluding the kick from the compressor (FUNC + filter setup → compressor routing).
- **Hold TRACK + turn** = apply to all tracks; push NO to revert; RELOAD to recover.

Closing: a first-time DT2 user's verdict — workflow is "extremely quick", with free firmware updates expected.

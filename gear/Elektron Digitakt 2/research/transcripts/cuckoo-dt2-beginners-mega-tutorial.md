https://www.youtube.com/watch?v=651_lCCJ1-w
True Cuckoo · Digitakt 2 - Beginner's MEGA TUTORIAL · 2024-04-24

> Source captions: YouTube auto-generated, cleaned to prose. ~1h40m. Entirely DIGITAKT II (DT2) specific — Cuckoo repeatedly contrasts against the OG ("8x more storage", "stereo throughout", "twice the steps"). Highest-value single beginner-to-intermediate walkthrough.

## Memory architecture (DT2 numbers)
The DT2 stores everything on the **+Drive**. The +Drive holds: **20 GB of samples** (vs 1 GB on OG), **2048 preset slots**, and **128 kits** (Cuckoo says "124"; manual says 1024 kits — treat as "many"). A **project** holds the musical/sequencing data: 16 audio-or-MIDI tracks, the patterns, and a sample pool. Sample pool = **1016 usable sample slots** ("127 × 8 banks" — eight banks A–H of sample slots, 8x more than OG) and **400 MB of sample RAM** for playback. A project also has a **preset pool of 128 slots** for instant preset-locking at any trig.

Key concept: a sample loaded into a project is a **reference** to the file on the +Drive, not a copy. Delete the +Drive file and the project loses the sample. A **preset** = a sample plus all its track settings (filter, envelope, FX, sends, modulation). A **kit** = how all 16 tracks are set up together; every pattern has its own kit, so you can ignore kits entirely if you want.

## Panel orientation
- Master VOLUME (top-left) is **analog** — nothing in software reaches past it. If anything goes crazy, turn it down.
- 8 DATA ENTRY encoders correspond to the 8 on-screen parameters; positions match.
- Parameter pages: TRIG, SRC, FLTR, AMP, FX, MOD. Three dots on the screen edge = sub-pages (press the page button again, or up/down).
- FUNC (orange) accesses everything labeled orange: perform, quantize, sequencer, song, clear, paste.
- Trig keys: KEYBOARD off = play tracks; edit mode (RECORD lit) = program steps. **Watch the RECORD LED**: statically lit = editing the pattern; off = playing.
- Stop playback fully with a **double-tap of STOP** (single tap leaves long/looping samples ringing).
- Pattern address shown top-left, e.g. "C01" = Bank C, pattern 1. 8 banks × 16 patterns = 128 patterns/project.

## Building a first beat
1. Press RECORD to enter edit mode, place trigs on the 16 steps for the kick. Press PLAY.
2. Select snare track, repeat. Then hats.
3. **Live record**: hold RECORD + press PLAY (RECORD LED flashes = real-time recording). Top of screen shows "live rec unquantized". Tap RECORD+PLAY again to toggle **quantized**.
4. Metronome: press the TEMPO (metronome) button; bottom-left knob enables click; set time signature (e.g. 7/8), tempo (e.g. 128), and a **pre-roll** count-in (1 or 2 bars).

## Sound-shaping the kit
- **AMP page**: drum sounds default to **attack/hold/decay (AHD)** envelope; melodic sounds default to **ADSR**. Shorten HOLD/DECAY for tighter hits.
- **FX page** (per track): **Bit Reduction, Overdrive, Sample Rate Reduction**. Cuckoo: a snare's late tail gets "crazy" with bit reduction; two parameters (bit reduction + overdrive) entirely re-voice a snare.
- **SRC page sub-page 2** shows the waveform — one waveform = mono sample, two = stereo. Use to confirm stereo vs mono.
- Trim a one-shot: SRC sub-page has **START / LENGTH / LOOP**. Shorten LENGTH for a tighter hit.
- **FLTR page**: type knob sweeps low-pass → band-pass → high-pass on the default Multi-Mode filter. To get rid of competing low-mids on a synth, switch to high-pass. Filter has its **own envelope** (ENV DEPTH + attack/decay) so you don't need an LFO for filter motion.

## LFOs / modulation (MOD page — three LFOs per audio track)
- Three sub-pages = three LFOs. Per LFO: SPEED, fade in/out, DEST (destination), WAVEFORM, DEPTH, multiplier.
- Workflow: pick DEST (e.g. AMP DECAY), set DEPTH (nothing happens until depth ≠ 0), pick waveform.
- For **per-trig randomness**, set DEST to e.g. AMP DECAY with a RANDOM waveform; set the AMP DECAY value to a mid point because random sends both + and − values around it.
- Use a waveform with an **arrow icon** = LFO restarts on each key/trig press (one-shot trigger). Set speed slow so only the initial value is sent.
- Second LFO → SRC TUNE for pitch wobble. Build several modulations across the three LFOs per track.

## Pattern length / pages / polymeter
- **FUNC + PAGE** = page setup. Press PAGE again to double the pattern length; new pages are **copied** from the existing content (not blank).
- Navigate pages by **holding PAGE** then using arrows.
- **FUNC + YES** inside page setup = per-track independent length. Set e.g. Track 9 LENGTH to 32 while others stay 16. **Crucial gotcha**: also set the pattern RESET (shown right side, "reset at 16") to match the longest track or it never reaches the longer page.

## Sends & send-FX engine
- FX page hosts the three send levels: **Delay, Reverb, Chorus** (Supervoid reverb, Panoramic chorus, Saturator delay per dossier; Cuckoo calls them by generic names).
- **FUNC + (send effects)** enters the send-FX engine: make the delay stereo/wider, faster; tune the reverb DECAY longer for "epic" tails; set delay ping-pong L/R.
- P-lock a send on a single step: hold the step on the FX page, raise REVERB or DELAY send — that step alone gets the send (the trig blinks to show it carries a p-lock). Reset a p-lock by pressing the encoder for that parameter.

## Filter machines
- **FUNC + FLTR machine** swaps the filter per track: Multi-Mode, Lowpass (EQ), Comb. Cuckoo on **Comb**: "it's a tuned filter… actually fat" — turns a sample into a pitched/metallic resonator.

## Conditional trigs
- On the TRIG page, scroll the conditional knob to e.g. **1:2** (plays first of every two passes), so a part isn't identical every loop. "Very powerful for irregularity / making sequences come to life."

## Compressor / master (FUNC + MOD = mixer, 5 pages)
- Page with the **compressor**: dial WET in/out with the mix knob; raise THRESHOLD to be less aggressive; set ATTACK/RELEASE, MAKEUP GAIN, RATIO/LIMIT.
- **Side-chain filter** knob: dial up to ignore the kick's lows, or invert to react only to the kick+bass.
- True **side-chain**: set side-chain SOURCE to Track 1 (the kick) — ducks everything on each kick. Or use the external L/R input as the side-chain source.
- Tip: match output level dry vs compressed so you judge the compressor honestly, not just "louder = better".

## Patterns / performance
- **FUNC + COPY** copies the whole pattern (or the track sequence if you're in edit mode); paste to another slot. Make a variant by radically filtering, etc.
- Pattern change while playing: press the destination pattern; it queues (blinks) and switches at the end of the current pattern.
- **Mutes**: FUNC + (mute) = mute tracks. **Green = global mute** (project-level, persists across patterns). **Purple = pattern/local mute** (remembered per pattern). FUNC + MUTE-MODE toggles color and enters a **latched** prepare-then-release workflow for planned mutes.
- **FUNC + PERFORM** = Perform Kit mode: all changes are temporary; exit and everything reverts. The screen flashes to confirm you're "safe". (Save the perform-kit state as a kit with FUNC + YES.)

## Sampling (the input port)
- Press SAMPLER. A live signal/noise-floor is shown. Two record modes: **threshold** (gate — set threshold, arm, plays into it) and **PLAY** (records on transport with the pre-roll count-in).
- Cuckoo sampled a TR-606/vinyl bassline: arm, hit YES on the beat, YES again to stop. **FUNC + YES** previews the buffer. Trim START/END with zoom (FUNC + zoom = vertical zoom). YES saves (auto-suggests a name via the cog; FUNC + COPY copies the name to reuse). Then assign to a track. **FUNC + NO clears the record buffer.**
- **Loop machines**: FUNC + (SRC machine, left page) swaps the *track* machine (right page = filter machine). **Stretch** time-stretches a loop to the project tempo (granular-ish, some artifacts). **Warp** chops into segments (set segment size, e.g. 16th notes; works best when you tell it the source's bar count). **Repitch** = turntable behaviour (slows = pitches down, no artifacts).
- Set AMP RELEASE to infinite so a loop just plays through.
- **GRID machine** (Cuckoo's favourite): lines up evenly-spaced slices and plays them across the keyboard. Set GRID (e.g. 8 or 16) and trigger slices via keyboard mode. Used it to sample a long synth chord run on the beat then play the slices chromatically.
- Changing tempo restretches all stretch/warp/grid material; the repitch bass changes pitch with tempo.

## Keyboard / scales / preset pool
- **FUNC + KEYBOARD** = keyboard setup. **Keyboard Fold ON** snaps the trig keys to a chosen scale (Ionian, Dorian, Phrygian, Mixolydian, Lydian, blues, Persian…) and root.
- **TRIG page 2**: PORTAMENTO toggle for glide between notes.
- **Preset pool** workflow: save crafted sounds as presets (preset/kit icon → save → name → tag). Then add them to the **project preset pool** (preset menu → pool, or manage → add to pool). Two uses: (1) hold a step + turn the level encoder to lock a *different preset* to that single trig (sound-locking) — multiple sounds on one track; (2) **FUNC + up/down** switches the trig-key mode to "preset pool" so you play/sequence straight from the pool on one track. Other trig modes via FUNC + up/down: **velocity** and **retrig**.

## Closing note (platform)
Cuckoo claims the DT2 is "the first product on Elektron's new technical platform" layered over the old Digitakt hardware — implying much more CPU headroom and faster firmware updates and entirely new machines to come. (Unverified opinion from the presenter, not an Elektron spec.) Also notes DT2 is backward-compatible: OG Digitakt projects load and "just work" (he didn't demo it).

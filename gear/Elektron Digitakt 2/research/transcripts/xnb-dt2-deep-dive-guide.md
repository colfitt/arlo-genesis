https://www.youtube.com/watch?v=8zXBNqRstxQ
XNB · The Elektron DIGITAKT II deep dive guide tutorial · 2024-07-27

> Source captions: YouTube auto-generated, cleaned to prose. ~1h59m — the deepest single DT2 walkthrough found, structured as chaptered "course". Entirely DIGITAKT II specific, with explicit Mark 1 vs Mark 2 contrasts throughout. (Note: the auto-transcript repeatedly mis-hears the device name as "digit/Dy/digitact" — it is the Digitakt II.)

## Projects / storage (DT2)
- +Drive = main storage: **20 GB**, holds samples, sounds (presets), kits, projects. Default factory project is "presets" and is write-protected.
- A project remembers **~400 MB of samples** in RAM; each loaded sample takes a sample slot. Check usage at **Settings → System → Storage** (shows +Drive free, samples count, remaining sample time, RAM use).
- **16 tracks**, each freely **audio OR MIDI** (vs OG's fixed 8 audio + 8 MIDI). Silent track select = hold TRACK + key.
- **Machines**: SRC machine = the engine that plays the sample (FUNC + SRC to swap). Filter machines via FUNC + FLTR. DT2 has more SRC + filter machines than OG.

## Assigning samples — two methods
1. **One-at-a-time**: SRC page → sample-select encoder → pick an empty slot → YES → browse +Drive (Factory has categorized folders: textures, tonal, oscillators…). Right-arrow shows assign target + an auto-preview toggle; FUNC + YES auditions. YES assigns to that one slot.
2. **Batch**: FUNC + SAMPLES → +Drive → check multiple samples (YES adds a checkmark) → right-arrow for advanced ops (select all / deselect / move / rename / delete) → **Load to Project**. You can target a specific destination **bank** (FUNC + YES on the "bank: any" field, then choose A–H) so samples land in, e.g., bank H.

## Presets, kits, and housekeeping
- **Preset** = a sample + all track params (filter/env/FX/sends). PRESET button → load / save / manage / pool. 8 banks × 256 preset slots. Search and category-filter (e.g. "kick") in the load menu; FUNC + down jumps by 5; FUNC + YES loads without leaving the list.
- A preset imports its sample into the project (the sample is the "backbone" — deleting it breaks the preset).
- **Kit** = a collection of 16 presets (like a DAW drum rack). Loading a kit imports all its samples — sample count balloons.
- **Free RAM**: FUNC + SAMPLES → Project RAM → right-arrow → **Select Unused** → back → **Unload**. Removes samples not referenced by the project (slots stay allocated but RAM frees).

## Recording modes
- **Live record**: hold RECORD + PLAY (RECORD flashes). Tap RECORD again toggles quantized/unquantized (shown top of screen). PLAY exits live-rec but keeps playing; PLAY again pauses; STOP stops.
- **Quantize menu**: FUNC + TRIG → set quantize strength; can quantize the whole pattern or per-track (hold TRACK while quantizing).
- **Grid record**: tap RECORD once (steady, not flashing). Select track, tap steps. FUNC + CLEAR clears the *selected track's* sequence while in grid record (vs whole pattern when not in record).
- **Micro timing**: in grid record, press a step + use arrows to nudge it forward/back off the grid ("on grid" shown when centered).
- **Step record** exists but is least-used — see manual.
- Tempo: FUNC + tap TEMPO four times. Metronome volume/time-sig/swing on that page. **Pre-roll** count-in up to 16 bars. **Per-pattern vs per-project tempo** toggle (E knob): per-project keeps tempo constant across pattern changes — useful for live sets. Hold FUNC + turn A to *cue* a new tempo that only applies on release; arrows nudge tempo and snap back on release.

## Keyboard / scales / trig modes
- KEYBOARD mode plays the selected track melodically. FUNC + KEYBOARD shows the on-screen keyboard + scale select (E knob): pick scale + root; trig keys re-lay-out to the scale. **Keyboard Fold ON** removes dead keys so every key plays a scale note; up/down change octave. Fold mode is most useful for recording and octave jumps.
- **Trig modes** (FUNC + up/down): **Tracks** (default — each key plays a track); **Velocity** (every key plays the *selected* track at different velocity); **Retrig** (selected track at different retrig rates); **Preset Pool** (each key plays a preset from the pool). All record straight into the sequencer.

## Pattern length / polymeter / reset
- FUNC + PAGE = page setup. Up to **128 steps = 8 pages of 16** (twice the OG). E knob by ones; PAGE button by 16; trig keys set odd lengths (e.g. 5). Extending **copies** existing content forward. Resolution (F knob) speeds/slows the sequence.
- **FUNC + YES** toggles **per-pattern vs per-track** length. Per-track lets you set different LENGTH and **speed multiplier** (F knob) per track = **polymeter/polyrhythm**.
- **Pattern RESET** (right side) decides when all tracks realign to step 1. Set to INF for never-resetting evolving patterns — **but**: with no reset the pattern won't *cue* a change while playing (it doesn't know its length); it only switches on STOP. Set the **change length** to control how long a cued pattern waits before switching.

## Mutes
- FUNC + (mute) — **Green = global mute** (project-level, persists across patterns); **Purple = track/pattern mute** (only that pattern). FUNC + MUTE-MODE toggles. Global is the performance-friendly one for cueing patterns.

## Copy / paste
- RECORD off: FUNC + RECORD copies the whole pattern; FUNC + PASTE pastes it. RECORD on (grid): FUNC + COPY/PASTE copies the *selected track's sequence*. Hold PAGE + FUNC + COPY/PASTE copies a single page (of the selected track).

## Euclidean sequencer (FUNC + AMP)
- Per-track pulse generator. Turn ON; **two pulse generators** each with a pulse count + **rotation (ro)**, plus **TRO** to rotate both together. Behind the scenes it writes trigs you can see in grid record.
- **Operators** combine the two pulses: **OR** (plays all trigs of both), **XOR** (a trig on the same step cancels — silence where they overlap; offset them for combinations), **AND** (only where both land), **SUB** (pulse-2 cancels pulse-1 only). **LENGTH** field only works in per-track length mode. Advice: don't overthink it — offset the pulses and audition.

## TRIG page parameters (two pages, toggle with arrows)
- Page 1: **NOTE** (offsets the key, not the sample tune), **VELOCITY**, **LENGTH** (note duration ¼…8 steps; FUNC jumps values), **PROBABILITY** (e.g. 50% = coin-flip per trig). On DT2 the conditional/**FILL** lives in its own knob (locked until you hold the trig). **LFO-T** and **FLTR-T** = whether a trig fires the LFO / filter envelope (turn off to stop re-triggering the envelope per step).
- Page 2: **RETRIG** (toggle on; RATE sets subdivision; LEN sets how many steps it retrigs; **VFAD** velocity-fade negative = fade out / positive = fade in — depends on the trig's base velocity); **PORTAMENTO** + time (deeper config under FUNC + FLTR setup: slope, legato/glide modes).
- Hold a param button to read its **value**; FUNC + turn = **param value jump** (bigger increments).
- Hold PAGE + PLAY = clear page (roll params back to default). Hold + YES (page 2) = randomize. Hold RETRIG = reload last saved state.

## SRC machines (one-shot detail)
- One-shot: START / END (L) trim points, plus a LOOP point. Play modes: forward, **forward+loop** (loops the loop section), reverse, reverse+loop. (XNB defers a full machines breakdown to a separate video.)

## Filter
- Default = variable-state Multi-Mode (low→band→high). CUTOFF, RESONANCE, ENV DEPTH (envelope modulates cutoff by default).

## P-locks (parameter locks) & preset locks
- **P-lock**: in grid record, **hold a trig** (do not release) and turn a control — that value is locked to that step (the trig blinks; locked param pages turn red). Remove a lock by re-entering the step, or **hold NO + the locked encoder** ("erase locks"), or live-erase by holding NO during live record. Red blinking trig = trig + lock; **yellow blinking = lock only, no trig** (a parameter step with no note).
- **Preset/sound lock**: first add presets to the **preset pool** (PRESET → manage → select → "Add presets to pool"). Then hold a trig and **turn the level encoder** to assign a different preset to that single step. The pool exists so the box can pre-load the samples/presets and switch instantly per step. Hold trig shows the locked preset's name; push the level encoder to revert that step.

## Perform Kit (new on Mark 2)
- Solves two OG problems: (1) no transition when changing patterns, (2) the box auto-remembering live tweaks on the source pattern. FUNC + PERFORM = Perform Kit ON. Tweaks made now are carried *into the next pattern* you cue (so you can craft a real transition) and are **not** auto-saved to the source pattern. Exit and everything reverts. FUNC + YES (instead of NO) saves the perform-kit state as a kit.

## Page Loop (recent firmware)
- In grid record, **hold PAGE** — the top trig row shows all pages (green = active). Tap one page to loop just it, or tap two to loop a range. Great for performance and for editing one page in isolation.

## Mixer / master (FUNC + MOD)
- Internal mixer: levels of all 16 tracks across two pages (level data / source level / amp level).
- Sends mixer page: send levels + **Master Overdrive** (crank for grit) + master volume.
- **Compressor** page: attack, release, makeup gain, threshold, ratio/limit, **side-chain filter** (HPF the detector so it ignores lows), and **side-chain source**: COMP MIX (reacts to everything), NOT-COMP (inverted selection), tracks 1–16, or external L/R input. Parallel blend via the wet knob.
- **Compressor routing** (FUNC + setup → compressor routing): choose which tracks feed the compressor — e.g. exclude all percussion so only bass+synth get compressed; NOT-COMP then inverts the routing. Effect-send and external-input can also be routed into the compressor.
- **Track FX bypass** (FUNC + setup, "effect setup"): hold TRACK → effects → exclude percussion so a master filter/FX affects everything *but* the drums.

## External mixer
- For audio coming in the rear inputs: set how much of the input goes to the sends, plus its volume and balance.

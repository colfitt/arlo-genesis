https://www.youtube.com/watch?v=1wt1Vx3-_0k
loopop · "Akai MPC SAMPLE // Does it BEAT the Competition? + 5 Power Tips // Review & Tutorial" · 2026-03-24 (46 min)

The single best AC50-specific deep-dive on file. loopop walks the entire MPC Sample workflow on the actual hardware (not a bigger MPC), so every technique below is AC50-verified unless noted. Captured for the craft angle: sampling, chopping, sound design per pad, sequencing, FX, and the resample tricks that make it punch — plus honest limits.

## Sampling & the recall buffer (do NOT chase a perfect take)
- Two standout sampling features: the **25-second recall buffer** and **very long samples (up to ~20 min)**. The recall buffer means you never have to nail a performance on the record button — just play, and if it was good, hit **Shift + Sample Record/Recall** to pull the last 25 s onto the next free pad, then trim/chop. "Like the government, it's always listening" — and the same applies to the **sequencer**: Shift + Recall embeds the last played MIDI loop into the sequence even if you forgot to press record. This is the fastest, most fun-preserving capture workflow on the box. Use it constantly when sampling the banjo, baritone, or a pedal swell off the Apollo bus.
- Sources: built-in mic (surprisingly sensitive), rear stereo 1/4" inputs, USB from Mac/phone, and Resample. Record with or without FX (an Input Config toggle).
- **REC LENGTH = Seq** turns sampling into a looper: recording starts at the next sequence loop and captures exactly one sequence length. Great for printing a tempo-locked bed.

## Chopping (the heart of the box) — "super fast workflow for lazy chops"
- Chop modes: Threshold (auto, "a bit laggy, depends on the sample" — treat auto placement as a *starting point*), Regions 4/8/16 (even splits), and Manual (tap pads in time to place slices live). Always fine-tune slice Start/End by zooming with the knobs or encoder; move, add, or delete split points freely.
- **Polyphonic chops = mini melodic tracks.** Key trick: a chopped pad can act like its own polyphonic instrument track. Set the pad to **Poly** (Tune page 2 → Polyphony), and you can sequence/play the 16 slices as a little melodic or chordal part — this is how loopop built the multisampled instruments in the intro. While in Chop mode all slices share one set of sound-design params; **Shift + Extract (B1)** copies any slice out to its own pad for independent editing.
- You can **sequence chop slices** directly: trigger the slices while recording and the MPC automates which slice plays where. (You can't edit chop slices in Step Edit on this firmware, though.)

## Per-pad sound design (where punch is dialed in)
- **Amp Env:** Attack + Decay (0–127). Shift+K2 sets **Decay From Start or End** — Decay-From-Start with a low decay value is how you shorten/tighten a one-shot's tail; Decay-From-End is the default that lets a loop ring out.
- **Tune:** ±24 semitones coarse, ±90 cents fine. **Warp** does Time Stretch (length/tempo, pitch independent — "pretty good algorithm") or Re-Pitch (length + pitch together, like varispeed; 100% = original). For tempo-locked loops set Warp = **Seq** and # Beats to auto/manual.
- **Filter:** per pad, multiple types incl. **Classic** (modeled on the MPC3000 LPF), plus LPF/HPF/BPF (2- and 4-pole), each with resonance and a filter envelope (decay from start or release).
- **Note On vs One Shot:** Note On = sample sounds only while pad is held (envelope gets a Release stage) — use it for played/melodic chops; One Shot for drums.
- **Loop trick for ambient beds:** turn Loop on and the sample keeps playing even with the transport stopped — park a drone loop in the background while you work on other pages, until you double-tap Stop. On-aesthetic for the fuzz-wall material.
- **Mute Groups** (e.g. closed + open hat share a group so closed chokes open) and **Pad Link** (one pad triggers two — e.g. layer a sub under a kick, or fire a melodic pad with a break). **Offset** delays a pad's start; pairs nicely with Pad Link.

## Sequencing fast
- Play live (quantized or not via the Q toggle), or finger-drum with **Note Repeat** (pressure-sensitive — vary finger pressure for natural rolls). One level of undo only, so to experiment: stop record, toggle record + play a risky idea, undo if you hate it.
- **Sequence shortcuts to develop ideas fast:** Double Seq (copies bar 1 into bar 2 so you can vary it), Half Seq, Double/Half Speed.
- **Time Correct after the fact:** select only the pads you want corrected and "Do It" — so you can leave kick/snare loose and tighten just the hats. Apply Swing here ("wouldn't be an MPC without swing").
- **Automation:** record knob moves (e.g. hat filter cutoff + resonance) live into the sequence; erase automation with Shift + touch the parameter. Almost all pad params automate.

## FX — and the all-important resample-to-bake trick
- Four engines: **Pad FX** (16 master insert FX, pressure = depth, up to 4 at once, latchable — incl. LoFi/12-bit, Color, Beat Repeat, Reverb, Delay), **Flex Beat** (16 time-warp/stutter/scratch/gate master FX, quantize them on launch, has a Mix control so you don't lose the pattern), **Knob FX** (one effect on K1–K3, up to 6 params via Shift, **applied to selected pads only** — incl. Vintage Emulator [MPC3000/MPC60/SP1200/SP1200Ring], Vinyl, Tape, a "pumper" pseudo-sidechain), and the **master Compressor with vintage Color**.
- **Critical limit + workaround:** Pad FX, Flex Beat, and the Compressor are all **master insert FX on everything**; Knob FX is the only per-pad option. There's **no true sidechain**. To get an effect on just one sound (e.g. reverb only on the snare): apply the Knob FX, then **Resample that single pad** — but you can't trigger the pad while armed to resample into another pad, so use the **recall buffer**: play the wet snare, Shift+Recall, then bypass the live FX → you've baked the wet snare to its own pad. Trim off the recall pre-roll.
- **Resample the whole sequence:** Shift + Resample (Pad 11) bounces the entire sequence (FX and all) to one pad — "I don't have to get the timing right, I now have the whole thing." Chop that, rebuild, degrade further. This is the core generative loop.

## Honest limits (where the AC50 gets in the way)
- **One sequence track for all 128 pads**, one fixed length — no per-pad/per-track lengths, no clip launching per sample like the SP-404 MkII.
- **No TR-style step sequencer** ("can't say, sequence a kick every four steps") — it's list/live oriented.
- **No true sidechain** (only the pumper Knob FX), **no granular voice** per pad (Granulator only as a Pad FX), one level of undo, small fonts in list/step-edit modes.
- **16 Levels Tune = 16 chromatic semitones only**, no scale options, and Pad Bank does NOT transpose the grid (unlike bigger MPCs).
- Built-in **speaker is mono and drops off hard below 200 Hz** — never judge your low end on it; use headphones/monitors (the JBL LSR305s).
- **No internal-storage access over USB** and no way to see free space; SD-card access works in drive mode.

## Bonus (computer-assisted, flagged as not-on-device)
loopop wrote a free auto-sampler web app (his Patreon) that samples a hardware synth or plugin chromatically/by chord into a 16-region WAV you drop onto a pad — turning a chopped pad into a playable multisampled instrument or chord bank, working around the lack of scales/chord modes. Useful if the owner wants to sample the S08/upright/accordion into a tuned MPC instrument, but it requires a Mac + BlackHole/IAC routing, so it's an off-device add-on, not an AC50 feature.

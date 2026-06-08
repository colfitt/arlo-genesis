https://www.youtube.com/watch?v=rUkuktFkSLw
Richard DeHove · Strymon Timeline: Complete walkthrough · 2022-03-04 (65 min)

> The single most thorough free TimeLine tutorial. DeHove (intelligent-machinery / "How To Make Electronic Music") configures the globals for a MIDI-clock-as-master rig, then builds one starter preset on every one of the 12 machines in dial order, narrating each machine's specific parameters as he goes. Clock-face knob references throughout. Cleaned from the channel's manual English captions.

---

Some machines are good for random twiddlings; others like this one will serve you best when you know all their ways. Happily, this is a simple machine, and once you understand a couple of its basic concepts, all its global options, all its fun and all its powers become very clear. What we'll do is go through the global menu, then go through each of the 12 delay types and create a starter preset on each. But before we even get to the global menu, the one important thing you should decide is: how are you going to handle the clock?

In my case I'm going to take an external clock via MIDI, which I've already got plugged in, and the presets I make are all going to take whatever this incoming clock is. So if I change the incoming clock to 120 BPM, the presets play at 120; if I change it to 90, they play at 90. You could instead set it up so the preset itself takes precedence — you program a preset at a set rate and that's what you get when you call it up. I prefer the idea that an incoming clock is the master and every preset conforms to it. The choice is yours, but it helps to have that decided before you get into the global configurations, and certainly before you start programming individual presets.

## Global menu — navigation
The VALUE and TYPE knobs control all the parameter/menu navigation. They both turn and press (push-click). To get into the global menu, press and **hold** the VALUE knob a few seconds — "globals" comes up. Turn the knob to see options; press to enter an option, press again to back out. To get out of the global menu entirely, press the TYPE knob (because there's nothing worse than being stuck in a menu).

## Global menu — settings (DeHove's choices)
- **Time units:** ms or BPM — set to **BPM**.
- **LP LOC / Looper level / Looper exit:** looper settings, skipped here.
- **Bypass:** True or Buffered. Buffered if you're running insanely long cable runs; **True bypass** is probably the one you want.
- **MIDI channel / MIDI CC (on) / MIDI PC (on):** keep CC and Program Change on.
- **MIDI THRU:** off by default, left off.
- **Bank SC (bank scroll):** limits the highest preset bank you can scroll to; no reason to change from 99.
- **Expression:** skipped.
- **Dry signal:** Normal (normal dry+wet on the MIX knob) vs Kill (kills dry, MIX becomes a wet-level mixer). Kept on **Normal**.
- **Spillover:** lets the delay tail continue even after you switch it off. Turned **ON**.
- **Names:** On / Scroll / Off. "Scroll" scrolls the whole preset name across the 6-char screen (he finds that annoying). "On" shows only the first 6 characters. "Off" shows just bank numbers. Kept on **On**.
- **Preset dump:** dump all presets over MIDI.
- **MC Sweep (MIDI clock sweep):** on/off — whether you get the "sweep" delay-pitch effect when you change presets or tempo. Left **ON**.
- **MIDI Clock Reset:** *Important.* Turned **OFF**. With it ON, the moment another clock pulse arrives the unit forces the time back up to the clock speed — so if you manually tweak the time it keeps "correcting" you back to clock. He wants presets to load at the incoming clock speed but then be free to nudge manually, so reset is OFF.
- **MIDI ST (MIDI send state):** whether preset CC values are sent to MIDI out; may matter depending on your THRU setting. Left **off**.

Exit globals with the TYPE knob. Pressing TYPE again toggles the main display between **preset name** and **time value** (time shows as BPM because the units global is set to BPM).

## Presets & front-panel controls
100 banks, each with an **A** and a **B** preset. To go **up** banks: press **B + TAP** together. To go **down** banks: press **A + B** together. Then press A or B to select that preset. The little engine LED ring shows which delay type the preset is on.

Front-panel knobs (the same across nearly all machines, with small differences on dTape and dBucket):
- **TIME** — coarse delay time (display toggles ms/BPM).
- **VALUE** — fine delay time; quick **press** = preset PARAMS, **hold** = globals.
- **REPEATS** (feedback) — affected by machine, filter, etc. **3 o'clock is a reasonably safe ceiling before self-oscillation.**
- **MIX** — fully CCW = dry, fully CW = 100% wet. **3 o'clock is 50/50, NOT 12 o'clock.** Flicking to 100% wet is useful to hear exactly what a machine is doing.
- **FILTER** — fully left = OFF; **12 o'clock = darkest**; fully right adds some highs back in.
- **GRIT** — input-level-dependent distortion/artifacts. He finds it very subtle; fully on it can slightly mute/reduce volume. He keeps it off as a default and winds it up per-track.
- **SPEED / DEPTH** — modulation LFO rate/intensity, plus a subtle stereo-field enhancement. Worth experimenting before programming: ~0.1 Hz at minimum, ~12 Hz fully up ("a fast vibrator"). 12 o'clock is "a bit seasick." Turning DEPTH off entirely makes things sterile; opening it up brings the stereo field in. There's a "knob memory" — the SPEED/DEPTH/FILTER/GRIT positions you set carry as the default as you move around the machines, so set a comfortable modulation baseline once and every starter preset inherits it.

DeHove's philosophy for a default preset bank: pick your modulation SPEED/DEPTH, leave GRIT off and FILTER off, so every preset starts from a known place; you then add filter/grit per song. This is better than copying random factory presets (each of which has different mod/grit/filter you'd have to re-fix).

## PARAMS — common vs machine-specific
Quick-press VALUE = that machine's PARAMS. Turn through them. The **common** parameters (shared by every machine) begin at **Tap Division** — so anything before Tap Division is machine-specific. Common params:
- **Tap Division:** quarter / dotted-eighth / triplet / 16th (he keeps quarter as the default).
- **Boost:** ±volume trim to match preset levels.
- **Persist:** per-preset trails (mirrors the global Spillover).
- **Name:** name the preset.
- **EP / EP Set:** expression pedal on/off + heel/toe positions.
- **Tap:** **Global** vs **Preset.** Preset = the preset always recalls its own programmed tempo regardless of incoming clock. Global = it follows the global setting (here, the incoming MIDI clock). He leaves it on **Global**.
- **MIDI Clock:** on/off — will this preset accept incoming MIDI clock.

## The 12 machines (starter presets, in dial order)
1. **Digital** (bank 1) — machine-specific: **Smear** (off), **High Pass** (off → 900 Hz; 900 is high, well into the mids), **Repeat Dynamics** (changes how repeats trail off; subtle; off). Voiced clean digital.
2. **Dual** (bank 2) — **Time 2** (a time-division ratio of the main time), **Repeats 2** (2nd line feedback), **Mix 2**, **High Pass**, **Config: Series** (one delay feeds the other) **or Parallel** (left/right stereo field). TimeLine has few ping-pong patterns, so he leaves Dual on **Parallel** for the L/R spread.
3. **Pattern** (bank 3) — **Pattern number** (16 patterns; **#16 = early reflections**, a reverb-ish trick), **Smear** (off), **High Pass** (off). One pattern had a long repeat tail he had to dial down.
4. **Reverse** (bank 4) — **Smear**, **High Pass**, then straight to Tap Division. Best with big chords / slow ambient material.
5. **Ice** (bank 6) — **Interval** (pitch of the slice; one octave down to two octaves up — he keeps +1 octave), **Slice** (short/medium/long — medium), **Blend** (a *secondary* dry↔ice mixer inside the engine, on top of the main MIX), **Smear** (very effective here, set ~halfway), **High Pass** (off). "Ice is like what other pedals call shimmer." A profound effect, especially with the pitch interval + smear.
6. **Duck** (bank 6... he saves it next) — **Sensitivity** (higher = harder ducking, so it's harder for the delay to push through), **Release** (how fast you get full delay after playing stops), **Feedback: Normal or Gate** (Normal = whatever repeats is set; Gate = nothing until ducking activates). He uses **Gate** + a fast/16th tap to make the ducking obvious.
7. **Swell** (bank 7) — **Rise** (attack time in seconds; up to ~2 s where nothing's heard until late), **Smell**... **Smear** (benefits from some — left ~halfway), **High Pass** (off). Very dependent on tempo and what you're playing.
8. **Trem** (bank 8) — **LFO shape** (triangle / square / sine / ramp / saw — he picks sine), **Speed** (a *ratio* of the BPM; good to pick something not identical to the pattern so the trem doesn't get lost in it), **Depth** (full up), **High Pass** (turned off to match the rest).
9. **Filter** (bank 9) — like Trem it starts with an **LFO** but with many more shapes incl. **polarity** (+/− triangle, etc. — where the LFO starts has a big effect), **Speed** (ratio of BPM), **Depth** (full up = interesting), **Filter Q** (resonance — can be vicious; kept ~halfway), **Location: pre or post delay** (audibly different — he demos both). "A great little engine, hours of fun."
10. **Lo-Fi** (bank 10) — **Sample** rate (gets really nasty at **4 kHz** or below; up to 96), **Bits** (at least 8-bit to count as lo-fi; lower really breaks up — he picks **8-bit**), **Mix** (an internal dry↔lo-fi mixer like Ice's Blend — tends toward lo-fi), **Vinyl/Final:** off / **Dynamic** (crackle in the repeats) / **Static** ("S", a constant crackle — he leaves off to avoid mystery clicks later), **Filter:** 8 gadget shapes — vintage amp, old phonograph, 70s clock radio, megaphone (cheerleader megaphone), antique phone, cell phone, intercom (he keeps vintage amp).
11. **dTape** (bank 11) — **Tape Speed:** Fast (high-fidelity) or Normal (weird lo-fi). **Low End** contour: fully left = full low end, fully right = a high-pass effect. On dTape the four bottom knobs re-map: **FILTER → Tape Age** (left = new, right = old), **GRIT → Tape Bias** (left = under-biased, right = over-biased, **9 o'clock = balanced**), **SPEED → Crinkle** (left = new tape, right = mangled tape), **DEPTH → Wow & Flutter** (tape machine speed fluctuation). His starter ends up "a mangled tape in a rotten machine" — seasick — but that's the point if you want tape.
12. **dBucket** (bank 12) — **Single** (one bucket chip) or **Double** (two chips, cleaner). On dBucket: **FILTER** stays a filter but left = bright, middle = neutral, right = dark; **GRIT → Bucket Loss** (further right = more loss/degradation). His starter: filter dark, a modest amount of bucket loss, modulation back to the standard baseline.

## Saving workflow (his repeatable habit)
Press-and-**hold** VALUE to save → "save" appears → toggle to the target **bank** → press **A** (or B). To name mid-save, press TAP to back into PARAMS, set the Name, then re-save. His trick: save the same vanilla starter onto **both A and B** of each machine's bank, so A stays the clean reference and B is the one you experiment on without losing the vanilla. Naming convention: "1 DIGI", "2 DUAL", etc. The engine LED turns a different color when you've modified an unsaved preset and back to green when you return knobs to the saved values. "The more you save and name, the less of a hassle it becomes."

To become a "time lord" he notes the next steps are CC control, an expression pedal, and the looper — "that will be for next time" (see the looping-in-perfect-sync video).

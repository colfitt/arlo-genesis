https://www.youtube.com/watch?v=2kfrZbEbRY8
Mark Johnston (Secret Weapons) · Introducing the Chase Bliss X EAE Big Time · 2026-04-30 (1:51:42, ~26k views)

NOTE: ~1h52m deep-dive — the most thorough Big Time tutorial available at launch. Auto-captions cleaned to prose; long wordless playing passages removed. This is the primary workflow reference. Signal chain in the video: Jennings Voyager guitar → Big Time (mono in / stereo out) → Quad Cortex Mini (Bad Cat Cub 5 captures, clean) → Pro Tools.

---

## Easter egg + framing
- **Vegas mode** (LED light show, like other Automatone pedals): with the pedal OFF, take all faders to the bottom, push the left-most and right-most faders to the top, then apply power.
- Designed by John Snyder (EAE) + Chase Bliss over several years. Price ~$900–1000. Homage to early-'80s digital rack delays — an "end-to-end recreation," not just a model.

## Architecture (how the boxes connect)
Analog stereo PREAMP at the input → stereo DIGITAL delay engine in the middle → analog LIMITER at the end of the feedback loop. Two channels of high-quality analog preamp in, two channels of analog limiter out. It is "an interconnected system": **input gain (COLOR) plays into feedback, which plays into the output limiter** — a full delay-machine ecosystem that feels analog/tactile but is a stereo digital delay at its core.

## Hardware navigation
- 6 faders, 5 arcade buttons (marquee through settings), 2 footswitches. Top: stereo ins, stereo outs, MIDI in/out, expression port.
- **RIGHT footswitch = bypass** (and scroll-up in preset mode; press-and-hold = freeze/overload, behavior depends on mode).
- **LEFT footswitch = tap tempo** (and scroll in preset mode). **Press-and-hold LEFT = preset mode** (LED turns green; use left/right to scroll the 10 onboard presets; press-and-hold LEFT again to exit).
- **Press-and-hold the far-LEFT arcade button = Alt/"secondary" menu** (flashing "A"). Press again to exit.

**Alt (secondary) map — all labeled on the pedal:**
| Primary fader | Alt parameter |
|---|---|
| COLOR | TEXTURE (tunes the current STATE) |
| TIME | RATE (modulation) |
| CLUSTER | DEPTH (modulation) |
| TILT EQ | CROSSOVER (tilt pivot frequency) |
| FEEDBACK | DIFFUSE (amount) |
| WET | DRY (volume) — WET is a wet-VOLUME, not a mix; alt = dry volume |
| MOTION (btn) | SPREAD |
| MODE (btn) | 0.5X clock |
| VOICING (btn) | DIFFUSE TYPE |
| STATE (btn) | +12dB boost |

## The six faders (in SHORT delay mode)
- **COLOR (input gain):** sets how hard signal hits the feedback loop AND the output limiter. = input gain / preamp saturation / feedback intensity / limiter impact, all at once. Lower = cleaner repeats, less feedback intensity.
- **TIME:** delay speed AND a master CLOCK that governs modulation speed and how MOTION interacts with the rest of the pedal. It's a clock control more than a literal time control — fidelity stretches as you lengthen.
- **CLUSTER:** introduces additional delay lines that subdivide/bounce around the primary delay. Low = one extra ping-ponging line; higher = progressively more multitap lines (more obviously discrete delay lines in LONG mode; more multitap-ish in shorter modes). Top of CLUSTER ping-pongs the added taps. Great for instant blurry delay pads.
- **TILT EQ:** north of noon = cut lows / boost highs; below noon = cut highs / boost lows. **It sits BEFORE the feedback loop**, so boosting lows raises feedback-loop volume → more/longer repeats (and conversely, cutting lows shortens the tail).
- **FEEDBACK:** lots of throw in the first ~10%, then extreme. Controls number of repeats.
- **WET:** wet output level (NOT a wet/dry mix). Pull it fully down and use COLOR alone for an "expensive boost"/preamp. Separate wet & dry volumes make it a clean kill-dry, line-level wet/dry-wet or DAW aux-send tool.

## Modes (center arcade button: MOD / SHORT / LONG / LOOP)
- **MOD (off):** ~4 ms to ~36 ms — slapback/double at the long end, comb-filter/flange/chorus territory as you shorten, especially with modulation.
- **SHORT:** up to ~736 ms.
- **LONG:** up to ~12.5 s (and ~24 s with 0.5X engaged).
- **LOOP (purple):** phrase looper (see below). Jump into it with audio already in the buffer and it freezes/holds that audio.

## Tap tempo, subdivisions, "return to clean" hacks
- **Panic / reset hack:** press-and-hold the MODE button → recalls a simple, clean, straightforward delay from anywhere (even preset 0 can get big/unruly).
- Tapping with LEFT footswitch **snaps TIME to the center of the fader's throw** so you can bend faster/slower around the tapped value and return to it (MODE button dims while in this tapped state). Useful with SCALE = octaves. Tap a new tempo to re-center; press MODE to return to "traditional time mode" (slider top/bottom = full predetermined range).
- Default tap = a whole note. **Change tap subdivision:** double-tap both footswitches (or press-and-hold both) → enters the "E" expression-programming / OPTIONS page → press-and-hold SCALE → TIME slider becomes subdivisions (UNLABELED, low = whole note, higher = faster) → double-tap to exit.

## MOTION (modulation) + SCALE (pitch quantize)
- MOTION button: **1 = Sine, 2 = Square (Thermae-style pitch jumps), 3 = Envelope follower.** RATE/DEPTH live in the Alt menu (under TIME / CLUSTER). RATE/DEPTH get "insane" quickly. Because TIME is a clock, the TIME fader sets how fast the modulation range runs.
- SCALE quantizes the pitch movement of both TIME and MOTION: **off = smooth glides; Chromatic; Oct+4+5 (4ths/5ths/octaves); Octave (octave jumps only).** Combine square-wave MOTION + SCALE = quantized pitch-stepping cascades.
- With everything quantized to a scale, the whole pedal becomes a **stereo Thermae** with strong ambient properties.

## STEP mode (Thermae-style sequencing) — OPTIONS menu under MOTION
- Turn on STEP MODE in options → MOTION goes a dull blue (you can no longer step its waveforms). Instead, **tapping the LEFT (tempo) footswitch steps the pitch through the active SCALE intervals.** TIME sets how quickly steps happen (and legato vs. abrupt). Tune to octaves, etc. Pure Thermae/step-sequenced behavior.

## SPREAD (stereo) — Alt under MOTION
- **Off = true stereo / dual mono** (whatever stereo image comes in, comes out; no inherent widening from a mono source).
- **Mode 2 (the demo's default, "blue") = gentle stereo widening of the primary delay.**
- **Top = ping-pong** on the final added delays. CLUSTER also adds stereo image; combine CLUSTER + MOTION for very wide delays without going full ping-pong.

## DIFFUSE / reverb behavior — Alt: DIFFUSE (under FEEDBACK) + DIFFUSE TYPE (under VOICING)
- Diffusion smears even a single delay line into a reverb-like wash. Blend with CLUSTER for big ambient clouds. Big Time can act as a reverb this way. (Has a diffusion strength as well as type.)

## VOICING (core tone filter) vs TILT EQ
- VOICING button: **HiFi (clear/pristine), Focus, Warm, Analog (BBD-style dark/filtered).** Each has its own EQ curve. Analog mode + darken TILT EQ + a little chorusing + drive harder + soften output = very convincing "analog/BBD" delay.
- **CROSSOVER** (Alt under TILT EQ): sets the pivot frequency of the tilt — likened to the CXM 1978 (Meris) dual-decay crossover. Lets you keep low-end even with a heavily high-tilted EQ.

## STATE (limiter character) + TEXTURE (Alt under COLOR)
Far-right arcade button cycles **Digital / Compressed / Saturated / #!&% (misbias)**. Severity also driven by COLOR (input gain) and FEEDBACK.
- **Digital** = no limiter; clean & consistent, but allows runaway oscillation / big volume spikes. TEXTURE = reduce bit depth / add aliasing (vintage digital-rack character).
- **Compressed** = subtle comp up to full-on ducking delay. TEXTURE = compression amount (sustain → ducking).
- **Saturated** = clipping/breakup that intensifies the harder you drive (its workhorse dirty state). TEXTURE = clipping symmetry (distort the repeats).
- **#!&% (misbias)** = broken, drifting delay lines; "vintage fuzz on your delays / broken-speaker" chaos. TEXTURE = misbias amount. Soft playing = grit without much loss; big hits drop out fast.

## 0.5X (Alt under MODE)
- Halves the clock: **twice the delay time, half the bandwidth, bit depth dropped 32-bit → 16-bit** (NOTE: Chase Bliss's own materials / the dossier say 32→12-bit — Mark says 16-bit; treat the exact reduced bit depth as UNVERIFIED), plus added clock noise. Up to ~24 s in LONG. Great with Focus/Analog voicings for dark lo-fi.

## +12dB (Alt under STATE)
- Extra 12 dB of preamp volume on top of COLOR — for hitting the delay/limiter (or your amp) harder than the instrument allows. "For those who really need to destroy something."

## Bypass footswitch behaviors
- Press-and-hold RIGHT in a normal delay = **OVERLOAD ramp: maxes FEEDBACK + COLOR momentarily** ("beware volume"). Release to return.
- Press-and-hold RIGHT (different context) = **freeze**: nothing new into the buffer, current sound revolves infinitely; with long times it functions like a phrase looper.

## OPTIONS menu extras (the "E" page)
- **TRAILS** (on in the video = delay continues after bypass).
- **SCALE IGNORE:** lets the MOTION/modulation matrix ignore the TIME control — e.g. big octave MOTION steps while keeping a smooth sine modulation, without the full chaos.
- **DRY KILL:** removes dry from the output entirely (good for reamping / parallel/aux use).
- **DRY CLEAN:** removes COLOR (preamp) from the DRY path only — wet repeats stay gained-up/saturated while the dry stays clean.

## Expression + AUX footswitch
- **Assign expression:** on the expression-programming page, move any fader to the TOP to enable it for expression (then set heel/toe values by positioning the fader at each end of the expression throw). Multiple faders can be mapped.
- **AUX (external) footswitch modes:** scroll presets without entering preset menu; **"Fun mode"** (LEFT = toggle 0.5X clock for real-time half-time lo-fi drops, RIGHT = clear buffer); **Desktop expander** (footswitch records/overdubs/stops/clears the looper for tabletop use).

## Looper (LOOP mode) details
- Start from LOOP with everything set (TIME at midpoint). Press-and-hold the STOP (right) button to **return TIME to center** for the next loop (so you have equal speed-up/slow-down range). 
- Record: set COLOR etc., press LEFT to record, press LEFT again to enter playback (an Alt option auto-enters overdub). RIGHT = stop; press-and-hold RIGHT = reset/erase the buffer.
- **For pristine infinite looping:** VOICING = HiFi, TIME at noon → clean signal, ~45 s record time. Take TIME to the top → 3+ minutes of very lo-fi looping.
- Drop VOICING to Focus/Warm/Analog → tape-delay / sound-on-sound looper that degrades and morphs each pass (analog EQ slowly carves old loops away). Add SCALE for quantized/pitched loop tracking, MOTION for stereo-Thermae looping, CLUSTER + DIFFUSE to turn the whole loop into a cloud, STATE = Saturated/misbias to destroy loops over time.
- Tradeoff: higher TIME between recordings = less record time but higher fidelity (and vice-versa).

## Verdict
"Marvel of a device," phenomenal for guitarists and especially soundscape artists, but expensive (~$900–1000) and power-hungry (9V/1A — dedicated brick or a power Y-cable across two 500 mA ports). Does almost everything except reverse delay. Getting conventional dotted delays requires the subdivision menu dance, so there's a learning curve.

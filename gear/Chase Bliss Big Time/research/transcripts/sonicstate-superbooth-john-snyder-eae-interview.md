https://www.youtube.com/watch?v=1E06eN0A-vM
sonicstate · Big Time: Chase Bliss and EAE — Superbooth 26 (interview w/ John Snyder of EAE) · 2026-05-12 (17:17, ~3.7k views)

NOTE: First-party designer walkthrough. John Snyder (EAE) explains the design and the analog character he brought. Auto-captions cleaned to prose; music passages trimmed. Best single source for the EAE-collaboration character and the engineering intent behind each STATE/VOICING. ("Firman" / "thema" / "Automaton" are auto-caption mishearings of Thermae / Automatone.)

---

## What it is (Snyder's framing)
"We've been working on this for 6 years with Chase Bliss. They brought me on as an analog designer; I had a lot of contributions to the overall sound, vibe, and firmware. It's a **digital delay wrapped in lots of interesting analog processing** — preamplification, analog feedback, analog compression and limiting. That compression/limiting/saturation can be pulled into all kinds of unique directions because it lives within a complex feedback loop. It's an adventure that's like a **1980s rack delay from a parallel universe.**"

## Automatone format
All presets are accessed via **flying (motorized) faders** — swap presets and the faders move in real time, so you always know what the pedal is doing. Makes it a strong live-performance tool.

## The six primary faders
- **COLOR** = input preamplification: sets sensitivity / saturation, and has lots of downstream effects by feeding the internal compressor/limiter and other circuitry.
- **TIME** = delay time; range set by MODE.
  - **LONG (red):** ~0.5–1 s up to ~12 s.
  - **SHORT:** "classic analog delay range," ~40 ms to ~1.5 s.
  - **MOD (off):** ~3 ms to ~40 ms.  *(NOTE: Snyder's spoken short/mod ranges differ from the manual, which labels MOD = 3–46 ms and SHORT = 46–736 ms. Treat exact figures as approximate; the manual's are the spec.)*
  - **LOOP:** time set by punch-in/out; ~1 min up, or 2–3 min if you want really lo-fi. "That mode is for the disintegration-loop soundscape enthusiasts, because of all the ways to manipulate the feedback loop as the loop evolves."
- **CLUSTER** = introduces multi-taps. Short room sound / strange multi-tap at short times; a "round-robin of delays — extra loops interwoven with your loops" at longer times. Turn up and it adds DIFFUSION → reverberant, modulates nicely in the stereo field. "Great to use almost as a reverb but not quite a reverb"; can momentarily introduce bursts of ghostly extra echoes.
- **TILT EQ** = placed WITHIN the feedback loop to shape how repeats evolve. Centered = flat repeats. Cut highs or cut lows → effectively boosts the other band as the feedback loop reprocesses the audio over time.
- **WET** = wet output level. Kept separate from dry "because the wet is capable of so much dynamic range that we wanted it to have its own dedicated control."

## Alt / secondary layer (hold SCALE → blinking "A"; faders fly to the alt page; long-press to enter, short-press to exit)
- COLOR → **TEXTURE** (changes the limiter behavior)
- TIME / CLUSTER → **RATE / DEPTH** (modulation)
- TILT EQ → **CROSSOVER** (tilt pivot point)
- FEEDBACK → **DIFFUSE** — "another way to get reverberant quality; smears delays into ghostly echoes over time; neat way to evolve and degrade loops."
- WET → **DRY** (dry level; usually unity, but fun to kill dry for vibrato/lo-fi effects)
- (buttons) MOTION → SPREAD, MODE → 0.5X, VOICING → DIFFUSE TYPE, STATE → +12dB

## SCALE (quantizes TIME and the LFO)
- Off = time free-running.
- Chromatic = half-steps.
- **Oct+4+5** = octaves/4ths/5ths — "happens to map to the traditional subdivisions of tap tempo in a delay, so it's very convenient for rhythmic stuff when using tap tempo."
- Octave = delay time only halves/doubles — "change the speed of your loop in musical intervals very easily."

## MOTION (modulation of delay time)
- Off; **Sine** (subtle, but the LFO can get extreme — even audio-rate modulation); **Square** ("pitchy octave jumps, very reminiscent of our old pal Thermae" — there's a preset that's nice for that); **Envelope** (playing dynamics alter delay time → bizarre vibratos, dive bombs).
- Env mode is "inspired by an old delay I had with a failing power supply — play hard and the VCO would drop in frequency and eat itself alive. It was delightful. This is a callback to that."

## VOICING (filter curve applied to the DSP — the core "vibe")
- **HiFi** = totally flat.
- **Focus** = gentle band-pass.
- **Warm** = brick-wall filter like vintage digital delays, "pretty much cutting off everything at 10k" — lots of bandwidth still, pleasant high-end roll-off, keeps the truly harsh stuff out.
- **Analog** = a callback to EAE's **Sending V2** delay — gentler slope at ~4 kHz, smoother/darker analog tone "without being fully murky." Works with TILT EQ to fine-tune how repeats evolve.

## STATE — "the most important button on the whole pedal" (changes the feedback-loop behavior)
- **Digital** = hi-fi feedback living within the DSP; evolves very linearly.
- **Compressed** = VCA compression on the echoes; the sum of input + feedback loop interact and apply gain reduction. Subtle comp keeps the feedback loop stable over long periods, OR push it so the sidechain over-reacts → ducking echoes and "crumbling textures that are really fun to play."
- **Saturated** = lifts the compressor threshold and engages a non-linear wave-shaper: tasteful soft clipping, with a **DC bias offset (via TEXTURE) to push the clipping into asymmetrical, ragged territory** — "an edge like a misbiased console channel, or a BBD delay desperately in need of calibration." Saturation also widens the sound stage.
- **#!&% (misbias / "exploitative" mode)** = uses the **compressor sidechain to change the bias of the limiter**. When you dig in, the limiter takes an excursion out of the region where it can reproduce your audio, then comes back in gently → crackling "sag-and-return" sounds, very reminiscent of disintegration-loop / failing-tape textures. "A very musical way to destroy a loop with your own playing — play gently and it stays clean; dig in and you get more texture."

## SPREAD (3 levels): none / gentle widening / full ping-pong.

## 0.5X (Alt under MODE)
- "Basically doubles all the delay time by **cutting the sample rate in half**, and adds some **12-bit** bit-reduction, which sounds really nice." (Confirms 32→12-bit per first-party; resolves the Secret-Weapons "16-bit" discrepancy in Big Time's favor of 12-bit.)

## DIFFUSE TYPE (Alt under VOICING)
- Makes the diffusion stronger — applies to both CLUSTER and DIFFUSE — "more ethereal and ghostly sounding."

## +12dB (Alt under STATE) — "the second most important button"
- Adds a lot of input gain at the front end for weak/quiet instruments or to really push the pedal hard. The pedal already handles line level → hot guitars; the design choice was to **add gain, not cut it**.

## STATE behavior in practice (demo notes)
- Saturated widens the soundstage and gives crumbling/evolving texture; TILT shaves highs (open it to let harsher material through). +12dB pushes it into blistering territory while still passing everything you play.
- If saturation's too intense, Analog voicing shaves more high end.
- Misbias ("purple"/extreme) + Warm voicing + TEXTURE: "the mix sounds like it's ripping itself in half"; lower COLOR to explore the dynamic threshold. **With a delay time longer than the bias-sag attack/recovery envelope, you can punch in clean sections of a loop and come back to destroy them later.** At 12 s, the low-frequency rumble is "the contents of the delay continuing to eat themselves alive."

## Price / availability
$999 US / €1099 EU (VAT + duties incl.), pre-order at chasebliss.com / chasebliss.eu, shipping early June 2026 (finishing final firmware bugs at the time of the interview).

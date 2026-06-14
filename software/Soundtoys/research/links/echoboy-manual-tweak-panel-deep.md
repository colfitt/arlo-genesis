https://www.soundtoys.com/wp-content/uploads/EchoBoy-Manual.pdf
soundtoys.com · EchoBoy User's Guide v5 (official manual) · 2015

Authoritative reference, mined here only for the *deep/hidden* mechanics that matter for tape/ambient
work. The community usage is in the other files; this is the "what every knob actually does" backbone.

## Echo Styles (full list, with the ones that matter for a tape/drone rig)
30+ styles. Tape/lo-fi & ambient relevant:
- **Master Tape** — Ampex ATR-102 @ 30 ips; hi-fi, smooth, saturates nicely.
- **Studio Tape** — ATR-102 @ 15 ips; subtle distortion + HF compression (the "tracked to tape" sound).
- **EchoPlex** — EP-3 solid-state tape echo.
- **Space Echo** — Roland RE-201; warm + gritty. **Manual explicitly notes the RE-201's self-oscillation
  is achievable via the Feedback control.** (The drone trick.)
- **Tube Tape** — modern tape echo, lots of high-mids + distortion.
- **Cheap Tape** — bright, very compressed consumer-grade tape.
- **Memory Man** — EHX Deluxe Memory Man; warm low-bandwidth chorus echo.
- **DM-2** — Boss bucket-brigade; warm, resonant, punchy but clean.
- **TelRay** — oil-can delay; dark, warbling/wavering.
- **Binsonette** — Binson Echorec; warbly, compressed (the Pink Floyd sound).
- **Ambient** — distortion + diffusion; "great for long feedback loops and solo instruments."
- **Diffused** — "great for creating ambient reverb-like echo effects."
- **Splattered** — "highly reflective reverb effect."
- **Verbed** — echo with a cheap-verb chaser; "very responsive to Feedback and Saturation."
- **Limited** — built-in limiter; "great when coupled with high feedback settings" (tames runaway).
- Plus: Saturated / Fat / Distressed / Distorted / Queeked (color/distortion styles), and clean
  Digital Delay, Analog Delay, chorus/vibrato styles (CE-1 Chorus, Analog Chorus, Vibrato).

## Main-panel controls (the ones with non-obvious behavior)
- **Saturation** — tube/tape compression + distortion on the *delay only*. Behavior depends on the style:
  on Studio Tape it adds odd low/mid harmonics + HF compression ("automatic de-essing on the echo");
  on Limited it acts like a limiter threshold (pumping). Manual: when building a custom style, leave the
  *front-panel* Saturation at 12 o'clock and set saturation in the Tweak menu.
- **Input/Output** — only affect the echo signal, never the dry. Replicate analog input-stage behavior;
  "keep it clean or make it dirty and messy." Sound very different per style.
- **Feedback** — number of repeats. "Too high / near max easily drives EchoBoy into 'runaway' mode" =
  the RE-201-style self-oscillation. **High feedback boosts output level significantly — be careful.**
- **Prime Numbers switch (up):** slightly de-aligns repeat times to minimize resonance build-up. Most
  noticeable in Dual/Rhythm. **Especially useful with short delay + feedback, chorusing/flanging, and
  reverb-like effects** — keeps repeats from stacking resonance. (Key for clean ambient washes.)
- **Low Cut / High Cut** — shape the repeats per the current style; High Cut "darkens" (tape roll-off).
- **Groove** — CCW = Shuffle, CW = Swing; 12 o'clock = zero.
- **Feel** — shifts the whole delay output ahead/behind the beat (the "pocket"), not just the groove.

## Single-mode Tweak menu
- **Width** — stereo spread; past 3 o'clock uses out-of-phase info for a "beyond the speakers" spread.
- **L/R Offset** — small ms delay diff L vs R; max **25 ms (default 8 ms)**. Small = tighter but may
  phase; large = looser, less phasing. Only audible with Width up.
- **Accent** — bipolar (12 o'clock = off). Alternates repeat loudness; CW emphasizes on-beat (1,3,5),
  CCW emphasizes off-beat (2,4,6) for syncopation. Turn feedback up + use 1/8 or 1/16 to hear it.

## Dual-mode Tweak extras (great for evolving stereo drones)
- **FB Mix** — cross-feeds Echo 1↔Echo 2. At 12 o'clock equal cross-feed = "a great way to get dense,
  reverb-like echo sounds." At max = full "cross" mixing → cross-pollinated/syncopated tails. (Only with
  front-panel Feedback up.)
- **FB Bal / Balance** — tilt feedback or level L vs R.

## Rhythm-mode Tweak extras
- **Shape** — amplitude envelope across taps: Decay (natural decay, "reverb-like"), Reverse (80s backwards
  echo), Swell, Fade, **NonLin** (random cluster, modeled on the AMS RMX16 NonLinear reverb).
- **Repeats** — sets exact number of audible taps independently of Feedback → precise control of both
  level *and* timing of each echo.
- **Warp** (replaces Accent when Time button is selected) — "time clustering": pulls all taps toward the
  start (CCW) or end (CW) of the pattern. Great with Shape for bouncing-ball / robotic effects.
- **Pan Shape** — Double/Center/Alt/Sweep/Pan. "Double" halves taps to 8, each a stereo output with
  independent modulation → "really meaty, thick, rich chorus."
- **Length** — pattern length 1–8 beats (odd values = odd-meter patterns).

## The Style Editor (the real deep end — the tape/generation-loss engine)
- **3-band EQ + Gain/Decay per band:** Gain = tone of the *first* repeat; **Decay = how the tone changes
  with each successive repeat (needs Feedback up).** Negative High Decay → each repeat darker (tape
  generation loss); positive → each repeat brighter. Set independently per band for "a million" evolving
  tonal trajectories. This is the heart of authentic tape-echo decay.
- **Diffusion** — reverb-style "smear"; each pass through the filter blurs the repeat. Short echo time +
  diffusion = room reverb; long echo time + feedback + diffusion = plate/hall. Too much = metallic/
  flanger-resonant. Highly interactive with Size, Loop/Post, Echo Time, Feedback.
- **Size** — character of the diffusion; small = subtle/phasey, large = more reverb-like.
- **Loop/Post switch** — Post = each repeat equally diffused (diffusion at the end of the chain). **Loop =
  diffusion inside the feedback loop → each successive repeat gets progressively more diffused** (the
  evolving, washing-out-into-reverb behavior — the ambient money setting).
- **Wobble** (the tape wow/flutter engine):
  - Depth (full CCW = off), **Rate** (slow→fast pitch wobble), **Shape** (Triangle / Sine / Square /
    Random Walk / Random S&H). Random Walk + Random S&H = analog randomness; slow rate + low depth =
    "sauntering randomness" of vintage tape units.
  - **FB / Out toggles:** FB = wobble applies to initial echo *and* feedback repeats; Out = wobble on the
    wet signal only (dry untouched) → "truly wild," very resonant at high levels.
  - **Sync knob** (12 o'clock = all paths identical): CCW = paths wobble out of *rate-sync* (each path
    different rate); CW = paths stay rate-synced but go out of *phase* (R pitches up while L pitches
    down). Both give rich choruses/flanges/modulated delays.
- **Tweak-menu Saturation:** two extra knobs — **Decay Sat** (saturate the delay only) and **Out Sat**
  (saturate the total signal), each with a type menu: Clean / Tape / Warm / Pump / Dirt / Hard Limit /
  Soft Limit / Warm Limit / Bright Limit. (Tape = HF compression + low-end distortion of quality tape.)

## Echo Time behavior worth knowing
- Turning the Echo Time knob in real time produces the **analog pitch-slide** (varispeed) — automating it
  = pitch-slide transition effects. Note values smoothly crossfade; Time (ms) values pitch-shift.
- Very short times: 0–10 ms = flanging; 10–50 ms = chorus/doubling; 100–200 ms = slapback.

https://www.youtube.com/watch?v=WQ_FJ2ntRHs
XNB · RC-20 Retro color from XLN audio, the best LOFI plugin you can buy - Plugin guide · 2022-03-17 · 27 min

The deepest single control-by-control walkthrough captured. Cleaned from auto-subs.

## Overview
RC-20 is a very complete plugin — it can do noise, distortion, a little reverb. One of the presenter's favorite plugins. The video starts from an INIT patch and goes through every stage left-to-right (the order audio flows through the modules).

## Noise module
Click the module title to turn it on/off. Many noise TYPES: vinyl, tape, DC (which is "transformer"), VHS, and even the "JP8 / Jupiter-8 white noise" of the synthesizer. Each type sounds distinctly different. Vinyl = classic record crackle; tape = much darker/different; DC/transformer, VHS, etc.

Controls:
- **Routing** — by default the Master EQ (post-EQ, which comes after everything) cuts the noise too. The routing option means the EQ will NOT cut the noise — the noise is left unaffected by the post-EQ. Useful when you want noise "playing in the background" as a standalone noise machine independent of the EQ shaping the rest.
- **Tone** — darker vs brighter; it's essentially an EQ/boost on the highs (a lower/duller noise to the left, brighter to the right).
- **Follow** — an envelope follower. By default noise is constant (always there). Follow makes the noise listen to the incoming signal and move WITH it — e.g. add a little noise only at the tail of the snare and kick. Higher = sharper response.
- **Duck** — a compressor. It compresses/evens out the peaks of the noise so loud transient-driven bursts get tamed; gives a more even, compressed noise floor. (Some noise types like vinyl have loud "pops" that vary in volume — Duck evens them.)
- **Flux** — a randomized feature (present on every module). On vinyl it makes the crackle go "crazier"/more random, more natural movement vs the constant default.

## Distort module
The saturation/distortion stage. Several distortion TYPES (not a huge number but "enough"), e.g. tubes (warmer as you push it). Pushing it up raises the output volume, so there's a **gain-adjust** to compensate so you don't clip. Changing the distortion type changes the character a lot.

Controls:
- **Mix** — blend dry/distorted (parallel saturation).
- **Focus filter** — like a multiband: focus the distortion on a frequency range, e.g. distort only the highs of the drums while the lows stay consistent and clean.
- **Flux** — adds variation/movement to the distortion (clearly audible as the drive moves around). Combined with noise = "a wonderful, very lo-fi sound."

## Digital module
A different type of saturation = digital. Essentially a **bit crusher**. The central slider goes between **Rate** (sample-rate reduction) and **Bits** (bit-depth reduction — behaves more like a distortion/saturation). You can use a bit of both.

Controls:
- **Focus / Cut** — focus filter applies the crushing to a frequency range only (e.g. only the lows, "less annoying"). The **Cut** mode filters out whatever is outside the range; disabling Cut makes it work like the distort focus (crush only the focused band, pass the rest clean).
- **Smooth** — smooths out the rate reduction so the high frequencies are smoother/less harsh; "very lo-fi."
- **Mix** — blend.
- **Flux** — randomizes rate/bits ("really weird").

## Wobble module (Wow + Flutter — PITCH modulation)
Tape-style pitch instability. The presenter demos on a bass.
- **Wow** = slow detuning pitch modulation; a visual shows the detuning. Good as subtle pitch modulation on a synth.
- **Rate** — speed of the wow.
- **Flutter** — a faster, slightly different-sounding modulation. The Wow↔Flutter slider blends between them: at 50% you get a sine-ish wow going up/down with the faster flutter riding inside it.
- **Stereo** — spreads the modulation across L/R (it shows the left/right speakers doing it), makes it wider. Too much = obviously warbly; dial the blend down for subtle.
- **Flux** — randomizes it for a more natural/realistic wobble (the constant LFO becomes more tape-like).

## Magnetic module (tape WEAR — VOLUME modulation, NOT pitch)
"Magnetic" because tape recording used magnets. Simulates the wearing of the tape and the magnet — more wear = inconsistencies in the volume/balance ("it sounds crappy" at extremes — that's too much wear).
- **Wear** (main knob) — volume inconsistency from tape wear; up/down volume fluctuation. Works mono or stereo.
- **Dropouts** — extreme volume drops, like equipment that needs servicing/maintenance. Random, can be used as an effect.
- **Flutter** — same family as the Wobble flutter but here it's a VOLUME flutter (the presenter notes Magnetic-flutter and Wobble-flutter are "related — both tape-related"). Subtle by default; up = more obvious; never constant (and shouldn't be).
- **Flux** — adds the randomness so it isn't constant.

## Space module (reverb)
The reverb side. A nice, fairly large "shimmer-ish"/synth-y reverb.
- **Decay** — size/length; large by default; lower it to get into "room" territory but it stays quite large.
- **Pre-delay** — standard.
- **Stereo / mono**.
- **Focus** — like an EQ for the reverb: choose which frequencies get reverb (e.g. only highs, or full spectrum incl. lows).
- **Flux** — least noticeable of all the modules' flux.
- Honest take: "the plugin market is filled with good reverbs — this isn't my favorite standalone reverb, but it works very well BLENDED with the other modules."

## Master section
- **Magnitude** — the master "blend." Everything is at 100% by default; pull Magnitude down and it brings ALL modules and the master controls down at once (a single macro instead of riding every knob). The "how much lo-fi" master.
- **Input gain** — drive harder going in (this is a saturation device, so more input makes it react harder).
- **Output gain**.
- **Width** — widens the stereo (Space and stereo content). Magnitude also scales width and gain.
- **EQ** — post EQ. Tone (darker/brighter) with two modes: a high-shelf mode or a narrower mid mode. Standard low-cut and high-cut shelves. One low-cut option is a plain low shelf; another adds a resonant low-end bump at the bottom. The high-cut has a soft option and a more aggressive option. (Manual doesn't state pole/slope.) Remember the EQ is POST — it cuts everything coming out of the modules unless you used the Noise "post/routing" option.

## Presets & the dice
Preset browser has many good presets. Nice touch: when saving a user preset, there's a **randomized NAME generator** (a dice for the name) if you can't think of one.

## Verdict
"Worth every penny, one of my favorite plugins. Called Retro Color but you don't have to use it retro — works on modern productions too. A must-have."

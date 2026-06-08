# Pedal, Amp, and Cabinet — Live's Guitar Color Chain

**Scope:** daw
**Source:** Deep-research synthesis (2026-05) — Ableton Live 12.x — verify before treating as authoritative
**Canonical references:** Ableton Live 12 Reference Manual — Pedal, Amp, Cabinet; Sound on Sound *Amp & Cabinet FX In Live*; MusicRadar Live 10 Pedal coverage
**Tags:** `daw-ableton`, `live-12`, `device`, `pedal`, `amp`, `cabinet`, `guitar`, `reamping`, `mixing`

---

## What the guitar trio is, and why non-guitarists should care

Pedal, Amp, and Cabinet are Live's stock guitar-color chain — three Softube-modelled devices designed to be patched in sequence to take a clean DI guitar from "plugged into the interface" to "mic'd amp in a room." Amp and Cabinet have shipped in Live Suite since Live 9; Pedal arrived in [Live 10](https://www.musicradar.com/how-to/ableton-live-10s-new-pedal-device-in-action). In Live 12 the chain is unchanged but is now joined by [Roar](https://www.ableton.com/en/manual/live-audio-effect-reference/) (a multi-stage saturator) and the [Drift](https://www.soundonsound.com/techniques/ableton-live-drift-synthesizer) synth's own saturation stage, which means Pedal/Amp/Cab are no longer the only character-coloring options. They remain the right reach for amp-style nonlinearity — particularly for synth bass, drum buses, and vocals where a "miked cab" feel sells the source better than a transparent saturator. As Sound on Sound puts it, ["You shouldn't overlook Amp and Cabinet even if guitar is not your thing."](https://www.soundonsound.com/techniques/amp-cabinet-fx-live)

## Pedal — three modes for three flavors of dirt

Pedal models three circuit-level stomp-box archetypes selected by a button row: [**Overdrive** (warm and smooth), **Distortion** (tight and aggressive), and **Fuzz** (heavy and broken / "broken amp")](https://www.ableton.com/en/manual/live-audio-effect-reference/). Each mode has its own gain-staging behavior. Overdrive responds dynamically — soft passages stay cleaner, hot input drives harder — which is what makes it the most musical choice for sustained sources like vocals or pads. Distortion clamps harder and faster, useful for grit you want to sit still in the mix. Fuzz collapses the dynamic range almost entirely and adds a square-wave-ish "buzz" — used judiciously, it's a [characterful drum-bus tool](https://warpacademy.com/pedal-in-live-10-ableton-tutorial/). All three modes are post-distortion EQ'd via a three-band tone stack described next.

## Pedal's tone shaping — Sub, Bass, Mid, Treble, output

Pedal's tone section sits *after* the distortion stage, so it sculpts harmonics that were just generated. The **Sub** switch toggles a low-shelf boost below ~250 Hz — useful for retaining low end that's typically scooped by amp-style clippers. **Bass**, **Mid**, and **Treble** form a three-band EQ; [Treble is a shelf at ~3.3 kHz](https://obedia.com/how-to-use-the-ableton-live-overdrive-audio-effect/) and the **Mid Frequency** switch picks the Mid's center and Q (narrower at low setting, broader at high). The **Output** knob compensates for the volume boost distortion typically introduces — match perceived loudness to bypassed before judging tone. **Dry/Wet** at the bottom is the parallel-distortion knob: a Pedal returns to Dry at 50/50 already covers most "smashed parallel drum bus" use cases without a separate Return track.

## Amp — the seven physical-model amplifiers

Amp emulates seven guitar amps via Softube physical modelling, selected from a button row at the device's left. The [official model list](https://www.ableton.com/en/manual/live-audio-effect-reference/) is: **Clean** (60s "Brilliant" channel, British Invasion clean), **Boost** (same amp's "Tremolo" channel, edgy rock), **Blues** (70s bright amp), **Rock** (a classic 45-watt 60s head — the most-reached-for of the bunch), **Lead** (modern high-gain "Modern" channel), **Heavy** ("Vintage" channel of the same high-gain head), and **Bass** (70s PA-style amp with strong low end and high-volume fuzz). The architecture deliberately copies real amps: **Gain** drives the preamp into nonlinearity; **Volume** is the power-amp stage; **Bass/Middle/Treble** are interactive tone-stack controls (moving one *changes* the others, as on a real amp); **Presence** sits above Treble. The **Output** switch chooses Mono or Dual (stereo); Dual uses more CPU and processes channels separately, which matters for stereo synth pads but is overkill for mono guitar DIs.

## Cabinet — five cabs, three mic positions, two mic types

Cabinet emulates [five guitar cabinets, named by speaker count × inches](https://www.ableton.com/en/manual/live-audio-effect-reference/) (e.g., "4x12" = four twelve-inch speakers). The **Microphone** chooser sets distance and angle: **Near On-Axis** (bright, focused — the SM57-on-the-grille sound), **Near Off-Axis** (resonant, slightly darker — the same mic angled off the cone), and **Far** (room character, more low-mid body). The **Mic Type** toggle selects **Dynamic** (grittier, handles high SPL — close-mic standard) or **Condenser** (more accurate, typical for distance miking). Output offers Mono or Dual. **Cabinet is paired with Amp** — Live's manual notes the two are "normally used together" — but useful effects emerge from running them independently (e.g., Amp alone for clean preamp warmth, Cabinet alone as a 1x12 colorbox on a kick drum).

## The canonical chain order

The Live default is **Pedal → Amp → Cabinet**, mirroring real signal flow: stomp boxes before the amp's input, cab miked at the output. Within this, the producer choices are:

- Pedal optional — Amp's Gain alone covers light overdrive; reach for Pedal when you want a *specific* pedal flavor (Fuzz especially) or to push the amp's front end harder than its Gain knob will go.
- Cabinet always recommended after Amp — the Amp on its own sounds buzzy and undamped because real cabs are aggressive low-pass filters.
- Place **Auto Filter** or **EQ Eight** *before* Pedal to shape what gets distorted (HPF below 80 Hz keeps the Fuzz from getting flubby on synth bass).
- Place **EQ Eight** or **EQ Three** *after* Cabinet to balance the mic'd sound into the mix — typically a slight high-shelf cut and a mid scoop.

## Reamping a DI guitar inside Live

The typical workflow: record a clean DI through your interface's instrument input to an audio track. Insert Pedal → Amp → Cabinet on that track. Now the chain is non-destructive — change amp model, swap pedal mode, move the mic to Far — without retracking. When committed, **Freeze and Flatten** (or **Bounce in Place**, Live 12) renders the chain to audio and frees the CPU. Keep an unprocessed DI on a parallel track as insurance — re-amping decisions made at 2 a.m. rarely survive next-day listening. For double-tracked rhythm guitar, hard-pan two passes L/R and reach for slightly different Amp models (e.g., Rock left, Blues right) for natural width — copying the chain and identically processing both sides collapses the stereo image.

## Non-guitar use 1 — synth-bass character

Sub-heavy synth basses (Operator FM bass, Drift sawtooth bass) often need *distortion* to translate on small speakers — the upper harmonics generated by clipping are what laptops and phones reproduce when the fundamental drops below their cutoff. The standard move: send the bass to a Pedal in **Overdrive** mode with Gain around 30–50% and Sub *off* (you want harmonics, not more sub), or to a Pedal → Amp **Bass** model chain. Use **Dry/Wet** around 30–50% to retain the clean fundamental. Watch the Mid switch — narrow Mid setting boosted at a specific frequency creates the "growly" or "honking" bass character used in dnb and dubstep.

## Non-guitar use 2 — drum-bus coloring

Routing a drum bus through Pedal or Amp+Cabinet adds analog-style nonlinearity that the [Drum Buss](https://www.ableton.com/en/manual/live-audio-effect-reference/) device doesn't quite reach. Sound on Sound's recommended workflow: [insert a **Gate** before Amp to truncate ambient hits, then add Ping Pong Delay after the chain for rhythmic motion](https://www.soundonsound.com/techniques/amp-cabinet-fx-live). For a "smashed room" parallel sound, send drums to a Return track loaded with Pedal (**Fuzz**, Gain ~70%) → Amp (**Heavy**) → Cabinet (**Far** mic) and dial the Return up to ~20% behind the dry drums. The Far mic position is what sells the "in a room" character; Near On-Axis collapses too much for parallel use.

## Non-guitar use 3 — vocal saturation and "telephone" effects

For a vocal warmer than Saturator but less destructive than Roar, try Amp **Clean** with Gain at ~30%, Volume compensating output, Treble cut slightly. This adds 2nd-harmonic warmth without obvious distortion. For overt effects — verse vs. chorus contrast, a "bullhorn" pre-chorus — Pedal in **Distortion** mode followed by an EQ Eight with everything below 300 Hz and above 3 kHz steeply rolled off produces the classic "telephone vocal." Wet the effect via clip automation or a Modulator-mapped Dry/Wet so it only hits the chosen lines. Always automate Output to match perceived loudness — distorted lines are louder than clean ones at the same fader.

## Non-guitar use 4 — electric piano and Wurli

Rhodes and Wurlitzer-style EPs often want a slight cabinet color even when running clean. The Sound on Sound recipe: [Cabinet in **Dual mode** to preserve tremolo's stereo movement, **EQ Three** before Amp boosting low/mid and after Amp cutting highs](https://www.soundonsound.com/techniques/amp-cabinet-fx-live). The Amp model choice for EP is usually **Blues** or **Clean** — keep Gain low (under 25%) and let Volume do the loudness work. For overdriven Wurli (the "Mr. Soul" or Supertramp sound), step up to **Boost** or **Rock** with Gain ~50% and watch the Treble — EPs already have aggressive 2 kHz energy that Amp will exaggerate.

## CPU, output mode, and the freeze decision

All three devices are Softube physical models, which means they cost meaningful CPU compared to native Live effects. **Output: Mono** halves the cost relative to **Dual** — use Dual only when stereo source matters (stereo synth, stereo guitar DI, ping-pong'd drum bus). On a busy session, **Freeze** any track whose Pedal/Amp/Cab chain is committed; **Flatten** when you're sure. Freezing also resolves the rare PDC quirks that Softube devices can introduce when chained with other latency-inducing plugins. Bounce in Place (Live 12) gives you a Flatten that preserves the source — usually the better commit move because it lets you bring back the unprocessed take if a later mix decision reverses course.

## Limits and IR-based alternatives

The Amp/Cabinet pair is a *physical model*, not an IR convolution. That means it captures dynamic amp behavior — sag, bias shift, feedback into resonance — but lacks the cab-specific room and speaker fidelity of a high-quality impulse-response loader. For genres where the cab is the sound (modern metal, ambient post-rock), pairing Amp's preamp with a third-party IR loader (Cab-only, with bypassed Cabinet) often translates better. [Convolution Reverb Pro](https://www.ableton.com/en/manual/max-for-live-devices/) (Max for Live Essentials) can load cab IRs in a pinch. Conversely, when you don't have an IR library, Live's Cabinet is the only stock option that captures speaker resonance — Saturator and Roar do nothing about the post-amp acoustic stage.

## When to pick which device — quick decision

- Clean DI guitar needs to sound recorded → **Pedal → Amp → Cabinet** in that order.
- DI guitar but you don't want a "guitar" sound → just **Amp** alone (no Cabinet) for preamp warmth.
- Bass guitar DI → **Amp** *Bass* model + **Cabinet** 4x10 + DI parallel for low-end retention.
- Synth bass needs upper harmonics → **Pedal** alone, Overdrive mode, Sub off.
- Drum bus coloring → **Pedal** Fuzz on a parallel Return, or **Amp** + **Cabinet** with Gate first.
- Vocal "telephone" or bullhorn effect → **Pedal** Distortion → EQ Eight band-pass.
- Electric piano → **Amp** Clean/Blues + **Cabinet** Dual, low Gain.
- You want amp character but the CPU budget is tight → **Saturator** (Soft Sine or Analog Clip curve) instead; commits the "amp-ish" feel without Softube cost.

## Cited Retrieval Topics

- "how do i make a clean DI guitar sound like a real amp in ableton"
- "what's the difference between pedal overdrive distortion and fuzz in live"
- "what are the seven amp models in ableton live amp"
- "how do i use cabinet on drums in ableton"
- "best way to add distortion to a synth bass in ableton"
- "telephone vocal effect with pedal in ableton live"
- "should i use amp or saturator on a drum bus"
- "how to reamp inside ableton live 12"
- "ableton pedal amp cabinet chain order"
- "how much cpu does ableton amp use"

## Sources

- [Live Audio Effect Reference — Ableton Reference Manual Version 12](https://www.ableton.com/en/manual/live-audio-effect-reference/)
- [Sound on Sound — Amp & Cabinet FX In Live](https://www.soundonsound.com/techniques/amp-cabinet-fx-live)
- [MusicRadar — Ableton Live 10's new Pedal device in action](https://www.musicradar.com/how-to/ableton-live-10s-new-pedal-device-in-action)
- [OBEDIA — How To Use The Ableton Live OVERDRIVE Audio Effect](https://obedia.com/how-to-use-the-ableton-live-overdrive-audio-effect/)
- [OBEDIA — How To Use The Ableton Live AMP And CABINET Audio Effects](https://obedia.com/how-to-use-the-ableton-live-amp-and-cabinet-audio-effects/)
- [Warp Academy — How to Distort Bass, Drums & Vocals with Pedal in Live](https://warpacademy.com/pedal-in-live-10-ableton-tutorial/)
- [Sound on Sound — Ableton Live Drift Synthesizer](https://www.soundonsound.com/techniques/ableton-live-drift-synthesizer)
- [Ableton Reference Manual — Max for Live Devices](https://www.ableton.com/en/manual/max-for-live-devices/)

See also: `corpus/mixing/eq-fundamentals.md`, `corpus/recording/tracking-vocals-in-the-small-studio.md`, `corpus/daw/ableton/devices/saturator-vs-roar.md` (planned), `corpus/daw/ableton/timeless/reamping-through-pedal-amp-cabinet.md` (planned)

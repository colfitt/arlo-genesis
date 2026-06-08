# UAFX Del-Verb — App Voicings (the hidden depth)

Source of truth: **[UAFX Preset and Voicing Lists — UA Support](https://help.uaudio.com/hc/en-us/articles/8272165765012-UAFX-Preset-and-Voicing-Lists)** (page blocks scripted fetch; names/descriptions below were pulled verbatim from that page's indexed text via web search, 2026-06). Cross-checked against the [Del-Verb manual](https://help.uaudio.com/hc/en-us/articles/13621234251284-UAFX-Del-Verb-Ambience-Companion-Manual) and the Thomann gear-check walkthrough (`transcripts/thomann-gear-check.md`).

## How voicings work (verified)
- A **voicing** = a factory-configured sound applied to one of the 6 effects. There are **no onboard user presets**, but voicings are the substitute: they change the *fundamental character* (reverb decay/tone/pre-delay/dwell, alternate tape machines, pitched-repeat delays, ping-pong, glide) that the **hardware knobs cannot reach**.
- You **assign** a voicing per effect in the UAFX Control app (Bluetooth). You **cannot edit a voicing's internal parameters** — assign-only, pick from the factory list (confirmed by Guitar Bonedo + Thomann).
- **Total pool ≈ 126 voicings** across all 6 engines (Thomann counted on beta firmware; "~12 per effect" is the per-mode feel). Number may grow with firmware.
- **The assignment is STORED IN THE PEDAL, not the app** (Thomann, verbatim). Once you pick a voicing for a toggle position it persists there until changed — so you can pre-load 6 voicings (one per Delay mode + one per Reverb mode) and then play phone-free. Knob + tempo settings are also remembered per effect when you switch types.
- Each effect type has a **"Default [type]"** voicing as its factory baseline.
- Recall via MIDI: selecting a delay/reverb *type* over CC loads whatever voicing you assigned to that type (you cannot pick among voicings by CC beyond the type itself — the voicing rides with the type assignment).

---

## DELAY voicings

### Tape EP-III (tape echo)
- **Default Tape EP-III** — used/warm tape & machine at ~500 ms, ~5 repeats (factory baseline).
- **Bright Spank** — brighter-era preamp on the tape head.
- **Broken Bottom** — no bass response in the circuit (thin/lo-fi repeats).
- **Dark Tape n Preamp** — dirty heads + adjusted azimuth for an extremely dark tape sound.
- **Dirty Heads** — treble and bass cut in the head-circuit path.
- **EP with 5th Pitched Buckets** — EP-III routed into the DMM with a pitched-5th delay swing (harmonized echo). *(DMM stage is hardwired; you shape the EP-III with the knobs.)*
- **EP with Chorus Buckets** — EP-III routed into DMM with a classic chorus echo.
- **EP with octave pitched buckets** — octave-shimmer pitched repeats (named on Thomann demo).

### Analog DMM (bucket-brigade)
- **Default Analog DMM** — baseline BBD delay.
- (Several BBD variants exist in the pool; the EP-into-DMM hybrids above live under the Tape list. Bipolar Mod knob: left = Vibrato, right = Chorus; Color past noon = overdrive.)

### Precision (clean digital)
- **Default Precision** — studio-standard long delay, no coloration on repeats (factory baseline).
- **Delay Tempo Glide** — drags pitch when moving to a new delay time (the only Precision mode where time changes alter pitch — a tape-style glide).
- **Stereo Ping Pong** — repeats bounce L↔R.
- **Stereo Ping Pong Hi-Cut** — L↔R ping-pong with 3.5 kHz low-pass + 130 Hz high-pass in the feedback loop (tames buildup; great for ambient washes).
- **Stereo Ping Pong Vibrato** — as above + LFO vibrato on the repeats.

---

## REVERB voicings

### Spring '65
- **Spring Stock Classic A** / **Stock Tank A** — classic '65 combo-amp spring (factory default).
- **Spring Tube Drive A** / **Spring Tube Drive B** — custom tube-drive into the tank for more sizzle/compression (two hand-picked tanks A/B).
- **Spring C Rotato** — spring with lush rotary-speaker vibrato.
- **Symphonic Reverb** — cavernous 'verb with pitch-shifted modulation.

### Plate 140
- **Studio standard Plate A** — ~3.0 ms (pre-delay) plate, the factory default.
- (Additional plate-A/B variants with different decay/pre-delay in the pool.)

### Hall 224 (the ambient workhorse for this rig)
- **Default 224 Hall** — Room A set for long ambient reverb tails (factory default).
- **Fractal Forest** — 224 Small Hall A, **maximum mid decay, 150 ms pre-delay** (big, slightly held-back bloom).
- **Swimmy and Shakey** — 224 Small Hall A, lots of mid decay, **150 ms pre-delay** (modulated/wobbly tail).
- **Cascade 224** — 224 Large Hall B with lots of mid + treble decay (bright, huge).
- **Dark N Dusty Trail** — 224 Large Hall B with lots of pre-delay (dark, distant wall).
- **Shimmeron** — 224 Chamber with maximum mid decay (shimmer-leaning hall).
- **Hallelujah Stack Verbs** — Small Room 224 + Large Hall 224 stacked for complex decays (best clean/fingerpicked; from a Buckley "Hallelujah" cover voicing).

> **Drone/doom/shoegaze picks for this rig:** *Dark N Dusty Trail* (dark distant wall), *Cascade 224* (big bright bloom), *Fractal Forest* / *Swimmy and Shakey* (modulated halls with pre-delay) on Hall 224; pair with *Stereo Ping Pong Hi-Cut* or *EP with octave/5th pitched buckets* on the delay side for a controlled shimmer-wash. *Symphonic Reverb* on Spring '65 is the surprise pitch-modulated big-verb option.

*(Coverage note: this is a representative, sourced sample of the named voicings — not guaranteed to be all ~126. The complete current list lives only inside the UAFX Control app and the support page above. Verify exact names in-app when configuring; firmware may add more.)*

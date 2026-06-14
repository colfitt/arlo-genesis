https://www.youtube.com/watch?v=Ysds84M6_9k
XNB · The Arturia KORG MS-20 complete guide walkthrough tutorial · 2022-10-10

Full ~23k-word patch-by-patch walkthrough of Arturia KORG MS-20 V. Distilled to the parts that matter for drone / external-audio / patch-bay use.

== Oscillators & pre-wiring ==
- Two VCOs, each with a waveform selector; OSC1 also does pulse-width modulation (PWM). The basic pre-wired signal path is "easy peasy" — you get sound immediately before you ever touch the patch bay. The MG (LFO) → pitch gives instant vibrato with no cabling.
- The MG waveform is *continuously variable* (not fixed shapes): one knob morphs saw → triangle → ramp on one output, and narrow-pulse → square → narrow-pulse on the other (square output is on the patch bay).

== The two filters (HPF + LPF in series) ==
- Highpass then Lowpass, each with Cutoff + Peak (resonance). Push Peak up and you visibly/audibly get the resonant peak ringing at the cutoff — "especially when you move it." This is the screaming-filter character; drive Peak toward self-oscillation for a pure tone.
- Both filters can be modulated by an envelope (EG1 or EG2) or, via the patch bay, by an external CV. Cutoff Mod Sidechain lets MIDI velocity brighten notes (play harder = brighter).

== The patch bay (the whole point) ==
- "Looks confusing but it's really not." Hovering a patch point lights up where it goes. Go through it one by one.
- TOTAL = patch into "pretty much all of this section at once" (both VCOs pitch + both filter cutoffs); the MG/T.EXT knobs set how much. Patch the MG square wave into TOTAL and you modulate everything with the square instead of the triangle.
- EXTERNAL IN: when you patch a source here (e.g. the noise generator, or external audio) it gets *blended with the oscillators before the filters* — "you get a blend of both, something you can only do when using the patch ins and outs." You can then filter the blend, cut what you don't want, and send it on.
- Noise generator (pink/white) is a key drone/texture source. Straight from the noise jack it's "super loud" with no level control — so the smarter move is to run noise through the ESP first (which has a level + bandpass) so you can tame it, cut lows and highs, then send it on.

== The ESP — External Signal Processor (most important patch-bay section for this rig) ==
- Described as "one of the most important parts of the patch bay." It's where you bring an external sound (or an internal sound) under control before using it.
- Chain: SIGNAL IN → Amplifier (Signal Level — crank it up) → Bandpass Filter (Low Cut / High Cut to remove extreme lows/highs) → taps out at OUT points.
- F-to-V (Frequency-to-Voltage) Converter: "grab some sound source and convert it to voltage so you can use it as a modulation source" / pitch-track it. (The narrator is candid: on the original hardware this let a guitar play the synth; in a plugin you typically feed it audio for the same effect.)
- Envelope Follower (ENV OUT): "this will listen to whatever incoming signal and create an envelope out of that... it doesn't matter if it's a sound from here or a sound from an external like a side chain — it will listen to it and then create an envelope and follow." → route ENV OUT to a cutoff for a self-playing wah/wall.
- TRIG OUT + Threshold Level: when the incoming signal passes the Threshold, it fires a trigger. The Threshold knob fine-tunes catching the trigger: too low = everything triggers constantly; too high = it stays open / never triggers, "that's not gonna help." Use a short percussive sound to get a tight trigger; you can use the trigger as a clock for other things.

== Sample & Hold / VCA / utilities ==
- S&H is most useful fed by noise → outputs a new random voltage each clock pulse ("computer bleeps") — classic random-cutoff shimmer source.
- The patch-bay VCA can scale a *control voltage* (not just audio) automatically — useful for taming modulation depth.

== Takeaway for drone/processing ==
The ESP + EXTERNAL IN + self-oscillating filters are the trio. Noise (or external audio) → ESP (level + bandpass to tame) → filters near self-oscillation → envelope follower back to cutoff = a self-evolving filtered wall. The narrator stresses patience and experimenting; the pre-wiring gets you 80% there and the patch bay is where the "uncharted territory" lives.

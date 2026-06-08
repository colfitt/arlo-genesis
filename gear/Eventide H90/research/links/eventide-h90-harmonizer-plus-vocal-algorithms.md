https://cdn.eventideaudio.com/manuals/h90/1.11.4/content/algorithms/harmonizer-plus.html
eventideaudio.com (official H90 manual) · Eventide · firmware v1.10, announced 2025-04-29

# H90 Harmonizer+ vocal algorithms (the "vocoder-like" suite)

Added **free in firmware v1.10 (April 29, 2025)** via the H90 Control app, ported down
from the flagship **H9000**. Four algorithms — pitch correction, formant shifting, and
up-to-4-voice harmony with intelligent scale recognition. These are the headline "vocal/
vocoder-like" additions. (A later v1.12.x granular update added Cosmic Web/Glitch/
GrainMod/Stutter — separate; covered elsewhere.) Sources: official manual (params,
quoted below), [press release](https://www.eventideaudio.com/press-releases/eventide-expands-h90-pedals-capabilities-with-harmonizer-vocal-algorithms/),
[KVR](https://www.kvraudio.com/news/eventide-releases-harmonizer-and-vocal-algorithms-for-h90-pedal-63687).
Official intro video (music demo, no spoken params): https://www.youtube.com/watch?v=caepdHqAzY8

## VocalTune — pitch correction + EQ + compression
Quantizes pitch to a key/scale, from "snappy, robotic" hard-tune to subtle correction.
- **Root / Scale** — key + scale the input is quantized to
- **Tuning Reference** — reference point for the key/scale quantization
- **Quant Error** — lets small pitch variations through un-quantized (more natural)
- **Formant** — shift formants −600 to +600 c **without changing pitch** (chipmunk↔monster)
- **Tuning Speed** — robotic hard-tune ⟷ subtle correction (the "auto-tune effect" knob)
- **Bass / Treble** — shelving EQ, −18 to +12 dB / −18 to +12 dB
- **Threshold / Ratio (1:1–20:1) / Attack (0.1–100 ms) / Release (1–1000 ms) / Gain (−16/+12 dB)** — built-in compressor
- **Gate** — noise-gate threshold

## VocalShift — 3-voice harmonizer (independent pitch + formant per voice)
"Subtle doublings to expansive vocal ensembles."
- **Mix** (wet/dry), **Root / Scale**
- **Shift A/B/C** — pitch-shift interval per voice; **Formant A/B/C** — formant per voice
- **Formant Link** — auto-stretches formants in proportion to the shift interval (natural harmonies)
- **Gain / Delay (ms or tempo-synced) / Feedback / Pan A/B/C** — per voice
- **Detune** — equal up/down detune on Voices B & C (thickening)
- **Tuning Speed**, **Quant On/Off**, **Quant Error**, **Latency Mode (Low/High)**
- **Glide A/B/C + Rise + Fall** — pitch-glide performance control
- **Solo A/B/C** — solo a voice for fine-tuning
- Performance controls: **Root learn, Glide, Glide (M), Hold (M), Hold**

## VocalShiftMIDI — 4-voice, MIDI-controlled harmonizer
Play the harmony intervals from a MIDI keyboard (e.g. the rig's 61SL).
- **Unison Mix / Unison Formant (−600..600 c)**
- **Tuning Speed**, **Gate / Gate Attack / Gate Release**
- **Vibe Rate / Depth / Slew** — vibrato on the MIDI voices
- **Glide**, **Delay (ms/synced) / Feedback**, **Formant Link**
- **Spread (Narrow/Med/Wide)**, **Attack / Release** (voice envelope)
- **Hold** (Off = only sound while a MIDI note is held), **Velocity Sens**, **Bend Range**, **Auto EQ**, **Latency Mode**
- Performance: **Root learn, Freeze, Freeze (M)**

## Quadravox+ — 4-voice diatonic harmonizer w/ staggered delays + arpeggio
- **Unison Mix / Unison Formant**, **Key / Scale / Quantization**, **Formant Link**
- **Pitch Mix** (A+C vs B+D), **Shift A/B/C/D**
- **Delay** (4 staggered, A shortest) + **Division**, **Feedback / Feedback Path (early)**
- **Spread**, **Tuning Speed**, **Detune (±50 c)**, **Auto EQ**, **Glide A/B/C/D + Rise + Fall**
- Performance: **Root learn, Glide, Glide (Mom)**

## Why it matters for THIS rig (instrument, not just vocals — feed it banjo/baritone)
- **Formant-shift the banjo/baritone** (Formant, ±600 c) *without* repitching → talkbox/
  vocal-vowel textures on a string source; pair with Blackhole for a "singing wall."
- **Harmonize a mono drone** into a 3- or 4-voice chord with **VocalShift / Quadravox+** —
  diatonic, scale-locked, with per-voice Pan/Delay for a wide stereo bed (another banjo-as-
  chordal-engine route alongside Polyphony).
- **VocalTune as a creative effect:** crank **Tuning Speed** to the robotic/hard-tune end on
  a sustained baritone or sampled vocal for the auto-tune/"vocoder-like" sound the owner is
  after; back it off for gentle pitch-locking of the banjo lead.
- **VocalShiftMIDI** = play harmony intervals live from the **Novation 61SL MkIII** over a
  held note; **Glide/Hold** performance controls map to footswitches for pitch-rise swells
  and frozen vowel-drones.

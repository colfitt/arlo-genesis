https://www.youtube.com/watch?v=4f81OuOBq2I
Arturia (Glen Darcey, VP Product Management) · "Arturia Matrix 12 V tutorial part 2" · 2014-12-02
[Original V1 tutorial; architecture (voices/multi/FX/program-chain) carries to V2.]

Official walkthrough of the FX, the Voice/Multi page (the synth's real power) and program
chain. (Distilled from captions.) NOTE: filmed for the original Matrix-12 V — the V2 overhaul
re-skins UI / adds the modern FX rack, but the **voice-allocation and Multi architecture
described here are unchanged and are the key to big Matrix-12 textures.**

## Per-voice FX
**Two FX in series per voice** — click the slot name to pick the effect; toggle enable/disable.
Everything is MIDI-learnable (click MIDI, learn any param; KeyLab presets ship; build/copy/
export your own templates).

## Voice playback / Multi = the headline (★ key technique)
Each of the **12 voices** can have its own **MIDI channel, key zone, transpose, detune, volume,
pan, AND preset** → build a "Multi." This is what gives the Matrix-12 its signature.
- **Stereo rotation:** assign voices across the pan field, set a zone to **Rotate** mode → a
  single repeated note physically bounces around the stereo field as it cycles through voices.
  (Strip the attack/release/FX to hear it clearly.)
- **24-oscillator monster:** one preset = all voices on Zone 1, zone in **Unison-last** mode,
  every voice detuned a little, panned differently, some voices ±1 octave → "a 24-oscillator
  Oberheim, pretty big." (12 voices × 2 VCOs = 24 oscillators.) THE giant-wall recipe.
- **Layering:** split the 12 voices 6+6 across two zones, detune zone 2 → instant fat layer
  from one note.

## ★ The Michael Brecker "Original Rays" single-note-harmony trick
Sax legend Michael Brecker used the hardware Matrix-12 to play **harmonized patterns from a
single note** via an EWI (wind controller). Glen recreates it: per-voice **transpose** sets a
chord —
- Zone 1: 1 voice un-transposed.
- Zone 2: 3 voices at **+5th, +4th, +2nd**.
- Zone 3: voices an **octave down**, at **−5th, −4th, −2nd**.
- Plus 3 more detuned & panned voices in the same zone.
→ Play one note (or a 3-note C-scale) and get a full moving harmonized pattern out. For this
rig: a way to make the Matrix-12 itself voice the drone/pad chord from a single sustained note
(or from a banjo/MIDI single line).

## Vibrato / 5th–6th LFO + program chain
The vibrato generator (the extra LFO beyond the 5 per-voice LFOs) lives on the Voices page;
classically routed from **mod wheel → VCOs/filter** (enabled in Page 2). **Program Chain** page:
sequence presets (singles or multis) to recall via program-change messages.

# Antares Vocodist — Usage Guide

Vocodist is the bundle's vocoder — a **modulator** (the input voice/instrument) shapes a
**carrier** through a bank of bandpass filters, modelling a lineage of classic vocoders. For
this rig it's the **machine-choir / talking-drone** tool: vocode a sustained synth/VG-800/
Mellotron carrier with a played **banjo or voice** as the modulator → robotic vocal-texture
walls, then degrade. Good news for a Logic rig: **no AU-sidechain blocker** (unlike the MS-20 V)
— and the simplest path (internal carrier, voice-tracked) needs **no routing at all**.

---

## 1. Essential workflow

Insert Vocodist on the track carrying your **modulator** (banjo/voice/baritone) — the insert
audio always supplies the band/formant movement. The **carrier** = **Synth → Source**:
**Oscillator** (internal dual 8-voice) or **Side Chain** (external). Verified machine-choir
starting point (off the manual): a vintage editable **Model** (or Antares Voc-1), **Bands 8–12**
(fewer = more vintage/lo-fi), **Q ~5**, **Min/Max 100 Hz / 10 kHz**, **Retune Speed 0 +
Auto-Tune ON** (robotic snap), **Envelope: short Attack / long Release** (sustain), **Voice Mix
0** (vocoder only), **Warmth ~3 dB + Chorus + Smear** (ringing wall). The Noise section
(Sensitivity/Balance up, Color ~3500 Hz) adds the breathy fricative layer.
[links/vocodist-official-manual.md; transcripts/vocodist-official-walkthrough.md]

---

## 2. Carrier routing in Logic (the key practical answer)

Three paths, in confidence order:
- **A — internal osc, voice/Key-tracked (NO routing):** drop on the audio track, Source =
  **Oscillator**, Pitch Track = **Voice** or **Key**. The internal synth *is* the carrier and
  follows the input — zero MIDI, zero sidechain. **Fully verified**, and on its own it delivers
  the drone/machine-choir wall (**Key** mode = pick one drone note = instant talking-pad).
- **B — internal osc played by MIDI:** load Vocodist as the **Instrument** via **AU
  MIDI-controlled Effects → Antares → Auto-Tune Vocodist**; put the modulator on an audio track
  set to **"No Output"**; select it in Vocodist's **Side Chain** menu; Pitch Track = **MIDI**;
  record-enable and play the 61SL.
- **C — external carrier (a drone/VG-800/synth as the carrier):** route the carrier to a bus,
  select it as Vocodist's **Side Chain**, set Source = **Side Chain** (Oscillator greys out).
  Modulator stays on the insert track.

**Honest finding:** this is Logic's standard, long-established **AU-MIDI-controlled-Effects +
Side-Chain** mechanism that the whole Auto-Tune family uses — **no known Vocodist-in-Logic
blocker comparable to the Arturia MS-20 V AU-sidechain problem.** Path A needs no routing and is
the safest. Caveat: the manual defers exact sidechain setup to a JS-walled help page, so the
**B/C click-paths are triangulated** from the official Auto-Tune-Pro-in-Logic article (same
framework) + the official video (which demos C in Pro Tools) — confirm exact menu labels on your
install. [links/vocodist-logic-carrier-routing.md]

---

## 3. Signature settings (machine-choir / talking-drone / robotic walls)

- **Talking drone:** Source = Oscillator, Pitch Track = **Key**, pick the song's root → sustained
  vocoded pad on one pitch.
- **Robotic snap:** Retune Speed **0**, Auto-Tune ON, Voice Mix 0.
- **Wall/sustain:** Envelope Release high + **Smear** (ringing reverb), or **Freeze** to lock a
  vowel indefinitely.
- **Vintage/lo-fi grit:** fewer **Bands** + a **lower-order (wider) filter slope** (more band
  overlap).
- **Crowd/choir width:** Pitch Track = MIDI, **Voices 8 + Unison + Detune**, **Spread** for stereo.
- **Alien/scramble:** **Band Shift** X1/X2/X3 (criss-cross re-patch) + **Cross Mod / Voice Mod**
  ring modulation.
[transcripts/vocodist-official-walkthrough.md; links/vocodist-official-manual.md]

---

## 4. Rig-specific recipes

- **Banjo modulator + synth/VG-800/Mellotron drone carrier → wall → degrade:** carrier on a bus
  → Source = Side Chain; banjo on the Vocodist insert track; Bands 8, long Release, Smear, Warmth
  → out through **RC-20 / SketchCassette / Decapitator / Valhalla / EchoBoy**.
- **Voice carrier (inverse):** voice on the insert track, Pitch Track = Key (drone) or MIDI
  chords from the 61SL → robotic talking-pad.
- **Fastest, no-routing:** any played part on the insert track, Source = Oscillator, Pitch Track
  = **Voice**, pick a vintage model + preset.

---

## 5. Notable users & techniques
**No documented drone/doom/shoegaze/post-rock credit for Vocodist exists** — recipes are
capability/technique-based. Genre-adjacent anchor: preset designer **Buddy Ross** (Frank Ocean
collaborator) — same experimental-pop orbit as the Harmony-Engine **Prismizer**. The modeled
hardware's lineage (Dudley Voder 1937 → Wendy Carlos, Herbie Hancock, **Kraftwerk**, Daft Punk,
ELO) is the legit "Kraftwerk → Burial" vocoder-technique citation — but those are the *hardware's*
users, not Vocodist's. [links/vocodist-reviews-and-lineage.md]

## 6. Pitfalls / gotchas
- **Two separate decisions:** Source (Oscillator vs Side-Chain) and Pitch Track (Voice/MIDI/Key,
  which only applies to the Oscillator) — easy to confuse.
- **Logic MIDI:** audio inserts don't receive MIDI → for a MIDI-played carrier use the
  AU-MIDI-effect instrument-track variant (set the audio source track to **No Output**).
- **CPU:** 24 bands + 8 voices + ring-mod is heavy → print/freeze.
- **Voice Mix = 0** disables the Voice HPF/Voice Mod (no dry signal to process).
- **5 models have fixed (uneditable) curves** (Barkhausen, ES 2000, SN VSM-201, DF A-129,
  MM VF11) — pick another to tweak Bands/Q.
- **Mono instances** collapse Spread/Chorus to mono. **Ableton Lite:** subscription-gated; bounce
  heavy returns.

## 7. Captured sources & QC
- Transcripts: `vocodist-official-walkthrough` (deepest control-by-control; demos all 3 carrier
  modes), `vocodist-soundoracle-in-action` (producer session — guitar-as-sidechain-carrier).
- Links: `vocodist-official-manual` (48 pp, read page-by-page — verified controls/defaults/
  lineage), `vocodist-logic-carrier-routing` (the carrier-routing answer), `vocodist-reviews-and-lineage`.
  (Builds on the existing overview `links/antares-vocodist-review.md`.)

**QC:** controls/defaults/ranges verified directly off the rendered manual PDF (high confidence);
Path-A internal carrier verified (manual + both videos). The **Logic B/C sidechain/MIDI click-
paths are triangulated** (the manual punts to a JS-walled help page; built from the official
Auto-Tune-Pro-in-Logic article + the video's Pro-Tools demo) — confirm menu labels on the install.
The degrade-chain order and the exact machine-choir setting combos are **inferred** (manual
confirms each control's behavior, not these specific combos). No drone/doom artist credit.

## Sources
See §7. Originals: youtube.com (Antares official, SoundOracle), the Antares Vocodist manual PDF,
mixonline.com / Synth&Software / soundonsound.com. URLs on line 1 of each captured file.

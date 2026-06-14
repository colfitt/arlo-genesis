https://www.loopmasters.com/articles/2620-Drone-Sound-Design-8211-How-to-Design-a-Background-Drone-Sound
loopmasters.com · Loopmasters articles · "How to Design a Background Drone Sound"

A full stock-Logic drone-from-a-sample build, and a clean example of the "source → 3 pre-fader aux processors" structure that recurs across every good ambient Logic recipe.

## Source material
- A pitched-down sample (article uses a Native American flute from Logic's EXS24) + a "growl" sample from Freesound.
- Primary track: pitch the flute **down 2400 cents** (= 2 octaves) with the **Time and Pitch Machine** (Monophonic algorithm, Classic mode) → instant drone fundamental.

## Routing (the reusable template)
Primary drone track → **3 pre-fader sends**, roughly equal level to each aux:
- **Aux 1 — Tremolo**: rhythmic movement.
- **Aux 2 — Spectral Bin Shift** (3rd-party SoundMagic Spectral, free) OR stock spectral move: harmonic-texture manipulation by shifting frequency bins.
- **Aux 3 — Space Designer**: using the **edited growl sample as a custom IR** (resonant, vocal-ish reverb) — the "convolve any object" trick in practice.

Pre-fader sends mean you can pull the dry primary down independently and live on the processed auxes.

## Movement / automation
- **Clip Distortion** on the primary flute, output dropped ~**-20 dB** to add HF grit without volume jump.
- Automate three params for slow evolution: **Clip Drive** (distortion), **Tremolo Rate**, **Bins To Shift** (spectral).

## Rig fit
Swap the flute for a bowed banjo / VG-800 pad / sustained baritone note; swap the growl IR for a convolved rig sound. The pitch-down-2-octaves + 3-aux fan is the leanest stock-Logic drone template and pairs with the 4-bus reverb fan-out and the shimmer chain captured in this folder.

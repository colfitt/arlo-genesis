---
name: Lossy
brand: Goodhertz
category: software
subcategory: effect
formats: [vst3, au, aax]
host_in: [logic, ableton]
installed: true
install_path: /Library/Audio/Plug-Ins/Components/Ghz Lossy 3.component
version: latest
status: owned
tags: []
related: []
---

# Goodhertz Lossy

**Summary** — Creative codec/data-compression-artifact effect (MP3 spectral crush,
joint-stereo swirl, phase jitter, packet dropouts/stutter, dial-up/bad-stream
glitch). NOT a real codec — it *generates* the sound of heavily compressed audio in
a realtime, fully-automatable plugin. Installed build = **Ghz Lossy 3** (v3.13).

→ Full deep-dive: `research/Lossy-UsageGuide.md`

## Why I have it
The rig's **codec/digital-degrade axis** — the one degrade tool that does *digital*
damage the others can't: MP3 artifacts, streaming/packet glitch, the "recorded-wrong
/ sent over a bad connection / ripped from YouTube" sound. Complements the tape
(SketchCassette II), lo-fi suite (RC-20), saturation (Decapitator), bitcrush (NI
Bite), and the hardware (Generation Loss / Big Time) without overlapping any of them.

## Signature uses
- **Loss-Amount automation arc** — ride Loss Amount (or jump Loss Mode) clean →
  destroyed across a section (zipper-free automation); on a stem *or* the master bus.
- **Under-the-drone ambience crush** (Lorde "Shapeshifter" technique) — crush a
  texture/ambience layer so it sits dirty and far-off beneath a clean sustained wall.
- **Master-bus codec-crush** (Jane Remover *Frailty* technique) — Lossy on the 2-bus,
  low Mix + Auto Gain, for whole-mix grit & depth.
- **Verb = Pre** to Lossify the reverb tail → smeared underwater-cathedral drone wash.
- **Lo-fi banjo/vocal** — Standard + Phase Jitter, Gate Threshold up for jagged
  results; automate up only where the lead should sound recorded-wrong.
- **Telephone/streaming glitch** — tight steep filter band + Packet Loss/Repeat.

## Notes
- **Controls:** Loss Mode (Standard/Inverse/Phase Jitter/Packet Repeat/Packet
  Loss/+hybrids) · Loss Amount (the "bitrate" knob) · **Loss Speed** (slow = smear,
  fast = garbled) · Filter (low/high cut + slope) · built-in Verb (Pre/Post + Decay)
  · Master Mix (true global wet/dry). Advanced: Auto Gain, Gate Threshold, **Stereo
  Mode** (Joint Stereo = the MP3 swirl), Weighting (Perceptual/Flat).
- **Automation:** every param is zipper-free (Goodhertz house feature) — the
  bitrate/degrade arc is the headline move; rides cleanly on the master bus.
- **vs the free DIY route:** bouncing to a low-bitrate MP3 and re-importing is more
  "authentic" to one real bitrate but destructive/offline/un-automatable — Lossy is
  the realtime, recallable, push-past-any-real-encoder version.
- **Gotchas:** $79 special-interest character plugin ("love/hate"), limited factory
  preset bank, first-load wants a Goodhertz account login (offline challenge/response
  auth exists). Light on CPU. Budget alt = Aberrant Digitalis ($24); free = Lese
  Codec / MAIM.
- **No verified drone/doom/shoegaze artist credit** — relevance is by technique
  (Lorde ambience-crush + Jane Remover master-bus use, both verified) and the
  aesthetic. The Omar Apollo "Evergreen" claim is unverified — don't assert it.

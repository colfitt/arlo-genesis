https://www.youtube.com/watch?v=FbtY3wheI_Q
YouTube · "A Deep Dive to ECHOBOY JR by Soundtoys - Guide tutorial" · Feb 2023

Distilled from auto-captions (no spoken-word channel name given on-screen; a
chaptered single-creator deep-dive, "not a review"). Demoed on a mono Sylenth-style
synth through a vectorscope.

## Framing
- "This is the small version of the echo boy... I like the junior the most because
  it gives me different styles of delay with **minimal tweaking**." The full
  (non-Junior) "can do the same but you have crazy amount of properties you can
  adjust so you can spend more time fine-tuning." Jr = pick a flavor and move on.
- "This plugin is designed to be used as a **hardware unit** — that's the vibe."

## Core knobs
- **Echo Time** — tied to the bottom buttons: ms mode (up to ~2.4 s; double-click
  resets to default ~100 ms), or Note/Dot/Trip note-divisions synced to host. Same
  ms/note logic as full EchoBoy.
- **Mix** — dry↔wet; full wet = just delay (use for sends).
- **Feedback** — number/length of repeats; "tied to whatever style you're using —
  this knob reacts very differently depending on the style." Push it = "just gonna
  go crazy."

## Stereo Modes (3)
- **Normal** — centered, "somewhat narrow"; on a mono source it adds "a little bit
  of stiffness/width" but stays mostly mono. A stereo source in = stereo delay out.
  (You can't force full-mono collapse.)
- **Wide** — like Normal but **offsets L/R times slightly** (e.g. 100 ms L vs ~105 ms
  R — exact offset undocumented) → much wider image. The go-to for a fat stereo
  spread off a mono part.
- **Ping Pong** — successive repeats bounce L↔R.

## Glide
- ON = tape/analog behavior: change Echo Time while audio passes through and you get
  **pitch-shift sweeps** ("very cool pitch jumps" when switching note values; can
  modulate it as an SFX). OFF = retime with no pitch artifact — "much easier to dial
  in a delay time when feedback is up."

## The 7 styles (creator's ears, A/B'd against Studio Tape)
- **Studio Tape** — Ampex ATR-102 @ 15 IPS, "most-emulated tape machine in human
  history." Mild tape compression/saturation; "not too aggressive, not too dark, not
  too bright" — the neutral reference.
- **Plex** — Echoplex (EP-3). Brighter, thinner, more saturated than Studio Tape,
  with **pitch modulation on the tail**. "Right in your face" — repeats sit forward.
- **Space** — Roland RE-201 (real one in the lab is 4-head/multi-tap; Jr gives you
  **one tap**). Darker, smoother, warmer than Plex; modulation as it decays; the dark
  pick. Self-oscillates on high Feedback.
- **Cheap Tape** — Soundtoys original (worn consumer tape). With Studio Tape, the two
  "controlled/compressed" styles — longer, thinner decay, less colored.
- **Memory** — EHX Memory Man, bucket-brigade: repeats **get darker as they decay**
  and are subtly **chorused**. Key point: "even if you're aggressive, the dark decay
  **always stays in the background**" — so it's the style for leads where the dry
  must shine. (Contrast: Plex repeats are "in your face.")
- **Ambient** — emulates nothing; combines Distortion + Diffusion. "Like you put a
  reverb on the feedback loop of the delay" — long and lush, open. The reverb-ish one.
- **Transmitter** — CB-radio: distorted, resonant, **heavy on the mids**, "gritty."
  Creator's favorite; "not for everything" — shines on guitar/synth, dull on dull
  sources. Good for adding grit/character.

## Low Cut / High Cut
- 2-band tone shaping on the repeats; effect **depends on the style**. Use High Cut to
  push repeats back / tame an "in your face" style (e.g. Plex), Low Cut to clear the
  bottom so the delay blends. "Really useful to shape whatever you're doing and make
  a better blend."

## Input / Output + Saturation (the dirt path)
- **Input drives the echo circuit** like hitting a hardware preamp harder: low input =
  cleaner delays, more input = dirty delays; amount of dirt depends on the style. LEDs:
  green = mild, **yellow = ~6 dB below clip (not clipping)**, **red = clipping** (have it
  if you want it). Input/Output affect **only the echo, not the dry**.
- **Saturation** = quick tube/tape compression + emphasis + subtle distortion on the
  delay; "smooth and compressed," **reduces dynamics**. Tames a too-aggressive style:
  e.g. take the in-your-face Plex, High-Cut it, raise Saturation, drive Input, drop
  Output → a controlled, darker, compressed tone. Saturation effect varies by style
  (can be subtle).

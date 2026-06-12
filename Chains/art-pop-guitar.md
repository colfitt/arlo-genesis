---
type: chain
title: Art Pop Guitar Board
date: 2026-06-11
artists: [Peter Gabriel, Prince, The Police, mk.gee]
instrument: guitar
amp: ampless (Iridium)
gear:
  - TC Electronic Polytune 3
  - MXNHLT PORTA424
  - Chase Bliss Brothers AM
  - Chase Bliss Clean
  - Boss CE-2W
  - Chase Bliss Big Time
  - Chase Bliss MOOD MkII
  - Strymon Iridium
---

# Art Pop Guitar Board

Peter Gabriel atmospherics, Prince funk-drive dynamics, Andy Summers chorus/texture, mk.gee lo-fi DI philosophy. Ampless into Iridium — the whole character comes from the chain, not the amp.

## Signal Path

### 1. TC Electronic Polytune 3
Tuner + BonaFide buffer at the front. The buffer matters here — it keeps the signal clean through a long chain before the PORTA424 degrades it on purpose.

### 2. MXNHLT PORTA424
mk.gee's core move: Tascam Portastudio preamp as a tone-shaping stage. Push the gain for mild clipping and midrange bloom. This is your "anti-amp" — deliberately lo-fi, deliberately committed. Run at 9V for more grit or 18V for cleaner headroom with tape color.

### 3. Chase Bliss Brothers AM
Dual gain engine for Prince-style dynamics. Use [Boost mode](guide:Chase%20Bliss%20Brothers%20AM/boost-mode) into [Drive](guide:Chase%20Bliss%20Brothers%20AM/drive-mode) for funky edge-of-breakup rhythm parts. Stack both sides into distortion for Gabriel-era big guitar moments. The versatility here covers clean funk to searing lead without swapping pedals.

### 4. Chase Bliss Clean
Not a clean boost — a creative dynamics tool. Use the [compressor with swell](guide:Chase%20Bliss%20Clean/swell-mode) for Peter Gabriel-style gated pad textures. The two-stage compression locks down Prince funk rhythm playing. Dusty mode adds another flavor of overdrive after Brothers if you want to stack.

### 5. Boss CE-2W
The Andy Summers pedal. [CE-2 mode](guide:Boss%20CE-2W/ce-2-mode) for classic "Every Breath You Take" chorus. [CE-1 Vibrato mode](guide:Boss%20CE-2W/ce-1-vibrato-mode) for deeper, warbly pitch modulation on leads. This is the most direct reference to The Police in the chain.

### 6. Chase Bliss Big Time
80s rack-delay character — exactly the era for Gabriel and Police. The [motorized faders](guide:Chase%20Bliss%20Big%20Time/motorized-faders) let you morph between short slapback (Prince funk) and long atmospheric repeats (Gabriel). Mod range adds chorus-on-the-repeats for that "Intruder"/"Red Rain" vibe. Stereo out feeds MOOD.

### 7. Chase Bliss MOOD MkII
The mk.gee/texture wildcard at the end of the chain. [Micro-looper side](guide:Chase%20Bliss%20MOOD%20MkII/micro-looper) captures and mangles what Big Time feeds it — granular stutters, reversed fragments, tape-stretch. [Wet channel reverb/slip](guide:Chase%20Bliss%20MOOD%20MkII/wet-channel-slip) adds otherworldly ambience. This is where "guitar" stops sounding like guitar. Clock knob syncs both sides for rhythmic glitch.

### 8. Strymon Iridium
Amp sim at the end — [Round mode](guide:Strymon%20Iridium/round-amp) (Fender Deluxe) for clean/funk parts, [Chime mode](guide:Strymon%20Iridium/chime-amp) (Vox AC30) for jangly Police tones. The cab IR does the "speaker" work so MOOD's weirdness stays intact through a believable speaker response. Stereo out to interface.

## Routing Notes

- Entire chain runs mono until Big Time, then stereo through MOOD and Iridium
- PORTA424 is mono-only — place it early where mono is fine
- Big Time draws 1A — needs isolated power supply
- Brothers, Clean, Big Time, and MOOD all accept MIDI — a single MIDI controller (or the Novation 61SL MkIII) can preset-switch the whole middle of the board

## The Vibe

- **Prince funk rhythm**: Brothers boost side, Clean comp tight, CE-2W off, Big Time short slapback
- **Police shimmer**: Brothers clean, CE-2W on, Big Time medium delay with mod
- **Gabriel atmosphere**: Clean swell mode, Big Time long delay, MOOD slip reverb
- **mk.gee mangled**: PORTA424 pushed hard, MOOD micro-looper engaged, everything committed

## Sources

- `gear/MXNHLT PORTA424/GearProfile.md`
- `gear/Chase Bliss Brothers AM/GearProfile.md`
- `gear/Chase Bliss Clean/GearProfile.md`
- `gear/Boss CE-2W/GearProfile.md`
- `gear/Chase Bliss Big Time/GearProfile.md`
- `gear/Chase Bliss MOOD MkII/GearProfile.md`
- `gear/Strymon Iridium/GearProfile.md`
- `gear/TC Electronic Polytune 3/GearProfile.md`
- `arlo/corpus/artists/mk-gee-di-direct-philosophy.md`

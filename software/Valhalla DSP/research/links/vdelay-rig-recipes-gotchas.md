https://valhalladsp.com/shop/delay/valhalladelay/
(synthesis from the official posts + Tape Op + SOS + this rig's existing guides)

Rig-specific recipes and gotchas for ValhallaDelay. Settings synthesized from official
control ranges + the designer interview + the video walkthroughs — not one verbatim
factory patch. SYNTHESIS where inferred for this rig.

## Status (lead banner)
**NOT currently installed.** $50 paid Valhalla plugin (AU/VST3/AAX). Rig has VintageVerb +
Room installed; free **Supermassive** covers infinite ambient walls at $0. Buy Delay for
the *character delay* the box lacks: authentic tape/BBD/Digital, tempo sync, Ghost drift,
Pitch-Duck adaptive shimmer (see vdelay-vs-supermassive-ambient.md).

## Copyable starting points (SYNTHESIS)
- **Tape-ghost ambient WALL** — Mode **Ghost** · Style Single · long delay (or sync 1/4) ·
  **DIFF Amount 91% + DIFF Size large** (delay → reverb wash) · Feedback 40–70% · small
  **FREQ Shift/Detune** for metallic drift · **EQ Low-cut ~150 Hz, EQ High-cut ~3–4 kHz**
  in the feedback so the wall darkens as it recirculates · Mix 100% (return).
- **Octave shimmer-DELAY** — Mode **Pitch** · **PITCH Shift +12** · Feedback 0.5+ (spirals
  up) · Diffusion high for the wash · or use **PitchDuck** + Ducking so it stays under the
  played source. −12 = spiraling down/doom.
- **Dirty self-oscillating tape drone** — Mode **Tape** · ERA Past · **Feedback ~100–130%**
  (controlled self-oscillation) · ride the DELAY time to "play" the howl (SOS) · MOD
  Wow/Flutter up + Age up for wear.
- **Golden-ratio pseudo-reverb** — Style **Ratio**, **RATIO 61.8%** · higher feedback ·
  Diffusion up = a delay-built reverb with no obvious rhythm.
- **Swelling multi-head wall** — Style **Quad**, **SWELL** mode · 3–4 taps · rising
  feedback = a wall that builds (RE-201 multi-head bloom).
- **Frippertronics loop** — long delay (up to **20 s**) · high feedback · Tape mode · let
  layers stack into an evolving tape-loop drone.
- **Lo-fi BBD/Digital** — Mode BBD or Digital · Age ~50% (≈12-bit on Digital) · short delay
  for grainy slap, long for crunchy wash.

## Rig recipes (banjo / baritone / synth / drones)
- **On banjo/baritone**: PitchDuck (+12 or +7) on a send — the shimmer-delay wall ducks
  under your picking and blooms in the gaps; keeps the attack legible. Or Tape mode synced
  dotted-1/8 for a dub-echo under baritone.
- **Into/after the degrade chain**: ValhallaDelay IS a degrader (Tape Age, BBD, Digital
  bit-crush) — put it as the tape/echo stage. Or run a Ghost/Diffusion wash 100% wet and
  **saturate the return** (Decapitator / SketchCassette II / RC-20, Low-cut first) for the
  doom/shoegaze wall — same return-saturation move as the VintageVerb/Room guides.
- **Delay AFTER reverb vs before**: ValhallaDelay → (Room/VintageVerb) keeps repeats
  legible then washes them; (Room/VintageVerb) → ValhallaDelay re-throws the reverb tail
  into a bigger drifting wall (less legible, more wall). The rig's documented Tycho-style
  "delay after reverb" wall applies — and Delay's own Diffusion can be the reverb, so one
  instance can do reverb→delay internally.
- **vs the rig's hardware**: the tape/echo pedals + Big Sky/Microcosm are the played-bed
  capture tools; ValhallaDelay is the recallable, automatable, tempo-synced, stack-12-
  instances in-the-box version (the Tape Op interview: designer runs 10–12+ aux instances).

## Gotchas
- **Feedback runaway / self-oscillation**: Feedback "begins to self-oscillate around 100%"
  and goes to **200%** — a howling drone is a feature, but watch output level; automate
  Feedback down or limit the return. Use **DIFF Amount 91% to get the reverb wash WITHOUT
  cranking feedback** (safer than runaway).
- **No tap-tempo / click-free tempo change** — the designer's own named limitation; you
  can't ride delay time live without artifacts. Automate Sync changes at bar lines.
- **Modes gate controls** — Ducking, Wow/Flutter, FREQ Shift etc. only exist in certain
  modes; you can't add Ducking to a mode that lacks it. Pick the mode for its control set.
- **Logic (AU-only host)**: Delay is AU-native, fine in Logic. As with the documented Room
  AU pan-vs-parameter quirk, run **stereo source track + stereo aux** for a mono source on
  a 100%-wet send so panning doesn't scale the wet. ⚠️ INFERRED from the Room AU bug.
- **Ableton Live 12 LITE**: AU/VST hosting works in Lite; the constraint is Lite's device/
  track count, not plugin support — fine for a few instances, watch the cap if you stack
  the designer's 10–12. ⚠️ INFERRED.
- **CPU**: near-zero per instance (designed to run 10+ auxes).

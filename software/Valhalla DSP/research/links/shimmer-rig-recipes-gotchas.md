https://valhalladsp.com/shop/reverb/valhalla-shimmer/
(synthesis from the official posts + KVR threads + this rig's existing VintageVerb/Room guides)

Rig-specific recipes and gotchas for ValhallaShimmer. Settings synthesized from the
official control ranges + the two video walkthroughs — not one verbatim factory patch.
Marked SYNTHESIS where inferred for this rig.

## Status (lead banner)
**NOT currently installed.** $50 paid Valhalla plugin (AU/VST3/AAX). The rig has
VintageVerb + Room installed; the FREE **Supermassive** (and free CloudSeed) cover most
shimmer-wall needs at $0 — see shimmer-vs-supermassive-best-for-ambient.md. Buy Shimmer
only if you want shimmer as a daily, low-CPU, recallable workhorse with the cleaner
Reverse pitch modes and the cascade-chord trick.

## Copyable starting points (SYNTHESIS)
- **Infinite octave shimmer wall** — Big/Medium Stereo · Single (or SingleReverse for
  glassy) · **Shift +12** · **Feedback 0.5–0.7** · **Diffusion ~0.9** · Size large · Color
  **Dark** · Mod low · Mix 100% (return). Push Feedback toward 0.8+ for near-frozen.
- **Tasteful evolving ambient pad** — same but **Feedback <0.5** · **Diffusion ~0.6**
  (slow swell-in) · **Mix 20–30% on a send** so the source stays legible (Thales).
- **Dark/haunted descending wall** — **Shift −12** · Dark · Feedback 0.5+ · the wall
  sinks instead of rising = doom-leaning. (Try −5/−7 for a less obvious darkening.)
- **Symphonic shimmer chord** — **cascade 3–4 instances** in series, each a different
  interval (±12, ±7, ±5) — the designer's own trick; builds an octave+fifth+fourth stack
  one instance can't make. Low CPU makes this cheap.
- **Reverse-reverb swell** — Diffusion ~0.55–0.62 (slow fade-in) · Bypass pitch for a
  clean swell, or Single +12 for a climbing swell.

## Rig recipes (banjo / baritone / synth / drones)
- **On banjo/baritone**: send at 20–30%, Diffusion ~0.6 so the picked attack stays clear
  and the octave wall blooms behind it. SingleReverse for a smooth glass pad over fingered
  baritone drones.
- **Into/after the degrade chain**: run Shimmer 100% wet on an aux, then **saturate the
  return** with Decapitator / SketchCassette II / RC-20 (Low Cut FIRST) = the saturated
  shoegaze/doom shimmer wall — exactly the move the VintageVerb/Room guides use, applied
  to the pitched wall. Or place a degrader BEFORE the send so the climbing octaves inherit
  baked-in grit.
- **Shimmer → Delay (or EchoBoy) after**: re-throw the climbing wall with a long delay for
  an even bigger, drifting wall (delay-after-reverb destroys legibility on purpose).
- **vs the rig's pitched-reverb hardware**: the **H90/Blackhole** is the hardware shimmer/
  pitched-reverb-as-instrument; Shimmer is the recallable, near-zero-CPU, stack-many in-
  the-box version. Capture a played bed through H90/Big Sky, then add recallable Shimmer
  color in the box.

## Gotchas
- **Feedback runaway**: Feedback ≥ ~0.7 with high Diffusion can build toward self-
  oscillation / runaway level — automate it down, or gate/limit the return. Many users
  gate or rhythm-gate the wet (KVR).
- **Aliasing on +12 climbs**: the pitch shifter aliases on bright content — use **Color
  Dark** + High Cut to tame it (that's literally why Dark exists).
- **Mono in Logic (AU-only host)**: Shimmer's Mono mode is mono-in/stereo-out. As with the
  documented Room AU pan-vs-parameter quirk, run the **source track AND the aux as STEREO**
  (hard-center a mono banjo on a stereo track) so panning doesn't scale the wet. ⚠️ INFERRED
  from the Room AU bug — not separately confirmed for Shimmer.
- **Ableton Live 12 LITE**: third-party AU/VST plugins DO load in Lite (Lite only limits
  scenes/tracks/devices count, not plugin hosting) — Shimmer works, but watch the device
  cap when cascading many instances. ⚠️ INFERRED.
- **NOT a realistic reverb** — Costello says so; don't reach for it when you need a
  believable room (that's Room).
- **CPU**: near-zero per instance (designed for cascading); the cap is Live Lite's device
  count, not CPU.
